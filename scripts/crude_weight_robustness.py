"""Crude tanker weight-robustness diagnostic (METHODOLOGY §9.10).

Runs all six crude tanker watchlist names (DHT, ECO, FRO, INSW, TNK, NAT) under
four defensible probability-weight sets and classifies each name's position
recommendation as weight-robust (same call across all four) or weight-driven
(call changes across sets).

Driver (2026-06-01): Catlin / VIE analysis (2026-05-25) plus the June 1 macro
briefing suggest current crude weights {escalation 0.10, pre_mou_baseline 0.15,
mou_base 0.50, mou_bear 0.25} may put too much weight on "deep normalization"
relative to "slow normalization with extended Phase 1." This diagnostic does
NOT change the locked Set A weights — it surfaces which calls would survive a
defensible reweighting (Set B Catlin-leaning) vs which depend on the specific
Set A prior.

Output:
  - outputs/weight_robustness_diagnostic.md   (markdown table + per-name detail)
  - outputs/weight_robustness_diagnostic.xlsx (single sheet, machine-readable)

Naming-namespace note: this script uses "Set A/B/C/D" for CRUDE weight families.
The LNG sector already uses "Set B" / "Set B-revised" for its own weight family
(METHODOLOGY §11.3). To avoid ambiguity, every label here carries the explicit
"(crude)" qualifier. Cross-sector conflation would be a methodology error.
"""

from __future__ import annotations

import copy
import sys
from pathlib import Path

# Make src importable
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from crude_tanker_fv.loaders import load_company_inputs, load_watchlist
from crude_tanker_fv.pipeline import _load_all_sectors, _run_scenarios_for_ticker

# ----------------------------------------------------------------------------
# Weight definitions (METHODOLOGY §9.10)
# ----------------------------------------------------------------------------
# All four sets sum to 1.0 across the four active crude scenarios.
# Set A is the production lock; B / C / D are defensible alternatives chosen to
# bracket the "how fast does normalisation arrive" axis (the dominant
# uncertainty for 2026 crude calls).
CRUDE_WEIGHT_SETS = {
    "Crude Set A (current locked)": {
        "escalation": 0.10, "pre_mou_baseline": 0.15,
        "mou_base":   0.50, "mou_bear":         0.25,
    },
    "Crude Set B (Catlin-leaning, slow normalization)": {
        "escalation": 0.10, "pre_mou_baseline": 0.25,
        "mou_base":   0.45, "mou_bear":         0.20,
    },
    "Crude Set C (bullish, extended Phase 1)": {
        "escalation": 0.15, "pre_mou_baseline": 0.30,
        "mou_base":   0.40, "mou_bear":         0.15,
    },
    "Crude Set D (bearish, deep normalization)": {
        "escalation": 0.05, "pre_mou_baseline": 0.10,
        "mou_base":   0.55, "mou_bear":         0.30,
    },
}

for label, weights in CRUDE_WEIGHT_SETS.items():
    assert abs(sum(weights.values()) - 1.0) < 1e-9, f"{label} doesn't sum to 1"

CRUDE_TICKERS = ["DHT", "ECO", "FRO", "INSW", "TNK", "NAT"]


# ----------------------------------------------------------------------------
# Helpers
# ----------------------------------------------------------------------------
def doc_with_weights(base_doc: dict, weights: dict) -> dict:
    """Deep-copy the crude doc and overwrite scenario weights in place."""
    d = copy.deepcopy(base_doc)
    for name, w in weights.items():
        if name in d["scenarios"]:
            d["scenarios"][name]["weight"] = w
    return d


def position_label(ev_pct: float) -> str:
    """Same threshold as scenarios.position_recommendation but shorter labels."""
    if ev_pct > 5.0:
        return "BUY"
    if ev_pct < -5.0:
        return "TRIM/SHORT"
    return "HOLD"


# ----------------------------------------------------------------------------
# Per-ticker × per-weight-set run
# ----------------------------------------------------------------------------
def run_ticker_under_all_sets(ticker: str, watchlist: dict, base_sector_docs: dict):
    """Returns dict {set_label: {pw_fv, ev_pct, position}}.

    Uses the production scenario-routing path (`_run_scenarios_for_ticker`) so
    INSW's hybrid carve-out aggregation is handled identically to a real
    pipeline run. The weight override only touches `sector_docs["crude"]`, so
    INSW's product sleeve (running through `sectors.product`) is unchanged —
    the diagnostic correctly isolates the crude-weight sensitivity.
    """
    entry = watchlist[ticker]
    price = entry["current_price"]
    target = entry["analyst_target"]
    ci = load_company_inputs(ticker, "2026-Q1")

    results: dict[str, dict] = {}
    for set_label, weights in CRUDE_WEIGHT_SETS.items():
        # Build sector_docs with the overridden crude weights; LNG and product
        # docs pass through unchanged (their tickers aren't in this analysis
        # but the dict still needs to be complete for the routing logic).
        modified_docs = dict(base_sector_docs)
        modified_docs["crude"] = doc_with_weights(base_sector_docs["crude"], weights)

        report, _, _ = _run_scenarios_for_ticker(
            ticker, ci, price, target, modified_docs, watchlist,
        )
        ev_pct = report.expected_value_vs_current / price * 100.0
        results[set_label] = {
            "pw_fv":    round(report.probability_weighted_fv, 2),
            "ev_pct":   round(ev_pct, 1),
            "position": position_label(ev_pct),
        }
    return {"ticker": ticker, "price": price, "target": target, "results": results}


def classify_robustness(per_ticker: dict) -> tuple[str, list[str], str]:
    """Returns (verdict, positions_across_sets, robust_or_driven_note).

    WEIGHT-ROBUST = same position across all four sets.
    WEIGHT-DRIVEN = position changes; we identify which set produces the flip.
    """
    positions = [per_ticker["results"][s]["position"] for s in CRUDE_WEIGHT_SETS]
    unique_positions = set(positions)
    if len(unique_positions) == 1:
        return "WEIGHT-ROBUST", positions, f"position {positions[0]} across all four weight sets"

    # Weight-driven — describe the flip. Find the "majority" position then
    # name the dissenting set(s).
    set_labels = list(CRUDE_WEIGHT_SETS.keys())
    by_position: dict[str, list[str]] = {}
    for s, pos in zip(set_labels, positions):
        by_position.setdefault(pos, []).append(s)
    parts = []
    for pos, sets in by_position.items():
        # Shorten set label for inline display
        short = [s.split("(")[0].strip().replace("Crude ", "") for s in sets]
        parts.append(f"{pos} under {'/'.join(short)}")
    return "WEIGHT-DRIVEN", positions, "; ".join(parts)


# ----------------------------------------------------------------------------
# Output rendering
# ----------------------------------------------------------------------------
def render_markdown(analyses: list[dict]) -> str:
    lines: list[str] = []
    lines.append("# Crude Weight-Robustness Diagnostic\n")
    lines.append("Diagnostic (METHODOLOGY §9.10) — does NOT change the locked "
                 "Crude Set A weights. Surfaces which crude tanker calls "
                 "survive defensible reweighting (call is **weight-robust**) "
                 "vs which depend on a specific weight prior (**weight-driven**).")
    lines.append("")
    lines.append("**Driver:** Catlin / VIE analysis (2026-05-25) plus the "
                 "June 1 macro briefing suggest current Set A weights may put "
                 "too much weight on \"deep normalisation\" relative to \"slow "
                 "normalisation with extended Phase 1.\" Sets B/C/D bracket the "
                 "normalisation-speed axis.")
    lines.append("")
    lines.append("**Naming namespace:** the labels below are CRUDE-sector "
                 "weight families. The LNG sector uses its own \"Set B\" / "
                 "\"Set B-revised\" naming (METHODOLOGY §11.3). Cross-sector "
                 "conflation would be a methodology error.\n")

    # Pre-computed key findings block — gives the reader the headline before
    # the table. Hand-curated rather than auto-generated because the cross-
    # reference to mark spreads is the interesting interpretive layer.
    lines.append("## Key findings (combined mark + weight robustness)\n")
    lines.append("Cross-referencing with the broker-NAV sweep "
                 "(`outputs/broker_nav_sweep.md`):")
    lines.append("")
    lines.append("| Ticker | Mark spread | Weight robustness | Combined conviction |")
    lines.append("|---|---:|---|---|")
    lines.append("| DHT  | −1pp  (mark-robust)  | ✓ robust | **HIGHEST** — TRIM survives both dimensions |")
    lines.append("| ECO  | −1pp  (mark-robust)  | ✓ robust | **HIGHEST** — TRIM survives both dimensions |")
    lines.append("| FRO  | −1pp  (mark-robust)  | ✓ robust | **HIGHEST** — TRIM survives both dimensions |")
    lines.append("| INSW | +22pp (mark-driven)  | ✓ robust | MIXED — TRIM survives weights but depends on marks |")
    lines.append("| TNK  | +10pp (mark-driven)  | ⚑ driven | **LOWEST** — call sensitive to BOTH dimensions |")
    lines.append("| NAT  | +53pp (mark-driven)  | ✓ robust | **§12 archetype** — tool TRIM is structural (read NAV as floor, not call) |")
    lines.append("")
    lines.append("**Takeaway:** the three pure-VLCC / VLCC+Suezmax names "
                 "(DHT/ECO/FRO) are the highest-conviction TRIM calls in the "
                 "current crude watchlist — their TRIM signal survives both a "
                 "reasonable mark perturbation AND a defensible reweighting "
                 "toward Catlin's slow-normalisation view. **TNK is the only "
                 "name where both judgemental dimensions matter** — and "
                 "specifically, TNK flips to TRIM/SHORT only under the "
                 "bearish Set D weighting; under the Catlin-leaning Set B "
                 "TNK's EV is mildly positive (+0.8%). For TNK position "
                 "decisions, the weight prior is the dominant uncertainty.\n")

    # Weight-set definitions table
    lines.append("## Weight sets compared\n")
    lines.append("| Scenario | Set A (current) | Set B (Catlin) | Set C (bullish) | Set D (bearish) |")
    lines.append("|---|--:|--:|--:|--:|")
    scen_order = ["escalation", "pre_mou_baseline", "mou_base", "mou_bear"]
    for scen in scen_order:
        vals = [CRUDE_WEIGHT_SETS[s][scen] for s in CRUDE_WEIGHT_SETS]
        lines.append(f"| {scen} | {vals[0]:.2f} | {vals[1]:.2f} | {vals[2]:.2f} | {vals[3]:.2f} |")
    lines.append("")
    lines.append("Set B (Catlin-leaning) shifts 10pp from `mou_base` and 5pp "
                 "from `mou_bear` into `pre_mou_baseline` — i.e. Phase 1 "
                 "extends, Phase 2 normalisation arrives later. Set C is more "
                 "bullish (15pp into Phase 1). Set D is more bearish (15pp "
                 "deeper into MoU phase).\n")

    # Headline robustness table
    lines.append("## Summary — per-name robustness\n")
    lines.append("| Ticker | Set A EV | Set B EV | Set C EV | Set D EV | "
                 "Robustness | Notes |")
    lines.append("|---|--:|--:|--:|--:|---|---|")
    for a in analyses:
        r = a["results"]
        verdict, positions, note = classify_robustness(a)
        cells = []
        for s in CRUDE_WEIGHT_SETS:
            ev = r[s]["ev_pct"]
            pos = r[s]["position"]
            cells.append(f"{ev:+.1f}% ({pos})")
        badge = "✓ robust" if verdict == "WEIGHT-ROBUST" else "⚑ driven"
        lines.append(f"| {a['ticker']} | {cells[0]} | {cells[1]} | "
                     f"{cells[2]} | {cells[3]} | {badge} | {note} |")
    lines.append("")

    # Per-name detail
    lines.append("## Per-name detail\n")
    for a in analyses:
        lines.append(f"### {a['ticker']} — price ${a['price']:.2f}, target ${a['target']:.2f}\n")
        verdict, positions, note = classify_robustness(a)
        lines.append(f"**Classification:** {verdict}. {note}.\n")
        lines.append("| Weight set | PW FV | EV % | Position |")
        lines.append("|---|--:|--:|---|")
        for s, r in a["results"].items():
            lines.append(f"| {s} | ${r['pw_fv']:.2f} | {r['ev_pct']:+.1f}% | {r['position']} |")
        lines.append("")

    # Methodology + combined diagnostic note
    lines.append("## Combined mark + weight robustness framework\n")
    lines.append("Pairing this diagnostic with the broker-NAV sweep (METHODOLOGY §9.9) "
                 "gives every name two robustness dimensions:")
    lines.append("")
    lines.append("- **Mark-robust + weight-robust** = highest-conviction signals "
                 "(call survives both vessel-mark uncertainty and probability-"
                 "weight reshuffling)")
    lines.append("- **Mark-driven OR weight-driven** (one of the two) = "
                 "moderate conviction; the call depends on one specific "
                 "judgemental input")
    lines.append("- **Mark-driven AND weight-driven** = lowest conviction; "
                 "two compounding judgemental dependencies. Treat with "
                 "explicit sizing discipline.\n")

    lines.append("See METHODOLOGY §9.9 (mark robustness) and §9.10 (weight "
                 "robustness) for the methodology. This diagnostic is the "
                 "§9.10 output for the crude sector; the LNG analogue lives "
                 "in `outputs/lng_weight_robustness.md`.\n")

    return "\n".join(lines)


def write_xlsx(analyses: list[dict], path: Path) -> None:
    """Single-sheet xlsx — same content as the markdown table, machine-readable."""
    from openpyxl import Workbook
    from openpyxl.styles import Font, PatternFill

    wb = Workbook()
    ws = wb.active
    ws.title = "Weight robustness (crude)"

    headers = ["ticker", "price", "target"]
    for s in CRUDE_WEIGHT_SETS:
        # Strip the long parenthetical for column-header brevity
        short = s.split("(")[0].strip()
        headers.extend([f"{short} PW FV", f"{short} EV %", f"{short} position"])
    headers.extend(["robustness", "notes"])
    ws.append(headers)
    for c in ws[1]:
        c.font = Font(bold=True)

    driven_fill = PatternFill("solid", fgColor="FFE6E6")  # soft pink for flagged

    for a in analyses:
        verdict, positions, note = classify_robustness(a)
        row = [a["ticker"], a["price"], a["target"]]
        for s in CRUDE_WEIGHT_SETS:
            r = a["results"][s]
            row.extend([r["pw_fv"], r["ev_pct"], r["position"]])
        row.extend([verdict, note])
        ws.append(row)
        if verdict == "WEIGHT-DRIVEN":
            for c in ws[ws.max_row]:
                c.fill = driven_fill

    for col in ws.columns:
        width = max((len(str(c.value)) for c in col if c.value is not None), default=10)
        ws.column_dimensions[col[0].column_letter].width = min(width + 2, 40)

    wb.save(path)


# ----------------------------------------------------------------------------
# Main
# ----------------------------------------------------------------------------
def main():
    watchlist = load_watchlist()
    base_sector_docs = _load_all_sectors()

    analyses = []
    for ticker in CRUDE_TICKERS:
        if ticker not in watchlist:
            print(f"skip {ticker}: not in watchlist")
            continue
        a = run_ticker_under_all_sets(ticker, watchlist, base_sector_docs)
        analyses.append(a)

    project_root = Path(__file__).resolve().parents[1]
    out_md = project_root / "outputs" / "weight_robustness_diagnostic.md"
    out_xlsx = project_root / "outputs" / "weight_robustness_diagnostic.xlsx"

    out_md.write_text(render_markdown(analyses))
    write_xlsx(analyses, out_xlsx)

    print(f"→ {out_md}")
    print(f"→ {out_xlsx}")
    print()

    # Compact terminal summary
    print(f"{'Ticker':6s}  {'Set A':12s} {'Set B':12s} {'Set C':12s} {'Set D':12s}  Robustness")
    print("-" * 80)
    for a in analyses:
        verdict, positions, _ = classify_robustness(a)
        cells = []
        for s in CRUDE_WEIGHT_SETS:
            r = a["results"][s]
            cells.append(f"{r['ev_pct']:+5.1f}% {r['position'][:4]}")
        print(f"{a['ticker']:6s}  {cells[0]:12s} {cells[1]:12s} {cells[2]:12s} {cells[3]:12s}  {verdict}")


if __name__ == "__main__":
    main()
