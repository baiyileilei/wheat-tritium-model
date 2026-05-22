#!/usr/bin/env python3
"""v42 扩展敏感性分析：E-OBT/NE-OBT、日夜差异、土壤模块、根系途径"""
import sys, os, csv
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import wheat_t.config as cfg
from wheat_t.config import DIABATE_SCENARIO
from wheat_t.model import SolvegModel


def run_scenario(params):
    m = SolvegModel(params)
    r = m.run()
    h = r.get('harvest', {})
    return {
        'grain': h.get('grain_OBT_Bq_g', 0),
        'leaf': h.get('leaf_OBT_Bq_g', 0),
        'stem': h.get('stem_OBT_Bq_g', 0),
        'ear': h.get('ear_OBT_Bq_g', 0),
        'peak_TFWT': h.get('peak_TFWT_Bq_L', 0),
        'TLI': h.get('TLI_diabate_pct', 0) / 100.0,
    }


def run_diabate(**overrides):
    params = {k: v for k, v in DIABATE_SCENARIO.items()
              if k not in ['expected_TFWT_peak_ratio', 'expected_TFWT_halflife',
                           'expected_OBT', 'expected_day_night_ratio']}
    params.update(overrides)
    return run_scenario(params)


def scan_config(name, values, attr):
    """Scan a config attribute, return list of (value, result_dict)."""
    results = []
    old = getattr(cfg, attr)
    for v in values:
        try:
            setattr(cfg, attr, v)
            r = run_diabate()
            results.append((v, r))
            print(f'  {attr}={v}: grain={r["grain"]:.1f} leaf={r["leaf"]:.1f} ear={r["ear"]:.1f}')
        except Exception as e:
            results.append((v, {'grain': float('nan'), 'leaf': float('nan'), 'ear': float('nan')}))
            print(f'  {attr}={v}: FAILED {e}')
    setattr(cfg, attr, old)
    return results


def scan_scenario_param(name, values, key):
    """Scan a scenario parameter."""
    results = []
    for v in values:
        try:
            r = run_diabate(**{key: v})
            results.append((v, r))
            print(f'  {key}={v}: grain={r["grain"]:.1f} leaf={r["leaf"]:.1f} ear={r["ear"]:.1f}')
        except Exception as e:
            results.append((v, {'grain': float('nan'), 'leaf': float('nan'), 'ear': float('nan')}))
            print(f'  {key}={v}: FAILED {e}')
    return results


def scan_irrigation(name, values):
    """Scan irrigation concentration (requires open soil)."""
    results = []
    for v in values:
        try:
            params = {k: v2 for k, v2 in DIABATE_SCENARIO.items()
                      if k not in ['expected_TFWT_peak_ratio', 'expected_TFWT_halflife',
                                   'expected_OBT', 'expected_day_night_ratio']}
            params.update({
                'soil_covered': False,
                'soil_HTO_input': v,
                'irrigation_rate': 0.01,  # 10mm/day
            })
            r = run_scenario(params)
            results.append((v, r))
            print(f'  irrig={v} Bq/L: grain={r["grain"]:.1f} leaf={r["leaf"]:.1f} ear={r["ear"]:.1f}')
        except Exception as e:
            results.append((v, {'grain': float('nan'), 'leaf': float('nan'), 'ear': float('nan')}))
            print(f'  irrig={v}: FAILED {e}')
    return results


# ═══════════════════════════════════════════════════════
print('=' * 60)
print('v42 Extended Sensitivity: E-OBT/NE-OBT + Night + Soil')
print('=' * 60)

all_results = {}

# ── 1. E-OBT/NE-OBT (OBT_EXCH_SPLIT) ──
print('\n[1/5] OBT_EXCH_SPLIT (E-OBT fraction)')
all_results['obt_exch'] = scan_config(
    'OBT_EXCH_SPLIT',
    [0.20, 0.30, 0.40, 0.50, 0.60, 0.70, 0.80],
    'OBT_EXCH_SPLIT'
)

# ── 2. Night OBT formation (NU_DARK) ──
print('\n[2/5] NU_DARK (nighttime OBT formation rate)')
all_results['nu_dark'] = scan_config(
    'NU_DARK',
    [0.0005, 0.001, 0.002, 0.004, 0.008, 0.016],
    'NU_DARK'
)

# ── 3. Soil HTO sink (SOIL_HTO_SINK_FRAC) ──
print('\n[3/5] SOIL_HTO_SINK_FRAC (soil dry deposition)')
all_results['soil_sink'] = scan_config(
    'SOIL_HTO_SINK_FRAC',
    [0.0, 0.10, 0.20, 0.33, 0.50, 0.70],
    'SOIL_HTO_SINK_FRAC'
)

# ── 4. Root uptake efficiency (ROOT_UPTAKE_EFF) ──
print('\n[4/5] ROOT_UPTAKE_EFF (root HTO selectivity)')
all_results['root_eff'] = scan_config(
    'ROOT_UPTAKE_EFF',
    [0.01, 0.05, 0.10, 0.25, 0.50, 0.80, 1.00],
    'ROOT_UPTAKE_EFF'
)

# ── 5. Irrigation concentration ──
print('\n[5/5] Irrigation concentration (open soil + atmospheric)')
all_results['irrigation'] = scan_irrigation(
    'irrigation',
    [0, 100, 1000, 10000, 50000, 100000, 500000]
)

# ═══════════════════════════════════════════════════════
# Save CSV
# ═══════════════════════════════════════════════════════
with open('extended_sensitivity_v42.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['Group', 'Parameter', 'Grain_OBT', 'Leaf_OBT', 'Stem_OBT', 'Ear_OBT', 'Peak_TFWT', 'TLI'])
    for group, data in all_results.items():
        for val, r in data:
            w.writerow([group, val, f'{r["grain"]:.2f}', f'{r["leaf"]:.2f}',
                        f'{r["stem"]:.2f}', f'{r["ear"]:.2f}',
                        f'{r["peak_TFWT"]:.0f}', f'{r["TLI"]:.4f}'])
print('\n✅ CSV saved: extended_sensitivity_v42.csv')

# ═══════════════════════════════════════════════════════
# Plot 5 subplots
# ═══════════════════════════════════════════════════════
fig, axes = plt.subplots(2, 3, figsize=(15, 9))
fig.suptitle('Extended Sensitivity Analysis (v42)', fontsize=14)

configs = [
    ('obt_exch', 'OBT_EXCH_SPLIT', 'E-OBT Fraction', axes[0, 0], 'c'),
    ('nu_dark', 'NU_DARK (h⁻¹)', 'Night OBT Rate', axes[0, 1], 'm'),
    ('soil_sink', 'SOIL_HTO_SINK_FRAC', 'Soil HTO Sink', axes[0, 2], 'brown'),
    ('root_eff', 'ROOT_UPTAKE_EFF', 'Root Uptake Eff.', axes[1, 0], 'green'),
    ('irrigation', 'Irrigation (Bq/L)', 'Irrigation Conc.', axes[1, 1], 'orange'),
]

for key, xlabel, title, ax, color in configs:
    data = all_results[key]
    x = [d[0] for d in data]
    grain = [d[1]['grain'] for d in data]
    leaf = [d[1]['leaf'] for d in data]
    ear = [d[1]['ear'] for d in data]
    ax.plot(x, grain, 'o-', color=color, label='Grain', linewidth=2)
    ax.plot(x, leaf, 's--', color='gray', label='Leaf', alpha=0.7)
    ax.plot(x, ear, '^:', color='red', label='Ear', alpha=0.7)
    ax.set_xlabel(xlabel)
    ax.set_ylabel('OBT (Bq/g)')
    ax.set_title(title)
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)
    if key == 'irrigation':
        ax.set_xscale('log')

# Hide unused subplot
axes[1, 2].axis('off')

plt.tight_layout()
plt.savefig('extended_sensitivity_v42.png', dpi=150, bbox_inches='tight')
print('✅ Plot saved: extended_sensitivity_v42.png')

# ═══════════════════════════════════════════════════════
# Print summary
# ═══════════════════════════════════════════════════════
print('\n' + '=' * 60)
print('SUMMARY')
print('=' * 60)
for group, data in all_results.items():
    grains = [d[1]['grain'] for d in data if not np.isnan(d[1]['grain'])]
    if grains:
        ratio = max(grains) / max(min(grains), 1e-10)
        print(f'{group}: grain range {min(grains):.1f} - {max(grains):.1f} Bq/g, ratio={ratio:.1f}×')
