# CMDB — Scenario Fair Value (Bulk Set A (China-driven))

- **Current price:** $20.52
- **Analyst target:** $27.98
- **NAV / share (reference, unflexed):** $32.20 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $19.53 (-4.8% vs price)
- **Breakeven TCE (scenario-invariant):** $18,156/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** HOLD (fairly valued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| China acceleration | 20% | 1.07× | $34.14 | $23.14 | $22.64–$23.65 | 1.75× | 0.70 | $21.37 | $29,253 | 1.61× |
| Moderate growth (base) | 40% | 0.93× | $30.30 | $19.83 | $19.31–$20.35 | 1.33× | 0.60 | $17.77 | $22,070 | 1.22× |
| China property drag | 25% | 0.87× | $28.46 | $18.18 | $17.61–$18.76 | 1.14× | 0.50 | $16.44 | $18,387 | 1.01× |
| Coordinated slowdown | 15% | 0.79× | $26.31 | $16.12 | $15.68–$16.57 | 0.95× | 0.50 | $13.83 | $15,520 | 0.85× |
| **Probability-weighted** | | | | **$19.53** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $+2.62
- **Downside (worst scenario − price):** $-4.40
- **Expected value vs current** (weighted FV − price): $-0.99 (-4.8%)
- **Position:** HOLD (fairly valued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
