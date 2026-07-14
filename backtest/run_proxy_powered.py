"""Amendment-3 driver — Sharadar deep-history P/B proxy on the actual watchlist.

Sector-neutral pooled IC of cheapness (-P/B) vs 1q-forward total return, over
the deep window Sharadar's standardized FPI fundamentals afford (17 watchlist
names incl. the 5 crude flagships + full product). Same machinery as the wide
panel / Amendment-2 proxy; only the data source (Sharadar cache) and universe
change. Method + decision rule locked in PRE_REGISTRATION.md Amendment 3.

Run: PYTHONPATH=. .venv/bin/python -m backtest.run_proxy_powered
"""

from __future__ import annotations

import datetime as dt
import random

from .evaluate_wide import mean_t, wide_quarter_ic
from .loaders import bvps_at, price_at, quarter_ends
from .loaders_sharadar import (
    SECTOR_OF, cache_available, cache_provenance, load_bvps, load_prices,
)

START = dt.date(2008, 1, 1)
PERIOD_STALENESS_DAYS = 550        # annual book carries across the year (incl. a late-filing Q1)
MIN_POOLED = 4                     # usable-quarter filter (matches run_proxy.py)
BOOT_BLOCK = 4                     # quarter-block bootstrap — params locked in pre-registration
BOOT_B = 10000
BOOT_SEED = 20260622


def _fmt(x, nd=3):
    return "n/a" if x is None else f"{x:+.{nd}f}"


def block_bootstrap_ci(ics: list[float], block: int = BOOT_BLOCK,
                       B: int = BOOT_B, seed: int = BOOT_SEED):
    xs = [x for x in ics if x is not None]
    n = len(xs)
    if n < block:
        return None, None
    blocks = [xs[i:i + block] for i in range(0, n, block)]   # non-overlapping
    rng = random.Random(seed)
    means = []
    for _ in range(B):
        sample: list[float] = []
        while len(sample) < n:
            sample.extend(rng.choice(blocks))
        sample = sample[:n]
        means.append(sum(sample) / len(sample))
    means.sort()
    return means[int(0.025 * B)], means[int(0.975 * B)]


def verdict(mean_ic, t) -> str:
    if mean_ic is None or t is None:
        return "INCONCLUSIVE (insufficient quarters)"
    if mean_ic > 0 and t >= 2.0:
        return "EDGE (premise supported)"
    if mean_ic <= 0 and abs(t) < 2.0:
        return "NO-EDGE"
    extra = " [significant NEGATIVE — anti-value, noted]" if (mean_ic < 0 and abs(t) >= 2.0) else ""
    return "INCONCLUSIVE" + extra


def main() -> int:
    if not cache_available():
        print("Sharadar cache not found (set FACTOR_PORTFOLIO_ROOT or clone the "
              "factor-portfolio repo). Nothing to run.")
        return 2

    bvps = load_bvps()
    prices = load_prices()
    print(f"Sharadar cache provenance: {cache_provenance()}")
    print(f"names with BVPS: {sorted(bvps)}  (n={len(bvps)})")
    print(f"names with prices: {sorted(prices)}  (n={len(prices)})\n")

    print("per-name coverage (BVPS period range / price range):")
    for nm in sorted(SECTOR_OF):
        b = bvps.get(nm, []); p = prices.get(nm, [])
        brange = f"{b[0][1]}..{b[-1][1]}" if b else "—"
        prange = f"{p[0][0]}..{p[-1][0]}" if p else "—"
        print(f"  {nm:5} {SECTOR_OF[nm]:14} BVPS[{brange:24}] px[{prange}]")

    last_price = max(d for s in prices.values() for d, _ in s)
    qe = quarter_ends(START, last_price)
    print(f"\nwindow: {qe[0]} .. {qe[-1]}  ({len(qe)} quarter-ends)\n")
    print(f"{'asof':12}{'n':>4}{'sec':>4}{'IC_sectorN':>12}{'IC_raw':>10}{'ewPanel%':>10}")

    quarters = []
    for i in range(len(qe) - 1):
        t, t1 = qe[i], qe[i + 1]
        data = {}
        for nm in SECTOR_OF:
            bv = bvps_at(bvps.get(nm, []), t, PERIOD_STALENESS_DAYS)
            p0 = price_at(prices.get(nm, []), t)
            p1 = price_at(prices.get(nm, []), t1)
            if bv is None or bv <= 0 or p0 is None or p1 is None or p0 <= 0:
                continue
            pb = p0 / bv                       # price-to-book; cheap = low P/B
            data[nm] = (pb, p1 / p0 - 1.0, SECTOR_OF[nm])
        wq = wide_quarter_ic(data)
        if wq is None or wq.n_pooled < MIN_POOLED:
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
    lo, hi = block_bootstrap_ci(sn)

    print("\n=== PRIMARY (Amendment 3, Sharadar P/B proxy): sector-neutral pooled IC ===")
    print(f"mean IC {_fmt(m_sn)}   t {_fmt(t_sn, 2)}   Nq={nq}")
    print(f"quarter-block bootstrap 95% CI (block={BOOT_BLOCK}, B={BOOT_B}, seed={BOOT_SEED}): "
          f"[{_fmt(lo)}, {_fmt(hi)}]")
    print(f"VERDICT: {verdict(m_sn, t_sn)}")

    print("\n=== SECONDARY: raw whole-panel IC (cross-sector confounded) ===")
    print(f"mean IC {_fmt(m_raw)}   t {_fmt(t_raw, 2)}   Nq={len([x for x in raw if x is not None])}")

    half = nq // 2
    e_m, e_t = mean_t(sn[:half]); l_m, l_t = mean_t(sn[half:])
    print("\n=== EXPLORATORY: split-half stability ===")
    print(f"early half mean IC {_fmt(e_m)} t {_fmt(e_t, 2)} (Nq={half}); "
          f"late half mean IC {_fmt(l_m)} t {_fmt(l_t, 2)} (Nq={nq - half})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
