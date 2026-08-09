# INSW [WHOLE-CO] — Scenario Fair Value (three-phase MoU framework)

> **Valuation basis:** WHOLE-COMPANY = crude sleeve (66.2% of vessel value) + product sleeve (33.8%) AGGREGATED. Compared to the WHOLE-COMPANY tape price (not the crude-allocated proxy). Each sleeve is probability-weighted by its OWN sector's scenario weights (cross-sector independence; METHODOLOGY 6 v2, rank-1 pairing removed 2026-07-02).

- **Current price:** $92.41
- **Analyst target:** $79.50
- **NAV / share (reference, unflexed):** $53.88 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $55.59 (-39.8% vs price)
- **Breakeven TCE (scenario-invariant):** $380,065/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** TRIM/SHORT (overvalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Escalation | 25% | 1.25× | $67.37 | $79.30 | $75.40–$83.81 | 6.20× | 0.70 | $107.12 | $170,568 | 0.45× |
| Pre-MoU baseline | 57% | 0.82× | $51.85 | $53.51 | $51.69–$55.51 | 2.17× | 0.70 | $57.39 | $66,443 | 0.17× |
| MoU base case | 5% | 0.75× | $43.50 | $43.16 | $41.57–$44.82 | 1.78× | 0.70 | $42.76 | $48,952 | 0.13× |
| MoU bear | 13% | 0.71× | $40.46 | $39.31 | $37.66–$41.05 | 1.45× | 0.60 | $38.07 | $39,451 | 0.10× |
| **Probability-weighted** | | | | **$55.59** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $-13.11
- **Downside (worst scenario − price):** $-55.56
- **Expected value vs current** (weighted FV − price): $-36.82 (-39.8%)
- **Position:** TRIM/SHORT (overvalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_

## Hybrid sleeve breakdown (v2 whole-company aggregation)

| Sleeve | Share | Allocated price | Weighted FV | EV% | Position |
|---|--:|--:|--:|--:|---|
| Crude | 66.2% | $61.20 | $35.79 | -41.5% | TRIM/SHORT |
| Product | 33.8% | $31.21 | $19.80 | -36.6% | TRIM/SHORT |
| **WHOLE-COMPANY** | 100% | **$92.41** | **$55.59** | **-39.8%** | **TRIM/SHORT** |

_Whole-company FV = crude FV + product FV (both per shares-outstanding); compared against the whole-company tape price, not the carved proxy. The product sleeve uses CLEAN trading rates (LR1/LR2 via clean curves, MR via its own scenario forwards). The product sleeve carries MORE downside than crude because product is leading the MoU rate normalisation (MR -52% w/w, LR2 -28% w/w as of 2026-05-29) — flagged in METHODOLOGY 6 v2._
