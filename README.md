# 小麦氚迁移模型

气态 HTO 经叶片输入的小麦 OBT 预测模型

## 概述

预测大气 HTO 短期/长期暴露后小麦各器官（叶片、茎、穗、籽粒）中有机结合氚（OBT）的积累。基于 SOLVEG 陆地生态系统框架扩展构建，融合了多个模型的机制。

本科毕业论文（南华大学核科学技术学院，2026）配套代码。

## 模型来源

本模型的各个模块来自不同的研究框架，组合形成完整的氚迁移预测系统：

| 模块 | 来源 | 说明 |
|------|------|------|
| 冠层光合 + 气孔导度 | SOLVEG（Ota et al.） | Farquhar 光合模型 + Ball-Berry 气孔模型 |
| 两室水模型（TFWT） | SOLVEG 扩展 | 快室（叶肉水）+ 慢室（维管束水） |
| 光合 OBT 形成 | SOLVEG 公式 | K_photo × (TFWT/ρ_w) × m_w × f_An × A_n |
| 碳分配 | WOFOST（DVS 查表） | 发育阶段驱动的器官碳分配系数 |
| 器官碳池管理 | WOFOST/DSSAT | 双碳池（suc 可溶 + str 结构） |
| 维护呼吸 OBT 释放 | Ota Eq.16 | 慢性暴露饱和的关键机制 |
| 暗反应 OBT | Atarashi-Andoh (2002) | 暴露后 0-2 天 OBT 继续上升 |
| OBT 转运机制 | Galeriu (2013) | 快速 phloem loading，与碳流耦合 |
| 快照 Receptivity | 本研究提出 | 曝光时灌浆进度的 bell curve，产生 DAF 非单调性 |
| Senescence 门控 | 本研究提出 | 叶片衰老→籽粒 OBT 转移受 receptivity 调制 |

## 模型结构

```
大气 HTO
  ↓
冠层（Farquhar 光合 + Ball-Berry 气孔 + 两室水模型）
  ↓ TFWT
光合固氚（SOLVEG 公式）+ 暗代谢 + 夜间快速代谢
  ↓ OBT
四碳池（suc/str × OBT_exch/OBT_str）+ 蛋白周转
  ↓
器官间分配（WOFOST DVS 查表 + 维护呼吸）
  ↓
籽粒 OBT（K_REMOB + senescence + 快照 receptivity 门控）
```

### 核心机制

- **光合 OBT 形成**：唯一的物理 OBT 来源，不绕过碳分配路径
- **快照 Receptivity**：曝光瞬间灌浆进度的 bell curve 系数，峰值在 DAF≈12，产生 DAF 非单调性
- **Senescence 门控**：叶片衰老→籽粒 OBT 转移被 snapshot receptivity 门控，避免 senescence 路径绕过调制
- **暗反应延续**：NU_DARK = 0.002/h，暴露后 0-2 天 OBT 继续上升
- **维护呼吸 OBT 释放**：Ota Eq.16，慢性饱和的关键机制

### 验证结果（Diabaté 1997）

| 器官 | 模型 | 实验 |
|------|------|------|
| grain | 478 Bq/g dm | 480 ± 24 |
| leaf | 26.4 | 26 ± 1.3 |
| stem | 6.2 | 6.3 ± 0.3 |
| ear | 198 | 230 ± 11 |
| peak TFWT | 85,889 Bq/L | 86,600 |

## 目录结构

```
wheat_t/
  config.py        参数配置（物理常数 + 文献参数 + 标定参数）
  model.py         模型主驱动（时间步循环）
  organs.py        器官碳池 + OBT 形成
  canopy.py        冠层光合 + 气孔 + 水模型
  atmosphere.py    大气状态 + LAI + 气动导度
  soil.py          土壤 HTO 迁移
  plant_water.py   植物木质部水输运
  run.py           运行入口
```

## 快速开始

```python
from wheat_t.model import SolvegModel
from wheat_t import config as cfg

# 运行 Diabaté 1997 验证场景
model, results = SolvegModel.run_diabate()

# 查看收获结果
harvest = results['harvest']
print(f"grain = {harvest['grain_OBT_Bq_g']:.1f} Bq/g dm")  # ~478
print(f"leaf  = {harvest['leaf_OBT_Bq_g']:.1f}")            # ~26
print(f"stem  = {harvest['stem_OBT_Bq_g']:.1f}")            # ~6.2
```

## 参数

- **物理常数**：14 个（不可改动）
- **文献参数**：71 个（来自发表数据）
- **标定参数**：27 个（基于 Diabaté 1997 数据标定，config.py 中有注释标注）

## 依赖

- Python 3.10+
- NumPy（可选，当前版本用纯 Python）

## 参考文献

- Diabaté et al. (1997) — 短期 HTO 暴露小麦 OBT 实验数据
- Galeriu et al. (2013) — 田间氚迁移模型综述，OBT 转运机制
- Ota et al. (SOLVEG) — 陆地生态系统模型框架，光合 OBT 公式
- Atarashi-Andoh et al. (2002) — 暗反应 OBT 形成
- WOFOST — 作物发育阶段驱动的碳分配

## 许可

学术用途。
