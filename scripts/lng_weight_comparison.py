"""Ad-hoc analysis: LNG Set B vs candidate Set B-revised weight comparison.

Driven by the Ras Laffan Trains 4 & 6 reality check (12.8 mtpa / ~17% of Qatar
LNG offline through end-summer 2026 at earliest, restart risk), which
partially offsets the US Gulf Coast capacity ramp (Cheniere Stage 3 Trains
5/6) through H2 2026. Current Set B puts 55% on glut_base, which implicitly
asserts that glut is the dominant 2026 condition. Empirical: LNG spot $67.5k
(+391% YoY) and TFDE $98.5k point at tight-market pricing, not glut.

This script reads the current LNG scenario doc, builds the candidate Set
B-revised weights in memory, re-runs FLNG and CCEC under both, and outputs:
  1. Per-scenario FV table (same for both weight sets)
  2. Probability-weighted FV under Set B vs Set B-revised + EV% / position
  3. Threshold analysis: minimum weight shift that flips FLNG to HOLD / BUY

Does NOT mutate inputs/scenario_inputs.yaml. Decision happens after review.
"""

from __future__ import annotations

import copy
import sys
from pathlib import Path

# Make src importable
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from crude_tanker_fv.loaders import load_company_inputs, load_watchlist
from crude_tanker_fv.scenarios import load_scenarios, run_scenarios

# ----------------------------------------------------------------------------
# Weight definitions
# ----------------------------------------------------------------------------
SET_B = {
    "tight_resurgence":     0.10,
    "moderate_tightening":  0.15,
    "glut_base":            0.55,
    "glut_intensifies":     0.20,
    "structural_reset":     0.00,
}

SET_B_REVISED = {
    "tight_resurgence":     0.15,   # +0.05 — Ras Laffan + winter
    "moderate_tightening":  0.25,   # +0.10 — 2026 ramp partially absorbed
    "glut_base":            0.45,   # -0.10 — glut shifts to 2027
    "glut_intensifies":     0.15,   # -0.05 — 2026 doesn't justify extreme glut
    "structural_reset":     0.00,   # unchanged
}

assert abs(sum(SET_B.values()) - 1.0) < 1e-9, "Set B weights don't sum to 1"
assert abs(sum(SET_B_REVISED.values()) - 1.0) < 1e-9, "Set B-revised weights don't sum to 1"


# ----------------------------------------------------------------------------
# Helpers
# ----------------------------------------------------------------------------
def doc_with_weights(base_doc: dict, weights: dict) -> dict:
    """Deep-copy the LNG doc and overwrite scenario weights in place."""
    d = copy.deepcopy(base_doc)
    for name, w in weights.items():
        if name in d["scenarios"]:
            d["scenarios"][name]["weight"] = w
    return d


def run_under_weights(ticker: str, ci, price: float, target: float,
                      base_doc: dict, weights: dict):
    """Run scenarios for one ticker with overridden weights."""
    doc = doc_with_weights(base_doc, weights)
    return run_scenarios(ci, price, target, doc)


def fmt_scenario_table(report) -> str:
    """Per-scenario FV table — same across weight sets since only weights
    differ; FV per scenario is a function of vessel-scale + forward curve."""
    lines = ["| Scenario | Vessel× | NAV/sh | FV (base) | Strip NPV | Assumed 12M TCE |",
             "|---|--:|--:|--:|--:|--:|"]
    for s in report.scenarios:
        lines.append(f"| {s.name} | {s.vessel_scale:.2f}× | "
                     f"${s.nav_per_share:.2f} | ${s.fair_value:.2f} | "
                     f"${s.divstrip_npv:.2f} | ${s.assumed_tce:,.0f} |")
    return "\n".join(lines)


def pw_fv(per_scenario_fvs: dict, weights: dict) -> float:
    """Probability-weighted FV given per-scenario FVs and weight dict."""
    return sum(weights[name] * per_scenario_fvs[name] for name in weights)


def position_at(ev_pct: float) -> str:
    """Short label — collapse the verbose framing in the production code."""
    if ev_pct > 5: return "BUY"
    if ev_pct < -5: return "TRIM/SHORT"
    return "HOLD"


# ----------------------------------------------------------------------------
# Threshold analysis (1-parameter shift)
# ----------------------------------------------------------------------------
def threshold_sweep(per_scenario_fvs: dict, price: float):
    """Find the minimum 1-parameter shift that flips position to HOLD then BUY.

    Parameterise as alpha ∈ [0, 1]:
      weights(alpha) = (1-alpha) × Set B + alpha × Set B-revised

    Linear in alpha. Solve analytically for the alpha at which PW FV crosses
    the HOLD threshold (FV / price = 0.95) and the BUY threshold (FV / price
    = 1.05).
    """
    # FV(alpha) = (1-alpha) × FV_B + alpha × FV_BR  (since FV is linear in weights)
    fv_b = pw_fv(per_scenario_fvs, SET_B)
    fv_br = pw_fv(per_scenario_fvs, SET_B_REVISED)
    slope = fv_br - fv_b
    intercept = fv_b

    hold_threshold = price * 0.95
    buy_threshold = price * 1.05

    def alpha_for_fv(target_fv):
        """Return (alpha_in_range, alpha_raw):
           - alpha_in_range: alpha ∈ [0, 1] crossing the threshold, else None
           - alpha_raw: the raw solve, used for extrapolation reporting
        """
        if abs(slope) < 1e-9:
            return None, None
        a = (target_fv - intercept) / slope
        return (a if 0 <= a <= 1 else None), a

    alpha_hold_in, alpha_hold_raw = alpha_for_fv(hold_threshold)
    alpha_buy_in, alpha_buy_raw = alpha_for_fv(buy_threshold)

    return {
        "fv_B": fv_b, "fv_BR": fv_br, "slope": slope,
        "alpha_HOLD": alpha_hold_in, "alpha_BUY": alpha_buy_in,
        "alpha_HOLD_raw": alpha_hold_raw, "alpha_BUY_raw": alpha_buy_raw,
        "hold_threshold": hold_threshold, "buy_threshold": buy_threshold,
    }


def interp_weights(alpha: float) -> dict:
    """Convex combination of Set B and Set B-revised at parameter alpha."""
    return {k: (1 - alpha) * SET_B[k] + alpha * SET_B_REVISED[k] for k in SET_B}


# ----------------------------------------------------------------------------
# Per-ticker run
# ----------------------------------------------------------------------------
def analyze_ticker(ticker: str, watchlist: dict, base_doc: dict) -> dict:
    entry = watchlist[ticker]
    price = entry["current_price"]
    target = entry["analyst_target"]
    ci = load_company_inputs(ticker, "2026-Q1")

    rep_b = run_under_weights(ticker, ci, price, target, base_doc, SET_B)
    rep_br = run_under_weights(ticker, ci, price, target, base_doc, SET_B_REVISED)

    # Per-scenario FV is identical across runs (only weights changed) — use
    # rep_b. Build the lookup dict for threshold analysis.
    per_scenario_fvs = {s.name: s.fair_value for s in rep_b.scenarios}

    thresh = threshold_sweep(per_scenario_fvs, price)

    return {
        "ticker": ticker, "price": price, "target": target,
        "rep_b": rep_b, "rep_br": rep_br,
        "per_scenario_fvs": per_scenario_fvs,
        "threshold": thresh,
    }


# ----------------------------------------------------------------------------
# Markdown report
# ----------------------------------------------------------------------------
def render(analyses: list[dict]) -> str:
    out = ["# LNG Weight Robustness Diagnostic — Set B vs Set B-revised",
           "",
           "**Purpose** (METHODOLOGY §13): the recurring per-LNG-name weight-",
           "sensitivity diagnostic. Identifies which calls are weight-robust",
           "(small EV% spread across plausible weight sets) vs weight-driven",
           "(call would flip under reasonable alternative weights). Refresh at",
           "the start of each quarterly cycle alongside the refresh checklist.",
           "",
           "**Current production lock:** Set B-revised (v3, 2026-06-01).",
           "Comparison reference: Set B (v2, prior lock, same day).",
           "",
           "**Lock driver:** Ras Laffan Trains 4 & 6 (12.8 mtpa / ~17% of Qatar "
           "LNG) offline through end-summer 2026 at earliest; restart risk from "
           "subsurface complications. Partially offsets Cheniere Stage 3 ramp "
           "through H2 2026. Empirical pricing: spot $67.5k (+391% YoY), TFDE "
           "$98.5k — tight-market levels, not glut levels.",
           "",
           "**Weights:**",
           "",
           "| Scenario | Set B (v2, prior) | **Set B-revised (v3, current)** | Δ |",
           "|---|--:|--:|--:|"]
    for name in SET_B:
        b = SET_B[name]
        br = SET_B_REVISED[name]
        out.append(f"| {name} | {b:.2f} | {br:.2f} | {br - b:+.2f} |")
    out.append("")

    for a in analyses:
        t = a["ticker"]
        price = a["price"]
        rep_b = a["rep_b"]
        rep_br = a["rep_br"]
        out.append(f"## {t} — at price ${price:.2f}, target ${a['target']:.2f}")
        out.append("")
        out.append("**Per-scenario FV (identical under both weight sets — "
                   "only weights change, scenario forwards unchanged):**")
        out.append("")
        out.append(fmt_scenario_table(rep_b))
        out.append("")

        # Headline comparison
        ev_b = rep_b.expected_value_vs_current / price * 100
        ev_br = rep_br.expected_value_vs_current / price * 100
        pos_b = position_at(ev_b)
        pos_br = position_at(ev_br)
        out.append("**Headline:**")
        out.append("")
        out.append("| Metric | Set B | Set B-revised | Δ |")
        out.append("|---|--:|--:|--:|")
        out.append(f"| PW FV | ${rep_b.probability_weighted_fv:.2f} | "
                   f"${rep_br.probability_weighted_fv:.2f} | "
                   f"${rep_br.probability_weighted_fv - rep_b.probability_weighted_fv:+.2f} "
                   f"({(rep_br.probability_weighted_fv / rep_b.probability_weighted_fv - 1) * 100:+.1f}%) |")
        out.append(f"| EV% | {ev_b:+.1f}% | {ev_br:+.1f}% | {ev_br - ev_b:+.1f}pp |")
        out.append(f"| Position | {pos_b} | {pos_br} | "
                   f"{'**FLIP**' if pos_b != pos_br else 'unchanged'} |")
        out.append("")

        # Threshold sweep
        t = a["threshold"]
        out.append("**Threshold analysis** "
                   "(alpha = 0: Set B; alpha = 1: Set B-revised; "
                   "FV is linear in weights so the convex combination is exact):")
        out.append("")
        out.append(f"- HOLD threshold (FV ≥ ${t['hold_threshold']:.2f}, EV ≥ -5%): "
                   + (f"alpha ≥ **{t['alpha_HOLD']:.2f}**"
                      if t['alpha_HOLD'] is not None
                      else "_not reachable on the [Set B → Set B-revised] line_"))
        out.append(f"- BUY threshold (FV ≥ ${t['buy_threshold']:.2f}, EV ≥ +5%): "
                   + (f"alpha ≥ **{t['alpha_BUY']:.2f}**"
                      if t['alpha_BUY'] is not None
                      else "_not reachable on the [Set B → Set B-revised] line_"))
        out.append("")

        # Show the interpolated weights at the HOLD threshold (if reachable)
        if t['alpha_HOLD'] is not None:
            w_at_hold = interp_weights(t['alpha_HOLD'])
            out.append(f"**Weights at the minimum HOLD threshold "
                       f"(alpha = {t['alpha_HOLD']:.2f}):**")
            out.append("")
            out.append("| Scenario | Weight at HOLD threshold | vs Set B |")
            out.append("|---|--:|--:|")
            for name in SET_B:
                out.append(f"| {name} | {w_at_hold[name]:.3f} | "
                           f"{w_at_hold[name] - SET_B[name]:+.3f} |")
            out.append("")
        elif t["alpha_HOLD_raw"] is not None and t["alpha_HOLD_raw"] > 1:
            # Set B-revised is not enough — alpha needs to extrapolate BEYOND 1.
            # (We DON'T enter this branch when alpha < 0, which means Set B is
            # already past the threshold — already at HOLD or better.)
            alpha_extr_hold = t["alpha_HOLD_raw"]
            alpha_extr_buy = t["alpha_BUY_raw"]
            out.append(f"**Set B → Set B-revised is NOT sufficient to flip "
                       f"{a['ticker']} to HOLD.** Extrapolating along the "
                       f"same direction (more aggressive constructive "
                       f"reweighting):")
            out.append("")
            out.append(f"- alpha for HOLD = **{alpha_extr_hold:.2f}** "
                       f"(must extrapolate {alpha_extr_hold - 1:.0%} beyond Set B-revised)")
            buy_str = (f"{alpha_extr_buy:.2f}" if alpha_extr_buy is not None
                       else "_(degenerate)_")
            out.append(f"- alpha for BUY = **{buy_str}**")
            out.append("")
            w_extr = interp_weights(alpha_extr_hold)
            out.append(f"**Extrapolated weights that would flip "
                       f"{a['ticker']} to HOLD (alpha = {alpha_extr_hold:.2f}):**")
            out.append("")
            out.append("| Scenario | Weight at HOLD threshold | vs Set B | vs Set B-revised |")
            out.append("|---|--:|--:|--:|")
            for name in SET_B:
                out.append(f"| {name} | {w_extr[name]:.3f} | "
                           f"{w_extr[name] - SET_B[name]:+.3f} | "
                           f"{w_extr[name] - SET_B_REVISED[name]:+.3f} |")
            out.append("")
            constructive = (w_extr["tight_resurgence"]
                            + w_extr["moderate_tightening"]
                            + w_extr["glut_base"])
            out.append(f"**Constructive total (tight + moderate + glut_base) "
                       f"at the flip point: {constructive:.0%}**")
            out.append(f"  (vs Set B: {0.10 + 0.15 + 0.55:.0%}; "
                       f"Set B-revised: {0.15 + 0.25 + 0.45:.0%}). "
                       f"Whether this is defensible depends on whether the "
                       f"Ras Laffan + winter view warrants a constructive "
                       f"environment lasting deep into 2027 with only "
                       f"{(1 - constructive):.0%} on the bear cases.")
            out.append("")
        out.append("---")
        out.append("")

    return "\n".join(out)


LNG_FRAGILITY_SETS = {
    # Post-vintage sign-stability family (S-2, 2026-07-02) — the C-4-reviewed
    # brackets: the restored v3 lock, the Jun-9 transit tilt (history bracket),
    # and the bear bracket from the proposal §15.
    "LNG Set B-revised v3 (locked, Jul-2 restore)": {
        "tight_resurgence": 0.15, "moderate_tightening": 0.25,
        "glut_base": 0.45, "glut_intensifies": 0.15, "structural_reset": 0.00,
    },
    "Jun-9 transit tilt (history bracket)": {
        "tight_resurgence": 0.25, "moderate_tightening": 0.25,
        "glut_base": 0.38, "glut_intensifies": 0.12, "structural_reset": 0.00,
    },
    "bear bracket": {
        "tight_resurgence": 0.10, "moderate_tightening": 0.20,
        "glut_base": 0.50, "glut_intensifies": 0.20, "structural_reset": 0.00,
    },
}


def write_fragility_sidecar(watchlist, base_doc):
    """EV-sign-stability across LNG_FRAGILITY_SETS -> the shared sidecar
    (scorecard W-frag + JSON weight_sign_stable). S-2 (2026-07-02): the seam
    exported null for LNG names whose diagnostics had run. No txn-anchoring
    step: LNGC/MGC carry no transaction fits (anchoring is a no-op)."""
    from crude_tanker_fv.scorecard import update_weight_fragility_sidecar

    entries = {}
    for ticker in ("FLNG", "CCEC"):
        if ticker not in watchlist:
            continue
        entry = watchlist[ticker]
        ci = load_company_inputs(ticker, "2026-Q1")
        evs, positions = [], []
        for weights in LNG_FRAGILITY_SETS.values():
            rep = run_under_weights(ticker, ci, entry["current_price"],
                                    entry["analyst_target"], base_doc, weights)
            evs.append(round(rep.expected_value_vs_current / entry["current_price"] * 100.0, 1))
            positions.append(rep.position_recommendation)
        entries[ticker] = {
            "ev_min_pct": min(evs), "ev_max_pct": max(evs),
            "ev_sign_stable": (min(evs) > 0) == (max(evs) > 0) and 0 not in (min(evs), max(evs)),
            "positions": positions,
        }
    path = update_weight_fragility_sidecar("lng", dict(LNG_FRAGILITY_SETS), entries)
    print(f"fragility sidecar (lng) -> {path}")


def main():
    watchlist = load_watchlist(live_prices=True)
    base_doc = load_scenarios(sector="lng")
    write_fragility_sidecar(watchlist, base_doc)
    analyses = []
    for t in ("FLNG", "CCEC"):
        if t in watchlist:
            analyses.append(analyze_ticker(t, watchlist, base_doc))

    report = render(analyses)
    out_path = Path(__file__).resolve().parents[1] / "outputs" / "lng_weight_robustness.md"
    out_path.write_text(report)
    print(f"→ {out_path}")
    print()
    # Also print a compact terminal summary
    for a in analyses:
        rep_b, rep_br = a["rep_b"], a["rep_br"]
        ev_b = rep_b.expected_value_vs_current / a["price"] * 100
        ev_br = rep_br.expected_value_vs_current / a["price"] * 100
        t = a["threshold"]
        alpha_h = f"{t['alpha_HOLD']:.2f}" if t['alpha_HOLD'] is not None else "—"
        alpha_b = f"{t['alpha_BUY']:.2f}" if t['alpha_BUY'] is not None else "—"
        print(f"{a['ticker']:5s}  Set B: ${rep_b.probability_weighted_fv:.2f} ({ev_b:+.1f}%, {position_at(ev_b):11s})"
              f"   Set B-rev: ${rep_br.probability_weighted_fv:.2f} ({ev_br:+.1f}%, {position_at(ev_br):11s})"
              f"   alpha_HOLD={alpha_h}  alpha_BUY={alpha_b}")


if __name__ == "__main__":
    main()
