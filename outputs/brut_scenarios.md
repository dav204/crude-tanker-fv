# BRUT — Scenario Fair Value (three-phase MoU framework)

- **Current price:** $5.72
- **Analyst target:** $7.13
- **NAV / share (reference, unflexed):** $8.80 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $6.21 (+8.4% vs price)
- **Breakeven TCE (scenario-invariant):** $0/day — **price justified by NAV alone** (blended FV clears the price even at zero rates; the entire earnings leg is optionality on top of asset coverage).
- **Position (tool view):** BUY (undervalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Escalation | 25% | 1.25× | $16.28 | $17.18 | $16.85–$17.55 | 8.44× | 0.70 | $19.28 | $337,500 | n/a |
| Pre-MoU baseline | 45% | 0.82× | $3.29 | $3.65 | $3.53–$3.77 | 2.65× | 0.70 | $4.49 | $106,100 | n/a |
| MoU base case | 18% | 0.74× | $1.13 | $1.46 | $1.36–$1.55 | 2.12× | 0.70 | $2.22 | $84,875 | n/a |
| MoU bear | 12% | 0.70× | $-0.27 | $0.07 | $-0.01–$0.15 | 1.63× | 0.70 | $0.86 | $65,250 | n/a |
| **Probability-weighted** | | | | **$6.21** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven is n/a — the price clears at any rate, so every scenario's rates trivially justify it._

## Decision signals

- **Upside (best scenario − price):** $+11.45
- **Downside (worst scenario − price):** $-5.65
- **Expected value vs current** (weighted FV − price): $+0.48 (+8.4%)
- **Position:** BUY (undervalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
