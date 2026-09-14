# SB — Scenario Fair Value (Bulk Set A (China-driven))

- **Current price:** $8.51
- **Analyst target:** $7.10
- **NAV / share (reference, unflexed):** $10.72 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $8.95 (+5.2% vs price)
- **Breakeven TCE (scenario-invariant):** $0/day — **price justified by NAV alone** (blended FV clears the price even at zero rates; the entire earnings leg is optionality on top of asset coverage).
- **Position (tool view):** BUY (undervalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| China acceleration | 20% | 1.05× | $11.60 | $11.30 | $11.19–$11.40 | 1.96× | 0.70 | $10.58 | $26,674 | n/a |
| Moderate growth (base) | 40% | 0.91× | $9.09 | $9.02 | $8.92–$9.12 | 1.49× | 0.60 | $8.92 | $20,192 | n/a |
| China property drag | 25% | 0.86× | $8.19 | $8.17 | $8.07–$8.26 | 1.30× | 0.60 | $8.14 | $17,209 | n/a |
| Coordinated slowdown | 15% | 0.77× | $6.71 | $6.97 | $6.88–$7.06 | 1.08× | 0.50 | $7.22 | $14,459 | n/a |
| **Probability-weighted** | | | | **$8.95** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven is n/a — the price clears at any rate, so every scenario's rates trivially justify it._

## Decision signals

- **Upside (best scenario − price):** $+2.79
- **Downside (worst scenario − price):** $-1.54
- **Expected value vs current** (weighted FV − price): $+0.44 (+5.2%)
- **Position:** BUY (undervalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
