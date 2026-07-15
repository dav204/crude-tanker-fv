# NAT — Scenario Fair Value (three-phase MoU framework)

- **Current price:** $6.29
- **Analyst target:** $6.00
- **NAV / share (reference, unflexed):** $2.79 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $2.72 (-56.8% vs price)
- **Breakeven TCE (scenario-invariant):** $445,150/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** TRIM/SHORT (overvalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Escalation | 25% | 1.25× | $3.75 | $4.48 | $4.25–$4.75 | 5.36× | 0.70 | $6.20 | $148,750 | 0.33× |
| Pre-MoU baseline | 45% | 0.83× | $2.14 | $2.26 | $2.17–$2.36 | 2.06× | 0.70 | $2.55 | $57,175 | 0.13× |
| MoU base case | 18% | 0.77× | $1.92 | $1.98 | $1.90–$2.06 | 1.73× | 0.70 | $2.13 | $47,875 | 0.11× |
| MoU bear | 12% | 0.73× | $1.78 | $1.85 | $1.76–$1.94 | 1.48× | 0.60 | $1.95 | $41,000 | 0.09× |
| **Probability-weighted** | | | | **$2.72** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $-1.81
- **Downside (worst scenario − price):** $-4.44
- **Expected value vs current** (weighted FV − price): $-3.57 (-56.8%)
- **Position:** TRIM/SHORT (overvalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
