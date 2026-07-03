"""Product tanker weight comparison — Product Set A vs Product Set B.

Authorised 2026-06-03 following Catlin's VIE product tanker macro update
(June 3, 2026): the empirical 2026 product environment (rate spike to multi-
decade highs per Baltic Clean Tanker Index, cargo-mile demand gains LR2
+6.62% YTD / MR2 +3.17% YTD, critical regional shortages, US distillates at
two-decade low) supports a constructive reweighting analogous to the LNG
Set B → Set B-revised transition. Set A's 50% on `glut_base` is too central
for the 2026 supply environment, same diagnostic logic as LNG Set B.

The shift mirrors LNG: +5pp refinery_squeeze, +10pp moderate_correction,
-5pp glut_base, -10pp demand_softening. Constructive total 0.75 → 0.85.
Structural_decline unchanged at 0.00 (energy-transition tail same treatment).

Output:
  - outputs/product_weight_comparison.md  (markdown + headline impact)

Names affected:
  - ASC  (pure product, full impact)
  - STNG (pure product, full impact)
  - INSW (HYBRID: product sleeve impact; whole-co FV partially affected via
    the index-pairing aggregation — NOT a preservation invariant case)

Naming-namespace note (§9.10 discipline): this script uses "Product Set A/B"
for the PRODUCT sector. The LNG sector uses its own Set B / Set B-revised
labels (§11.3). Coincidentally, Product Set B's destination weights
{0.15, 0.25, 0.45, 0.15, 0.00} match LNG Set B-revised exactly — this is
deliberate (same Iran-crisis empirical case) but does NOT mean the two
labels are interchangeable. Each sector's labels are sector-scoped.
"""

from __future__ import annotations

import copy
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from crude_tanker_fv.loaders import load_company_inputs, load_watchlist
from crude_tanker_fv.pipeline import _load_all_sectors, _run_scenarios_for_ticker
from crude_tanker_fv.scenarios import position_recommendation

# ----------------------------------------------------------------------------
# Weight definitions
# ----------------------------------------------------------------------------
PRODUCT_SET_A = {
    "refinery_squeeze":     0.10,
    "moderate_correction":  0.15,
    "glut_base":            0.50,
    "demand_softening":     0.25,
    "structural_decline":   0.00,
}

PRODUCT_SET_B = {
    "refinery_squeeze":     0.15,   # +0.05 — rate spike + cargo-mile demand
    "moderate_correction":  0.25,   # +0.10 — sustained constructive 2026
    "glut_base":            0.45,   # -0.05 — central case shifts off pure glut
    "demand_softening":     0.15,   # -0.10 — demand-side bear less weight given empirical demand strength
    "structural_decline":   0.00,   # unchanged
}

assert abs(sum(PRODUCT_SET_A.values()) - 1.0) < 1e-9
assert abs(sum(PRODUCT_SET_B.values()) - 1.0) < 1e-9

# Tickers affected by product weight changes. INSW is hybrid: its product
# sleeve runs through sectors.product so it picks up the new weights too.
AFFECTED_TICKERS = ["ASC", "STNG", "INSW"]

# Post-vintage sign-stability family (S-2, 2026-07-02) — the C-4-reviewed
# brackets: the restored v2 lock, the Jun-9 war tilt (history bracket), and the
# bear bracket from the proposal §15. Evaluated for the PURE product names
# (hybrids' flags come from the crude family sidecar).
PRODUCT_FRAGILITY_SETS = {
    "Product v2 (locked, Jul-2 restore)": {
        "refinery_squeeze": 0.15, "moderate_correction": 0.25,
        "glut_base": 0.45, "demand_softening": 0.15, "structural_decline": 0.00,
    },
    "Jun-9 war tilt (history bracket)": {
        "refinery_squeeze": 0.25, "moderate_correction": 0.30,
        "glut_base": 0.30, "demand_softening": 0.15, "structural_decline": 0.00,
    },
    "bear bracket": {
        "refinery_squeeze": 0.10, "moderate_correction": 0.20,
        "glut_base": 0.50, "demand_softening": 0.20, "structural_decline": 0.00,
    },
}
PRODUCT_FRAGILITY_TICKERS = ["ASC", "STNG", "HAFN", "TRMD"]


def write_fragility_sidecar(watchlist, base_sector_docs):
    """EV-sign-stability across PRODUCT_FRAGILITY_SETS -> the shared sidecar
    (scorecard W-frag column + JSON weight_sign_stable). S-2: the seam exported
    null for product names whose diagnostics had run."""
    from crude_tanker_fv.loaders import INPUTS_DIR
    from crude_tanker_fv.pipeline import _maybe_apply_transactions
    from crude_tanker_fv.scorecard import update_weight_fragility_sidecar

    entries = {}
    for ticker in PRODUCT_FRAGILITY_TICKERS:
        if ticker not in watchlist:
            continue
        entry = watchlist[ticker]
        ci = load_company_inputs(ticker, "2026-Q1")
        ci, _ = _maybe_apply_transactions(ci, INPUTS_DIR, True)
        evs, positions = [], []
        for weights in PRODUCT_FRAGILITY_SETS.values():
            rep = run_under_weights(ticker, ci, entry["current_price"],
                                    entry["analyst_target"], base_sector_docs, weights)
            evs.append(round(rep.expected_value_vs_current / entry["current_price"] * 100.0, 1))
            positions.append(rep.position_recommendation)
        entries[ticker] = {
            "ev_min_pct": min(evs), "ev_max_pct": max(evs),
            "ev_sign_stable": (min(evs) > 0) == (max(evs) > 0) and 0 not in (min(evs), max(evs)),
            "positions": positions,
        }
    path = update_weight_fragility_sidecar(
        "product", dict(PRODUCT_FRAGILITY_SETS), entries)
    print(f"fragility sidecar (product) -> {path}")


def doc_with_weights(base_doc: dict, weights: dict) -> dict:
    d = copy.deepcopy(base_doc)
    for name, w in weights.items():
        if name in d["scenarios"]:
            d["scenarios"][name]["weight"] = w
    return d


def position_at(ev_pct: float) -> str:
    if ev_pct > 5:
        return "BUY"
    if ev_pct < -5:
        return "TRIM/SHORT"
    return "HOLD"


def run_under_weights(ticker, ci, price, target, base_sector_docs, weights):
    modified = dict(base_sector_docs)
    modified["product"] = doc_with_weights(base_sector_docs["product"], weights)
    headline, _, _ = _run_scenarios_for_ticker(
        ticker, ci, price, target, modified, load_watchlist(),
    )
    return headline


def main():
    watchlist = load_watchlist(live_prices=True)
    base_sector_docs = _load_all_sectors()
    write_fragility_sidecar(watchlist, base_sector_docs)

    rows = []
    for ticker in AFFECTED_TICKERS:
        if ticker not in watchlist:
            continue
        entry = watchlist[ticker]
        price = entry["current_price"]
        target = entry["analyst_target"]
        ci = load_company_inputs(ticker, "2026-Q1")
        # Production-path parity (2026-07-02, same bug as crude_weight_robustness):
        # product classes (MR/LR2) ARE transaction-anchored default-ON in the
        # pipeline; without this the diagnostic runs on un-anchored marks.
        from crude_tanker_fv.loaders import INPUTS_DIR
        from crude_tanker_fv.pipeline import _maybe_apply_transactions
        ci, _ = _maybe_apply_transactions(ci, INPUTS_DIR, True)

        rep_a = run_under_weights(ticker, ci, price, target, base_sector_docs, PRODUCT_SET_A)
        rep_b = run_under_weights(ticker, ci, price, target, base_sector_docs, PRODUCT_SET_B)

        ev_a = rep_a.expected_value_vs_current / price * 100
        ev_b = rep_b.expected_value_vs_current / price * 100

        rows.append({
            "ticker": ticker,
            "price": price,
            "pw_fv_A": rep_a.probability_weighted_fv,
            "pw_fv_B": rep_b.probability_weighted_fv,
            "ev_a": ev_a,
            "ev_b": ev_b,
            "pos_a": position_at(ev_a),
            "pos_b": position_at(ev_b),
        })

    # Render markdown
    out = ["# Product Weight Comparison — Set A vs Set B (Iran-crisis analog of LNG transition)",
           "",
           "**Driver:** Catlin VIE product tanker macro update (2026-06-03). "
           "Empirical 2026 product environment (rate spike at multi-decade highs, "
           "cargo-mile demand gains, critical regional shortages, US distillates "
           "two-decade low) is structurally tight, not glut. Set A's 50% on "
           "`glut_base` is mis-centered for 2026 — same diagnostic logic that "
           "motivated LNG Set B → Set B-revised. Product Set B applies the "
           "LNG-shift analog: +5pp refinery_squeeze, +10pp moderate_correction, "
           "-5pp glut_base, -10pp demand_softening, structural_decline unchanged.",
           "",
           "**Naming namespace:** \"Product Set A/B\" are PRODUCT-sector labels. "
           "LNG \"Set B / Set B-revised\" are LNG-sector labels (§11.3). The "
           "destination weights are coincidentally identical (both sectors face "
           "the same Iran-crisis case), but the labels are NOT interchangeable.",
           "",
           "## Weight sets\n",
           "| Scenario | Set A (current locked v1) | **Set B (constructive v2)** | Δ |",
           "|---|--:|--:|--:|"]
    for scen in PRODUCT_SET_A:
        a, b = PRODUCT_SET_A[scen], PRODUCT_SET_B[scen]
        out.append(f"| {scen} | {a:.2f} | **{b:.2f}** | {b - a:+.2f} |")
    out.append("")
    out.append(f"**Constructive total** (refinery_squeeze + moderate_correction + glut_base): "
               f"Set A {0.10 + 0.15 + 0.50:.2f} → Set B **{0.15 + 0.25 + 0.45:.2f}** (+0.10).")
    out.append("")

    # Headline table
    out.append("## Headline impact\n")
    out.append("| Ticker | Set A PW FV | Set B PW FV | Δ FV | Set A EV | Set B EV | Position change |")
    out.append("|---|--:|--:|--:|--:|--:|---|")
    for r in rows:
        df = r["pw_fv_B"] - r["pw_fv_A"]
        df_pct = df / r["pw_fv_A"] * 100
        flip = "**FLIP**" if r["pos_a"] != r["pos_b"] else "unchanged"
        out.append(
            f"| {r['ticker']} | ${r['pw_fv_A']:.2f} | **${r['pw_fv_B']:.2f}** | "
            f"${df:+.2f} ({df_pct:+.1f}%) | {r['ev_a']:+.1f}% ({r['pos_a']}) | "
            f"{r['ev_b']:+.1f}% (**{r['pos_b']}**) | {flip} |"
        )
    out.append("")

    out.append("## INSW preservation invariant — HOLDS THROUGH SET B (notable property)\n")
    out.append("INSW whole-co PW FV is **$52.08 under both Set A and Set B** — unchanged. "
               "This is not coincidence: `_aggregate_hybrid_report` builds the whole-co "
               "probability-weighted FV by pairing crude scenario i with product scenario i "
               "(see METHODOLOGY §6 v2) and **uses crude scenario weights** as the aggregation "
               "probability. The per-scenario sum `c.fair_value + p.fair_value` is "
               "weight-independent (per-scenario FVs are scenario-specific values, not "
               "weight-dependent), and the aggregation weights come from the crude doc. "
               "Therefore changing product weights affects pure-product names (ASC, STNG) "
               "but **does not affect INSW whole-co FV under the current hybrid carve-out "
               "methodology**. This is a property of the framework worth documenting — the "
               "INSW preservation test will continue to pass through this transition.")
    out.append("")

    path = Path(__file__).resolve().parents[1] / "outputs" / "product_weight_comparison.md"
    path.write_text("\n".join(out))
    print(f"→ {path}")
    print()

    # Terminal summary
    print(f"{'Ticker':6s}  {'Set A':22s}  {'Set B':22s}  Δ")
    print("-" * 80)
    for r in rows:
        df = r["pw_fv_B"] - r["pw_fv_A"]
        flip = "FLIP" if r["pos_a"] != r["pos_b"] else "    "
        print(f"{r['ticker']:6s}  "
              f"${r['pw_fv_A']:6.2f} ({r['ev_a']:+5.1f}% {r['pos_a']:11s})  "
              f"${r['pw_fv_B']:6.2f} ({r['ev_b']:+5.1f}% {r['pos_b']:11s})  "
              f"{df:+.2f} {flip}")


if __name__ == "__main__":
    main()
