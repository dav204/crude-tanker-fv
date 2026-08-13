# ECO — Scenario Fair Value (three-phase MoU framework)

- **Current price:** $62.88
- **Analyst target:** $45.00
- **NAV / share (reference, unflexed):** $39.54 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $41.44 (-34.1% vs price)
- **Breakeven TCE (scenario-invariant):** $549,197/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** TRIM/SHORT (overvalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Escalation | 25% | 1.25× | $52.08 | $60.70 | $57.95–$63.87 | 6.91× | 0.70 | $80.80 | $244,039 | 0.44× |
| Pre-MoU baseline | 57% | 0.95× | $37.17 | $36.92 | $35.87–$38.03 | 2.36× | 0.70 | $36.33 | $81,874 | 0.15× |
| MoU base case | 5% | 0.86× | $32.39 | $31.53 | $30.59–$32.42 | 1.93× | 0.70 | $29.54 | $66,554 | 0.12× |
| MoU bear | 13% | 0.80× | $29.34 | $28.08 | $27.33–$28.82 | 1.56× | 0.70 | $25.13 | $53,242 | 0.10× |
| **Probability-weighted** | | | | **$41.44** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $-2.18
- **Downside (worst scenario − price):** $-34.80
- **Expected value vs current** (weighted FV − price): $-21.44 (-34.1%)
- **Position:** TRIM/SHORT (overvalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
