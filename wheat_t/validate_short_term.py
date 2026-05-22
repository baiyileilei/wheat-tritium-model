"""短期验证：2h 暴露 → 72h 追踪，对比 Diabaté 1997 Table 3 数据。

用法:
    python -m wheat_t.validate_short_term
    python -m wheat_t.validate_short_term --night   # 夜间暴露
    python -m wheat_t.validate_short_term --plot     # 生成图表
"""
import sys
import os
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from wheat_t import config as cfg
from wheat_t.model import SolvegModel


def run_short_term(day_or_night='day', sim_h=72, plot=False):
    """跑 Diabaté 2h 暴露 → sim_h 追踪，对比短期数据。"""
    st = cfg.DIABATE_SHORT_TERM[day_or_night]
    expt = cfg.DIABATE_SCENARIO.copy()

    # 覆盖为短期验证参数
    # 注意: airHTO 单位是 Bq/L（不是 Bq/m³），用 DIABATE_SCENARIO 的标定值
    expt['simH'] = sim_h
    expt['expH'] = st['exposure_h']
    if day_or_night == 'night':
        expt['startH'] = 22.0  # 夜间暴露起始

    print(f"\n{'='*70}")
    print(f"短期验证: Diabaté 1997 {day_or_night.upper()} exposure")
    print(f"  曝光: {st['exposure_h']}h × {st['airHTO_Bq_L']:.0e} Bq/L")
    print(f"  模拟: {sim_h}h (曝光后追踪 {sim_h - st['exposure_h']}h)")
    print(f"{'='*70}")

    model = SolvegModel(expt)
    results = model.run(progress_every=50)

    ts = results['ts']
    harvest = results['harvest']

    # ── 短期数据对比 ──
    print(f"\n{'='*70}")
    print(f"短期 TFWT 衰减对比 ({day_or_night})")
    print(f"{'='*70}")
    print(f"  {'时间(h)':>8} | {'模型 TFWT':>12} {'实验 TFWT':>12} {'比值':>8}")
    print(f"  {'':>8} | {'(Bq/mL)':>12} {'(Bq/mL)':>12} {'':>8}")
    print("  " + "-" * 50)

    ts_arr = np.array(ts['t_h'])
    tfwt_arr = np.array(ts['leaf_tfwt'])
    exp_h = st['exposure_h']

    # 数据的时间参考: t=0 = 曝光结束，模型 t=0 = 曝光开始
    # 所以数据的 t_h 对应模型的 (t_h + exposure_h)

    for i, t_h in enumerate(st['times_h']):
        expt_val = st['leaf_hto'][i]
        if expt_val is None:
            continue
        # 模型时间 = 数据时间 + 曝光时长
        model_t = t_h + exp_h
        idx = np.argmin(np.abs(ts_arr - model_t))
        model_val = tfwt_arr[idx]
        ratio = model_val / expt_val if expt_val > 0 else float('nan')
        flag = " ✓" if 0.5 < ratio < 2.0 else " ✗"
        print(f"  {t_h:>8.1f} | {model_val:>12.0f} {expt_val:>12.0f} {ratio:>8.2f}{flag}")

    # ── 短期 OBT 对比 ──
    print(f"\n{'='*70}")
    print(f"短期 OBT 对比 ({day_or_night})")
    print(f"{'='*70}")
    print(f"  {'时间(h)':>8} | {'Leaf OBT':>12} {'实验':>12} {'Ear OBT':>12} {'实验':>12}")
    print(f"  {'':>8} | {'(Bq/g DW)':>12} {'':>12} {'(Bq/g DW)':>12} {'':>12}")
    print("  " + "-" * 60)

    leaf_obt_arr = np.array(ts['leaf_obt_str'])
    ear_obt_arr = np.array(ts['ear_obt'])

    for i, t_h in enumerate(st['times_h']):
        e_leaf = st['leaf_obt'][i]
        e_ear = st['ear_obt'][i]
        model_t = t_h + exp_h
        idx = np.argmin(np.abs(ts_arr - model_t))
        m_leaf = leaf_obt_arr[idx]
        m_ear = ear_obt_arr[idx]

        leaf_str = f"{m_leaf:>12.1f}" if e_leaf is not None else f"{'--':>12}"
        ear_str = f"{m_ear:>12.1f}" if e_ear is not None else f"{'--':>12}"
        e_leaf_str = f"{e_leaf:>12.1f}" if e_leaf is not None else f"{'--':>12}"
        e_ear_str = f"{e_ear:>12.1f}" if e_ear is not None else f"{'--':>12}"

        print(f"  {t_h:>8.1f} | {leaf_str} {e_leaf_str} {ear_str} {e_ear_str}")

    # ── OBT 产生量检查 ──
    # 曝光结束时 leaf OBT / HTO@2h × 100 应该 ≈ 1.25%
    idx_exposure_end = np.argmin(np.abs(ts_arr - exp_h))
    leaf_hto_at_end = tfwt_arr[idx_exposure_end]
    leaf_obt_at_end = leaf_obt_arr[idx_exposure_end]
    if leaf_hto_at_end > 0:
        obt_pct = leaf_obt_at_end / leaf_hto_at_end * 100
        target_pct = st['leaf_obt_pct']
        ratio_pct = obt_pct / target_pct if target_pct > 0 else float('nan')
        print(f"\n  OBT 产生量: {obt_pct:.3f}% of HTO (目标 {target_pct}%, 比值 {ratio_pct:.2f})")

    # ── 收割对比 ──
    print(f"\n{'='*70}")
    print(f"收割对比 ({day_or_night}, {st['harvest_d']}天)")
    print(f"{'='*70}")
    print(f"  {'指标':>12} | {'模型':>10} {'实验':>10} {'比值':>8}")
    print("  " + "-" * 45)

    harvest_data = st['harvest']
    for key, expt_val in harvest_data.items():
        model_key = f'{key}_OBT_Bq_g'
        model_val = harvest.get(model_key, 0)
        ratio = model_val / expt_val if expt_val > 0 else float('nan')
        flag = " ✓" if 0.5 < ratio < 2.0 else " ✗"
        print(f"  {key:>12} | {model_val:>10.1f} {expt_val:>10.1f} {ratio:>8.2f}{flag}")

    # ── TLI ──
    tli = harvest.get('TLI_diabate_pct', 0)
    tli_target = st['tli_pct']
    tli_ratio = tli / tli_target if tli_target > 0 else float('nan')
    print(f"  {'TLI':>12} | {tli:>10.3f}% {tli_target:>9.3f}% {tli_ratio:>8.2f}")

    # ── 图表 ──
    if plot:
        try:
            import matplotlib
            matplotlib.use('Agg')
            import matplotlib.pyplot as plt

            fig, axes = plt.subplots(2, 2, figsize=(14, 10))
            fig.suptitle(f'Diabaté 1997 Short-term Validation ({day_or_night})', fontsize=14)

            # TFWT decay
            ax = axes[0, 0]
            ax.plot(ts_arr, tfwt_arr, 'b-', linewidth=1.5, label='Model')
            for i, t_h in enumerate(st['times_h']):
                v = st['leaf_hto'][i]
                if v is not None:
                    ax.plot(t_h, v, 'ro', markersize=8)
            ax.set_xlabel('Time (h)')
            ax.set_ylabel('Leaf TFWT (Bq/mL)')
            ax.set_title('TFWT Decay')
            ax.legend()
            ax.set_yscale('log')
            ax.set_ylim(1, 200000)

            # Leaf OBT
            ax = axes[0, 1]
            ax.plot(ts_arr, leaf_obt_arr, 'r-', linewidth=1.5, label='Model leaf OBT_str')
            for i, t_h in enumerate(st['times_h']):
                v = st['leaf_obt'][i]
                if v is not None:
                    ax.plot(t_h, v, 'bo', markersize=8)
            ax.set_xlabel('Time (h)')
            ax.set_ylabel('Leaf OBT (Bq/g DW)')
            ax.set_title('Leaf OBT')
            ax.legend()

            # Ear OBT
            ax = axes[1, 0]
            ax.plot(ts_arr, ear_obt_arr, 'g-', linewidth=1.5, label='Model ear OBT')
            for i, t_h in enumerate(st['times_h']):
                v = st['ear_obt'][i]
                if v is not None:
                    ax.plot(t_h, v, 'ro', markersize=8)
            ax.set_xlabel('Time (h)')
            ax.set_ylabel('Ear OBT (Bq/g DW)')
            ax.set_title('Ear OBT')
            ax.legend()

            # Grain OBT (full trajectory)
            ax = axes[1, 1]
            grain_arr = np.array(ts['grain_obt'])
            ax.plot(ts_arr, grain_arr, 'm-', linewidth=1.5, label='Model grain OBT')
            ax.set_xlabel('Time (h)')
            ax.set_ylabel('Grain OBT (Bq/g DW)')
            ax.set_title('Grain OBT')
            ax.legend()

            plt.tight_layout()
            out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                    f'output/short_term_{day_or_night}.png')
            os.makedirs(os.path.dirname(out_path), exist_ok=True)
            plt.savefig(out_path, dpi=150)
            plt.close()
            print(f"\n  图表已保存: {out_path}")
        except ImportError:
            print("\n  matplotlib 不可用，跳过图表")

    return results


def main():
    import argparse
    parser = argparse.ArgumentParser(description='Diabaté 1997 短期验证')
    parser.add_argument('--night', action='store_true', help='夜间暴露')
    parser.add_argument('--plot', action='store_true', help='生成图表')
    parser.add_argument('--simH', type=float, default=72, help='模拟时长 (h)')
    args = parser.parse_args()

    mode = 'night' if args.night else 'day'
    run_short_term(mode, sim_h=args.simH, plot=args.plot)


if __name__ == '__main__':
    main()
