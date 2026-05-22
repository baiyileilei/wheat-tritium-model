"""SOLVEG-II  Organ Module (§3.9–3.12, §3.14–3.16)

Multi-organ carbon + OBT allocation, transport chain, protein turnover,
ear photosynthesis, maintenance respiration.
"""

import math
from . import config as cfg
from .canopy import farquhar, stomatal_conductance, transpiration_rate


# ═══════════════════════════════════════════════════════════════════════
# §3.11.3  DVS interpolation
# ═══════════════════════════════════════════════════════════════════════

def interpolate_partition(dvs, table=None):
    """Linear interpolation of organ partition coefficients by DVS.

    Returns:
        (f_root, f_stem, f_leaf, f_grain, f_ear)
    """
    if table is None:
        table = cfg.ORGAN_PARTITION_WHEAT

    if dvs <= table[0][0]:
        return table[0][1], table[0][2], table[0][3], table[0][4], table[0][5]
    if dvs >= table[-1][0]:
        return table[-1][1], table[-1][2], table[-1][3], table[-1][4], table[-1][5]

    for i in range(len(table) - 1):
        if table[i][0] <= dvs <= table[i + 1][0]:
            f = (dvs - table[i][0]) / (table[i + 1][0] - table[i][0])
            return tuple(
                table[i][j] + f * (table[i + 1][j] - table[i][j]) for j in range(1, 6)
            )

    return table[-1][1], table[-1][2], table[-1][3], table[-1][4], table[-1][5]


# ═══════════════════════════════════════════════════════════════════════
# OrganPool — single organ (two-pool suc + str)
# ═══════════════════════════════════════════════════════════════════════

class OrganPool:
    """Carbon and OBT pools for a single plant organ (two-pool, no OBT_fast)."""

    def __init__(self, name, W_init):
        self.name = name

        # Two-pool: suc (mobile) + str (structural)
        self.W_suc = 0.10 * W_init
        self.W_str = 0.90 * W_init

        # OBT concentrations [Bq/kg C]
        self.OBT_suc = 0.0
        self.OBT_str = 0.0
        self.OBT_exch = 0.0  # exchangeable OBT (O/N/S-bound, equilibrium with TFWT)

        # neOBT inventory [Bq]
        self._neOBT_inv = 0.0

        # Carbon flux OBT pathway: track W_str for dW_str calculation
        self._prev_W_str = 0.90 * W_init

    @property
    def W_total(self):
        return self.W_suc + self.W_str

    def receive_carbon_obt(self, dW, S_source):
        """Receive carbon with OBT into suc pool."""
        if dW < 1e-20:
            return
        W_old = self.W_suc
        OBT_old = self.OBT_suc
        self.W_suc += dW
        if self.W_suc > 1e-20:
            self.OBT_suc = (OBT_old * W_old + S_source * dW) / self.W_suc

    def step_metabolism(self, dt, is_night, TFWT_local, T_mean=25.0, is_sink=False, obt_signal=0.0,
                        is_exposed=False):
        """Internal metabolism: respiration + growth + dark OBT + resp OBT release.

        Removed NU_EXPOSE_* (black-box injection). All non-leaf organs get OBT
        via TFWT transport chain + dark reaction (NU_DARK=0.002/h, uniform).
        Added: maintenance respiration OBT release (Ota Eq.16).
        """
        dt_h = dt / 3600.0
        Q10 = cfg.Q10_RESP ** ((T_mean - 25.0) / 10.0)

        # ── 1. Maintenance respiration + OBT release (Ota Eq.16) ──
        resp_recycled_Bq = 0.0
        if self.W_str > 1e-20 and self.W_suc > 1e-20:
            R_m = cfg.K_RESP * self.W_str * Q10 * dt_h
            R_m = min(R_m, self.W_suc * 0.5)
            if R_m > 1e-20:
                self.W_suc -= R_m
                self.W_suc = max(0.0, self.W_suc)

                # OBT release: respiration consumes W_str, releases ³H as HTO
                if self.OBT_str > 0 and self.W_str > 1e-20:
                    dOBT_release = R_m * self.OBT_str * cfg.F_RELEASE
                    resp_recycled_Bq = dOBT_release
                    self.OBT_str -= dOBT_release / max(self.W_str, 1e-20)
                    self.OBT_str = max(0.0, self.OBT_str)

        # ── 2. Growth: suc → str ──
        if self.W_suc > 1e-20 and not is_sink:
            k_grow = cfg.SINK_K_STEM if self.name == 'stem' else \
                     cfg.SINK_K_ROOT if self.name == 'root' else \
                     cfg.SINK_K_EAR if self.name == 'ear' else 0.001
            G = min(k_grow * self.W_suc * dt_h, self.W_suc * 0.5)
            dW_str = G * cfg.Y_GROWTH
            if dW_str > 1e-20:
                OBT_per_C_suc = self.OBT_suc
                W_str_old = self.W_str
                self.W_str += dW_str
                if self.W_str > 1e-20:
                    OBT_per_C_str = OBT_per_C_suc / 3.0
                    self.OBT_str = (self.OBT_str * W_str_old +
                                    OBT_per_C_str * dW_str) / self.W_str
                self._neOBT_inv += (OBT_per_C_suc / 3.0) * dW_str * 0.30
                self.W_suc -= G
                self.W_suc = max(0.0, self.W_suc)
                if self.W_suc > 1e-20 and G > 1e-20:
                    self.OBT_suc *= (self.W_suc / (self.W_suc + G))

        # ── 3. OBT formation (fast exposure + dark reaction + dynamic exchange) ──
        if self.name != 'grain' and self.W_str > 1e-20:

            # 3a. Exposure-period fast HTO metabolism
            if is_exposed and TFWT_local > 0:
                nu_fast_map = {
                    'stem': cfg.NU_FAST_STEM,
                    'ear': cfg.NU_FAST_EAR,
                    'root': cfg.NU_FAST_ROOT,
                    'leaf': 0.0,
                }
                nu_fast = nu_fast_map.get(self.name, 0.0)
                if nu_fast > 0:
                    dOBT_fast = nu_fast * TFWT_local * dt_h
                    f_prot = cfg.ORGAN_PHYSICS.get(self.name, {}).get('f_prot', 0.10)
                    exch_frac = f_prot * cfg.OBT_EXCH_HYDROGEN_FRAC
                    self.OBT_exch += dOBT_fast * exch_frac
                    self.OBT_str += dOBT_fast * (1.0 - exch_frac)

            # 3b. Dark reaction OBT (post-exposure)
            if not is_exposed and TFWT_local > 0:
                nu = cfg.NU_DARK
                # ear has independent dark metabolism (3× leaf, Diabaté Fig.2)
                if self.name == 'ear':
                    nu = cfg.NU_EAR_DARK
                dOBT_dark = nu * TFWT_local * dt_h
                f_prot = cfg.ORGAN_PHYSICS.get(self.name, {}).get('f_prot', 0.10)
                exch_frac = f_prot * cfg.OBT_EXCH_HYDROGEN_FRAC
                self.OBT_exch += dOBT_dark * exch_frac
                self.OBT_str += dOBT_dark * (1.0 - exch_frac)

            # 3c. OBT_exch dynamic exchange (replaces instantaneous equilibrium)
            # Physical: OBT_exch exchanges with TFWT via O-H/N-H/S-H bonds
            # Rate: K_OBT_EXCH = 0.1/h (not instantaneous!)
            if TFWT_local > 0:
                f_prot = cfg.ORGAN_PHYSICS.get(self.name, {}).get('f_prot', 0.10)
                exch_frac = f_prot * cfg.OBT_EXCH_HYDROGEN_FRAC
                OBT_exch_eq = exch_frac * TFWT_local
                k_exch = cfg.K_OBT_EXCH * dt_h
                self.OBT_exch += k_exch * (OBT_exch_eq - self.OBT_exch)
                self.OBT_exch = max(0.0, self.OBT_exch)
            else:
                k_exch = cfg.K_OBT_EXCH * dt_h
                self.OBT_exch *= (1.0 - k_exch)
                self.OBT_exch = max(0.0, self.OBT_exch)

            # 3d. OBT_str decay (non-leaf organs use own k_turn_day only)
            # NO OBT_RESP_DECAY for non-leaf organs (they don't have photosynthetic OBT input)
            k_turn = cfg.ORGAN_PHYSICS.get(self.name, {}).get('k_turn_day', 0.001)
            # add non-leaf OBT_str decay (ds analysis: faster turnover for stem/ear)
            k_resp = cfg.OBT_RESP_DECAY_NONLEAF if self.name != 'grain' else 0.0
            k_decay = (k_turn + k_resp) * dt_h
            if k_decay > 0:
                self.OBT_str *= (1.0 - k_decay)
                self._neOBT_inv *= (1.0 - k_turn * dt_h)

        return resp_recycled_Bq

    def obt_inventory(self):
        """Total OBT inventory [Bq]."""
        return self.OBT_suc * self.W_suc + self.OBT_str * self.W_str + self.OBT_exch

    def obt_concentration(self):
        """Weighted mean OBT concentration [Bq/kg C]."""
        return self.obt_inventory() / max(self.W_total, 1e-20)

    def obt_harvest(self):
        """OBT at harvest [Bq/g dry]."""
        obt_c = self.obt_concentration()
        return obt_c * cfg.FNEX * 0.0004


# ═══════════════════════════════════════════════════════════════════════
# PlantOrgans — collection of all organs (sink-strength allocation)
# ═══════════════════════════════════════════════════════════════════════

class PlantOrgans:
    """All plant organs with TFWT transport chain and sink-strength allocation."""

    def __init__(self, leaf_C_total, crop_name='wheat', grain_fill_max_h=None):
        W_root = 0.05    # kg C/m²
        W_stem = 0.15
        W_ear = 0.01
        W_grain = 0.001

        self.root = OrganPool('root', W_root)
        self.stem = OrganPool('stem', W_stem)
        self.ear  = OrganPool('ear',  W_ear)
        self.grain = OrganPool('grain', W_grain)

        # TFWT transport chain (unchanged)
        self._stem_TFWT = 0.0
        self._ear_TFWT = 0.0
        self._grain_TFWT = 0.0


        self._grain_W_total_prev = self.grain.W_suc + self.grain.W_str  # for grain fill OBT tracking
        self._grain_obt_total = 0.0  # legacy: kept for compatibility, now grain OBT goes directly to OBT_str
        self._grain_W_at_fill_start = 0.0  # W_total when grain filling began (for avg dW)

        # Grain fill time limit (configurable per scenario)
        self._grain_fill_hours = 0.0
        self._grain_fill_max_h = grain_fill_max_h if grain_fill_max_h is not None else cfg.CROP_PARAMS_WHEAT.get('GRAIN_FILL_H', 720.0)
        self._grain_filling_active = False  # starts inactive, DVS-triggered
        self._exposure_delay_h = 0.0  # deprecated: kept for compatibility
        self._fill_progress_at_exposure = -1.0  # fill progress when exposure occurred (-1=not set)
        self._receptivity_at_exposure = 1.0     # snapshot receptivity (fixed after exposure)

        # Grain microenvironment Cair (husk-enclosed, humid — decays slower than bulk air)
        self._grain_Cair_local = 0.0
        self._TAU_GRAIN_ENV = 72.0  # h — grain husk microenvironment decay
        self._grain_water_frac = 1.0  # grain water fraction (DVS dependent)
        self._last_dW_grain_rate = 0.0  # grain allocation rate for TFWT coupling
        self._last_dW_grain = 0.0  # grain carbon increment per step (for phloem loading)
        self._prev_grain_W_for_rate = 0.001  # for growth rate coupling

        # Reallocation tracking
        self._stem_reallocated = 0.0
        self._ear_reallocated = 0.0

        # Diagnostic counters: grain OBT sources [Bq]
        self.diag_ear_to_grain_obt = 0.0   # K_EAR_TO_GRAIN path
        self.diag_ear_realloc_obt = 0.0    # ear→grain realloc
        self.diag_phloem_loading_obt = 0.0  # canopy→grain phloem loading
        self.diag_stem_realloc_obt = 0.0   # stem→grain realloc
        self.diag_leaf_realloc_obt = 0.0   # leaf→grain realloc
        self.diag_direct_alloc_obt = 0.0   # direct carbon allocation
        self.diag_senescence_obt = 0.0     # leaf senescence → grain

        # expH stored for ear dose correction
        self._expH = 2.0

    def update_organ_TFWT(self, C_air, C_slow_canopy, dt, dvs, canopy_mean_TFWT=0.0, C_xylem=0.0):
        """Update TFWT transport chain for all organs (§3.14.5, + surface absorption).

        Added surface absorption for stem/ear during exposure.
        Physical: stem/ear surface directly contacts atmospheric HTO,
        equilibrating faster than the slow transport chain (τ=30h).
        """
        tau_stem_s = cfg.TAU_STEM * 3600.0
        tau_ear_s = cfg.TAU_EAR * 3600.0

        # Stem: approaches C_stem_water (max of canopy C_slow and xylem)
        k_stem = 1.0 / tau_stem_s
        self._stem_TFWT += k_stem * (C_slow_canopy - self._stem_TFWT) * dt
        self._stem_TFWT = max(0.0, self._stem_TFWT)

        # Surface absorption during exposure — stem directly absorbs atmospheric HTO
        # Physical: moist stem surface equilibrates with ambient HTO much faster than
        # the internal transport chain (τ=30h). Effective τ_surface ≈ 1/k_abs.
        if C_air > 0 and hasattr(cfg, 'K_ABSORP_STEM'):
            k_abs_stem = cfg.K_ABSORP_STEM / 3600.0  # 1/s
            target_atmo = C_air / cfg.ALPHA_CG
            self._stem_TFWT += k_abs_stem * (target_atmo - self._stem_TFWT) * dt
            self._stem_TFWT = max(0.0, self._stem_TFWT)

        # Ear: approaches max(stem, xylem)
        ear_target = max(self._stem_TFWT, C_xylem)
        k_ear = 1.0 / tau_ear_s
        self._ear_TFWT += k_ear * (ear_target - self._ear_TFWT) * dt
        self._ear_TFWT = max(0.0, self._ear_TFWT)

        # Surface absorption for ear during exposure
        if C_air > 0 and hasattr(cfg, 'K_ABSORP_EAR'):
            k_abs_ear = cfg.K_ABSORP_EAR / 3600.0  # 1/s
            target_atmo = C_air / cfg.ALPHA_CG
            self._ear_TFWT += k_abs_ear * (target_atmo - self._ear_TFWT) * dt
            self._ear_TFWT = max(0.0, self._ear_TFWT)

        # Grain water: slow equilibration during exposure, slow decay after
        # grain water fraction decreases as grain matures (DVS 1.0→2.0)
        if dvs >= 1.0:
            canopy_TFWT = max(canopy_mean_TFWT, 0.0)

            # Grain water fraction: 0.60 at DVS=1.0 → 0.14 at DVS=2.0
            w_frac = cfg.GRAIN_WATER_FRAC_INITIAL + \
                     (cfg.GRAIN_WATER_FRAC_MATURE - cfg.GRAIN_WATER_FRAC_INITIAL) * \
                     min(1.0, max(0.0, (dvs - 1.0)) ** 0.5)
            prev_frac = getattr(self, '_prev_grain_water_frac', w_frac)
            if prev_frac > 1e-10 and abs(w_frac - prev_frac) / prev_frac > 1e-6:
                self._grain_TFWT *= prev_frac / w_frac  # concentrate: less water → higher Bq/L
            self._prev_grain_water_frac = w_frac

            if canopy_TFWT > self._grain_TFWT:  # exposure ongoing — HTO entering grain via phloem
                k_base = 1.0 / (4.0 * 3600.0)  # τ_rise = 4h (phloem transport, fast)
                # Scale rise by fill_progress — early grain fill has less phloem activity
                # This suppresses DAF=1 (exposure at anthesis, fill_progress≈0)
                # while keeping DAF=13+ (fill_progress>0.3) effective.
                fill_p = max(0.0, min(1.0, (dvs - 1.0) / max(cfg.DVS_MATURE - 1.0, 0.1)))
                k_base *= fill_p ** cfg.GRAIN_TFWT_RISE_POWER
                alloc_rate = getattr(self, '_last_dW_grain_rate', 0.0)
                k_rise = k_base
                self._grain_TFWT += k_rise * (canopy_TFWT - self._grain_TFWT) * dt
            else:  # post-exposure — slow decay (grain water HTO loss)
                k_slow = 1.0 / (cfg.TAU_CANOPY_TO_GRAIN * 3600.0)
                self._grain_TFWT -= k_slow * self._grain_TFWT * dt
            self._grain_TFWT = max(0.0, self._grain_TFWT)

        # Grain microenvironment Cair
        k_env = 1.0 / (self._TAU_GRAIN_ENV * 3600.0)
        self._grain_Cair_local += k_env * (C_air - self._grain_Cair_local) * dt
        self._grain_Cair_local = max(0.0, self._grain_Cair_local)

    def _grain_receptivity(self):
        """Grain receptivity: snapshot at exposure time.

        Receptivity is a FIXED coefficient computed at exposure time.
        Uses fill_progress (0→1) in a bell curve:
          fp=0 → baseline (0.10), fp=0.012 → peak (1.0), fp>0.012 → decay
        Non-monotonic DAF: low fp → low receptivity (DAF=1), mid fp → peak (DAF=12).
        """
        return max(0.0, min(1.0, self._receptivity_at_exposure))

    @staticmethod
    def compute_snapshot_receptivity(fill_progress):
        """Compute snapshot receptivity from fill_progress.

        Bell curve centered at RECEPTIVITY_PEAK_FP with baseline at fp=0.
        """
        fp = max(0.0, fill_progress)
        peak = cfg.RECEPTIVITY_PEAK_FP
        sigma = cfg.RECEPTIVITY_SIGMA
        baseline = cfg.RECEPTIVITY_BASELINE

        if fp <= 0:
            return baseline

        # Bell curve: peak=1.0 at fp=peak, decays as fp moves away
        import math
        bell = math.exp(-0.5 * ((fp - peak) / sigma) ** 2)

        # Scale so baseline at fp=0
        bell_at_zero = math.exp(-0.5 * (peak / sigma) ** 2)
        # receptivity = baseline + (1.0 - baseline) * (bell - bell_at_zero) / (1.0 - bell_at_zero)
        if bell_at_zero >= 1.0:
            return baseline
        receptivity = baseline + (1.0 - baseline) * (bell - bell_at_zero) / (1.0 - bell_at_zero)
        return max(baseline, min(1.0, receptivity))

    def step_allocate(self, dW_leaf, S_leaf_suc, dvs, T_mean, dt, is_night,
                      C_slow_canopy, obt_signal=0.0, canopy_mean_TFWT=0.0,
                      is_exposed=False):
        """Allocate carbon from leaves to organs via sink strength.

        dW_leaf: total photo carbon from canopy [kg C/m² ground]
        S_leaf_suc: OBT concentration in leaf suc pool [Bq/kg C]
        grain OBT injection removed — all grain OBT via step_grain_obt + senescence.
        No dose_factor.
        """
        # Sink strength for each organ
        S_root  = cfg.SINK_K_ROOT * max(0.0, 0.05 - self.root.W_str)
        S_stem  = cfg.SINK_K_STEM * self.stem.W_str
        S_ear   = cfg.SINK_K_EAR  * self.ear.W_str
        # Grain: dominant sink during grain fill, saturates
        if dvs >= 1.0:
            grain_fill = max(0.0, cfg.GRAIN_W_STR_MAX - self.grain.W_str)
            tf = 0.65 + 0.0787 * max(0.0, T_mean - 10.0) ** 0.8 if T_mean > 10.0 else 0.065 * max(0.0, T_mean)
            tf = min(1.0, max(0.0, tf))
            S_grain = cfg.SINK_K_GRAIN * grain_fill * tf
        else:
            S_grain = 0.0

        S_total = S_root + S_stem + S_ear + S_grain
        if S_total < 1e-20 or dW_leaf < 1e-20:
            # No sinks active — just run metabolism
            recycled = self._run_metabolism(dt, is_night, T_mean, obt_signal=obt_signal,
                                              canopy_mean_TFWT=canopy_mean_TFWT,
                                              is_exposed=is_exposed)
            return recycled

        # Allocate by sink proportion
        alloc = [
            (self.root,  S_root  / S_total),
            (self.stem,  S_stem  / S_total),
            (self.ear,   S_ear   / S_total),
            (self.grain, S_grain / S_total),
        ]

        # Ear mean OBT — used as grain's OBT source (ear→grain transfer)
        ear_inv = self.ear.OBT_str * self.ear.W_str + self.ear.OBT_suc * self.ear.W_suc
        ear_W = self.ear.W_str + self.ear.W_suc
        ear_mean_OBT = ear_inv / max(ear_W, 1e-20)

        # Compute grain growth rate (for grain_TFWT coupling)
        dW_grain = dW_leaf * (S_grain / S_total) if S_total > 1e-20 else 0.0

        # Track grain allocation rate for grain_TFWT coupling
        self._last_dW_grain_rate = dW_grain / max(dt / 3600.0, 1e-10)
        self._last_dW_grain = dW_grain

        for organ, frac in alloc:
            dW = dW_leaf * frac
            if dW > 1e-20:
                # grain receives carbon only (no OBT injection here)
                # grain OBT comes from K_OBT_REMOB (step_grain_obt) + senescence
                organ.receive_carbon_obt(dW, S_leaf_suc if organ is not self.grain else 0.0)
        # Internal metabolism for each organ
        recycled = self._run_metabolism(dt, is_night, T_mean, obt_signal=obt_signal,
                                        canopy_mean_TFWT=canopy_mean_TFWT,
                                        is_exposed=is_exposed)
        return recycled

    def _run_metabolism(self, dt, is_night, T_mean=25.0, obt_signal=0.0,
                        canopy_mean_TFWT=0.0, is_exposed=False):
        """Run metabolism for all organs, collect respiratory recycling.

        passes organ-specific TFWT (from transport chain) for fast HTO metabolism.
        Each organ has its own TFWT from update_organ_TFWT (stem_TFWT, ear_TFWT, etc.)
        which is critical for exposure-period fast HTO incorporation.
        """
        recycled = 0.0
        # Use organ-specific TFWT for each organ (from transport chain)
        recycled += self.root.step_metabolism(dt, is_night, canopy_mean_TFWT, T_mean, is_exposed=is_exposed)
        recycled += self.stem.step_metabolism(dt, is_night, self._stem_TFWT, T_mean, is_exposed=is_exposed)
        recycled += self.ear.step_metabolism(dt, is_night, self._ear_TFWT, T_mean, is_exposed=is_exposed)
        recycled += self.grain.step_metabolism(dt, is_night, self._grain_TFWT, T_mean, is_exposed=is_exposed)

        # ── Grain OBT turnover (limits chronic accumulation) ──
        if cfg.K_GRAIN_TURN > 0 and self._grain_obt_total > 1e-20 and not self._grain_filling_active:
            dt_h = dt / 3600.0
            k_turn = cfg.K_GRAIN_TURN * dt_h
            self._grain_obt_total *= (1.0 - k_turn)

        return recycled

    def receive_leaf_realloc(self, dW, S_leaf, is_night, expH=2.0):
        """Receive carbon reallocated from leaves → grain.

        OBT transfers with carbon via S_leaf. No dose correction.
        Only active during grain fill.
        OBT gated by snapshot receptivity.
        """
        if dW < 1e-20:
            return
        dW_eff = dW * cfg.REALLOC_EFF
        # Carbon to grain W_suc (only during grain fill)
        if self._grain_filling_active:
            self.grain.W_suc += dW_eff
            # OBT gated by snapshot receptivity
            if S_leaf > 1e-20:
                receptivity = self._grain_receptivity()
                self._grain_obt_total += S_leaf * dW_eff * receptivity

    def step_stem_reallocation(self, dt, dvs):
        """Stem carbon reallocation to grain during grain fill.

        Draws from BOTH suc and str pools. OBT transfers proportional to mean OBT.
        Use config K_RECEP for receptivity. Removed OBT_fast.
        """
        if dvs < cfg.REALLOC_DVS:
            return

        dt_day = dt / 86400.0
        W_avail = (self.stem.W_suc + self.stem.W_str) * cfg.REALLOC_STEM_FRAC
        remaining = W_avail - self._stem_reallocated

        if remaining < 1e-20:
            return

        dW = min(cfg.REALLOC_STEM_RATE * remaining * dt_day, remaining)
        W_total_stem = self.stem.W_suc + self.stem.W_str
        if W_total_stem < 1e-20:
            return
        dW = min(dW, W_total_stem * 0.10)

        if dW > 1e-20:
            S_stem = self.stem.obt_concentration()

            # Receptivity based on grain development stage (fill_progress)
            receptivity = self._grain_receptivity()

            obt = S_stem * dW * cfg.REALLOC_EFF * receptivity
            self.diag_stem_realloc_obt += obt
            frac_suc = self.stem.W_suc / W_total_stem
            frac_str = self.stem.W_str / W_total_stem
            self.stem.W_suc -= dW * frac_suc
            self.stem.W_str -= dW * frac_str
            frac_transferred = dW / W_total_stem
            obt_exch_transferred = self.stem.OBT_exch * frac_transferred * receptivity
            self.stem.OBT_exch -= obt_exch_transferred
            if self._grain_filling_active:
                self.grain.W_suc += dW * cfg.REALLOC_EFF
                if cfg.ENABLE_SENESCENCE_OBT_TRANSFER:
                    self._grain_obt_total += obt + obt_exch_transferred
            self._stem_reallocated += dW

    def step_ear_reallocation(self, dt, dvs):
        """Ear carbon reallocation to grain during grain fill.

        Draws from BOTH suc and str pools. Carbon goes to grain W_str.
        OBT goes to _grain_obt_total (not OBT_str) to avoid dilution.
        Removed EAR_DOSE_POWER (dose correction). Removed OBT_fast.
        """
        if dvs < cfg.REALLOC_DVS:
            return

        dt_day = dt / 86400.0
        W_total_ear = self.ear.W_suc + self.ear.W_str
        W_avail = W_total_ear * cfg.REALLOC_EAR_FRAC
        remaining = W_avail - self._ear_reallocated

        if remaining < 1e-20:
            return

        dW = min(cfg.REALLOC_EAR_RATE * remaining * dt_day, remaining)
        dW = min(dW, W_total_ear * 0.10)

        if dW > 1e-20:
            S_ear = self.ear.obt_concentration()

            # Receptivity based on grain development stage (fill_progress)
            receptivity = self._grain_receptivity()

            frac_suc = self.ear.W_suc / W_total_ear if W_total_ear > 1e-20 else 0
            frac_str = self.ear.W_str / W_total_ear if W_total_ear > 1e-20 else 0
            self.ear.W_suc -= dW * frac_suc
            self.ear.W_str -= dW * frac_str

            dW_grain = dW * cfg.REALLOC_EFF
            if dW_grain > 1e-20 and self._grain_filling_active:
                self.grain.W_str += dW_grain

                # no dose correction (removed EAR_DOSE_POWER)
                if S_ear > 0 and cfg.ENABLE_SENESCENCE_OBT_TRANSFER:
                    obt_transferred = S_ear * dW_grain * receptivity
                    self.diag_ear_realloc_obt += obt_transferred
                    self._grain_obt_total += obt_transferred

                frac_transferred = dW / W_total_ear if W_total_ear > 1e-20 else 0
                if cfg.ENABLE_SENESCENCE_OBT_TRANSFER:
                    obt_exch_transferred = self.ear.OBT_exch * frac_transferred * receptivity
                    self.ear.OBT_exch -= obt_exch_transferred
                    self._grain_obt_total += obt_exch_transferred

            self._ear_reallocated += dW

    def step_ear_obt_to_grain(self, dt, dvs):
        """Ear OBT → grain transfer during grain fill.

        Physical: ear accumulates OBT from canopy (phloem + senescence) during
        pre-grain-fill period. During grain fill, ear OBT transfers to grain.
        Removed OBT_fast. Simplified.
        """
        if dvs < 1.0 or not self._grain_filling_active:
            return
        if self.ear.OBT_str < 1e-20 or self.ear.W_str < 1e-20:
            return

        dt_h = dt / 3600.0
        fill_progress = min(1.0, self._grain_fill_hours / max(self._grain_fill_max_h, 1.0))

        transfer_frac = 0.50 * dt_h * fill_progress  # EAR_TO_GRAIN_OBT_RATE
        transfer_frac = min(transfer_frac, 0.5)

        obt_transferred = self.ear.OBT_str * self.ear.W_str * transfer_frac
        if obt_transferred > 1e-20 and cfg.ENABLE_SENESCENCE_OBT_TRANSFER:
            self.ear.OBT_str -= obt_transferred / max(self.ear.W_str, 1e-20)
            self.ear.OBT_str = max(0.0, self.ear.OBT_str)
            self._grain_obt_total += obt_transferred
            self.diag_ear_realloc_obt += obt_transferred

    def stop_grain_filling(self):
        """Stop grain filling (time limit reached)."""
        self._grain_filling_active = False
        self._grain_W_at_fill_end = self.grain.W_total  # snapshot for harvest concentration

    def trigger_grain_fill(self):
        """Start grain filling (GDD-based trigger at anthesis).

        Called by model when GDD reaches GDD_ANTHESIS.
        Resets fill hours counter and activates grain fill.
        """
        self._grain_fill_hours = 0.0
        self._grain_filling_active = True
        self._grain_W_at_fill_start = self.grain.W_total

    def step_grain_obt(self, dt, dvs, T_mean=25.0, grain_TFWT=0.0, is_night=False,
                       leaf_mean_OBT_str=0.0, leaf_mean_OBT_exch=0.0):
        """Grain OBT: leaf OBT_str remobilization (with receptivity gate).

        Physical: during grain fill, leaf proteins are hydrolyzed → amino acids
        travel via phloem → re-synthesized as grain proteins.

        K_REMOB gated by grain receptivity (sigmoid).
        Grain needs time to build enzyme system before it can efficiently accept OBT.
        This ensures grain OBT monotonically increases during grain fill
        (receptivity ↑ compensates for canopy OBT ↓).
        """
        if dvs < 1.0:
            self._grain_W_total_prev = self.grain.W_total
            return

        dt_h = dt / 3600.0

        # Only accumulate grain fill hours when grain filling is active
        # (triggered by GDD at anthesis, not by DVS)
        if self._grain_filling_active:
            self._grain_fill_hours += dt_h

        if not self._grain_filling_active:
            self._grain_W_total_prev = self.grain.W_total
            k_turn = cfg.ORGAN_PHYSICS['grain']['k_turn_day'] * dt_h
            if k_turn > 0:
                self._grain_obt_total *= (1.0 - k_turn)
            return

        if self._grain_fill_hours >= self._grain_fill_max_h:
            self.stop_grain_filling()
            self._grain_W_total_prev = self.grain.W_total
            return

        W_now = self.grain.W_total
        dW = W_now - self._grain_W_total_prev
        self._grain_W_total_prev = W_now

        if dW < 1e-20:
            return

        # ═══════ Receptivity gates K_REMOB ═══════
        # Sigmoid on fill_progress_at_exposure: grain receptivity depends on
        # developmental stage when exposure occurred.
        # DAF non-monotonicity: receptivity × canopy_OBT_decay × remaining_fill_time
        receptivity = self._grain_receptivity()

        # K_REMOB path: leaf OBT_str → grain (gated by receptivity)
        # based on W_grain (continuous transfer), not dW (stops when grain stops growing)
        if cfg.K_REMOB > 0 and leaf_mean_OBT_str > 0:
            dOBT = cfg.K_REMOB * leaf_mean_OBT_str * W_now * dt_h * receptivity
            self._grain_obt_total += dOBT

        # Ear→grain direct OBT transfer (Galeriu mechanism)
        # Ear tissue absorbs HTO directly → OBT → transfers to grain
        if hasattr(cfg, 'K_EAR_TO_GRAIN') and cfg.K_EAR_TO_GRAIN > 0:
            ear_obt = getattr(self, '_ear_obt_total', 0.0)
            if ear_obt > 0:
                fill_progress = min(self._grain_fill_hours / max(self._grain_fill_max_h, 1.0), 1.0)
                dOBT_ear = cfg.K_EAR_TO_GRAIN * ear_obt * dt_h * fill_progress
                self._grain_obt_total += dOBT_ear

        # Stem→grain OBT backflow (late DAF: canopy OBT exhausted, stem reserves feed grain)
        if cfg.K_STEM_TO_GRAIN > 0 and self.stem.OBT_str > 0 and self.stem.W_str > 1e-20:
            dOBT_stem = cfg.K_STEM_TO_GRAIN * self.stem.OBT_str * self.stem.W_str * dt_h * receptivity
            self._grain_obt_total += dOBT_stem
            self.diag_stem_realloc_obt += dOBT_stem

        k_turn = cfg.ORGAN_PHYSICS['grain']['k_turn_day'] * dt_h
        if k_turn > 0:
            self._grain_obt_total *= (1.0 - k_turn)

    # ─────────────────────────────────────────────────────────────────
    # §3.15  Ear photosynthesis
    # ─────────────────────────────────────────────────────────────────

    def step_ear_photosynthesis(self, PAR_top, T_ear, dt):
        """Independent ear photosynthesis (OBT via F_DARK['ear'])."""
        if PAR_top <= 0:
            return

        PAR_ear = PAR_top * cfg.F_EAR_PAR / max(cfg.EAR_GREEN_AREA, 0.01)

        crop_ear = dict(cfg.CROP_PARAMS_WHEAT)
        crop_ear['Vcmax25'] *= cfg.VCMAX_EAR_SCALE
        crop_ear['Jmax25'] *= (0.5 + 0.5 * cfg.VCMAX_EAR_SCALE)
        crop_ear['g0'] = cfg.G0_EAR
        crop_ear['g1'] = cfg.G1_EAR

        Ci_mol = 0.7 * cfg.CO2_ATM * 1e-6
        result = farquhar(Ci_mol, PAR_ear, T_ear, crop_ear)
        A_ear = result['A']

        if A_ear <= 0:
            return

        dW = (1.0 / 6.0) * cfg.MD * A_ear * 1e-6 * cfg.EAR_GREEN_AREA * dt

        if dW > 1e-20:
            self.ear.receive_carbon_obt(dW, self.ear.OBT_suc)  # inherit from ear suc

    # ─────────────────────────────────────────────────────────────────
    # Summary outputs
    # ─────────────────────────────────────────────────────────────────

    def total_obt_inventory(self):
        """Total plant OBT inventory [Bq/m² ground]."""
        return (self.root.obt_inventory() + self.stem.obt_inventory() +
                self.ear.obt_inventory() + self.grain.obt_inventory())

    def grain_obt_harvest(self):
        """Grain OBT at harvest [Bq/g dry]."""
        total_C = getattr(self, '_grain_W_at_fill_end', self.grain.W_total)
        if total_C < 1e-20:
            return 0.0
        total_obt = (self.grain.OBT_str * self.grain.W_str +
                     self.grain.OBT_suc * self.grain.W_suc +
                     self._grain_obt_total)
        g_dry = total_C / 0.4 * 1000
        return total_obt * cfg.FNEX / max(g_dry, 1e-20)

    def stem_obt_harvest(self):
        """Stem OBT at harvest [Bq/g dry]."""
        return self.stem.obt_harvest()

    def ear_obt_harvest(self):
        """Ear OBT at harvest [Bq/g dry]."""
        return self.ear.obt_harvest()

    def root_obt_harvest(self):
        """Root OBT at harvest [Bq/g dry]."""
        return self.root.obt_harvest()

    def tli(self, canopy_obt_inv):
        """Translocation Index (§4.4).

        TLI = grain_OBT / (grain + stem + root + ear + canopy)
        """
        g = self.grain.obt_inventory()
        s = self.stem.obt_inventory()
        r = self.root.obt_inventory()
        e = self.ear.obt_inventory()
        total = g + s + r + e + canopy_obt_inv
        return g / max(total, 1e-20)

    def tli_diabate(self, peak_tfwt):
        """TLI per Diabaté definition."""
        if peak_tfwt < 1e-20:
            return 0.0
        return self.grain_obt_harvest() / peak_tfwt * 100.0
