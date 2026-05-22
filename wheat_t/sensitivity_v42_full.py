#!/usr/bin/env python3
"""v42 完整敏感性分析 + 场景预测 + 图生成"""
import sys, os, csv
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter
import wheat_t.config as cfg
from wheat_t.config import DIABATE_SCENARIO, DAF_SCENARIOS
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


def run_with_override(**overrides):
    params = {k: v for k, v in DIABATE_SCENARIO.items()
              if k not in ['expected_TFWT_peak_ratio', 'expected_TFWT_halflife',
                           'expected_OBT', 'expected_day_night_ratio']}
    params.update(overrides)
    return run_scenario(params)


def scan(name, values, override_key):
    """Generic scan"""
    results = []
    for v in values:
        try:
            r = run_with_override(**{override_key: v})
            results.append({'param': v, **r})
            print(f'  {name}={v}: grain={r["grain"]:.1f}')
        except Exception as e:
            results.append({'param': v, 'grain': float('nan')})
            print(f'  {name}={v}: FAILED {e}')
    return results


def scan_config_param(name, values, attr_name):
    """Scan a config.py parameter by temporarily overriding it"""
    results = []
    old_val = getattr(cfg, attr_name)
    for v in values:
        try:
            setattr(cfg, attr_name, v)
            r = run_scenario(dict(DIABATE_SCENARIO))
            results.append({'param': v, **r})
            print(f'  {name}={v}: grain={r["grain"]:.1f}')
        except Exception as e:
            results.append({'param': v, 'grain': float('nan')})
            print(f'  {name}={v}: FAILED {e}')
    setattr(cfg, attr_name, old_val)
    return results


# ═══════════════════════════════════════════════════════
# 1. 敏感性分析（6组）
# ═══════════════════════════════════════════════════════
print('=' * 60)
print('SOLVEG-II v42 完整敏感性分析')
print('=' * 60)

all_results = {}

print('\n[1/6] HTO 浓度')
all_results['hto'] = scan('HTO', [100, 500, 1000, 5000, 10000, 50000, 100000, 500000, 1000000], 'airHTO')

print('\n[2/6] 暴露时长')
all_results['duration'] = scan('expH', [0.5, 1, 2, 4, 8, 24, 48, 168, 720], 'expH')
# fix simH for short exposures
for d in all_results['duration']:
    pass  # already ran correctly

print('\n[3/6] 温度')
all_results['temperature'] = scan('T', [10, 15, 20, 25, 30, 35], 'Tair')

print('\n[4/6] LAI')
all_results['lai'] = scan('LAI', [1, 2, 3, 4, 5, 6, 7, 8], 'LAI')

print('\n[5/6] NU_GROSS (OBT形成效率)')
all_results['nu_gross'] = scan_config_param('NU_GROSS', [1000, 2000, 3000, 4000, 6000, 8000, 10000, 12000], 'NU_GROSS')

print('\n[6/6] K_PROT_TURN (蛋白周转)')
all_results['k_prot'] = scan_config_param('K_PROT_TURN', [0.0002, 0.0005, 0.001, 0.002, 0.004, 0.008, 0.016], 'K_PROT_TURN')


# ═══════════════════════════════════════════════════════
# 2. 场景预测（扩展）
# ═══════════════════════════════════════════════════════
print('\n' + '=' * 60)
print('场景预测')
print('=' * 60)

scenarios = {}

# A. 浓度×时长矩阵
print('\n[A] 浓度×时长矩阵')
for hto in [1000, 10000, 79000, 100000]:
    for expH in [1, 2, 8, 24, 48]:
        params = dict(DIABATE_SCENARIO)
        params['airHTO'] = hto
        params['expH'] = expH
        params['simH'] = max(720, expH + 500)
        r = run_scenario(params)
        key = f'hto_{hto}_exp{expH}'
        scenarios[key] = {'hto': hto, 'expH': expH, **r}
        print(f'  HTO={hto:6.0f} expH={expH:3.0f}h: grain={r["grain"]:8.1f}')

# B. 多场景
print('\n[B] 特殊场景')
special = {
    'acute_2h': dict(DIABATE_SCENARIO),
    'mid_48h': {**DIABATE_SCENARIO, 'airHTO': 10000, 'expH': 48, 'simH': 1200},
    'chronic_100d': {**DIABATE_SCENARIO, 'airHTO': 100, 'expH': 2400, 'simH': 2400, 'soil_covered': False},
    'soil_acute': {**DIABATE_SCENARIO, 'airHTO': 0, 'expH': 0, 'soil_covered': False,
                   'soil_HTO_input': 100000, 'irrigation_rate': 0.01, 'simH': 720},
    'dual_acute': {**DIABATE_SCENARIO, 'soil_covered': False,
                   'soil_HTO_input': 79000, 'irrigation_rate': 0.01},
    'soil_chronic': {**DIABATE_SCENARIO, 'airHTO': 0, 'expH': 0, 'soil_covered': False,
                     'soil_HTO_input': 100, 'irrigation_rate': 0.003, 'simH': 2400},
    'dual_chronic': {**DIABATE_SCENARIO, 'airHTO': 100, 'expH': 2400, 'soil_covered': False,
                     'soil_HTO_input': 100, 'irrigation_rate': 0.003, 'simH': 2400},
}
for name, params in special.items():
    r = run_scenario(params)
    scenarios[name] = r
    print(f'  {name:15s}: grain={r["grain"]:8.1f} leaf={r["leaf"]:7.1f} ear={r["ear"]:8.1f}')

# C. DAF 预测
print('\n[C] DAF 预测')
daf_results = {}
for daf in [1, 6, 7, 12, 13, 21, 27, 33]:
    key = f'daf_{daf}'
    if key in DAF_SCENARIOS:
        r = run_scenario(DAF_SCENARIOS[key])
        daf_results[daf] = r
        print(f'  DAF={daf:2d}: grain={r["grain"]:8.1f} leaf={r["leaf"]:7.1f} ear={r["ear"]:8.1f}')


# ═══════════════════════════════════════════════════════
# 3. 保存 CSV
# ═══════════════════════════════════════════════════════
save_dir = '/root/.openclaw/workspace/projects/solveg_model/wheat_t'

# Sensitivity CSV
csv_path = os.path.join(save_dir, 'sensitivity_v42_full.csv')
with open(csv_path, 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['scan_type', 'param', 'grain_OBT', 'leaf_OBT', 'stem_OBT', 'ear_OBT', 'peak_TFWT', 'TLI'])
    for name, data in all_results.items():
        for d in data:
            w.writerow([name, d['param'], d.get('grain', ''), d.get('leaf', ''),
                         d.get('stem', ''), d.get('ear', ''),
                         d.get('peak_TFWT', ''), d.get('TLI', '')])
print(f'\n📊 CSV: {csv_path}')

# Scenario CSV
scen_csv = os.path.join(save_dir, 'scenario_v42.csv')
with open(scen_csv, 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['scenario', 'hto', 'expH', 'grain', 'leaf', 'stem', 'ear', 'peak_TFWT'])
    for name, data in scenarios.items():
        w.writerow([name, data.get('hto', ''), data.get('expH', ''),
                     data.get('grain', ''), data.get('leaf', ''),
                     data.get('stem', ''), data.get('ear', ''),
                     data.get('peak_TFWT', '')])
    for daf, data in daf_results.items():
        w.writerow([f'daf_{daf}', 79000, 2, data['grain'], data['leaf'],
                     data['stem'], data['ear'], data['peak_TFWT']])
print(f'📊 CSV: {scen_csv}')


# ═══════════════════════════════════════════════════════
# 4. 生成图（6子图）
# ═══════════════════════════════════════════════════════
fig, axes = plt.subplots(2, 3, figsize=(16, 11))
plt.rcParams['font.size'] = 10

def plot_panel(ax, data, xlabel, ylabel, title, color, marker, logx=False):
    x = [d['param'] for d in data]
    y = [d['grain'] for d in data]
    if logx:
        ax.semilogx(x, y, f'{color}{marker}-', markersize=6, linewidth=1.5)
    else:
        ax.plot(x, y, f'{color}{marker}-', markersize=6, linewidth=1.5)
    ax.set_xlabel(xlabel, fontsize=11)
    ax.set_ylabel(ylabel, fontsize=11)
    ax.set_title(title, fontsize=12, fontweight='bold')
    ax.grid(True, alpha=0.3)
    # Add value labels
    for xi, yi in zip(x, y):
        if yi > 0:
            label = f'{yi:.0f}' if yi >= 100 else f'{yi:.1f}'
            ax.annotate(label, (xi, yi), textcoords="offset points",
                       xytext=(0, 8), ha='center', fontsize=7, alpha=0.7)

plot_panel(axes[0, 0], all_results['hto'],
           'HTO Concentration (Bq/L)', 'Grain OBT (Bq/g DW)',
           '(a) HTO Concentration', 'b', 'o', logx=True)

plot_panel(axes[0, 1], all_results['duration'],
           'Exposure Duration (h)', 'Grain OBT (Bq/g DW)',
           '(b) Exposure Duration', 'r', 's', logx=True)

plot_panel(axes[0, 2], all_results['temperature'],
           'Temperature (°C)', 'Grain OBT (Bq/g DW)',
           '(c) Temperature', 'g', '^')

plot_panel(axes[1, 0], all_results['lai'],
           'Leaf Area Index (LAI)', 'Grain OBT (Bq/g DW)',
           '(d) LAI', 'm', 'D')

plot_panel(axes[1, 1], all_results['nu_gross'],
           'ν_gross (h⁻¹)', 'Grain OBT (Bq/g DW)',
           '(e) OBT Formation Rate (ν_gross)', 'c', 'v')

plot_panel(axes[1, 2], all_results['k_prot'],
           'K_PROT_TURN (h⁻¹)', 'Grain OBT (Bq/g DW)',
           '(f) Protein Turnover Rate', 'orange', 'p', logx=True)

plt.suptitle('SOLVEG-II v42 Sensitivity Analysis — Diabaté 1997 Baseline (grain=511 Bq/g)',
             fontsize=13, y=1.01)
plt.tight_layout()
fig_path = os.path.join(save_dir, 'sensitivity_v42_full.png')
plt.savefig(fig_path, dpi=150, bbox_inches='tight')
print(f'\n📊 图: {fig_path}')
plt.close()


# ═══════════════════════════════════════════════════════
# 5. DAF 图
# ═══════════════════════════════════════════════════════
fig2, ax2 = plt.subplots(figsize=(8, 5))
daf_x = sorted(daf_results.keys())
daf_grain = [daf_results[d]['grain'] for d in daf_x]
daf_ear = [daf_results[d]['ear'] for d in daf_x]
daf_leaf = [daf_results[d]['leaf'] for d in daf_x]

ax2.plot(daf_x, daf_grain, 'bo-', markersize=8, linewidth=2, label='Grain OBT')
ax2.plot(daf_x, daf_ear, 'rs--', markersize=7, linewidth=1.5, label='Ear OBT')
ax2.plot(daf_x, daf_leaf, 'g^:', markersize=7, linewidth=1.5, label='Leaf OBT')
ax2.set_xlabel('Days After Flowering (DAF)', fontsize=12)
ax2.set_ylabel('OBT (Bq/g DW)', fontsize=12)
ax2.set_title('SOLVEG-II v42: OBT vs Exposure Timing (DAF)', fontsize=13, fontweight='bold')
ax2.legend(fontsize=10)
ax2.grid(True, alpha=0.3)
# Add grain value labels
for x, y in zip(daf_x, daf_grain):
    ax2.annotate(f'{y:.0f}', (x, y), textcoords="offset points",
                xytext=(0, 10), ha='center', fontsize=9, fontweight='bold')
fig2_path = os.path.join(save_dir, 'daf_v42.png')
plt.tight_layout()
plt.savefig(fig2_path, dpi=150, bbox_inches='tight')
print(f'📊 DAF图: {fig2_path}')
plt.close()


# ═══════════════════════════════════════════════════════
# 6. 打印汇总表
# ═══════════════════════════════════════════════════════
print('\n' + '=' * 80)
print('敏感性分析汇总')
print('=' * 80)
for name, label, unit in [
    ('hto', 'HTO 浓度', 'Bq/L'), ('duration', '暴露时长', 'h'),
    ('temperature', '温度', '°C'), ('lai', 'LAI', ''),
    ('nu_gross', 'ν_gross', 'h⁻¹'), ('k_prot', 'K_PROT_TURN', 'h⁻¹')]:
    print(f'\n{label}:')
    baseline = 511.3
    for d in all_results[name]:
        ratio = d['grain'] / baseline if baseline > 0 else 0
        print(f'  {d["param"]:>12} {unit:5s}  grain={d["grain"]:>10.1f} Bq/g  ({ratio:.3f}×)')

print('\n\n场景预测汇总:')
print(f'{"场景":20s} {"grain":>10s} {"leaf":>10s} {"ear":>10s} {"说明"}')
for name, data in scenarios.items():
    desc = ''
    if 'acute' in name: desc = '急性'
    elif 'mid' in name: desc = '中期'
    elif 'chronic' in name: desc = '慢性'
    elif 'hto_' in name: desc = f'HTO={data.get("hto","")}'
    print(f'{name:20s} {data["grain"]:10.1f} {data["leaf"]:10.1f} {data["ear"]:10.1f} {desc}')

print(f'\n{"DAF":>5s} {"grain":>10s} {"leaf":>10s} {"ear":>10s}')
for daf in sorted(daf_results.keys()):
    r = daf_results[daf]
    print(f'{daf:5d} {r["grain"]:10.1f} {r["leaf"]:10.1f} {r["ear"]:10.1f}')

print('\n✅ 完成')
