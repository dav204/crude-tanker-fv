# DHT — Scenario Fair Value (three-phase MoU framework)

- **Current price:** $19.17
- **Analyst target:** $16.00
- **NAV / share (reference, unflexed):** $15.01 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $15.97 (-16.7% vs price)
- **Breakeven TCE (scenario-invariant):** $535,858/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** TRIM/SHORT (overvalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Escalation | 25% | 1.25× | $19.09 | $21.53 | $20.85–$22.31 | 8.44× | 0.70 | $27.21 | $337,500 | 0.63× |
| Pre-MoU baseline | 62% | 0.96× | $14.38 | $14.63 | $14.38–$14.90 | 2.65× | 0.70 | $15.23 | $106,100 | 0.20× |
| MoU base case | 0% | 0.86× | $12.65 | $12.82 | $12.59–$13.03 | 2.12× | 0.70 | $13.20 | $84,875 | 0.16× |
| MoU bear | 13% | 0.79× | $11.54 | $11.64 | $11.46–$11.81 | 1.63× | 0.70 | $11.86 | $65,250 | 0.12× |
| **Probability-weighted** | | | | **$15.97** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $+2.36
- **Downside (worst scenario − price):** $-7.53
- **Expected value vs current** (weighted FV − price): $-3.20 (-16.7%)
- **Position:** TRIM/SHORT (overvalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
