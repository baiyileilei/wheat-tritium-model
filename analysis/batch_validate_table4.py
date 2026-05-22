"""Batch validation: Diabaté Table 4 chamber experiments (2h, different DAF)
Compare model grain OBT with experimental data at harvest.

Table 4 data (normalized to 10,000 Bq/mL leaf HTO at end of 2h exposure).
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from solveg_model_v3 import config as cfg
from solveg_model_v3.model import SolvegModel

TABLE4_DAY = [
    ("W7",   7,  291),
    ("W8",  12,  794),
    ("W7a", 13,  834),
    ("W6",  16,  512),
    ("W8b", 19,  465),
    ("W8a", 27,   76),
    ("W9",  33, 1054),
]

AIR_HTO = 100000.0
NORMALIZE_REF = 10000.0


def run_daf(daf):
    """Run model: pre-anthesis start, anthesis during sim, expose at DAF days."""
    exposure_hours = 2.0
    grain_fill_total_h = cfg.CROPS['wheat'].get('GRAIN_FILL_H', 720.0)
    gdd_anthesis = cfg.CROPS['wheat'].get('GDD_mature', 2500.0) * 0.5

    # Pre-anthesis growth: DAF days before exposure
    pre_anthesis_h = daf * 24.0
    # Post-exposure grain fill
    post_exposure_h = max(0, grain_fill_total_h - daf * 24.0)
    # Total simulation
    sim_hours = pre_anthesis_h + exposure_hours + post_exposure_h + 48.0

    # Start before anthesis. At 25°C, GDD accumulates at 25 °C·h per hour.
    # We need anthesis to occur after pre_anthesis_h hours.
    # startGDD + pre_anthesis_h * 25 = gdd_anthesis
    # startGDD = gdd_anthesis - pre_anthesis_h * 25
    start_gdd = gdd_anthesis - pre_anthesis_h * 25.0
    if start_gdd < 0:
        start_gdd = 0.1  # minimum

    # Exposure at 8:00 AM on the DAF-th day
    # startH sets hour-of-day at t=0. Exposure starts at t=pre_anthesis_h (DAF days)
    # At that moment, hour_of_day = (startH + pre_anthesis_h) % 24
    # We want this to be 8:00 → startH = 8 - (pre_anthesis_h % 24)
    start_h = 8.0 - (pre_anthesis_h % 24.0)

    model, results = SolvegModel.run_diabate(
        airHTO=AIR_HTO,
        expH=exposure_hours,
        expDelay=pre_anthesis_h,  # exposure starts after DAF days of growth
        startH=start_h,
        simH=sim_hours,
        startGDD=start_gdd,
        progress_every=0,
        silent=True,
    )

    harvest = results.get('harvest', {})
    return harvest.get('grain_OBT_Bq_g', 0.0), results.get('peak_TFWT', 0.0)


print("=" * 80)
print("Diabaté Table 4 Chamber Validation (2h, different DAF)")
print("=" * 80)

# Baseline
obt_base, peak = run_daf(12)
print(f"Baseline (DAF=12): grain_OBT={obt_base:.1f}, peak_TFWT={peak:.0f}")
print()

print(f"{'Exp':<6} {'DAF':>4} {'Obs(norm)':>10} {'Obs(Bq/g)':>10} {'Model':>10} {'Ratio':>8} {'Status'}")
print("-" * 80)

for exp_name, daf, obs_norm in TABLE4_DAY:
    model_obt, _ = run_daf(daf)
    obs_abs = obs_norm * (peak / NORMALIZE_REF) * 1.667
    ratio = model_obt / obs_abs if obs_abs > 0 else 0
    status = "✓" if 0.5 <= ratio <= 2.0 else ("~" if 0.25 <= ratio <= 4.0 else "✗")
    print(f"{exp_name:<6} {daf:>4} {obs_norm:>10.0f} {obs_abs:>10.1f} {model_obt:>10.1f} {ratio:>8.2f} {status}")

print(f"\npeak_TFWT = {peak:.0f} Bq/L")
