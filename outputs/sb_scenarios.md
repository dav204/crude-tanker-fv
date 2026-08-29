# SB — Scenario Fair Value (Bulk Set A (China-driven))

- **Current price:** $6.39
- **Analyst target:** $7.10
- **NAV / share (reference, unflexed):** $10.58 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $9.53 (+49.2% vs price)
- **Breakeven TCE (scenario-invariant):** $0/day — **price justified by NAV alone** (blended FV clears the price even at zero rates; the entire earnings leg is optionality on top of asset coverage).
- **Position (tool view):** BUY (undervalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| China acceleration | 20% | 1.11× | $12.54 | $12.13 | $12.02–$12.23 | 1.96× | 0.70 | $11.16 | $26,700 | n/a |
| Moderate growth (base) | 40% | 0.95× | $9.77 | $9.60 | $9.50–$9.71 | 1.49× | 0.60 | $9.36 | $20,209 | n/a |
| China property drag | 25% | 0.90× | $8.77 | $8.67 | $8.57–$8.76 | 1.30× | 0.60 | $8.51 | $17,219 | n/a |
| Coordinated slowdown | 15% | 0.81× | $7.15 | $7.33 | $7.24–$7.42 | 1.08× | 0.50 | $7.51 | $14,469 | n/a |
| **Probability-weighted** | | | | **$9.53** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven is n/a — the price clears at any rate, so every scenario's rates trivially justify it._

## Decision signals

- **Upside (best scenario − price):** $+5.74
- **Downside (worst scenario − price):** $+0.94
- **Expected value vs current** (weighted FV − price): $+3.14 (+49.2%)
- **Position:** BUY (undervalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
