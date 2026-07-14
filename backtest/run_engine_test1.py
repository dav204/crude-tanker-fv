"""Test 1 driver — engine EV% ex-post falsification (PRE_REGISTRATION_TEST1.md).

Sector-neutral pooled IC of engine **EV%-cheapness** vs 1q-forward total return,
over historical vintages produced per DATA_CONTRACT_TEST1.md. This is the tool's
OWN signal (not a proxy): EV%(i,q) = the engine's probability-weighted scenario
FV vs price, valued AS-OF q via the Phase-3b as-of plumbing.

The harness is complete and tested; it has no result until vintages are
populated (the env-gated free-broker-weekly backfill). With an empty
``backtest/vintages/`` it reports what to populate and exits cleanly.

Run: PYTHONPATH=. .venv/bin/python -m backtest.run_engine_test1
"""

from __future__ import annotations

import datetime as dt
from pathlib import Path

from .evaluate_wide import mean_t, wide_quarter_ic
from .loaders import price_at, quarter_ends  # noqa: F401  (quarter_ends used by callers/tests)
from .loaders_sharadar import load_prices
from .run_proxy_powered import block_bootstrap_ci

REPO = Path(__file__).resolve().parent.parent
SRC = REPO / "src"
VINTAGES_DIR = Path(__file__).resolve().parent / "vintages"

_QEND = {1: (3, 31), 2: (6, 30), 3: (9, 30), 4: (12, 31)}


def _fmt(x, nd=3):
    return "n/a" if x is None else f"{x:+.{nd}f}"


def qend_date(q: str) -> dt.date:
    y, qn = q.split("-Q")
    m, d = _QEND[int(qn)]
    return dt.date(int(y), m, d)


def next_quarter(q: str) -> str:
    y, qn = q.split("-Q")
    y, qn = int(y), int(qn)
    return f"{y + 1}-Q1" if qn == 4 else f"{y}-Q{qn + 1}"


# --------------------------------------------------------------------------- #
# statistic — the novel, pre-registered piece (sign convention is load-bearing)
# --------------------------------------------------------------------------- #

def engine_quarter_ic(ev_by_name: dict, ret_by_name: dict, sector_by_name: dict):
    """One quarter's sector-neutral IC of EV%-cheapness vs forward return.

    CHEAP = HIGH EV% (the engine calls a name cheap when EV% is high). We pass
    ``-EV%`` as the cheapness key so the reused ``wide_quarter_ic`` — built for
    P/NAV, where *low* = cheap and which internally negates the key — ranks HIGH
    EV% as cheap. Positive IC ⇒ higher EV% predicts peer-relative outperformance.
    """
    common = sorted(set(ev_by_name) & set(ret_by_name) & set(sector_by_name))
    data = {n: (-ev_by_name[n], ret_by_name[n], sector_by_name[n]) for n in common}
    return wide_quarter_ic(data)


def sign_hit_rate(ev_by_name: dict, ret_by_name: dict, sector_by_name: dict):
    """Pooled fraction of name-quarters where sign(sector-relative EV%) matches
    sign(sector-relative forward return) — the pre-registered directional read."""
    hits = total = 0
    by_sector: dict[str, list[str]] = {}
    common = set(ev_by_name) & set(ret_by_name) & set(sector_by_name)
    for n in common:
        by_sector.setdefault(sector_by_name[n], []).append(n)
    for members in by_sector.values():
        if len(members) < 2:
            continue
        ev_mean = sum(ev_by_name[m] for m in members) / len(members)
        ret_mean = sum(ret_by_name[m] for m in members) / len(members)
        for m in members:
            d_ev, d_ret = ev_by_name[m] - ev_mean, ret_by_name[m] - ret_mean
            if d_ev == 0 or d_ret == 0:
                continue
            total += 1
            hits += (d_ev > 0) == (d_ret > 0)
    return (hits / total, total) if total else (None, 0)


def verdict(mean_ic, t) -> str:
    """Pre-registered decision rule (PRE_REGISTRATION_TEST1.md): FAIL only on a
    significant anti-predictive result; EDGE on significant positive; else
    INCONCLUSIVE (the expected MVP outcome)."""
    if mean_ic is None or t is None:
        return "INCONCLUSIVE (insufficient quarters)"
    if mean_ic < 0 and t <= -2.0:
        return "FAIL (engine EV% anti-predictive)"
    if mean_ic > 0 and t >= 2.0:
        return "EDGE (engine EV% adds signal)"
    return "INCONCLUSIVE (expected at MVP n)"


# --------------------------------------------------------------------------- #
# vintage loop
# --------------------------------------------------------------------------- #

def discover_vintages(vintages_dir: Path = VINTAGES_DIR) -> list[Path]:
    if not vintages_dir.exists():
        return []
    return sorted(p for p in vintages_dir.iterdir()
                  if p.is_dir() and (p / "scenario_inputs.yaml").exists())


def engine_ev_at(quarter: str, inputs_dir: Path, outputs_dir: Path) -> dict:
    """{ticker: (ev_pct, sector)} for one vintage via the as-of engine."""
    import sys
    if str(SRC) not in sys.path:
        sys.path.insert(0, str(SRC))
    from crude_tanker_fv.pipeline import run_scenarios_watchlist
    reports = run_scenarios_watchlist(
        quarter, inputs_dir=inputs_dir, outputs_dir=outputs_dir, asof_quarter=quarter,
    )
    return {r.ticker: (r.expected_value_vs_current / r.current_price * 100.0, r.sector)
            for r in reports if r.current_price}


def main() -> int:
    vintages = discover_vintages()
    if not vintages:
        print("No vintages in backtest/vintages/ — nothing to run.")
        print("Populate per DATA_CONTRACT_TEST1.md (free broker-weekly backfill, "
              "env-gated on a 3.10+ harvester), then re-run. The harness + "
              "statistic are tested and ready.")
        return 0

    prices = load_prices()
    tmp_out = REPO / "state" / "test1_scratch"
    quarters = []
    print(f"{'asof':10}{'n':>4}{'sec':>4}{'IC_sectorN':>12}{'hit%':>8}")
    for vd in vintages:
        q = vd.name
        ev = engine_ev_at(q, vd, tmp_out)
        nq = next_quarter(q)
        ev_by, ret_by, sec_by = {}, {}, {}
        for t, (ev_pct, sector) in ev.items():
            p0 = price_at(prices.get(t, []), qend_date(q))
            p1 = price_at(prices.get(t, []), qend_date(nq))
            if p0 is None or p1 is None or p0 <= 0:
                continue
            ev_by[t], ret_by[t], sec_by[t] = ev_pct, p1 / p0 - 1.0, sector
        wq = engine_quarter_ic(ev_by, ret_by, sec_by)
        if wq is None or wq.n_pooled < 4:
            continue
        hit, _ = sign_hit_rate(ev_by, ret_by, sec_by)
        wq.asof = q
        quarters.append((wq, hit))
        print(f"{q:10}{wq.n_pooled:>4}{wq.sectors:>4}{_fmt(wq.ic_sector_neutral):>12}"
              f"{'' if hit is None else f'{hit*100:>7.0f}'}")

    sn = [wq.ic_sector_neutral for wq, _ in quarters]
    m_sn, t_sn = mean_t(sn)
    lo, hi = block_bootstrap_ci(sn)
    nq = len([x for x in sn if x is not None])
    hits = [h for _, h in quarters if h is not None]
    print("\n=== PRIMARY (Test 1): engine EV% sector-neutral pooled IC ===")
    print(f"mean IC {_fmt(m_sn)}   t {_fmt(t_sn, 2)}   Nq={nq}")
    print(f"quarter-block bootstrap 95% CI: [{_fmt(lo)}, {_fmt(hi)}]")
    print(f"VERDICT: {verdict(m_sn, t_sn)}")
    if hits:
        print("=== SECONDARY: directional sign hit-rate ===")
        print(f"pooled hit-rate {sum(hits)/len(hits)*100:.0f}% over {len(hits)} quarters "
              f"(anti-predictive trip: ≤40%)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
