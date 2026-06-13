"""Test 0 driver — does cheap-on-P/NAV predict forward relative return?

No engine. Signal = -P/NAV (cheapness). Forward return = 1q-forward price
return (total-return caveat in returns.py). Market-neutral = minus the
equal-weight crude basket. Primary metric = mean quarterly Spearman IC with
a t-stat (see backtest/PRE_REGISTRATION.md).

Writes outputs/backtest_test0_report.md and prints a summary. Pure stdlib.
"""

from __future__ import annotations

from datetime import date
from pathlib import Path

from .evaluate import spearman, summarize_ics, ICSummary
from .returns import forward_price_returns, market_neutralize
from .vintage_loader import (
    CRUDE_EXPLORATORY,
    CRUDE_PRIMARY,
    REPO_ROOT,
    as_of_panel,
    coverage_report,
    load_observations,
    quarter_end_cutoffs,
)

REPORT_PATH = REPO_ROOT / "outputs" / "backtest_test0_report.md"


def _run_window(obs, cutoffs, names) -> tuple[ICSummary, list]:
    """Compute per-quarter IC of (-P/NAV) vs 1q-fwd market-neutral return."""
    per_quarter = []
    detail = []
    for i in range(len(cutoffs) - 1):
        t, t_next = cutoffs[i], cutoffs[i + 1]
        panel = as_of_panel(obs, t, names, require_pnav=True)
        rets = forward_price_returns(obs, panel, t_next, names)
        # cross-section = names with BOTH a signal at t and a fwd return
        xsec = [s for s in panel if s in rets]
        signal = [-panel[s].pnav for s in xsec]  # cheapness: lower P/NAV = higher signal
        mn = market_neutralize({s: rets[s] for s in xsec})
        y = [mn[s] for s in xsec]
        ic = spearman(signal, y)
        per_quarter.append((t.isoformat(), ic, len(xsec)))
        detail.append(
            {
                "cutoff": t.isoformat(),
                "fwd_to": t_next.isoformat(),
                "names": xsec,
                "pnav": {s: round(panel[s].pnav, 3) for s in xsec},
                "fwd_ret": {s: round(rets[s], 4) for s in xsec},
                "mn_ret": {s: round(mn[s], 4) for s in xsec},
                "ic": ic,
            }
        )
    return summarize_ics(per_quarter), detail


def _pairwise_sign_agreement(detail) -> tuple[int, int]:
    """For 2-name cross-sections: did the cheaper name (lower P/NAV) win?
    Returns (hits, total) — a coin-flip test, reported because IC is
    degenerate (±1) at n=2."""
    hits = total = 0
    for d in detail:
        if len(d["names"]) != 2:
            continue
        a, b = d["names"]
        cheaper = a if d["pnav"][a] < d["pnav"][b] else b
        other = b if cheaper == a else a
        total += 1
        if d["mn_ret"][cheaper] > d["mn_ret"][other]:
            hits += 1
    return hits, total


def _fmt(x, nd=3):
    return "n/a" if x is None else f"{x:.{nd}f}"


def build_report() -> str:
    obs = load_observations()
    cov = coverage_report(obs)

    # Primary window: the owner's 5 crude names, full available span.
    cutoffs = quarter_end_cutoffs(date(2024, 9, 30), date(2026, 6, 30))
    primary, p_detail = _run_window(obs, cutoffs, CRUDE_PRIMARY)
    hits, total = _pairwise_sign_agreement(p_detail)

    # Exploratory: add INSW (deferred name) to thicken the early cross-section.
    expl_names = {**CRUDE_PRIMARY, **CRUDE_EXPLORATORY}
    expl, _ = _run_window(obs, cutoffs, expl_names)

    L = []
    A = L.append
    A("# Crude edge backtest — Test 0 report")
    A("")
    A("**Verdict: INCONCLUSIVE — the available data cannot power the "
      "pre-registered test.** This is NOT a no-edge finding; it is a "
      "data-insufficiency finding. See 'Why inconclusive' and 'Data needed'.")
    A("")
    A("Pre-registered metric (fixed before results, "
      "`backtest/PRE_REGISTRATION.md`): mean quarterly cross-sectional "
      "Spearman IC of the signal (Test 0: −P/NAV) vs 1q-forward "
      "market-neutral return, with a t-stat over non-overlapping quarters.")
    A("")

    A("## Data coverage actually on disk")
    A("")
    A("Only historical (date, ticker, price, P/NAV) series available: "
      "`inputs/market_data/pareto_share_prices.csv`, weekly Pareto prints, "
      "**2024-08-22 → 2026-06-08** (~22 months — not the 2018–2025 scope). "
      "Network is blocked (Yahoo/stooq 403), so no external price/dividend "
      "history could be fetched.")
    A("")
    A("| Name | Pareto ticker | rows | rows w/ P/NAV | P/NAV span |")
    A("|---|---|---:|---:|---|")
    for s in ["DHT", "NAT", "FRO", "ECO", "TNK", "INSW"]:
        c = cov[s]
        span = (f"{c['pnav_first']} → {c['pnav_last']}"
                if c["rows_with_pnav"] else "— (no P/NAV)")
        present = "absent" if c["rows"] == 0 else ""
        A(f"| {s} {present} | {c['pareto_ticker']} | {c['rows']} | "
          f"{c['rows_with_pnav']} | {span} |")
    A("")
    A("Net: of the five long-listed crude names, only **DHT** is continuous "
      "over the full window. **TNK** has a ~4-month hole in the extract "
      "(no rows mid-May → mid-Sep 2025), so two quarters below collapse to a "
      "single name. **ECO** stops at 2025-04-07; **NAT** has rows but no "
      "P/NAV (the known APPROX gap); **FRO is absent from the extract**. So "
      "the realizable crude cross-section is 2–3 names early and 1–2 names "
      "later — never enough for a non-degenerate rank IC.")
    A("")

    A("## Primary result (5-name window, exploratory point estimate)")
    A("")
    A(f"- Non-overlapping quarters with a usable cross-section: "
      f"**N = {primary.n_quarters}**")
    A(f"- Mean quarterly IC (−P/NAV vs 1q-fwd market-neutral return): "
      f"**{_fmt(primary.mean_ic)}**")
    A(f"- Std of quarterly IC: {_fmt(primary.std_ic)}")
    A(f"- t-stat: **{_fmt(primary.t_stat, 2)}**  "
      f"(0.05 two-sided bar, df={max(primary.n_quarters-1,0)}: "
      f"|t| ≥ {_fmt(primary.t_crit_05, 2)})")
    A(f"- Newey-West (lag 1) SE: {_fmt(primary.nw_se)} → NW t: "
      f"{_fmt(primary.nw_t, 2)}")
    sig = primary.significant_05()
    A(f"- Distinguishable from zero at 0.05? "
      f"**{'yes' if sig else 'no' if sig is not None else 'undetermined'}**")
    A("")
    A("Per-quarter (cross-section size in parens):")
    A("")
    A("| Signal date | → forward | names (n) | IC |")
    A("|---|---|---|---:|")
    for d in p_detail:
        A(f"| {d['cutoff']} | {d['fwd_to']} | "
          f"{', '.join(d['names'])} ({len(d['names'])}) | {_fmt(d['ic'], 2)} |")
    A("")
    A(f"Pairwise sign-agreement on the 2-name quarters (did the cheaper "
      f"name beat the other?): **{hits}/{total}**. A coin-flip test, "
      f"powerless at this N.")
    A("")

    A("## Exploratory: +INSW to thicken the early cross-section")
    A("")
    A(f"- N = {expl.n_quarters}, mean IC = {_fmt(expl.mean_ic)}, "
      f"t = {_fmt(expl.t_stat, 2)}. Exploratory only (INSW deferred by the "
      "owner; adds depth only Aug-2024→Apr-2025). Does not move the verdict.")
    A("")

    A("## Why inconclusive (decided by the pre-registered verdict rule)")
    A("")
    A("1. **Wrong period.** Signal series starts 2024-08; the test wanted "
      "~2018–2025. ~22 months ⇒ at most ~7 non-overlapping quarters.")
    A("2. **Cross-section too thin.** Full-window crude P/NAV exists for only "
      "2 names (DHT, TNK). At n=2 the cross-sectional Spearman IC is "
      "mechanically ±1 (degenerate); at n=3 it is in {−1,−0.5,+0.5,+1}. The "
      "point estimate above is dominated by this degeneracy.")
    A("3. **No total return.** Returns are price-only; crude dividends are "
      "large and cross-sectionally uneven, a material omission for the "
      "neutralized return.")
    A("4. **Underpowered t.** With N≈6 quarters, |t| must exceed ~2.57 "
      "(df=5) for p<0.05 — not reachable from this signal/cross-section.")
    A("")
    A("Per the pre-registered rule, a tiny degenerate sample is **reported "
      "as exploratory and called INCONCLUSIVE**, not edge or no-edge. "
      "Test 1 (engine) is **GATED** behind a non-zero, trustworthy Test 0 "
      "IC and is therefore NOT run (it also cannot run here: no "
      "numpy/pandas/scipy and no `.venv` in this container).")
    A("")

    A("## Data the owner must supply to make Test 0 conclusive")
    A("")
    A("Do not fabricate any of this — these are the inputs to obtain:")
    A("")
    A("1. **Historical quarterly P/NAV, 2018–2025, for DHT, NAT, FRO, ECO, "
      "TNK** — archived broker NAV prints (Pareto/Clarksons/Fearnley) or VIE "
      "archived analyst NAVs. This is the binding gap. FRO is missing "
      "entirely from the current extract; NAT needs a real P/NAV source "
      "(Pareto doesn't publish one).")
    A("2. **Total-return history** for those names 2018–2025 — adjusted close "
      "OR (price + dividend-per-share with ex-dates). Needed to replace the "
      "price-only proxy.")
    A("3. (For Test 1) **Point-in-time fundamentals** per name per quarter — "
      "fleet/balance-sheet/dividend-policy vintages — to reconstruct "
      "`CompanyInputs` as-of each quarter. Only 2026-Q1 exists on disk today.")
    A("")
    A("**Transparent proxy if 1–2 are hard:** a depreciated-book NAV per "
      "share rebuilt from each name's historical 20-F/10-K (book equity ÷ "
      "shares) as a stand-in P/NAV denominator — clearly flagged as a proxy, "
      "not a broker mark. That requires historical financials, which are "
      "also not on disk. Both routes need the owner to supply source data.")
    A("")
    A("## Reproduce")
    A("")
    A("`PYTHONPATH=. python3 -m backtest.run_test0` (pure stdlib; no deps). "
      "No-look-ahead is assertion-enforced in `vintage_loader.as_of_panel`.")
    A("")
    return "\n".join(L)


def main() -> None:
    report = build_report()
    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    REPORT_PATH.write_text(report)
    # Console summary
    print(report)
    print(f"\n[written] {REPORT_PATH}")


if __name__ == "__main__":
    main()
