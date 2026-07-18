# TEN [WHOLE-CO] — Scenario Fair Value (three-phase MoU framework)

> **Valuation basis:** WHOLE-COMPANY 3-SLEEVE = crude (71.3%) + product (16.7%) + lng (11.9%) AGGREGATED (METHODOLOGY §11.6). Off-curve shuttle-contracted-book sleeve sits at the corporate level (`shuttle_contracted_book`) and flows through NAV uniformly across scenarios. Compared to the WHOLE-COMPANY tape price.

- **Current price:** $37.62
- **Analyst target:** $51.50
- **NAV / share (reference, unflexed):** $87.35 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $56.46 (+50.1% vs price)
- **Breakeven TCE (scenario-invariant):** $0/day — **price justified by NAV alone** (blended FV clears the price even at zero rates; the entire earnings leg is optionality on top of asset coverage).
- **Position (tool view):** BUY (undervalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Escalation | 25% | 1.25× | $118.12 | $81.91 | $80.93–$83.04 | 4.24× | 0.70 | $80.11 | $143,342 | n/a |
| Pre-MoU baseline | 45% | 0.80× | $76.91 | $53.74 | $53.23–$54.29 | 1.64× | 0.70 | $54.03 | $63,055 | n/a |
| MoU base case | 18% | 0.75× | $62.33 | $44.31 | $43.89–$44.75 | 1.40× | 0.60 | $45.31 | $44,830 | n/a |
| MoU bear | 12% | 0.72× | $56.19 | $41.45 | $41.02–$41.89 | 1.19× | 0.50 | $43.50 | $37,198 | n/a |
| **Probability-weighted** | | | | **$56.46** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven is n/a — the price clears at any rate, so every scenario's rates trivially justify it._

## Decision signals

- **Upside (best scenario − price):** $+44.29
- **Downside (worst scenario − price):** $+1.32
- **Expected value vs current** (weighted FV − price): $+18.84 (+50.1%)
- **Position:** BUY (undervalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
