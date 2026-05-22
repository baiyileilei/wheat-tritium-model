"""SOLVEG-II v43 Model Configuration

v43 rebuild: NU_GROSS → SOLVEG formula (K_photo × TFWT × A_n).
Dead code removed (~25 params deleted). Grain OBT: 2 paths only.
"""
from math import pi

# ═══════════════════════════════════════════════════════════════════════
# §5.1  Physical Constants (never change)
# ═══════════════════════════════════════════════════════════════════════
R_GAS = 8.314
TK0 = 273.15
RHO_AIR = 1.204
CP_AIR = 1005.0
LV = 2.45e6
KAPPA = 0.4
G_GRAV = 9.81
MW = 0.018
RHO_W = 1000.0
MD = 0.180
VM_AIR = 0.0245
CO2_ATM = 420.0

# HTO/OBT constants
ALPHA_CG = 0.91
F_AN = 0.78
FNEX = 0.79
FD_DAY = 0.015
FD_NIGHT = 0.025

# ═══════════════════════════════════════════════════════════════
# §5.x  Xylem-Canopy Coupling
# ═══════════════════════════════════════════════════════════════
XYLEM_TO_SLOW = 1.0 / (2.0 * 3600.0)  # 1/s — τ=2h for xylem→leaf mixing

# ═══════════════════════════════════════════════════════════════
# Organ literature parameters (from published data, NOT calibrated)
# ═══════════════════════════════════════════════════════════════
ORGAN_PHYSICS = {
    'leaf': {
        'f_prot': 0.70,
        'H_per_C': 1.5,
        'k_turn_day': 0.00096,  # /h, t½=30d (Schnyder 1993)
        't_half_d': 30,
    },
    'stem': {
        'f_prot': 0.01,
        'H_per_C': 1.2,
        'k_turn_day': 0.00032,  # t½=90d
        't_half_d': 90,
    },
    'ear': {
        'f_prot': 0.10,
        'H_per_C': 1.3,
        'k_turn_day': 0.00048,  # t½=60d
        't_half_d': 60,
    },
    'grain': {
        'f_prot': 0.10,
        'H_per_C': 1.2,
        'k_turn_day': 0.00014,  # t½=200d (minimal turnover)
        't_half_d': 200,
    },
    'root': {
        'f_prot': 0.15,
        'H_per_C': 1.3,
        'k_turn_day': 0.00064,  # t½=45d
        't_half_d': 45,
    },
}

# Root HTO uptake selectivity (soil pathway)
ROOT_UPTAKE_EFF = 0.5

# PAR
S0_MAX = 500.0
PAR_CONV = 4.57

# ═══════════════════════════════════════════════════════════════════════
# Leaf Water Model (single-chamber, §3.5)
# ═══════════════════════════════════════════════════════════════════════
TAU_LEAF = 2.0        # h — day (transpiration-driven)
TAU_LEAF_NIGHT = 5.0  # h — night (stomata closed, cuticular loss only) (v45: faster night decay)

# Two-chamber water model params (used by step_two_chamber_water)
FV = 0.15
TAU_SLOW = 30.0
K_12 = 1.0 / (TAU_SLOW * 3600)
TAU_SLOW_LOSS = 30.0
CANOPY_TFWT_FLOOR = 0.0

# ═══════════════════════════════════════════════════════════════════════
# Organ TFWT Transport Chain (§3.14)
# ═══════════════════════════════════════════════════════════════════════
TAU_STEM = 30.0
TAU_EAR = 24.0
TAU_CANOPY_TO_GRAIN = 720.0  # grain water HTO retention
GRAIN_TFWT_RISE_POWER = 1.0  # fill_progress scaling exponent
DVS_MATURE = 2.0

# Grain water dynamics
GRAIN_WATER_FRAC_INITIAL = 0.60  # at DVS=1.0
GRAIN_WATER_FRAC_MATURE = 0.14   # at DVS=2.0

# ═══════════════════════════════════════════════════════════════════════
# Carbon Flow Model (two-pool suc+str, sink-strength allocation)
# ═══════════════════════════════════════════════════════════════════════

# Maintenance respiration
K_RESP = 0.015       # /h
Q10_RESP = 2.0

# Sink strength parameters
SINK_K_ROOT = 0.008    # /h
SINK_K_STEM = 0.004    # /h
SINK_K_LEAF = 0.015    # /h
SINK_K_EAR  = 0.003    # /h
SINK_K_GRAIN = 0.04    # /h

# Grain carbon saturation
GRAIN_W_STR_MAX = 0.50  # kg C/m²

# Growth efficiency (suc → str conversion)
Y_GROWTH = 0.80

# ═══════════════════════════════════════════════════════════════════════
# OBT Formation — SOLVEG Formula + Dark Reaction + Resp Release (v44)
# ═══════════════════════════════════════════════════════════════════════
# v44: All OBT from SOLVEG formula (K_photo × TFWT × A_n) for leaves.
# Non-leaf organs get OBT via TFWT transport chain + dark reaction (ν_dark).
# No black-box injection (NU_EXPOSE_* removed).
# Dose response from OBT_exch loss + carbon pool saturation (no dose_factor).
# DAF non-monotonicity from maintenance respiration OBT release.

# SOLVEG formula: OBT_photo = K_photo × (TFWT/ρ_w) × m_w × f_An × A_n × dt
K_photo = 10**10.25  # [Bq·s/mol] — v60 recalibrated for leaf=26

# Dark reaction OBT (post-exposure metabolic turnover, Atarashi-Andoh 2002)
NU_DARK = 0.002  # /h — dark reaction OBT (original value)

# Non-leaf organ HTO surface absorption during exposure (v44)
K_ABSORP_STEM = 5.0   # /h — stem HTO surface absorption rate
K_ABSORP_EAR = 50.0   # /h — ear HTO surface absorption rate (husk, higher SA/V)
K_ABSORP_ROOT = 0.5   # /h — root (minimal, soil pathway dominant)

# Maintenance respiration OBT release (Ota Eq.16, Galeriu IAEA TECDOC)
F_RELEASE = 0.10  # — fraction of respired ³H released as HTO (literature: 0.05-0.20)

# ═══════ v45: Protein turnover (leaf vs non-leaf separation) ═══════
# Leaf: faster turnover (photosynthetic OBT continuously replenishes)
K_PROT_TURN = 0.0028  # /h — v60 recalibrated for leaf=26 (t½≈10.3d)
# Non-leaf organs: use ORGAN_PHYSICS[name]['k_turn_day'] (stem=0.00032, ear=0.00048, grain=0.00014)

# ═══════ v45: OBT_str decay — leaf only ═══════
# Leaf has photosynthetic OBT input → needs decay to prevent infinite accumulation
# Non-leaf organs: NO OBT_RESP_DECAY (their OBT comes from transfer, not photosynthesis)
OBT_RESP_DECAY_LEAF = 0.0005  # /h — leaf-only OBT_str decay (leaf total decay = 0.003+0.0005 = 0.0035/h, t½≈8.3d)

# ═══════ v45: OBT_exch dynamic exchange (replaces instantaneous equilibrium) ═══════
# Physical: OBT_exch exchanges with TFWT via O-H/N-H/S-H bonds
# Rate: K_OBT_EXCH = 0.1/h (not instantaneous!)
# During exposure: OBT_exch can accumulate (not erased by equilibrium)
# After exposure: OBT_exch slowly equilibrates with decaying TFWT
K_OBT_EXCH = 0.1  # /h — OBT_exch ↔ TFWT exchange rate

# OBT_exch/str split: determined by organ protein content (ORGAN_PHYSICS.f_prot)
OBT_EXCH_HYDROGEN_FRAC = 0.25  # fraction of protein H that is exchangeable (N-H, S-H)

# ═══════ v45: Nighttime leaf fast HTO metabolism ═══════
# Night exposure: no photosynthetic OBT, but HTO still enters leaf water
# and is rapidly metabolized into organic matter (faster than dark reaction)
NU_FAST_LEAF_NIGHT = 0.005  # /h — nighttime leaf HTO fast metabolism

# ═══════════════════════════════════════════════════════════════════════
# Grain OBT — 2 Physical Paths (v44)
# ═══════════════════════════════════════════════════════════════════════
# Path A: leaf OBT_str remobilization via phloem (primary)
#   dOBT_grain = K_REMOB × leaf_OBT_str_conc × dW_grain
#   Physical: leaf protein hydrolysis → amino acids → phloem → grain protein.
#   No dose correction — OBT_str naturally decays (protein turnover) → longer
#   exposure means more OBT_str accumulated, with natural saturation.
K_REMOB = 0.000146  # /h — v60 recalibrated: grain=478(480) with snapshot receptivity

# Path B: leaf senescence → grain (secondary)
SENESCENCE_OBT_EFF = 0.30  # transfer efficiency
ENABLE_SENESCENCE_OBT_TRANSFER = True

# Grain receptivity — snapshot at exposure time (v59)
# Receptivity is a FIXED coefficient computed at exposure time from fill_progress.
# fill_progress = grain_fill_gdd / grain_fill_max_gdd at the moment of exposure.
# Bell curve: peak at RECEPTIVITY_PEAK_FP, baseline at fp=0.
# All grain OBT pathways (K_REMOB, senescence, stem→grain, ear→grain) gated.
RECEPTIVITY_PEAK_FP = 0.012   # fill_progress at peak receptivity (DAF≈12)
RECEPTIVITY_SIGMA = 0.008     # bell curve width
RECEPTIVITY_BASELINE = 0.10   # receptivity at fp=0 (Diabaté, exposure at anthesis)
K_RECEP = 15.0     # deprecated: kept for compatibility
K_RECEP_MID = 0.25  # deprecated: kept for compatibility

# Grain OBT turnover (chronic saturation limit)
K_GRAIN_TURN = 0.00027   # /h — t½≈30d

# Ear→grain direct OBT transfer (v46: Galeriu mechanism)
K_EAR_TO_GRAIN = 0.01  # /h — ear tissue OBT → grain (direct absorption path)

# ═══════ v47: OBT_exch fast pool (exposure-period quick formation + post-exposure decay) ═══════
# Physical: during exposure, OBT_exch forms rapidly (t½≈7h via K_OBT_EXCH=0.1/h).
# After exposure, OBT_exch decays via exchange with decaying TFWT.
# This explains leaf OBT peak at 6h then decline (Diabaté Fig.1).
OBT_EXCH_FAST_FRAC = 0.80  # fraction of exposure OBT that goes to OBT_exch (vs OBT_str)

# ═══════ v47: Canopy OBT redistribution to stem/ear ═══════
# Physical: canopy protein turnover releases HTO → boundary layer → stem/ear surface absorption.
# This is the main source of stem/ear OBT (Diabaté: stem=65, ear=45 at t=0h).
CANOPY_OBT_RELEASE_FRAC = 0.30   # fraction of canopy protein turnover that releases HTO
CANOPY_OBT_TO_STEM = 0.00000002  # /h — canopy released OBT → stem surface absorption
CANOPY_OBT_TO_EAR = 0.000022   # /h — canopy released OBT → ear surface absorption (v47: 10×)

# ═══════ v47: Grain age gate for receptivity ═══════
# Physical: grain needs ~24h to build enzyme system (AGPase, SSS, GBSS).
# Before that, it cannot efficiently accept OBT.
GRAIN_AGE_GATE_H = 24.0   # hours — below this, receptivity is suppressed
GRAIN_AGE_GATE_R = 0.01   # receptivity floor during age gate

# ═══════ v47: Stem/ear → grain OBT backflow ═══════
# Physical: late DAF (canopy OBT exhausted) grain OBT comes from stem/ear reserves.
K_STEM_TO_GRAIN = 0.00002  # /h — stem OBT → grain (via phloem re-mobilization)

# ═══════ v47: Ear independent dark metabolism ═══════
# Physical: ear is independent metabolic pump (Diabaté Fig.2: 3× in darkness)
NU_EAR_DARK = 0.003  # /h — ear dark reaction OBT (3× leaf NU_DARK)

# ═══════ v47: Non-leaf OBT_str decay ═══════
# Physical: non-leaf organs have faster OBT turnover than leaf (ds analysis: t½≈2-3d)
OBT_RESP_DECAY_NONLEAF = 0.0002  # /h — stem/ear OBT_str decay (original)

# Exposure-period fast HTO metabolism for non-leaf organs (v45)
# Physical: during exposure, atmospheric HTO directly contacts organ surfaces.
# HTO is rapidly incorporated into organic matter via enzymatic pathways
# (much faster than post-exposure dark reaction NU_DARK=0.002/h).
# This produces the observed stem/ear OBT during the 2h exposure period.
# Diabaté 1997: stem=55, ear=100 Bq/kg C at 2h → requires ~0.005-0.01/h
NU_FAST_STEM = 0.23    # /h — v47 calibrated value
NU_FAST_EAR = 56     # /h — v60 recalibrated for ear=230 (was 48)
NU_FAST_ROOT = 0.001   # /h — root (minimal, soil pathway dominant)

# ═══════════════════════════════════════════════════════════════════════
# Carbon Reallocation (§3.12)
# ═══════════════════════════════════════════════════════════════════════
REALLOC_DVS = 1.5
REALLOC_STEM_FRAC = 0.60
REALLOC_LEAF_FRAC = 0.40
REALLOC_STEM_RATE = 0.03
REALLOC_LEAF_RATE = 0.03
REALLOC_EAR_FRAC = 0.25
REALLOC_EAR_RATE = 0.025
REALLOC_EFF = 0.95

# ═══════════════════════════════════════════════════════════════════════
# Leaf Senescence (§3.13)
# ═══════════════════════════════════════════════════════════════════════
SENESCENCE_POWER = 1.4
SENESCENCE_REMAIN = 0.25
F_STR_RELEASE = 0.30
F_NEOBT_LITTER = 0.90

# ═══════════════════════════════════════════════════════════════════════
# Ear Photosynthesis (§3.15)
# ═══════════════════════════════════════════════════════════════════════
VCMAX_EAR_SCALE = 0.30
F_EAR_PAR = 0.20
EAR_GREEN_AREA = 0.50
G0_EAR = 0.005
G1_EAR = 3.0

# ═══════════════════════════════════════════════════════════════════════
# Leaf Physical / Microenvironment / Soil
# ═══════════════════════════════════════════════════════════════════════
HV = 1.54e-4
LEAF_WATER_FRAC = 0.65
LEAF_C_PER_LAYER = 0.06  # kg C/m² leaf per layer

T_AMP_DEFAULT = 5.0
WIND_AMP_DEFAULT = 0.5
G_AERO = 0.05
CANOPY_HEIGHT = 0.8

E_SOIL_BASE = 4e-7
SOIL_HTO_SINK_FRAC = 0.33  # v42: open soil absorbs 33% airHTO during pulse

LAI_MAX = 6.0
DVS_LAI_PEAK = 1.0

SOIL_PROFILES = {
    'sand': {'theta_R': 0.045, 'theta_S': 0.43, 'alpha': 0.145, 'n': 2.68},
    'loam': {'theta_R': 0.078, 'theta_S': 0.43, 'alpha': 0.036, 'n': 1.56},
    'clay': {'theta_R': 0.068, 'theta_S': 0.38, 'alpha': 0.008, 'n': 1.09},
}
SOIL_N_LAYERS = 6
SOIL_Z_MAX = 0.80
D_WATER = 2.4e-9
D_AIR = 2.4e-5
V_DEP = 0.008

# ═══════════════════════════════════════════════════════════════════════
# WOFOST DVS Partition Table (wheat)
# ═══════════════════════════════════════════════════════════════════════
ORGAN_PARTITION_WHEAT = [
    [0.00,  0.45,  0.10,  0.45,  0.00,  0.00],
    [0.20,  0.35,  0.20,  0.45,  0.00,  0.00],
    [0.40,  0.20,  0.30,  0.50,  0.00,  0.00],
    [0.60,  0.15,  0.30,  0.50,  0.00,  0.05],
    [0.80,  0.12,  0.28,  0.48,  0.00,  0.12],
    [1.00,  0.10,  0.28,  0.45,  0.05,  0.12],
    [1.20,  0.08,  0.20,  0.20,  0.40,  0.12],
    [1.50,  0.05,  0.08,  0.05,  0.72,  0.10],
    [1.80,  0.05,  0.04,  0.00,  0.82,  0.09],
    [2.00,  0.05,  0.04,  0.00,  0.82,  0.09],
]

# ═══════════════════════════════════════════════════════════════════════
# Literature Parameters (wheat C3)
# ═══════════════════════════════════════════════════════════════════════
CROP_PARAMS_WHEAT = {
    'C4': False,
    'Vcmax25': 60.0, 'Jmax25': 120.0, 'Rd25': 1.0, 'TPU25': 18.0,
    'HaV': 65330.0, 'HdV': 200000.0, 'Sv': 650.0,
    'HaJ': 43540.0, 'HdJ': 200000.0, 'Sj': 640.0,
    'HaRd': 46390.0,
    'g0': 0.01, 'g1': 5.5,
    'g0_night': 0.024,
    'Tbase': 0.0,
    'GDD_mature': 2500.0,
    'GRAIN_FILL_H': 1200.0,  # real hours — grain fill period (anthesis→harvest), ~50 days at 25°C
}

# ═══════════════════════════════════════════════════════════════════════
# GDD-based developmental timeline (v58: "scenario passes through model")
# ═══════════════════════════════════════════════════════════════════════
# Model internal clock is GDD-driven. Developmental events trigger at fixed
# GDD thresholds. Scenarios inject exposure at the correct GDD point.
# At 25°C: 1 GDD ≈ 1 real hour. At other temperatures, real hours stretch/compress.
GDD_ANTHESIS = 1250.0    # GDD from seed to anthesis (DVS=1.0)
GDD_GRAIN_FILL_START = GDD_ANTHESIS  # grain fill starts at anthesis
GDD_GRAIN_FILL_DURATION = 1200.0     # GDD for grain fill period (≈50d at 25°C)
GDD_GRAIN_FILL_END = GDD_GRAIN_FILL_START + GDD_GRAIN_FILL_DURATION  # =2450

CROPS = {'wheat': CROP_PARAMS_WHEAT}

# ═══════════════════════════════════════════════════════════════════════
# Scenarios
# ═══════════════════════════════════════════════════════════════════════
DIABATE_SCENARIO = {
    'crop': 'wheat',
    'airHTO': 79000.0,
    'expH': 2.0,
    'startH': 8.0,
    'Tair': 25.0,
    'RH': 0.65,
    'wind': 2.0,
    'LAI': 5.0,
    'height': 0.8,
    'soilType': 'loam',
    'theta0': 0.30,
    'simH': 1201.0,  # v60: will be computed from GDD, this is fallback for constant-T scenarios
    'lat': 50.0,
    'doy': 150,
    'nLayers': 5,
    'dt': 60,
    'startGDD': 1250.0,  # v58: start at anthesis (GDD_ANTHESIS)
    'soil_covered': True,
}

SOIL_EXPOSURE_SCENARIO = {
    'crop': 'wheat', 'airHTO': 0.0, 'expH': 0.0, 'startH': 8.0,
    'Tair': 25.0, 'RH': 0.65, 'wind': 2.0, 'LAI': 5.0, 'height': 0.8,
    'soilType': 'loam', 'theta0': 0.30, 'simH': 720.0,
    'lat': 50.0, 'doy': 150, 'nLayers': 5, 'dt': 60,
    'startGDD': 1500.0, 'soil_covered': False,
    'soil_HTO_input': 10000.0, 'irrigation_rate': 0.001,
}

MID_EXPOSURE_SCENARIO = {
    'crop': 'wheat', 'airHTO': 10000.0, 'expH': 48.0, 'startH': 8.0,
    'Tair': 25.0, 'RH': 0.65, 'wind': 2.0, 'LAI': 5.0, 'height': 0.8,
    'soilType': 'loam', 'theta0': 0.30, 'simH': 1200.0,
    'lat': 50.0, 'doy': 150, 'nLayers': 5, 'dt': 60,
    'startGDD': 1500.0, 'soil_covered': True,
}

CHRONIC_SCENARIO = {
    'crop': 'wheat', 'airHTO': 100.0, 'expH': 2400.0, 'startH': 8.0,
    'Tair': 25.0, 'RH': 0.65, 'wind': 2.0, 'LAI': 5.0, 'height': 0.8,
    'soilType': 'loam', 'theta0': 0.30, 'simH': 2400.0,
    'lat': 50.0, 'doy': 150, 'nLayers': 5, 'dt': 60,
    'startGDD': 1500.0, 'soil_covered': False,
}

DIABATE_SOIL_SCENARIO = dict(DIABATE_SCENARIO, soil_covered=False)
DIABATE_NIGHT_SCENARIO = dict(DIABATE_SCENARIO, startH=22.0)

SOIL_ACUTE_SCENARIO = {
    'crop': 'wheat', 'airHTO': 0.0, 'expH': 0.0, 'startH': 8.0,
    'Tair': 25.0, 'RH': 0.65, 'wind': 2.0, 'LAI': 5.0, 'height': 0.8,
    'soilType': 'loam', 'theta0': 0.30, 'simH': 720.0,
    'lat': 50.0, 'doy': 150, 'nLayers': 5, 'dt': 60,
    'startGDD': 1500.0, 'soil_covered': False,
    'soil_HTO_input': 100000.0, 'irrigation_rate': 0.01,
}

DUAL_ACUTE_SCENARIO = dict(DIABATE_SCENARIO,
    soil_covered=False, soil_HTO_input=79000.0, irrigation_rate=0.01)

SOIL_MID_SCENARIO = {
    'crop': 'wheat', 'airHTO': 0.0, 'expH': 0.0, 'startH': 8.0,
    'Tair': 25.0, 'RH': 0.65, 'wind': 2.0, 'LAI': 5.0, 'height': 0.8,
    'soilType': 'loam', 'theta0': 0.30, 'simH': 720.0,
    'lat': 50.0, 'doy': 150, 'nLayers': 5, 'dt': 60,
    'startGDD': 1500.0, 'soil_covered': False,
    'soil_HTO_input': 10000.0, 'irrigation_rate': 0.005,
}

DUAL_MID_SCENARIO = dict(MID_EXPOSURE_SCENARIO,
    soil_covered=False, soil_HTO_input=10000.0, irrigation_rate=0.005)

SOIL_CHRONIC_SCENARIO = {
    'crop': 'wheat', 'airHTO': 0.0, 'expH': 0.0, 'startH': 8.0,
    'Tair': 25.0, 'RH': 0.65, 'wind': 2.0, 'LAI': 5.0, 'height': 0.8,
    'soilType': 'loam', 'theta0': 0.30, 'simH': 2400.0,
    'lat': 50.0, 'doy': 150, 'nLayers': 5, 'dt': 60,
    'startGDD': 1500.0, 'soil_covered': False,
    'soil_HTO_input': 100.0, 'irrigation_rate': 0.003,
}

DUAL_CHRONIC_SCENARIO = dict(CHRONIC_SCENARIO,
    soil_covered=False, soil_HTO_input=100.0, irrigation_rate=0.003)

SCENARIOS = {
    'diabate': DIABATE_SCENARIO,
    'diabate_soil': DIABATE_SOIL_SCENARIO,
    'diabate_night': DIABATE_NIGHT_SCENARIO,
    'soil_exposure': SOIL_EXPOSURE_SCENARIO,
    'mid_exposure': MID_EXPOSURE_SCENARIO,
    'chronic': CHRONIC_SCENARIO,
    'soil_acute': SOIL_ACUTE_SCENARIO,
    'dual_acute': DUAL_ACUTE_SCENARIO,
    'soil_mid': SOIL_MID_SCENARIO,
    'dual_mid': DUAL_MID_SCENARIO,
    'soil_chronic': SOIL_CHRONIC_SCENARIO,
    'dual_chronic': DUAL_CHRONIC_SCENARIO,
}

# ═══════════════════════════════════════════════════════════════════════
# DAF Scenarios (DVS-triggered exposure)
# ═══════════════════════════════════════════════════════════════════════
def _make_daf_scenario(daf, Tair=25.0, Tbase=0.0, GDD_mature=2500.0):
    """Create a DAF scenario: exposure at DAF days after flowering.

    v58: Fixed timeline approach.
    - Model starts pre-anthesis (GDD=900, DVS≈0.72)
    - Grain fill triggers naturally when DVS reaches 1.0 (anthesis)
    - DAF is real days: 1 DAF = 24 real hours
    - Exposure starts when DVS reaches threshold (matching old behavior)
    - Grain fill: 1200 real hours (fixed)
    """
    gdd_anthesis = GDD_mature * 0.5  # =1250
    # DVS at exposure: anthesis + DAF worth of GDD
    gdd_per_day = max(0.0, Tair - Tbase)
    dvs_at_daf = 1.0 + (daf * gdd_per_day) / (GDD_mature - gdd_anthesis)

    # Simulation duration: enough for pre-anthesis + grain fill + buffer
    start_gdd = gdd_anthesis * 0.6  # =900, pre-anthesis
    days_to_anthesis = (gdd_anthesis - start_gdd) / gdd_per_day
    sim_h = (days_to_anthesis * 24.0) + 1200.0 + 100.0  # pre-fill + grain fill + buffer

    def _constant_weather(t):
        return {
            'Tair': Tair, 'RH': 0.65, 'wind': 2.0,
            'PAR': 300.0, 'sinBeta': 0.5,
            'ea': 0.65 * 3.17, 'es': 3.17,
            'isNight': False,
        }

    return {
        'crop': 'wheat', 'airHTO': 79000.0, 'expH': 2.0, 'startH': 8.0,
        'Tair': Tair, 'RH': 0.65, 'wind': 2.0, 'LAI': 5.0, 'height': 0.8,
        'soilType': 'loam', 'theta0': 0.30, 'simH': sim_h,
        'lat': 50.0, 'doy': 150, 'nLayers': 5, 'dt': 60,
        'startGDD': start_gdd,  # pre-anthesis
        'soil_covered': True,
        'exp_start_DVS': dvs_at_daf,  # DVS-triggered exposure
        'weather_fn': _constant_weather,
        'GRAIN_FILL_H': 1200.0,
    }

DAF_SCENARIOS = {}
for _daf in [1, 6, 7, 12, 13, 21, 27, 33]:
    DAF_SCENARIOS[f'daf_{_daf}'] = _make_daf_scenario(_daf)

SCENARIOS.update(DAF_SCENARIOS)

# ═══════════════════════════════════════════════════════════════════════
# Diabaté 1997 Short-Term Validation Data
# ═══════════════════════════════════════════════════════════════════════
DIABATE_SHORT_TERM = {
    'day': {
        'exposure_h': 2.0,
        'airHTO_Bq_L': 79000.0,
        'times_h': [0, 1, 2, 24],
        'leaf_hto': [86600, 66900, 52100, 4680],
        'stem_hto': [15700, None, 13000, 1590],
        'ear_hto':  [26100, None, 30200, 7420],
        'leaf_obt': [340, None, 335, 190],
        'stem_obt': [65, None, 55, 31],
        'ear_obt':  [45, None, 100, 460],
        'harvest_d': 37,
        'harvest': {'leaf': 26, 'stem': 6.3, 'ear': 230, 'grain': 480},
        'leaf_obt_pct': 1.25,
        'tli_pct': 0.25,
    },
    'night': {
        'exposure_h': 2.0,
        'airHTO_Bq_L': 79000.0,
        'times_h': [0, 1, 2, 24],
        'leaf_hto': [67400, 71100, 56600, None],
        'stem_hto': [None, 8760, 7760, 1360],
        'ear_hto':  [36300, 31000, None, 9000],
        'leaf_obt': [78, 106, 63, 175],
        'stem_obt': [14, 11, 13, 29],
        'ear_obt':  [62, 64, 32, 243],
        'harvest_d': 30,
        'harvest': {'leaf': 214, 'ear': 214, 'grain': 268},
    },
}
