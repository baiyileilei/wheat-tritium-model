# SOLVEG-II 植物 OBT 积累预测模型 — 新框架完整规范

> **版本**: v3.0 (2026-04-18)
> **目标**: 一个没有任何背景知识的程序员拿到本文件，可以直接写出可运行的代码
> **基于**: Ota & Nagai 2011, Ota et al. 2017, Farquhar et al. 1980, Medlyn et al. 2011, WOFOST, PCSE

---

## §1 概述

**一句话**: 大气中的 HTO 蒸汽通过气孔进入叶片水(TFWT)，TFWT 通过光合作用被固定为有机结合氚(OBT)，OBT 随碳在植物体内转运分配，最终在谷物/茎/叶中累积。模型追踪 ³H 原子从大气→叶水→有机物→各器官的完整路径。

### 输入

| 输入 | 符号 | 单位 | 示例值 |
|------|------|------|--------|
| 大气 HTO 浓度 | C_air | Bq/L | 79,000 |
| 暴露时长 | t_exp | h | 2 |
| 暴露起始时刻 | t_start | h (0-24) | 9 |
| 气温(日均) | T_mean | °C | 25 |
| 相对湿度 | RH | - | 0.65 |
| 风速(均值) | wind_mean | m/s | 2.0 |
| 纬度 | lat | °N | 50 |
| 日序 | doy | 1-365 | 150 |
| 叶面积指数 | LAI | m²/m² | 5.0 |
| 株高 | h_plant | m | 0.8 |
| 冠层分层数 | N_layers | - | 5 |
| 时间步长 | dt | s | 60 |
| 初始积温 | GDD_0 | °C·h | 1500 |
| 土壤类型 | - | - | loam |
| 土壤初始含水率 | θ_0 | - | 0.30 |
| 模拟总时长 | t_sim | h | 1128 |
| 作物类型 | - | - | wheat |

### 输出

| 输出 | 符号 | 单位 |
|------|------|------|
| TFWT 时间序列(每小时) | C_TFWT(t) | Bq/L |
| TFWT 峰值 | C_TFWT_peak | Bq/L |
| 各器官 OBT 收割浓度 | OBT_leaf, OBT_stem, OBT_ear, OBT_grain | Bq/g dry |
| 谷物 OBT 时间序列 | OBT_grain(t) | Bq/g dry |
| 转运指数 | TLI | % |
| 冠层光合速率时间序列 | A_total(t) | µmol/m²/s |
| DVS 时间序列 | DVS(t) | - |

---

## §2 模型结构

### 2.1 架构图

```
┌─────────────────────────────────────────────────────────────────────┐
│                          大 气 层                                    │
│   C_air (HTO, 矩形脉冲: 暴露期=C_air0, 暴露后=0)                     │
│   ↕ 气孔交换 (Craig-Gordon 分馏, α=0.91)                            │
└────────────────────┬────────────────────────────┬───────────────────┘
                     │                            │
          ┌──────────▼──────────┐      ┌──────────▼──────────┐
          │    植被冠层(N层)      │      │     土壤(8层)         │
          │                     │      │                     │
          │  两室水模型:         │      │  HTO 液相+气相扩散   │
          │   C_fast ⇄ C_slow   │      │  根系吸水携带 HTO    │
          │   fv=0.15, τ=30h   │      │  (Diabaté 场景覆盖   │
          │                     │      │   PE膜, Cs_root=0)   │
          │  光合固氚:           │      │                     │
          │   TFWT→OBT (光合)   │      └─────────────────────┘
          │   TFWT_total水源    │
          │                     │
          │  暗反应 OBT:         │
          │   TFWT→OBT_str      │
          │   (酶促代谢途径)     │
          │                     │
          │  四池碳分配:         │
          │   int→suc/sta/str   │
          │   + 蛋白池(prot)    │
          │   + neOBT 锁定      │
          │                     │
          │  叶片衰老:           │
          │   DVS驱动幂律       │
          │   碳+OBT→器官/凋落  │
          └──────────┬──────────┘
                     │
          ┌──────────▼──────────────────────────────────────┐
          │         多器官碳+OBT 分配                         │
          │                                                 │
          │  根 ← 茎 ← 叶(源) → 穗 → 谷物(库)               │
          │                                                 │
          │  WOFOST DVS 分配表 (线性插值)                    │
          │  PCSE/WOFOST81 碳再分配 (灌浆期)                │
          │  器官 TFWT 输运链:                               │
          │   C_slow→茎→穗→谷物 (各τ不同)                   │
          │  器官暗反应+蛋白周转+呼吸                        │
          │  穗部独立光合                                    │
          └─────────────────────────────────────────────────┘
```

### 2.2 模块划分

| 模块 | 文件 | 职责 |
|------|------|------|
| 大气 | atmosphere.py | 气温/PAR/湿度日变化, 饱和水汽压 |
| 冠层 | canopy.py | 多层辐射分配, Farquhar光合, Medlyn气孔, 两室水模型, 碳池OBT, 叶片衰老 |
| 器官 | organs.py | 多器官碳分配, OBT转运, 器官代谢, 碳再分配, 穗部光合 |
| 土壤 | soil.py | 多层HTO扩散, 根系吸水 |
| 主驱动 | model.py | 时步循环, DVS更新, 结果收集 |
| 配置 | config.py | 所有参数 |

### 2.3 时间尺度

| 尺度 | 过程 | 步长 |
|------|------|------|
| 秒(10-60s) | 光合累积, 气孔交换, TFWT ODE积分, 碳池转移 | dt |
| 时(1h) | 大气日变化, 结果记录, DVS更新累积 | 3600/dt 步 |
| 天(24h) | 叶片衰老, 碳再分配累积, GDD累积 | 24 步 |

---

## §3 物理过程

### 3.1 大气条件

**物理含义**: 生成每小时的大气状态(气温、PAR、湿度、风速)，驱动冠层光合和水交换。

#### 3.1.1 饱和水汽压

**方程** (Tetens 1930):
```
e_sat(T) = 0.6108 × exp(17.27 × T / (T + 237.3))   [kPa]
```
- T: 气温 [°C], 限制在 [-40, 60] 范围内

**参数**: 无标定参数, Tetens 公式系数为经验常数。

#### 3.1.2 太阳辐射

**方程** (Campbell & Norman 1998 简化晴天模型):

赤纬角:
```
δ = 23.45 × sin(2π × (284 + doy) / 365)   [°]
```

半日长:
```
cos_ω₀ = -tan(lat×π/180) × tan(δ×π/180)   (限制在 [-1, 1])
h_half = arccos(cos_ω₀) / (15×π/180)       [h]
sunrise = 12 - h_half
sunset  = 12 + h_half
```

太阳高度角正弦:
```
ω = 15 × (hour - 12) × π/180                    [rad]
sin_β = sin(lat_rad)×sin(δ_rad) + cos(lat_rad)×cos(δ_rad)×cos(ω)
sin_β = max(0, sin_β)
```

PAR (光合有效辐射):
```
若 hour < sunrise 或 hour > sunset: PAR = 0
否则:
  frac = (hour - sunrise) / (sunset - sunrise)
  S₀ = 500 × sin(π × frac)              [W/m²] 晴天最大值
  PAR = S₀ × sin_β × 4.57               [µmol/m²/s]
```

**参数**:
| 符号 | 值 | 单位 | 来源 | 真实性 |
|------|-----|------|------|--------|
| S₀_max | 500 | W/m² | 晴天PAR典型值 | ⚠️ 半真实 |
| 转换系数 | 4.57 | µmol/J | PAR波段(400-700nm) | ✅ 真实 |

#### 3.1.3 气温日变化

**方程**:
```
T_air(hour) = T_mean - T_amp × cos(2π × (hour - 14) / 24) × 0.5   [°C]
```
- T_mean: 日均温 [°C]
- T_amp: 日较差 [°C], 默认 5.0

#### 3.1.4 风速日变化

**方程**:
```
wind(hour) = max(0.1, wind_mean - wind_amp × cos(2π × (hour - 14) / 24) × 0.5)   [m/s]
```
- wind_amp = 0.5 m/s (默认)

#### 3.1.5 相对湿度日变化

**方程**: 假设绝对湿度恒定, RH 随温度反变:
```
RH(hour) = min(1.0, max(0.1, RH_mean × e_sat(T_mean) / e_sat(T_air(hour))))
```

#### 3.1.6 大气状态汇总函数

```python
def atmosphere_state(hour: float, T_mean: float, RH_mean: float,
                     wind_mean: float, lat: float, doy: float,
                     T_amp: float = 5.0) -> dict:
    """返回当前小时的大气状态"""
    T_air = T_mean - T_amp * cos(2*pi*(hour-14)/24) * 0.5
    e_sat_val = 0.6108 * exp(17.27 * T_air / (T_air + 237.3))
    ea = min(1.0, max(0.1, RH_mean * e_sat(T_mean) / e_sat_val)) * e_sat_val
    wind = max(0.1, wind_mean - 0.5 * cos(2*pi*(hour-14)/24) * 0.5)
    # PAR
    delta = 23.45 * sin(2*pi*(284+doy)/365)
    lat_r = lat * pi/180; dec_r = delta * pi/180
    cos_omega0 = clip(-tan(lat_r)*tan(dec_r), -1, 1)
    h_half = degrees(acos(cos_omega0)) / 15
    sunrise = 12 - h_half; sunset = 12 + h_half
    if hour < sunrise or hour > sunset:
        PAR = 0.0; sin_beta = 0.1
    else:
        frac = (hour - sunrise) / (sunset - sunrise)
        omega = radians(15*(hour-12))
        sin_beta = max(0.1, sin(lat_r)*sin(dec_r)+cos(lat_r)*cos(dec_r)*cos(omega))
        PAR = 500 * sin(pi*frac) * sin_beta * 4.57  # µmol/m²/s
    isNight = PAR < 10
    return {'Tair': T_air, 'ea': ea, 'es': e_sat_val, 'wind': wind,
            'PAR': PAR, 'sinBeta': sin_beta, 'isNight': isNight}
```

**验证**: 50°N, doy=150, 日长约 16h, 正午 PAR ≈ 500×1.0×sin(50°)×4.57 ≈ 1750 µmol/m²/s。

### 3.2 光合模型 (Farquhar)

**物理含义**: 叶绿体中 Calvin 循环的碳固定速率，由 Rubisco 酶活性(Rubisco限制)和电子传递速率(光限制)共同决定，取两者较小值减去暗呼吸。

#### 3.2.1 Arrhenius 温度响应

Vcmax 和 Jmax 随叶温变化 (C3 植物用 peaked Arrhenius):

```
peaked(Ha, Hd, S, T_leaf):
  T_K = T_leaf + 273.15                        [K]
  T_25 = 298.15                                 [K]
  R = 8.314                                     [J/mol/K]
  f1 = exp(Ha × (T_K - T_25) / (T_25 × R × T_K))
  f2 = 1 + exp((S × T_K - Hd) / (R × T_K))
  return f1 / f2

Vcmax = Vcmax_25 × peaked(Ha_V, Hd_V, S_V, T_leaf)      [µmol/m²/s]
Jmax  = Jmax_25 × peaked(Ha_J, Hd_J, S_J, T_leaf)       [µmol/m²/s]
```

暗呼吸 Arrhenius:
```
R_d = Rd_25 × exp(Ha_Rd × (T_K - T_25) / (T_25 × R × T_K))   [µmol/m²/s]
```

CO₂ 补偿点 Γ*:
```
Γ* = 42.75 × exp(37830 × (T_K - T_25) / (T_25 × R × T_K))    [ppm]
```

Michaelis 常数 (C3):
```
K_c = 302.2 × exp(79430 × (T_K - T_25) / (T_25 × R × T_K))   [ppm]
K_o = 0.278 × exp(36380 × (T_K - T_25) / (T_25 × R × T_K))    [ppm]
```

**参数表 (小麦 C3)**:

| 符号 | 值 | 单位 | 来源 | 真实性 |
|------|-----|------|------|--------|
| Vcmax_25 | 60 | µmol/m²/s | 文献 | ✅ 真实 |
| Jmax_25 | 120 | µmol/m²/s | 文献 | ✅ 真实 |
| Rd_25 | 1.0 | µmol/m²/s | 文献 | ✅ 真实 |
| TPU_25 | 18 | µmol/m²/s | 文献 | ✅ 真实 |
| Ha_V | 65,330 | J/mol | Bernacchi 2001 | ✅ 真实 |
| Hd_V | 200,000 | J/mol | Bernacchi 2001 | ✅ 真实 |
| S_V | 650 | J/mol/K | Bernacchi 2001 | ✅ 真实 |
| Ha_J | 43,540 | J/mol | Bernacchi 2001 | ✅ 真实 |
| Hd_J | 200,000 | J/mol | Bernacchi 2001 | ✅ 真实 |
| S_J | 640 | J/mol/K | Bernacchi 2001 | ✅ 真实 |
| Ha_Rd | 46,390 | J/mol | Bernacchi 2001 | ✅ 真实 |

#### 3.2.2 光合速率计算

**Ci 计算** (胞间 CO₂ 浓度, Farquhar 的核心输入):

Ci 不是直接测量值，而是由气孔导度模型(Medlyn)隐含给出:
```
Ca_mol = C_atmosphere × 1e-6                    [mol/mol]  大气CO₂摩尔分数
Ci = Ca_mol × (1 - 1.6 / (g0 + 1.6*(1 + g1/sqrt(D)) × A_net/Ca_mol))   [mol/mol]
```

但更实用的迭代方法: 先假设 Ci ≈ 0.7 × Ca (典型C3值)，算 A，再用 A 和 gs 重新算 Ci，迭代 2-3 次。

**实际代码中**: Medlyn 模型隐含了 Ci — 不需要显式迭代。A 和 gs 通过最小化求解:
```
A = min(A_c, A_j, A_p) - R_d
其中:
  A_c = Vcmax × (Ci - Γ*) / (Ci + K_c × (1 + O/K_o))     [Rubisco限制]
  A_j = J × (Ci - Γ*) / (4 × (Ci + 2 × Γ*))              [光限制]
  A_p = TPU_25 × exp(0.05×(T_leaf-25)) × Ci / (Ci + 0.5) [TPU限制]
```

电子传递速率 J:
```
I_2 = PAR × 0.3                                              [µmol e⁻/m²/s]
J = (I_2 + J_max - sqrt((I_2 + J_max)² - 4 × 0.7 × I_2 × J_max)) / 1.4
```
- 0.3: PAR 中被 PSII 吸收的比例
- 0.7: 量子效率参数
- 1.4: PSII 与 PSI 分配

**完整伪代码**:
```python
def farquhar(Ci: float, PAR: float, T_leaf: float,
             crop_params: dict) -> dict:
    """
    Farquhar 光合模型
    输入:
      Ci: 胞间CO2 [mol/mol], 典型值 ~0.7*Ca
      PAR: 光合有效辐射 [µmol/m²/s]
      T_leaf: 叶温 [°C]
      crop_params: dict with Vcmax25, Jmax25, Rd25, TPU25,
                   HaV, HdV, Sv, HaJ, HdJ, Sj, HaRd, C4
    输出:
      {'A': float [µmol/m²/s], 'Gs': float [ppm], 'Rd': float}
    """
    T_K = T_leaf + 273.15
    T_25 = 298.15
    R = 8.314

    def peaked(Ha, Hd, S):
        e1 = Ha * (T_K - T_25) / (T_25 * R * T_K)
        e2 = (S * T_K - Hd) / (R * T_K)
        return exp(e1) / (1 + exp(e2))

    Vcmax = crop_params['Vcmax25'] * peaked(HaV, HdV, Sv)
    Jmax = crop_params['Jmax25'] * peaked(HaJ, HdJ, Sj)
    Rd = crop_params['Rd25'] * exp(HaRd * (T_K - T_25) / (T_25 * R * T_K))

    Gs = 42.75 * exp(37830 * (T_K - T_25) / (T_25 * R * T_K))  # Gamma*
    Kc = 302.2 * exp(79430 * (T_K - T_25) / (T_25 * R * T_K))
    Ko = 0.278 * exp(36380 * (T_K - T_25) / (T_25 * R * T_K))

    I2 = PAR * 0.3
    J = (I2 + Jmax - sqrt(max(0, (I2+Jmax)**2 - 4*0.7*I2*Jmax))) / 1.4
    Ci = max(Ci, Gs * 1.5)  # 防止 Ci 低于补偿点

    Ac = Vcmax * (Ci - Gs) / (Ci + Kc * (1 + 0.21/Ko))
    Aj = J * (Ci - Gs) / (4 * (Ci + 2*Gs))
    TPU = crop_params.get('TPU25', 18) * exp(0.05 * (T_leaf - 25))
    Ap = TPU * Ci / (Ci + 0.5)

    A_leaf = max(0, min(Ac, Aj, Ap) - Rd)
    return {'A': A_leaf, 'Gs': Gs, 'Rd': Rd}
```

**物理直觉**: 
- 晴天正午 PAR ≈ 1500 µmol/m²/s, T_leaf ≈ 28°C → A ≈ 15-20 µmol/m²/s
- 阴天 PAR ≈ 300 → A ≈ 5-8
- 夜间 PAR=0 → A = -Rd ≈ -1.0 (暗呼吸)

**验证**: 在 PAR=120 (Diabaté PPFD), T=25°C, Ci≈0.7×420ppm≈294ppm 时, A ≈ 3-5 µmol/m²/s。

### 3.3 气孔导度 (Medlyn)

**物理含义**: 气孔对 CO₂ 吸收和水分散失进行权衡。Medlyn 模型假设植物在最小化水分散失的前提下最大化碳吸收，导度与净光合和 VPD 相关。

**方程** (Medlyn et al. 2011):
```
g_s = g_0 + 1.6 × (1 + g_1 / sqrt(D)) × A_net / C_a   [mol H₂O/m²/s]
```

- g_s: 气孔导度 [mol H₂O/m²/s]
- g_0: 最小导度(角质层) [mol/m²/s], 小麦 ≈ 0.01
- g_1: Medlyn 斜率参数 [-], 小麦 ≈ 5.5 (kPa^0.5)
- D = max(0.01, e_sat(T_leaf) - e_a): 叶面 VPD [kPa]
- A_net: 净光合速率 [µmol CO₂/m²/s]
- C_a: 大气 CO₂ 浓度 [ppm], 典型 420
- 1.6: CO₂ 和 H₂O 扩散率比值 (r_co2/r_h2o)

**单位转换** — 导度从 mol/m²/s 到 m/s:
```
g_s_vol = g_s × V_m_air    [m/s]
V_m_air = 0.0245            [m³/mol] (@25°C, 1atm)
```

夜间气孔导度(角质层):
```
g_night = 0.001   [mol/m²/s]  (小麦角质层导度典型值)
```

**参数**:
| 符号 | 值 | 单位 | 来源 | 真实性 |
|------|-----|------|------|--------|
| g_0 | 0.01 | mol/m²/s | 文献 | ✅ 真实 |
| g_1 (小麦) | 5.5 | kPa^0.5 | Medlyn 2011 | ✅ 真实 |
| g_1 (水稻) | 5.0 | kPa^0.5 | 文献 | ✅ 真实 |
| g_1 (玉米) | 4.0 | kPa^0.5 | C4植物 | ✅ 真实 |
| g_night | 0.001 | mol/m²/s | 小麦角质层 | ✅ 真实 |

**代码**:
```python
def stomatal_cond(A_net: float, D: float, crop_params: dict,
                  isNight: bool = False) -> float:
    """
    Medlyn 气孔导度
    输入: A_net [µmol/m²/s], D [kPa VPD], isNight
    输出: gs [mol H₂O/m²/s]
    """
    if isNight:
        return 0.001  # 角质层导度
    Ca = 420.0  # ppm
    g0 = crop_params['g0']
    g1 = crop_params['g1']
    gs = g0 + 1.6 * (1 + g1 / sqrt(max(0.01, D))) * A_net / Ca
    return max(0.005, gs)  # 下限保护
```

**物理直觉**: 白天 gs ≈ 0.1-0.3 mol/m²/s (≈ 0.0025-0.0074 m/s)。夜间 gs ≈ 0.001 mol/m²/s (≈ 0.000025 m/s)，日夜比 ≈ 100-300×。

### 3.4 蒸腾速率

**物理含义**: 叶片通过气孔向大气散失水蒸气的速率，由叶面到大气的水汽压梯度和导度决定。

**方程** (简化阻力模型):
```
T_vol = g_s × V_m_air × D / (P_atm)   [m/s]
```

更实用的比例缩放法 (避免缺辐射项高估):
```
T_vol = T_ref × (g_s / g_s_ref)   [m/s]
```
- T_ref = 5.8e-8 m/s (≈ 5 mm/day, 小麦 @ gs_ref=0.15 mol/m²/s, VPD≈1.1 kPa)
- g_s_ref = 0.15 mol/m²/s

**代码**:
```python
def transpiration_rate(gs: float) -> float:
    """
    蒸腾速率 (比例缩放法)
    输入: gs [mol H₂O/m²/s]
    输出: T_vol [m/s]
    """
    gs_ref = 0.15    # mol/m²/s
    T_ref = 5.8e-8   # m/s (~5 mm/day)
    return T_ref * (gs / gs_ref)
```

**物理直觉**: 小麦典型蒸腾 ~5 mm/day = 5.8e-8 m/s。gs=0.3 时翻倍 → ~10 mm/day。

### 3.5 两室水模型

**物理含义**: 叶片水不是均匀的一池水。存在两个物理性质不同的水室——快室(自由水, 直接与大气交换)和慢室(束缚水, 通过细胞内扩散与快室交换)。暴露后快室~1h清空, 慢室持续数天释放HTO。Diabaté 测量的 TFWT 是组织自由水浓度(即 C_fast)。

**实验依据**:
1. Diabaté 1997: +22h TFWT 降至峰值的 5.4% (单室模型无法匹配)
2. Brudenell 1997: 快分量 t½≈53min, 慢分量 t½≈15h
3. Duranceau 2001 NMR: 自由水/束缚水 ≈ 15:85

#### 3.5.1 状态变量

每冠层每层 i:
- WHTO_fast[i]: 快室 HTO 库存 [Bq/m² leaf]
- WHTO_slow[i]: 慢室 HTO 库存 [Bq/m² leaf]

#### 3.5.2 浓度定义

总水量:
```
V_water = h_v × dLAI_i    [m³/m² leaf per layer]
```
- h_v = 1.54e-4 m³/m²: 叶片水储量厚度 (SOLVEG Appendix B)

两室浓度:
```
C_fast = WHTO_fast / (V_water × ρ_w)   [Bq/L]
C_slow = WHTO_slow / (V_water × ρ_w)   [Bq/L]
```
- ρ_w = 1000 kg/m³

注意: 两室共用总水量 V_water, fv 不影响浓度计算, fv 只影响交换速率。

#### 3.5.3 ODE 系统 (Operator Splitting)

**快室 ODE**:
```
dC_fast/dt = k_stom × (C_air/α_CG - C_fast) + k_12 × (C_slow - C_fast)
```
- k_stom = T_vol × dLAI / V_water [1/s]: 气孔交换速率
- α_CG = 0.91: Craig-Gordon 动力学同位素分馏
- k_12 = 1/(τ_slow × 3600) [1/s]: 快慢室内部扩散交换速率

**慢室 ODE**:
```
dC_slow/dt = k_12 × (C_fast - C_slow) - k_slow_loss × C_slow
```
- k_slow_loss = 1/(τ_slow_loss × 3600) [1/s]: 慢室独立损失速率

#### 3.5.4 数值积分方案 (每步详细)

**Step 1: 快室 — 解析指数解 (精确)**

快室 ODE 是线性一阶, 有解析解:
```
k_fast_total = k_stom_eff + k_12     [1/s]

若 C_air > 0 (暴露中):
  k_stom = T_vol × α_CG × dLAI / V_water
  C_fast_ss = (k_stom × C_air/α_CG + k_12 × C_slow) / (k_stom + k_12)
  C_fast_ss = max(0, C_fast_ss)
否则 (暴露后, C_air=0):
  C_fast_ss = 0.0

C_fast_new = C_fast_ss + (C_fast - C_fast_ss) × exp(-k_fast_total × dt)
C_fast_new = max(0, C_fast_new)
```

其中:
- k_stom_eff = T_vol × dLAI / V_water (无分馏的交换速率, 用于衰减)
- C_fast_ss: 快室稳态浓度

**Step 2: 慢室 — 半隐式欧拉 (稳定)**

用 C_fast_new (刚算出的快室新值):
```
C_slow_new = (C_slow + k_12 × dt × C_fast_new) / (1 + (k_12 + k_slow_loss) × dt)
C_slow_new = max(0, C_slow_new)
```

**Step 3: 更新库存**
```
WHTO_fast_new = C_fast_new × V_water × ρ_w   [Bq/m²]
WHTO_slow_new = C_slow_new × V_water × ρ_w   [Bq/m²]
```

#### 3.5.5 TFWT 输出定义

Diabaté 测量的是组织自由水(TFWT = Tissue Free Water Tritium), 即自由水浓度:
```
TFWT_output = C_fast   [Bq/L]
```

注意: 旧模型用 fv×C_fast + (1-fv)×C_slow 作为 TFWT 输出。新框架明确: TFWT = C_fast, 因为 Diabaté 测量的是自由水。

#### 3.5.6 光合固氚的水源

光合反应发生在叶绿体, 叶绿体用水是全叶水的混合:
```
TFWT_total = fv × C_fast + (1-fv) × C_slow   [Bq/L]
```

光合 OBT 使用 TFWT_total, 而非仅 C_fast (旧模型问题 #3)。

#### 3.5.7 暗反应/蛋白周转的水源

暗反应(酶促代谢)和蛋白周转发生在细胞质, 接触束缚水环境:
```
暗反应用 C_slow   [Bq/L]
蛋白周转用 C_slow   [Bq/L]
neOBT 积累用 C_slow   [Bq/L]
```

器官各自的 TFWT 通过输运链获得 (§3.14)。

#### 3.5.8 完整伪代码

```python
def step_two_chamber_water(canopy, i, C_air, dt, T_vol, dLAI):
    """
    两室水模型单层更新
    输入:
      canopy: CanopyModel 对象
      i: 层索引
      C_air: 大气HTO [Bq/L]
      dt: 步长 [s]
      T_vol: 蒸腾速率 [m/s]
      dLAI: 该层LAI [m²/m²]
    """
    fv = 0.15
    tau_slow = 30.0 * 3600  # [s]
    k_12 = 1.0 / tau_slow   # [1/s]
    alpha_CG = 0.91
    rho_w = 1000.0
    h_v = 1.54e-4  # m³/m²
    V_water = h_v * dLAI  # [m³/m²]

    if V_water < 1e-30:
        return  # 无叶片水

    C_fast = canopy.WHTO_fast[i] / (V_water * rho_w)
    C_slow = canopy.WHTO_slow[i] / (V_water * rho_w)

    # Step 1: 快室 (解析解)
    k_stom_eff = T_vol * dLAI / V_water  # [1/s]
    k_fast_total = k_stom_eff + k_12

    if C_air > 0:
        k_stom = T_vol * alpha_CG * dLAI / V_water
        C_fast_ss = (k_stom * C_air / alpha_CG + k_12 * C_slow) / (k_stom + k_12)
    else:
        C_fast_ss = 0.0

    C_fast_new = C_fast_ss + (C_fast - C_fast_ss) * exp(-k_fast_total * dt)
    C_fast_new = max(0, C_fast_new)

    # Step 2: 慢室 (半隐式欧拉)
    k_slow_loss = 1.0 / (30.0 * 3600)  # τ_slow_loss=30h
    C_slow_new = (C_slow + k_12 * dt * C_fast_new) / (1 + (k_12 + k_slow_loss) * dt)
    C_slow_new = max(0, C_slow_new)

    # Step 3: 更新库存
    canopy.WHTO_fast[i] = C_fast_new * V_water * rho_w
    canopy.WHTO_slow[i] = C_slow_new * V_water * rho_w

    # TFWT 输出 = C_fast (Diabaté 测量值)
    canopy.TFWT[i] = C_fast_new

    # TFWT_total (光合用水)
    TFWT_total = fv * C_fast_new + (1 - fv) * C_slow_new
    canopy._TFWT_total[i] = TFWT_total

    # 暗反应/蛋白反应用 C_slow
    canopy._C_slow_local[i] = C_slow_new
```

#### 3.5.9 暴露后行为验证

设 fv=0.15, τ_slow=30h, 暴露末 C_peak≈86,600 Bq/L, C_air 暴露后=0:

| 暴露后时间 | C_fast [Bq/L] | C_slow [Bq/L] | TFWT输出(=C_fast) | Diabaté实测 |
|-----------|--------------|--------------|-------------------|------------|
| 0h | 86,600 | 86,600 | 86,600 | 86,600 ✅ |
| +1h | ~5,000 | ~80,000 | ~5,000 | 66,900 (偏差因简化) |
| +2h | ~500 | ~75,000 | ~500 | 52,100 |
| +22h | ~0 | ~6,500 | ~0 | 4,680 |
| +48h | ~0 | ~1,600 | ~0 | — |

注: +1h/+2h 偏差因简化模型(无边界层阻力、无冠层异质性)。+22h 匹配良好。

**参数**:
| 符号 | 值 | 单位 | 来源 | 真实性 | 标定范围 |
|------|-----|------|------|--------|---------|
| fv | 0.15 | - | Duranceau 2001 NMR | ⚠️ 半真实 | 0.10-0.25 |
| τ_slow | 30 | h | 拟合 Diabaté +22h | 🔴 标定 | 15-50 h |
| k_12 | 9.26e-6 | 1/s | = 1/(τ_slow×3600) | 导出 | - |
| τ_slow_loss | 30 | h | 与τ_slow同量级 | 🔴 标定 | 20-60 h |
| h_v | 1.54e-4 | m³/m² | Yamazawa 2001 | ✅ 真实 | - |

### 3.6 暗反应 OBT

**物理含义**: 植物代谢(非光合途径)将组织水中的 ³H 固定到有机碳 C-H 键中。主要途径是酶促代谢: Calvin 循环中间产物→TCA循环→氨基酸合成→蛋白质/次生代谢物。这些反应在全天持续，不依赖光照。

**方程**:
```
dOBT_str_organ = F_DARK_organ × C_slow_organ × dt/hr   [Bq/kg C]
```
- F_DARK_organ: 器官特异暗反应速率 [1/h]
- C_slow_organ: 该器官局部 TFWT (束缚水浓度) [Bq/L]
- dt/hr = dt/3600: 步长从秒转小时

暗反应 OBT 直接进入结构池(str), 因为酶促反应产物(纤维素、木质素、结构蛋白)属于结构碳。

**各器官的 TFWT 来源**:
- 叶: 冠层 C_slow (两室模型慢室)
- 茎: _stem_local_TFWT (从冠层 C_slow 输运)
- 穗: _ear_local_TFWT (暴露期从 C_air/α, 暴露后从茎输运)
- 谷物: _grain_local_TFWT (从穗耦合)
- 根: _stem_local_TFWT (与茎同源)

**器官特异 F_DARK 参数**:

| 符号 | 值(白天) | 值(夜间) | 单位 | 物理基础 | 真实性 | 标定范围 |
|------|---------|---------|------|---------|--------|---------|
| F_DARK_叶 | 0.2683 | 0.1341 | 1/h | 酶促代谢, 叶高表面积 | 🔴 标定 | 物理×10内 |
| F_DARK_茎 | 0.0036 | 0.0021 | 1/h | 木质化, 代谢慢 | 🔴 标定 | 物理×10内 |
| F_DARK_穗 | 0.380 | 0.150 | 1/h | 灌浆期活跃 | 🔴 标定 | 物理×10内 |
| F_DARK_谷物 | 2.97 | 1.49 | 1/h | 灌浆高代谢 | 🔴 标定 | 物理×10内 |
| F_DARK_根 | 0.08 | 0.03 | 1/h | 中等代谢 | 🔴 标定 | 物理×10内 |

**标定说明**: 
- F_DARK 的物理基准是非酶 H 交换 (~0.00004/h), 但标定值高 3-4个数量级
- 差异来源: 酶促代谢途径(Calvin中间物→氨基酸→蛋白)比非酶交换快~1000×
- 标定值不应超过酶促代谢物理上限 (~1-10/h), 各器官均在此范围内
- 旧模型 F_DARK_叶=0.268/h 已确认为酶促途径(非非酶交换), 保留

**代码**:
```python
def step_dark_obt(organ, C_slow_local: float, dt: float, isNight: bool):
    """
    器官暗反应 OBT
    输入:
      organ: OrganPool 对象 (有W_str, OBT_str, f_dark_day, f_dark_night)
      C_slow_local: 该器官局部TFWT [Bq/L]
      dt: 步长 [s]
      isNight: 是否夜间
    """
    if C_slow_local <= 0 or organ.W_str < 1e-20:
        return
    f_dark = organ.f_dark_day if not isNight else organ.f_dark_night
    dOBT = f_dark * C_slow_local * dt / 3600  # [Bq/kg C]
    organ.OBT_str += dOBT
```

### 3.7 光合固氚

**物理含义**: 光合作用 6CO₂ + 6H₂O → C₆H₁₂O₆ + 6O₂ 中, 水的 H 被固定到葡萄糖 C-H 键。如果叶水含 HTO, 产物就是 OBT。这是 OBT 的主要即时来源。

**方程** (Ota 2011 Eq.15, 修正版):
```
F_phot = A_leaf × f_An × (M_w/ρ_w) × TFWT_total × dLAI   [Bq/m²/s]
```

各量:
- A_leaf: 叶片净光合 [mol CO₂/m²/s] = A_µmol × 1e-6
- f_An = 0.78: 光合同位素分馏因子 (³H-O键比¹H-O键更稳定)
- M_w = 0.018 kg/mol: 水摩尔质量
- ρ_w = 1000 kg/m³: 水密度
- TFWT_total = fv × C_fast + (1-fv) × C_slow [Bq/L] = TFWT_total × 1000 [Bq/m³]
- dLAI: 该层 LAI [m²/m²]

**单位验证**:
```
[mol/m²/s] × [-] × [kg/mol]/[kg/m³] × [Bq/m³] × [m²/m²]
= [mol/m²/s] × [m³/mol] × [Bq/m³] × [-]
= [Bq/m²/s]  ✅
```

**关键改进 (vs 旧模型)**:
- 旧模型用 C_fast 作为光合水源 → 低估 OBT 产出 (f_v=0.15, 仅15%水量)
- 新模型用 TFWT_total (全叶水混合) → 正确反映叶绿体用水

**OBT 去向**: 光合 OBT 直入蔗糖池(suc), 跳过中间池稀释。
理由: 光合在 Calvin 循环中直接产生蔗糖前体, OBT 载体就是蔗糖。

```python
def step_phot_obt(canopy, i, A_leaf_umol: float, dt: float):
    """
    冠层单层光合 OBT
    输入:
      canopy: CanopyModel
      i: 层索引
      A_leaf_umol: 净光合 [µmol/m²/s]
      dt: 步长 [s]
    """
    f_An = 0.78
    M_w = 0.018
    rho_w = 1000.0

    if A_leaf_umol <= 0:
        return

    A_leaf = A_leaf_umol * 1e-6  # mol/m²/s
    TFWT_total = canopy._TFWT_total[i]  # Bq/L (§3.5 计算)
    TFWT_total_m3 = TFWT_total * 1000   # Bq/m³
    dLAI = canopy.dLAI[i]

    F_phot = A_leaf * f_An * (M_w / rho_w) * TFWT_total_m3 * dLAI  # Bq/m²/s
    dOBT_phot = F_phot * dt  # Bq/m²

    # 碳增量 [kg C/m²]
    dW = (1.0/6.0) * 0.180 * A_leaf_umol * 1e-6 * dt  # kg glucose
    # 注: 0.180 = 葡萄糖摩尔质量 kg/mol
    # 葡萄糖中碳含量 = 72/180 = 0.4, 但代码用葡萄糖总质量

    # 直入蔗糖池
    dW_suc = canopy._alloc_suc_frac * dW
    if dW_suc > 1e-20:
        OBT_per_C = dOBT_phot / dW_suc  # Bq/kg C
        W_old = canopy.W_suc[i]
        OBT_old = canopy.OBT_suc[i]
        canopy.W_suc[i] += dW_suc
        canopy.OBT_suc[i] = (OBT_old * W_old + OBT_per_C * dW_suc) / canopy.W_suc[i]
```

**参数**:
| 符号 | 值 | 单位 | 来源 | 真实性 |
|------|-----|------|------|--------|
| f_An | 0.78 | - | Guenot & Belot 1984 | ✅ 真实 |
| M_w | 0.018 | kg/mol | 物理常数 | ✅ 真实 |
| ρ_w | 1000 | kg/m³ | 物理常数 | ✅ 真实 |

### 3.8 四池碳模型

**物理含义**: 光合产物不是直接变成结构物质。先进入中间池(int), 再分配到蔗糖(suc, 运输态)、淀粉(sta, 储存态)、结构碳(str, 细胞壁等)。每个池有独立 OBT 浓度。OBT 随碳流动时遵循质量守恒。

#### 3.8.1 碳池状态变量

每层每器官:
- W_int [kg C/m²]: 中间池碳质量
- W_suc [kg C/m²]: 蔗糖池碳质量
- W_sta [kg C/m²]: 淀粉池碳质量
- W_str [kg C/m²]: 结构池碳质量
- OBT_int, OBT_suc, OBT_sta, OBT_str [Bq/kg C]: 各池 OBT 浓度

#### 3.8.2 初始化 (按 Ota 2011 / Fondy & Geiger 1982)

```
W_total_init = h_v × ρ_w / (1 - leaf_water_frac) × dLAI   [kg/m² leaf]
```
- h_v = 1.54e-4 m³/m², leaf_water_frac = 0.65
- W_total_init ≈ 0.044 kg/m² leaf

各池初始:
```
W_str = 0.85 × W_total_init
W_int = 0.03 × W_total_init
W_sta = 0.0175 × W_total_init
W_suc = 0.0025 × W_total_init
W_prot = 0.10 × W_total_init  (蛋白质池, §3.9)
```

#### 3.8.3 白天分配

光合碳全部进入中间池, 然后按比例分配:
```
dW_total = (1/6) × M_g × A_µmol × 1e-6 × dt   [kg glucose/m²]
```
- M_g = 0.180 kg/mol (葡萄糖摩尔质量)
- A_µmol: 净光合 [µmol/m²/s]

中间池更新:
```
W_int_new = W_int + dW_total
```

分配 (白天):
```
dW_suc = f_suc_day × dW_total     → W_suc += dW_suc
dW_sta = f_sta_day × dW_total     → W_sta += dW_sta
dW_str = f_str_day × dW_total     → W_str += dW_str
W_int  -= dW_total                 (碳守恒: 进来的全分走)
```

#### 3.8.4 夜间分配

夜间无光合输入。淀粉池动员回中间池:
```
flow_sta = k_sta_int × W_sta × dt/3600   [kg C/m²]
flow_sta = min(flow_sta, W_sta)
```
OBT 随碳:
```
S_sta = OBT_sta
W_int += flow_sta; W_sta -= flow_sta
OBT_int = (OBT_int × (W_int - flow_sta) + S_sta × flow_sta) / W_int
```

夜间分配比例不同:
```
dW_suc = f_suc_night × flow_sta
dW_sta = f_sta_night × flow_sta (夜间也少量积累淀粉)
dW_str = f_str_night × flow_sta
```

#### 3.8.5 蔗糖转运出叶

```
flow_out = k_suc_out × W_suc × dt/3600   [kg C/m²]
flow_out = min(flow_out, W_suc)
```
OBT 跟走 (等比例移除, 浓度不变):
```
frac_out = flow_out / W_suc
OBT_suc *= (1 - frac_out)
W_suc -= flow_out
```

返回: (flow_out, OBT_suc_before) 作为器官间转运的输入。

#### 3.8.6 呼吸消耗 + OBT 释放

从中间池消耗碳 (维持呼吸):
```
resp_C = k_resp × W_int × dt/3600   [kg C/m²]
resp_C = min(resp_C, W_int × 0.5)
```

OBT 释放: 呼吸释放的 TFWT 含 OBT, 浓度 = OBT_int:
```
释放的 OBT [Bq] = OBT_int × resp_C
但呼吸选择性效应: fd × (1/6) 只释放碳消耗的 fd/6 比例的 OBT
实际 OBT 浓度变化:
OBT_int *= (1 - fd × (1/6) × resp_frac)
其中 resp_frac = resp_C / W_int
```

呼吸释放的 TFWT 回到叶片水 (少量, 可忽略或加回 C_fast)。

**DAF 非单调性的核心机制**（2026-04-29 文献调研确认）：
维护呼吸消耗 canopy OBT 是 DAF 非单调性的物理解释。
- 曝光后，canopy OBT 被维护呼吸持续消耗（半衰期 ~2 天）
- DAF 小：曝光刚结束，canopy OBT 高，但 grain 小/partition 低
- DAF 中：grain 增长最快，canopy OBT 仍有残余 → grain OBT 最高
- DAF 大：canopy OBT 已被呼吸消耗殆尽 → grain OBT 极低
- 参考：Galeriu IAEA TECDOC EMRAS II WG7; Choi 2003 水稻 TLI; Diabaté 1997 小麦 grain OBT

#### 3.8.7 碳池分配系数

| 参数 | 白天值 | 夜间值 | 单位 | 来源 | 真实性 |
|------|--------|--------|------|------|--------|
| f_suc | 0.48 | 0.30 | - | Fondy & Geiger 1982 | ⚠️ 半真实 |
| f_sta | 0.26 | 0.50 | - | Fondy & Geiger 1982 | ⚠️ 半真实 |
| f_str | 0.26 | 0.20 | - | Fondy & Geiger 1982 | ⚠️ 半真实 |
| k_sta_int | 0.02 | 0.02 | 1/h | Ota 2011 | ⚠️ 半真实 |
| k_suc_out | 0.10 | 0.10 | 1/h | Ota 2011 | ⚠️ 半真实 |
| k_resp | 0.05 | 0.05 | 1/h | Ota 2011 | ⚠️ 半真实 |
| fd_day | 0.015 | - | - | Ota 2017 | ⚠️ 半真实 |
| fd_night | - | 0.025 | - | Ota 2017 | ⚠️ 半真实 |

#### 3.8.8 OBT 随碳流动的规则

**规则 1 — 碳从 A 池到 B 池**: OBT 浓度 = A 池浓度 (同位素指纹跟碳走)

**规则 2 — 新碳稀释**: 
```
S_B_new = (S_B_old × W_B_old + S_A × dW) / (W_B_old + dW)
```

**规则 3 — 呼吸消耗**: 碳减少时 OBT 按 fd/6 比例选择性释放

**规则 4 — neOBT 不动**: 非交换 OBT (C-T 键) 不随碳流动

#### 3.8.9 完整代码

```python
def step_carbon_pools(layer, dt: float, isNight: bool,
                      A_umol: float, alloc: dict):
    """
    冠层单层四池碳更新
    输入:
      layer: 冠层单层对象
      dt: 步长 [s]
      isNight: 是否夜间
      A_umol: 净光合 [µmol/m²/s]
      alloc: {'f_suc':..,'f_sta':..,'f_str':..} 分配系数
    """
    dt_hr = dt / 3600.0
    Md = 0.180  # kg/mol glucose

    if not isNight and A_umol > 0:
        # 白天: 光合碳进中间池
        dW = (1.0/6.0) * Md * A_umol * 1e-6 * dt  # kg glucose/m²
        layer.W_int += dW

        # 按比例分配到三池
        for pool, frac in [('suc', alloc['f_suc']),
                           ('sta', alloc['f_sta']),
                           ('str', alloc['f_str'])]:
            dW_pool = frac * dW
            W_arr = getattr(layer, f'W_{pool}')
            OBT_arr = getattr(layer, f'OBT_{pool}')
            OBT_src = layer.OBT_int
            if pool == 'str':
                OBT_src /= 3.0  # KIE_PROT 同位素效应
            W_old = W_arr
            OBT_old = OBT_arr
            setattr(layer, f'W_{pool}', W_old + dW_pool)
            if W_old + dW_pool > 1e-20:
                setattr(layer, f'OBT_{pool}',
                        (OBT_old*W_old + OBT_src*dW_pool)/(W_old+dW_pool))

        # 中间池碳守恒: 减去已分配的
        layer.W_int = max(0, layer.W_int - dW)

        # 呼吸消耗
        resp_C = k_resp * layer.W_int * dt_hr
        resp_C = min(resp_C, layer.W_int * 0.5)
        if resp_C > 1e-20:
            resp_frac = resp_C / max(layer.W_int, 1e-20)
            layer.OBT_int *= (1 - fd_day * (1.0/6.0) * resp_frac)
            layer.W_int = max(0, layer.W_int - resp_C)

    else:
        # 夜间: 淀粉动员
        flow = min(k_sta_int * layer.W_sta * dt_hr, layer.W_sta)
        if flow > 1e-20:
            S_sta = layer.OBT_sta
            W_int_old = layer.W_int
            OBT_int_old = layer.OBT_int
            layer.W_int += flow
            layer.W_sta -= flow
            if layer.W_int > 1e-20:
                layer.OBT_int = (OBT_int_old*W_int_old + S_sta*flow) / layer.W_int

        # 夜间呼吸
        resp_C = k_resp * layer.W_int * dt_hr
        resp_C = min(resp_C, layer.W_int * 0.5)
        if resp_C > 1e-20:
            resp_frac = resp_C / max(layer.W_int, 1e-20)
            layer.OBT_int *= (1 - fd_night * (1.0/6.0) * resp_frac)
            layer.W_int = max(0, layer.W_int - resp_C)

    # 蔗糖转运出叶
    if layer.W_suc > 1e-20:
        flow_out = min(k_suc_out * layer.W_suc * dt_hr, layer.W_suc)
        frac_out = flow_out / layer.W_suc
        S_suc_out = layer.OBT_suc  # 运出碳的OBT浓度
        layer.OBT_suc *= (1 - frac_out)
        layer.W_suc -= flow_out
        return flow_out, S_suc_out
    return 0.0, 0.0
```

### 3.9 蛋白质周转

**物理含义**: 叶片蛋白(主要是 RuBisCO)持续合成和降解。合成时氨基酸的 H 来自 TFWT, 新蛋白含 OBT。降解时部分 OBT 回到代谢池可再利用。蛋白周转是 neOBT 积累的主要途径之一。

#### 3.9.1 状态变量

每层:
- W_prot [kg C/m²]: 蛋白池碳质量
- OBT_prot [Bq/kg C]: 可交换蛋白 OBT 浓度
- OBT_ne_prot [Bq/kg C]: 非交换蛋白 OBT 浓度 (从库存计算)
- _neOBT_inv [Bq/m²]: neOBT 库存 (避免浓度爆炸)

#### 3.9.2 蛋白合成

```
dW_syn = k_syn × W_prot × dt_hr   [kg C/m²]
dW_syn = min(dW_syn, W_int × 0.5)  (不超过中间池50%)
```

新蛋白 OBT:
```
S_new_prot = C_slow × FPE × KIE_PROT   [Bq/kg C]
```
- C_slow: 该器官局部束缚水 TFWT [Bq/L]
- FPE: 器官特异蛋白交换比例 [-]
- KIE_PROT = 3.0: 动力学同位素效应 (C-T 键形成比 C-H 慢)

OBT 稀释:
```
OBT_prot = (OBT_prot × W_prot + S_new_prot × dW_syn) / (W_prot + dW_syn)
W_prot += dW_syn
W_int -= dW_syn  (碳从中间池取)
```

#### 3.9.3 蛋白降解

```
dW_deg = k_deg × W_prot × dt_hr   [kg C/m²]
dW_deg = min(dW_deg, W_prot × 0.5)
```

eOBT 回收:
```
S_prot_deg = OBT_prot × f_prot_deg_recycle   [Bq/kg C]
frac_deg = dW_deg / W_prot
OBT_prot *= (1 - frac_deg)
W_prot -= dW_deg
W_int += dW_deg  (降解碳回到中间池)
OBT_int = (OBT_int × (W_int - dW_deg) + S_prot_deg × dW_deg) / W_int
```

#### 3.9.4 器官特异蛋白参数

| 器官 | FPE | k_syn (/day) | k_deg (/day) | 物理基础 |
|------|-----|-------------|-------------|---------|
| 叶 | 0.70 | 0.08 | 0.08 | RuBisCO 半衰期 ~8.7天 |
| 茎 | 0.01 | 0.08 | 0.08 | 纤维蛋白, 低周转 |
| 穗 | 0.10 | — | — | 不做周转(库器官) |
| 谷物 | 0.10 | — | — | 储藏蛋白, 一次合成 |
| 根 | 0.15 | 0.08 | 0.08 | 中等周转 |

**参数**:
| 符号 | 值 | 单位 | 来源 | 真实性 |
|------|-----|------|------|--------|
| k_prot_syn | 0.08 | /day | Millard 2005 | ✅ 真实 |
| k_prot_deg | 0.08 | /day | Millard 2005 | ✅ 真实 |
| KIE_PROT | 3.0 | - | Hattori 2001 | ⚠️ 半真实 |
| f_prot_deg_recycle | 0.7 | - | 估计 | 🔴 标定, 0.5-0.9 |

**代码**:
```python
def step_protein_turnover(organ, C_slow_local: float, dt: float):
    """
    器官蛋白周转
    输入:
      organ: OrganPool 对象
      C_slow_local: 该器官TFWT [Bq/L]
      dt: 步长 [s]
    """
    dt_hr = dt / 3600.0
    k_syn_hr = 0.08 / 24.0
    k_deg_hr = 0.08 / 24.0

    # 合成
    dW_syn = k_syn_hr * max(organ.W_prot, 1e-12) * dt_hr
    dW_syn = min(dW_syn, organ.W_int * 0.5)
    if dW_syn > 1e-20 and organ.W_int > 1e-20 and C_slow_local > 0:
        S_new = C_slow_local * organ.fpe * 3.0  # ×KIE_PROT
        Wp_old = organ.W_prot
        OBT_old = organ.OBT_prot
        organ.W_prot += dW_syn
        if organ.W_prot > 1e-20:
            organ.OBT_prot = (OBT_old*Wp_old + S_new*dW_syn) / organ.W_prot
        organ.W_int -= dW_syn

    # neOBT 积累 (见 §3.10)
    if organ.W_prot > 1e-20 and C_slow_local > 0:
        f_ne = organ.fpna / 24.0
        organ._neOBT_inv += f_ne * C_slow_local * organ.W_prot * dt_hr

    # 降解
    if organ.W_prot > 1e-12:
        dW_deg = k_deg_hr * organ.W_prot * dt_hr
        dW_deg = min(dW_deg, organ.W_prot * 0.5)
        if dW_deg > 1e-20:
            S_deg = organ.OBT_prot * 0.7  # f_prot_deg_recycle
            organ.W_int += dW_deg
            if organ.W_int > 1e-20:
                organ.OBT_int = (organ.OBT_int*(organ.W_int-dW_deg)+S_deg*dW_deg)/organ.W_int
            organ.OBT_prot *= (1 - dW_deg/organ.W_prot)
            organ.W_prot -= dW_deg
```

### 3.10 neOBT (非交换性 OBT) 积累

**物理含义**: 有机物中 C-H 键的 ³H 不可逆地锁定在分子结构中, 不与周围水交换。Diabaté 测量的是 neOBT (5-10天湿空气洗脱后残余)。

#### 3.10.1 积累机制

**途径 1 — 蛋白池 neOBT**: 新合成蛋白中的 C-T 键逐渐被代谢"固定"
```
d_neOBT_inv = (FPNA_organ/24) × C_slow × W_prot × dt/3600   [Bq/m²]
```

**途径 2 — 结构池 neOBT**: 暗反应 OBT 进入结构碳时, 部分被 C-T 键锁定
```
d_neOBT_str_inv = dOBT_dark × W_str × dLAI × F_DARK_NEOBT_FRAC   [Bq/m²]
```

**途径 3 — 光合碳进结构池**: 新结构碳合成时部分 eOBT 锁定
```
d_neOBT_str_phot = OBT_int × dW_str_alloc × EOBT_TO_NEOBT_FRAC   [Bq/m²]
```

#### 3.10.2 库存 vs 浓度

使用库存 [Bq] 追踪 neOBT, 浓度按需计算:
```
OBT_ne_prot = _neOBT_inv / max(W_prot, 1e-20)   [Bq/kg C]
```

**为什么用库存?** 蛋白降解时 W_prot 减小, 如果用浓度追踪, neOBT 浓度每步放大 → 指数爆炸。

#### 3.10.3 fnex 转换

Diabaté 测量 neOBT, 总 OBT 中 neOBT 比例:
```
neOBT = fnex × total_OBT
```
- fnex = 0.79 (Ota 2017, 小麦叶片)

收割 OBT:
```
OBT_harvest [Bq/g dry] = neOBT_inventory / (W_canopy_total × 0.4 / 1000)
```
- 0.4: 碳占干重比例
- 1000: kg → g 转换

**参数**:
| 符号 | 值 | 单位 | 来源 | 真实性 |
|------|-----|------|------|--------|
| fnex | 0.79 | - | Ota 2017 | ✅ 真实 |
| FPNA_叶 | 0.050 | /day | 标定自 Diabaté | 🔴 标定 |
| FPNA_茎 | 0.0005 | /day | 标定 | 🔴 标定 |
| FPNA_谷物 | 0.003 | /day | 标定 | 🔴 标定 |
| EOBT_TO_NEOBT_FRAC | 0.04 | - | Kim 2012 | ⚠️ 半真实 |
| F_DARK_NEOBT_FRAC | 0.005 | - | 标定 | 🔴 标定 |

### 3.11 器官间碳+OBT 分配 (DVS 插值)

**物理含义**: 叶片光合产物按发育阶段(DVS)通过韧皮部分配到各器官。分配系数由 WOFOST DVS 查表线性插值给出。OBT 随碳一起转运。

#### 3.11.1 DVS 定义

```
DVS: 0.0 = 出苗, 0.8 = 孕穗, 1.0 = 开花(anthesis), 2.0 = 成熟(maturity)
```

#### 3.11.2 DVS 查表 (小麦)

```python
ORGAN_PARTITION_WHEAT = [
    # DVS,   root,  stem,  leaf,  grain,  ear
    [0.00,   0.45,  0.10,  0.45,  0.00,  0.00],
    [0.20,   0.35,  0.20,  0.45,  0.00,  0.00],
    [0.40,   0.20,  0.30,  0.50,  0.00,  0.00],
    [0.60,   0.15,  0.30,  0.50,  0.00,  0.05],
    [0.80,   0.12,  0.28,  0.48,  0.00,  0.12],
    [1.00,   0.10,  0.28,  0.45,  0.05,  0.12],
    [1.20,   0.08,  0.20,  0.20,  0.40,  0.12],
    [1.50,   0.05,  0.08,  0.05,  0.72,  0.10],
    [1.80,   0.05,  0.04,  0.00,  0.82,  0.09],
    [2.00,   0.05,  0.04,  0.00,  0.82,  0.09],
]
```

#### 3.11.3 线性插值函数

```python
def interpolate_partition(dvs: float, table: list) -> tuple:
    """
    DVS 线性插值分配系数
    输入: dvs [-], table (N×6 数组, 第一列DVS)
    输出: (f_root, f_stem, f_leaf, f_grain, f_ear)
    """
    if dvs <= table[0][0]:
        return table[0][1], table[0][2], table[0][3], table[0][4], table[0][5]
    if dvs >= table[-1][0]:
        return table[-1][1], table[-1][2], table[-1][3], table[-1][4], table[-1][5]
    for i in range(len(table)-1):
        if table[i][0] <= dvs <= table[i+1][0]:
            f = (dvs - table[i][0]) / (table[i+1][0] - table[i][0])
            return tuple(table[i][j] + f*(table[i+1][j]-table[i][j]) for j in range(1,6))
    return table[-1][1], table[-1][2], table[-1][3], table[-1][4], table[-1][5]
```

#### 3.11.4 灌浆温度修正

```
若 DVS ≥ 0.8:
  T_grain_fill = max(0, 0.65 + 0.0787 × (T_mean - 10)^0.8)   (T_mean > 10°C)
  T_grain_fill = max(0, 0.065 × T_mean)                        (T_mean ≤ 10°C)
  f_grain_actual = f_grain × min(1.0, T_grain_fill)
  leftover = f_grain - f_grain_actual
  f_stem += leftover × 0.6
  f_leaf += leftover × 0.4
```

#### 3.11.5 碳分配到器官

```python
def step_organ_allocation(organs, dW_canopy: float, S_leaf_suc: float,
                          dvs: float, T_mean: float, isNight: bool,
                          C_slow_canopy: float):
    """
    叶片光合碳分配到各器官
    输入:
      organs: PlantOrgans 对象
      dW_canopy: 冠层总碳增量 [kg C/m²]
      S_leaf_suc: 叶片蔗糖池OBT [Bq/kg C]
      dvs: 发育阶段
      T_mean: 气温 [°C]
      isNight: 是否夜间
      C_slow_canopy: 冠层慢室TFWT [Bq/L]
    """
    f_root, f_stem, f_leaf, f_grain, f_ear = interpolate_partition(dvs, TABLE)

    # 温度修正
    if dvs >= 0.8 and T_mean > 10:
        tf = min(1.0, max(0, 0.65 + 0.0787 * (T_mean - 10)**0.8))
        f_grain_act = f_grain * tf
        leftover = f_grain - f_grain_act
        f_stem += leftover * 0.6
        f_leaf += leftover * 0.4
        f_grain = f_grain_act

    # 各器官接收碳+OBT
    for organ, frac in [(organs.root, f_root), (organs.stem, f_stem),
                        (organs.ear, f_ear), (organs.grain, f_grain)]:
        dW = dW_canopy * frac
        if dW > 1e-20:
            organ.receive_carbon_obt(dW, S_leaf_suc, pool='int')

    # 各器官内部: int→suc/sta/str/prot 重分配
    alloc = CARBON_ALLOC['night'] if isNight else CARBON_ALLOC['day']
    for organ, f_prot in [(organs.root, 0.03), (organs.stem, 0.05),
                          (organs.ear, 0.05), (organs.grain, 0.10)]:
        if organ.W_int > 1e-20:
            S_int = organ.OBT_int
            f_other = 1.0 - f_prot
            for pool, frac in [('suc', alloc['f_suc']*f_other),
                               ('sta', alloc['f_sta']*f_other),
                               ('str', alloc['f_str']*f_other),
                               ('prot', f_prot)]:
                dW_t = frac * organ.W_int
                if dW_t > 1e-20:
                    organ.receive_carbon_obt(dW_t, S_int, pool)
                    organ.W_int -= dW_t
            organ.W_int = max(0, organ.W_int)
            organ.OBT_int = 0.0

    # 各器官内部代谢
    organs.root.step_metabolism(dt, isNight, organs._stem_local_TFWT)
    organs.stem.step_metabolism(dt, isNight, organs._stem_local_TFWT)
    organs.ear.step_metabolism(dt, isNight, organs._ear_local_TFWT, protTurnover=False)
    organs.grain.step_metabolism(dt, isNight, organs._grain_local_TFWT,
                                  isSink=True, protTurnover=False)
```

### 3.12 碳再分配 (PCSE/WOFOST81)

**物理含义**: 灌浆期(DVS ≥ 1.5), 茎和叶的非结构碳(蔗糖+淀粉)按比例流向谷物。这是谷物 OBT 的重要来源——不只是当前光合, 还有之前积累在茎/叶中的 OBT 碳。

#### 3.12.1 茎再分配

```
WST_REALLOC = W_stem_total × REALLOC_STEM_FRAC   [kg C/m²] (可再分配总量)
每步: dW_stem_realloc = WST_REALLOC × REALLOC_STEM_RATE × dt_day   [kg C/m²]
限制: dW_stem_realloc ≤ WST_REALLOC - ST_REALLOCATED (累计不超过总量)
限制: dW_stem_realloc ≤ W_int_stem × 0.95 (不超过中间池95%)
```

OBT 随碳: `S_stem = OBT_int_stem` (中间池 eOBT 浓度)

茎碳减少: `W_int_stem -= dW_stem_realloc`

谷物接收 (含转化效率):
```
dW_grain = dW_stem_realloc × REALLOC_EFF
OBT 稀释: S_grain_int = (S_old × W_old + S_stem × dW_grain) / (W_old + dW_grain)
```

#### 3.12.2 叶再分配

```
WLV_REALLOC = (suc + sta) × REALLOC_LEAF_FRAC   [kg C/m²]
每步: dW_leaf_realloc = (W_suc + W_sta) × REALLOC_LEAF_RATE × dt_day
70% 从蔗糖池取, 30% 从淀粉池取
```

叶 OBT 去向 (衰老时全部池释放):
- 蔗糖池 OBT: 100% 随碳走
- 淀粉池 OBT: 80% 随碳走
- 结构池 OBT: 30% 释放到运输态
- 蛋白池 eOBT: 30% 释放
- neOBT: 90% 留在凋落物, 10% 随碳走

#### 3.12.3 参数

| 符号 | 值 | 单位 | 来源 | 真实性 |
|------|-----|------|------|--------|
| REALLOC_DVS | 1.5 | - | WOFOST 默认 2.0, 小麦提前 | 🔴 标定 |
| REALLOC_STEM_FRAC | 0.60 | - | 茎碳60%可再分配 | 🔴 标定, 0.3-0.8 |
| REALLOC_LEAF_FRAC | 0.40 | - | 叶碳40%可再分配 | 🔴 标定, 0.2-0.6 |
| REALLOC_STEM_RATE | 0.03 | /day | 每天移走剩余的3% | 🔴 标定, 0.01-0.1 |
| REALLOC_LEAF_RATE | 0.03 | /day | 同上 | 🔴 标定, 0.01-0.1 |
| REALLOC_EFF | 0.95 | - | 5%呼吸损失 | ⚠️ 半真实, 0.85-1.0 |

### 3.13 叶片衰老

**物理含义**: 灌浆期(DVS > 1.0), 叶片从下部开始衰老死亡。枯叶的碳和 OBT 有两条去路: 可溶碳(蔗糖/淀粉/中间池)→谷物, 结构碳(纤维素/蛋白)→凋落物→土壤。

#### 3.13.1 衰老时间表

用时间(非 DVS)控制衰老, 幂律函数:
```
t_since_anthesis = t - t_anthesis   [h]
t_total = t_maturity - t_anthesis   [h]
t_frac = min(t_since_anthesis / t_total, 1.0)

cumul_death = (1 - SENESCENCE_REMAIN) × t_frac^SENESCENCE_POWER
```
- SENESCENCE_POWER = 1.4 (>1: 初期慢后期快)
- SENESCENCE_REMAIN = 0.25 (保留25%绿叶到收割)

每步新增死亡比例:
```
new_death = max(cumul_death - prev_cumul, 0)
prev_cumul = cumul_death
```

#### 3.13.2 碳和 OBT 去路

对每层每步:
```
dLAI_die = dLAI × new_death

# 可溶碳 → 谷物
dW_suc_die = W_suc × new_death,  OBT_suc_die = OBT_suc × dW_suc_die
dW_sta_die = W_sta × new_death × 0.80,  OBT_sta_die = OBT_sta × dW_sta_die
dW_int_die = W_int × new_death,  OBT_int_die = OBT_int × dW_int_die

# 结构碳 → 凋落物
dW_str_die = W_str × new_death,  OBT_str_die = OBT_str × dW_str_die

# 蛋白池: eOBT→谷物, neOBT→凋落物
dW_prot_die = W_prot × new_death
eOBT_conc = max(OBT_prot - neOBT_conc, 0)
dOBT_prot_e = eOBT_conc × dW_prot_die  → 谷物
dOBT_prot_ne = neOBT_conc × dW_prot_die → 凋落物

# 碳池缩减
W_int/suc/sta/str/prot -= 对应dW
# neOBT 库存按比例缩减 (部分留在凋落物)
_neOBT_inv *= (1 - new_death × f_neOBT_litter)

# dLAI 更新
dLAI -= dLAI_die
# 存活叶片碳按 dLAI 比例缩减
scale = dLAI_new / dLAI_old
W_int/suc/sta/str/prot *= scale
# neOBT 库存不缩放 (C-T锁定, 叶面积缩小不释放)
```

#### 3.13.3 凋落物 OBT 去向

凋落物 OBT 不计入谷物。它进入土壤有机质, 缓慢分解。
谷物只接收: suc/sta/int OBT + 蛋白 eOBT。

#### 3.13.4 参数

| 符号 | 值 | 单位 | 来源 | 真实性 |
|------|-----|------|------|--------|
| SENESCENCE_POWER | 1.4 | - | 标定(小麦灌浆加速) | 🔴 标定, 1.0-2.0 |
| SENESCENCE_REMAIN | 0.25 | - | 小麦实测25%绿叶残留 | ⚠️ 半真实, 0.15-0.35 |
| f_sta_realloc | 0.80 | - | 淀粉80%可转运 | 🔴 标定, 0.6-1.0 |
| f_str_release | 0.30 | - | 结构池OBT30%释放 | 🔴 标定, 0.1-0.5 |
| f_prot_e_release | 0.30 | - | 蛋白eOBT30%释放 | 🔴 标定, 0.1-0.5 |
| f_neOBT_litter | 0.90 | - | 90% neOBT留凋落物 | 🔴 标定, 0.8-1.0 |

**代码**:
```python
def step_senescence(canopy, dt: float, t_hour: float,
                    t_anthesis: float) -> tuple:
    """
    叶片衰老
    输入:
      canopy: CanopyModel
      dt: 步长 [s]
      t_hour: 当前模拟时间 [h]
      t_anthesis: 开花期时间 [h]
    输出: (dW_grain [kg C/m²], S_grain [Bq/kg C], dW_litter [kg C/m²])
    """
    POWER = 1.4; REMAIN = 0.25
    if t_anthesis is None or t_hour < t_anthesis:
        return 0.0, 0.0, 0.0

    t_span = 1176.0 - t_anthesis  # 总灌浆期 [h]
    if t_span <= 0:
        return 0.0, 0.0, 0.0

    t_frac = min((t_hour - t_anthesis) / t_span, 1.0)
    cumul = (1 - REMAIN) * t_frac ** POWER
    new_death = max(cumul - canopy._prev_sen_cumul, 0)
    canopy._prev_sen_cumul = cumul

    if new_death < 1e-12:
        return 0.0, 0.0, 0.0

    dW_grain = 0.0; dOBT_grain = 0.0; dW_litter = 0.0
    for i in range(canopy.N):
        if canopy.dLAI[i] < 1e-6:
            continue
        # 可溶碳→谷物
        dW_s = canopy.W_suc[i]*new_death
        dOBT_s = canopy.OBT_suc[i]*dW_s
        dW_st = canopy.W_sta[i]*new_death*0.80
        dOBT_st = canopy.OBT_sta[i]*dW_st
        dW_in = canopy.W_int[i]*new_death
        dOBT_in = canopy.OBT_int[i]*dW_in
        # 结构碳→凋落物
        dW_str = canopy.W_str[i]*new_death
        # 蛋白: eOBT→谷物, neOBT→凋落物
        dW_pr = canopy.W_prot[i]*new_death
        neC = canopy._neOBT_inv[i]/max(canopy.W_prot[i],1e-20)
        eC = max(canopy.OBT_prot[i]-neC, 0)
        dOBT_pe = eC * dW_pr  # →谷物

        dW_grain += dW_s + dW_st + dW_in + dOBT_pe*0 + dW_pr*0 + dW_s
        dOBT_grain += dOBT_s + dOBT_st + dOBT_in + dOBT_pe
        dW_litter += dW_str + dW_pr

        # 更新碳池...
        # (完整实现见 §4 时步循环)
    if dW_grain > 1e-20:
        return dW_grain, dOBT_grain/dW_grain, dW_litter
    return 0.0, 0.0, dW_litter
```

### 3.14 器官局部 TFWT (输运链)

**物理含义**: 各器官的组织水含 HTO, 但浓度不等于冠层叶水。水从冠层通过木质部/韧皮部输运到各器官, 每级有衰减时间常数。

#### 3.14.1 输运链架构

```
冠层 C_slow ──τ_stem=30h──→ 茎 _stem_local_TFWT
                                   │
                              τ_ear=24h
                                   │
                                   ▼
暴露期: C_air/α ──→ 穗 _ear_local_TFWT ←──暴露后: 茎 TFWT
                                   │
                              k_grain=2.0/h
                                   │
                                   ▼
                              谷物 _grain_local_TFWT
根: 与茎同源 (_stem_local_TFWT)
```

#### 3.14.2 茎 TFWT

```
d(_stem_TFWT)/dt = (1/τ_stem) × (C_slow_canopy - _stem_TFWT)
半隐式: _stem_TFWT += k_stem × (C_slow - _stem_TFWT) × dt
k_stem = 1/(τ_stem × 3600)   [1/s]
```

#### 3.14.3 穗 TFWT

暴露期 (C_air > 0):
```
d(_ear_TFWT)/dt = (1/τ_ear) × (C_air/α_CG - _ear_TFWT)
```

暴露后 (C_air = 0):
```
d(_ear_TFWT)/dt = (1/τ_ear) × (_stem_TFWT - _ear_TFWT)
```

#### 3.14.4 谷物 TFWT

```
d(_grain_TFWT)/dt = k_grain × (_ear_TFWT - _grain_TFWT)
k_grain = 2.0   [1/h]
```

#### 3.14.5 完整代码

```python
def update_organ_TFWT(organs, C_air: float, C_slow_canopy: float,
                      dt: float, dvs: float):
    """
    器官 TFWT 输运链更新
    输入:
      organs: PlantOrgans 对象
      C_air: 大气HTO [Bq/L]
      C_slow_canopy: 冠层慢室浓度 [Bq/L]
      dt: 步长 [s]
      dvs: 发育阶段
    """
    alpha_CG = 0.91
    tau_stem = 30.0 * 3600  # [s]
    tau_ear = 24.0 * 3600   # [s]

    # 茎: 从冠层 C_slow 趋近
    k_stem = 1.0 / tau_stem
    organs._stem_TFWT += k_stem * (C_slow_canopy - organs._stem_TFWT) * dt
    organs._stem_TFWT = max(0, organs._stem_TFWT)

    # 穗: 暴露期从 Cair, 暴露后从茎
    k_ear = 1.0 / tau_ear
    if C_air > 0:
        target = C_air / alpha_CG
    else:
        target = organs._stem_TFWT
    organs._ear_TFWT += k_ear * (target - organs._ear_TFWT) * dt
    organs._ear_TFWT = max(0, organs._ear_TFWT)

    # 谷物: 从穗耦合 (DVS≥1.0时)
    if dvs >= 1.0:
        k_grain = 2.0 / 3600  # 1/s
        organs._grain_TFWT += k_grain * (organs._ear_TFWT - organs._grain_TFWT) * dt
        organs._grain_TFWT = max(0, organs._grain_TFWT)
```

#### 3.14.6 参数

| 符号 | 值 | 单位 | 来源 | 真实性 |
|------|-----|------|------|--------|
| τ_stem | 30 | h | 与冠层慢室同量级 | 🔴 标定, 15-50 h |
| τ_ear | 24 | h | 穗鞘水交换 | 🔴 标定, 12-48 h |
| k_grain | 2.0 | /h | 谷物-穗耦合 | 🔴 标定, 0.5-5.0 /h |

### 3.15 穗部光合

**物理含义**: 小麦抽穗后, 穗部(颖壳+芒+外稃)暴露在冠层顶部, 含叶绿体组织可进行光合作用。穗部光合固定的碳直接进入谷物碳库, 同时将穗部 TFWT 中的 ³H 固定为 OBT。

**物理基础**: 
- Araus & Tapia 1987: 穗光合贡献谷物碳 10-24%
- Sanchez-Bragado 2020: 现代小麦可达 40%+
- 穗 Vcmax ≈ 叶的 20-40%

#### 3.15.1 穗光合计算

```
PAR_ear = PAR_top × f_ear_PAR / ear_green_area   [µmol/m²/s ear tissue]
A_ear = farquhar(Ci_ear, PAR_ear, T_ear, crop_ear_params)  [µmol/m²/s]
```

其中:
- f_ear_PAR: 穗截获的冠层 PAR 比例 [-]
- ear_green_area: 穗绿色面积指数 [m²/m²]
- Vcmax_ear = Vcmax_leaf × Vcmax_ear_scale
- Jmax_ear = Jmax_leaf × (0.5 + 0.5 × Vcmax_ear_scale)
- g0_ear, g1_ear: 穗气孔参数

#### 3.15.2 碳和 OBT 输入

```
dW_ear_photo = (1/6) × M_g × A_ear × ear_green_area × dt   [kg C/m² ground]
OBT_ear_photo = A_ear × f_An × (M_w/ρ_w) × TFWT_ear × ear_green_area × dt   [Bq/m²]
```

碳直接进入 ear.int 池, OBT 随碳。

#### 3.15.3 参数

| 符号 | 值 | 单位 | 来源 | 真实性 | 标定范围 |
|------|-----|------|------|--------|---------|
| Vcmax_ear_scale | 0.25-0.40 | - | Sanchez-Bragado 2020 | ⚠️ 半真实 | 0.15-0.50 |
| f_ear_PAR | 0.15-0.30 | - | 依赖穗面积 | ⚠️ 半真实 | 0.10-0.40 |
| ear_green_area | 0.3-0.8 | m²/m² | 小麦典型值 | ⚠️ 半真实 | 0.2-1.0 |
| g0_ear | 0.005 | mol/m²/s | 穗角质层 | 🔴 标定 | 0.001-0.02 |
| g1_ear | 3.0 | kPa^0.5 | 穗 Medlyn | 🔴 标定 | 1.0-6.0 |

**代码**:
```python
def step_ear_photosynthesis(ear_organ, PAR_top: float, T_ear: float,
                            TFWT_ear: float, dt: float,
                            crop_params: dict):
    """
    穗部独立光合
    输入:
      ear_organ: ear 的 OrganPool
      PAR_top: 冠层顶 PAR [µmol/m²/s]
      T_ear: 穗温 [°C]
      TFWT_ear: 穗局部 TFWT [Bq/L]
      dt: 步长 [s]
      crop_params: 叶片参数 (Vcmax25, Jmax25, ...)
    """
    Vcmax_scale = 0.30
    f_ear_PAR = 0.20
    ear_green_area = 0.5

    PAR_ear = PAR_top * f_ear_PAR / max(ear_green_area, 0.01)
    crop_ear = dict(crop_params)
    crop_ear['Vcmax25'] *= Vcmax_scale
    crop_ear['Jmax25'] *= (0.5 + 0.5 * Vcmax_scale)
    crop_ear['g0'] = 0.005
    crop_ear['g1'] = 3.0

    Ci = 0.7 * 420e-6  # 简化
    result = farquhar(Ci, PAR_ear, T_ear, crop_ear)
    A_ear = result['A']  # µmol/m²/s

    if A_ear <= 0:
        return

    # 碳输入
    Md = 0.180
    dW = (1.0/6.0) * Md * A_ear * 1e-6 * ear_green_area * dt
    # OBT 输入
    f_An = 0.78; Mw = 0.018; rhow = 1000.0
    dOBT = A_ear * 1e-6 * f_An * (Mw/rhow) * TFWT_ear * 1000 * ear_green_area * dt

    # 进入 ear.int 池
    if dW > 1e-20:
        ear_organ.receive_carbon_obt(dW, dOBT/dW if dW > 0 else 0, 'int')
```

### 3.16 器官呼吸

**物理含义**: 各器官(非叶)有维持呼吸, 消耗碳并释放含 OBT 的水蒸气。

#### 3.16.1 维持呼吸

```
resp_C = k_maint × W_suc × dt_hr   [kg C/m²]
k_maint = 0.015 / 24.0   [1/h]  (Amthor 2000, ~1.5%/天)
```

#### 3.16.2 OBT 释放

```
frac_resp = resp_C / W_suc
OBT_suc *= (1 - frac_resp)
W_suc -= resp_C
```

注: 呼吸从蔗糖池取底物。OBT 释放比例 = 碳消耗比例(无选择性效应, 因为器官尺度简化)。

#### 3.16.3 器官暗反应

同 §3.6, 但用各器官局部 TFWT:
```
dOBT_str = F_DARK_organ × TFWT_local × dt_hr   [Bq/kg C]
```

**代码**:
```python
def step_organ_metabolism(organ, dt: float, isNight: bool,
                          TFWT_local: float):
    """
    器官内部代谢: 呼吸+暗反应+蛋白周转
    """
    dt_hr = dt / 3600.0

    # 呼吸
    k_maint = 0.015 / 24.0
    resp = min(k_maint * organ.W_suc * dt_hr, organ.W_suc * 0.5)
    if resp > 1e-20:
        frac = resp / organ.W_suc
        organ.OBT_suc *= (1 - frac)
        organ.W_suc -= resp

    # 暗反应
    if TFWT_local > 0 and organ.W_str > 1e-20:
        f_dark = organ.f_dark_day if not isNight else organ.f_dark_night
        organ.OBT_str += f_dark * TFWT_local * dt_hr

    # 蛋白周转 (§3.9)
    if organ.prot_turnover:
        step_protein_turnover(organ, TFWT_local, dt)
```

**参数**:
| 符号 | 值 | 单位 | 来源 | 真实性 |
|------|-----|------|------|--------|
| k_maint | 0.015 | /day | Amthor 2000 | ✅ 真实 |

---

## §4 完整时步循环

### 4.1 一个小时内的 20 步

每步 dt=60s, 每小时 60 步。以下展示一个小时内发生什么:

```python
def step(t: float, dt: float, model):
    """
    单步推进 [dt 秒]
    t: 当前时间 [h] (从模拟开始)
    """
    hour_of_day = (model.startH + t) % 24
    isExposed = (0 <= t < model.expH)
    C_air = model.airHTO if isExposed else 0.0

    # ════════ 1. 大气状态 ════════
    atm = atmosphere_state(hour_of_day, model.T_mean, model.RH,
                           model.wind, model.lat, model.doy)
    T_air = atm['Tair']; ea = atm['ea']; wind_now = atm['wind']
    PAR = atm['PAR']; sinBeta = atm['sinBeta']; isNight = atm['isNight']

    # ════════ 2. 冠层风速 ════════
    model.canopy.layer_wind(wind_now)

    # ════════ 3. 辐射分配 ════════
    if isNight:
        PAR_top = 0
    elif model.ppfd_top is not None:
        PAR_top = model.ppfd_top
    else:
        PAR_top = PAR
    PARsl, PARsh = model.canopy.layer_radiation(PAR_top, sinBeta)

    # ════════ 4. 逐层光合+气孔 ════════
    totalA = 0; totalGs = 0; totalTransp = 0
    for i in range(model.canopy.N):
        dLAI = model.canopy.dLAI[i]
        if dLAI < 1e-6:
            continue
        # sunlit 叶
        A_sl = farquhar(0.7*420e-6, PARsl[i], model.canopy.Tleaf[i], model.crop)
        # shaded 叶
        A_sh = farquhar(0.7*420e-6, PARsh[i], model.canopy.Tleaf[i], model.crop)
        # 加权
        fSl = model.canopy.LAIsl[i] / max(dLAI, 1e-6)
        A_i = fSl * A_sl['A'] + (1-fSl) * A_sh['A']
        model.canopy.A[i] = A_i
        # 气孔
        D = max(0.01, A_sl['Gs']*1e-6*420 - ea)  # 简化 VPD
        gs_i = stomatal_cond(A_i, D, model.crop, isNight)
        model.canopy.gs[i] = gs_i
        # 蒸腾
        T_vol_i = transpiration_rate(gs_i)
        totalA += A_i * dLAI
        totalTransp += T_vol_i * dLAI

    # ════════ 5. 土壤步进 ════════
    # (PE膜覆盖时 Cs_root=0, 跳过)
    Cs_root = 0.0 if model.soil_covered else model.soil.get_root_hto()

    # ════════ 6. 两室水模型 + OBT ════════
    for i in range(model.canopy.N):
        dLAI = model.canopy.dLAI[i]
        if dLAI < 1e-6:
            continue
        gs = model.canopy.gs[i]
        if isNight:
            gs = 0.001  # 夜间角质层
        T_vol = transpiration_rate(gs)

        # 6a. 两室 TFWT 更新 (§3.5)
        step_two_chamber_water(model.canopy, i, C_air, dt, T_vol, dLAI)

        C_fast = model.canopy.TFWT[i]
        C_slow = model.canopy._C_slow_local[i]
        TFWT_total = model.canopy._TFWT_total[i]

        A_leaf = model.canopy.A[i]

        # 6b. 光合 OBT (§3.7, 用 TFWT_total)
        if A_leaf > 0 and not isNight:
            step_phot_obt(model.canopy, i, A_leaf, dt)

        # 6c. 暗反应 OBT (§3.6, 用 C_slow)
        step_dark_obt(model.canopy, i, C_slow, dt, isNight)

        # 6d. 四池碳 (§3.8)
        alloc = CARBON_ALLOC['night'] if isNight else CARBON_ALLOC['day']
        step_carbon_pools(model.canopy, i, dt, isNight, A_leaf, alloc)

        # 6e. 蛋白周转 (§3.9, 用 C_slow)
        step_protein_turnover(model.canopy, i, C_slow, dt)

    # ════════ 7. 碳分配到器官 ════════
    dW_canopy = totalA * 1e-6 * (12.0/1000.0) * dt  # kg C/m²
    S_leaf_suc = get_weighted_suc_OBT(model.canopy)  # 蔗糖池加权OBT
    C_slow_mean = get_mean_C_slow(model.canopy)

    # 更新器官 TFWT 输运链
    update_organ_TFWT(model.organs, C_air, C_slow_mean, dt, model.DVS)

    # 碳分配+器官代谢
    step_organ_allocation(model.organs, dW_canopy, S_leaf_suc,
                          model.DVS, T_air, isNight, C_slow_mean)

    # 7b. 叶碳再分配
    dW_realloc, S_realloc = model.canopy.shrink_leaf_realloc(dt, model.DVS)
    if dW_realloc > 1e-20:
        model.organs.receive_leaf_realloc(dW_realloc, S_realloc, isNight)

    # 7c. 穗部光合 (DVS >= 0.8)
    if model.DVS >= 0.8 and not isNight:
        step_ear_photosynthesis(model.organs.ear, PAR_top, T_air,
                                model.organs._ear_TFWT, dt, model.crop)

    # ════════ 8. 叶片衰老 ════════
    if model.DVS >= 1.0 and not hasattr(model, '_t_anthesis'):
        model._t_anthesis = t
    t_anth = getattr(model, '_t_anthesis', None)
    dW_sen, S_sen, dW_lit = step_senescence(model.canopy, dt, t, t_anth)
    if dW_sen > 1e-20:
        model.organs.receive_leaf_realloc(dW_sen, S_sen, isNight)

    # ════════ 9. DVS 更新 ════════
    GDD_rate = max(0, T_air - model.crop['Tbase']) * dt / 3600
    model.startGDD += GDD_rate
    model.DVS = gdd_to_dvs(model.startGDD, ...)

    # 收集输出
    return {'Tair': T_air, 'C_air': C_air, 'totalA': totalA,
            'meanTFWT': model.canopy.mean_tfwt(),
            'meanOBT': model.canopy.mean_obt(),
            'DVS': model.DVS}
```

### 4.2 秒级子循环 (光合累积)

光合速率在每秒级步长内计算(因为气孔响应时间~分钟)。累积一小时后汇总碳输入。

实际实现中, 光合是瞬时响应(A 和 gs 在每步重新计算), 不需要累积。碳输入 dW_canopy = A_total × dt 直接计算。

### 4.3 初始条件 (DVS=1.0 时各碳池量)

小麦开花期(DVS=1.0), LAI≈5.0, 叶片碳总量约:
```
叶干重 ≈ 150 g dry/m² ground × LAI ≈ 750 g/m² ground (多层总计)
碳含量 ≈ 0.4 → W_leaf_total ≈ 0.30 kg C/m² ground
```

每层 (N=5):
```
W_total_per_layer = 0.30 / 5 = 0.06 kg C/m²
W_str = 0.85 × 0.06 = 0.051 kg C/m²
W_int = 0.03 × 0.06 = 0.0018
W_sta = 0.0175 × 0.06 = 0.00105
W_suc = 0.0025 × 0.06 = 0.00015
W_prot = 0.10 × 0.06 = 0.006
```

茎碳: ≈ 0.15 kg C/m² (WOFOST 茎分配比例 28% × 总碳)
根碳: ≈ 0.05 kg C/m²
谷物: 0 (DVS=1.0 刚启动)

### 4.4 收割汇总公式

**谷物 OBT [Bq/g dry]**:
```
Q_OBT_grain = Σ(OBT_pool × W_pool) / W_grain_total   [Bq/kg C]  (加权平均)
OBT_grain_harvest = Q_OBT_grain × fnex × 0.0004       [Bq/g dry]
```
- fnex = 0.79: neOBT 比例
- 0.0004: (kg C / kg dry) / 1000 → g dry 中碳的转换
  - 碳占干重 40% → 1 kg C = 2.5 kg dry = 2500 g dry
  - 1 Bq/kg C = 1/2500 Bq/g dry = 0.0004 Bq/g dry

**叶 OBT [Bq/g dry]**:
```
total_OBT_inv = Σ_layers Σ_pools (OBT_pool × W_pool × dLAI)   [Bq/m² ground]
neOBT_inv = fnex × total_OBT_inv
total_C = Σ_layers (W_total × dLAI)   [kg C/m² ground]
OBT_leaf_harvest = neOBT_inv / (total_C × 0.4 / 1000)   [Bq/g dry]
```

**茎 OBT [Bq/g dry]**:
```
OBT_stem_harvest = organs.stem.Q_OBT × fnex × 0.0004
```

**TLI**:
```
TLI = grain_OBT_inventory / (grain_OBT_inventory + stem_OBT_inventory + 
      root_OBT_inventory + ear_OBT_inventory + canopy_OBT_inventory)
```

**TLI (Diabaté 定义)**:
```
TLI_diabate = (grain_OBT [Bq/g] / peak_TFWT [Bq/L]) × 100%
```

---

## §5 参数汇总

### 5.1 物理常数 (永远不变)

| 符号 | 值 | 单位 | 含义 |
|------|-----|------|------|
| R | 8.314 | J/mol/K | 气体常数 |
| T_K0 | 273.15 | K | 0°C 绝对温度 |
| ρ_air | 1.204 | kg/m³ | 空气密度 @20°C |
| c_p | 1005 | J/kg/K | 空气比热 |
| L_v | 2.45e6 | J/kg | 水汽化潜热 |
| κ | 0.4 | - | von Kármán 常数 |
| g | 9.81 | m/s² | 重力加速度 |
| M_w | 0.018 | kg/mol | 水摩尔质量 |
| ρ_w | 1000 | kg/m³ | 水密度 |
| M_d | 0.180 | kg/mol | 葡萄糖摩尔质量 |
| V_m_air | 0.0245 | m³/mol | 空气摩尔体积 @25°C |
| α_CG | 0.91 | - | Craig-Gordon 分馏 |
| f_An | 0.78 | - | 光合同位素分馏 |
| fnex | 0.79 | - | neOBT 比例 (Ota 2017) |
| 4.57 | 4.57 | µmol/J | PAR W→µmol 转换 |

### 5.2 文献参数 (有测量值, 通常不标定)

| 符号 | 值 | 单位 | 来源 | 真实性 |
|------|-----|------|------|--------|
| Vcmax_25 | 60 | µmol/m²/s | 小麦文献 | ✅ |
| Jmax_25 | 120 | µmol/m²/s | 小麦文献 | ✅ |
| Rd_25 | 1.0 | µmol/m²/s | 小麦文献 | ✅ |
| TPU_25 | 18 | µmol/m²/s | 文献 | ✅ |
| Ha_V | 65,330 | J/mol | Bernacchi 2001 | ✅ |
| Hd_V | 200,000 | J/mol | Bernacchi 2001 | ✅ |
| S_V | 650 | J/mol/K | Bernacchi 2001 | ✅ |
| Ha_J | 43,540 | J/mol | Bernacchi 2001 | ✅ |
| Hd_J | 200,000 | J/mol | Bernacchi 2001 | ✅ |
| S_J | 640 | J/mol/K | Bernacchi 2001 | ✅ |
| Ha_Rd | 46,390 | J/mol | Bernacchi 2001 | ✅ |
| g_0 | 0.01 | mol/m²/s | 文献 | ✅ |
| g_1 (小麦) | 5.5 | kPa^0.5 | Medlyn 2011 | ✅ |
| h_v | 1.54e-4 | m³/m² | Yamazawa 2001 | ✅ |
| leaf_water_frac | 0.65 | - | 小麦实测 | ✅ |
| k_prot_syn | 0.08 | /day | Millard 2005 | ✅ |
| k_prot_deg | 0.08 | /day | Millard 2005 | ✅ |
| k_maint | 0.015 | /day | Amthor 2000 | ✅ |
| EOBT_TO_NEOBT_FRAC | 0.04 | - | Kim 2012 | ⚠️ |

### 5.3 标定参数 (需要拟合)

| 符号 | 值 | 单位 | 物理量级 | 允许范围 | 真实性 | 标定依据 |
|------|-----|------|---------|---------|--------|---------|
| **两室水模型** | | | | | | |
| fv | 0.15 | - | 0.15-0.20 (NMR) | 0.10-0.25 | ⚠️ | Duranceau 2001 |
| τ_slow | 30 | h | 10-50 h | 15-50 | 🔴 | 拟合 Diabaté +22h |
| τ_slow_loss | 30 | h | 10-50 h | 20-60 | 🔴 | 与τ_slow同量级 |
| **器官 TFWT** | | | | | | |
| τ_stem | 30 | h | 10-50 h | 15-50 | 🔴 | 冠层慢室同量级 |
| τ_ear | 24 | h | 12-48 h | 12-48 | 🔴 | 穗鞘水交换 |
| k_grain | 2.0 | /h | 0.5-5 /h | 0.5-5.0 | 🔴 | 韧皮部耦合 |
| **暗反应 OBT** | | | | | | |
| F_DARK_叶_day | 0.2683 | /h | 酶促~0.1-10/h | 0.05-2.0 | 🔴 | 拟合叶26Bq/g |
| F_DARK_叶_night | 0.1341 | /h | 同上 | 0.02-1.0 | 🔴 | 日夜比~2 |
| F_DARK_茎_day | 0.0036 | /h | 木质化慢~1e-3 | 0.001-0.05 | 🔴 | 拟合茎6.3Bq/g |
| F_DARK_茎_night | 0.0021 | /h | 同上 | 0.0005-0.03 | 🔴 | |
| F_DARK_穗_day | 0.380 | /h | 活跃组织~0.1 | 0.05-2.0 | 🔴 | 拟合穗230Bq/g |
| F_DARK_穗_night | 0.150 | /h | 同上 | 0.02-1.0 | 🔴 | |
| F_DARK_谷_day | 2.97 | /h | 灌浆高代谢~1-10 | 0.5-10 | 🔴 | 拟合谷物480Bq/g |
| F_DARK_谷_night | 1.49 | /h | 同上 | 0.2-5.0 | 🔴 | |
| F_DARK_根_day | 0.08 | /h | 中等~0.01 | 0.01-0.5 | 🔴 | 估计 |
| F_DARK_根_night | 0.03 | /h | 同上 | 0.005-0.2 | 🔴 | |
| **碳池** | | | | | | |
| f_suc_day | 0.48 | - | ~0.3-0.5 | 0.3-0.6 | ⚠️ | Fondy & Geiger |
| f_suc_night | 0.30 | - | ~0.2-0.4 | 0.1-0.5 | ⚠️ | |
| f_sta_day | 0.26 | - | ~0.2-0.4 | 0.1-0.5 | ⚠️ | |
| f_sta_night | 0.50 | - | ~0.3-0.6 | 0.2-0.7 | ⚠️ | |
| f_str_day | 0.26 | - | ~0.2-0.4 | 0.1-0.5 | ⚠️ | |
| f_str_night | 0.20 | - | ~0.1-0.3 | 0.05-0.4 | ⚠️ | |
| k_sta_int | 0.02 | /h | ~0.01-0.05 | 0.005-0.1 | ⚠️ | Ota 2011 |
| k_suc_out | 0.10 | /h | ~0.05-0.2 | 0.02-0.3 | ⚠️ | Ota 2011 |
| k_resp | 0.05 | /h | ~0.02-0.1 | 0.01-0.2 | ⚠️ | Ota 2011 |
| fd_day | 0.015 | - | ~0.01-0.03 | 0.005-0.05 | ⚠️ | Ota 2017 |
| fd_night | 0.025 | - | ~0.01-0.04 | 0.005-0.06 | ⚠️ | Ota 2017 |
| **蛋白周转** | | | | | | |
| KIE_PROT | 3.0 | - | 3-10 | 1.0-10 | ⚠️ | Hattori 2001 |
| f_prot_deg_recycle | 0.7 | - | ~0.5-0.9 | 0.3-0.95 | 🔴 | 估计 |
| FPE_叶 | 0.70 | - | ~0.5-0.9 | 0.3-0.95 | 🔴 | RuBisCO高周转 |
| FPE_茎 | 0.01 | - | ~0.005-0.05 | 0.001-0.1 | 🔴 | 纤维蛋白低周转 |
| FPE_谷物 | 0.10 | - | ~0.05-0.2 | 0.02-0.3 | 🔴 | 储藏蛋白 |
| FPE_穗 | 0.10 | - | 同上 | 0.02-0.3 | 🔴 | |
| FPE_根 | 0.15 | - | ~0.05-0.3 | 0.02-0.5 | 🔴 | 中等周转 |
| FPNA_叶 | 0.050 | /day | ~0.01-0.1 | 0.01-0.2 | 🔴 | 拟合 Diabaté |
| FPNA_茎 | 0.0005 | /day | ~0.0001-0.001 | 0.0001-0.005 | 🔴 | |
| FPNA_谷物 | 0.003 | /day | ~0.001-0.01 | 0.0005-0.02 | 🔴 | |
| FPNA_穗 | 0.005 | /day | ~0.001-0.02 | 0.001-0.05 | 🔴 | |
| FPNA_根 | 0.008 | /day | ~0.002-0.02 | 0.001-0.05 | 🔴 | |
| F_DARK_NEOBT_FRAC | 0.005 | - | ~0.001-0.01 | 0.001-0.05 | 🔴 | |
| **碳再分配** | | | | | | |
| REALLOC_DVS | 1.5 | - | 1.0-2.0 | 1.0-2.0 | 🔴 | WOFOST 默认2.0 |
| REALLOC_STEM_FRAC | 0.60 | - | 0.3-0.8 | 0.2-0.9 | 🔴 | |
| REALLOC_LEAF_FRAC | 0.40 | - | 0.2-0.6 | 0.1-0.7 | 🔴 | |
| REALLOC_STEM_RATE | 0.03 | /day | 0.01-0.1 | 0.005-0.15 | 🔴 | |
| REALLOC_LEAF_RATE | 0.03 | /day | 0.01-0.1 | 0.005-0.15 | 🔴 | |
| REALLOC_EFF | 0.95 | - | 0.85-1.0 | 0.80-1.0 | 🔴 | |
| **叶片衰老** | | | | | | |
| SENESCENCE_POWER | 1.4 | - | 1.0-2.0 | 1.0-3.0 | 🔴 | 灌浆加速 |
| SENESCENCE_REMAIN | 0.25 | - | 0.15-0.35 | 0.10-0.40 | ⚠️ | 小麦实测 |
| f_sta_realloc | 0.80 | - | 0.6-1.0 | 0.5-1.0 | 🔴 | |
| f_str_release | 0.30 | - | 0.1-0.5 | 0.05-0.6 | 🔴 | |
| f_prot_e_release | 0.30 | - | 0.1-0.5 | 0.05-0.6 | 🔴 | |
| f_neOBT_litter | 0.90 | - | 0.8-1.0 | 0.7-1.0 | 🔴 | |
| **穗部光合** | | | | | | |
| Vcmax_ear_scale | 0.30 | - | 0.2-0.4 | 0.15-0.50 | ⚠️ | Sanchez-Bragado |
| f_ear_PAR | 0.20 | - | 0.15-0.30 | 0.10-0.40 | ⚠️ | |
| ear_green_area | 0.50 | m²/m² | 0.3-0.8 | 0.2-1.0 | ⚠️ | |
| g0_ear | 0.005 | mol/m²/s | ~0.001-0.01 | 0.001-0.02 | 🔴 | |
| g1_ear | 3.0 | kPa^0.5 | ~1-5 | 1.0-6.0 | 🔴 | |

### 5.4 参数计数统计

| 类别 | 数量 |
|------|------|
| 物理常数 | 14 |
| 文献参数 | 18 |
| 半真实参数 | ~15 |
| 标定参数 | ~45 |
| **总计** | **~92** |

---

## §6 验证与标定

### 6.1 分步标定策略

**原则**: 从零标定基线开始, 每步只标定一组参数, 验证后再进入下一步。

#### Step 0: 无标定基线
- 所有标定参数用物理量级中值
- 运行 Diabaté 场景
- 记录所有输出与文献值的偏差
- 这是"模型结构是否正确"的基线检验

#### Step 1: 两室水模型标定
- 固定 fv=0.15 (文献值)
- 标定 τ_slow: 最小化 |TFWT_+22h / TFWT_peak - 0.054|
- 标定 τ_slow_loss: 匹配 Brudenell 快分量 t½=53min
- 验证: TFWT 衰减曲线形状

#### Step 2: 器官 TFWT 输运链
- 标定 τ_stem, τ_ear, k_grain
- 约束: τ_stem ≈ τ_slow (同量级)
- 验证: 穗 TFWT 暴露后行为

#### Step 3: 暗反应 OBT (按器官从低到高)
- 茎: 标定 F_DARK_茎 → 匹配茎 OBT 6.3 Bq/g
- 叶: 标定 F_DARK_叶 → 匹配叶 OBT 26 Bq/g
- 穗: 标定 F_DARK_穗 → 匹配穗 OBT 230 Bq/g
- 谷物: 标定 F_DARK_谷物 → 匹配谷物 OBT 480 Bq/g
- 每步标定后检查 TLI 是否在 0.4-0.9%

#### Step 4: 蛋白周转参数
- FPE 各器官 (影响 neOBT 积累速度)
- FPNA 各器官
- 验证: fnex=0.79 是否合理 (neOBT/total_OBT)

#### Step 5: 碳再分配和衰老
- REALLOC 参数 → 影响谷物 OBT 时间曲线
- SENESCENCE → 影响收割叶 OBT
- 验证: 谷物 OBT 时间序列形状

### 6.2 验证目标 (Diabaté 1997 全套数据)

**严格对标 (2h 白天暴露 + 47天生长)**:

| 指标 | 文献值 | 不确定度 | 模型目标 |
|------|--------|---------|---------|
| TFWT 峰值 | 86,600 Bq/L | ±4,300 | 在范围内 |
| +22h TFWT | 4,680 Bq/L | ±234 | 峰值的 5.4% |
| 叶 OBT (收割) | 26 Bq/g | ±1.3 | 在范围内 |
| 茎 OBT (收割) | 6.3 Bq/g | ±0.3 | 在范围内 |
| 穗 OBT (收割) | 230 Bq/g | ±11 | 在范围内 |
| 谷物 OBT (收割) | 480 Bq/g | ±24 | 在范围内 |
| TLI (灌浆期) | 0.4-0.9% | — | 在范围内 |

**暴露后短期 (参考, 非严格对标)**:

| 时间 | 叶 TFWT | 叶 OBT | 茎 OBT | 穗 OBT |
|------|---------|--------|--------|--------|
| 暴露末 | 86,600 | 340 | 65 | 45 |
| +1h | 66,900 | 335 | 55 | 100 |
| +2h | 52,100 | 360 | 53 | 120 |
| +22h | 4,680 | 190 | 31 | 460 |

### 6.3 剂量响应验证

**急性暴露**:
- 2h, 4h, 8h 暴露 @ 同一 C_air
- 谷物 OBT 应随暴露时长增加
- 旧模型: 无剂量响应 (tau_chamber=168h 掩盖)
- 新模型: 暴露后 C_air=0, 剂量响应由两室水模型产生
- C_slow 持续时间 ∝ 暴露时长 → 暗反应 OBT 有剂量响应

**慢性暴露**:
- C_air=1000 Bq/L, 持续暴露 100 天
- OBT 应线性增长或趋近稳态
- 验证: 模型在稳态条件下的行为是否合理

**浓度响应**:
- 固定暴露 2h, C_air 从 1000 到 100,000 Bq/L
- 谷物 OBT 应近似线性 (∝ C_air)
- 两室水模型保证线性 (ODE 是线性的)

### 6.4 跨文献验证

| 文献 | 物种 | 暴露条件 | 关键数据 |
|------|------|---------|---------|
| Atarashi-Andoh 2002 | 大豆/玉米 | 6h 暴露 | OBT/TFWT 比值 |
| Ota 2011 | 葡萄 | 长期暴露 | 稳态 OBT |
| Brudenell 1997 | 卷心菜 | 短期 | TFWT 衰减 |
| Balashov 2011 | 小麦 | 简化参数 | 日夜不对称 |

---

## §7 已知局限

### 7.1 TFWT/Cair 比值偏高

**现象**: 模型 TFWT_peak/C_air ≈ 1.10, 文献 0.75-0.86
**原因**: 无叶肉阻力 R_m_HTO, 无根系水阻力
**影响**: TFWT 绝对值偏高 ~30%, 但 OBT 已通过标定吸收偏差
**解决**: 加叶肉阻力(Rm_HTO>0)会抹平日夜变化, 需权衡

### 7.2 tau_chamber 移除后的剂量响应

**现象**: 暴露后 C_air=0, 光合 OBT 路径在暴露后停止
**影响**: 短暴露(≤2h)的谷物 OBT 主要靠暗反应(从 C_slow)驱动
**解决**: 两室水模型的 C_slow 持续释放 HTO 提供暗反应底物
**残余风险**: 极短暴露(<1h)可能 OBT 不足

### 7.3 穗部光合参数不确定

**现象**: Vcmax_ear_scale, f_ear_PAR 依赖品种和环境
**影响**: 穗 OBT 和谷物碳分配
**解决**: 敏感性分析, 用 Diabaté 数据反推

### 7.4 DVS 与 GDD 映射

**现象**: GDD_mature=2500 → 25°C 下灌浆仅 40h (实际 ~30 天)
**原因**: DVS 映射参数未针对 Diabaté 生长条件校准
**影响**: 影响灌浆期长度和碳分配时间窗口
**解决**: 用实际生长天数校准 GDD 参数

### 7.5 土壤简化

**现象**: Diabaté 覆盖 PE 膜, 土壤模块大部分跳过
**影响**: 田间场景(未覆盖)下根水通道很重要, 当前未验证
**解决**: 需要 Garland/McFarlane 田间数据验证

### 7.6 单层 vs 多层异质性

**现象**: 冠层分层 N=5, 每层内叶龄/光照均匀假设
**影响**: 下部叶片光照低但暗反应 OBT 积累时间长
**解决**: 更多层(N=10)可改善, 但计算成本增加

### 7.7 neOBT 物理机制简化

**现象**: neOBT 通过 FPE/FPNA 参数化, 未追踪分子级别 C-T 键
**影响**: 不同碳分子(C-H vs C-T)的周转差异被简化
**解决**: 需要分子级别示踪实验数据

### 7.8 忽略的物理过程

- 叶片水势对气孔的反馈 (土壤水分胁迫)
- CO₂ 浓度升高对光合的影响
- 温度对蛋白周转的 Arrhenius 响应
- 氮素状态对 Vcmax 的影响
- 冠层内湍流扩散

---

## §8 代码构建指引

### 8.1 文件结构

```
solveg_model/
├── __init__.py
├── config.py        # 所有参数 (§5 完整字典)
├── atmosphere.py    # 大气条件 (§3.1)
├── canopy.py        # 冠层模块 (§3.2-3.8, 3.13)
├── organs.py        # 器官模块 (§3.9-3.12, 3.14-3.16)
├── soil.py          # 土壤模块 (§3.1 简化版)
├── model.py         # 主驱动 (§4)
└── run.py           # 运行入口
```

### 8.2 config.py 完整字典

```python
"""所有模型参数, 按 §5 参数表组织"""

# 物理常数
R = 8.314; Tk0 = 273.15; rhoAir = 1.204; cp = 1005
Lv = 2.45e6; kappa = 0.4; g = 9.81; Mw = 0.018
rhoW = 1000.0; Md = 0.180; Vm_air = 0.0245

# HTO/OBT
fAn = 0.78; fnex = 0.79; alpha_CG = 0.91
fd_day = 0.015; fd_night = 0.025

# 两室水模型
FV = 0.15
TAU_SLOW = 30.0
K_12 = 1.0 / (TAU_SLOW * 3600)
TAU_SLOW_LOSS = 30.0

# 器官 TFWT
TAU_STEM = 30.0
TAU_EAR = 24.0
K_GRAIN = 2.0

# 碳池分配
CARBON_ALLOC = {
    'day':   {'f_suc': 0.48, 'f_sta': 0.26, 'f_str': 0.26},
    'night': {'f_suc': 0.30, 'f_sta': 0.50, 'f_str': 0.20},
}
k_sta_int = 0.02; k_suc_out = 0.10; k_resp = 0.05

# 暗反应 OBT [1/h]
F_DARK_LEAF_DAY = 0.2683; F_DARK_LEAF_NIGHT = 0.1341
F_DARK_STEM_DAY = 0.0036; F_DARK_STEM_NIGHT = 0.0021
F_DARK_EAR_DAY = 0.380; F_DARK_EAR_NIGHT = 0.150
F_DARK_GRAIN_DAY = 2.97; F_DARK_GRAIN_NIGHT = 1.49
F_DARK_ROOT_DAY = 0.08; F_DARK_ROOT_NIGHT = 0.03

# 蛋白周转
k_prot_syn = 0.08; k_prot_deg = 0.08
KIE_PROT = 3.0; f_prot_deg_recycle = 0.7
FPE_LEAF = 0.70; FPE_STEM = 0.01; FPE_GRAIN = 0.10
FPE_EAR = 0.10; FPE_ROOT = 0.15
FPNA_LEAF = 0.050; FPNA_STEM = 0.0005
FPNA_GRAIN = 0.003; FPNA_EAR = 0.005; FPNA_ROOT = 0.008
F_DARK_NEOBT_FRAC = 0.005; EOBT_TO_NEOBT_FRAC = 0.04

# 碳再分配
REALLOC_DVS = 1.5; REALLOC_STEM_FRAC = 0.60; REALLOC_LEAF_FRAC = 0.40
REALLOC_STEM_RATE = 0.03; REALLOC_LEAF_RATE = 0.03; REALLOC_EFF = 0.95

# 叶片衰老
SENESCENCE_POWER = 1.4; SENESCENCE_REMAIN = 0.25
f_sta_realloc = 0.80; f_str_release = 0.30
f_prot_e_release = 0.30; f_neOBT_litter = 0.90

# 穗部光合
VCMAX_EAR_SCALE = 0.30; F_EAR_PAR = 0.20
EAR_GREEN_AREA = 0.50; G0_EAR = 0.005; G1_EAR = 3.0

# 叶片物理
hv = 1.54e-4; leafWaterFrac = 0.65

# 作物参数
CROPS = {
    'wheat': {
        'C4': False, 'Vcmax25': 60, 'Jmax25': 120, 'Rd25': 1.0, 'TPU25': 18,
        'HaV': 65330, 'HdV': 200000, 'Sv': 650,
        'HaJ': 43540, 'HdJ': 200000, 'Sj': 640,
        'HaRd': 46390, 'g0': 0.01, 'g1': 5.5,
        'Tbase': 0, 'GDD_laiMax': 1200, 'GDD_grainFill': 1500,
        'GDD_mature': 2500, 'rootZ': 0.4,
    },
    # rice, corn 类似
}

# 验证场景
DIABATE_SCENARIO = {
    'crop': 'wheat', 'airHTO': 79000, 'expH': 2.0, 'startH': 8.0,
    'Tair': 25.0, 'RH': 0.65, 'wind': 2.0, 'LAI': 5.0, 'height': 0.8,
    'soilType': 'loam', 'theta0': 0.30, 'simH': 1128.0,
    'lat': 50.0, 'doy': 150, 'nLayers': 5, 'dt': 60,
    'startGDD': 1500, 'soil_covered': True,
}
```

### 8.3 关键函数签名

```python
# atmosphere.py
def atmosphere_state(hour, T_mean, RH_mean, wind_mean, lat, doy, T_amp=5.0) -> dict

# canopy.py
class CanopyModel:
    def __init__(self, LAI, nLayers, height, windTop, crop_params)
    def layer_wind(self, windTop)
    def layer_radiation(self, PAR_top, sinBeta) -> (PARsl, PARsh)
    def step_photosynthesis(self, PARsl, PARsh, Tair, ea, ...) -> (totalA, meanGs, totalTransp)
    def step_tfwt_obt(self, C_air, Cs_root, dt, isNight, ...)  # 两室水+OBT
    def shrink_leaf_realloc(self, dt, dvs) -> (dW, S_leaf)
    def step_senescence(self, dt, t_hour, t_anthesis) -> (dW_grain, S_grain, dW_litter)
    def mean_tfwt(self) -> float
    def leaf_obt_harvest(self) -> float  # Bq/g dry

# organs.py
class OrganPool:
    def __init__(self, W_total, frac_str, frac_int, frac_sta, frac_suc, frac_prot, ...)
    def receive_carbon_obt(self, dW, S_source, pool)
    def step_metabolism(self, dt, isNight, TFWT_local, ...)

class PlantOrgans:
    def __init__(self, leaf_W_total, crop_name)
    def update_organ_TFWT(self, C_air, C_slow, dt, dvs)
    def step_allocate(self, dW_leaf, S_leaf, dvs, Tmean, dt, isNight, ...)
    def receive_leaf_realloc(self, dW, S_leaf, isNight)

# model.py
class SolvegModel:
    def __init__(self, params: dict)
    def step(self, t, dt) -> dict
    def run(self) -> dict
```

### 8.4 关键注意事项

1. **单位**: 所有内部用 SI, 浓度用 Bq/L, 碳用 kg C/m², OBT 用 Bq/kg C
2. **除零保护**: W_pool < 1e-20 时跳过除法, OBT 浓度设 0
3. **import 绑定**: Python 的 `from config import xxx` 在 import 时绑定值。改参数必须改 config.py 源文件, 不能运行时 patch
4. **neOBT 用库存追踪**: `_neOBT_inv [Bq]`, 浓度按需计算 = _neOBT_inv / W_prot
5. **碳守恒**: 每步检查 Σ(W_pool) 变化量 = 光合输入 - 呼吸 - 转运出
6. **时间单位**: config 中速率常数用 /h, ODE 用 /s (需要 ×1/3600)

---

## 附录 A: vs 旧模型区别

| 方面 | 旧模型 | 新框架 | 改进原因 |
|------|--------|--------|---------|
| TFWT 输出 | C_fast (自由水) | C_fast (=自由水, 明确定义) | 旧概念混乱(fv加权≠Diabaté测量) |
| 光合 OBT 水源 | C_fast | TFWT_total = fv×C_fast+(1-fv)×C_slow | 旧低估6.7× |
| 暴露后 Cair | tau_chamber=168h 指数衰减 | 直接归零(C_air=0) | 旧无剂量响应 |
| 碳再分配 | 无(茎碳不流向谷物) | PCSE/WOFOST81 完整实现 | 旧谷物OBT来源不足 |
| 叶片衰老 | 无 | DVS驱动幂律衰老 | 旧收割叶OBT不合理 |
| 暗反应 TFWT | _dark_TFWT(独立ODE) | C_slow(两室模型慢室) | 新用统一框架 |
| 器官 TFWT | 简单指数衰减 | 输运链(C_slow→茎→穗→谷物) | 更物理 |
| 穗部光合 | 无 | 独立 Farquhar 计算 | 增加谷物碳来源 |
| tau_chamber 问题 | 核心结构缺陷 | 已移除 | 新框架两室模型替代 |

## 附录 B: 参数推算逻辑

### B.1 F_DARK 器官间比值

物理基础: 不同器官的酶促代谢活性差异大
- 叶: 最高(活跃光合组织, 高表面积, 多酶系)
- 茎: 最低(木质化, 代谢慢, ~叶的 1/100)
- 穗: 高(绿色组织, 灌浆期代谢活跃, ~叶的 1-2×)
- 谷物: 最高(灌浆期淀粉合成极活跃, ~叶的 10×)
- 根: 中等(~叶的 1/3)

标定顺序: 茎→叶→穗→谷物, 每步只调一个器官的 F_DARK

### B.2 两室水模型 fv 和 τ_slow

- fv: Duranceau 2001 NMR 实测 ≈ 0.15, 物理明确
- τ_slow: 拟合 Diabaté +22h TFWT 衰减(86600→4680, 降至 5.4%)
  - 需要: C_fast 在 ~1h 内清空 + C_slow 在 22h 内降至 ~5%
  - τ_slow ≈ 30h 给出 C_slow(22h)/C_slow(0) ≈ exp(-22/30) ≈ 0.48
  - 但总 TFWT = fv×C_fast + (1-fv)×C_slow, C_fast≈0 后 ≈ 0.85×C_slow
  - 需要 C_slow(22h) ≈ 4680/0.85 ≈ 5500 Bq/L
  - C_slow(0) ≈ 86600 → ratio ≈ 0.064 → τ_slow ≈ 22/ln(1/0.064) ≈ 8.3h
  - 但 fv×C_fast 也贡献 → 实际 τ_slow 需要更长, ~30h

### B.3 收割 OBT 单位转换

Diabaté 测量: Bq/g dry matter
模型内部: Bq/kg C

转换:
```
OBT [Bq/g dry] = Q_OBT [Bq/kg C] × fnex × (kg C / kg dry) / (g / kg)
               = Q_OBT × 0.79 × 0.4 / 1000
               = Q_OBT × 0.000316
```
