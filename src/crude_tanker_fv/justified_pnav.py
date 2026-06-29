"""Justified P/NAV diagnostic (METHODOLOGY.md §17).

A **coverage-independent** companion to the broker-NAV sweep (§9.9) and the
consensus-EPS cross-check (§9.11). Where those two lean on Pareto coverage (a
broker P/NAV, a consensus forward P/E), this leg asks a question answerable from
fundamentals alone — **"does the fleet earn its cost of capital on its own marked
NAV?"** — so it gives the APPROX / no-Pareto names (SB, CMDB, GSL, MPCC, CCEC,
NAT, ASC, TEN, CMBT) a NAV benchmark they otherwise lack, and lets the subsector
multiple structure fall out of fundamentals rather than hand-set scenario weights.

Formula (Gordon / residual-income justified price-to-book, applied to NAV):

    P/NAV*           = (RONAV_norm − g) / (r − g)
                     = 1 + (RONAV_norm − r) / (r − g)        # residual-income form
    Justified FV/sh  = P/NAV* × NAV_per_share
    RONAV_implied    = g + (price / NAV_per_share) × (r − g)  # the market's implied return
    P/NAV(mkt)       = price / NAV_per_share

where:

- ``NAV_per_share`` is the tool's CLEAN, un-haircut marked NAV (``compute_nav`` —
  the governance discount is applied downstream of it, never inside it, so this is
  the denominator the P/NAV signal needs).
- ``RONAV_norm`` is return on (marked) NAV at THROUGH-CYCLE earning power:
  ``normalized_annual_EPS / NAV_per_share``, where ``normalized_annual_EPS`` runs
  the existing dividend-strip earnings machinery with every vessel class's TCE set
  to its cycle anchor (``historical_tce_means`` — the same anchor ``cycle.py`` uses
  for cycle position), NOT the FFA forward curve (the hot NTM number the strip's
  front end carries near a peak, which would inflate the multiple). It is return on
  marked NAV, not on depreciated book (book always "earns well" mid-cycle and says
  nothing about whether the market value is justified), and it is mid-cycle, not
  next-twelve-months.
- ``r`` = ``COST_OF_EQUITY`` (11%), constant across all names in v1.
- ``g`` = per-subsector sustainable nominal growth (``sectors.<sector>.g`` in
  ``scenario_inputs.yaml``).

This is a DIAGNOSTIC ONLY — it is not wired into the headline FV, and whether
justified- (or subsector-demeaned-) P/NAV predicts forward returns is a separate,
pre-registered study (§17). ``r − g`` is a small denominator, so the multiple is
hypersensitive to ``g`` and ``RONAV_norm`` (±1pp swings it 10-20%): read it as an
ORDERING tool, not a precision estimate. See §17 for the dry-bulk anchor-bias and
dwt-scaling caveats.
"""

from __future__ import annotations

from dataclasses import dataclass, replace
from pathlib import Path
from statistics import median
from typing import Optional

from .dividend_strip import STRIP_HORIZON_QUARTERS, compute_dividend_strip
from .loaders import INPUTS_DIR, load_company_inputs, load_watchlist
from .nav import COST_OF_EQUITY, compute_nav
from .report import OUTPUTS_DIR
from .scenarios import SCENARIOS_PATH, load_scenarios
from .schemas import CompanyInputs
from .vessel_values import vessel_market_value

# Hybrid name registries (single source of truth — pipeline owns them). The
# import is acyclic: pipeline imports THIS module only lazily inside main().
from .pipeline import HYBRID_TICKERS, MULTI_SLEEVE_TICKERS, THREE_SLEEVE_TICKERS

# Fallback per-subsector growth if a sector lacks an explicit ``g:`` in the YAML.
DEFAULT_G = 0.01

# Newbuild value share above which RONAV_norm is unreliable (a not-yet-delivered
# hull earns a full anchor-year in the strip while its NAV is PV-haircut and its
# capex commitment never hits strip EPS — the numerator/denominator bases are
# irreconcilable). The observed distribution is bimodal: newbuild-DOMINATED names
# (BRUT 100%, CAPT 73%, MPCC 40%) sit well above a flagship with a modest program
# (FRO ~17%), so 25% cleanly separates them — FRO computes (with a mild residual
# bias, footnoted) and stays in its sector median.
NEWBUILD_HEAVY_SHARE = 0.25

# |Justified P/NAV − P/NAV(mkt)| within this fraction of P/NAV(mkt) reads "fair".
FAIR_BAND = 0.10

_NTM_QUARTERS = 4


# ---------------------------------------------------------------------------
# Pure formula functions (unit-tested to agree / round-trip)
# ---------------------------------------------------------------------------
def justified_pnav(ronav_norm: float, r: float, g: float) -> float:
    """Gordon form: (RONAV_norm − g) / (r − g)."""
    return (ronav_norm - g) / (r - g)


def justified_pnav_resid(ronav_norm: float, r: float, g: float) -> float:
    """Residual-income form: 1 + (RONAV_norm − r) / (r − g). Equals the Gordon form."""
    return 1.0 + (ronav_norm - r) / (r - g)


def ronav_implied(price: float, nav_per_share: float, r: float, g: float) -> float:
    """The return on NAV the market is pricing in: g + (price/NAV) × (r − g)."""
    return g + (price / nav_per_share) * (r - g)


# ---------------------------------------------------------------------------
# Normalized through-cycle earning power
# ---------------------------------------------------------------------------
def normalized_annual_eps(
    ci: CompanyInputs, nav_per_share: float
) -> tuple[Optional[float], list[str]]:
    """Annual EPS with every vessel class's TCE pinned to its cycle anchor.

    Returns ``(eps, missing_anchor_classes)``. ``eps`` is None iff a fleet class
    has no ``historical_tce_means`` anchor (then ``missing`` is non-empty). The
    strip is reused unchanged via a normalized ``CompanyInputs``:

    - ``ffa_forward_curve`` -> flat per-class anchor (the through-cycle rate),
    - coverage neutralized (cov=0 ⇒ blended TCE = anchor for EVERY vessel, so a
      name's idiosyncratic locked-charter book does not leak into a through-cycle
      number — load-bearing for names with real disclosed charters like CCEC),
    - ``fleet_schedule`` neutralized ⇒ all current manifest vessels earn a full
      anchor-year (steady-state), matched to the full-fleet NAV denominator.

    Annual EPS = sum of the first four quarters (flat rates + static fleet ⇒ the
    four quarters are identical, so this is 4× the quarterly figure). The strip's
    terminal value is computed but discarded — only ``eps_by_quarter`` is read.
    """
    md = ci.market_data
    anchors = md.historical_tce_means
    fleet_classes = {v.cls for v in ci.fleet.vessels}
    missing = sorted(c for c in fleet_classes if c not in anchors)
    if missing:
        return None, missing
    norm_ffa = {cls: [anchors[cls]] * STRIP_HORIZON_QUARTERS for cls in fleet_classes}
    norm_md = replace(md, ffa_forward_curve=norm_ffa)
    norm_fleet = replace(
        ci.fleet, coverage_schedule={}, spot_coverage_pct={}, fleet_schedule={}
    )
    norm_ci = replace(ci, market_data=norm_md, fleet=norm_fleet)
    strip = compute_dividend_strip(norm_ci, nav_per_share)
    return sum(strip.eps_by_quarter[:_NTM_QUARTERS]), []


def _newbuild_value_share(ci: CompanyInputs) -> float:
    """Fraction of fleet market value carried by not-yet-delivered newbuilds."""
    curves = ci.market_data.vessel_value_curves
    yard_discounts = ci.market_data.yard_discounts
    total = 0.0
    newbuild = 0.0
    for v in ci.fleet.vessels:
        value = vessel_market_value(v, curves[v.cls], yard_discounts) * v.count
        total += value
        if v.years_to_delivery > 0:
            newbuild += value
    return newbuild / total if total else 0.0


# ---------------------------------------------------------------------------
# Row model
# ---------------------------------------------------------------------------
@dataclass
class JustifiedPnavRow:
    """One name's justified-P/NAV read. Multiple/FV/label are None when a guard trips."""

    ticker: str
    hybrid: bool
    sector: str
    nav_per_share: float
    price: float
    pnav_mkt: Optional[float]              # price / NAV
    ronav_norm: Optional[float]            # normalized annual EPS / NAV
    r: float
    g: float
    justified_pnav: Optional[float]        # (RONAV_norm − g)/(r − g)
    justified_fv: Optional[float]          # justified P/NAV × NAV
    ronav_implied: Optional[float]         # g + P/NAV(mkt)·(r − g)
    gap: Optional[float]                   # RONAV_norm − RONAV_implied
    flag: Optional[str]                    # guard that blocked the multiple, else None

    @property
    def read(self) -> str:
        if self.flag is not None:
            return self.flag
        diff = self.justified_pnav - self.pnav_mkt
        if abs(diff) <= FAIR_BAND * self.pnav_mkt:
            return "fair"
        return "cheap" if diff > 0 else "rich"


def _g_by_sector(inputs_dir: Path) -> dict[str, float]:
    """Per-sector sustainable growth from ``sectors.<sector>.g``."""
    path = inputs_dir / "scenario_inputs.yaml" if inputs_dir != INPUTS_DIR else SCENARIOS_PATH
    out: dict[str, float] = {}
    for sector in ("crude", "product", "lng", "dry_bulk", "containerships"):
        try:
            doc = load_scenarios(path, sector)
        except KeyError:
            continue
        gv = doc.get("g")
        if gv is not None:
            out[sector] = float(gv)
    return out


@dataclass
class _Eval:
    """Outcome of the guard+formula decision (pure; testable with scalars)."""

    flag: Optional[str]
    ronav_norm: Optional[float]
    pnav_mkt: Optional[float]
    ronav_implied: Optional[float]
    justified_pnav: Optional[float]
    justified_fv: Optional[float]
    gap: Optional[float]


def evaluate(
    nav: float,
    price: float,
    eps: Optional[float],
    missing_anchor: bool,
    has_cost: bool,
    newbuild_share: float,
    r: float,
    g: float,
) -> _Eval:
    """Apply the ordered guards and (if all pass) the justified-P/NAV formula.

    ``eps`` is the normalized annual EPS (None when a guard upstream made it
    uncomputable). The first blocking guard wins; a flagged row carries no
    multiple/FV but may still show RONAV_norm (newbuild-heavy) and a gap.
    """
    pnav_mkt = price / nav if nav > 0 else None
    implied = ronav_implied(price, nav, r, g) if nav > 0 and r > g else None
    flag: Optional[str] = None
    ronav: Optional[float] = None
    if nav <= 0:
        flag = "non-positive NAV"
    elif not has_cost:
        flag = "no cost data"
    elif r - g <= 0:
        flag = "r≤g (invalid)"
    elif missing_anchor:
        flag = "no anchor"
    else:
        # newbuild-heavy still shows RONAV_norm (for transparency) but no multiple
        if newbuild_share > NEWBUILD_HEAVY_SHARE:
            flag = "newbuild-heavy (unreliable)"
        ronav = eps / nav
        if eps < 0 and flag is None:
            flag = "negative mid-cycle EPS"
        elif ronav < g and flag is None:
            flag = "sub-growth returns"
    gap = ronav - implied if (ronav is not None and implied is not None) else None
    justified = justified_pnav(ronav, r, g) if (flag is None and ronav is not None) else None
    fv = justified * nav if justified is not None else None
    return _Eval(flag, ronav, pnav_mkt, implied, justified, fv, gap)


def compute_justified_pnav_rows(
    quarter: str, inputs_dir: Path = INPUTS_DIR
) -> list[JustifiedPnavRow]:
    """Build the justified-P/NAV row for every valued watchlist name.

    Coverage-independent: iterates ALL names (no consensus_fwd_pe / consensus_pnav
    gate), so the APPROX names get a benchmark too.
    """
    watchlist = load_watchlist(inputs_dir)
    g_by_sector = _g_by_sector(inputs_dir)
    rows: list[JustifiedPnavRow] = []
    for ticker, entry in watchlist.items():
        try:
            ci = load_company_inputs(ticker, quarter, inputs_dir)
        except FileNotFoundError:
            continue
        sector = entry.get("sector", "crude")
        g = g_by_sector.get(sector, DEFAULT_G)
        r = COST_OF_EQUITY
        # Vintage price, same convention as consensus_eps (deterministic; tool-NAV based).
        price = float(entry.get("as_of_price") or entry["current_price"])
        nav = compute_nav(ci).nav_per_share
        has_cost = bool(ci.cost_structure.opex_per_day)

        eps: Optional[float] = None
        missing: list[str] = []
        if nav > 0 and has_cost and r > g:
            eps, missing = normalized_annual_eps(ci, nav)
        ev = evaluate(
            nav, price, eps, bool(missing), has_cost, _newbuild_value_share(ci), r, g
        )

        rows.append(JustifiedPnavRow(
            ticker=ticker,
            hybrid=(
                ticker in HYBRID_TICKERS
                or ticker in THREE_SLEEVE_TICKERS
                or ticker in MULTI_SLEEVE_TICKERS
            ),
            sector=sector,
            nav_per_share=nav,
            price=price,
            pnav_mkt=ev.pnav_mkt,
            ronav_norm=ev.ronav_norm,
            r=r,
            g=g,
            justified_pnav=ev.justified_pnav,
            justified_fv=ev.justified_fv,
            ronav_implied=ev.ronav_implied,
            gap=ev.gap,
            flag=ev.flag,
        ))
    return rows


# ---------------------------------------------------------------------------
# Summaries
# ---------------------------------------------------------------------------
def subsector_median_pnav(rows: list[JustifiedPnavRow]) -> dict[str, float]:
    """Median Justified P/NAV by sector (valid rows only) — the headline artifact."""
    by_sector: dict[str, list[float]] = {}
    for r in rows:
        if r.justified_pnav is not None:
            by_sector.setdefault(r.sector, []).append(r.justified_pnav)
    return {s: median(v) for s, v in by_sector.items() if v}


def _sector_base_ronav(rows: list[JustifiedPnavRow]) -> dict[str, float]:
    """Median RONAV_norm by sector (valid rows) — the sensitivity-grid base."""
    by_sector: dict[str, list[float]] = {}
    for r in rows:
        if r.justified_pnav is not None and r.ronav_norm is not None:
            by_sector.setdefault(r.sector, []).append(r.ronav_norm)
    return {s: median(v) for s, v in by_sector.items() if v}


_GRID_G = (0.0, 0.01, 0.02)
_GRID_RONAV_OFFSETS = (-0.02, 0.0, 0.02)


# ---------------------------------------------------------------------------
# Output
# ---------------------------------------------------------------------------
def _pct(x: Optional[float], places: int = 1, signed: bool = False) -> str:
    if x is None:
        return "n/a"
    sign = "+" if signed else ""
    return f"{x * 100.0:{sign}.{places}f}%"


def write_justified_pnav(
    rows: list[JustifiedPnavRow], outputs_dir: Path = OUTPUTS_DIR
) -> Path:
    """Render outputs/justified_pnav.md (+ .xlsx)."""
    from openpyxl import Workbook
    from openpyxl.styles import Font

    outputs_dir.mkdir(parents=True, exist_ok=True)
    r0 = COST_OF_EQUITY
    out: list[str] = []
    w = out.append
    w("# Justified P/NAV diagnostic\n")
    w("A **coverage-independent** fair-multiple benchmark (METHODOLOGY §17). The broker-NAV "
      "sweep (§9.9) and consensus-EPS cross-check (§9.11) lean on Pareto coverage; this asks a "
      "question answerable from fundamentals alone — **does the fleet earn its cost of capital "
      "on its own marked NAV (net asset value)?** — so the APPROX / no-Pareto names (SB, CMDB, "
      "GSL, MPCC, CCEC, NAT, ASC, TEN, CMBT) get a NAV benchmark too.\n")
    w("**`RONAV` = return on NAV** — the asset-NAV analog of return on equity: annual earnings ÷ "
      "NAV per share. Two variants appear below. **`RONAV_norm`** (normalized) is what the fleet "
      "*would* earn on its marked NAV at mid-cycle rates; **`RONAV_implied`** is the return on NAV "
      "the *market price* is implying, backed out of the same identity.\n")
    w("`P/NAV* = (RONAV_norm − g)/(r − g) = 1 + (RONAV_norm − r)/(r − g)`; "
      "`Justified FV/sh = P/NAV* × NAV/sh`; `RONAV_implied = g + P/NAV(mkt)·(r − g)`. "
      f"`r` = cost of equity {r0:.0%} (constant in v1). `NAV/sh` is the tool's CLEAN, "
      "un-haircut marked NAV (governance discount is applied downstream, never inside it).\n")
    w("**RONAV_norm is return on *marked NAV*, not on accounting book**, and **through-cycle, not "
      "NTM (next-twelve-months)**: `normalized_annual_EPS / NAV/sh`, where the EPS runs the "
      "dividend-strip earnings machinery with every vessel class's day-rate (TCE, time-charter "
      "equivalent) pinned to its cycle anchor (`historical_tce_means`), NOT the FFA (forward "
      "freight agreement) forward curve. Book always 'earns well' mid-cycle and says nothing "
      "about whether the market value is justified; the FFA front end is the hot near-term number "
      "that would inflate the multiple — both are deliberately avoided.\n")
    w("**Read this as an ORDERING tool, not a precision estimate.** `r − g` is a small "
      "denominator, so the multiple is hypersensitive: ±1pp on `g` or `RONAV_norm` swings it "
      "10-20% (see the per-sector sensitivity grids below). **Anchor-bias caveats — RONAV_norm "
      "inherits the cycle anchors, which are not all true long-run means:** (1) **dry-bulk** "
      "anchors are 22-month firm-window medians, biased elevated (§11.7.5), so its multiples are "
      "an **upper bound**; (2) **containership** anchors are FY2021-2025 calendar averages "
      "(boom-tilted, `fy_calendar_avg` per §10 — NOT a through-cycle mean), so containership "
      "`RONAV_norm` is biased high even more than dry-bulk — GSL/MPCC's multiples are a **loose "
      "upper bound, not a real target**; (3) NAV dwt-scales per vessel but strip revenue is "
      "per-class count-based, so large-hull dry-bulk names (SB, CMBT) are biased toward 'rich' "
      "(partially offsetting (1)).\n")
    w("**Not in the headline FV** (diagnostic only); whether justified-P/NAV ranking predicts "
      "forward returns is a separate pre-registered study.\n")

    w("| Ticker | Sector | NAV/sh | Price | P/NAV (mkt) | RONAV_norm | r | g | "
      "Justified P/NAV | Justified FV/sh | RONAV_implied (mkt) | Gap (RONAV−impl) | Read |")
    w("|---|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|---|")

    def _sort_key(row: JustifiedPnavRow):
        # Valid rows by gap descending (cheapest first); flagged rows last.
        return (0, -(row.gap if row.gap is not None else 0.0)) if row.flag is None else (1, 0.0)

    for r in sorted(rows, key=_sort_key):
        tag = " **(WHOLE-CO)**" if r.hybrid else ""
        pnav_mkt = f"{r.pnav_mkt:.3f}×" if r.pnav_mkt is not None else "n/a"
        jp = f"{r.justified_pnav:.3f}×" if r.justified_pnav is not None else "—"
        fv = f"${r.justified_fv:,.2f}" if r.justified_fv is not None else "—"
        gap = _pct(r.gap, 1, signed=True) if r.gap is not None else "—"
        w(f"| {r.ticker}{tag} | {r.sector} | ${r.nav_per_share:,.2f} | ${r.price:,.2f} | "
          f"{pnav_mkt} | {_pct(r.ronav_norm)} | {r.r:.0%} | {r.g:.1%} | {jp} | {fv} | "
          f"{_pct(r.ronav_implied)} | {gap} | {r.read} |")

    medians = subsector_median_pnav(rows)
    w("\n## Subsector vector — median Justified P/NAV\n")
    w("| Sector | Median Justified P/NAV | n |")
    w("|---|--:|--:|")
    counts = {s: sum(1 for r in rows if r.sector == s and r.justified_pnav is not None)
              for s in medians}
    for s in sorted(medians, key=lambda s: medians[s], reverse=True):
        w(f"| {s} | {medians[s]:.3f}× | {counts[s]} |")
    w("\n_Expected ordering lng / containerships ≥ tankers ≥ dry bulk — but the dry-bulk "
      "anchor-bias (upward) and dwt-scaling (downward on the multiple) caveats above make a "
      "strict ordering indicative only._\n")

    bases = _sector_base_ronav(rows)
    w("\n## Sensitivity grids — Justified P/NAV across g × RONAV_norm "
      f"(r = {r0:.0%}, base = sector median RONAV_norm)\n")
    for s in sorted(bases):
        base = bases[s]
        w(f"\n**{s}** (base RONAV_norm {base * 100:.1f}%)\n")
        w("| RONAV_norm \\ g | " + " | ".join(f"g={gg:.0%}" if gg else "g=0%" for gg in _GRID_G) + " |")
        w("|---|" + "--:|" * len(_GRID_G))
        for off in _GRID_RONAV_OFFSETS:
            ronav = base + off
            cells = []
            for gg in _GRID_G:
                if r0 - gg <= 0:
                    cells.append("n/a")
                else:
                    cells.append(f"{justified_pnav(ronav, r0, gg):.2f}×")
            w(f"| {ronav * 100:.1f}% | " + " | ".join(cells) + " |")

    if any(r.hybrid for r in rows):
        w("\n_**(WHOLE-CO)** = hybrid (INSW / TEN / CMBT) valued whole-company: whole-company "
          "normalized EPS ÷ whole-company NAV, with the lead-sleeve `g` (the watchlist sector "
          "tag). Value-weighted `g` is the intended v2 refinement._\n")
    w("\n_Flags: `non-positive NAV`, `no cost data`, `no anchor`, `r≤g (invalid)`, "
      "`newbuild-heavy (unreliable)` (newbuild value share > 25% — a not-yet-delivered hull "
      "earns a full anchor-year in the strip while its NAV is PV-haircut), `negative mid-cycle "
      "EPS`, `sub-growth returns` (RONAV_norm < g ⇒ P/NAV* unstable). Flagged rows carry no "
      "multiple. Names with a sub-threshold newbuild program (e.g. FRO ~17%) compute but carry "
      "a mild residual upward RONAV bias. Per-subsector `r` is a documented v2 extension._\n")

    md_path = outputs_dir / "justified_pnav.md"
    md_path.write_text("\n".join(out))

    wb = Workbook()
    ws = wb.active
    ws.title = "Justified PNAV"
    headers = ["ticker", "basis", "sector", "nav_per_share", "price", "pnav_mkt",
               "ronav_norm", "r", "g", "justified_pnav", "justified_fv",
               "ronav_implied", "gap", "read", "flag"]
    ws.append(headers)
    for c in ws[1]:
        c.font = Font(bold=True)
    for r in sorted(rows, key=_sort_key):
        basis = "WHOLE-COMPANY (hybrid)" if r.hybrid else "whole-company"
        ws.append([
            r.ticker, basis, r.sector, round(r.nav_per_share, 3), round(r.price, 2),
            (round(r.pnav_mkt, 4) if r.pnav_mkt is not None else None),
            (round(r.ronav_norm, 4) if r.ronav_norm is not None else None),
            round(r.r, 4), round(r.g, 4),
            (round(r.justified_pnav, 4) if r.justified_pnav is not None else None),
            (round(r.justified_fv, 2) if r.justified_fv is not None else None),
            (round(r.ronav_implied, 4) if r.ronav_implied is not None else None),
            (round(r.gap, 4) if r.gap is not None else None),
            r.read, (r.flag or ""),
        ])
    for col in ws.columns:
        width = max((len(str(c.value)) for c in col if c.value is not None), default=10)
        ws.column_dimensions[col[0].column_letter].width = min(width + 2, 26)

    ws2 = wb.create_sheet("sensitivity")
    ws2.append(["sector", "base_ronav_norm", "ronav_norm", *[f"g={gg}" for gg in _GRID_G]])
    for c in ws2[1]:
        c.font = Font(bold=True)
    for s in sorted(bases):
        base = bases[s]
        for off in _GRID_RONAV_OFFSETS:
            ronav = base + off
            cells = [
                (round(justified_pnav(ronav, r0, gg), 4) if r0 - gg > 0 else None)
                for gg in _GRID_G
            ]
            ws2.append([s, round(base, 4), round(ronav, 4), *cells])
    for col in ws2.columns:
        width = max((len(str(c.value)) for c in col if c.value is not None), default=10)
        ws2.column_dimensions[col[0].column_letter].width = min(width + 2, 18)

    wb.save(outputs_dir / "justified_pnav.xlsx")
    return md_path


def run_justified_pnav_xref(
    quarter: str, inputs_dir: Path = INPUTS_DIR, outputs_dir: Path = OUTPUTS_DIR
) -> list[JustifiedPnavRow]:
    """Compute, write, and print the justified-P/NAV diagnostic."""
    rows = compute_justified_pnav_rows(quarter, inputs_dir)
    if rows:
        path = write_justified_pnav(rows, outputs_dir)
        for r in sorted(rows, key=lambda x: (x.gap is None, -(x.gap or 0.0))):
            jp = f"{r.justified_pnav:.2f}x" if r.justified_pnav is not None else "—"
            pm = f"{r.pnav_mkt:.2f}x" if r.pnav_mkt is not None else "n/a"
            print(f"{r.ticker}: P/NAV mkt {pm} vs justified {jp} "
                  f"[RONAV_norm {_pct(r.ronav_norm)}] {r.read}")
        for s, m in sorted(subsector_median_pnav(rows).items(), key=lambda kv: kv[1], reverse=True):
            print(f"  median justified P/NAV [{s}] = {m:.2f}x")
        print(f"justified-P/NAV diagnostic -> {path}")
    return rows
