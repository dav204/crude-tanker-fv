# SB — Scenario Fair Value (Bulk Set A (China-driven))

- **Current price:** $7.81
- **Analyst target:** $7.10
- **NAV / share (reference, unflexed):** $10.07 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $9.47 (+21.3% vs price)
- **Breakeven TCE (scenario-invariant):** $0/day — **price justified by NAV alone** (blended FV clears the price even at zero rates; the entire earnings leg is optionality on top of asset coverage).
- **Position (tool view):** BUY (undervalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| China acceleration | 20% | 1.15× | $12.53 | $12.22 | $12.04–$12.39 | 1.96× | 0.70 | $11.50 | $26,962 | n/a |
| Moderate growth (base) | 40% | 0.98× | $9.78 | $9.58 | $9.41–$9.75 | 1.49× | 0.60 | $9.29 | $20,390 | n/a |
| China property drag | 25% | 0.92× | $8.77 | $8.53 | $8.38–$8.67 | 1.29× | 0.60 | $8.16 | $17,319 | n/a |
| Coordinated slowdown | 15% | 0.82× | $7.17 | $7.10 | $6.95–$7.24 | 1.08× | 0.50 | $7.02 | $14,569 | n/a |
| **Probability-weighted** | | | | **$9.47** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven is n/a — the price clears at any rate, so every scenario's rates trivially justify it._

## Decision signals

- **Upside (best scenario − price):** $+4.41
- **Downside (worst scenario − price):** $-0.71
- **Expected value vs current** (weighted FV − price): $+1.66 (+21.3%)
- **Position:** BUY (undervalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
