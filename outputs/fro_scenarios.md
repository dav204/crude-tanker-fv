# FRO — Scenario Fair Value (three-phase MoU framework)

- **Current price:** $44.19
- **Analyst target:** $30.50
- **NAV / share (reference, unflexed):** $25.34 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $27.79 (-37.1% vs price)
- **Breakeven TCE (scenario-invariant):** $682,553/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** TRIM/SHORT (overvalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Escalation | 25% | 1.25× | $34.80 | $41.59 | $39.68–$43.79 | 7.66× | 0.70 | $57.42 | $281,002 | 0.41× |
| Pre-MoU baseline | 62% | 0.96× | $23.95 | $24.41 | $23.72–$25.15 | 2.46× | 0.70 | $25.49 | $89,867 | 0.13× |
| MoU base case | 0% | 0.86× | $20.08 | $20.19 | $19.54–$20.80 | 2.00× | 0.70 | $20.43 | $72,716 | 0.11× |
| MoU bear | 13% | 0.79× | $17.49 | $17.32 | $16.84–$17.81 | 1.55× | 0.70 | $16.93 | $56,124 | 0.08× |
| **Probability-weighted** | | | | **$27.79** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $-2.60
- **Downside (worst scenario − price):** $-26.87
- **Expected value vs current** (weighted FV − price): $-16.40 (-37.1%)
- **Position:** TRIM/SHORT (overvalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
