# TEN [WHOLE-CO] — Scenario Fair Value (three-phase MoU framework)

> **Valuation basis:** WHOLE-COMPANY 3-SLEEVE = crude (71.4%) + product (16.6%) + lng (11.9%) AGGREGATED (METHODOLOGY §11.6). Off-curve shuttle-contracted-book sleeve sits at the corporate level (`shuttle_contracted_book`) and flows through NAV uniformly across scenarios. Compared to the WHOLE-COMPANY tape price.

- **Current price:** $39.14
- **Analyst target:** $51.50
- **NAV / share (reference, unflexed):** $87.57 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $56.83 (+45.2% vs price)
- **Breakeven TCE (scenario-invariant):** $0/day — **price justified by NAV alone** (blended FV clears the price even at zero rates; the entire earnings leg is optionality on top of asset coverage).
- **Position (tool view):** BUY (undervalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Escalation | 25% | 1.25× | $118.40 | $82.07 | $81.09–$83.20 | 4.24× | 0.70 | $80.17 | $143,164 | n/a |
| Pre-MoU baseline | 57% | 0.80× | $77.07 | $53.82 | $53.31–$54.37 | 1.64× | 0.70 | $54.05 | $62,971 | n/a |
| MoU base case | 5% | 0.75× | $62.51 | $44.40 | $43.98–$44.83 | 1.40× | 0.60 | $45.35 | $44,812 | n/a |
| MoU bear | 13% | 0.72× | $56.35 | $41.52 | $41.10–$41.96 | 1.19× | 0.50 | $43.53 | $37,191 | n/a |
| **Probability-weighted** | | | | **$56.83** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven is n/a — the price clears at any rate, so every scenario's rates trivially justify it._

## Decision signals

- **Upside (best scenario − price):** $+42.93
- **Downside (worst scenario − price):** $-0.12
- **Expected value vs current** (weighted FV − price): $+17.69 (+45.2%)
- **Position:** BUY (undervalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
