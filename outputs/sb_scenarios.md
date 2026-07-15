# SB — Scenario Fair Value (Bulk Set A (China-driven))

- **Current price:** $7.13
- **Analyst target:** $7.10
- **NAV / share (reference, unflexed):** $10.12 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $9.56 (+34.1% vs price)
- **Breakeven TCE (scenario-invariant):** $0/day — **price justified by NAV alone** (blended FV clears the price even at zero rates; the entire earnings leg is optionality on top of asset coverage).
- **Position (tool view):** BUY (undervalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| China acceleration | 20% | 1.15× | $12.65 | $12.33 | $12.16–$12.51 | 1.96× | 0.70 | $11.58 | $26,868 | n/a |
| Moderate growth (base) | 40% | 0.99× | $9.88 | $9.67 | $9.50–$9.84 | 1.49× | 0.60 | $9.36 | $20,326 | n/a |
| China property drag | 25% | 0.92× | $8.87 | $8.62 | $8.47–$8.76 | 1.29× | 0.60 | $8.23 | $17,283 | n/a |
| Coordinated slowdown | 15% | 0.83× | $7.25 | $7.17 | $7.02–$7.31 | 1.08× | 0.50 | $7.08 | $14,533 | n/a |
| **Probability-weighted** | | | | **$9.56** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven is n/a — the price clears at any rate, so every scenario's rates trivially justify it._

## Decision signals

- **Upside (best scenario − price):** $+5.20
- **Downside (worst scenario − price):** $+0.04
- **Expected value vs current** (weighted FV − price): $+2.43 (+34.1%)
- **Position:** BUY (undervalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
