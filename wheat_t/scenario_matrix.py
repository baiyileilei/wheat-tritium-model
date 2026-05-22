"""Scenario matrix — one-shot validation of all key metrics.

Usage:
    cd projects && python3 -m solveg_model.wheat_t.scenario_matrix
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from solveg_model.wheat_t.model import SolvegModel
from solveg_model.wheat_t import config as cfg


def run_matrix():
    """Run key scenarios and print comparison table."""
    results = {}

    # 1. Diabaté baseline (2h, day)
    m, r = SolvegModel.run_diabate(progress_every=0)
    h = r['harvest']
    day_grain = h['grain_OBT_Bq_g']
    results['diabate_2h'] = h

    # 2. Night exposure (2h)
    m2, r2 = SolvegModel.run_diabate(startH=22, progress_every=0)
    night_grain = r2['harvest']['grain_OBT_Bq_g']
    results['diabate_night'] = r2['harvest']

    # 3. 8h exposure
    m3, r3 = SolvegModel.run_diabate(expH=8.0, progress_every=0)
    h8_grain = r3['harvest']['grain_OBT_Bq_g']
    results['diabate_8h'] = r3['harvest']

    # 4. Open soil
    m4, r4 = SolvegModel.run_diabate(soil_covered=False, progress_every=0)
    results['diabate_soil'] = r4['harvest']

    # 5. Chronic (100d)
    s5 = dict(cfg.CHRONIC_SCENARIO)
    m5 = SolvegModel(s5)
    r5 = m5.run(progress_every=0)
    results['chronic'] = r5['harvest']

    # Print matrix
    print("\n" + "=" * 90)
    print("SCENARIO MATRIX — v16")
    print("=" * 90)

    targets = {
        'diabate_2h':    {'grain_OBT_Bq_g': (480, 24), 'leaf_OBT_Bq_g': (26, 1.3),
                          'ear_OBT_Bq_g': (230, 11), 'stem_OBT_Bq_g': (6.3, 0.3)},
    }

    for name, h in results.items():
        g = h['grain_OBT_Bq_g']
        lf = h['leaf_OBT_Bq_g']
        e = h['ear_OBT_Bq_g']
        s = h['stem_OBT_Bq_g']
        tf = h['peak_TFWT_Bq_L']
        tli = h['TLI_diabate_pct']

        # Pass/fail for diabate
        tag = ''
        if name in targets and targets[name]:
            t = targets[name]
            ok = all(
                t[k][0] - t[k][1] <= h.get(k, 0) <= t[k][0] + t[k][1]
                for k in t
            )
            tag = ' ✓' if ok else ' ✗'

        print(f"  {name:<16s}  grain={g:8.1f}  leaf={lf:7.1f}  ear={e:7.1f}  "
              f"stem={s:5.1f}  peakTF={tf:8.0f}  TLI={tli:5.2f}%{tag}")

    # Derived metrics
    print("-" * 90)
    nd = night_grain / day_grain if day_grain > 0 else 0
    d82 = h8_grain / day_grain if day_grain > 0 else 0
    soil_ratio = results['diabate_soil']['grain_OBT_Bq_g'] / day_grain if day_grain > 0 else 0

    nd_ok = abs(nd - 0.56) < 0.05
    d82_ok = abs(d82 - 2.0) < 0.15

    print(f"  N/D  = {nd:.3f}  (target 0.56)  {'✓' if nd_ok else '✗'}")
    print(f"  8h/2h = {d82:.3f}  (target ~2.0)  {'✓' if d82_ok else '✗'}")
    print(f"  soil/PE = {soil_ratio:.3f}  (expect ~0.67)")
    print(f"  chronic grain = {results['chronic']['grain_OBT_Bq_g']:.1f} Bq/g (saturated)")
    print("=" * 90)

    return results


if __name__ == '__main__':
    run_matrix()
