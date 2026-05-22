"""
wheat_t — 小麦氚传输模型

基于 SOLVEG v3 已标定内核。
新增模块：边界层导度、VPD 蒸腾修正、维管束、植物水力、碳周转、土壤 HTO
"""

from .model import SolvegModel
from .config import DIABATE_SCENARIO
from .canopy import CanopyModel, transpiration_rate
from .organs import PlantOrgans
