# BRUT — Scenario Fair Value (three-phase MoU framework)

- **Current price:** $6.41
- **Analyst target:** $7.13
- **NAV / share (reference, unflexed):** $8.80 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $9.33 (+45.6% vs price)
- **Breakeven TCE (scenario-invariant):** $0/day — **price justified by NAV alone** (blended FV clears the price even at zero rates; the entire earnings leg is optionality on top of asset coverage).
- **Position (tool view):** BUY (undervalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Escalation | 25% | 1.25× | $16.28 | $17.23 | $16.90–$17.60 | 8.44× | 0.70 | $19.44 | $337,500 | n/a |
| Pre-MoU baseline | 57% | 0.96× | $7.65 | $7.80 | $7.68–$7.92 | 2.65× | 0.70 | $8.15 | $106,100 | n/a |
| MoU base case | 5% | 0.86× | $4.49 | $4.66 | $4.57–$4.75 | 2.12× | 0.70 | $5.06 | $84,875 | n/a |
| MoU bear | 13% | 0.79× | $2.45 | $2.67 | $2.59–$2.75 | 1.63× | 0.70 | $3.17 | $65,250 | n/a |
| **Probability-weighted** | | | | **$9.33** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven is n/a — the price clears at any rate, so every scenario's rates trivially justify it._

## Decision signals

- **Upside (best scenario − price):** $+10.82
- **Downside (worst scenario − price):** $-3.74
- **Expected value vs current** (weighted FV − price): $+2.92 (+45.6%)
- **Position:** BUY (undervalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
