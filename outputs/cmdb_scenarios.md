# CMDB — Scenario Fair Value (Bulk Set A (China-driven))

- **Current price:** $17.80
- **Analyst target:** $27.98
- **NAV / share (reference, unflexed):** $32.65 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $20.79 (+16.8% vs price)
- **Breakeven TCE (scenario-invariant):** $0/day — **price justified by NAV alone** (blended FV clears the price even at zero rates; the entire earnings leg is optionality on top of asset coverage).
- **Position (tool view):** BUY (undervalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| China acceleration | 20% | 1.14× | $36.75 | $24.79 | $24.28–$25.29 | 1.75× | 0.70 | $22.60 | $29,403 | n/a |
| Moderate growth (base) | 40% | 0.99× | $32.38 | $21.12 | $20.60–$21.64 | 1.33× | 0.60 | $18.80 | $22,174 | n/a |
| China property drag | 25% | 0.92× | $30.27 | $19.29 | $18.71–$19.87 | 1.14× | 0.50 | $17.38 | $18,446 | n/a |
| Coordinated slowdown | 15% | 0.83× | $27.84 | $17.06 | $16.61–$17.51 | 0.95× | 0.50 | $14.62 | $15,577 | n/a |
| **Probability-weighted** | | | | **$20.79** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven is n/a — the price clears at any rate, so every scenario's rates trivially justify it._

## Decision signals

- **Upside (best scenario − price):** $+6.99
- **Downside (worst scenario − price):** $-0.74
- **Expected value vs current** (weighted FV − price): $+2.99 (+16.8%)
- **Position:** BUY (undervalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
