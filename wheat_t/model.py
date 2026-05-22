"""SOLVEG-II  Main Model Driver (§4)

Orchestrates time-step loop:
  atmosphere → LAI dynamic → canopy → organs → soil → microenvironment → DVS → output.

All framework concepts from FRAMEWORK_FINAL.md integrated:
  - LAI dynamic from DVS (§20.2)
  - Aerodynamic conductance from wind (§20.3)
  - Soil evaporation from met (§20.1)
  - Microenvironment re-evaporation (§19.3)
  - Carbon turnover (§6.7)
  - Night gs from crop param (§3.3)
  - VPD reference from config (§3.4)
  - Conservation check (§15.8)
  - WeatherSeries support (§19.1)
"""

import math
from . import config as cfg
from .atmosphere import (atmosphere_state, soil_evaporation,
                         aero_conductance, lai_dynamic, WeatherSeries)
from .canopy import CanopyModel, transpiration_rate
from .organs import PlantOrgans
from .soil import SoilModel
from .plant_water import VascularWater, PlantWater


class SolvegModel:
    """SOLVEG-II plant OBT accumulation prediction model."""

    def __init__(self, params=None):
        if params is None:
            params = {}

        p = dict(cfg.DIABATE_SCENARIO)
        p.update(params)

        # ─── Scenario ───
        self.airHTO = p['airHTO']
        self.expH = p['expH']
        self.expDelay = p.get('expDelay', 0.0)
        self.startH = p['startH']

        # DAF dynamic exposure: exposure starts when DVS reaches threshold
        # If exp_start_DVS is set, exposure is DVS-triggered (ignores expDelay).
        # If not set, falls back to time-based expDelay (backward compatible).
        self.exp_start_DVS = p.get('exp_start_DVS', None)
        self._exp_started = False   # tracks whether DVS-triggered exposure has begun
        self._exp_t_start = None    # simulation time when DVS-triggered exposure started
        self.T_mean = p['Tair']
        self.RH = p['RH']
        self.wind = p['wind']
        self.LAI = p['LAI']
        self.height = p.get('height', cfg.CANOPY_HEIGHT)
        self.simH = p['simH']
        self.lat = p['lat']
        self.doy = p['doy']
        self.nLayers = p['nLayers']
        self.dt = p['dt']
        self.startGDD = p['startGDD']
        self.soil_covered = p['soil_covered']

        # Soil-specific params
        self.soil_HTO_input = p.get('soil_HTO_input', 0.0)
        self.irrigation_rate = p.get('irrigation_rate', 0.0) / 86400.0  # m/day → m/s

        # Weather mode: constant (default) or WeatherSeries
        self.weather_fn = p.get('weather_fn', None)

        # Crop parameters
        crop_name = p.get('crop', 'wheat')
        self.crop = dict(cfg.CROPS.get(crop_name, cfg.CROP_PARAMS_WHEAT))

        # Derived
        self.steps_per_hour = int(3600 / self.dt)
        self.total_hours = int(self.simH)
        # GRAIN_FILL_H: scenario override > crop params > default
        self.grain_fill_h = p.get('GRAIN_FILL_H', self.crop.get('GRAIN_FILL_H', 720.0))

        # State
        self.DVS = self._gdd_to_dvs(self.startGDD)
        self._t_anthesis = None        # real hours when anthesis occurred
        self._gdd_anthesis = None      # GDD when anthesis occurred
        self._had_atmo_exposure = False  # Track if any atmospheric exposure occurred
        self._grain_fill_triggered = False  # grain fill trigger flag

        # Modules
        self.canopy = CanopyModel(
            self.LAI, self.nLayers, self.height, self.wind, self.crop)
        self.organs = PlantOrgans(leaf_C_total=0.30, crop_name=crop_name,
                                   grain_fill_max_h=self.grain_fill_h)
        self.soil = SoilModel(
            soil_type=p.get('soilType', 'loam'),
            theta0=p.get('theta0', 0.30))
        self.soil.covered = self.soil_covered

        # Water transport modules (§4, §5)
        self.vascular = VascularWater(tau_vascular=15.0)
        self.plant_water = PlantWater(tau_root=10.0)

        # Carbon turnover: enable for open soil scenarios
        self.use_turnover = p.get('use_carbon_turnover',
                                   not self.soil_covered)

        # Microenvironment state
        self.C_air_local = 0.0
        self.soil_root_C = 0.0
        self._E_soil = 0.0
        self._g_aero = cfg.G_AERO

        # Carbon conservation tracking
        self._prev_C_total = None
        self._conservation_warnings = 0

        # Output storage
        self.results = {
            'time_h': [],
            'hour_of_day': [],
            'Tair': [],
            'PAR': [],
            'C_air': [],
            'C_air_local': [],
            'total_A': [],
            'DVS': [],
            'LAI': [],
            'mean_TFWT': [],
            'mean_OBT': [],
            'peak_TFWT': 0.0,
            'grain_OBT': [],
            'grain_W': [],
            'E_soil': [],
            'g_aero': [],
            'A_total': [],
        }
        # Fine-grained time series for short-term validation (every step)
        self._ts = {
            't_h': [], 'leaf_tfwt': [], 'leaf_obt_str': [],
            'leaf_obt_exch': [], 'ear_obt': [], 'ear_obt_str': [],
            'grain_obt': [], 'stem_obt': [],
            'a_n_top': [], 'canopy_mean_obt': [],
        }

    # ─────────────────────────────────────────────────────────────────
    # DVS mapping (GDD → DVS)
    # ─────────────────────────────────────────────────────────────────

    def _gdd_to_dvs(self, gdd):
        """GDD → DVS。DVS 允许 > 2.0（超成熟），分配表在 2.0 截断。"""
        gdd_anthesis = self.crop.get('GDD_mature', 2500.0) * 0.5
        gdd_mature = self.crop.get('GDD_mature', 2500.0)
        if gdd <= 0:
            return 0.0
        elif gdd < gdd_anthesis:
            return gdd / gdd_anthesis
        else:
            return 1.0 + (gdd - gdd_anthesis) / (gdd_mature - gdd_anthesis)
            # 注意：不截断到 2.0！DVS > 2.0 表示超成熟期
            # 分配表插值自动用最后一行（DVS≥2.0）

    # ─────────────────────────────────────────────────────────────────
    # Carbon turnover (§6.7) — OBT dilution via structural pool loss
    # ─────────────────────────────────────────────────────────────────

    def _step_carbon_turnover(self, dt):
        """Leaf and organ carbon turnover — dilutes OBT concentration.
        Uses framework §10.3 turnover rates (not the leaf-specific CARBON_TURNOVER_DAY).
        """
        dt_h = dt / 3600.0

        # Leaf turnover (§10.3: 0.001/h = 29-day half-life)
        k_leaf = 0.001 * dt_h
        for i in range(self.canopy.N):
            if self.canopy.W_str[i] > 1e-20:
                dW = min(k_leaf * self.canopy.W_str[i], self.canopy.W_str[i] * 0.1)
                if dW > 1e-20:
                    self.canopy.OBT_str[i] *= (1.0 - dW / self.canopy.W_str[i])
                    self.canopy.W_str[i] -= dW

        # Stem turnover (0.0002/h = 144-day half-life)
        k_stem = 0.0002 * dt_h
        if self.organs.stem.W_str > 1e-20:
            dW = min(k_stem * self.organs.stem.W_str, self.organs.stem.W_str * 0.1)
            if dW > 1e-20:
                self.organs.stem.OBT_str *= (1.0 - dW / self.organs.stem.W_str)
                self.organs.stem.W_str -= dW

        # Root turnover (0.0005/h = 58-day half-life)
        k_root = 0.0005 * dt_h
        if self.organs.root.W_str > 1e-20:
            dW = min(k_root * self.organs.root.W_str, self.organs.root.W_str * 0.1)
            if dW > 1e-20:
                self.organs.root.OBT_str *= (1.0 - dW / self.organs.root.W_str)
                self.organs.root.W_str -= dW

    # ─────────────────────────────────────────────────────────────────
    # Conservation check (§15.8)
    # ─────────────────────────────────────────────────────────────────

    def _check_conservation(self, step_i):
        """Warn if carbon drops unexpectedly (two-pool)."""
        C_now = sum(
            self.canopy.W_suc[i] + self.canopy.W_str[i]
            for i in range(self.canopy.N)
        ) + self.organs.root.W_total + self.organs.stem.W_total + \
            self.organs.ear.W_total + self.organs.grain.W_total

        if self._prev_C_total is not None and self._prev_C_total > 1e-10:
            rel = (C_now - self._prev_C_total) / self._prev_C_total
            if rel < -0.05 and self.DVS < 1.5:
                self._conservation_warnings += 1
                if self._conservation_warnings <= 5:
                    print(f"  WARNING step {step_i}: carbon dropped {rel*100:.1f}% "
                          f"(DVS={self.DVS:.2f})")
        self._prev_C_total = C_now

    # ─────────────────────────────────────────────────────────────────
    # Single time step (§4.1) — full framework
    # ─────────────────────────────────────────────────────────────────

    def step(self, t, dt):
        """Advance model by one time step.

        Args:
            t: elapsed time from simulation start [h]
            dt: time step [s]

        Returns:
            dict of instantaneous diagnostics
        """
        hour_of_day = (self.startH + t) % 24.0

        # ════════ Exposure timing ════════
        # Mode 1: DVS-triggered (exp_start_DVS set) — exposure starts when DVS >= threshold
        # Mode 2: Time-based (default) — exposure at expDelay..expDelay+expH
        TAU_CHAMBER = 7.0  # h — exposure chamber ventilation time constant

        if self.exp_start_DVS is not None:
            # DVS-triggered mode
            if not self._exp_started and self.DVS >= self.exp_start_DVS:
                self._exp_started = True
                self._exp_t_start = t

            if self._exp_started:
                t_exp_end = self._exp_t_start + self.expH
                is_exposed = (t < t_exp_end)
                if is_exposed:
                    C_ambient = self.airHTO
                elif t < t_exp_end + TAU_CHAMBER * 5:
                    C_ambient = self.airHTO * math.exp(-(t - t_exp_end) / TAU_CHAMBER)
                else:
                    C_ambient = 0.0
            else:
                is_exposed = False
                C_ambient = 0.0
        else:
            # Time-based mode (backward compatible)
            is_exposed = (self.expDelay <= t < self.expDelay + self.expH)
            if is_exposed:
                C_ambient = self.airHTO
            elif t < self.expDelay + self.expH + TAU_CHAMBER * 5:
                C_ambient = self.airHTO * math.exp(-(t - self.expDelay - self.expH) / TAU_CHAMBER)
            else:
                C_ambient = 0.0

        self._is_exposed = is_exposed  # store for organs/canopy access

        # Record fill progress at exposure for grain receptivity
        if is_exposed and not getattr(self, '_exposure_recorded', False):
            fp = min(1.0, self.organs._grain_fill_hours / max(self.organs._grain_fill_max_h, 1.0))
            self.organs._fill_progress_at_exposure = fp
            # Compute snapshot receptivity from fill_progress
            self.organs._receptivity_at_exposure = self.organs.compute_snapshot_receptivity(fp)
            # Record delay from anthesis to exposure (hours)
            if self._t_anthesis is not None:
                self.organs._exp_delay_from_anthesis = max(0.0, t - self._t_anthesis) / 3600.0
            else:
                self.organs._exp_delay_from_anthesis = 0.0
            self._exposure_recorded = True

        # Soil HTO sink — open soil absorbs atmospheric HTO during exposure (dry deposition).
        # PE-covered soil has no exchange. Diabaté: soil/PE ≈ 0.67.
        C_effective = C_ambient
        if not self.soil_covered and is_exposed and C_ambient > 0:
            C_effective = C_ambient * (1.0 - cfg.SOIL_HTO_SINK_FRAC)
        self.organs._expH = self.expH  # pass expH for ear dose correction

        # ════════ 1. Atmospheric state ════════
        if self.weather_fn is not None:
            atm = self.weather_fn(t)
        else:
            atm = atmosphere_state(hour_of_day, self.T_mean, self.RH,
                                   self.wind, self.lat, self.doy)
        T_air = atm['Tair']
        ea = atm['ea']
        PAR = atm['PAR']
        sin_beta = atm['sinBeta']
        is_night = atm['isNight']

        # ════════ 2. LAI (§20.2) ════════
        # PE film: constant LAI (laboratory canopy, Diabaté protocol)
        # Open soil + emergence start (DVS₀≈0): lai_dynamic from DVS
        # Open soil + late start (DVS₀≥0.8): keep initial LAI (crop already established)
        if not self.soil_covered and self.startGDD < self.crop.get('GDD_mature', 2500.0) * 0.4:
            self.LAI = lai_dynamic(self.DVS)
            self.canopy.LAI = self.LAI
            for i in range(self.canopy.N):
                self.canopy.dLAI[i] = self.LAI / self.canopy.N

        # ════════ 3. Aerodynamic conductance (§20.3) ════════
        self._g_aero = aero_conductance(atm['wind'], self.height)

        # ════════ 4. Soil evaporation (§20.1) ════════
        if not self.soil_covered and self.soil is not None:
            self._E_soil = soil_evaporation(
                T_air, ea, atm['wind'],
                theta=self.soil.theta[0],
                theta_sat=self.soil.theta_S,
                theta_R=self.soil.theta_R,
                covered=False)
        else:
            self._E_soil = 0.0

        # ════════ 5. Canopy wind profile ════════
        self.canopy.layer_wind(atm['wind'])

        # ════════ 6. Radiation allocation ════════
        PAR_top = PAR
        PARsl, PARsh = self.canopy.layer_radiation(PAR_top, sin_beta)

        # ════════ 7. Layer-wise photosynthesis + stomata ════════
        total_A, mean_gs, total_transp = self.canopy.step_photosynthesis(
            T_air, ea, is_night)

        # ════════ 7b. PlantWater pre-step (soil → xylem) ════════
        # Must run BEFORE canopy loop so C_xylem is available for leaf water.
        # soil_root_C was set at end of previous step.
        self.plant_water.step(self.soil_root_C, dt, uptake_eff=cfg.ROOT_UPTAKE_EFF)
        C_xylem = self.plant_water.C_xylem if (
            self.plant_water.C_xylem > 1e-10 and not self.soil_covered
        ) else 0.0

        # ════════ 8. Single-chamber water + carbon flow + OBT (per layer) ════════
        for i in range(self.canopy.N):
            dLAI = self.canopy.dLAI[i]
            if dLAI < 1e-6:
                continue

            gs = self.canopy.gs[i]
            if is_night:
                gs = self.crop.get('g0_night', 0.0001)

            VPD = max(0.01, atm['es'] - ea)
            T_vol = transpiration_rate(
                gs, wind=self.canopy.wind_layer[i],
                VPD=VPD, is_night=is_night)

            # Two-chamber leaf water (fast room + slow room)
            self.canopy.step_two_chamber_water(i, self.C_air_local, dt, T_vol,
                                               C_xylem=C_xylem)

            # Carbon flow + OBT formation (uses TFWT directly)
            A_leaf = self.canopy.A[i]
            self.canopy.step_carbon_flow(i, dt, is_night, A_leaf,
                                         C_air_local=self.C_air_local,
                                         is_exposed=self._is_exposed)

        # ════════ 9. Carbon turnover — DISABLED ════════
        # Replaced by protein turnover in canopy.py and organs.py (K_PROT_TURN).
        # W_str stays constant; OBT diluted by protein turnover, not structural carbon loss.
        # self._step_carbon_turnover(dt)

        # ════════ 9b. Vascular + C_stem_water (§4.2, §5) ════════
        # PlantWater already stepped in 7b (before canopy loop).
        C_slow_mean = self.canopy.get_mean_C_slow()
        self.vascular.step(C_slow_mean, dt)        # tracked for output

        # C_stem_water: two pathways feed the same stem water pool.
        # - Atmospheric: C_slow from canopy two-chamber model (dominant for short pulses)
        # - Soil: C_xylem from root uptake (important for chronic soil irrigation)
        # Use MAX to avoid double-counting in chronic scenarios where both ≈ C_air.
        C_stem_water = max(C_slow_mean, C_xylem) if C_xylem > 0 else C_slow_mean

        # ════════ 10. Organ allocation ════════
        dW_canopy = total_A * 1e-6 * (12.0 / 1000.0) * dt  # kg C/m²
        S_leaf_suc = self.canopy.get_weighted_suc_obt()

        # Organ TFWT transport chain (§3.14)
        self.organs.update_organ_TFWT(C_effective, C_stem_water, dt, self.DVS, self.canopy.mean_tfwt(),
                                       self.plant_water.C_xylem)

        # Carbon allocation + organ metabolism
        canopy_mean_obt = self.canopy.mean_obt()
        recycled_Bq = self.organs.step_allocate(dW_canopy, S_leaf_suc, self.DVS,
                                  T_air, dt, is_night, C_slow_mean,
                                  canopy_mean_TFWT=self.canopy.mean_tfwt(),
                                  is_exposed=self._is_exposed,
                                  obt_signal=canopy_mean_obt)

        # Stem reallocation
        self.organs.step_stem_reallocation(dt, self.DVS)

        # Ear reallocation (ear→grain OBT transfer)
        self.organs.step_ear_reallocation(dt, self.DVS)

        # ════════ Canopy→stem/ear OBT redistribution ════════
        # Physical: canopy protein turnover releases HTO → boundary layer → stem/ear surface absorption.
        # This is the main source of stem/ear OBT (Diabaté: stem=65, ear=45 at t=0h).
        obt_released = self.canopy.total_obt_released()  # [Bq/m²] released this step
        if obt_released > 1e-20:
            dt_h = dt / 3600.0
            # Stem: absorb released OHT from boundary layer
            dOBT_stem = cfg.CANOPY_OBT_TO_STEM * obt_released * dt_h
            if dOBT_stem > 1e-20:
                self.organs.stem.OBT_str += dOBT_stem / max(self.organs.stem.W_str, 1e-20)
            # Ear: absorb released OHT from boundary layer
            dOBT_ear = cfg.CANOPY_OBT_TO_EAR * obt_released * dt_h
            if dOBT_ear > 1e-20:
                self.organs.ear.OBT_str += dOBT_ear / max(self.organs.ear.W_str, 1e-20)

        # Grain fill OBT: leaf OBT_str remobilization (no dose correction)
        # Calculate leaf mean OBT_str (LAI-weighted)
        total_lai = sum(self.canopy.dLAI[i] for i in range(self.canopy.N))
        if total_lai > 1e-6:
            leaf_mean_OBT_str = sum(
                self.canopy.OBT_str[i] * self.canopy.W_str[i] * self.canopy.dLAI[i]
                for i in range(self.canopy.N)
            ) / sum(
                self.canopy.W_str[i] * self.canopy.dLAI[i]
                for i in range(self.canopy.N)
                if self.canopy.dLAI[i] > 1e-6
            ) if sum(self.canopy.W_str[i] * self.canopy.dLAI[i]
                     for i in range(self.canopy.N)) > 1e-20 else 0.0
            leaf_mean_OBT_exch = sum(
                self.canopy.OBT_exch[i] * self.canopy.dLAI[i]
                for i in range(self.canopy.N)
            ) / max(total_lai, 1e-6)
        else:
            leaf_mean_OBT_str = 0.0
            leaf_mean_OBT_exch = 0.0
        # no dose_factor — removed DOSE_POWER_GRAIN
        self.organs.step_grain_obt(dt, self.DVS, T_air,
                                   self.organs._grain_TFWT, is_night,
                                   leaf_mean_OBT_str=leaf_mean_OBT_str,
                                   leaf_mean_OBT_exch=leaf_mean_OBT_exch)

        # SEL_PHLOEM 路径移除 — OBT通过senescence+ear realloc路径转移
        # 旧的phloem loading路径与senescence重复，且没有receptivity调制

        # Leaf carbon reallocation (S_leaf=0, OBT不通过碳再分配转移)
        # if ENABLE_SENESCENCE_OBT_TRANSFER=False, zero S_leaf to prevent OBT transfer
        dW_realloc, S_realloc = self.canopy.shrink_leaf_realloc(dt, self.DVS)
        if dW_realloc > 1e-20:
            S_realloc_obt = S_realloc if cfg.ENABLE_SENESCENCE_OBT_TRANSFER else 0.0
            self.organs.receive_leaf_realloc(dW_realloc, S_realloc_obt, is_night,
                                             expH=self.expH)

        # Ear photosynthesis (DVS >= 0.8)
        if self.DVS >= 0.8 and not is_night:
            self.organs.step_ear_photosynthesis(PAR_top, T_air, dt)

        # ════════ 11. Soil step (§8) ════════
        evap_flux = 0.0
        if not self.soil_covered and self.soil is not None:
            evap_flux, root_C = self.soil.step(
                dt, C_ambient, self._E_soil, total_transp,
                C_irrigation=self.soil_HTO_input,
                irrig_rate=self.irrigation_rate)
            self.soil_root_C = root_C
        else:
            self.soil_root_C = 0.0

        # ════════ 12. Microenvironment C_air_local (§19.3) ════════
        self.C_air_local = C_effective + evap_flux / max(self._g_aero, 0.01)

        # ════════ 13. Leaf senescence ════════
        if self.DVS >= 1.0 and self._t_anthesis is None:
            self._t_anthesis = t
            self._gdd_anthesis = self.startGDD  # current GDD at anthesis
            # Trigger grain fill at anthesis (DVS-based)
            if not self._grain_fill_triggered:
                self.organs.trigger_grain_fill()
                self._grain_fill_triggered = True
            # Set exposure delay for grain receptivity bell curve
            if self._exp_t_start is not None:
                self.organs._exposure_delay_h = max(0.0, t - self._exp_t_start)
            else:
                self.organs._exposure_delay_h = max(0.0, t - self.expDelay)

        # Grain fill weight reverted to 1.0 — grain_TFWT pathway handles DAF dependence
        # pass exp_delay_h for DAF decay correction in senescence transfer
        if self._exp_t_start is not None and self._t_anthesis is not None:
            exp_delay_h = max(0.0, self._exp_t_start - self._t_anthesis)
        else:
            exp_delay_h = max(0.0, self.expDelay - (self._t_anthesis or 0.0))
        dW_sen, S_sen, dW_lit = self.canopy.step_senescence(
            dt, t, self._t_anthesis, self.grain_fill_h, exp_delay_h=exp_delay_h)
        if dW_sen > 1e-20:
            S_sen_obt = S_sen if cfg.ENABLE_SENESCENCE_OBT_TRANSFER else 0.0
            self.organs.receive_leaf_realloc(dW_sen, S_sen_obt, is_night,
                                             expH=self.expH)

        # ════════ 14. DVS update (封顶在 DVS_MATURE) ════════
        GDD_rate = max(0.0, T_air - self.crop.get('Tbase', 0.0)) * dt / 3600.0
        self.startGDD += GDD_rate
        self.DVS = min(self._gdd_to_dvs(self.startGDD), cfg.DVS_MATURE)

        # ════════ 15. Conservation check (periodic) ════════
        if self.steps_per_hour > 0:
            self._check_conservation(int(t * 3600 / dt))

        # ════════ Diagnostics ════════
        return {
            't': t,
            'hour': hour_of_day,
            'Tair': T_air,
            'PAR': PAR,
            'C_air': C_ambient,
            'C_air_local': self.C_air_local,
            'total_A': total_A,
            'DVS': self.DVS,
            'LAI': self.LAI,
            'mean_TFWT': self.canopy.mean_tfwt(),
            'mean_OBT': self.canopy.mean_obt(),
            'E_soil': self._E_soil,
            'g_aero': self._g_aero,
        }

    # ─────────────────────────────────────────────────────────────────
    # Full simulation run
    # ─────────────────────────────────────────────────────────────────

    def run(self, progress_every=100):
        """Run the full simulation.

        Args:
            progress_every: print progress every N hours (0 = silent)

        Returns:
            dict with full time series and harvest results
        """
        n_steps = self.total_hours * self.steps_per_hour
        dt = self.dt

        if progress_every > 0:
            soil_mode = "PE" if self.soil_covered else "open"
            print(f"SOLVEG-II starting: {self.total_hours}h, dt={dt}s, "
                  f"{n_steps} steps, DVS₀={self.DVS:.2f}, soil={soil_mode}")

        for step_i in range(n_steps):
            t = step_i * dt / 3600.0
            diag = self.step(t, dt)

            # Capture harvest snapshot when grain fill ends
            if not self.organs._grain_filling_active and not getattr(self, '_harvest_captured', False):
                self._harvest_snapshot = {
                    'leaf_OBT_Bq_g': self.canopy.leaf_obt_harvest(),
                    'stem_OBT_Bq_g': self.organs.stem_obt_harvest(),
                    'ear_OBT_Bq_g': self.organs.ear_obt_harvest(),
                    'root_OBT_Bq_g': self.organs.root_obt_harvest(),
                }
                self._harvest_captured = True

            # Peak TFWT — every step
            top_tfwt = self.canopy.TFWT[0] if self.canopy.N > 0 else 0.0
            if top_tfwt > self.results['peak_TFWT']:
                self.results['peak_TFWT'] = top_tfwt

            # Fine-grained time series (every step, for short-term validation)
            ts = self._ts
            ts['t_h'].append(t)
            ts['leaf_tfwt'].append(self.canopy.TFWT[0] if self.canopy.N > 0 else 0.0)
            ts['leaf_obt_str'].append(self.canopy.OBT_str[0] if self.canopy.N > 0 else 0.0)
            ts['leaf_obt_exch'].append(self.canopy.OBT_exch[0] if self.canopy.N > 0 else 0.0)
            ts['ear_obt'].append(self.organs.ear.obt_concentration())
            ts['ear_obt_str'].append(self.organs.ear.OBT_str)
            ts['grain_obt'].append(self.organs.grain_obt_harvest())
            ts['stem_obt'].append(self.organs.stem.obt_concentration())
            ts['a_n_top'].append(self.canopy.A[0] if self.canopy.N > 0 else 0.0)
            ts['canopy_mean_obt'].append(diag['mean_OBT'])

            # Record hourly
            if step_i % self.steps_per_hour == 0:
                self.results['time_h'].append(t)
                self.results['hour_of_day'].append(diag['hour'])
                self.results['Tair'].append(diag['Tair'])
                self.results['PAR'].append(diag['PAR'])
                self.results['C_air'].append(diag['C_air'])
                self.results['C_air_local'].append(diag['C_air_local'])
                self.results['total_A'].append(diag['total_A'])
                self.results['DVS'].append(diag['DVS'])
                self.results['LAI'].append(diag['LAI'])
                self.results['mean_TFWT'].append(diag['mean_TFWT'])
                self.results['mean_OBT'].append(diag['mean_OBT'])
                self.results['grain_OBT'].append(self.organs.grain_obt_harvest())
                self.results['grain_W'].append(self.organs.grain.W_total)
                self.results['E_soil'].append(diag['E_soil'])
                self.results['g_aero'].append(diag['g_aero'])

                if progress_every > 0 and len(self.results['time_h']) % progress_every == 0:
                    print(f"  t={t:.0f}h  DVS={diag['DVS']:.2f}  "
                          f"TFWT={diag['mean_TFWT']:.0f} Bq/L  "
                          f"grain_OBT={self.organs.grain_obt_harvest():.2f} Bq/g  "
                          f"LAI={diag['LAI']:.1f}")

        # ════════ Harvest summary ════════
        harvest = self._harvest_summary()
        self.results['harvest'] = harvest
        self.results['ts'] = {k: v for k, v in self._ts.items()}

        if progress_every > 0:
            print("\n" + "=" * 60)
            print("HARVEST RESULTS")
            print("=" * 60)
            for k, v in harvest.items():
                print(f"  {k}: {v}")
            if self._conservation_warnings > 0:
                print(f"  ⚠ Carbon conservation warnings: {self._conservation_warnings}")

        return self.results

    def _harvest_summary(self):
        """Compute final harvest outputs.

        Uses snapshot captured at grain fill end for leaf/stem/ear
        (to avoid post-fill decay artifacts).
        """
        canopy_obt = self.canopy.total_leaf_obt_inventory()
        peak_tfwt = self.results['peak_TFWT']

        # Use snapshot if available (captured at grain fill end)
        snap = getattr(self, '_harvest_snapshot', None)

        return {
            'grain_OBT_Bq_g': self.organs.grain_obt_harvest(),
            'leaf_OBT_Bq_g': snap['leaf_OBT_Bq_g'] if snap else self.canopy.leaf_obt_harvest(),
            'stem_OBT_Bq_g': snap['stem_OBT_Bq_g'] if snap else self.organs.stem_obt_harvest(),
            'ear_OBT_Bq_g': snap['ear_OBT_Bq_g'] if snap else self.organs.ear_obt_harvest(),
            'root_OBT_Bq_g': snap['root_OBT_Bq_g'] if snap else self.organs.root_obt_harvest(),
            'peak_TFWT_Bq_L': peak_tfwt,
            'final_TFWT_Bq_L': self.canopy.mean_tfwt(),
            'DVS_final': self.DVS,
            'GDD_final': self.startGDD,
            'LAI_final': self.LAI,
            'TLI_pct': self.organs.tli(canopy_obt) * 100,
            # TLI_diabate: only for atmospheric exposure scenarios.
            # Soil-driven scenarios (irrigation) produce meaningless ratios.
            'TLI_diabate_pct': self.organs.tli_diabate(peak_tfwt)
                if (self.soil_HTO_input == 0 and peak_tfwt > 1e-20) else 0.0,
        }

    # ─────────────────────────────────────────────────────────────────
    # Convenience: run Diabaté validation
    # ─────────────────────────────────────────────────────────────────

    @classmethod
    def run_diabate(cls, **overrides):
        """Run the Diabaté 1997 validation scenario."""
        params = dict(cfg.DIABATE_SCENARIO)
        params.update(overrides)
        model = cls(params)
        results = model.run()
        return model, results
