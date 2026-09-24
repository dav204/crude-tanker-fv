# SB — Scenario Fair Value (Bulk Set A (China-driven))

- **Current price:** $8.37
- **Analyst target:** $7.10
- **NAV / share (reference, unflexed):** $10.72 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $9.04 (+8.0% vs price)
- **Breakeven TCE (scenario-invariant):** $0/day — **price justified by NAV alone** (blended FV clears the price even at zero rates; the entire earnings leg is optionality on top of asset coverage).
- **Position (tool view):** BUY (undervalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| China acceleration | 20% | 1.06× | $11.73 | $11.41 | $11.31–$11.52 | 1.96× | 0.70 | $10.67 | $26,674 | n/a |
| Moderate growth (base) | 40% | 0.91× | $9.18 | $9.11 | $9.00–$9.21 | 1.49× | 0.60 | $8.99 | $20,192 | n/a |
| China property drag | 25% | 0.86× | $8.27 | $8.24 | $8.15–$8.34 | 1.30× | 0.60 | $8.20 | $17,209 | n/a |
| Coordinated slowdown | 15% | 0.78× | $6.78 | $7.03 | $6.94–$7.12 | 1.08× | 0.50 | $7.27 | $14,459 | n/a |
| **Probability-weighted** | | | | **$9.04** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven is n/a — the price clears at any rate, so every scenario's rates trivially justify it._

## Decision signals

- **Upside (best scenario − price):** $+3.04
- **Downside (worst scenario − price):** $-1.34
- **Expected value vs current** (weighted FV − price): $+0.67 (+8.0%)
- **Position:** BUY (undervalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
