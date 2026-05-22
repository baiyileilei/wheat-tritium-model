"""小麦氚迁移模型 — Soil HTO Module (§8)

Van Genuchten soil hydraulic model with multilayer HTO convection-diffusion.
- 6 layers, 0-80 cm
- Millington-Quirk effective diffusion
- Root water uptake (exponential profile)
- Soil surface evaporation (from met conditions)
- Irrigation input
- PE film mode: all fluxes zero (Diabaté laboratory)
"""
import math
import numpy as np
from . import config as cfg


class SoilModel:
    """Multilayer soil HTO transport (§8)."""

    def __init__(self, soil_type='loam', theta0=0.30,
                 n_layers=None, z_max=None):
        prof = cfg.SOIL_PROFILES.get(soil_type, cfg.SOIL_PROFILES['loam'])
        self.theta_R = prof['theta_R']
        self.theta_S = prof['theta_S']
        self.alpha_vg = prof['alpha']
        self.n_vg = prof['n']
        self.m_vg = 1.0 - 1.0 / self.n_vg

        self.n = n_layers or cfg.SOIL_N_LAYERS
        self.z_max = z_max or cfg.SOIL_Z_MAX
        self.dz = self.z_max / self.n

        self.covered = True  # PE film mode (default)

        # State arrays
        self.theta = np.full(self.n, theta0)   # volumetric water content [-]
        self.C = np.zeros(self.n)               # HTO concentration [Bq/L]

        # Root uptake profile (exponential decay with depth)
        z_mid = np.array([(i + 0.5) * self.dz for i in range(self.n)])
        f = np.exp(-3.0 * z_mid / self.z_max)
        self._root_frac = f / max(np.sum(f), 1e-10)

    # ─── Effective diffusion (Millington-Quirk) ───

    def _D_eff(self, i):
        """Effective HTO diffusion coefficient for layer i [m²/s]."""
        th = self.theta[i]
        phi = self.theta_S
        # Liquid phase diffusion
        Dl = cfg.D_WATER * th ** (10.0 / 3.0) / max(phi ** 2, 1e-10)
        # Vapor phase diffusion (air-filled porosity)
        air_por = max(0.0, phi - th)
        Dv = cfg.D_AIR * air_por ** (10.0 / 3.0) / max(phi ** 2, 1e-10)
        return Dl + Dv

    # ─── Evaporation flux from soil surface ───

    def evap_flux(self):
        """Current HTO evaporation flux [Bq/m²/s]."""
        if self.covered:
            return 0.0
        return self._E_soil * self.C[0]

    # ─── Main step ───

    def step(self, dt, C_air, E_soil, T_transp,
             C_irrigation=0.0, irrig_rate=0.0):
        """
        Single time step.

        Args:
            dt: time step [s]
            C_air: ambient HTO [Bq/L]
            E_soil: soil surface evaporation rate [m/s]
            T_transp: total plant transpiration [m/s] (canopy-summed)
            C_irrigation: irrigation water HTO [Bq/L]
            irrig_rate: irrigation rate [m/s]

        Returns:
            (evap_flux [Bq/m²/s], root_C [Bq/L])
        """
        if self.covered:
            self.C[:] = 0.0
            self._E_soil = 0.0
            return 0.0, 0.0

        self._E_soil = E_soil
        dt_s = dt

        # ─── 1. Irrigation (surface layer) ───
        if irrig_rate > 0 and C_irrigation > 0:
            V_add = irrig_rate * dt_s  # m³/m² added to surface
            V_old = self.dz * max(self.theta[0], 1e-10)
            self.theta[0] += V_add / self.dz
            self.theta[0] = min(self.theta[0], self.theta_S)
            V_new = self.dz * self.theta[0]
            if V_new > 1e-20:
                self.C[0] = (self.C[0] * V_old + C_irrigation * V_add) / V_new

        # ─── 2. Water balance ───
        for i in range(self.n):
            dth = 0.0
            if i == 0:
                dth -= E_soil * dt_s / self.dz
            dth -= self._root_frac[i] * T_transp * dt_s / self.dz
            self.theta[i] = np.clip(self.theta[i] + dth,
                                     self.theta_R, self.theta_S)

        # ─── 3. HTO convection-diffusion ───
        C_new = self.C.copy()
        for i in range(self.n):
            V = self.dz * self.theta[i]
            if V < 1e-20:
                continue

            flux = 0.0

            # Diffusion from above
            if i > 0:
                D = 0.5 * (self._D_eff(i) + self._D_eff(i - 1))
                flux += D * (self.C[i - 1] - self.C[i]) / self.dz ** 2

            # Diffusion from below
            if i < self.n - 1:
                D = 0.5 * (self._D_eff(i) + self._D_eff(i + 1))
                flux -= D * (self.C[i] - self.C[i + 1]) / self.dz ** 2

            # Root uptake (water extraction carries HTO)
            flux -= self._root_frac[i] * T_transp * self.C[i] / V

            # Surface boundary
            if i == 0:
                # Atmospheric vapor exchange: soil surface HTO equilibrates with
                # ambient air HTO moisture via soil pore diffusion.
                # Rate reflects tortuous diffusion path in soil pores (~2h half-life).
                k_exch = 0.0001  # 1/s (~2h half-life)
                flux += k_exch * (C_air - self.C[0])
                # Evaporation loss (removes HTO with evaporating water)
                flux -= E_soil * self.C[0] / self.dz

            C_new[i] += flux * dt_s
            C_new[i] = max(0.0, C_new[i])

        self.C = C_new

        # ─── 4. Return values ───
        evap = E_soil * self.C[0] if E_soil > 0 else 0.0
        root_C = float(np.sum(self._root_frac * self.C))

        return evap, root_C
