"""Batch: 重跑 28 场景确认高温 leaf_OBT 修复后全通过。
包含:
- 14 组 Galeriu 田间实验 (1h, 不同时段)
- 暴露时长扫描 (1h, 2h, 4h, 8h)
- 温度扫描 (15-36°C)
"""
import sys, os, json
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from wheat_t_iii.config import DIABATE_SCENARIO
from wheat_t_iii.model import SolvegModel

# 加载 Galeriu 正确数据
with open(os.path.join(os.path.dirname(__file__), '..', 'literature', 'galeriu_2013_data.json')) as f:
    galeriu = json.load(f)

field_exps = galeriu['table1_field_experiments']['experiments']
field_tli_ref = galeriu['table1_field_experiments']['field_TLI']['1h_daytime_avg']

AIR_HTO = 79000.0

def run_one(startH=8.0, expH=2.0, Tair=25.0, airHTO=AIR_HTO, label='', silent=True):
    params = dict(DIABATE_SCENARIO)
    params.update(startH=startH, expH=expH, Tair=Tair, airHTO=airHTO)
    model = SolvegModel(params)
    results = model.run()
    h = results.get('harvest', {})
    return {
        'label': label,
        'grain': h.get('grain_OBT_Bq_g', 0),
        'leaf': h.get('leaf_OBT_Bq_g', 0),
        'stem': h.get('stem_OBT_Bq_g', 0),
        'ear': h.get('ear_OBT_Bq_g', 0),
        'TLI': h.get('TLI_pct', 0),
        'peak_TFWT': results.get('peak_TFWT', 0),
    }

print("=" * 90)
print("GALERIU 14 组田间实验 (1h 暴露)")
print("=" * 90)
print(f"{'Exp':<6} {'Hour':>4} {'T°C':>4} {'PPFD':>6} {'grain':>8} {'leaf':>8} {'TLI%':>8} {'status'}")
print("-" * 90)

day_grains, night_grains = [], []
for exp in field_exps:
    r = run_one(startH=exp['startH'], expH=1.0, Tair=exp['T'], label=exp['name'])
    is_night = exp['PPFD'] == 0
    status = '🌙' if is_night else '☀️'
    print(f"{exp['name']:<6} {exp['startH']:>4} {exp['T']:>4} {exp['PPFD']:>6} {r['grain']:>8.1f} {r['leaf']:>8.1f} {r['TLI']:>8.3f} {status}")
    if is_night:
        night_grains.append(r['grain'])
    else:
        day_grains.append(r['grain'])

if day_grains:
    print(f"\n白天平均 grain: {sum(day_grains)/len(day_grains):.1f} Bq/g")
if night_grains:
    print(f"夜间平均 grain: {sum(night_grains)/len(night_grains):.1f} Bq/g")

print("\n" + "=" * 90)
print("暴露时长扫描 (白天 8h 起始)")
print("=" * 90)
print(f"{'expH':>4} {'grain':>8} {'vs2h':>8} {'TLI%':>8} {'leaf':>8} {'stem':>8} {'ear':>8}")
print("-" * 90)

base_2h = None
for expH in [1.0, 2.0, 4.0, 8.0]:
    r = run_one(startH=8.0, expH=expH, label=f'{expH}h')
    if expH == 2.0:
        base_2h = r['grain']
    vs2h = r['grain'] / base_2h if base_2h else 0
    print(f"{expH:>4.0f} {r['grain']:>8.1f} {vs2h:>8.2f}x {r['TLI']:>8.3f} {r['leaf']:>8.1f} {r['stem']:>8.1f} {r['ear']:>8.1f}")

print("\n" + "=" * 90)
print("温度扫描 (2h 暴露, 8h 起始)")
print("=" * 90)
print(f"{'T°C':>4} {'grain':>8} {'leaf':>8} {'stem':>8} {'ear':>8} {'TLI%':>8} {'status'}")
print("-" * 90)

for T in [15, 18, 20, 22, 25, 28, 30, 32, 33, 35, 36]:
    r = run_one(startH=8.0, expH=2.0, Tair=T, label=f'T={T}')
    # 检查数值爆炸
    exploded = any(v > 1e5 for v in [r['grain'], r['leaf'], r['stem'], r['ear']])
    status = '💥 EXPLODE' if exploded else ('⚠️ HIGH' if r['leaf'] > 100 else '✅')
    print(f"{T:>4} {r['grain']:>8.1f} {r['leaf']:>8.1f} {r['stem']:>8.1f} {r['ear']:>8.1f} {r['TLI']:>8.3f} {status}")

print("\n✅ 批量验证完成")
