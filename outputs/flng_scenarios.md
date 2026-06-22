# FLNG — Scenario Fair Value (LNG glut-cycle framework)

- **Current price:** $29.74
- **Analyst target:** $25.00
- **NAV / share (reference, unflexed):** $28.45 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $29.73 (-0.0% vs price)
- **Breakeven TCE (scenario-invariant):** $3,162,500/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** HOLD (fairly valued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Tight resurgence | 25% | 1.25× | $41.93 | $39.76 | $39.76–$39.76 | 1.74× | 0.70 | $34.70 | $147,500 | 0.05× |
| Moderate tightening | 25% | 1.13× | $35.59 | $32.82 | $32.82–$32.82 | 0.93× | 0.50 | $30.04 | $78,750 | 0.02× |
| Glut base case | 38% | 0.96× | $26.34 | $24.49 | $24.49–$24.49 | 0.68× | 0.40 | $23.25 | $58,000 | 0.02× |
| Glut intensifies | 12% | 0.84× | $19.84 | $19.03 | $19.03–$19.03 | 0.51× | 0.40 | $18.48 | $43,250 | 0.01× |
| Structural reset | 0% | 0.72× | $13.60 | $13.81 | $13.81–$13.81 | 0.48× | 0.30 | $13.90 | $40,500 | 0.01× |
| **Probability-weighted** | | | | **$29.73** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $+10.02
- **Downside (worst scenario − price):** $-15.93
- **Expected value vs current** (weighted FV − price): $-0.01 (-0.0%)
- **Position:** HOLD (fairly valued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
