# BRUT — Scenario Fair Value (three-phase MoU framework)

- **Current price:** $6.74
- **Analyst target:** $7.13
- **NAV / share (reference, unflexed):** $9.62 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $10.28 (+52.5% vs price)
- **Breakeven TCE (scenario-invariant):** $0/day — **price justified by NAV alone** (blended FV clears the price even at zero rates; the entire earnings leg is optionality on top of asset coverage).
- **Position (tool view):** BUY (undervalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Escalation | 25% | 1.25× | $17.12 | $18.11 | $17.76–$18.51 | 8.44× | 0.70 | $20.41 | $337,500 | n/a |
| Pre-MoU baseline | 62% | 0.96× | $8.47 | $8.57 | $8.45–$8.70 | 2.65× | 0.70 | $8.81 | $106,100 | n/a |
| MoU base case | 0% | 0.86× | $5.31 | $5.42 | $5.32–$5.51 | 2.12× | 0.70 | $5.68 | $84,875 | n/a |
| MoU bear | 13% | 0.79× | $3.26 | $3.42 | $3.33–$3.50 | 1.63× | 0.70 | $3.78 | $65,250 | n/a |
| **Probability-weighted** | | | | **$10.28** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven is n/a — the price clears at any rate, so every scenario's rates trivially justify it._

## Decision signals

- **Upside (best scenario − price):** $+11.36
- **Downside (worst scenario − price):** $-3.33
- **Expected value vs current** (weighted FV − price): $+3.54 (+52.5%)
- **Position:** BUY (undervalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
