# SOLVEG 碳流框架 — 替换章节

> **版本**: v5.0-carbon (2026-04-21)
> **范围**: 仅碳分配和 OBT 形成模块。冠层水力学、大气驱动、土壤模块、器官 TFWT 输运链保持 wheat_t 现有代码不变。
> **设计原则**: 追踪碳通量，不追踪碳池质量。OBT 是碳流上的浓度标签。

---

## 0 为什么换

旧模型（wheat_t 现有）的碳部分：

```
光合 → int 池 → suc 池 → sta/str/prot 池
                        ↓ (DVS 查表分配)
                      根/茎/叶/穗/谷物
OBT: F_DARK × TFWT → 直接注入 str 池
```

**三个结构性缺陷：**
1. DVS 查表分配是经验性的，不反映库强竞争
2. F_DARK 是纯拟合参数，物理含义不清（暗反应？酶活性？同位素效应？）
3. OBT 只进不出 → 慢性暴露永远线性，不可能饱和

新模型的碳部分：

```
光合 → 蔗糖通量 → 各器官汇消耗 (呼吸 + 生长)
OBT: F_biochem × 蔗糖通量 → 标记在消耗的碳上
呼吸消耗碳 → 释放 ³H 回 TFWT (负反馈)
新碳进入 → 稀释旧 OBT (生物半衰期)
```

**三个核心改进：**
1. 汇强驱动分配：器官需求决定碳流向，自然处理库竞争
2. F_biochem 有物理含义：光合作用暗反应中 ³H 相对于 ¹H 的富集因子
3. OBT 有出项：呼吸释放 + 碳周转稀释 → 慢性场景自然饱和

---

## 1 状态变量

旧模型：4 个碳池 (int, suc, sta, str) × 5 器官 = 20 个碳状态 + neOBT = 25 个

新模型：**5 个器官，每个器官 2 个状态 = 10 个 + neOBT = 11 个**

| 变量 | 单位 | 含义 |
|------|------|------|
| W_suc[organ] | g C | 器官可溶性碳（蔗糖+淀粉），可被呼吸消耗、可运输 |
| W_str[organ] | g C | 器官结构碳（纤维素+木质素+蛋白），不可移动 |
| neOBT[organ] | Bq | 不可交换 OBT（C-T 键不可逆锁定） |
| TFWT[organ] | Bq/L | 器官束缚水氚浓度（输运链已有，不新增） |

**删除的：** int 池、sta 池、prot 池。int 是瞬态量，不需要显式追踪。sta 并入 suc（淀粉在我们的粒度下和蔗糖行为相同，都是可消耗碳）。prot 的 OBT 行为由 neOBT 代替。

---

## 2 碳流方程

### 2.1 光合碳输入

每时步，冠层光合产生的碳总量：

```
A_total = Σ_layers(A_sunlit × LAI_sl + A_shaded × LAI_sh)    [µmol CO₂/m²/s]
```

转换为碳通量：

```
F_photo = A_total × LAI × dt × 12e-6    [g C/m²/时步]
```

分配到各器官（替代 DVS 查表）：

```
dW_suc[organ] += F_photo × f_alloc[organ]
```

其中 `f_alloc` 由汇强决定（见 §2.2）。

### 2.2 汇强驱动分配（替代 DVS 查表）

**核心思想：** 每个器官有一个碳需求速率（汇强），总光合碳按汇强比例分配。

各器官汇强：

```
S_root = K_root × max(0, W_str_target_root - W_str[root])    [g C/h]
S_stem = K_stem × W_str[stem] × g(DVS)                       [g C/h]
S_leaf = K_leaf × max(0, W_str_target_leaf - W_str[leaf])    [g C/h]
S_ear  = K_ear × W_str[ear] × g(DVS)                         [g C/h]
S_grain = K_grain × (W_str_max_grain - W_str[grain]) × f(T)  [g C/h]
```

其中：
- `K_organ` 是各器官的最大生长速率常数 [h⁻¹]
- `W_str_target` 是结构碳目标值，由生育期决定
- `g(DVS)` 是生育期调制函数
- `f(T)` 是谷物灌浆温度响应（直接用 DSSAT 公式：`0.65 + 0.0787×(T-10)^0.8`）

分配比例：

```
f_alloc[organ] = S_organ / Σ_all(S_organ)     （归一化）
```

**特殊情况：**
- 灌浆前（DVS < 1.0）：S_grain = 0，碳全分给营养器官
- 灌浆期（DVS ≥ 1.0）：S_grain 占主导（~90%），营养器官仅维持
- 叶衰老：释放的 W_suc[leaf] 按 f_alloc 重新分配到茎/穗/谷物

**与旧 DVS 查表的映射关系：**

| DVS | 旧模型 | 新模型 |
|-----|--------|--------|
| 0.0 | root 45%, stem 10%, leaf 45%, grain 0% | S_root 高（需建根系），S_leaf 高（需建叶面积） |
| 0.8 | root 10%, stem 30%, leaf 20%, grain 0% | S_stem 主导（茎伸长），S_leaf 降低 |
| 1.0 | root 5%, stem 5%, leaf 0%, grain 90% | S_grain 极强（库优势），S_leaf→0 |
| >1.0 | root 5%, stem 5%, leaf 0%, grain 90% | S_grain 饱和曲线下降 |

不需要显式查表 — 汇强函数自然产生正确的分配比例。

### 2.2.1 谷物接受度函数（Grain Receptivity）— DAF 非单调性来源

**物理依据**：Diabaté 1997 原文 — "Translocation of OBT to grain was found to depend on the growth rate of the grain"。谷物在灌浆初期需要时间建立淀粉合成酶系统（AGPase、SSS、GBSS等），发育完成后才能高效接受 OBT。

**接受度函数**：
```
receptivity(t_fill) = 1 - exp(-K_RECEP × t_fill)    [无量纲, 0→1]
```

- `t_fill` = 灌浆开始后的时间 [h]
- `K_RECEP` = grain 发育速率 [h⁻¹]，标定范围 0.01-0.05（t½=14-70h）
- 物理含义：grain 酶系统建立的速率常数

**行为**：
- t_fill=0（灌浆刚开始）：receptivity≈0 → grain 不接受 OBT
- t_fill=48h（2天后）：receptivity≈0.39（K_RECEP=0.01）
- t_fill=144h（6天后）：receptivity≈0.76
- t_fill→∞：receptivity→1

**OBT 转移公式**：
```
dOBT_grain = ear_obt_conc × SEL_PHLOEM × S_grain × receptivity(t_fill) × dt
```

**DAF 非单调性解释**（需配合灌浆窗口 DAF 依赖）：
- DAF=1（曝光后 1 天开始灌浆）：ear_obt 高，但 receptivity≈0 → grain OBT 低
- DAF=13（曝光后 13 天）：ear_obt 中等，receptivity=1 → grain OBT 高
- DAF=33（曝光后 33 天）：ear_obt 低（衰减），receptivity=1 → grain OBT 中等

⚠️ **2026-04-29 验证**：单独使用 receptivity 无法产生非单调性。当灌浆窗口固定（不随 DAF 变化）时，receptivity 对所有 DAF 从 0 开始，等比例抑制，不改变单调趋势。根因：模型灌浆窗口固定在 SEN_START_H，不随 DAF 移动。receptivity 需配合灌浆窗口 DAF 依赖才能生效。

**与 fill_rate 的区别**：
- fill_rate 同时调制 dW_grain 和 OBT → 效果抵消
- receptivity 只调制 OBT 转移，不影响碳分配 → 不抵消
- 两者在固定灌浆窗口下均无法产生非单调性

### 2.3 器官碳动态

**可溶碳（suc）消耗 — 两个汇：**

```
# 维持呼吸（碳离开系统，变成 CO₂）
R_maint[organ] = K_resp × W_str[organ] × Q10^((T-25)/10)    [g C/h]

# 生长消耗（suc → str）
Growth[organ] = f_alloc[organ] × F_photo - R_maint[organ]    [g C/h]（如果 >0）
```

**结构碳累积：**

```
dW_str[organ] = Growth[organ] × Y_growth    [g C/h]
```

其中 `Y_growth` 是生长效率（= Gr_Y = 0.8，和 CPlantBox 一致）。

**可溶碳余额：**

```
dW_suc[organ] = 输入（光合分配）- 呼吸消耗 - 生长消耗
```

### 2.4 叶片衰老（碳再分配）

```
senescence_rate = k_senescence × max(0, DVS - DVS_sen_start)^p    [h⁻¹]

dW_suc[leaf] -= senescence_rate × W_suc[leaf]
dW_str[leaf] -= senescence_rate × W_str[leaf]

# 转出的碳按汇强重新分配（替代旧模型的固定比例 REALLOC）
released_C = senescence_rate × (W_suc[leaf] + W_str[leaf] × 0.3)
→ 按 f_alloc 分配到 stem/ear/grain
```

**关键区别：** 旧模型 REALLOC 把 30% str OBT + 10% neOBT 转到谷物。新模型：
- 结构碳（纤维素/木质素）不可被韧皮部运输 → W_str[leaf] 和 neOBT[leaf] 保留（凋落到土壤或留在茎基）
- 只有可溶碳（W_suc[leaf]）被再分配 → OBT[suc] 跟着走

---

## 3 OBT 形成方程

### 3.1 光合 OBT（替代旧的 step_phot_obt）

光合作用固定 ³H 的机制：
1. 光反应：H₂O → O₂ + 2H⁺ + 2e⁻ → ³H 进入水相，不固定到碳
2. 暗反应（Calvin 循环）：CO₂ + 3RuBP → G3P → 蔗糖
   - G3P 中的 H 来自 NADPH（光反应产物）
   - ³H/¹H 比值在 G3P 中的富集 = **F_biochem**

```
F_biochem = (³H/¹H)_G3P / (³H/¹H)_H2O
```

**物理含义：** Calvin 循环中 NADPH → G3P 的同位素分馏因子。文献范围 0.3-1.0（大部分实验测到 <1，说明 ³H 在暗反应中被部分排斥）。

**OBT 产生速率：**

```
R_OBT_photo = F_biochem × α_CG × F_photo × C_TFWT / (12 × 1000)    [Bq/h/m²]
```

其中：
- `F_photo`：光合碳通量 [g C/h/m²]
- `α_CG`：Craig-Gordon 分馏因子（= 0.91，TFWT 中 ³H 富集）
- `C_TFWT`：叶片 TFWT 浓度 [Bq/L]
- `12 × 1000`：碳摩尔质量转换 (g/mol × mol→mmol)

**分配到器官：** 光合 OBT 随碳一起按 f_alloc 分配。

```
dOBT_photo[organ] = R_OBT_photo × f_alloc[organ] / dLAI    [Bq/h]
```

**与旧模型的对比：**

| | 旧模型 | 新模型 |
|---|--------|--------|
| 参数 | F_DARK（纯拟合） | F_biochem（同位素效应） |
| 物理 | 暗反应 × TFWT（不管有没有光合） | 暗反应 × 碳通量 × TFWT（必须有碳流才有 OBT） |
| 夜间 | F_DARK × 0.1（硬编码） | F_photo = 0 → R_OBT = 0（自动为零，不需要夜间系数） |
| 剂量响应 | 被 tau_chamber 淹没 | 直接来自碳通量线性 |

### 3.2 呼吸 OBT 回收（新增，Ota Eq.16）

维持呼吸消耗 W_str（结构碳），释放 CO₂。如果 W_str 中含有 OBT（C-T 键），呼吸会将 ³H 以 HTO 形式释放回器官束缚水。

```
R_OBT_resp[organ] = K_resp × W_str[organ] × OBT_str[organ] / W_str[organ] × f_release
```

其中：
- `OBT_str[organ] / W_str[organ]` = 结构碳中的 OBT 浓度 [Bq/g C]
- `f_release` = 呼吸释放 ³H 的比例（文献值 0.05-0.2，大部分 ³H 以 CO₂ 形式出去，少部分以 HTO 形式保留）
- 结果：OBT_str 减少，TFWT 增加

**这是慢性场景的关键负反馈：**
- OBT 浓度高 → 呼吸释放更多 ³H → OBT 下降 → 净积累变慢 → 自然饱和

**DAF 非单调性的关键机制**（2026-04-29 发现）：
维护呼吸消耗 canopy OBT 是 DAF 非单调性的物理解释。
- 曝光后，canopy OBT 被维护呼吸持续消耗（半衰期 ~2 天）
- DAF=1：曝光刚结束，canopy OBT 高 → grain OBT 中等
- DAF=14：grain 增长最快，canopy OBT 仍有残余 → grain OBT 最高
- DAF=35：canopy OBT 已被呼吸消耗殆尽 → grain OBT 极低
- 参考：Galeriu IAEA TECDOC EMRAS II WG7: "The total OBT per plant increases in the first 2 days and can decrease until harvest at 80% from maximum value."
- 参考：日本水稻 TLI 数据 (Choi 2003): DAF=6→0.39%, DAF=14→0.55%, DAF=21→0.43%, DAF=35→0.045%
- 参考：德国小麦数据 (Diabaté 1997): grain OBT 峰值在 DAF=12-13

⚠️ **2026-04-29 验证结论**：
- **canopy K_RESP_OBT**：对 grain OBT 无效果。原因：标准场景灌浆从 720h 开始，canopy OBT_str 已被蛋白周转耗尽，再加呼吸消耗无影响。
- **ear K_RESP_OBT**：产生单调递减（DAF=1 最高，DAF=33 最低），无法产生非单调性。ear OBT 随时间单调衰减，grain OBT 跟随。
- **ear K_RESP_OBT + K_RECEP 组合**：仍然单调。receptivity 对所有 DAF 等比例抑制。
- **关闭 grain_TFWT 路径 (K_SYNTH_GRAIN=0)**：DAF 效应更明显但仍单调。
- **根因**：模型灌浆窗口固定在 SEN_START_H（720h），不随 DAF 变化。DAF=1 时灌浆在曝光后 24h 开始，DAF=33 时在 792h 后开始，但灌浆时长相同 → 结构性单调。
- **框架方案正确但不充分**：维护呼吸消耗 + receptivity 是 DAF 非单调性的正确机制，但需先修复灌浆窗口的 DAF 依赖（grain fill 起点随 DAF 移动）。

### 3.3 碳周转稀释（新增，Korolevych OBT t½≈25d）

新碳进入器官（光合分配），不含 OBT（或含少量 OBT）。新碳稀释旧 OBT 浓度。

```
OBT_str[organ] += dOBT_photo[organ] × dt          # 新 OBT 进入
OBT_str[organ] -= R_OBT_resp[organ] × dt          # 呼吸释放
OBT_str[organ] ×= W_str[organ]_new / W_str[organ]_old  # 周转稀释
```

稀释效应的物理量级：
- 叶片：K_turnover_leaf ≈ 0.001/day → t½ ≈ 700 天（纤维素/木质素极慢）
- 谷物：灌浆期不断有新碳进入 → 稀释效应在灌浆 47 天内显著
- 慢性暴露 100 天：累积的新碳足以将初始 OBT 稀释 ~15%

### 3.4 neOBT 锁定

当碳从可溶态（suc）变为结构态（str）时，OBT 被"锁定"为 neOBT：

```
dneOBT[organ] = Growth[organ] × OBT_suc[organ] / W_suc[organ] × Y_growth
```

neOBT 不参与呼吸消耗，不参与再分配，只被周转稀释。

---

## 4 参数表（碳流模块）

### 4.1 新增参数

| 参数 | 符号 | 单位 | 初始猜测 | 物理含义 | 标定方法 |
|------|------|------|----------|----------|----------|
| 光合 OBT 富集因子 | F_biochem | - | 0.3-1.0 | Calvin 循环 ³H/¹H 同位素效应 | Diabaté grain OBT |
| 维持呼吸速率 | K_resp | h⁻¹ | 0.002 | 结构碳呼吸消耗速率 | Diabaté 叶 OBT 衰减 |
| 呼吸 ³H 释放比例 | f_release | - | 0.1 | 呼吸释放 ³H→HTO 的比例 | 慢性 OBT 饱和曲线 |
| 根最大生长速率 | K_root | h⁻¹ | 0.01 | 根系汇强常数 | DVS 分配比例 |
| 茎最大生长速率 | K_stem | h⁻¹ | 0.005 | 茎汇强常数 | DVS 分配比例 |
| 叶最大生长速率 | K_leaf | h⁻¹ | 0.02 | 叶汇强常数 | DVS 分配比例 |
| 穗最大生长速率 | K_ear | h⁻¹ | 0.003 | 穗汇强常数 | DVS 分配比例 |
| 谷物最大生长速率 | K_grain | h⁻¹ | 0.05 | 谷物汇强常数 | Diabaté grain OBT |
| 谷物结构碳上限 | W_str_max_grain | g C | 0.5 | 谷物碳饱和值 | 灌浆曲线形状 |
| 生长效率 | Y_growth | - | 0.8 | suc→str 转化效率 | 文献固定 |
| 叶衰老速率 | k_senescence | h⁻¹ | 0.001 | 叶片碳释放速率 | 叶 OBT 动态 |
| 衰老起始 DVS | DVS_sen_start | - | 1.5 | 叶片开始衰老 | 文献固定 |
| 衰老幂指数 | p_sen | - | 2.0 | 衰老加速指数 | 文献固定 |
| 谷物接受度速率 | K_RECEP | h⁻¹ | 0.01-0.05 | grain 发育速率 (淀粉酶系统建立) | DAF 敏感性 |

### 4.2 删除的旧参数

| 参数 | 原值 | 删除原因 |
|------|------|----------|
| F_DARK_leaf | 12.89 | 被 F_biochem 替代 |
| F_DARK_stem | 0.540 | 被 F_biochem 替代 |
| F_DARK_ear | 231.5 | 被 F_biochem 替代 |
| F_DARK_grain | 1885.0 | 被 F_biochem 替代 |
| F_DARK_root | 0.09 | 被 F_biochem 替代 |
| F_DARK 夜间系数 | 0.10 | 不需要（夜间光合=0→OBT=0 自动成立） |

### 4.3 保留的旧参数（不变）

所有冠层参数（Farquhar, Medlyn, Craig-Gordon, 两室水模型）、所有器官 TFWT 输运链参数（tau_stem, tau_ear, k_grain）、所有土壤参数。

---

## 5 标定策略

### 5.1 第一步：Diabaté 基线（6/6 指标）

只调 3 个参数：F_biochem, K_grain, W_str_max_grain

1. 先设 F_biochem = 0.5（文献中值），跑 Diabaté 场景
2. 调 K_grain 使 grain OBT ≈ 480 Bq/g
3. 调 W_str_max_grain 使灌浆曲线形状合理
4. 检查叶/茎/穗 OBT 是否在文献范围内
5. 如果叶/茎偏低 → 调 K_leaf/K_stem 改变分配比例
6. **回归测试：每次调参后跑 Diabaté 全部 6 个指标**

### 5.2 第二步：日夜比

不需要调额外参数 — 夜间 F_photo = 0 → R_OBT_photo = 0 → grain OBT 夜间自动趋近 0。

如果日夜比不在 10-100× 范围内：
- 检查夜间 gs 是否 = 0.0001（已有）
- 检查暗反应 OBT 是否真的为零（不是，如果有非光合 OBT 来源）

### 5.3 第三步：剂量响应

跑 1h/2h/4h/8h 暴露 → grain OBT 应近线性（因为 OBT 直接跟碳通量，碳通量跟暴露时长线性）。

### 5.4 第四步：慢性暴露饱和

跑 100 天慢性 → grain OBT 应有饱和趋势（呼吸回收 + 碳周转稀释）。

如果仍完美线性 → f_release 太小或 K_resp 太小 → 增大。

### 5.5 第五步：其他文献验证

- Atarashi-Andoh（水稻短期暴露）
- Ota 2011（葡萄长期暴露）
- Korolevych 2014（OBT/HTO 比值动态）

---

## 6 实现约束

### 6.1 代码改动范围

| 文件 | 改动 | 行数估计 |
|------|------|----------|
| canopy.py | 删除 step_carbon_pools, step_phot_obt → 替换为 step_carbon_flux, step_obt_formation | ~200 行重写 |
| organs.py | 删除 DVS 查表分配 → 替换为 sink_strength 分配 | ~150 行重写 |
| config.py | 删除 F_DARK × 5 → 替换为 F_biochem + K_resp + 汇强参数 | ~30 行改 |
| model.py | 调用顺序调整：先碳流后 OBT | ~20 行改 |
| run.py | 不改（场景接口不变） | 0 |
| atmosphere.py | 不改 | 0 |
| soil.py | 不改 | 0 |
| plant_water.py | 不改 | 0 |

**总计：~400 行重写 + ~50 行微调。** 不是从零重写 2000 行。

### 6.2 回归测试

每改一步跑：
```python
cd projects/paper && python3 -m wheat_t.run
```

Diabaté 6/6 指标必须全部通过，否则不继续。不允许"先写完再标定"。

### 6.3 不做的事

- 不加种子→开花期生育前期
- 不改冠层水力学（Farquhar, Medlyn, 两室水模型保持不变）
- 不改土壤模块
- 不改器官 TFWT 输运链
- 不引入 3D 网络流求解器
- 不写 2000 行框架文档

---

## 7 与 CPlantBox 的关系

我们借鉴了 CPlantBox 的**概念**，没有借鉴**代码**：

| CPlantBox 概念 | 我们的简化版 |
|---------------|------------|
| 3D 网络流（每个节点独立） | 5 器官块（每个器官一个汇） |
| 筛管 Hagen-Poiseuille 导度 | 不需要（0D 模型无管网） |
| Michaelis-Menten 蔗糖利用 | 简化为线性汇强函数 |
| PiafMunch 外部求解器 | 不需要（Python 直接求解） |
| 植物结构动态生长 | 固定器官拓扑，只追碳量 |
| 根系分泌 Q_Exud | 不模拟（对 OBT 无直接影响） |

**核心借鉴：碳流 > 碳池。** 这是概念层面的，不需要 CPlantBox 的任何代码依赖。
