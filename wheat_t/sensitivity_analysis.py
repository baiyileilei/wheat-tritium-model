#!/usr/bin/env python3
"""敏感性分析 — SOLVEG-II 参数扫描

扫描 4 个参数对 OBT 的影响：
1. HTO 浓度 (10²-10⁶ Bq/L)
2. 暴露时长 (1-720h)
3. 温度 (10-35°C)
4. LAI (1-8)

输出：表格 + 图
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from wheat_t.config import DIABATE_SCENARIO
from wheat_t.model import SolvegModel


def run_with_overrides(**overrides):
    """用指定参数运行 Diabaté 场景"""
    params = {k: v for k, v in DIABATE_SCENARIO.items()
              if k not in ['expected_TFWT_peak_ratio', 'expected_TFWT_halflife',
                           'expected_OBT', 'expected_day_night_ratio']}
    params.update(overrides)
    model = SolvegModel(params)
    results = model.run()
    h = results.get('harvest', {})
    return {
        'grain_OBT': h.get('grain_OBT_Bq_g', 0),
        'leaf_OBT': h.get('leaf_OBT_Bq_g', 0),
        'stem_OBT': h.get('stem_OBT_Bq_g', 0),
        'ear_OBT': h.get('ear_OBT_Bq_g', 0),
        'peak_TFWT': h.get('peak_TFWT_Bq_L', 0),
        'TLI': h.get('TLI_diabate_pct', 0) / 100.0,
    }


def scan_hto_concentration():
    """扫描 HTO 浓度"""
    hto_values = [100, 500, 1000, 5000, 10000, 50000, 100000, 500000, 1000000]
    results = []
    for hto in hto_values:
        try:
            r = run_with_overrides(airHTO=hto)
            results.append({'param': hto, **r})
            print(f"  HTO={hto:10.0e}: grain={r['grain_OBT']:.1f} Bq/g")
        except Exception as e:
            results.append({'param': hto, 'grain_OBT': float('nan')})
            print(f"  HTO={hto:10.0e}: FAILED {e}")
    return results


def scan_exposure_duration():
    """扫描暴露时长"""
    exp_values = [0.5, 1, 2, 4, 8, 24, 48, 168, 720]
    results = []
    for exp in exp_values:
        try:
            sim_h = max(720, exp + 500)
            r = run_with_overrides(expH=exp, simH=sim_h)
            results.append({'param': exp, **r})
            print(f"  expH={exp:6.1f}h: grain={r['grain_OBT']:.1f} Bq/g")
        except Exception as e:
            results.append({'param': exp, 'grain_OBT': float('nan')})
            print(f"  expH={exp:6.1f}h: FAILED {e}")
    return results


def scan_temperature():
    """扫描温度"""
    temp_values = [10, 15, 20, 25, 30, 35]
    results = []
    for t in temp_values:
        try:
            r = run_with_overrides(Tair=t)
            results.append({'param': t, **r})
            print(f"  T={t:4.0f}°C: grain={r['grain_OBT']:.1f} Bq/g")
        except Exception as e:
            results.append({'param': t, 'grain_OBT': float('nan')})
            print(f"  T={t:4.0f}°C: FAILED {e}")
    return results


def scan_lai():
    """扫描 LAI"""
    lai_values = [1, 2, 3, 4, 5, 6, 7, 8]
    results = []
    for lai in lai_values:
        try:
            r = run_with_overrides(LAI=lai)
            results.append({'param': lai, **r})
            print(f"  LAI={lai:4.1f}: grain={r['grain_OBT']:.1f} Bq/g")
        except Exception as e:
            results.append({'param': lai, 'grain_OBT': float('nan')})
            print(f"  LAI={lai:4.1f}: FAILED {e}")
    return results


def plot_sensitivity(all_results, save_dir):
    """画 4 张敏感性分析子图"""
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))

    # HTO 浓度
    ax = axes[0, 0]
    data = all_results['hto']
    x = [d['param'] for d in data]
    y = [d['grain_OBT'] for d in data]
    ax.semilogx(x, y, 'bo-', markersize=6)
    ax.set_xlabel('HTO Concentration (Bq/L)', fontsize=11)
    ax.set_ylabel('Grain OBT (Bq/g DW)', fontsize=11)
    ax.set_title('(a) HTO Concentration Sensitivity', fontsize=12)
    ax.grid(True, alpha=0.3)

    # 暴露时长
    ax = axes[0, 1]
    data = all_results['duration']
    x = [d['param'] for d in data]
    y = [d['grain_OBT'] for d in data]
    ax.semilogx(x, y, 'rs-', markersize=6)
    ax.set_xlabel('Exposure Duration (h)', fontsize=11)
    ax.set_ylabel('Grain OBT (Bq/g DW)', fontsize=11)
    ax.set_title('(b) Exposure Duration Sensitivity', fontsize=12)
    ax.grid(True, alpha=0.3)

    # 温度
    ax = axes[1, 0]
    data = all_results['temperature']
    x = [d['param'] for d in data]
    y = [d['grain_OBT'] for d in data]
    ax.plot(x, y, 'g^-', markersize=8)
    ax.set_xlabel('Temperature (°C)', fontsize=11)
    ax.set_ylabel('Grain OBT (Bq/g DW)', fontsize=11)
    ax.set_title('(c) Temperature Sensitivity', fontsize=12)
    ax.grid(True, alpha=0.3)

    # LAI
    ax = axes[1, 1]
    data = all_results['lai']
    x = [d['param'] for d in data]
    y = [d['grain_OBT'] for d in data]
    ax.plot(x, y, 'mD-', markersize=6)
    ax.set_xlabel('Leaf Area Index (LAI)', fontsize=11)
    ax.set_ylabel('Grain OBT (Bq/g DW)', fontsize=11)
    ax.set_title('(d) LAI Sensitivity', fontsize=12)
    ax.grid(True, alpha=0.3)

    plt.suptitle('SOLVEG-II Sensitivity Analysis — Diabaté 1997 Baseline', fontsize=14, y=1.02)
    plt.tight_layout()
    path = os.path.join(save_dir, 'sensitivity_analysis.png')
    plt.savefig(path, dpi=150, bbox_inches='tight')
    print(f"\n📊 敏感性分析图: {path}")
    plt.close()


def print_table(all_results):
    """打印汇总表格"""
    print("\n" + "=" * 70)
    print("敏感性分析汇总表")
    print("=" * 70)

    for name, label in [('hto', 'HTO 浓度 (Bq/L)'), ('duration', '暴露时长 (h)'),
                         ('temperature', '温度 (°C)'), ('lai', 'LAI')]:
        print(f"\n{label}:")
        print(f"  {'参数值':>12s}  {'Grain OBT':>10s}  {'Leaf OBT':>10s}  {'Peak TFWT':>12s}  {'TLI':>8s}")
        print(f"  {'-'*12}  {'-'*10}  {'-'*10}  {'-'*12}  {'-'*8}")
        for d in all_results[name]:
            print(f"  {d['param']:12.1f}  {d.get('grain_OBT', float('nan')):10.1f}  {d.get('leaf_OBT', float('nan')):10.1f}  {d.get('peak_TFWT', float('nan')):12.0f}  {d.get('TLI', 0)*100:8.3f}%")


if __name__ == '__main__':
    save_dir = '/root/.openclaw/workspace/projects/solveg_model/wheat_t'

    print("=" * 60)
    print("SOLVEG-II 敏感性分析")
    print("=" * 60)

    all_results = {}

    print("\n[1/4] HTO 浓度扫描")
    all_results['hto'] = scan_hto_concentration()

    print("\n[2/4] 暴露时长扫描")
    all_results['duration'] = scan_exposure_duration()

    print("\n[3/4] 温度扫描")
    all_results['temperature'] = scan_temperature()

    print("\n[4/4] LAI 扫描")
    all_results['lai'] = scan_lai()

    print_table(all_results)
    plot_sensitivity(all_results, save_dir)

    # 保存数据为 CSV
    import csv
    csv_path = os.path.join(save_dir, 'sensitivity_data.csv')
    with open(csv_path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['scan_type', 'param', 'grain_OBT', 'leaf_OBT', 'stem_OBT', 'ear_OBT', 'peak_TFWT', 'TLI'])
        for name, data in all_results.items():
            for d in data:
                writer.writerow([name, d['param'], d.get('grain_OBT', ''), d.get('leaf_OBT', ''),
                                 d.get('stem_OBT', ''), d.get('ear_OBT', ''),
                                 d.get('peak_TFWT', ''), d.get('TLI', '')])
    print(f"\n📊 CSV 数据: {csv_path}")
