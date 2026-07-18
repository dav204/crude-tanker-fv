# SB — Scenario Fair Value (Bulk Set A (China-driven))

- **Current price:** $6.82
- **Analyst target:** $7.10
- **NAV / share (reference, unflexed):** $10.17 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $9.60 (+40.8% vs price)
- **Breakeven TCE (scenario-invariant):** $0/day — **price justified by NAV alone** (blended FV clears the price even at zero rates; the entire earnings leg is optionality on top of asset coverage).
- **Position (tool view):** BUY (undervalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| China acceleration | 20% | 1.15× | $12.71 | $12.38 | $12.21–$12.55 | 1.96× | 0.70 | $11.60 | $26,913 | n/a |
| Moderate growth (base) | 40% | 0.99× | $9.93 | $9.71 | $9.54–$9.88 | 1.49× | 0.60 | $9.38 | $20,356 | n/a |
| China property drag | 25% | 0.92× | $8.91 | $8.65 | $8.50–$8.79 | 1.29× | 0.60 | $8.25 | $17,300 | n/a |
| Coordinated slowdown | 15% | 0.83× | $7.29 | $7.19 | $7.05–$7.34 | 1.08× | 0.50 | $7.09 | $14,550 | n/a |
| **Probability-weighted** | | | | **$9.60** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven is n/a — the price clears at any rate, so every scenario's rates trivially justify it._

## Decision signals

- **Upside (best scenario − price):** $+5.56
- **Downside (worst scenario − price):** $+0.37
- **Expected value vs current** (weighted FV − price): $+2.78 (+40.8%)
- **Position:** BUY (undervalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
