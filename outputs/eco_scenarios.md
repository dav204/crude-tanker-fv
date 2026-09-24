# ECO — Scenario Fair Value (three-phase MoU framework)

- **Current price:** $77.91
- **Analyst target:** $45.00
- **NAV / share (reference, unflexed):** $39.54 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $44.15 (-43.3% vs price)
- **Breakeven TCE (scenario-invariant):** $794,493/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** TRIM/SHORT (overvalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Escalation | 28% | 1.25× | $52.08 | $60.70 | $57.95–$63.87 | 6.91× | 0.70 | $80.80 | $244,039 | 0.31× |
| Pre-MoU baseline | 59% | 1.00× | $39.53 | $39.79 | $38.60–$41.05 | 2.68× | 0.70 | $40.38 | $91,542 | 0.12× |
| MoU base case | 0% | 0.90× | $34.52 | $34.08 | $33.01–$35.10 | 2.20× | 0.70 | $33.05 | $75,415 | 0.09× |
| MoU bear | 13% | 0.80× | $29.50 | $28.33 | $27.56–$29.10 | 1.60× | 0.70 | $25.60 | $54,609 | 0.07× |
| **Probability-weighted** | | | | **$44.15** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $-17.21
- **Downside (worst scenario − price):** $-49.58
- **Expected value vs current** (weighted FV − price): $-33.76 (-43.3%)
- **Position:** TRIM/SHORT (overvalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
