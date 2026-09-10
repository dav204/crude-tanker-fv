# TEN [WHOLE-CO] — Scenario Fair Value (three-phase MoU framework)

> **Valuation basis:** WHOLE-COMPANY 3-SLEEVE = crude (71.6%) + product (16.5%) + lng (11.9%) AGGREGATED (METHODOLOGY §11.6). Off-curve shuttle-contracted-book sleeve sits at the corporate level (`shuttle_contracted_book`) and flows through NAV uniformly across scenarios. Compared to the WHOLE-COMPANY tape price.

- **Current price:** $44.32
- **Analyst target:** $51.50
- **NAV / share (reference, unflexed):** $88.16 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $61.80 (+39.4% vs price)
- **Breakeven TCE (scenario-invariant):** $0/day — **price justified by NAV alone** (blended FV clears the price even at zero rates; the entire earnings leg is optionality on top of asset coverage).
- **Position (tool view):** BUY (undervalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Escalation | 28% | 1.25× | $119.14 | $82.53 | $81.55–$83.66 | 4.27× | 0.70 | $80.52 | $144,175 | n/a |
| Pre-MoU baseline | 59% | 0.89× | $85.52 | $59.08 | $58.57–$59.63 | 1.65× | 0.70 | $57.76 | $63,175 | n/a |
| MoU base case | 0% | 0.83× | $71.04 | $49.56 | $49.15–$50.00 | 1.40× | 0.60 | $49.29 | $45,033 | n/a |
| MoU bear | 13% | 0.78× | $63.68 | $45.87 | $45.44–$46.31 | 1.19× | 0.50 | $47.10 | $37,347 | n/a |
| **Probability-weighted** | | | | **$61.80** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven is n/a — the price clears at any rate, so every scenario's rates trivially justify it._

## Decision signals

- **Upside (best scenario − price):** $+38.21
- **Downside (worst scenario − price):** $-1.12
- **Expected value vs current** (weighted FV − price): $+17.48 (+39.4%)
- **Position:** BUY (undervalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
