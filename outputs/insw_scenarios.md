# INSW [WHOLE-CO] — Scenario Fair Value (three-phase MoU framework)

> **Valuation basis:** WHOLE-COMPANY = crude sleeve (65.3% of vessel value) + product sleeve (34.7%) AGGREGATED. Compared to the WHOLE-COMPANY tape price (not the crude-allocated proxy). Per-sleeve FVs flow through the same scenario set (METHODOLOGY 6 v2).

- **Current price:** $78.00
- **Analyst target:** $79.50
- **NAV / share (reference, unflexed):** $52.43 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $59.50 (-23.7% vs price)
- **Breakeven TCE (scenario-invariant):** $341,877/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** TRIM/SHORT (overvalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Escalation | 25% | 1.25× | $65.55 | $74.14 | $71.30–$77.42 | 6.12× | 0.70 | $94.17 | $166,739 | 0.49× |
| Pre-MoU baseline | 45% | 1.09× | $60.19 | $64.00 | $62.24–$65.98 | 3.78× | 0.70 | $72.89 | $102,038 | 0.30× |
| MoU base case | 18% | 0.75× | $42.42 | $42.12 | $40.97–$43.33 | 1.77× | 0.70 | $41.82 | $48,109 | 0.14× |
| MoU bear | 12% | 0.71× | $39.44 | $38.18 | $36.98–$39.44 | 1.45× | 0.60 | $36.77 | $38,839 | 0.11× |
| **Probability-weighted** | | | | **$59.50** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $-3.86
- **Downside (worst scenario − price):** $-39.82
- **Expected value vs current** (weighted FV − price): $-18.50 (-23.7%)
- **Position:** TRIM/SHORT (overvalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_

## Hybrid sleeve breakdown (v2 whole-company aggregation)

| Sleeve | Share | Allocated price | Weighted FV | EV% | Position |
|---|--:|--:|--:|--:|---|
| Crude | 65.3% | $50.95 | $38.84 | -23.8% | TRIM/SHORT |
| Product | 34.7% | $27.05 | $19.54 | -27.8% | TRIM/SHORT |
| **WHOLE-COMPANY** | 100% | **$78.00** | **$59.50** | **-23.7%** | **TRIM/SHORT** |

_Whole-company FV = crude FV + product FV (both per shares-outstanding); compared against the whole-company tape price, not the carved proxy. The product sleeve uses CLEAN trading rates (LR1/LR2 via clean curves, MR via its own scenario forwards). The product sleeve carries MORE downside than crude because product is leading the MoU rate normalisation (MR -52% w/w, LR2 -28% w/w as of 2026-05-29) — flagged in METHODOLOGY 6 v2._
