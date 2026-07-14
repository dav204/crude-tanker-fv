"""Amendment-2 driver — P/B proxy from SEC book value, ~2018 onward.

Sector-neutral pooled IC of cheapness (-P/B) vs 1q-forward USD total return,
over the long window the SEC book-value history affords. Same machinery as the
wide panel; signal is the proxy, with a filed-date no-look-ahead guard.

Run: PYTHONPATH=. .venv/bin/python -m backtest.run_proxy
"""

from __future__ import annotations

import datetime as dt

from .evaluate_wide import mean_t, wide_quarter_ic
from .loaders import bvps_at, load_bvps, load_prices, price_at, quarter_ends
from .panel import SECTOR_OF

PROXY_NAMES = ["TNK", "INSW", "SBLK", "GNK", "HSHP", "GLNG", "FLNG", "LPG", "NVGS"]
START = dt.date(2018, 1, 1)


def _fmt(x, nd=3):
    return "n/a" if x is None else f"{x:+.{nd}f}"


def main() -> int:
    bvps = load_bvps()
    prices = load_prices()
    last_price = max(d for s in prices.values() for d, _ in s)
    qe = quarter_ends(START, last_price)

    print(f"proxy names: {PROXY_NAMES}")
    print(f"window: {qe[0]} .. {qe[-1]}  ({len(qe)} quarter-ends)\n")
    print(f"{'asof':12}{'n':>4}{'sec':>4}{'IC_sectorN':>12}{'IC_raw':>10}{'ewPanel%':>10}")

    quarters = []
    for i in range(len(qe) - 1):
        t, t1 = qe[i], qe[i + 1]
        data = {}
        for nm in PROXY_NAMES:
            bv = bvps_at(bvps.get(nm, []), t)
            p0 = price_at(prices.get(nm, []), t)
            p1 = price_at(prices.get(nm, []), t1)
            if bv is None or bv <= 0 or p0 is None or p1 is None or p0 <= 0:
                continue
            pb = p0 / bv                      # price-to-book; cheap = low P/B
            data[nm] = (pb, p1 / p0 - 1.0, SECTOR_OF[nm])
        wq = wide_quarter_ic(data)
        if wq is None or wq.n_pooled < 4:
            continue
        wq.asof = t.isoformat()
        quarters.append(wq)
        print(f"{wq.asof:12}{len(data):>4}{wq.sectors:>4}"
              f"{_fmt(wq.ic_sector_neutral):>12}{_fmt(wq.ic_raw_panel):>10}{wq.ew_panel_ret*100:>+9.1f}")

    sn = [q.ic_sector_neutral for q in quarters]
    raw = [q.ic_raw_panel for q in quarters]
    m_sn, t_sn = mean_t(sn)
    m_raw, t_raw = mean_t(raw)
    nq = len([x for x in sn if x is not None])
    print("\n=== PRIMARY (Amendment 2, P/B proxy): sector-neutral pooled IC ===")
    print(f"mean IC {_fmt(m_sn)}   t {_fmt(t_sn,2)}   Nq={nq}")
    print("=== SECONDARY: raw whole-panel IC ===")
    print(f"mean IC {_fmt(m_raw)}   t {_fmt(t_raw,2)}   Nq={len([x for x in raw if x is not None])}")

    # exploratory: split-half stability (early vs late)
    half = nq // 2
    e_m, e_t = mean_t(sn[:half]); l_m, l_t = mean_t(sn[half:])
    print("\n=== EXPLORATORY: stability ===")
    print(f"early half mean IC {_fmt(e_m)} (Nq={half}); late half mean IC {_fmt(l_m)} (Nq={nq-half})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
