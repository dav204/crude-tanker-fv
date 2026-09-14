# NAT — Scenario Fair Value (three-phase MoU framework)

- **Current price:** $7.46
- **Analyst target:** $6.00
- **NAV / share (reference, unflexed):** $2.76 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $2.97 (-60.2% vs price)
- **Breakeven TCE (scenario-invariant):** $778,983/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** TRIM/SHORT (overvalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Escalation | 28% | 1.25× | $3.69 | $4.43 | $4.20–$4.70 | 5.36× | 0.70 | $6.16 | $148,750 | 0.19× |
| Pre-MoU baseline | 59% | 0.90× | $2.39 | $2.48 | $2.39–$2.58 | 2.06× | 0.70 | $2.69 | $57,175 | 0.07× |
| MoU base case | 0% | 0.83× | $2.13 | $2.16 | $2.08–$2.24 | 1.73× | 0.70 | $2.25 | $47,875 | 0.06× |
| MoU bear | 13% | 0.78× | $1.96 | $2.00 | $1.91–$2.09 | 1.48× | 0.60 | $2.06 | $41,000 | 0.05× |
| **Probability-weighted** | | | | **$2.97** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $-3.03
- **Downside (worst scenario − price):** $-5.46
- **Expected value vs current** (weighted FV − price): $-4.49 (-60.2%)
- **Position:** TRIM/SHORT (overvalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
