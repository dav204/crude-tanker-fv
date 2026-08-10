# NAT — Scenario Fair Value (three-phase MoU framework)

- **Current price:** $6.46
- **Analyst target:** $6.00
- **NAV / share (reference, unflexed):** $2.85 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $3.05 (-52.8% vs price)
- **Breakeven TCE (scenario-invariant):** $620,285/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** TRIM/SHORT (overvalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Escalation | 25% | 1.25× | $3.81 | $4.54 | $4.31–$4.80 | 5.36× | 0.70 | $6.24 | $148,750 | 0.24× |
| Pre-MoU baseline | 57% | 0.94× | $2.61 | $2.67 | $2.58–$2.77 | 2.06× | 0.70 | $2.82 | $57,175 | 0.09× |
| MoU base case | 5% | 0.86× | $2.30 | $2.32 | $2.24–$2.40 | 1.73× | 0.70 | $2.35 | $47,875 | 0.08× |
| MoU bear | 13% | 0.81× | $2.12 | $2.14 | $2.05–$2.23 | 1.48× | 0.60 | $2.16 | $41,000 | 0.07× |
| **Probability-weighted** | | | | **$3.05** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $-1.92
- **Downside (worst scenario − price):** $-4.32
- **Expected value vs current** (weighted FV − price): $-3.41 (-52.8%)
- **Position:** TRIM/SHORT (overvalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
