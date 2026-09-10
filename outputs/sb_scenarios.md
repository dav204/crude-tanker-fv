# SB — Scenario Fair Value (Bulk Set A (China-driven))

- **Current price:** $8.36
- **Analyst target:** $7.10
- **NAV / share (reference, unflexed):** $10.72 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $9.07 (+8.5% vs price)
- **Breakeven TCE (scenario-invariant):** $0/day — **price justified by NAV alone** (blended FV clears the price even at zero rates; the entire earnings leg is optionality on top of asset coverage).
- **Position (tool view):** BUY (undervalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| China acceleration | 20% | 1.06× | $11.78 | $11.46 | $11.35–$11.56 | 1.96× | 0.70 | $10.70 | $26,674 | n/a |
| Moderate growth (base) | 40% | 0.92× | $9.22 | $9.14 | $9.03–$9.24 | 1.49× | 0.60 | $9.01 | $20,192 | n/a |
| China property drag | 25% | 0.86× | $8.31 | $8.27 | $8.18–$8.37 | 1.30× | 0.60 | $8.22 | $17,209 | n/a |
| Coordinated slowdown | 15% | 0.78× | $6.80 | $7.05 | $6.96–$7.14 | 1.08× | 0.50 | $7.29 | $14,459 | n/a |
| **Probability-weighted** | | | | **$9.07** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven is n/a — the price clears at any rate, so every scenario's rates trivially justify it._

## Decision signals

- **Upside (best scenario − price):** $+3.10
- **Downside (worst scenario − price):** $-1.31
- **Expected value vs current** (weighted FV − price): $+0.71 (+8.5%)
- **Position:** BUY (undervalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
