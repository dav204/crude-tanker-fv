"""Amendment-1 driver — wide USD shipping panel, sector-neutral pooled IC.

Run: PYTHONPATH=. .venv/bin/python -m backtest.run_wide
"""

from __future__ import annotations

from .evaluate import spearman
from .evaluate_wide import mean_t, wide_quarter_ic
from .loaders import load_pnav, load_prices, price_at, quarter_ends, signal_at
from .panel import PANEL, SECTOR_OF


def _fmt(x, nd=3):
    return "n/a" if x is None else f"{x:+.{nd}f}"


def main() -> int:
    pnav = load_pnav()
    prices = load_prices()
    names = list(PANEL)

    all_dates = [d for n in names for d, _ in pnav.get(n, [])]
    first = min(all_dates)
    last_price = max(d for s in prices.values() for d, _ in s)
    qe = quarter_ends(first, last_price)

    print(f"P/NAV window {min(all_dates)}..{max(all_dates)} | quarter-ends {len(qe)} "
          f"({qe[0]}..{qe[-1]})")
    print(f"universe: {len(names)} USD-listed names across "
          f"{len(set(SECTOR_OF.values()))} sectors\n")

    quarters = []
    per_sector_ic: dict[str, list[float]] = {}
    print(f"{'asof':12}{'pooled_n':>9}{'sectors':>8}{'IC_sectorN':>12}{'IC_rawpanel':>12}{'ewPanel%':>10}")
    for i in range(len(qe) - 1):
        t, t1 = qe[i], qe[i + 1]
        data = {}
        for nm in names:
            s = signal_at(pnav.get(nm, []), t)
            p0 = price_at(prices.get(nm, []), t)
            p1 = price_at(prices.get(nm, []), t1)
            if s is None or p0 is None or p1 is None or p0 <= 0:
                continue
            data[nm] = (s, p1 / p0 - 1.0, SECTOR_OF[nm])
        wq = wide_quarter_ic(data)
        if wq is None:
            continue
        wq.asof = t.isoformat()
        quarters.append(wq)
        print(f"{wq.asof:12}{wq.n_pooled:>9}{wq.sectors:>8}"
              f"{_fmt(wq.ic_sector_neutral):>12}{_fmt(wq.ic_raw_panel):>12}{wq.ew_panel_ret*100:>+9.1f}")
        # per-sector exploratory ICs
        for sec in set(SECTOR_OF.values()):
            members = [n for n in data if data[n][2] == sec]
            if len(members) >= 3:
                ic = spearman([-data[n][0] for n in members], [data[n][1] for n in members])
                if ic is not None:
                    per_sector_ic.setdefault(sec, []).append(ic)

    sn = [q.ic_sector_neutral for q in quarters]
    raw = [q.ic_raw_panel for q in quarters]
    m_sn, t_sn = mean_t(sn)
    m_raw, t_raw = mean_t(raw)

    print("\n=== PRIMARY (Amendment 1): sector-neutral pooled IC ===")
    print(f"mean IC {_fmt(m_sn)}   t {_fmt(t_sn,2)}   Nq={len([x for x in sn if x is not None])}")
    print("\n=== SECONDARY: raw whole-panel IC (cross-sector confounded) ===")
    print(f"mean IC {_fmt(m_raw)}   t {_fmt(t_raw,2)}   Nq={len([x for x in raw if x is not None])}")

    print("\n=== EXPLORATORY: per-sector mean IC (>=3 names that quarter) ===")
    for sec in sorted(per_sector_ic):
        m, t = mean_t(per_sector_ic[sec])
        print(f"  {sec:9} mean IC {_fmt(m)} t {_fmt(t,2)} (Nq={len(per_sector_ic[sec])})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
