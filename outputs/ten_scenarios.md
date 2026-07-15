# TEN [WHOLE-CO] — Scenario Fair Value (three-phase MoU framework)

> **Valuation basis:** WHOLE-COMPANY 3-SLEEVE = crude (72.8%) + product (15.9%) + lng (11.3%) AGGREGATED (METHODOLOGY §11.6). Off-curve shuttle-contracted-book sleeve sits at the corporate level (`shuttle_contracted_book`) and flows through NAV uniformly across scenarios. Compared to the WHOLE-COMPANY tape price.

- **Current price:** $39.75
- **Analyst target:** $51.50
- **NAV / share (reference, unflexed):** $88.76 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $57.64 (+45.0% vs price)
- **Breakeven TCE (scenario-invariant):** $0/day — **price justified by NAV alone** (blended FV clears the price even at zero rates; the entire earnings leg is optionality on top of asset coverage).
- **Position (tool view):** BUY (undervalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Escalation | 25% | 1.25× | $121.18 | $84.68 | $83.64–$85.90 | 4.40× | 0.70 | $84.35 | $147,975 | n/a |
| Pre-MoU baseline | 45% | 0.80× | $77.14 | $54.56 | $54.02–$55.15 | 1.68× | 0.70 | $56.33 | $63,874 | n/a |
| MoU base case | 18% | 0.75× | $62.10 | $45.09 | $44.63–$45.57 | 1.43× | 0.60 | $47.46 | $45,836 | n/a |
| MoU bear | 12% | 0.72× | $55.66 | $41.22 | $40.80–$41.64 | 1.20× | 0.60 | $43.92 | $37,937 | n/a |
| **Probability-weighted** | | | | **$57.64** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven is n/a — the price clears at any rate, so every scenario's rates trivially justify it._

## Decision signals

- **Upside (best scenario − price):** $+44.93
- **Downside (worst scenario − price):** $-1.03
- **Expected value vs current** (weighted FV − price): $+17.89 (+45.0%)
- **Position:** BUY (undervalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
