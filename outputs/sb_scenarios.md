# SB — Scenario Fair Value (Bulk Set A (China-driven))

- **Current price:** $8.91
- **Analyst target:** $7.10
- **NAV / share (reference, unflexed):** $10.72 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $9.08 (+1.9% vs price)
- **Breakeven TCE (scenario-invariant):** $0/day — **price justified by NAV alone** (blended FV clears the price even at zero rates; the entire earnings leg is optionality on top of asset coverage).
- **Position (tool view):** HOLD (fairly valued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| China acceleration | 20% | 1.06× | $11.80 | $11.47 | $11.37–$11.58 | 1.96× | 0.70 | $10.71 | $26,674 | n/a |
| Moderate growth (base) | 40% | 0.92× | $9.23 | $9.15 | $9.05–$9.25 | 1.49× | 0.60 | $9.02 | $20,192 | n/a |
| China property drag | 25% | 0.86× | $8.32 | $8.28 | $8.19–$8.38 | 1.30× | 0.60 | $8.23 | $17,209 | n/a |
| Coordinated slowdown | 15% | 0.78× | $6.81 | $7.06 | $6.97–$7.15 | 1.08× | 0.50 | $7.30 | $14,459 | n/a |
| **Probability-weighted** | | | | **$9.08** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven is n/a — the price clears at any rate, so every scenario's rates trivially justify it._

## Decision signals

- **Upside (best scenario − price):** $+2.56
- **Downside (worst scenario − price):** $-1.85
- **Expected value vs current** (weighted FV − price): $+0.17 (+1.9%)
- **Position:** HOLD (fairly valued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
