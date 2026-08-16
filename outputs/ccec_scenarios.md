# CCEC — Scenario Fair Value (LNG glut-cycle framework)

- **Current price:** $22.61
- **Analyst target:** $25.17
- **NAV / share (reference, unflexed):** $25.70 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $33.70 (+49.1% vs price)
- **Breakeven TCE (scenario-invariant):** $0/day — **price justified by NAV alone** (blended FV clears the price even at zero rates; the entire earnings leg is optionality on top of asset coverage).
- **Position (tool view):** BUY (undervalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Tight resurgence | 25% | 1.25× | $50.28 | $47.20 | $47.03–$47.41 | 1.79× | 0.70 | $40.03 | $136,327 | n/a |
| Moderate tightening | 25% | 1.13× | $38.81 | $39.08 | $38.93–$39.28 | 1.01× | 0.50 | $39.35 | $73,865 | n/a |
| Glut base case | 38% | 0.96× | $22.11 | $26.78 | $26.64–$26.95 | 0.75× | 0.40 | $29.89 | $54,599 | n/a |
| Glut intensifies | 12% | 0.84× | $10.31 | $16.27 | $16.15–$16.41 | 0.57× | 0.40 | $20.24 | $40,848 | n/a |
| Structural reset | 0% | 0.72× | $-1.37 | $6.00 | $5.88–$6.11 | 0.51× | 0.40 | $10.90 | $37,815 | n/a |
| **Probability-weighted** | | | | **$33.70** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven is n/a — the price clears at any rate, so every scenario's rates trivially justify it._

## Decision signals

- **Upside (best scenario − price):** $+24.59
- **Downside (worst scenario − price):** $-16.61
- **Expected value vs current** (weighted FV − price): $+11.09 (+49.1%)
- **Position:** BUY (undervalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
