"""小麦氚迁移模型 — Run Entry Point

Usage:
    python -m wheat_t.run                         # Diabaté default
    python -m wheat_t.run --scenario chronic      # chronic scenario
    python -m wheat_t.run --scenario soil_exposure # soil irrigation
    python -m wheat_t.run --all                   # run all scenarios
    python -m wheat_t.run --airHTO 50000          # custom param
"""

import argparse
import json
import sys
from . import config as cfg
from .model import SolvegModel


SCENARIO_DESC = {
    'diabate': 'Diabaté 1997 PE film baseline (2h × 79000 Bq/L)',
    'diabate_soil': 'Diabaté conditions with open soil (re-evaporation)',
    'diabate_night': 'Night exposure (day/night ratio test)',
    'soil_exposure': 'Irrigation with tritiated water (soil uptake)',
    'mid_exposure': '48h mid-term exposure (10000 Bq/L)',
    'chronic': '100-day chronic exposure (100 Bq/L)',
}


def run_scenario(name, silent=False, **overrides):
    """Run a named scenario from config.SCENARIOS."""
    if name not in cfg.SCENARIOS:
        print(f"Unknown scenario: {name}")
        print(f"Available: {', '.join(cfg.SCENARIOS.keys())}")
        return None, None

    params = dict(cfg.SCENARIOS[name])
    params.update(overrides)
    desc = SCENARIO_DESC.get(name, name)

    if not silent:
        print(f"\n{'='*60}")
        print(f"Scenario: {name}")
        print(f"  {desc}")
        print(f"{'='*60}")

    progress = 0 if silent else 100
    model = SolvegModel(params)
    results = model.run(progress_every=progress)

    return model, results


def run_all_scenarios(silent=True):
    """Run all scenarios and print comparison table."""
    all_results = {}
    for name in cfg.SCENARIOS:
        model, results = run_scenario(name, silent=silent)
        if results:
            h = results['harvest']
            all_results[name] = h

    # Print comparison
    print("\n" + "=" * 80)
    print("SCENARIO COMPARISON")
    print("=" * 80)
    header = f"{'Scenario':<18} {'grain':>8} {'leaf':>8} {'stem':>8} {'ear':>8} " \
             f"{'peakTF':>8} {'TLI%':>6} {'DVS':>5}"
    print(header)
    print("-" * 80)
    for name, h in all_results.items():
        print(f"{name:<18} {h['grain_OBT_Bq_g']:>8.1f} {h['leaf_OBT_Bq_g']:>8.1f} "
              f"{h['stem_OBT_Bq_g']:>8.1f} {h['ear_OBT_Bq_g']:>8.1f} "
              f"{h['peak_TFWT_Bq_L']:>8.0f} {h['TLI_diabate_pct']:>6.2f} "
              f"{h['DVS_final']:>5.2f}")
    print("=" * 80)

    return all_results


def validate_diabate(harvest):
    """Check Diabaté 1997 targets."""
    targets = [
        ('peak_TFWT', harvest.get('peak_TFWT_Bq_L', 0), 86600, 4300, 'Bq/L'),
        ('leaf_OBT',  harvest.get('leaf_OBT_Bq_g', 0),   26.0,   1.3, 'Bq/g'),
        ('stem_OBT',  harvest.get('stem_OBT_Bq_g', 0),   6.3,    0.3, 'Bq/g'),
        ('ear_OBT',   harvest.get('ear_OBT_Bq_g', 0),    230.0,  11.0,'Bq/g'),
        ('grain_OBT', harvest.get('grain_OBT_Bq_g', 0),  480.0,  24.0,'Bq/g'),
    ]

    print(f"\n{'='*60}")
    print("Diabaté 1997 Validation")
    print(f"{'='*60}")

    all_pass = True
    for name, val, target, tol, unit in targets:
        lo, hi = target - tol, target + tol
        ok = lo <= val <= hi
        if not ok:
            all_pass = False
        print(f"  {name:12s}: {val:10.2f} {unit:6s}  "
              f"target {target}±{tol}  {'✓' if ok else '✗'}")

    tli = harvest.get('TLI_diabate_pct', 0)
    tli_ok = 0.4 <= tli <= 0.9
    if not tli_ok:
        all_pass = False
    print(f"  {'TLI':12s}: {tli:10.2f} %       "
          f"target 0.4-0.9%      {'✓' if tli_ok else '✗'}")

    print(f"{'='*60}")
    print(f"Result: {'ALL PASS' if all_pass else 'FAILURES DETECTED'}")
    print(f"{'='*60}")

    # Print grain OBT budget if model is available
    if hasattr(validate_diabate, '_model'):
        m = validate_diabate._model
        organs = m.organs
        grain_inv = organs.grain.OBT_suc * organs.grain.W_suc + organs.grain.OBT_str * organs.grain.W_str + organs._grain_obt_total
        print(f"\n{'='*60}")
        print("GRAIN OBT BUDGET (Bq)")
        print(f"{'='*60}")
        print(f"  K_EAR_TO_GRAIN inject: {organs.diag_ear_to_grain_obt:12.1f}  ({100*organs.diag_ear_to_grain_obt/grain_inv:.1f}%)")
        print(f"  ear→grain realloc:     {organs.diag_ear_realloc_obt:12.1f}  ({100*organs.diag_ear_realloc_obt/grain_inv:.1f}%)")
        print(f"  stem→grain realloc:    {organs.diag_stem_realloc_obt:12.1f}  ({100*organs.diag_stem_realloc_obt/grain_inv:.1f}%)")
        print(f"  leaf→grain realloc:    {organs.diag_leaf_realloc_obt:12.1f}  ({100*organs.diag_leaf_realloc_obt/grain_inv:.1f}%)")
        print(f"  grain inventory total: {grain_inv:12.1f}")
        print(f"  grain OBT [Bq/g]:      {organs.grain_obt_harvest():12.2f}")
        print(f"{'='*60}")

    return all_pass


def main():
    parser = argparse.ArgumentParser(description='小麦 OBT 预测模型')
    parser.add_argument('--scenario', '-s', type=str, default='diabate',
                        help='Scenario name (diabate, diabate_soil, diabate_night, '
                             'soil_exposure, mid_exposure, chronic)')
    parser.add_argument('--all', action='store_true', help='Run all scenarios')
    parser.add_argument('--airHTO', type=float, default=None)
    parser.add_argument('--expH', type=float, default=None)
    parser.add_argument('--simH', type=float, default=None)
    parser.add_argument('--Tair', type=float, default=None)
    parser.add_argument('--silent', action='store_true')
    parser.add_argument('--json', action='store_true', help='JSON output')

    args = parser.parse_args()

    overrides = {}
    for key in ['airHTO', 'expH', 'simH', 'Tair']:
        val = getattr(args, key)
        if val is not None:
            overrides[key] = val

    if args.all:
        run_all_scenarios(silent=args.silent)
        return 0

    model, results = run_scenario(args.scenario, silent=args.silent, **overrides)
    if results is None:
        return 1

    harvest = results.get('harvest', {})

    if args.json:
        output = {
            'scenario': args.scenario,
            'harvest': harvest,
            'n_hours': len(results['time_h']),
            'peak_TFWT': results['peak_TFWT'],
        }
        print(json.dumps(output, indent=2))
    elif args.scenario == 'diabate':
        validate_diabate._model = model
        validate_diabate(harvest)
    else:
        print(f"\n{'='*60}")
        print(f"Results for: {args.scenario}")
        print(f"{'='*60}")
        for k, v in harvest.items():
            print(f"  {k}: {v}")

    return 0


if __name__ == '__main__':
    sys.exit(main())
