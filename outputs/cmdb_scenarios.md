# CMDB — Scenario Fair Value (Bulk Set A (China-driven))

- **Current price:** $17.80
- **Analyst target:** $27.98
- **NAV / share (reference, unflexed):** $32.43 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $20.61 (+15.8% vs price)
- **Breakeven TCE (scenario-invariant):** $949/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** BUY (undervalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| China acceleration | 20% | 1.14× | $36.53 | $24.62 | $24.11–$25.12 | 1.75× | 0.70 | $22.39 | $29,191 | 30.76× |
| Moderate growth (base) | 40% | 0.99× | $32.15 | $20.94 | $20.43–$21.46 | 1.33× | 0.60 | $18.60 | $22,028 | 23.21× |
| China property drag | 25% | 0.92× | $30.07 | $19.12 | $18.55–$19.70 | 1.14× | 0.50 | $17.20 | $18,366 | 19.35× |
| Coordinated slowdown | 15% | 0.83× | $27.61 | $16.88 | $16.44–$17.33 | 0.95× | 0.50 | $14.44 | $15,497 | 16.33× |
| **Probability-weighted** | | | | **$20.61** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $+6.82
- **Downside (worst scenario − price):** $-0.92
- **Expected value vs current** (weighted FV − price): $+2.81 (+15.8%)
- **Position:** BUY (undervalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
