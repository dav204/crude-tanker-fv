# ECO — Scenario Fair Value (three-phase MoU framework)

- **Current price:** $85.66
- **Analyst target:** $45.00
- **NAV / share (reference, unflexed):** $39.54 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $42.22 (-50.7% vs price)
- **Breakeven TCE (scenario-invariant):** $933,268/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** TRIM/SHORT (overvalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Escalation | 28% | 1.25× | $52.08 | $60.70 | $57.95–$63.87 | 6.91× | 0.70 | $80.80 | $244,039 | 0.26× |
| Pre-MoU baseline | 59% | 0.95× | $36.83 | $36.61 | $35.57–$37.73 | 2.36× | 0.70 | $36.11 | $81,874 | 0.09× |
| MoU base case | 0% | 0.85× | $32.12 | $31.29 | $30.36–$32.19 | 1.93× | 0.70 | $29.36 | $66,554 | 0.07× |
| MoU bear | 13% | 0.79× | $29.12 | $27.88 | $27.13–$28.63 | 1.56× | 0.70 | $24.99 | $53,242 | 0.06× |
| **Probability-weighted** | | | | **$42.22** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $-24.96
- **Downside (worst scenario − price):** $-57.78
- **Expected value vs current** (weighted FV − price): $-43.44 (-50.7%)
- **Position:** TRIM/SHORT (overvalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
