# NAT — Scenario Fair Value (three-phase MoU framework)

- **Current price:** $6.77
- **Analyst target:** $6.00
- **NAV / share (reference, unflexed):** $2.76 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $3.00 (-55.8% vs price)
- **Breakeven TCE (scenario-invariant):** $678,594/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** TRIM/SHORT (overvalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Escalation | 25% | 1.25× | $3.69 | $4.43 | $4.20–$4.70 | 5.36× | 0.70 | $6.16 | $148,750 | 0.22× |
| Pre-MoU baseline | 62% | 0.94× | $2.53 | $2.61 | $2.51–$2.70 | 2.06× | 0.70 | $2.78 | $57,175 | 0.08× |
| MoU base case | 0% | 0.86× | $2.24 | $2.26 | $2.19–$2.34 | 1.73× | 0.70 | $2.32 | $47,875 | 0.07× |
| MoU bear | 13% | 0.81× | $2.06 | $2.09 | $2.00–$2.18 | 1.48× | 0.60 | $2.12 | $41,000 | 0.06× |
| **Probability-weighted** | | | | **$3.00** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $-2.34
- **Downside (worst scenario − price):** $-4.68
- **Expected value vs current** (weighted FV − price): $-3.77 (-55.8%)
- **Position:** TRIM/SHORT (overvalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
