# SB — Scenario Fair Value (Bulk Set A (China-driven))

- **Current price:** $7.67
- **Analyst target:** $7.10
- **NAV / share (reference, unflexed):** $10.02 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $9.42 (+22.9% vs price)
- **Breakeven TCE (scenario-invariant):** $0/day — **price justified by NAV alone** (blended FV clears the price even at zero rates; the entire earnings leg is optionality on top of asset coverage).
- **Position (tool view):** BUY (undervalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| China acceleration | 20% | 1.15× | $12.46 | $12.16 | $11.98–$12.33 | 1.96× | 0.70 | $11.45 | $26,943 | n/a |
| Moderate growth (base) | 40% | 0.98× | $9.73 | $9.53 | $9.36–$9.70 | 1.49× | 0.60 | $9.24 | $20,378 | n/a |
| China property drag | 25% | 0.92× | $8.72 | $8.48 | $8.34–$8.63 | 1.29× | 0.60 | $8.12 | $17,312 | n/a |
| Coordinated slowdown | 15% | 0.82× | $7.13 | $7.06 | $6.91–$7.20 | 1.08× | 0.50 | $6.98 | $14,562 | n/a |
| **Probability-weighted** | | | | **$9.42** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven is n/a — the price clears at any rate, so every scenario's rates trivially justify it._

## Decision signals

- **Upside (best scenario − price):** $+4.49
- **Downside (worst scenario − price):** $-0.61
- **Expected value vs current** (weighted FV − price): $+1.75 (+22.9%)
- **Position:** BUY (undervalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
