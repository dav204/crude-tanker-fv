"""FFA forward curve vs the synthesised dry-bulk scenario strip.

The Stage-1 payoff diagnostic (METHODOLOGY §11.7.7 re-scope, rationale
b/c): lay the market's traded forward curve against the Bulk Set A
probability-weighted rate paths and see where the synthesised strip runs
hot or cold. Diagnostic only — writes outputs/ffa_vs_strip.md, touches
no pipeline input. Re-run at each refresh while the FFA curve is in its
diagnostic cycle.

Comparison caveats (carry these into any reading):
- FFA settles on the 5TC/“index” vessel; fleets earn index +/- premia
  (scrubber, size — an Ultramax earns over the Smax index, a scrubber
  Cape over C5TC). A modest tool-over-market gap can be premium, not heat.
- The traded curve embeds a risk premium; it is not a pure expectation.
- Panel mapping: Cape->cape, Pmax->pana, Smax->supra_ultra (same Pareto
  benchmark family the cycle anchors were derived from).

Usage: PYTHONPATH=src .venv/bin/python scripts/ffa_vs_strip.py
"""

import json
import statistics
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
CURVES_PATH = ROOT / "state" / "ffa_ocr_curves.json"
OUT_PATH = ROOT / "outputs" / "ffa_vs_strip.md"

PANEL_TO_CLASS = {"cape": "cape", "pmax": "pana", "smax": "supra_ultra"}
SMOOTH_DAYS = 5

# FFA tenor -> the strip quarters it speaks to (as of a mid-2026 vantage).
TENOR_TO_QUARTERS = {
    "q3": ["q3_2026"],
    "q4": ["q4_2026"],
    "cal27": ["q1_2027", "q2_2027", "q3_2027", "q4_2027"],
}


def load_ffa():
    db = json.loads(CURVES_PATH.read_text())
    clean = {d: e for d, e in db.items() if e.get("status") == "ok"}
    if not clean:
        sys.exit("no clean FFA curves parsed yet")
    days = sorted(clean)[-SMOOTH_DAYS:]
    smoothed: dict[str, dict[str, float]] = {}
    for panel in PANEL_TO_CLASS:
        smoothed[panel] = {}
        for tenor in TENOR_TO_QUARTERS:
            vals = [clean[d]["curves"][panel][tenor] for d in days
                    if tenor in clean[d]["curves"].get(panel, {})]
            if vals:
                smoothed[panel][tenor] = statistics.mean(vals)
    return days, smoothed


def load_strip():
    sector = yaml.safe_load((ROOT / "inputs" / "scenario_inputs.yaml").read_text())
    d = sector["sectors"]["dry_bulk"]["scenarios"]
    weights = {name: body["weight"] for name, body in d.items()}
    mids = {name: {cls: {q: v[1] for q, v in body[cls].items()}
                   for cls in PANEL_TO_CLASS.values()}
            for name, body in d.items()}
    return weights, mids


def main():
    days, ffa = load_ffa()
    weights, mids = load_strip()

    lines = [
        "# FFA forward curve vs synthesised dry-bulk strip",
        "",
        f"FFA legs: mean of the last {len(days)} clean parsed days "
        f"({days[0]} → {days[-1]}), `state/ffa_ocr_curves.json`.",
        "Strip legs: Bulk Set A probability-weighted scenario MIDs "
        "(`sectors.dry_bulk`, weights "
        + ", ".join(f"{k} {v:.2f}" for k, v in weights.items()) + ").",
        "",
        "Diagnostic only — see scripts/ffa_vs_strip.py header for caveats",
        "(index vs earned-TCE premia, risk premium in the traded curve).",
        "",
        "| Class | Tenor | FFA | Strip PW mid | Strip vs FFA | Nearest scenario |",
        "|---|---|---|---|---|---|",
    ]
    summary = {}
    for panel, cls in PANEL_TO_CLASS.items():
        for tenor, quarters in TENOR_TO_QUARTERS.items():
            if tenor not in ffa[panel]:
                continue
            market = ffa[panel][tenor]
            pw = statistics.mean(
                sum(weights[s] * mids[s][cls][q] for s in weights)
                for q in quarters)
            per_scenario = {
                s: statistics.mean(mids[s][cls][q] for q in quarters)
                for s in weights}
            nearest = min(per_scenario, key=lambda s: abs(per_scenario[s] - market))
            gap = (pw / market - 1.0) * 100.0
            summary.setdefault(cls, []).append(gap)
            lines.append(f"| {cls} | {tenor} | ${market:,.0f} | ${pw:,.0f} "
                         f"| {gap:+.1f}% | {nearest} (${per_scenario[nearest]:,.0f}) |")

    lines += ["", "## Read", ""]
    for cls, gaps in summary.items():
        avg = statistics.mean(gaps)
        verdict = ("HOT vs market" if avg > 10 else
                   "cold vs market" if avg < -10 else "market-consistent (±10%)")
        lines.append(f"- **{cls}**: strip runs {avg:+.1f}% vs the traded curve "
                     f"on average — {verdict}.")
    lines += [
        "",
        "Curve shape (market statement for the Bulk Set A weight diagnostic):",
    ]
    for panel, cls in PANEL_TO_CLASS.items():
        c = ffa[panel]
        if "q3" in c and "cal27" in c:
            slope = (c["cal27"] / c["q3"] - 1.0) * 100.0
            lines.append(f"- {cls}: Q3-26 ${c['q3']:,.0f} → Cal27 "
                         f"${c['cal27']:,.0f} ({slope:+.1f}% — "
                         f"{'backwardated' if slope < 0 else 'contango'})")

    OUT_PATH.write_text("\n".join(lines) + "\n")
    print("\n".join(lines))
    print(f"\n-> {OUT_PATH.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
