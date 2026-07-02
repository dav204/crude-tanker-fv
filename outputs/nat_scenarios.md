# NAT — Scenario Fair Value (three-phase MoU framework)

- **Current price:** $5.56
- **Analyst target:** $6.00
- **NAV / share (reference, unflexed):** $2.79 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $3.33 (-40.1% vs price)
- **Breakeven TCE (scenario-invariant):** $362,899/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** TRIM/SHORT (overvalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Escalation | 25% | 1.25× | $3.75 | $4.48 | $4.25–$4.75 | 5.36× | 0.70 | $6.20 | $148,750 | 0.41× |
| Pre-MoU baseline | 45% | 1.11× | $3.21 | $3.62 | $3.48–$3.79 | 3.63× | 0.70 | $4.59 | $100,750 | 0.28× |
| MoU base case | 18% | 0.77× | $1.92 | $1.98 | $1.90–$2.06 | 1.73× | 0.70 | $2.13 | $47,875 | 0.13× |
| MoU bear | 12% | 0.73× | $1.78 | $1.85 | $1.76–$1.94 | 1.48× | 0.60 | $1.95 | $41,000 | 0.11× |
| **Probability-weighted** | | | | **$3.33** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $-1.08
- **Downside (worst scenario − price):** $-3.71
- **Expected value vs current** (weighted FV − price): $-2.23 (-40.1%)
- **Position:** TRIM/SHORT (overvalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
