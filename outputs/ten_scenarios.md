# TEN [WHOLE-CO] — Scenario Fair Value (three-phase MoU framework)

> **Valuation basis:** WHOLE-COMPANY 3-SLEEVE = crude (71.6%) + product (16.5%) + lng (11.9%) AGGREGATED (METHODOLOGY §11.6). Off-curve shuttle-contracted-book sleeve sits at the corporate level (`shuttle_contracted_book`) and flows through NAV uniformly across scenarios. Compared to the WHOLE-COMPANY tape price.

- **Current price:** $39.14
- **Analyst target:** $51.50
- **NAV / share (reference, unflexed):** $88.16 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $57.16 (+46.0% vs price)
- **Breakeven TCE (scenario-invariant):** $0/day — **price justified by NAV alone** (blended FV clears the price even at zero rates; the entire earnings leg is optionality on top of asset coverage).
- **Position (tool view):** BUY (undervalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Escalation | 25% | 1.25× | $119.14 | $82.53 | $81.55–$83.66 | 4.27× | 0.70 | $80.52 | $144,175 | n/a |
| Pre-MoU baseline | 57% | 0.80× | $77.52 | $54.10 | $53.60–$54.66 | 1.65× | 0.70 | $54.25 | $63,175 | n/a |
| MoU base case | 5% | 0.75× | $62.94 | $44.67 | $44.25–$45.10 | 1.40× | 0.60 | $45.56 | $45,033 | n/a |
| MoU bear | 13% | 0.72× | $56.75 | $41.77 | $41.34–$42.21 | 1.19× | 0.50 | $43.74 | $37,347 | n/a |
| **Probability-weighted** | | | | **$57.16** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven is n/a — the price clears at any rate, so every scenario's rates trivially justify it._

## Decision signals

- **Upside (best scenario − price):** $+43.39
- **Downside (worst scenario − price):** $+0.13
- **Expected value vs current** (weighted FV − price): $+18.02 (+46.0%)
- **Position:** BUY (undervalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
