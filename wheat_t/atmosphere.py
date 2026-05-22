"""SOLVEG-II Atmosphere Module — complete diurnal model.

Features:
  - Latitude-based day length (Campbell & Norman 1998)
  - Solar elevation for Beer-Law extinction
  - Asymmetric diurnal temperature (min~05:00, max~14:00)
  - PAR with clear-sky sinusoidal + elevation correction
  - Wind diurnal variation
  - RH conserving absolute humidity
"""
import math
from . import config as cfg


def e_sat(T):
    """Saturation vapor pressure [kPa] (Tetens 1930)."""
    T = max(-40.0, min(60.0, T))
    return 0.6108 * math.exp(17.27 * T / (T + 237.3))


def _solar_geometry(hour, lat, doy):
    """Solar declination, hour angle, sin(elevation)."""
    dec = 23.45 * math.sin(math.radians(360 * (284 + doy) / 365))
    lat_r = math.radians(lat)
    dec_r = math.radians(dec)
    omega = math.radians(15 * (hour - 12))
    sin_beta = (math.sin(lat_r) * math.sin(dec_r) +
                math.cos(lat_r) * math.cos(dec_r) * math.cos(omega))
    return max(0.0, sin_beta)


def _day_length(lat, doy):
    """Sunrise and sunset hours."""
    dec = 23.45 * math.sin(math.radians(360 * (284 + doy) / 365))
    lat_r = math.radians(lat)
    dec_r = math.radians(dec)
    cos_w = -math.tan(lat_r) * math.tan(dec_r)
    cos_w = max(-1.0, min(1.0, cos_w))
    half_day = math.degrees(math.acos(cos_w)) / 15
    return 12 - half_day, 12 + half_day


def solar_radiation(hour, lat, doy):
    """PAR [µmol/m²/s] with sinusoidal diurnal + elevation correction."""
    sunrise, sunset = _day_length(lat, doy)
    if hour < sunrise or hour > sunset:
        return 0.0
    frac = (hour - sunrise) / (sunset - sunrise)
    S0 = cfg.S0_MAX * math.sin(math.pi * frac)
    sin_beta = _solar_geometry(hour, lat, doy)
    return S0 * sin_beta * cfg.PAR_CONV


def air_temperature(hour, Tmean, Tamp=None):
    """Diurnal temperature [°C], minimum ~05:00, maximum ~14:00."""
    if Tamp is None:
        Tamp = cfg.T_AMP_DEFAULT
    # Asymmetric: Tmin at 05:00, Tmax at 14:00
    omega = 2 * math.pi * (hour - 14) / 24
    return Tmean - Tamp * 0.5 * math.cos(omega)


def wind_speed(hour, wind_mean, wind_amp=None):
    """Diurnal wind speed [m/s]."""
    if wind_amp is None:
        wind_amp = cfg.WIND_AMP_DEFAULT
    omega = 2 * math.pi * (hour - 14) / 24
    return max(0.1, wind_mean - wind_amp * 0.5 * math.cos(omega))


def relative_humidity(hour, RH_mean, Tmean, Tamp=None):
    """Diurnal RH, conserving absolute humidity."""
    if Tamp is None:
        Tamp = cfg.T_AMP_DEFAULT
    T = air_temperature(hour, Tmean, Tamp)
    es_T = e_sat(T)
    es_mean = e_sat(Tmean)
    return min(1.0, max(0.1, RH_mean * es_mean / max(es_T, 0.01)))


def atmosphere_state(hour, Tmean, RH_mean, wind_mean, lat, doy, Tamp=None):
    """Full atmospheric state at given hour.

    Returns dict: Tair, RH, wind, PAR, sinBeta, ea, es, isNight
    """
    if Tamp is None:
        Tamp = cfg.T_AMP_DEFAULT

    T = air_temperature(hour, Tmean, Tamp)
    RH = relative_humidity(hour, RH_mean, Tmean, Tamp)
    w = wind_speed(hour, wind_mean)
    PAR = solar_radiation(hour, lat, doy)
    sin_beta = _solar_geometry(hour, lat, doy)
    es = e_sat(T)
    ea = RH * es

    return {
        'Tair': T,
        'RH': RH,
        'wind': w,
        'PAR': PAR,
        'sinBeta': sin_beta,
        'ea': ea,
        'es': es,
        'isNight': PAR < 10,
    }


# ═══════════════════════════════════════════════════════════════════════
# §20.1  Soil evaporation from meteorological conditions
# ═══════════════════════════════════════════════════════════════════════

def soil_evaporation(T_air, ea, wind, theta, theta_sat, theta_R, covered=False):
    """Soil surface evaporation rate [m/s].

    Depends on VPD, wind, and surface moisture.
    PE film mode returns 0.
    """
    if covered:
        return 0.0

    es = e_sat(T_air)
    VPD = max(0.0, es - ea)
    if VPD < 0.01:
        return 0.0

    g_base = cfg.E_SOIL_BASE
    theta_fc = theta_sat * 0.6
    moisture = max(0.0, min(1.0, (theta - theta_R) / max(theta_fc - theta_R, 0.01)))
    wind_f = max(0.3, min(2.0, math.sqrt(max(0.1, wind) / 2.0)))

    E = g_base * moisture * wind_f * VPD / (es + ea)
    return max(0.0, E)


# ═══════════════════════════════════════════════════════════════════════
# §20.3  Aerodynamic conductance from wind/canopy
# ═══════════════════════════════════════════════════════════════════════

def aero_conductance(wind, h_canopy, z_ref=2.0):
    """Canopy aerodynamic conductance [m/s] from log wind profile."""
    if h_canopy < 0.01 or wind < 0.01:
        return cfg.G_AERO

    kappa = 0.4
    d = 0.67 * h_canopy
    z0m = 0.1 * h_canopy
    z0h = 0.1 * z0m

    z_eff = max(z_ref - d, z0m * 2)
    num = kappa ** 2 * wind
    den = math.log(z_eff / z0m) * math.log(z_eff / z0h)

    return max(0.01, num / max(den, 0.01))


# ═══════════════════════════════════════════════════════════════════════
# §20.2  LAI dynamic from DVS
# ═══════════════════════════════════════════════════════════════════════

def lai_dynamic(dvs, LAI_max=None, dvs_peak=None):
    """LAI [m²/m²] as function of DVS. S-curve rise + linear decline."""
    LAI_max = LAI_max or cfg.LAI_MAX
    dvs_peak = dvs_peak or cfg.DVS_LAI_PEAK

    if dvs <= 0:
        return 0.1
    if dvs <= dvs_peak:
        t = dvs / dvs_peak
        return LAI_max * t ** 1.5 * math.exp(1.0 - t ** 1.5)
    else:
        t = (dvs - dvs_peak) / max(2.0 - dvs_peak, 0.1)
        return max(0.1, LAI_max * (1.0 - 0.6 * t))


# ═══════════════════════════════════════════════════════════════════════
# §19.1  Weather series (multi-day with real hourly data)
# ═══════════════════════════════════════════════════════════════════════

class WeatherSeries:
    """Hourly weather time series for chronic scenarios."""

    def __init__(self, records):
        """records: list of dicts with Tair, ea, es, wind, PAR, sinBeta, isNight"""
        self.records = records

    @classmethod
    def from_daily(cls, T_daily, RH_daily, wind_daily, lat, doy_start, n_days):
        """Generate hourly weather from daily mean values."""
        records = []
        for day in range(n_days):
            doy = doy_start + day
            for hour in range(24):
                atm = atmosphere_state(hour, T_daily[day], RH_daily[day],
                                       wind_daily[day], lat, doy)
                records.append(atm)
        return cls(records)

    def __call__(self, t):
        """Return atmospheric state at time t [h]."""
        idx = int(t) % len(self.records)
        return self.records[idx]
