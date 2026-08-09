# SB — Scenario Fair Value (Bulk Set A (China-driven))

- **Current price:** $7.60
- **Analyst target:** $7.10
- **NAV / share (reference, unflexed):** $10.58 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $9.97 (+31.1% vs price)
- **Breakeven TCE (scenario-invariant):** $0/day — **price justified by NAV alone** (blended FV clears the price even at zero rates; the entire earnings leg is optionality on top of asset coverage).
- **Position (tool view):** BUY (undervalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| China acceleration | 20% | 1.15× | $13.21 | $12.73 | $12.62–$12.83 | 1.96× | 0.70 | $11.61 | $26,700 | n/a |
| Moderate growth (base) | 40% | 0.98× | $10.26 | $10.04 | $9.93–$10.14 | 1.49× | 0.60 | $9.70 | $20,209 | n/a |
| China property drag | 25% | 0.92× | $9.21 | $9.05 | $8.96–$9.14 | 1.30× | 0.60 | $8.81 | $17,219 | n/a |
| Coordinated slowdown | 15% | 0.82× | $7.48 | $7.62 | $7.53–$7.71 | 1.08× | 0.50 | $7.75 | $14,469 | n/a |
| **Probability-weighted** | | | | **$9.97** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven is n/a — the price clears at any rate, so every scenario's rates trivially justify it._

## Decision signals

- **Upside (best scenario − price):** $+5.13
- **Downside (worst scenario − price):** $+0.02
- **Expected value vs current** (weighted FV − price): $+2.37 (+31.1%)
- **Position:** BUY (undervalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
