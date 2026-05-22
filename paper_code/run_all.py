#!/usr/bin/env python3
"""
一键复现论文全部结果（v60 版）
===================================
运行方式:
  python3 run_all.py          → 完整运行（约 10 分钟）
  python3 run_all.py --quick  → 快速模式（跳过 DAF 等长时间场景，约 3 分钟）
输出: results/ 目录下的 CSV 数据 + PNG 图表

复现内容:
  1. Diabaté 1997 验证（表 4-1）
  2. 四参数敏感性分析（表 4-2~4-5, 图 4-5~4-8）
  3. DAF 敏感性分析（表 4-6, 图 4-3）
  4. 多场景预测（表 4-7~4-8）
"""
import sys, os, csv
QUICK = '--quick' in sys.argv
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

import wheat_t.config as cfg
from wheat_t.config import DIABATE_SCENARIO, _make_daf_scenario
from wheat_t.model import SolvegModel

# ═══════════════════════════════════════════════════════
# 工具函数
# ═══════════════════════════════════════════════════════

def run_scenario(params):
    """运行单个场景, 返回 harvest 字典"""
    m = SolvegModel(params)
    r = m.run()
    return r.get('harvest', {})

def run_diabate(**overrides):
    """以 Diabaté 基线运行, 可覆盖参数"""
    params = dict(DIABATE_SCENARIO)
    params.update(overrides)
    return run_scenario(params)

def scan_config(attr, values):
    """扫描 config.py 中的参数, 返回 [(value, harvest_dict), ...]"""
    results = []
    old = getattr(cfg, attr)
    for v in values:
        try:
            setattr(cfg, attr, v)
            h = run_diabate()
            results.append((v, h))
            print(f'  {attr}={v}: grain={h.get("grain_OBT_Bq_g",0):.1f}')
        except Exception as e:
            results.append((v, {}))
            print(f'  {attr}={v}: FAILED ({e})')
    setattr(cfg, attr, old)
    return results

def grain(h):  return h.get('grain_OBT_Bq_g', 0)
def leaf(h):   return h.get('leaf_OBT_Bq_g', 0)
def stem(h):   return h.get('stem_OBT_Bq_g', 0)
def ear(h):    return h.get('ear_OBT_Bq_g', 0)
def tli(h):    return h.get('TLI_diabate_pct', 0)
def peak_tfwt(h): return h.get('peak_TFWT_Bq_L', 0)

# ═══════════════════════════════════════════════════════
# 主程序
# ═══════════════════════════════════════════════════════

os.makedirs('results', exist_ok=True)

print('=' * 60)
print('SOLVEG-II v60 — 论文结果复现')
print('=' * 60)

# ── 1. Diabaté 验证 ──────────────────────────────────
print('\n[1] Diabaté 1997 验证...')
h = run_diabate()
print(f'  grain={grain(h):.1f} (目标 480±24)')
print(f'  leaf ={leaf(h):.1f} (目标 26±1.3)')
print(f'  stem ={stem(h):.1f} (目标 6.3±0.3)')
print(f'  ear  ={ear(h):.1f} (目标 230±11)')
print(f'  TLI  ={tli(h):.2f}% (目标 0.25-0.55%)')
print(f'  peak_TFWT={peak_tfwt(h):.0f} Bq/L (目标 86600)')

# ── 2. 四参数敏感性分析 ───────────────────────────────
print('\n[2] 敏感性分析...')

# (1) HTO 浓度
print('\n  [2-1] HTO 浓度')
hto_vals = [100, 500, 1000, 5000, 10000, 50000, 100000, 500000, 1000000]
hto_results = []
for v in hto_vals:
    h = run_diabate(airHTO=v)
    hto_results.append((v, h))
    print(f'    {v:>8} Bq/L → grain={grain(h):.1f}')

# (2) 暴露时长
print('\n  [2-2] 暴露时长')
dur_vals = [0.5, 1, 2, 4, 8, 24, 48] if QUICK else [0.5, 1, 2, 4, 8, 24, 48, 168, 336, 720]
dur_results = []
for v in dur_vals:
    h = run_diabate(expH=v)
    dur_results.append((v, h))
    print(f'    {v:>6} h → grain={grain(h):.1f}')

# (3) 温度
print('\n  [2-3] 温度')
temp_vals = [10, 15, 20, 25, 30, 35]
temp_results = []
for v in temp_vals:
    h = run_diabate(Tair=v)
    temp_results.append((v, h))
    print(f'    {v:>4}°C → grain={grain(h):.1f}')

# (4) LAI
print('\n  [2-4] LAI')
lai_vals = [1, 2, 3, 4, 5, 6, 7, 8]
lai_results = []
for v in lai_vals:
    h = run_diabate(LAI=v)
    lai_results.append((v, h))
    print(f'    LAI={v} → grain={grain(h):.1f}')

# ── 3. DAF 敏感性 ─────────────────────────────────────
print('\n[3] DAF 敏感性...')
daf_vals = [1, 6, 12, 15, 21, 27, 33]
daf_results = []
if QUICK:
    print('  (skipped in quick mode)')
else:
    for daf in daf_vals:
        try:
            params = _make_daf_scenario(daf)
            h = run_scenario(params)
            daf_results.append((daf, h))
            print(f'    DAF={daf:>2} → grain={grain(h):.1f}')
        except Exception as e:
            daf_results.append((daf, {}))
            print(f'    DAF={daf:>2}: FAILED ({e})')

# ── 4. 多场景预测 ─────────────────────────────────────
print('\n[4] 多场景预测...')
scenario_defs = {
    'Diabaté (2h×79kBq/L)':    dict(DIABATE_SCENARIO),
    '中等暴露 (8h×10kBq/L)':   dict(DIABATE_SCENARIO, airHTO=10000, expH=8),
    '长时暴露 (24h×5kBq/L)':   dict(DIABATE_SCENARIO, airHTO=5000, expH=24),
    '中期暴露 (48h×10kBq/L)':  dict(DIABATE_SCENARIO, airHTO=10000, expH=48, simH=1200),
}
if not QUICK:
    scenario_defs['夜间暴露 (2h×79kBq/L)'] = dict(DIABATE_SCENARIO, startH=22.0)
    scenario_defs['无PE膜 (2h×79kBq/L)']   = dict(DIABATE_SCENARIO, soil_covered=False)

scenario_results = {}
for name, params in scenario_defs.items():
    try:
        h = run_scenario(params)
        scenario_results[name] = h
        print(f'  {name}: grain={grain(h):.1f}  ear={ear(h):.1f}')
    except Exception as e:
        scenario_results[name] = {}
        print(f'  {name}: FAILED ({e})')

# ═══════════════════════════════════════════════════════
# 保存 CSV
# ═══════════════════════════════════════════════════════
print('\n保存数据...')

# 敏感性数据
with open('results/sensitivity.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['Group', 'Parameter', 'Grain_OBT', 'Leaf_OBT', 'Stem_OBT', 'Ear_OBT', 'TLI_pct'])
    for group, data in [('hto', hto_results), ('duration', dur_results),
                        ('temperature', temp_results), ('lai', lai_results)]:
        for val, h in data:
            w.writerow([group, val, f'{grain(h):.2f}', f'{leaf(h):.2f}', f'{stem(h):.2f}',
                        f'{ear(h):.2f}', f'{tli(h):.2f}'])
print('  → results/sensitivity.csv')

# DAF 数据
if daf_results:
    with open('results/daf_predictions.csv', 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['DAF', 'Grain_OBT', 'Leaf_OBT', 'Stem_OBT', 'Ear_OBT'])
        for daf, h in daf_results:
            w.writerow([daf, f'{grain(h):.1f}', f'{leaf(h):.1f}', f'{stem(h):.1f}', f'{ear(h):.1f}'])
    print('  → results/daf_predictions.csv')

# 场景数据
with open('results/scenarios.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['Scenario', 'Grain_OBT', 'Leaf_OBT', 'Stem_OBT', 'Ear_OBT', 'Peak_TFWT'])
    for name, h in scenario_results.items():
        w.writerow([name, f'{grain(h):.1f}', f'{leaf(h):.1f}', f'{stem(h):.1f}',
                    f'{ear(h):.1f}', f'{peak_tfwt(h):.0f}'])
print('  → results/scenarios.csv')

# ═══════════════════════════════════════════════════════
# 生成图表
# ═══════════════════════════════════════════════════════
print('\n生成图表...')

# 图 4-5~4-8: 四参数敏感性 (2×2 子图)
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

panels = [
    (hto_results,  'HTO 浓度 (Bq/L)', '(a) HTO 浓度',   axes[0, 0], True),
    (dur_results,  '暴露时长 (h)',     '(b) 暴露时长',   axes[0, 1], True),
    (temp_results, '温度 (°C)',        '(c) 温度',       axes[1, 0], False),
    (lai_results,  'LAI',             '(d) 叶面积指数', axes[1, 1], False),
]

for data, xlabel, title, ax, logx in panels:
    x = [d[0] for d in data if d[1]]
    g = [grain(d[1]) for d in data if d[1]]
    ax.plot(x, g, 'o-', color='steelblue', linewidth=2, markersize=6)
    ax.set_xlabel(xlabel, fontsize=11)
    ax.set_ylabel('谷粒 OBT (Bq/g)', fontsize=11)
    ax.set_title(title, fontsize=12)
    ax.grid(True, alpha=0.3)
    if logx:
        ax.set_xscale('log')

plt.tight_layout()
plt.savefig('results/fig_sensitivity.png', dpi=150, bbox_inches='tight')
print('  → results/fig_sensitivity.png')

# 图 4-3: DAF 敏感性
if daf_results:
    fig, ax = plt.subplots(figsize=(8, 5))
    daf_x = [d[0] for d in daf_results if d[1]]
    daf_g = [grain(d[1]) for d in daf_results if d[1]]
    ax.plot(daf_x, daf_g, 's-', color='darkred', linewidth=2, markersize=7)
    ax.set_xlabel('DAF (开花后天数)', fontsize=11)
    ax.set_ylabel('谷粒 OBT (Bq/g)', fontsize=11)
    ax.set_title('DAF 敏感性分析', fontsize=12)
    ax.grid(True, alpha=0.3)
    plt.savefig('results/fig_daf.png', dpi=150, bbox_inches='tight')
    print('  → results/fig_daf.png')

# 场景柱状图
if scenario_results:
    fig, ax = plt.subplots(figsize=(10, 5))
    names = list(scenario_results.keys())
    grains = [grain(scenario_results[n]) for n in names]
    colors = ['#2196F3', '#4CAF50', '#FF9800', '#9C27B0', '#F44336', '#795548']
    bars = ax.bar(range(len(names)), grains, color=colors[:len(names)])
    ax.set_xticks(range(len(names)))
    ax.set_xticklabels(names, rotation=20, ha='right', fontsize=9)
    ax.set_ylabel('谷粒 OBT (Bq/g)', fontsize=11)
    ax.set_title('多场景谷粒 OBT 预测', fontsize=12)
    for bar, val in zip(bars, grains):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 5,
                f'{val:.0f}', ha='center', va='bottom', fontsize=9)
    plt.savefig('results/fig_scenarios.png', dpi=150, bbox_inches='tight')
    print('  → results/fig_scenarios.png')

# ═══════════════════════════════════════════════════════
# 打印总结
# ═══════════════════════════════════════════════════════
print('\n' + '=' * 60)
print('总结')
print('=' * 60)
h0 = run_diabate()
print(f'Diabaté 验证:')
print(f'  grain={grain(h0):.1f} (480±24)  leaf={leaf(h0):.1f} (26±1.3)')
print(f'  stem ={stem(h0):.1f} (6.3±0.3)  ear={ear(h0):.1f} (230±11)')
print(f'  TLI  ={tli(h0):.2f}% (0.25-0.55%)')

if temp_results and len(temp_results) >= 6:
    t25 = grain(temp_results[3][1])  # 25°C
    t35 = grain(temp_results[5][1])  # 35°C
    if t25 > 0:
        print(f'\n温度敏感性: 35°C/25°C = {t35/t25:.2f}×')

print(f'\n所有结果已保存至 results/ 目录')
print(f'完成!')
