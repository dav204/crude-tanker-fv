"""Consensus forward-EPS cross-check (METHODOLOGY.md §9.11).

The **earnings-leg analog of the broker-NAV sweep (§9.9)**. The broker sweep
cross-checks the *asset* leg of the blended FV (does our NAV agree with broker
consensus?); this cross-checks the *earnings* leg that drives the dividend strip
(do our modelled forward earnings agree with sell-side consensus?).

Mechanism. For each name with a published consensus 1-year-forward P/E (Pareto
Shipping Daily), we back out the consensus next-twelve-months EPS:

    consensus_fwd_eps = price / consensus_fwd_pe

and compare it to our own NTM forward EPS — the sum of the first four quarters of
the dividend strip's ``eps_by_quarter`` (the FFA-forward-curve-implied operating
EPS, net of tax, that feeds the strip's front end). Both are operating-EPS
constructs (the strip excludes one-off vessel-sale gains; forward consensus
likewise), so the comparison is apples-to-apples on operating earnings.

What the gap means. A large positive gap (tool EPS >> consensus) says our
forward-curve-implied earnings run hotter than the street — typically because the
FFA forward curve holds elevated near-peak rates while consensus bakes in
mean-reversion. This is the **earnings-driven** flag (analogous to mark-driven).
Crucially it is *expected* near a cycle peak, and the framework already
compensates: the cycle weighting down-weights the strip (low ``w_earn``) exactly
when the gap is widest. The row therefore carries ``cycle_position`` and
``w_earn`` so the reader can see the mitigation — a wide gap paired with a low
``w_earn`` is the framework working as designed, not a calibration error.

Limitations (see §9.11): 1-year horizon only (the strip is 8q + terminal NAV, so
this checks only the front end); EPS != dividends (payout policy and buybacks —
STNG's buyback channel is invisible to both EPS and the strip); shipping
consensus EPS is dispersed and lags spot. This is a directional cross-check, not
a calibration target.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from .cycle import compute_cycle
from .dividend_strip import compute_dividend_strip
from .loaders import INPUTS_DIR, load_company_inputs, load_watchlist
from .nav import compute_nav
from .report import OUTPUTS_DIR

# Names valued via crude+product carve-out — the whole-company FFA strip used here
# is a proxy (the headline FV uses the carve-out aggregation); flagged in output.
HYBRID_TICKERS = {"INSW"}

# |gap| at or above this ⇒ "earnings-driven": our strip EPS diverges materially
# from consensus. Wider than the §9.9 mark threshold (10pp) because forward EPS is
# structurally noisier than NAV and the FFA-vs-consensus normalisation gap is large
# by construction near a cycle peak.
EARNINGS_DRIVEN_THRESHOLD_PCT = 25.0

_STRIP_NTM_QUARTERS = 4


@dataclass
class ConsensusEpsRow:
    """One name's forward-EPS cross-check (consensus vs tool)."""

    ticker: str
    hybrid: bool
    sector: str
    price: float
    consensus_fwd_pe: float
    consensus_fwd_eps: float        # price / consensus_fwd_pe
    tool_fwd_eps: float             # sum of first 4 strip quarters (NTM, net of tax)
    tool_implied_pe: float | None   # price / tool_fwd_eps (None if tool EPS <= 0)
    eps_gap_pct: float              # 100 * (tool - consensus) / consensus
    consensus_earnings_yield_pct: float   # 100 / consensus_fwd_pe
    cycle_position: float
    band_label: str
    w_earn: float                   # strip weight in the blend (the mitigation)

    @property
    def earnings_driven(self) -> bool:
        return abs(self.eps_gap_pct) >= EARNINGS_DRIVEN_THRESHOLD_PCT

    @property
    def read(self) -> str:
        if not self.earnings_driven:
            return "earnings-aligned"
        hotter = "tool>cons" if self.eps_gap_pct > 0 else "tool<cons"
        return f"earnings-driven ({hotter})"


def compute_consensus_eps_rows(
    quarter: str, inputs_dir: Path = INPUTS_DIR
) -> list[ConsensusEpsRow]:
    """Build the consensus-vs-tool forward-EPS rows for every watchlist name
    with a published consensus_fwd_pe."""
    watchlist = load_watchlist(inputs_dir)
    rows: list[ConsensusEpsRow] = []
    for ticker, entry in watchlist.items():
        pe = entry.get("consensus_fwd_pe")
        if pe is None or pe <= 0:
            continue
        try:
            ci = load_company_inputs(ticker, quarter, inputs_dir)
        except FileNotFoundError:
            continue
        # Vintage-matched: consensus_fwd_pe is a Pareto ratio tied to the price
        # on the watchlist as_of date, so implied consensus EPS divides the
        # as_of price, never a live override (price_refresh.py docstring).
        price = float(entry.get("as_of_price") or entry["current_price"])
        nav = compute_nav(ci).nav_per_share
        cyc = compute_cycle(ci)
        strip = compute_dividend_strip(ci, nav, terminal_multiple=cyc.terminal_multiple)
        tool_fwd_eps = sum(strip.eps_by_quarter[:_STRIP_NTM_QUARTERS])
        consensus_fwd_eps = price / pe
        gap_pct = (
            100.0 * (tool_fwd_eps - consensus_fwd_eps) / consensus_fwd_eps
            if consensus_fwd_eps
            else 0.0
        )
        rows.append(ConsensusEpsRow(
            ticker=ticker,
            hybrid=ticker in HYBRID_TICKERS,
            sector=entry.get("sector", "crude"),
            price=price,
            consensus_fwd_pe=pe,
            consensus_fwd_eps=consensus_fwd_eps,
            tool_fwd_eps=tool_fwd_eps,
            tool_implied_pe=(price / tool_fwd_eps if tool_fwd_eps > 0 else None),
            eps_gap_pct=gap_pct,
            consensus_earnings_yield_pct=100.0 / pe,
            cycle_position=cyc.cycle_position,
            band_label=cyc.band_label,
            w_earn=cyc.w_earn,
        ))
    return rows


def write_consensus_eps_xref(
    rows: list[ConsensusEpsRow], outputs_dir: Path = OUTPUTS_DIR
) -> Path:
    """Render outputs/consensus_eps_xref.md (+ .xlsx)."""
    from openpyxl import Workbook
    from openpyxl.styles import Font

    outputs_dir.mkdir(parents=True, exist_ok=True)
    out: list[str] = []
    w = out.append
    w("# Consensus forward-EPS cross-check\n")
    w("The **earnings-leg analog of the broker-NAV sweep** (METHODOLOGY §9.11 / §9.9). "
      "The sweep asks whether our *NAV* agrees with broker consensus; this asks whether our "
      "modelled *forward earnings* — the input that drives the dividend strip — agree with "
      "sell-side consensus.\n")
    w("`consensus_fwd_eps = price / consensus_fwd_pe` (Pareto Shipping Daily, 1Y FWD P/E). "
      "`tool_fwd_eps` = sum of the first 4 quarters of our dividend strip's per-quarter EPS "
      "(NTM operating EPS, net of tax, FFA-forward-curve-implied). Both are operating-EPS "
      "constructs (each excludes one-off vessel-sale gains).\n")
    w("**Reading the gap.** A large positive gap (tool > consensus) means our forward-curve "
      "earnings run hotter than the street — typically the FFA curve holding near-peak rates "
      "while consensus prices mean-reversion. This is *expected* near a cycle peak, and the "
      "framework compensates: `w_earn` (the strip's weight in the blend) is low exactly when "
      "the gap is widest. **A wide gap + low `w_earn` is the cycle weighting working as "
      "designed, not an error.**\n")
    w("| Name | Sector | Price | Cons. fwd P/E | Cons. fwd EPS | Tool fwd EPS | Tool impl. P/E | "
      "EPS gap | Cons. earn. yld | Cycle (band) | w_earn | Read |")
    w("|---|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|---|")
    for r in sorted(rows, key=lambda x: x.eps_gap_pct, reverse=True):
        tag = " **(WHOLE-CO)**" if r.hybrid else ""
        impl_pe = f"{r.tool_implied_pe:.1f}×" if r.tool_implied_pe is not None else "n/a (EPS≤0)"
        w(f"| {r.ticker}{tag} | {r.sector} | ${r.price:,.2f} | {r.consensus_fwd_pe:.1f}× | "
          f"${r.consensus_fwd_eps:,.2f} | ${r.tool_fwd_eps:,.2f} | {impl_pe} | "
          f"{r.eps_gap_pct:+.0f}% | {r.consensus_earnings_yield_pct:.1f}% | "
          f"{r.cycle_position:.2f}× ({r.band_label}) | {r.w_earn:.2f} | {r.read} |")
    if any(r.hybrid for r in rows):
        w("\n_**(WHOLE-CO)** = hybrid name; the tool forward EPS here is the whole-company FFA "
          "strip (a proxy — the headline FV uses the crude+product carve-out aggregation)._\n")
    w("\n_Earnings-driven threshold: |gap| ≥ 25%. Near a cycle peak most names trip it on the "
      "high side by construction (FFA holds elevated rates; consensus normalises) — the signal "
      "is the **magnitude, direction, and cross-name pattern**, read alongside `w_earn`. "
      "Limitations: 1-year horizon only (strip is 8q + terminal NAV); EPS ≠ dividends "
      "(buyback channels like STNG are invisible); shipping consensus EPS is dispersed and "
      "lags spot. Directional cross-check, not a calibration target._\n")
    md_path = outputs_dir / "consensus_eps_xref.md"
    md_path.write_text("\n".join(out))

    wb = Workbook()
    ws = wb.active
    ws.title = "Consensus EPS xref"
    headers = ["ticker", "basis", "sector", "price", "consensus_fwd_pe", "consensus_fwd_eps",
               "tool_fwd_eps", "tool_implied_pe", "eps_gap_pct", "consensus_earnings_yield_pct",
               "cycle_position", "band_label", "w_earn", "read"]
    ws.append(headers)
    for c in ws[1]:
        c.font = Font(bold=True)
    for r in sorted(rows, key=lambda x: x.eps_gap_pct, reverse=True):
        basis = "WHOLE-COMPANY (hybrid proxy)" if r.hybrid else "whole-company"
        ws.append([
            r.ticker, basis, r.sector, round(r.price, 2), r.consensus_fwd_pe,
            round(r.consensus_fwd_eps, 3), round(r.tool_fwd_eps, 3),
            (round(r.tool_implied_pe, 2) if r.tool_implied_pe is not None else None),
            round(r.eps_gap_pct, 1), round(r.consensus_earnings_yield_pct, 2),
            round(r.cycle_position, 3), r.band_label, round(r.w_earn, 2), r.read,
        ])
    for col in ws.columns:
        width = max((len(str(c.value)) for c in col if c.value is not None), default=10)
        ws.column_dimensions[col[0].column_letter].width = min(width + 2, 30)
    wb.save(outputs_dir / "consensus_eps_xref.xlsx")
    return md_path


def run_consensus_eps_xref(
    quarter: str, inputs_dir: Path = INPUTS_DIR, outputs_dir: Path = OUTPUTS_DIR
) -> list[ConsensusEpsRow]:
    """Compute, write, and print the consensus forward-EPS cross-check."""
    rows = compute_consensus_eps_rows(quarter, inputs_dir)
    if rows:
        path = write_consensus_eps_xref(rows, outputs_dir)
        for r in sorted(rows, key=lambda x: x.eps_gap_pct, reverse=True):
            print(f"{r.ticker}: cons EPS ${r.consensus_fwd_eps:.2f} (P/E {r.consensus_fwd_pe:.1f}x) "
                  f"vs tool ${r.tool_fwd_eps:.2f} -> gap {r.eps_gap_pct:+.0f}% "
                  f"[{r.band_label}, w_earn {r.w_earn:.2f}] {r.read}")
        print(f"consensus-EPS cross-check -> {path}")
    return rows
