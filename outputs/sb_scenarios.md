# SB — Scenario Fair Value (Bulk Set A (China-driven))

- **Current price:** $7.60
- **Analyst target:** $7.10
- **NAV / share (reference, unflexed):** $10.03 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $9.47 (+24.6% vs price)
- **Breakeven TCE (scenario-invariant):** $0/day — **price justified by NAV alone** (blended FV clears the price even at zero rates; the entire earnings leg is optionality on top of asset coverage).
- **Position (tool view):** BUY (undervalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| China acceleration | 20% | 1.15× | $12.58 | $12.14 | $12.04–$12.25 | 1.96× | 0.70 | $11.11 | $26,780 | n/a |
| Moderate growth (base) | 40% | 0.98× | $9.73 | $9.54 | $9.44–$9.64 | 1.49× | 0.60 | $9.26 | $20,265 | n/a |
| China property drag | 25% | 0.92× | $8.70 | $8.58 | $8.48–$8.67 | 1.29× | 0.60 | $8.39 | $17,250 | n/a |
| Coordinated slowdown | 15% | 0.82× | $7.03 | $7.19 | $7.10–$7.28 | 1.08× | 0.50 | $7.36 | $14,500 | n/a |
| **Probability-weighted** | | | | **$9.47** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven is n/a — the price clears at any rate, so every scenario's rates trivially justify it._

## Decision signals

- **Upside (best scenario − price):** $+4.54
- **Downside (worst scenario − price):** $-0.41
- **Expected value vs current** (weighted FV − price): $+1.87 (+24.6%)
- **Position:** BUY (undervalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
