"""EXPLORATORY (not pre-registered): the ABSOLUTE / time-series reads of engine EV%.

PRE_REGISTRATION_TEST1 graded the sector-neutral cross-sectional IC (does cheap beat
its sector peers, market+sector removed) — a null. This script asks the on-thesis
question that frame strips out: does being cheap to the blended NAV+dividend-strip
fair value predict the name's OWN forward return? Decomposed so beta can't hide:

  (1) raw pooled IC      — EV% vs own 1q-fwd total return, all name-quarters
                           (includes the market/cycle move)
  (2) de-meaned pooled   — same, minus each quarter's cross-sectional mean
                           (market removed -> should echo the cross-sectional null;
                            if (1) is big and (2) is ~0, the signal is pure cycle-timing)
  (3) cycle timing       — corr(quarter-mean EV%, quarter-mean fwd return) over quarters
                           (does aggregate cheapness time the cycle? small n=#quarters)
  (4) per-name reversion  — within-name Spearman(EV%, fwd ret), averaged over names
                           with >=10 quarters (cheaper-than-its-own-history -> rises?)

Run: PYTHONPATH=. .venv/bin/python -m backtest.run_engine_timeseries
"""
from __future__ import annotations

import collections
import contextlib
import io
import statistics

from .loaders import price_at
from .loaders_sharadar import load_prices
from .run_engine_test1 import (
    discover_vintages, engine_ev_at, next_quarter, qend_date, REPO,
)

_RNG_SEED = 20260623
_B = 10000


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
    return cov / (sx * sy) if sx and sy else 0.0


def _fmt(x, nd=3):
    return "n/a" if x is None else f"{x:+.{nd}f}"


def main() -> int:
    prices = load_prices()
    tmp = REPO / "state" / "test1_scratch"
    panel = []  # (quarter, name, ev_pct, fwd_return)
    for vd in discover_vintages():
        q = vd.name
        with contextlib.redirect_stdout(io.StringIO()):   # silence the per-name engine prints
            ev = engine_ev_at(q, vd, tmp)
        nq = next_quarter(q)
        for t, (ev_pct, _sector) in ev.items():
            p0 = price_at(prices.get(t, []), qend_date(q))
            p1 = price_at(prices.get(t, []), qend_date(nq))
            if p0 and p1 and p0 > 0:
                panel.append((q, t, ev_pct, p1 / p0 - 1.0))

    quarters = sorted({r[0] for r in panel})
    names = sorted({r[1] for r in panel})
    print(f"panel: {len(panel)} name-quarters, {len(names)} names, {len(quarters)} quarters")

    ev_all = [r[2] for r in panel]
    ret_all = [r[3] for r in panel]

    # (1) raw pooled
    ic_raw = spearman(ev_all, ret_all)

    # (2) de-meaned by quarter (market/cycle removed)
    me = {q: statistics.mean([r[2] for r in panel if r[0] == q]) for q in quarters}
    mr = {q: statistics.mean([r[3] for r in panel if r[0] == q]) for q in quarters}
    ic_dm = spearman([r[2] - me[r[0]] for r in panel], [r[3] - mr[r[0]] for r in panel])

    # (3) cycle timing: quarter-mean EV% vs quarter-mean forward return
    qev = [me[q] for q in quarters]
    qret = [mr[q] for q in quarters]
    ic_cycle = spearman(qev, qret)

    # (4) per-name time-series reversion (>=10 quarters)
    byname = collections.defaultdict(list)
    for q, t, e, r in panel:
        byname[t].append((e, r))
    ts = [(t, spearman([o[0] for o in obs], [o[1] for o in obs]), len(obs))
          for t, obs in byname.items() if len(obs) >= 10]
    ts_vals = [v for _, v, _ in ts if v is not None]
    ts_mean = statistics.mean(ts_vals) if ts_vals else None

    # quarter-block bootstrap CI for the raw pooled IC (resample QUARTERS, the indep unit)
    import random
    rng = random.Random(_RNG_SEED)
    by_q = collections.defaultdict(list)
    for r in panel:
        by_q[r[0]].append(r)
    boots = []
    for _ in range(_B):
        samp = []
        for _ in range(len(quarters)):
            samp.extend(by_q[rng.choice(quarters)])
        ic = spearman([r[2] for r in samp], [r[3] for r in samp])
        if ic is not None:
            boots.append(ic)
    boots.sort()
    lo, hi = boots[int(0.025 * len(boots))], boots[int(0.975 * len(boots))]

    # PRIMARY powered estimand: the avg within-name (cycle-inclusive) reversion IC,
    # with a quarter-block bootstrap so the inference respects autocorrelation /
    # the shared cycle (the independent unit is the quarter, n=23).
    namesq = collections.defaultdict(dict)
    for q, t, e, r in panel:
        namesq[t][q] = (e, r)
    elig = [t for t, obs in byname.items() if len(obs) >= 10]
    rng2 = random.Random(_RNG_SEED + 1)
    boot_ts = []
    for _ in range(_B):
        qs = [rng2.choice(quarters) for _ in range(len(quarters))]
        vals = []
        for t in elig:
            pairs = [namesq[t][q] for q in qs if q in namesq[t]]
            if len(pairs) >= 5:
                sp = spearman([p[0] for p in pairs], [p[1] for p in pairs])
                if sp is not None:
                    vals.append(sp)
        if vals:
            boot_ts.append(statistics.mean(vals))
    boot_ts.sort()
    lo_ts = boot_ts[int(0.025 * len(boot_ts))]
    hi_ts = boot_ts[int(0.975 * len(boot_ts))]
    p_ts = sum(1 for b in boot_ts if b <= 0) / len(boot_ts)
    se_ts = statistics.pstdev(boot_ts)
    t_ts = ts_mean / se_ts if se_ts else None

    print("\n=== ABSOLUTE / time-series reads of engine EV% (EXPLORATORY) ===")
    print(f"PRIMARY per-name reversion IC {_fmt(ts_mean)}  quarter-block 95% CI "
          f"[{_fmt(lo_ts)}, {_fmt(hi_ts)}]  t {_fmt(t_ts, 2)}  p(IC<=0)={p_ts:.3f}")
    print(f"(1) raw pooled IC          {_fmt(ic_raw)}   quarter-block 95% CI [{_fmt(lo)}, {_fmt(hi)}]")
    print(f"(2) de-meaned pooled IC    {_fmt(ic_dm)}   (market removed; ~cross-sectional)")
    print(f"(3) cycle-timing IC        {_fmt(ic_cycle)}   (quarter-mean EV% vs quarter-mean return, n={len(quarters)})")
    print(f"(4) per-name reversion IC  {_fmt(ts_mean)}   (avg within-name, {len(ts_vals)} names >=10q)")
    print("\nper-name detail:")
    for t, v, n in sorted(ts, key=lambda x: (x[1] if x[1] is not None else 0), reverse=True):
        print(f"   {t:6s} {_fmt(v)}  ({n}q)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
