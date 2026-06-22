"""§12 dividend-window diagnostic (METHODOLOGY §12.5-§12.7).

Diagnostic-only resolution of the high-payout peak-cycle §12 case — **no FV change**
(mirrors ``consensus_eps`` / the broker-NAV sweep). It replaces §12's prior one-way
bullish override ("treat FV as a NAV floor, do not act on the TRIM"; audit finding
E-3) with a falsifiable per-name classification.

For each name passing the §12.5 trigger gate, compute ``Q*`` — the quarters of
discounted DPS needed to bridge the market premium over the tool's through-cycle NAV
floor — and compare it to ``H``, the FFA-rate-supported horizon (how many forward
quarters the curve holds above the through-cycle mean rate):

    gap = price - tool_NAV_floor
    Q*  = min N such that  sum_{q=1..N} DPS_q / (1+r)^(q/4) >= gap
    H   = leading FFA quarters above the 10yr-mean rate (value-weighted)

    Q* <= H  -> the premium is rate-supported -> §12 undervaluation (floor framing)
    Q* >  H  -> the premium is NOT rate-supported -> the TRIM stands (value trap)

NAT lands in the second bucket (spot-derived ~100% payout, no contracted book), so
§12 does not fire and its TRIM stands. The 0.9x cycle-conditional terminal (§9.2) is
unaffected and not exempted — it mean-reverts the *asset* level (through-cycle),
orthogonal to this *near-term cash-claim* test.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Optional

from .loaders import load_company_inputs, load_watchlist
from .nav import NavResult, compute_nav
from .report import OUTPUTS_DIR

# §12.5 trigger-gate thresholds.
HERFINDAHL_GATE = 0.80   # single-asset-class pure-play (sum of class-value-share^2)
PAYOUT_GATE = 0.90       # high stated/trailing payout
CYCLE_PEAK_GATE = 1.5    # late-cycle/peak band (cycle position > 1.5x)
PREMIUM_GATE = 1.5       # price / tool_NAV — large market premium over the floor


@dataclass
class DividendWindowRow:
    """One name's §12 dividend-window classification."""

    ticker: str
    sector: str
    price: float
    tool_nav: float
    premium_x: float              # price / tool_NAV
    payout_ratio: float
    herfindahl: float
    cycle_position: float
    gated: bool                   # passes §12.5
    gap: float                    # price - tool_NAV (per share)
    q_star: Optional[float]       # quarters to bridge gap; None if never within the strip
    supported_horizon: float      # H: FFA quarters above the through-cycle mean
    classification: str           # "undervaluation" | "TRIM-stands" | "n/a"


def fleet_herfindahl(nav: NavResult) -> float:
    """Sum of squared per-class fleet-value shares (→ 1.0 for a single-class fleet)."""
    total = nav.fleet_value or 1.0
    return sum((v / total) ** 2 for v in nav.fleet_value_by_class.values())


def supported_horizon(inputs, nav: NavResult) -> float:
    """H: forward quarters the FFA curve holds above the through-cycle (10yr-mean)
    rate — how long the forward curve says the peak persists, value-weighted across
    the fleet's classes (one class for the single-class names this gate selects)."""
    md = inputs.market_data
    means = md.historical_tce_means
    total = nav.fleet_value or 1.0
    h = 0.0
    for cls, curve in md.ffa_forward_curve.items():
        mean = means.get(cls)
        if mean is None:
            continue
        lead = 0
        for rate in curve:
            if rate > mean:
                lead += 1
            else:
                break
        h += (nav.fleet_value_by_class.get(cls, 0.0) / total) * lead
    return h


def q_star(dps_by_quarter: list[float], discount_rate: float, gap: float) -> Optional[float]:
    """First quarter N where cumulative discounted DPS >= gap; None if never reached."""
    if gap <= 0:
        return 0.0
    cum = 0.0
    for i, dps in enumerate(dps_by_quarter, start=1):
        cum += dps / (1.0 + discount_rate) ** (i / 4.0)
        if cum >= gap:
            return float(i)
    return None


def evaluate(ticker: str, quarter: str, entry: dict) -> DividendWindowRow:
    """Gate a name on §12.5 and, if gated, classify it via the §12.6 window test."""
    # value_company applies the transaction-anchored marks (default-on), so tool_nav
    # / cycle / strip match the headline (e.g. NAT $2.07), not the raw curves.
    from .pipeline import value_company

    price = float(entry.get("as_of_price") or entry["current_price"])
    target = float(entry.get("analyst_target") or price)
    report = value_company(ticker, quarter, current_price=price, analyst_target=target)
    nav, cyc, strip = report.nav, report.cycle, report.strip
    ci = load_company_inputs(ticker, quarter)  # FFA curve + means (txn-anchor doesn't touch these)

    tool_nav = nav.nav_per_share
    payout = ci.dividend_policy.payout_ratio
    herf = fleet_herfindahl(nav)
    premium = price / tool_nav if tool_nav > 0 else 0.0
    gated = (
        herf >= HERFINDAHL_GATE
        and payout > PAYOUT_GATE
        and cyc.cycle_position > CYCLE_PEAK_GATE
        and premium > PREMIUM_GATE
    )
    gap = price - tool_nav
    horizon = supported_horizon(ci, nav)
    qs: Optional[float] = None
    classification = "n/a"
    if gated:
        qs = q_star(strip.dps_by_quarter, strip.discount_rate, gap)
        classification = "undervaluation" if (qs is not None and qs <= horizon) else "TRIM-stands"
    return DividendWindowRow(
        ticker=ticker, sector=str(entry.get("sector", "")), price=price, tool_nav=tool_nav,
        premium_x=premium, payout_ratio=payout, herfindahl=herf,
        cycle_position=cyc.cycle_position, gated=gated, gap=gap, q_star=qs,
        supported_horizon=horizon, classification=classification,
    )


def build_rows(quarter: str) -> list[DividendWindowRow]:
    rows: list[DividendWindowRow] = []
    for ticker, entry in load_watchlist().items():
        try:
            rows.append(evaluate(ticker, quarter, entry))
        except FileNotFoundError:
            continue
    return rows


_RESOLUTION = {
    "undervaluation": "§12 undervaluation (floor applies)",
    "TRIM-stands": "TRIM stands (value trap)",
    "n/a": "n/a (gate)",
}


def write_dividend_window_test(rows: list[DividendWindowRow], outputs_dir: Path = OUTPUTS_DIR) -> Path:
    outputs_dir.mkdir(parents=True, exist_ok=True)
    gated = [r for r in rows if r.gated]
    out = [
        "# §12 dividend-window test (METHODOLOGY §12.5–§12.7)",
        "",
        "Diagnostic-only (no FV change). §12.5 gate: single-class Herfindahl≥0.80, payout>0.90,",
        "cycle>1.5×, price/tool-NAV>1.5×. §12.6: `Q*` = quarters of discounted DPS to bridge",
        "`price − tool_NAV`; `H` = FFA quarters above the through-cycle mean. `Q* ≤ H` ⇒ §12",
        "undervaluation (floor); `Q* > H` (or never) ⇒ the TRIM stands. (Replaces the prior",
        "one-way bullish override — audit E-3.)",
        "",
        "| Name | Gated | price/NAV | gap $ | Q* | H | Resolution |",
        "|---|:--:|--:|--:|:--:|--:|---|",
    ]
    for r in sorted(rows, key=lambda x: (not x.gated, x.ticker)):
        if not r.gated:
            qs = "—"
        elif r.q_star is None:
            qs = ">strip"
        else:
            qs = f"{r.q_star:.0f}"
        out.append(
            f"| {r.ticker} | {'Y' if r.gated else '·'} | {r.premium_x:.2f}× | "
            f"{r.gap:+.2f} | {qs} | {r.supported_horizon:.1f} | {_RESOLUTION[r.classification]} |"
        )
    names = ", ".join(r.ticker for r in gated) or "none"
    out += ["", f"**Gated** (high-payout single-class names at peak with a large market premium): {names}."]
    md_path = outputs_dir / "dividend_window_test.md"
    md_path.write_text("\n".join(out) + "\n")
    return md_path


def run_dividend_window_xref(quarter: str) -> Path:
    """Build + render the §12 dividend-window diagnostic (called from the pipeline)."""
    return write_dividend_window_test(build_rows(quarter))
