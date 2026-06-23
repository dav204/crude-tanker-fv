"""POWERED time-series reversion test on the deep Sharadar P/B proxy (multi-cycle).

The engine Test 2 (run_engine_timeseries) found a nominally-significant within-name
reversion signal but on ONE cycle (2019-2026) — not a clean verdict. This runs the
SAME estimand on the deep P/B proxy panel (Amendment 3's data: ~2008-2025, ~70
quarters = GFC + the 2011-16 shipping depression + 2020 COVID + the 2021-22 boom =
MULTIPLE independent cycles), so the quarter-block bootstrap is genuinely powered.

It tests the value PREMISE on a book proxy (P/B), not the engine's market-NAV marks
(same caveat as Amendment 3) — but it is the powered, multi-cycle read the engine
test can't yet be: does a name being cheap to its own book (low P/B) predict its OWN
forward return (reversion).

PRIMARY: avg within-name Spearman(cheapness=-P/B, own 1q-fwd total return), names
with >=20 quarters; quarter-block bootstrap over the ~70 quarter-ends (the independent
unit). SECONDARY decompositions mirror Test 2: quarter-de-meaned (cross-sectional,
should echo Amendment 3's ~null) and cycle-timing.

Run: PYTHONPATH=. .venv/bin/python -m backtest.run_proxy_timeseries
"""

from __future__ import annotations

import collections
import datetime as dt
import random
import statistics

from .loaders import bvps_at, price_at, quarter_ends
from .loaders_sharadar import (
    SECTOR_OF, cache_available, cache_provenance, load_bvps, load_prices,
)

START = dt.date(2008, 1, 1)
PERIOD_STALENESS_DAYS = 550
MIN_QUARTERS = 20          # per-name minimum for a within-name IC (deep names have ~50-70)
BOOT_B = 10000
BOOT_SEED = 20260624


def _fmt(x, nd=3):
    return "n/a" if x is None else f"{x:+.{nd}f}"


def _ranks(v):
    order = sorted(range(len(v)), key=lambda i: v[i])
    r = [0.0] * len(v)
    i = 0
    while i < len(v):
        j = i
        while j + 1 < len(v) and v[order[j + 1]] == v[order[i]]:
            j += 1
        avg = (i + j) / 2.0 + 1
        for k in range(i, j + 1):
            r[order[k]] = avg
        i = j + 1
    return r


def spearman(xs, ys):
    if len(xs) < 3:
        return None
    rx, ry = _ranks(xs), _ranks(ys)
    n = len(xs)
    mx, my = sum(rx) / n, sum(ry) / n
    cov = sum((a - mx) * (b - my) for a, b in zip(rx, ry))
    sx = sum((a - mx) ** 2 for a in rx) ** 0.5
    sy = sum((b - my) ** 2 for b in ry) ** 0.5
    return cov / (sx * sy) if sx and sy else None


def verdict(mean_ic, lo, hi) -> str:
    if mean_ic is None or lo is None:
        return "INCONCLUSIVE"
    if mean_ic > 0 and lo > 0:
        return "EDGE (reversion premise supported — powered, multi-cycle)"
    if mean_ic < 0 and hi < 0:
        return "FAIL (anti-reversion)"
    return "INCONCLUSIVE"


def main() -> int:
    if not cache_available():
        print("Sharadar cache not found (set FACTOR_PORTFOLIO_ROOT). Nothing to run.")
        return 2

    bvps = load_bvps()
    prices = load_prices()
    print(f"Sharadar cache provenance: {cache_provenance()}")

    last_price = max(d for s in prices.values() for d, _ in s)
    qe = quarter_ends(START, last_price)

    # panel: name -> {quarter_end: (cheapness=-P/B, own 1q-fwd total return)}
    namesq: dict[str, dict] = collections.defaultdict(dict)
    for i in range(len(qe) - 1):
        t, t1 = qe[i], qe[i + 1]
        for nm in SECTOR_OF:
            bv = bvps_at(bvps.get(nm, []), t, PERIOD_STALENESS_DAYS)
            p0 = price_at(prices.get(nm, []), t)
            p1 = price_at(prices.get(nm, []), t1)
            if bv is None or bv <= 0 or p0 is None or p1 is None or p0 <= 0:
                continue
            namesq[nm][t] = (-(p0 / bv), p1 / p0 - 1.0)

    elig = [nm for nm in namesq if len(namesq[nm]) >= MIN_QUARTERS]
    allq = sorted({t for nm in elig for t in namesq[nm]})
    nq = len(allq)
    npq = sum(len(namesq[nm]) for nm in elig)
    print(f"window {allq[0]} .. {allq[-1]}  |  {nq} quarter-ends, "
          f"{len(elig)} names >=({MIN_QUARTERS}q), {npq} name-quarters\n")

    # per-name within-name reversion IC
    per_name = []
    for nm in sorted(elig):
        pairs = list(namesq[nm].values())
        ic = spearman([p[0] for p in pairs], [p[1] for p in pairs])
        per_name.append((nm, ic, len(pairs)))
    ts_vals = [ic for _, ic, _ in per_name if ic is not None]
    ts_mean = statistics.mean(ts_vals)

    # quarter-block bootstrap over the quarter-ends (the independent unit)
    rng = random.Random(BOOT_SEED)
    boot = []
    for _ in range(BOOT_B):
        qs = [rng.choice(allq) for _ in range(nq)]
        vals = []
        for nm in elig:
            ps = [namesq[nm][q] for q in qs if q in namesq[nm]]
            if len(ps) >= 10:
                ic = spearman([p[0] for p in ps], [p[1] for p in ps])
                if ic is not None:
                    vals.append(ic)
        if vals:
            boot.append(statistics.mean(vals))
    boot.sort()
    lo, hi = boot[int(0.025 * len(boot))], boot[int(0.975 * len(boot))]
    p_le0 = sum(1 for b in boot if b <= 0) / len(boot)
    t_stat = ts_mean / statistics.pstdev(boot) if statistics.pstdev(boot) else None

    # decompositions (mirror Test 2)
    flat = [(t, nm, namesq[nm][t][0], namesq[nm][t][1]) for nm in elig for t in namesq[nm]]
    ic_raw = spearman([r[2] for r in flat], [r[3] for r in flat])
    me = {q: statistics.mean([r[2] for r in flat if r[0] == q]) for q in allq}
    mr = {q: statistics.mean([r[3] for r in flat if r[0] == q]) for q in allq}
    ic_dm = spearman([r[2] - me[r[0]] for r in flat], [r[3] - mr[r[0]] for r in flat])
    ic_cycle = spearman([me[q] for q in allq], [mr[q] for q in allq])

    print("=== POWERED multi-cycle P/B reversion (book proxy, not engine marks) ===")
    print(f"PRIMARY per-name reversion IC {_fmt(ts_mean)}  quarter-block 95% CI "
          f"[{_fmt(lo)}, {_fmt(hi)}]  t {_fmt(t_stat, 2)}  p(IC<=0)={p_le0:.4f}")
    print(f"(2) cross-sectional (de-meaned) IC {_fmt(ic_dm)}   (echoes Amendment 3 ~null)")
    print(f"(3) cycle-timing IC               {_fmt(ic_cycle)}   (n={nq})")
    print(f"(4) raw pooled IC                 {_fmt(ic_raw)}")
    print(f"\nVERDICT: {verdict(ts_mean, lo, hi)}")
    print("\nper-name within-name reversion IC:")
    for nm, ic, n in sorted(per_name, key=lambda x: (x[1] if x[1] is not None else 0), reverse=True):
        print(f"   {nm:6s} {_fmt(ic)}  ({n}q, {SECTOR_OF[nm]})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
