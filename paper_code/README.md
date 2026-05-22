# SOLVEG-II 氚迁移模型 — 论文代码包（v60）

配套论文：《气态HTO叶片输入途径下小麦OBT预测模型的构建与验证》

## 快速开始

```bash
# 1. 安装依赖（只需一次）
pip3 install numpy matplotlib

# 2. 一键运行全部结果
python3 run_all.py

# 3. 快速模式（跳过 DAF 等长时间场景，约 3 分钟）
python3 run_all.py --quick

# 4. 查看输出
ls results/
```

## 输出文件

| 文件 | 对应论文内容 |
|------|-------------|
| `sensitivity.csv` | 表 4-2~4-5（四参数敏感性数据） |
| `daf_predictions.csv` | 表 4-6（DAF 敏感性数据） |
| `scenarios.csv` | 表 4-7~4-8（多场景预测） |
| `fig_sensitivity.png` | 图 4-5~4-8（四参数敏感性综合图） |
| `fig_daf.png` | 图 4-3（DAF 敏感性曲线） |
| `fig_scenarios.png` | 多场景柱状图 |

## 代码结构

```
paper_code/
├── run_all.py              ← 一键运行（入口）
├── README.md               ← 本文件
├── 操作手册.md              ← 详细操作说明
└── wheat_t/                ← 模型核心代码
    ├── __init__.py
    ├── config.py           ← 全部参数定义 + 场景配置
    ├── model.py            ← 主模型（SolvegModel）
    ├── atmosphere.py       ← 气象模块
    ├── canopy.py           ← 冠层辐射/光合（Farquhar + 多层模型）
    ├── organs.py           ← 器官碳池 + OBT 形成/转移
    ├── soil.py             ← 土壤 HTO 传输（Van Genuchten 6 层）
    ├── plant_water.py      ← 植物水分传输（两室水模型）
    └── run.py              ← 命令行入口
```

## 核心参数（v60 标定值）

编辑 `wheat_t/config.py` 可修改所有参数：

```python
# 光合 OBT 形成（SOLVEG 公式）
K_photo = 10**10.25       # [Bq·s/mol] — 光合 OBT 形成速率常数

# 蛋白周转
K_PROT_TURN = 0.0028      # /h — 叶片蛋白周转速率 (t½≈10.3d)

# 谷粒 OBT 转移
K_REMOB = 0.000146        # /h — canopy→grain OBT 再转移速率

# Snapshot receptivity（bell curve）
RECEPTIVITY_PEAK_FP = 0.012   # bell curve 峰值位置（灌浆进度）
RECEPTIVITY_SIGMA = 0.008     # bell curve 宽度
RECEPTIVITY_BASELINE = 0.10   # fp=0 时的 receptivity
```

## 单独运行某个场景

```python
from wheat_t.config import DIABATE_SCENARIO
from wheat_t.model import SolvegModel

# 复制基线场景，修改参数
params = dict(DIABATE_SCENARIO)
params['airHTO'] = 50000   # 改 HTO 浓度
params['expH'] = 8         # 改暴露时长

# 运行
m = SolvegModel(params)
result = m.run()
h = result['harvest']

print(f"grain OBT = {h['grain_OBT_Bq_g']:.1f} Bq/g")
print(f"leaf  OBT = {h['leaf_OBT_Bq_g']:.1f} Bq/g")
print(f"ear   OBT = {h['ear_OBT_Bq_g']:.1f} Bq/g")
print(f"TLI       = {h['TLI_diabate_pct']:.2f}%")
```

## 运行 DAF 场景

```python
from wheat_t.config import _make_daf_scenario
from wheat_t.model import SolvegModel

# DAF=12（开花后第 12 天暴露）
params = _make_daf_scenario(daf=12)
m = SolvegModel(params)
result = m.run()
h = result['harvest']
print(f"DAF=12 grain OBT = {h['grain_OBT_Bq_g']:.1f} Bq/g")
```

## 依赖

- Python 3.10+
- numpy
- matplotlib（仅图表生成需要，纯数据运行可不要）

## Diabaté 1997 验证标准

论文标定基准（PE 膜覆盖，2h，79000 Bq/L，25°C）：

| 指标 | 实测值 | 模型值 (v60) |
|------|--------|-------------|
| Grain OBT | 480±24 Bq/g | 478.7 |
| Leaf OBT | 26±1.3 Bq/g | 26.4 |
| Stem OBT | 6.3±0.3 Bq/g | 6.2 |
| Ear OBT | 230±11 Bq/g | 230.4 |
| TLI | 0.25-0.55% | 0.56% |
| Peak TFWT | 86600 Bq/L | 85889 |

## v60 核心机制

1. **光合固氚**：K_photo × (TFWT/ρ_w) × m_w × f_An × A_n（SOLVEG 物理公式）
2. **Snapshot receptivity**：曝光时灌浆进度 → bell curve → 固定 receptivity 系数
3. **Senescence gating**：衰老→谷粒 OBT 转移被 receptivity 门控
4. **四池碳模型**：叶/茎/穗/谷独立碳池，碳分配由 WOFOST DVS 驱动
5. **暗反应延续**：NU_DARK=0.002/h，暴露后 0-2d OBT 继续上升

## 注意事项

- 模型基于 Diabaté 1997 实验条件标定
- 暴露期 OBT 绝对值偏差较大（150-1800×），已知结构性局限
- DAF 绝对值偏差已确认不需要精确匹配，作为敏感性分析处理
- 慢性/土壤场景预测为外推，缺乏独立实验验证
