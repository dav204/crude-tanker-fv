# SB — Scenario Fair Value (Bulk Set A (China-driven))

- **Current price:** $8.76
- **Analyst target:** $7.10
- **NAV / share (reference, unflexed):** $10.72 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $9.22 (+5.2% vs price)
- **Breakeven TCE (scenario-invariant):** $0/day — **price justified by NAV alone** (blended FV clears the price even at zero rates; the entire earnings leg is optionality on top of asset coverage).
- **Position (tool view):** BUY (undervalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| China acceleration | 20% | 1.07× | $12.01 | $11.66 | $11.56–$11.76 | 1.96× | 0.70 | $10.85 | $26,674 | n/a |
| Moderate growth (base) | 40% | 0.93× | $9.39 | $9.29 | $9.18–$9.39 | 1.49× | 0.60 | $9.13 | $20,192 | n/a |
| China property drag | 25% | 0.87× | $8.45 | $8.40 | $8.31–$8.50 | 1.30× | 0.60 | $8.32 | $17,209 | n/a |
| Coordinated slowdown | 15% | 0.79× | $6.92 | $7.15 | $7.06–$7.24 | 1.08× | 0.50 | $7.37 | $14,459 | n/a |
| **Probability-weighted** | | | | **$9.22** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven is n/a — the price clears at any rate, so every scenario's rates trivially justify it._

## Decision signals

- **Upside (best scenario − price):** $+2.90
- **Downside (worst scenario − price):** $-1.61
- **Expected value vs current** (weighted FV − price): $+0.46 (+5.2%)
- **Position:** BUY (undervalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
