# CCEC — Scenario Fair Value (LNG glut-cycle framework)

- **Current price:** $21.35
- **Analyst target:** $25.17
- **NAV / share (reference, unflexed):** $28.10 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $35.91 (+68.2% vs price)
- **Breakeven TCE (scenario-invariant):** $0/day — **price justified by NAV alone** (blended FV clears the price even at zero rates; the entire earnings leg is optionality on top of asset coverage).
- **Position (tool view):** BUY (undervalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Tight resurgence | 25% | 1.25× | $52.98 | $49.70 | $49.52–$49.91 | 1.78× | 0.70 | $42.05 | $137,383 | n/a |
| Moderate tightening | 25% | 1.13× | $41.36 | $41.36 | $41.21–$41.56 | 1.00× | 0.50 | $41.36 | $74,327 | n/a |
| Glut base case | 38% | 0.96× | $24.44 | $28.84 | $28.70–$29.00 | 0.75× | 0.40 | $31.77 | $54,921 | n/a |
| Glut intensifies | 12% | 0.84× | $12.48 | $18.18 | $18.07–$18.33 | 0.56× | 0.40 | $21.98 | $41,075 | n/a |
| Structural reset | 0% | 0.72× | $0.69 | $7.81 | $7.69–$7.92 | 0.51× | 0.40 | $12.55 | $38,068 | n/a |
| **Probability-weighted** | | | | **$35.91** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven is n/a — the price clears at any rate, so every scenario's rates trivially justify it._

## Decision signals

- **Upside (best scenario − price):** $+28.35
- **Downside (worst scenario − price):** $-13.54
- **Expected value vs current** (weighted FV − price): $+14.56 (+68.2%)
- **Position:** BUY (undervalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
