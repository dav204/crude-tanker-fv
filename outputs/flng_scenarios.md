# FLNG — Scenario Fair Value (LNG glut-cycle framework)

- **Current price:** $31.93
- **Analyst target:** $25.00
- **NAV / share (reference, unflexed):** $27.22 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $29.47 (-7.7% vs price)
- **Breakeven TCE (scenario-invariant):** $328,633/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** TRIM/SHORT (overvalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Tight resurgence | 25% | 1.25× | $40.48 | $38.00 | $37.76–$38.30 | 1.74× | 0.70 | $32.22 | $147,500 | 0.45× |
| Moderate tightening | 25% | 1.13× | $34.24 | $32.41 | $32.21–$32.68 | 0.93× | 0.50 | $30.59 | $78,750 | 0.24× |
| Glut base case | 38% | 0.96× | $25.14 | $25.13 | $24.94–$25.35 | 0.68× | 0.40 | $25.12 | $58,000 | 0.18× |
| Glut intensifies | 12% | 0.84× | $18.74 | $19.34 | $19.18–$19.53 | 0.51× | 0.40 | $19.73 | $43,250 | 0.13× |
| Structural reset | 0% | 0.72× | $12.60 | $15.18 | $14.99–$15.37 | 0.48× | 0.30 | $16.28 | $40,500 | 0.12× |
| **Probability-weighted** | | | | **$29.47** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $+6.07
- **Downside (worst scenario − price):** $-16.75
- **Expected value vs current** (weighted FV − price): $-2.46 (-7.7%)
- **Position:** TRIM/SHORT (overvalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
