# SB — Scenario Fair Value (Bulk Set A (China-driven))

- **Current price:** $6.90
- **Analyst target:** $7.10
- **NAV / share (reference, unflexed):** $10.12 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $9.82 (+42.3% vs price)
- **Breakeven TCE (scenario-invariant):** $0/day — **price justified by NAV alone** (blended FV clears the price even at zero rates; the entire earnings leg is optionality on top of asset coverage).
- **Position (tool view):** BUY (undervalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| China acceleration | 20% | 1.18× | $13.05 | $12.69 | $12.51–$12.86 | 1.96× | 0.70 | $11.84 | $26,868 | n/a |
| Moderate growth (base) | 40% | 1.00× | $10.17 | $9.93 | $9.76–$10.10 | 1.49× | 0.60 | $9.56 | $20,326 | n/a |
| China property drag | 25% | 0.94× | $9.13 | $8.84 | $8.70–$8.99 | 1.29× | 0.60 | $8.41 | $17,283 | n/a |
| Coordinated slowdown | 15% | 0.84× | $7.45 | $7.34 | $7.19–$7.48 | 1.08× | 0.50 | $7.22 | $14,533 | n/a |
| **Probability-weighted** | | | | **$9.82** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven is n/a — the price clears at any rate, so every scenario's rates trivially justify it._

## Decision signals

- **Upside (best scenario − price):** $+5.79
- **Downside (worst scenario − price):** $+0.44
- **Expected value vs current** (weighted FV − price): $+2.92 (+42.3%)
- **Position:** BUY (undervalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
