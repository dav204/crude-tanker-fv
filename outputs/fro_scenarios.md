# FRO — Scenario Fair Value (three-phase MoU framework)

- **Current price:** $35.52
- **Analyst target:** $30.50
- **NAV / share (reference, unflexed):** $22.67 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $27.53 (-22.5% vs price)
- **Breakeven TCE (scenario-invariant):** $366,009/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** TRIM/SHORT (overvalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Escalation | 25% | 1.25× | $31.47 | $38.69 | $36.78–$40.90 | 7.61× | 0.70 | $55.56 | $276,773 | 0.76× |
| Pre-MoU baseline | 45% | 1.12× | $26.86 | $30.44 | $29.33–$31.69 | 4.41× | 0.70 | $38.80 | $159,143 | 0.43× |
| MoU base case | 18% | 0.75× | $13.87 | $14.69 | $14.04–$15.30 | 1.99× | 0.70 | $16.61 | $71,773 | 0.20× |
| MoU bear | 12% | 0.70× | $12.20 | $12.65 | $12.17–$13.13 | 1.54× | 0.70 | $13.69 | $55,384 | 0.15× |
| **Probability-weighted** | | | | **$27.53** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $+3.17
- **Downside (worst scenario − price):** $-22.87
- **Expected value vs current** (weighted FV − price): $-7.99 (-22.5%)
- **Position:** TRIM/SHORT (overvalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
