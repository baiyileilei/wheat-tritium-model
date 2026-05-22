#!/usr/bin/env python3
"""K_RECEP + K_RESP_OBT 扫描 — 修 DAF 曲线

扫描两个参数对 DAF grain OBT 的影响：
1. K_RECEP: grain receptivity 发育速率
2. K_RESP_OBT: canopy OBT 维护呼吸衰减率
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import importlib
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# ── Galeriu 2013 Table 3 实验数据 ──
GALERIU_DAF = [1, 6, 7, 12, 13, 15, 19, 21, 27, 33]
GALERIU_GRAIN = [51, 229, 179, 483, 474, 657, 447, 610, 543, 362]

DAF_LIST = [1, 6, 12, 15, 21, 27, 33]


def run_daf_with_params(k_recep, k_resp_obt_str=0.0):
    """跑一组 DAF 场景，返回 {daf: grain_OBT}"""
    # 动态修改 config
    from wheat_t import config as cfg
    cfg.K_RECEP = k_recep
    cfg.K_RESP_OBT_STR = k_resp_obt_str

    # 重新加载 model 和 organs（config 变了）
    from wheat_t import model as mdl
    from wheat_t import organs as org
    importlib.reload(cfg)
    importlib.reload(mdl)

    # 再次确保 config 值
    cfg.K_RECEP = k_recep
    cfg.K_RESP_OBT_STR = k_resp_obt_str

    results = {}
    for daf in DAF_LIST:
        from wheat_t.config import _make_daf_scenario
        params = _make_daf_scenario(daf)
        try:
            m = mdl.SolvegModel(params)
            r = m.run()
            results[daf] = r['final_grain_OBT']
        except Exception as e:
            results[daf] = float('nan')
            print(f"  DAF={daf} FAILED: {e}")
    return results


def scan_k_recep():
    """扫描 K_RECEP（固定 K_RESP_OBT=0）"""
    k_values = [0.002, 0.005, 0.008, 0.010, 0.015, 0.020, 0.030]
    all_results = {}

    for k in k_values:
        print(f"\n{'='*50}")
        print(f"K_RECEP = {k}")
        print(f"{'='*50}")
        res = run_daf_with_params(k)
        all_results[k] = res
        for daf, grain in sorted(res.items()):
            print(f"  DAF={daf:2d}: grain={grain:.1f} Bq/g")

    return k_values, all_results


def scan_k_resp_obt(k_recep_fixed=0.015):
    """扫描 K_RESP_OBT_STR（固定 K_RECEP）"""
    k_values = [0.0, 0.0005, 0.001, 0.002, 0.003, 0.005]
    all_results = {}

    for k in k_values:
        print(f"\n{'='*50}")
        print(f"K_RESP_OBT_STR = {k} (K_RECEP={k_recep_fixed})")
        print(f"{'='*50}")
        res = run_daf_with_params(k_recep_fixed, k)
        all_results[k] = res
        for daf, grain in sorted(res.items()):
            print(f"  DAF={daf:2d}: grain={grain:.1f} Bq/g")

    return k_values, all_results


def plot_results(k_values, all_results, scan_name, save_path):
    """画 DAF 曲线对比图"""
    fig, ax = plt.subplots(1, 1, figsize=(10, 6))

    # Galeriu 实验数据
    ax.scatter(GALERIU_DAF, GALERIU_GRAIN, c='black', s=80, zorder=5,
               label='Galeriu 2013 (exp)', marker='D')

    # 扫描结果
    cmap = plt.cm.viridis
    for i, k in enumerate(k_values):
        dafs = sorted(all_results[k].keys())
        grains = [all_results[k][d] for d in dafs]
        color = cmap(i / max(len(k_values) - 1, 1))
        ax.plot(dafs, grains, 'o-', color=color, label=f'{scan_name}={k}', markersize=5)

    ax.set_xlabel('DAF (Days After Flowering)', fontsize=12)
    ax.set_ylabel('Grain OBT (Bq/g DW)', fontsize=12)
    ax.set_title(f'{scan_name} Sensitivity — DAF Grain OBT', fontsize=14)
    ax.legend(fontsize=9, loc='upper left')
    ax.grid(True, alpha=0.3)
    ax.set_xlim(0, 38)

    plt.tight_layout()
    plt.savefig(save_path, dpi=150)
    print(f"\n📊 图已保存: {save_path}")
    plt.close()


if __name__ == '__main__':
    print("=" * 60)
    print("K_RECEP 扫描 (K_RESP_OBT=0)")
    print("=" * 60)
    k_recep_vals, k_recep_results = scan_k_recep()
    plot_results(k_recep_vals, k_recep_results, 'K_RECEP',
                 '/root/.openclaw/workspace/projects/solveg_model/wheat_t/scan_k_recep.png')

    print("\n\n")
    print("=" * 60)
    print("K_RESP_OBT_STR 扫描 (K_RECEP=0.015)")
    print("=" * 60)
    k_resp_vals, k_resp_results = scan_k_resp_obt()
    plot_results(k_resp_vals, k_resp_results, 'K_RESP_OBT',
                 '/root/.openclaw/workspace/projects/solveg_model/wheat_t/scan_k_resp_obt.png')

    # 汇总表
    print("\n\n" + "=" * 60)
    print("汇总: K_RECEP 扫描")
    print("=" * 60)
    print(f"{'K_RECEP':>10}", end="")
    for d in DAF_LIST:
        print(f"  DAF={d:2d}", end="")
    print()
    for k in k_recep_vals:
        print(f"{k:10.4f}", end="")
        for d in DAF_LIST:
            print(f"  {k_recep_results[k][d]:7.0f}", end="")
        print()

    print(f"\n{'Galeriu':>10}", end="")
    for d in DAF_LIST:
        idx = GALERIU_DAF.index(d) if d in GALERIU_DAF else -1
        if idx >= 0:
            print(f"  {GALERIU_GRAIN[idx]:7.0f}", end="")
        else:
            print(f"      --", end="")
    print()
