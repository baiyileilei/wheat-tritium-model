"""
plant_water.py — 维管束慢组分 + 植物水力（根→茎）

新模块（v3 没有）：
- VascularWater: Brudenell 1997 双指数衰减慢组分 (τ=15h)
- PlantWater: 根系吸水 → 木质部 → 茎 (τ=10h)
"""

import math


class VascularWater:
    """全株维管束水池。匹配 Brudenell 1997 慢组分 t½≈15h"""

    def __init__(self, tau_vascular=15.0):
        self.C = 0.0  # Bq/L
        self.tau = tau_vascular  # h

    def step(self, C_slow_mean, dt):
        """C_slow_mean: 冠层 LAI 加权平均 C_bnd [Bq/L]"""
        k = 1.0 / (self.tau * 3600)
        self.C += k * (C_slow_mean - self.C) * dt
        self.C = max(0, self.C)


class PlantWater:
    """
    根系吸水 → 木质部 → 茎。

    慢性暴露核心路径。一阶滞后近似。
    """

    def __init__(self, tau_root=10.0):
        self.C_xylem = 0.0  # 茎木质部水 [Bq/L]
        self.tau = tau_root  # h

    def step(self, C_soil_root, dt, uptake_eff=0.5):
        """C_soil_root: 根区土壤加权平均 HTO [Bq/L]
        uptake_eff: 根系 HTO 吸收效率 (选择性 + 木质部稀释)
        """
        k = 1.0 / (self.tau * 3600)
        C_target = C_soil_root * uptake_eff
        self.C_xylem += k * (C_target - self.C_xylem) * dt
        self.C_xylem = max(0, self.C_xylem)
