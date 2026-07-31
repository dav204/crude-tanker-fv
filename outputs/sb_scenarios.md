# SB — Scenario Fair Value (Bulk Set A (China-driven))

- **Current price:** $7.81
- **Analyst target:** $7.10
- **NAV / share (reference, unflexed):** $10.73 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $10.10 (+29.4% vs price)
- **Breakeven TCE (scenario-invariant):** $0/day — **price justified by NAV alone** (blended FV clears the price even at zero rates; the entire earnings leg is optionality on top of asset coverage).
- **Position (tool view):** BUY (undervalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| China acceleration | 20% | 1.15× | $13.28 | $12.79 | $12.69–$12.90 | 1.96× | 0.70 | $11.66 | $26,780 | n/a |
| Moderate growth (base) | 40% | 0.98× | $10.42 | $10.17 | $10.07–$10.28 | 1.49× | 0.60 | $9.80 | $20,265 | n/a |
| China property drag | 25% | 0.92× | $9.39 | $9.21 | $9.12–$9.31 | 1.29× | 0.60 | $8.94 | $17,250 | n/a |
| Coordinated slowdown | 15% | 0.82× | $7.72 | $7.81 | $7.72–$7.90 | 1.08× | 0.50 | $7.91 | $14,500 | n/a |
| **Probability-weighted** | | | | **$10.10** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven is n/a — the price clears at any rate, so every scenario's rates trivially justify it._

## Decision signals

- **Upside (best scenario − price):** $+4.98
- **Downside (worst scenario − price):** $+0.00
- **Expected value vs current** (weighted FV − price): $+2.29 (+29.4%)
- **Position:** BUY (undervalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
