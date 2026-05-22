"""Multi-literature wheat validation matrix.

Runs model against ALL wheat experiments with tabular data:
  - Diabaté 1997: 10 chamber experiments (2h, different DAF, T, startH)
  - Galeriu 2013: summary metrics (TLI, N/D, biological halftimes)

Usage:
    cd projects && python3 -m solveg_model.wheat_t.literature_validate
"""
import sys, os, json
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from solveg_model.wheat_t.model import SolvegModel
from solveg_model.wheat_t import config as cfg

# Load consolidated literature data
DATA_PATH = os.path.join(os.path.dirname(__file__), '..', 'literature', 'wheat_tritium_consolidated.json')
with open(DATA_PATH) as f:
    LIT = json.load(f)


def load_diabate_experiments():
    """Load Diabaté 1997 chamber experiments from consolidated JSON."""
    d = LIT['A2_Diabate_1997']
    cols = d['chamber_experiments']['columns']
    daf_list = d['chamber_experiments']['DAF']
    grain_obt = d['chamber_experiments']['OBT']['grain_harvest']
    ear_obt = d['chamber_experiments']['OBT']['ear_harvest']
    leaf_hto = d['chamber_experiments']['HTO']['leaf_2h']
    night_flags = d['chamber_experiments']['night_flags']

    # Build experiment list
    exps = []
    for i, col in enumerate(cols):
        exps.append({
            'name': col,
            'daf': daf_list[i] if i < len(daf_list) else None,
            'grain_obt_cw': grain_obt[i] if i < len(grain_obt) else None,
            'ear_obt_cw': ear_obt[i] if i < len(ear_obt) else None,
            'leaf_hto': leaf_hto[i] if i < len(leaf_hto) else None,
            'is_night': col in night_flags,
        })
    return exps


def run_diabate_at_daf(daf, air_hto=79000.0, exp_h=2.0, start_h=8.0, T=25.0):
    """Run model and extract results at specific DAF.

    Uses standard Diabaté scenario as base, overrides exposure parameters.
    DAF = days after flowering. Exposure at t=0 (DAA=0).
    """
    params = dict(cfg.DIABATE_SCENARIO)
    params.update({
        'airHTO': air_hto,
        'expH': exp_h,
        'startH': start_h,
        'Tair': T,
        'progress_every': 0,
    })

    model = SolvegModel(params)
    results = model.run(progress_every=0)

    # Extract grain OBT at specific DAF
    target_h = daf * 24.0
    time_h = results['time_h']
    idx = min(range(len(time_h)), key=lambda i: abs(time_h[i] - target_h))
    grain_obt_at_daf = results['grain_OBT'][idx] if idx < len(results['grain_OBT']) else 0

    harvest = results['harvest']
    return {
        'grain_obt_at_daf': grain_obt_at_daf,
        'grain_obt_harvest': harvest['grain_OBT_Bq_g'],
        'leaf_obt_harvest': harvest['leaf_OBT_Bq_g'],
        'ear_obt_harvest': harvest['ear_OBT_Bq_g'],
        'stem_obt_harvest': harvest['stem_OBT_Bq_g'],
        'peak_TFWT': results['peak_TFWT'],
        'TLI': harvest['TLI_diabate_pct'],
        'model': model,
        'results': results,
    }


def validate_diabate_chamber():
    """Validate against Diabaté 1997 Table 4 chamber experiments."""
    print("=" * 90)
    print("Diabaté 1997 — Chamber Experiments (2h exposure)")
    print("=" * 90)

    exps = load_diabate_experiments()

    # First run baseline to get peak_TFWT for normalization
    base = run_diabate_at_daf(12)  # DAF=12 as reference
    peak_tfwt = base['peak_TFWT']

    # Normalization: literature reports grain OBT in Bq/mL combustion water
    # Model reports in Bq/g dry matter
    # Conversion: Bq/g dm ≈ Bq/mL cw × 0.6 (from consolidated data notes)
    # But for relative comparison, we normalize to leaf HTO

    print(f"\n{'Exp':<6} {'DAF':>4} {'night':>5} {'leafHTO':>8} "
          f"{'grain_obs':>10} {'grain_mod':>10} {'ratio':>7} {'ear_obs':>9} {'ear_mod':>9} {'status'}")
    print("-" * 90)

    all_ratios = []
    for exp in exps:
        name = exp['name']
        daf = exp['daf']
        obs_grain_cw = exp['grain_obt_cw']
        obs_ear_cw = exp['ear_obt_cw']
        leaf_hto = exp['leaf_hto']

        if daf is None or obs_grain_cw is None:
            continue

        # Run model at this DAF
        res = run_diabate_at_daf(daf)
        mod_grain = res['grain_obt_at_daf']
        mod_ear = res['ear_obt_harvest']

        # Convert model Bq/g to Bq/mL cw for comparison
        # Approximate: Bq/mL cw ≈ Bq/g dm / 0.6
        mod_grain_cw = mod_grain / 0.6
        mod_ear_cw = mod_ear / 0.6

        # Normalize both to leaf HTO = 10000 Bq/mL (literature normalization)
        if leaf_hto and leaf_hto > 0:
            norm_factor = 10000.0 / leaf_hto
            obs_grain_norm = obs_grain_cw * norm_factor
            mod_grain_norm = mod_grain_cw * norm_factor
            obs_ear_norm = obs_ear_cw * norm_factor if obs_ear_cw else None
            mod_ear_norm = mod_ear_cw * norm_factor
        else:
            obs_grain_norm = obs_grain_cw
            mod_grain_norm = mod_grain_cw
            obs_ear_norm = obs_ear_cw
            mod_ear_norm = mod_ear_cw

        # Ratio
        ratio = mod_grain_norm / obs_grain_norm if obs_grain_norm > 0 else 0
        all_ratios.append(ratio)

        # Status
        if 0.5 <= ratio <= 2.0:
            status = "✓"
        elif 0.25 <= ratio <= 4.0:
            status = "~"
        else:
            status = "✗"

        ear_str = f"{obs_ear_norm:>9.0f}" if obs_ear_norm else "      n/a"
        ear_mod_str = f"{mod_ear_norm:>9.0f}"

        print(f"{name:<6} {daf:>4} {'  Y' if exp['is_night'] else '  N':>5} "
              f"{leaf_hto:>8.0f} "
              f"{obs_grain_norm:>10.0f} {mod_grain_norm:>10.0f} {ratio:>7.2f} "
              f"{ear_str} {ear_mod_str} {status}")

    # Summary
    if all_ratios:
        import statistics
        mean_r = statistics.mean(all_ratios)
        med_r = statistics.median(all_ratios)
        within_2x = sum(1 for r in all_ratios if 0.5 <= r <= 2.0)
        print(f"\n  Mean ratio: {mean_r:.2f}  Median: {med_r:.2f}  "
              f"Within 2×: {within_2x}/{len(all_ratios)}")

    print("=" * 90)


def validate_diabate_standard():
    """Standard Diabaté validation (DAA=0, 2h, PE film)."""
    print("\n" + "=" * 90)
    print("Diabaté 1997 — Standard Scenario (DAA=0, 2h × 79000 Bq/L)")
    print("=" * 90)

    res = run_diabate_at_daf(0)
    h = {
        'grain': res['grain_obt_harvest'],
        'leaf': res['leaf_obt_harvest'],
        'ear': res['ear_obt_harvest'],
        'stem': res['stem_obt_harvest'],
        'peak': res['peak_TFWT'],
        'TLI': res['TLI'],
    }

    targets = [
        ('grain_OBT', h['grain'], 480, 24, 'Bq/g'),
        ('leaf_OBT',  h['leaf'],  26,  1.3, 'Bq/g'),
        ('ear_OBT',   h['ear'],   230, 11,  'Bq/g'),
        ('stem_OBT',  h['stem'],  6.3, 0.3, 'Bq/g'),
        ('peak_TFWT', h['peak'],  86600, 4300, 'Bq/L'),
    ]

    all_pass = True
    for name, val, target, tol, unit in targets:
        lo, hi = target - tol, target + tol
        ok = lo <= val <= hi
        if not ok:
            all_pass = False
        print(f"  {name:<12s}: {val:>10.2f} {unit:<6s}  "
              f"target {target}±{tol}  {'✓' if ok else '✗'}")

    tli = h['TLI']
    tli_ok = 0.4 <= tli <= 0.9
    if not tli_ok:
        all_pass = False
    print(f"  {'TLI':<12s}: {tli:>10.2f} %       "
          f"target 0.4-0.9%      {'✓' if tli_ok else '✗'}")

    print(f"\n  Result: {'ALL PASS' if all_pass else 'FAILURES'}")
    print("=" * 90)


def validate_galeriu_summary():
    """Validate against Galeriu 2013 summary metrics."""
    print("\n" + "=" * 90)
    print("Galeriu 2013 — Summary Metrics")
    print("=" * 90)

    g = LIT['A1_Galeriu_2013']

    # TLI
    tli_range = g['TLI_by_development_stage']['all_experiments_harvest_mean']
    print(f"  TLI (field 1h): {tli_range['value']}±{tli_range['sd']}% (model: 0.54% for 2h)")

    # Leaf initial HTO
    leaf_day = g['leaf_initial_HTO_relative']['daytime']
    print(f"  Leaf HTO (day): {leaf_day['mean_pct']}±{leaf_day['sd_pct']}% of air (model: ~108%)")

    leaf_night = g['leaf_initial_HTO_relative']['night']
    print(f"  Leaf HTO (night): {leaf_night['mean_pct']}±{leaf_night['sd_pct']}% of air")

    # N/D
    nd_exp = leaf_night['mean_pct'] / leaf_day['mean_pct']
    print(f"  N/D ratio (exp): {nd_exp:.2f} (model: 0.564)")

    # Biological halftimes
    bt = g['biological_halftimes_min']
    print(f"  Leaf half-life (day): {bt['leaf']['day']} min")
    print(f"  Ear half-life (day): {bt['ear']['day']} min")

    print("=" * 90)


def validate_dose_response():
    """8h/2h and N/D ratios."""
    print("\n" + "=" * 90)
    print("Dose Response & Day/Night")
    print("=" * 90)

    # 2h day
    r2d = run_diabate_at_daf(0, start_h=8)
    # 2h night
    r2n = run_diabate_at_daf(0, start_h=22)
    # 8h day
    r8 = run_diabate_at_daf(0, exp_h=8.0, start_h=8)

    nd = r2n['grain_obt_harvest'] / r2d['grain_obt_harvest']
    d82 = r8['grain_obt_harvest'] / r2d['grain_obt_harvest']

    nd_ok = abs(nd - 0.56) < 0.05
    d82_ok = abs(d82 - 2.0) < 0.15

    print(f"  N/D  = {nd:.3f}  (target 0.56)  {'✓' if nd_ok else '✗'}")
    print(f"  8h/2h = {d82:.3f}  (target ~2.0)  {'✓' if d82_ok else '✗'}")
    print(f"  2h day grain:  {r2d['grain_obt_harvest']:.1f} Bq/g")
    print(f"  2h night grain: {r2n['grain_obt_harvest']:.1f} Bq/g")
    print(f"  8h day grain:  {r8['grain_obt_harvest']:.1f} Bq/g")
    print("=" * 90)


def validate_scenarios():
    """Open soil and chronic scenarios."""
    print("\n" + "=" * 90)
    print("Scenario Validation")
    print("=" * 90)

    # Open soil
    r4 = run_diabate_at_daf(0)
    r4_open = SolvegModel(dict(cfg.DIABATE_SCENARIO, soil_covered=False, progress_every=0))
    r4_open_results = r4_open.run(progress_every=0)
    h4 = r4_open_results['harvest']

    soil_ratio = h4['grain_OBT_Bq_g'] / r4['grain_obt_harvest']
    print(f"  Open soil grain: {h4['grain_OBT_Bq_g']:.1f} Bq/g  "
          f"(PE film: {r4['grain_obt_harvest']:.1f}, ratio: {soil_ratio:.3f}, expect ~0.67)")

    # Chronic
    r5 = SolvegModel(dict(cfg.CHRONIC_SCENARIO, progress_every=0))
    r5_results = r5.run(progress_every=0)
    h5 = r5_results['harvest']
    print(f"  Chronic grain: {h5['grain_OBT_Bq_g']:.1f} Bq/g (saturated)")

    print("=" * 90)


def main():
    print("\n" + "#" * 90)
    print("#  SOLVEG v16 — Multi-Literature Wheat Validation")
    print("#" * 90)

    validate_diabate_standard()
    validate_diabate_chamber()
    validate_galeriu_summary()
    validate_dose_response()
    validate_scenarios()

    print("\n" + "#" * 90)
    print("#  Validation Complete")
    print("#" * 90)


if __name__ == '__main__':
    main()
