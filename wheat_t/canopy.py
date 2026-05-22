"""SOLVEG-II  Canopy Module (§3.2–3.8, §3.13)

Multi-layer canopy with:
  - Farquhar photosynthesis (§3.2)
  - Medlyn stomatal conductance (§3.3)
  - Transpiration (§3.4)
  - Two-chamber water model for TFWT (§3.5)
  - Dark reaction OBT (§3.6)
  - Photosynthetic OBT fixation (§3.7)
  - Four-pool carbon model (§3.8)
  - Protein turnover (§3.9)
  - neOBT accumulation (§3.10)
  - Leaf senescence (§3.13)
"""

import math
from . import config as cfg


# ═══════════════════════════════════════════════════════════════════════
# §3.2  Farquhar photosynthesis
# ═══════════════════════════════════════════════════════════════════════

def _peaked_arrhenius(Ha, Hd, S, T_leaf):
    """Peaked Arrhenius temperature response (Bernacchi 2001)."""
    T_K = T_leaf + cfg.TK0
    T_25 = cfg.TK0 + 25.0
    R = cfg.R_GAS
    e1 = Ha * (T_K - T_25) / (T_25 * R * T_K)
    e2 = (S * T_K - Hd) / (R * T_K)
    return math.exp(e1) / (1.0 + math.exp(e2))


def _arrhenius(Ha, T_leaf):
    """Simple Arrhenius temperature response."""
    T_K = T_leaf + cfg.TK0
    T_25 = cfg.TK0 + 25.0
    return math.exp(Ha * (T_K - T_25) / (T_25 * cfg.R_GAS * T_K))


def farquhar(Ci_mol, PAR, T_leaf, crop_params):
    """Farquhar photosynthesis model (§3.2.2).

    Args:
        Ci_mol: intercellular CO₂ [mol/mol]
        PAR: photosynthetically active radiation [µmol/m²/s]
        T_leaf: leaf temperature [°C]
        crop_params: dict with Vcmax25, Jmax25, Rd25, TPU25, ...

    Returns:
        dict with A [µmol/m²/s], Gs [ppm], Rd [µmol/m²/s]
    """
    Vcmax = crop_params['Vcmax25'] * _peaked_arrhenius(
        crop_params['HaV'], crop_params['HdV'], crop_params['Sv'], T_leaf)
    Jmax = crop_params['Jmax25'] * _peaked_arrhenius(
        crop_params['HaJ'], crop_params['HdJ'], crop_params['Sj'], T_leaf)
    Rd = crop_params['Rd25'] * _arrhenius(crop_params['HaRd'], T_leaf)

    # CO₂ compensation point Γ*  and Michaelis constants
    Gamma_star = 42.75e-6 * _arrhenius(37830.0, T_leaf)   # mol/mol  (ppm→mol)
    Kc = 302.2e-6 * _arrhenius(79430.0, T_leaf)            # mol/mol
    Ko = 0.278 * _arrhenius(36380.0, T_leaf)                # mol/mol  (not mol/mol, it's fractional)

    Ci = max(Ci_mol, Gamma_star * 1.5)

    # Electron transport rate
    I2 = PAR * 0.3  # µmol e⁻/m²/s
    J_num = I2 + Jmax - math.sqrt(max(0.0, (I2 + Jmax) ** 2 - 4 * 0.7 * I2 * Jmax))
    J = J_num / 1.4

    # Rubisco-limited
    Ac = Vcmax * (Ci - Gamma_star) / (Ci + Kc * (1.0 + 0.21 / Ko))

    # Light-limited
    Aj = J * (Ci - Gamma_star) / (4.0 * (Ci + 2.0 * Gamma_star))

    # TPU-limited — only relevant at very high Ci (>1000 ppm), disabled for normal conditions
    # TPU = crop_params.get('TPU25', 18.0) * math.exp(0.05 * (T_leaf - 25.0))
    # Ap = TPU * Ci / (Ci + 0.015)

    A_leaf = max(0.0, min(Ac, Aj) - Rd)

    return {'A': A_leaf, 'Gs': Gamma_star, 'Rd': Rd, 'Vcmax': Vcmax, 'Jmax': Jmax}


# ═══════════════════════════════════════════════════════════════════════
# §3.3  Medlyn stomatal conductance
# ═══════════════════════════════════════════════════════════════════════

def stomatal_conductance(A_net, D, crop_params, is_night=False):
    """Medlyn et al. 2011 stomatal conductance (§3.3).

    Args:
        A_net: net assimilation [µmol/m²/s]
        D: leaf-to-air VPD [kPa]
        crop_params: dict with g0, g1
        is_night: if True, return cuticular conductance

    Returns:
        gs [mol H₂O/m²/s]
    """
    if is_night:
        return crop_params.get('g0_night', 0.0001)  # cuticular conductance
    g0 = crop_params['g0']
    g1 = crop_params['g1']
    Ca = cfg.CO2_ATM  # ppm
    gs = g0 + 1.6 * (1.0 + g1 / math.sqrt(max(0.01, D))) * A_net / Ca
    return max(0.005, gs)


# ═══════════════════════════════════════════════════════════════════════
# §3.4  Transpiration rate
# ═══════════════════════════════════════════════════════════════════════

def gb_boundary(wind, d_leaf=0.02):
    """边界层导度 [mol/m²/s]"""
    return 0.004 * math.sqrt(max(0.01, wind / d_leaf)) / 0.0245  # m/s → mol/m²/s


def transpiration_rate(gs, wind=2.0, VPD=1.0, is_night=False):
    """
    蒸腾速率 [m/s]。

    改进点（vs v3）：
    - 边界层导度 gb 串联 gs（框架 §3.3）
    - VPD 修正仅白天（夜间 cuticular conductance 不受 VPD 调制）

    Args:
        gs: stomatal conductance [mol/m²/s]
        wind: wind speed [m/s] for boundary layer
        VPD: vapor pressure deficit [kPa]
        is_night: if True, skip VPD correction

    Returns:
        T_vol [m/s]
    """
    gs_ref = 0.15    # mol/m²/s（标定参考值）
    T_ref = 9.7e-8   # m/s（重新标定：补偿边界层串联效应）
    VPD_ref = 1.11   # kPa（Diabaté 条件标定）

    # 边界层导度 [mol/m²/s]
    gb = gb_boundary(wind)

    # 串联总导度
    if gs < 1e-12 and gb < 1e-12:
        return 0.0
    g_total = 1.0 / (1.0 / max(gs, 1e-12) + 1.0 / max(gb, 1e-12))

    # 蒸腾 = 导度缩放 × VPD 修正（仅白天）
    vpd_factor = 1.0 if is_night else (max(0.01, VPD) / VPD_ref)
    return T_ref * (g_total / gs_ref) * vpd_factor


# ═══════════════════════════════════════════════════════════════════════
# Canopy Model Class
# ═══════════════════════════════════════════════════════════════════════

class CanopyModel:
    """Multi-layer canopy model with TFWT, OBT, and carbon pools."""

    def __init__(self, LAI, n_layers, height, wind_top, crop_params):
        self.N = n_layers
        self.LAI = LAI
        self.height = height
        self.crop = crop_params

        # Layer division
        self.dLAI = [LAI / n_layers] * n_layers  # [m²/m²]
        self.dz = height / n_layers               # [m]

        # Radiation state
        self.LAIsl = [0.0] * n_layers   # sunlit LAI
        self.LAIsh = [0.0] * n_layers   # shaded LAI
        self.PARsl = [0.0] * n_layers
        self.PARsh = [0.0] * n_layers

        # Metabolic state (per layer)
        self.A = [0.0] * n_layers       # net assimilation [µmol/m²/s]
        self.gs = [0.0] * n_layers      # stomatal conductance [mol/m²/s]
        self.Tleaf = [25.0] * n_layers  # leaf temperature [°C]
        self.wind_layer = [wind_top] * n_layers

        # Two-chamber water model (§3.5)
        self.WHTO_fast = [0.0] * n_layers   # Bq/m² leaf
        self.WHTO_slow = [0.0] * n_layers
        self.TFWT = [0.0] * n_layers        # Bq/L  (single-chamber leaf water)
        self._TFWT_total = [0.0] * n_layers  # Bq/L  (compatibility: same as TFWT)
        self._C_slow_local = [0.0] * n_layers  # Bq/L  (C_slow for dark rxn)

        # Two-pool carbon model (suc=mobile, str=structural) [kg C/m² leaf]
        self.W_suc = [0.0] * n_layers
        self.W_str = [0.0] * n_layers

        # OBT concentrations per pool [Bq/kg C]
        self.OBT_suc = [0.0] * n_layers
        self.OBT_str = [0.0] * n_layers
        self.OBT_exch = [0.0] * n_layers  # exchangeable OBT (O/N/S-bound, equilibrium with TFWT)
        self._OBT_released = [0.0] * n_layers  # canopy protein turnover HTO release (for redistribution)

        # neOBT inventory [Bq/m² leaf] (not concentration!)
        self._neOBT_inv = [0.0] * n_layers

        # Cumulative photo OBT flux for this step (used by organs allocation)
        self._photo_OBT_flux = [0.0] * n_layers

        # Senescence state (per-instance, not class-level)
        self._prev_sen_cumul = 0.0

        # Initialise carbon pools per layer (~DVS=1.0)
        self._init_carbon_pools()

    def _init_carbon_pools(self):
        """Initialise carbon pools at DVS≈1.0 (two-pool model)."""
        W_tot = cfg.LEAF_C_PER_LAYER  # kg C/m² leaf per layer
        for i in range(self.N):
            self.W_str[i] = 0.90 * W_tot
            self.W_suc[i] = 0.10 * W_tot

    # ─────────────────────────────────────────────────────────────────
    # Radiation allocation
    # ─────────────────────────────────────────────────────────────────

    def layer_wind(self, wind_top):
        """Exponential wind profile through canopy (simplified)."""
        for i in range(self.N):
            # depth fraction from top: (i+0.5)/N
            depth_frac = (i + 0.5) / self.N
            self.wind_layer[i] = max(0.1, wind_top * math.exp(-0.5 * depth_frac * self.LAI))
            # Use wind to approximate leaf temperature
            self.Tleaf[i] = 25.0  # simplified, could couple with energy balance

    def layer_radiation(self, PAR_top, sin_beta):
        """Beer-Law extinction of PAR through canopy (§3.2 setup).

        Returns:
            (PARsl_list, PARsh_list)
        """
        if PAR_top <= 0:
            self.PARsl = [0.0] * self.N
            self.PARsh = [0.0] * self.N
            self.LAIsl = [0.0] * self.N
            self.LAIsh = [self.dLAI[i] for i in range(self.N)]
            return self.PARsl, self.PARsh

        k_b = 0.5 / max(0.1, sin_beta)  # beam extinction coefficient
        k_d = 0.7  # diffuse extinction coefficient

        cum_LAI = 0.0
        for i in range(self.N):
            dLAI = self.dLAI[i]
            mid_LAI = cum_LAI + dLAI / 2

            # Beam PAR at this layer
            PAR_beam = PAR_top * math.exp(-k_b * mid_LAI)
            PAR_diff = PAR_top * 0.15 * math.exp(-k_d * mid_LAI)  # ~15% diffuse

            # Sunlit / shaded LAI
            lai_sl = (1.0 / k_b) * math.exp(-k_b * cum_LAI) * (1.0 - math.exp(-k_b * dLAI))
            lai_sl = min(lai_sl, dLAI)
            lai_sh = dLAI - lai_sl

            self.LAIsl[i] = lai_sl
            self.LAIsh[i] = lai_sh
            self.PARsl[i] = PAR_beam + PAR_diff
            self.PARsh[i] = PAR_diff

            cum_LAI += dLAI

        return self.PARsl, self.PARsh

    # ─────────────────────────────────────────────────────────────────
    # Photosynthesis + stomatal conductance (per layer)
    # ─────────────────────────────────────────────────────────────────

    def step_photosynthesis(self, T_air, ea, is_night):
        """Compute layer-wise A, gs, transpiration.

        Returns:
            (total_A, mean_gs, total_transp)  summed/averaged over canopy
        """
        Ci_mol = 0.7 * cfg.CO2_ATM * 1e-6  # typical C3
        total_A = 0.0
        total_gs = 0.0
        total_transp = 0.0

        for i in range(self.N):
            if self.dLAI[i] < 1e-6:
                continue

            # Sunlit and shaded photosynthesis
            res_sl = farquhar(Ci_mol, self.PARsl[i], T_air, self.crop)
            res_sh = farquhar(Ci_mol, self.PARsh[i], T_air, self.crop)

            f_sl = self.LAIsl[i] / max(self.dLAI[i], 1e-6)
            A_i = f_sl * res_sl['A'] + (1.0 - f_sl) * res_sh['A']
            self.A[i] = A_i
            self.Tleaf[i] = T_air  # simplified

            # VPD
            D = max(0.01, self.crop.get('es_override', 0) or
                    (cfg.e_sat(T_air) - ea) if hasattr(cfg, 'e_sat') else 0.5)
            # Simpler: use a fixed VPD if we don't have ea available per-layer
            es_leaf = 0.6108 * math.exp(17.27 * T_air / (T_air + 237.3))
            D = max(0.01, es_leaf - ea)

            gs_i = stomatal_conductance(A_i, D, self.crop, is_night)
            self.gs[i] = gs_i

            es_leaf = 0.6108 * math.exp(17.27 * T_air / (T_air + 237.3))
            VPD_layer = max(0.01, es_leaf - ea)
            T_vol_i = transpiration_rate(gs_i, wind=self.wind_layer[i],
                                          VPD=VPD_layer, is_night=is_night)
            total_A += A_i * self.dLAI[i]
            total_gs += gs_i * self.dLAI[i]
            total_transp += T_vol_i * self.dLAI[i]

        return total_A, total_gs, total_transp

    # ─────────────────────────────────────────────────────────────────
    # §3.5  Two-chamber water model
    # ─────────────────────────────────────────────────────────────────

    def step_two_chamber_water(self, i, C_air, dt, T_vol, C_xylem=0.0):
        """Update two-chamber TFWT for layer i (§3.5.8, + xylem source).

        Args:
            i: layer index
            C_air: atmospheric HTO [Bq/L]
            dt: time step [s]
            T_vol: transpiration rate [m/s]
            C_xylem: xylem water HTO [Bq/L] from soil pathway (v3.2)
        """
        dLAI = self.dLAI[i]
        if dLAI < 1e-6:
            return

        V_water = cfg.HV * dLAI  # m³/m²
        if V_water < 1e-30:
            return

        C_fast = self.WHTO_fast[i] / (V_water * cfg.RHO_W)
        C_slow = self.WHTO_slow[i] / (V_water * cfg.RHO_W)

        # Step 1: fast chamber (analytical solution)
        k_stom_eff = T_vol * dLAI / V_water  # 1/s
        k_fast_total = k_stom_eff + cfg.K_12

        if C_air > 0:
            k_stom = T_vol * cfg.ALPHA_CG * dLAI / V_water
            C_fast_ss = (k_stom * C_air / cfg.ALPHA_CG + cfg.K_12 * C_slow) / (k_stom + cfg.K_12)
        else:
            C_fast_ss = 0.0

        C_fast_new = C_fast_ss + (C_fast - C_fast_ss) * math.exp(-k_fast_total * dt)
        C_fast_new = max(cfg.CANOPY_TFWT_FLOOR, C_fast_new)

        # Step 2: slow chamber (semi-implicit Euler)
        # + xylem source term — xylem water enters slow chamber during transpiration
        # Physical: transpiration stream carries soil-derived HTO into leaf bulk water.
        # Only activate xylem coupling when soil HTO is present (C_xylem > threshold).
        # This avoids perturbing the calibrated atmospheric pathway (PE film mode).
        k_slow_loss = 1.0 / (cfg.TAU_SLOW_LOSS * 3600.0)
        if C_xylem > 0.01:  # Bq/L threshold — couple when soil HTO is present
            k_xylem = cfg.XYLEM_TO_SLOW
            C_slow_new = (C_slow + dt * (cfg.K_12 * C_fast_new + k_xylem * C_xylem)) / \
                         (1.0 + (cfg.K_12 + k_xylem + k_slow_loss) * dt)
        else:
            C_slow_new = (C_slow + cfg.K_12 * dt * C_fast_new) / \
                         (1.0 + (cfg.K_12 + k_slow_loss) * dt)
        C_slow_new = max(cfg.CANOPY_TFWT_FLOOR, C_slow_new)

        # Step 3: update inventory
        self.WHTO_fast[i] = C_fast_new * V_water * cfg.RHO_W
        self.WHTO_slow[i] = C_slow_new * V_water * cfg.RHO_W

        # Output
        self.TFWT[i] = C_fast_new
        self._TFWT_total[i] = cfg.FV * C_fast_new + (1.0 - cfg.FV) * C_slow_new
        self._C_slow_local[i] = C_slow_new

    # ─────────────────────────────────────────────────────────────────
    # §3.5  Single-chamber leaf water model
    # ─────────────────────────────────────────────────────────────────

    def step_single_chamber_water(self, i, C_air, dt, T_vol, C_xylem=0.0,
                                  is_night=False):
        """Update single-chamber TFWT for layer i (well-mixed leaf water).

        Replaces two-chamber model. Physical basis:
        - Leaf water is a well-mixed pool (all major tritium models use this)
        - Input: stomatal HTO uptake from atmosphere + xylem HTO from soil
        - Loss: transpiration flushes HTO out
        - Steady state: TFWT_ss = max(C_air/ALPHA_CG, C_xylem) (two pathways)
        - Decay: τ = TAU_LEAF (day) / TAU_LEAF_NIGHT (night)
        - Night: stomata ~closed, only cuticular loss → τ much longer

        Args:
            i: layer index
            C_air: atmospheric HTO [Bq/L]
            dt: time step [s]
            T_vol: transpiration rate [m/s]
            C_xylem: soil pathway HTO via root uptake [Bq/L] (0 = no soil input)
            is_night: nighttime flag (slower leaf water turnover)
        """
        dLAI = self.dLAI[i]
        if dLAI < 1e-6:
            return

        # Leaf water turnover: day vs night
        # Day: τ=2h (transpiration-driven, matches Diabaté + Brudenell 1997)
        # Night: τ=8h (stomata closed, only cuticular loss + slow diffusion)
        tau = cfg.TAU_LEAF_NIGHT if is_night else cfg.TAU_LEAF
        k_loss = 1.0 / (tau * 3600.0)  # 1/s

        # Two pathways feed leaf water:
        # 1. Atmospheric: stomatal gas exchange → C_air / ALPHA_CG (Craig-Gordon)
        # 2. Soil: root uptake → xylem → transpiration stream → C_xylem
        # Use MAX (not sum) — they represent competing sources to the same pool.
        target_atmo = C_air / cfg.ALPHA_CG if C_air > 0 else 0.0
        target_soil = C_xylem  # direct liquid transport, no fractionation
        target = max(target_atmo, target_soil)

        # Analytical solution: exponential approach to target
        self.TFWT[i] = target + (self.TFWT[i] - target) * math.exp(-k_loss * dt)
        self.TFWT[i] = max(0.0, self.TFWT[i])

        # Update _TFWT_total for compatibility (single chamber: all water is "fast")
        self._TFWT_total[i] = self.TFWT[i]
        self._C_slow_local[i] = self.TFWT[i]

    # ─────────────────────────────────────────────────────────────────
    # v5  Carbon Flow + OBT Formation
    # ─────────────────────────────────────────────────────────────────

    def step_carbon_flow(self, i, dt, is_night, A_umol, obt_signal=0.0,
                         C_air_local=0.0, is_exposed=False):
        """Carbon flux + OBT formation for leaf layer i.

        v45 changes from v44:
        - Night fast HTO metabolism (NU_FAST_LEAF_NIGHT) for night exposure
        - OBT_exch dynamic exchange (K_OBT_EXCH) replaces instantaneous equilibrium
        - OBT_str decay: leaf-only (K_PROT_TURN + OBT_RESP_DECAY_LEAF)
        - Maintenance respiration OBT release (Ota Eq.16, unchanged)

        Returns:
            (dW_photo, dOBT_photo): carbon added [kg C/m²] and OBT produced [Bq/m²]
        """
        dt_h = dt / 3600.0
        dW_photo = 0.0
        dOBT_photo = 0.0

        # reset released OBT tracker for this step
        self._OBT_released[i] = 0.0

        # --- Carbon input from photosynthesis ---
        if A_umol > 0 and not is_night:
            A_leaf = A_umol * 1e-6  # mol/m²/s
            dW = (1.0 / 6.0) * cfg.MD * A_leaf * dt  # kg glucose/m²
            dW_photo = dW
            self.W_suc[i] += dW

        # --- OBT formation ---
        tfwt_local = self._TFWT_total[i]  # Bq/L
        if tfwt_local > 0 and self.W_str[i] > 1e-20:

            # 1. Photo OBT: SOLVEG formula (daytime photosynthesis)
            dOBT_photo_total = 0.0
            if A_umol > 0 and not is_night:
                A_mol = A_umol * 1e-6
                dOBT_photo_total = (cfg.K_photo
                                    * (tfwt_local / cfg.RHO_W)
                                    * cfg.MW
                                    * cfg.F_AN
                                    * A_mol
                                    * dt)

            # 2. Night fast HTO metabolism (v45 NEW)
            # Night exposure: no photosynthesis, but HTO enters leaf water
            # and is rapidly metabolized into organic matter
            dOBT_night_fast = 0.0
            if is_night and is_exposed and tfwt_local > 0:
                dOBT_night_fast = cfg.NU_FAST_LEAF_NIGHT * tfwt_local * dt_h

            # 3. Dark reaction OBT (post-exposure metabolic turnover)
            dOBT_dark_total = 0.0
            if not is_exposed and tfwt_local > 0:
                dOBT_dark_total = cfg.NU_DARK * tfwt_local * dt_h

            dOBT_total = dOBT_photo_total + dOBT_night_fast + dOBT_dark_total

            if dOBT_total > 0:
                f_prot = cfg.ORGAN_PHYSICS['leaf']['f_prot']
                obt_exch_frac = f_prot * cfg.OBT_EXCH_HYDROGEN_FRAC
                dOBT_exch = dOBT_total * obt_exch_frac
                dOBT_str = dOBT_total - dOBT_exch

                self.OBT_exch[i] += dOBT_exch
                self.OBT_str[i] += dOBT_str

                dOBT_photo = dOBT_str

        # --- OBT_exch dynamic exchange (replaces instantaneous equilibrium) ---
        # Physical: OBT_exch exchanges with TFWT via O-H/N-H/S-H bonds
        # Rate: K_OBT_EXCH = 0.1/h (not instantaneous)
        if tfwt_local > 0:
            f_prot = cfg.ORGAN_PHYSICS['leaf']['f_prot']
            obt_exch_frac = f_prot * cfg.OBT_EXCH_HYDROGEN_FRAC
            OBT_exch_eq = obt_exch_frac * tfwt_local
            k_exch = cfg.K_OBT_EXCH * dt_h
            self.OBT_exch[i] += k_exch * (OBT_exch_eq - self.OBT_exch[i])
            self.OBT_exch[i] = max(0.0, self.OBT_exch[i])
        else:
            # No TFWT → OBT_exch decays toward 0
            k_exch = cfg.K_OBT_EXCH * dt_h
            self.OBT_exch[i] *= (1.0 - k_exch)
            self.OBT_exch[i] = max(0.0, self.OBT_exch[i])

        # --- Maintenance respiration OBT release (Ota Eq.16) ---
        if self.W_str[i] > 1e-20 and self.OBT_str[i] > 0:
            Q10 = cfg.Q10_RESP ** ((25.0 - 25.0) / 10.0)
            R_m = cfg.K_RESP * self.W_str[i] * Q10 * dt_h
            R_m = min(R_m, self.W_suc[i] * 0.5)
            if R_m > 1e-20 and self.W_str[i] > 1e-20:
                obt_conc = self.OBT_str[i]
                dOBT_release = R_m * obt_conc * cfg.F_RELEASE
                self.OBT_str[i] -= dOBT_release / max(self.W_str[i], 1e-20)
                self.OBT_str[i] = max(0.0, self.OBT_str[i])
                # track released OBT for stem/ear redistribution
                self._OBT_released[i] += dOBT_release * cfg.CANOPY_OBT_RELEASE_FRAC

        # --- OBT_str decay (leaf-only, K_PROT_TURN + OBT_RESP_DECAY_LEAF) ---
        # Non-leaf organs use their own k_turn_day from ORGAN_PHYSICS (in organs.py)
        if self.OBT_str[i] > 0:
            k_decay = (cfg.K_PROT_TURN + cfg.OBT_RESP_DECAY_LEAF) * dt_h
            dOBT_turnover = self.OBT_str[i] * k_decay
            self.OBT_str[i] *= (1.0 - k_decay)
            self.OBT_str[i] = max(0.0, self.OBT_str[i])
            # track protein turnover OBT release for stem/ear redistribution
            self._OBT_released[i] += dOBT_turnover * self.W_str[i] * cfg.CANOPY_OBT_RELEASE_FRAC

        return dW_photo, dOBT_photo

    # ─────────────────────────────────────────────────────────────────
    # §3.13  Leaf senescence
    # ─────────────────────────────────────────────────────────────────

    def step_senescence(self, dt, t_hour, t_anthesis, grain_fill_h=1176.0,
                        exp_delay_h=0.0):
        """DVS-driven leaf senescence (natural OBT decay, no K_SEN_DAF).

        Removed K_SEN_DAF artificial decay. DAF non-monotonicity now produced by:
        1. Canopy OBT_str natural decay (K_PROT_TURN + OBT_RESP_DECAY in step_carbon_flow)
        2. Grain receptivity sigmoid
        3. Senescence timing relative to canopy OBT availability
        """
        if t_anthesis is None or t_hour < t_anthesis:
            return 0.0, 0.0, 0.0

        t_span = grain_fill_h
        if t_span <= 0:
            return 0.0, 0.0, 0.0

        # Receptivity sigmoid based on grain developmental stage at exposure
        # exp_delay_h = time from exposure to anthesis (proxy for grain maturity at exposure)
        # Low at early DAF, high at mid-late DAF
        t_frac = min(max(0.0, exp_delay_h) / max(t_span, 1.0), 1.0)
        k_rep = cfg.K_RECEP if hasattr(cfg, 'K_RECEP') else 5.0
        t_mid = cfg.K_RECEP_MID if hasattr(cfg, 'K_RECEP_MID') else 0.20
        import math
        receptivity = 1.0 / (1.0 + math.exp(-k_rep * (t_frac - t_mid)))
        receptivity = max(0.0, min(1.0, receptivity))

        # No K_SEN_DAF — canopy OBT decay is handled naturally by
        # K_PROT_TURN + OBT_RESP_DECAY in step_carbon_flow

        t_frac = min((t_hour - t_anthesis) / t_span, 1.0)
        cumul = (1.0 - cfg.SENESCENCE_REMAIN) * t_frac ** cfg.SENESCENCE_POWER
        new_death = max(cumul - self._prev_sen_cumul, 0.0)
        self._prev_sen_cumul = cumul

        if new_death < 1e-12:
            return 0.0, 0.0, 0.0

        dW_grain_total = 0.0
        dOBT_grain_total = 0.0
        dW_litter_total = 0.0

        for i in range(self.N):
            if self.dLAI[i] < 1e-6:
                continue

            # --- Soluble carbon (suc) → grain (carbon + OBT) ---
            dW_suc_die = self.W_suc[i] * new_death
            dOBT_suc_die = self.OBT_suc[i] * dW_suc_die * cfg.SENESCENCE_OBT_EFF * receptivity
            self.W_suc[i] -= dW_suc_die

            # --- OBT_exch → grain ---
            dOBT_exch_die = self.OBT_exch[i] * new_death * cfg.SENESCENCE_OBT_EFF * receptivity
            self.OBT_exch[i] -= dOBT_exch_die

            # --- Structural carbon (str) → litter ---
            dW_str_die = self.W_str[i] * new_death
            neOBT_str_conc = self._neOBT_inv[i] / max(self.W_str[i] * self.dLAI[i], 1e-20)
            eOBT_str_conc = max(self.OBT_str[i] - neOBT_str_conc, 0.0)
            EBT_EFFICIENCY = 0.125
            dOBT_str_eOBT = eOBT_str_conc * dW_str_die * EBT_EFFICIENCY * cfg.SENESCENCE_OBT_EFF * receptivity
            d_neOBT_die = self._neOBT_inv[i] * new_death
            self._neOBT_inv[i] -= d_neOBT_die
            self.W_str[i] -= dW_str_die

            dW_grain_total += dW_suc_die
            dOBT_grain_total += dOBT_suc_die + dOBT_str_eOBT + dOBT_exch_die
            dW_litter_total += dW_str_die

            dLAI_die = self.dLAI[i] * new_death
            self.dLAI[i] -= dLAI_die

            # Always scale when dLAI changes (even if dLAI is small)
            # This prevents OBT_str concentration from blowing up when leaves die
            scale = self.dLAI[i] / max(self.dLAI[i] + dLAI_die, 1e-20)
            self.W_suc[i] *= scale
            self.W_str[i] *= scale
            self.OBT_exch[i] *= scale
            self.OBT_str[i] *= scale  # scale OBT_str too!

            self._neOBT_inv[i] *= (1.0 - new_death * cfg.F_NEOBT_LITTER)

        if dW_grain_total > 1e-20:
            S_grain = dOBT_grain_total / dW_grain_total
        else:
            S_grain = 0.0

        return dW_grain_total, S_grain, dW_litter_total

    # ─────────────────────────────────────────────────────────────────
    # Utilities
    # ─────────────────────────────────────────────────────────────────

    def mean_tfwt(self):
        """Area-weighted mean TFWT [Bq/L] (two-chamber weighted average)."""
        total = 0.0
        total_lai = 0.0
        for i in range(self.N):
            total += self._TFWT_total[i] * self.dLAI[i]
            total_lai += self.dLAI[i]
        return total / max(total_lai, 1e-6)

    def mean_obt(self):
        """Area-weighted mean total leaf OBT [Bq/kg C]."""
        total_obt = 0.0
        total_c = 0.0
        for i in range(self.N):
            W_tot = self.W_suc[i] + self.W_str[i]
            OBT_tot = self.OBT_suc[i] * self.W_suc[i] + self.OBT_str[i] * self.W_str[i]
            total_obt += OBT_tot
            total_c += W_tot
        return total_obt / max(total_c, 1e-20)

    def get_weighted_suc_obt(self):
        """LAI-weighted mean sucrose pool OBT [Bq/kg C]."""
        total_obt = 0.0
        total_lai = 0.0
        for i in range(self.N):
            total_obt += self.OBT_suc[i] * self.dLAI[i]
            total_lai += self.dLAI[i]
        return total_obt / max(total_lai, 1e-6)

    def get_weighted_exch_obt(self):
        """LAI-weighted mean exchangeable OBT [Bq/kg C]. for phloem loading."""
        total_obt = 0.0
        total_lai = 0.0
        for i in range(self.N):
            total_obt += self.OBT_exch[i] * self.dLAI[i]
            total_lai += self.dLAI[i]
        return total_obt / max(total_lai, 1e-6)

    def get_mean_C_slow(self):
        """Area-weighted mean C_slow [Bq/L]."""
        total = 0.0
        total_lai = 0.0
        for i in range(self.N):
            total += self._C_slow_local[i] * self.dLAI[i]
            total_lai += self.dLAI[i]
        return total / max(total_lai, 1e-6)

    def total_leaf_obt_inventory(self):
        """Total leaf OBT inventory [Bq/m² ground]."""
        total_obt = 0.0
        for i in range(self.N):
            dLAI = self.dLAI[i]
            total_obt += (self.OBT_suc[i] * self.W_suc[i] +
                          self.OBT_str[i] * self.W_str[i]) * dLAI
        return total_obt

    def total_obt_released(self):
        """Total canopy OBT released via protein turnover [Bq/m² ground].

        This HTO is available for stem/ear surface re-absorption.
        Released OBT is tracked per layer, reset each step after redistribution.
        """
        return sum(self._OBT_released[i] for i in range(self.N))

    def total_leaf_C(self):
        """Total leaf carbon [kg C/m² ground]."""
        total = 0.0
        for i in range(self.N):
            total += (self.W_suc[i] + self.W_str[i]) * self.dLAI[i]
        return total

    def leaf_obt_harvest(self):
        """Leaf OBT at harvest [Bq/g dry]. Includes neOBT_inv (primary OBT source)."""
        total_obt = self.total_leaf_obt_inventory()
        ne_obt_inv = sum(self._neOBT_inv[i] for i in range(self.N))
        total_obt_with_ne = total_obt * cfg.FNEX + ne_obt_inv
        total_C = self.total_leaf_C()
        if total_C < 1e-20:
            return 0.0
        g_dry = total_C / 0.4 * 1000
        return total_obt_with_ne / max(g_dry, 1e-20)

    def shrink_leaf_realloc(self, dt, dvs):
        """Carbon reallocation from leaves to organs (OBT removed).

        Physical: leaf碳再分配 ≠ OBT转移。
        碳再分配是碳在器官间的重新分配，OBT应该通过专门的转移路径：
        - senescence → grain（衰老转移，受receptivity调制）
        - ear→grain realloc（穗缓冲转移）
        - stem→grain realloc（茎再分配）
        旧版本在这里把OBT随碳一起转，导致grain OBT在DAF=1就爆表。

        Returns:
            (dW_realloc [kg C/m² ground], S_leaf [Bq/kg C])  — S_leaf = 0 (不转移OBT)
        """
        if dvs < cfg.REALLOC_DVS:
            return 0.0, 0.0

        dt_day = dt / 86400.0
        total_dW = 0.0

        for i in range(self.N):
            # Soluble carbon reallocation
            W_avail_suc = self.W_suc[i] * cfg.REALLOC_LEAF_FRAC
            dW_suc = min(W_avail_suc * cfg.REALLOC_LEAF_RATE * dt_day, W_avail_suc * 0.1)
            dW_suc = min(dW_suc, self.W_suc[i])

            # Structural carbon reallocation
            W_avail_str = self.W_str[i] * cfg.F_STR_RELEASE
            dW_str = min(W_avail_str * cfg.REALLOC_LEAF_RATE * dt_day * 0.5, W_avail_str * 0.05)
            dW_str = min(dW_str, self.W_str[i])

            if dW_suc > 1e-20 or dW_str > 1e-20:
                # Only soluble carbon goes to grain; str carbon stays in litter
                dW_out = dW_suc

                # neOBT stays in leaf
                d_neOBT_str = self._neOBT_inv[i] * (dW_str / max(self.W_str[i], 1e-20)) * 0.5
                self._neOBT_inv[i] -= d_neOBT_str

                self.W_suc[i] -= dW_suc
                self.W_str[i] -= dW_str
                total_dW += dW_out

        # S_leaf = 0 — OBT不通过碳再分配路径转移
        return total_dW, 0.0
