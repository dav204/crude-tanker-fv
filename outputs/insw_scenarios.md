# INSW [WHOLE-CO] — Scenario Fair Value (three-phase MoU framework)

> **Valuation basis:** WHOLE-COMPANY = crude sleeve (65.0% of vessel value) + product sleeve (35.0%) AGGREGATED. Compared to the WHOLE-COMPANY tape price (not the crude-allocated proxy). Each sleeve is probability-weighted by its OWN sector's scenario weights (cross-sector independence; METHODOLOGY 6 v2, rank-1 pairing removed 2026-07-02).

- **Current price:** $103.65
- **Analyst target:** $79.50
- **NAV / share (reference, unflexed):** $54.64 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $59.91 (-42.2% vs price)
- **Breakeven TCE (scenario-invariant):** $560,027/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** TRIM/SHORT (overvalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Escalation | 28% | 1.25× | $68.10 | $80.41 | $76.43–$85.01 | 6.17× | 0.70 | $109.14 | $169,742 | 0.30× |
| Pre-MoU baseline | 59% | 0.93× | $57.03 | $58.39 | $56.53–$60.44 | 2.16× | 0.70 | $61.56 | $66,751 | 0.12× |
| MoU base case | 0% | 0.85× | $47.58 | $46.90 | $45.29–$48.58 | 1.78× | 0.70 | $45.69 | $48,498 | 0.09× |
| MoU bear | 13% | 0.79× | $44.01 | $42.51 | $40.83–$44.27 | 1.45× | 0.60 | $40.72 | $39,111 | 0.07× |
| **Probability-weighted** | | | | **$59.91** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $-23.24
- **Downside (worst scenario − price):** $-63.69
- **Expected value vs current** (weighted FV − price): $-43.74 (-42.2%)
- **Position:** TRIM/SHORT (overvalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_

## Hybrid sleeve breakdown (v2 whole-company aggregation)

| Sleeve | Share | Allocated price | Weighted FV | EV% | Position |
|---|--:|--:|--:|--:|---|
| Crude | 65.0% | $67.33 | $39.53 | -41.3% | TRIM/SHORT |
| Product | 35.0% | $36.32 | $20.39 | -43.9% | TRIM/SHORT |
| **WHOLE-COMPANY** | 100% | **$103.65** | **$59.91** | **-42.2%** | **TRIM/SHORT** |

_Whole-company FV = crude FV + product FV (both per shares-outstanding); compared against the whole-company tape price, not the carved proxy. The product sleeve uses CLEAN trading rates (LR1/LR2 via clean curves, MR via its own scenario forwards). The product sleeve carries MORE downside than crude because product is leading the MoU rate normalisation (MR -52% w/w, LR2 -28% w/w as of 2026-05-29) — flagged in METHODOLOGY 6 v2._
