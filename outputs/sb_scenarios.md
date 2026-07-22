# SB — Scenario Fair Value (Bulk Set A (China-driven))

- **Current price:** $7.16
- **Analyst target:** $7.10
- **NAV / share (reference, unflexed):** $10.02 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $9.47 (+32.3% vs price)
- **Breakeven TCE (scenario-invariant):** $0/day — **price justified by NAV alone** (blended FV clears the price even at zero rates; the entire earnings leg is optionality on top of asset coverage).
- **Position (tool view):** BUY (undervalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| China acceleration | 20% | 1.15× | $12.54 | $12.23 | $12.06–$12.40 | 1.96× | 0.70 | $11.50 | $26,943 | n/a |
| Moderate growth (base) | 40% | 0.99× | $9.78 | $9.58 | $9.41–$9.76 | 1.49× | 0.60 | $9.28 | $20,378 | n/a |
| China property drag | 25% | 0.92× | $8.78 | $8.53 | $8.38–$8.67 | 1.29× | 0.60 | $8.16 | $17,312 | n/a |
| Coordinated slowdown | 15% | 0.83× | $7.17 | $7.09 | $6.95–$7.23 | 1.08× | 0.50 | $7.01 | $14,562 | n/a |
| **Probability-weighted** | | | | **$9.47** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven is n/a — the price clears at any rate, so every scenario's rates trivially justify it._

## Decision signals

- **Upside (best scenario − price):** $+5.07
- **Downside (worst scenario − price):** $-0.07
- **Expected value vs current** (weighted FV − price): $+2.31 (+32.3%)
- **Position:** BUY (undervalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
