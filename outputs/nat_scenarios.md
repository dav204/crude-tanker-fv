# NAT — Scenario Fair Value (three-phase MoU framework)

- **Current price:** $6.53
- **Analyst target:** $6.00
- **NAV / share (reference, unflexed):** $2.85 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $2.79 (-57.2% vs price)
- **Breakeven TCE (scenario-invariant):** $466,586/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** TRIM/SHORT (overvalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Escalation | 25% | 1.25× | $3.81 | $4.54 | $4.31–$4.80 | 5.36× | 0.70 | $6.24 | $148,750 | 0.32× |
| Pre-MoU baseline | 57% | 0.83× | $2.18 | $2.30 | $2.21–$2.40 | 2.06× | 0.70 | $2.57 | $57,175 | 0.12× |
| MoU base case | 5% | 0.77× | $1.96 | $2.01 | $1.94–$2.09 | 1.73× | 0.70 | $2.15 | $47,875 | 0.10× |
| MoU bear | 13% | 0.73× | $1.82 | $1.88 | $1.79–$1.97 | 1.48× | 0.60 | $1.97 | $41,000 | 0.09× |
| **Probability-weighted** | | | | **$2.79** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $-1.99
- **Downside (worst scenario − price):** $-4.65
- **Expected value vs current** (weighted FV − price): $-3.73 (-57.2%)
- **Position:** TRIM/SHORT (overvalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
