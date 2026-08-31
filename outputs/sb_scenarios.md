# SB — Scenario Fair Value (Bulk Set A (China-driven))

- **Current price:** $8.52
- **Analyst target:** $7.10
- **NAV / share (reference, unflexed):** $10.65 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $9.23 (+8.4% vs price)
- **Breakeven TCE (scenario-invariant):** $0/day — **price justified by NAV alone** (blended FV clears the price even at zero rates; the entire earnings leg is optionality on top of asset coverage).
- **Position (tool view):** BUY (undervalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| China acceleration | 20% | 1.08× | $12.05 | $11.70 | $11.59–$11.80 | 1.96× | 0.70 | $10.87 | $26,686 | n/a |
| Moderate growth (base) | 40% | 0.93× | $9.41 | $9.30 | $9.20–$9.41 | 1.49× | 0.60 | $9.13 | $20,200 | n/a |
| China property drag | 25% | 0.88× | $8.47 | $8.41 | $8.32–$8.51 | 1.30× | 0.60 | $8.32 | $17,214 | n/a |
| Coordinated slowdown | 15% | 0.79× | $6.92 | $7.14 | $7.06–$7.23 | 1.08× | 0.50 | $7.37 | $14,464 | n/a |
| **Probability-weighted** | | | | **$9.23** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven is n/a — the price clears at any rate, so every scenario's rates trivially justify it._

## Decision signals

- **Upside (best scenario − price):** $+3.18
- **Downside (worst scenario − price):** $-1.38
- **Expected value vs current** (weighted FV − price): $+0.71 (+8.4%)
- **Position:** BUY (undervalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
