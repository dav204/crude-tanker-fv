# INSW [WHOLE-CO] — Scenario Fair Value (three-phase MoU framework)

> **Valuation basis:** WHOLE-COMPANY = crude sleeve (65.0% of vessel value) + product sleeve (35.0%) AGGREGATED. Compared to the WHOLE-COMPANY tape price (not the crude-allocated proxy). Each sleeve is probability-weighted by its OWN sector's scenario weights (cross-sector independence; METHODOLOGY 6 v2, rank-1 pairing removed 2026-07-02).

- **Current price:** $97.05
- **Analyst target:** $79.50
- **NAV / share (reference, unflexed):** $54.64 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $59.59 (-38.6% vs price)
- **Breakeven TCE (scenario-invariant):** $518,082/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** TRIM/SHORT (overvalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Escalation | 25% | 1.25× | $68.10 | $80.41 | $76.43–$85.01 | 6.17× | 0.70 | $109.14 | $169,742 | 0.33× |
| Pre-MoU baseline | 62% | 0.95× | $57.55 | $58.85 | $56.98–$60.89 | 2.16× | 0.70 | $61.88 | $66,751 | 0.13× |
| MoU base case | 0% | 0.86× | $47.85 | $47.14 | $45.53–$48.82 | 1.78× | 0.70 | $45.85 | $48,498 | 0.09× |
| MoU bear | 13% | 0.80× | $44.24 | $42.71 | $41.03–$44.47 | 1.45× | 0.60 | $40.87 | $39,111 | 0.08× |
| **Probability-weighted** | | | | **$59.59** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $-16.64
- **Downside (worst scenario − price):** $-56.86
- **Expected value vs current** (weighted FV − price): $-37.46 (-38.6%)
- **Position:** TRIM/SHORT (overvalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_

## Hybrid sleeve breakdown (v2 whole-company aggregation)

| Sleeve | Share | Allocated price | Weighted FV | EV% | Position |
|---|--:|--:|--:|--:|---|
| Crude | 65.0% | $63.04 | $39.25 | -37.7% | TRIM/SHORT |
| Product | 35.0% | $34.01 | $20.34 | -40.2% | TRIM/SHORT |
| **WHOLE-COMPANY** | 100% | **$97.05** | **$59.59** | **-38.6%** | **TRIM/SHORT** |

_Whole-company FV = crude FV + product FV (both per shares-outstanding); compared against the whole-company tape price, not the carved proxy. The product sleeve uses CLEAN trading rates (LR1/LR2 via clean curves, MR via its own scenario forwards). The product sleeve carries MORE downside than crude because product is leading the MoU rate normalisation (MR -52% w/w, LR2 -28% w/w as of 2026-05-29) — flagged in METHODOLOGY 6 v2._
