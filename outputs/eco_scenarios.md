# ECO — Scenario Fair Value (three-phase MoU framework)

- **Current price:** $50.12
- **Analyst target:** $45.00
- **NAV / share (reference, unflexed):** $34.56 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $40.17 (-19.9% vs price)
- **Breakeven TCE (scenario-invariant):** $299,354/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** TRIM/SHORT (overvalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Escalation | 25% | 1.25× | $46.90 | $55.80 | $53.05–$58.97 | 6.88× | 0.70 | $76.56 | $241,662 | 0.81× |
| Pre-MoU baseline | 45% | 1.11× | $40.01 | $44.06 | $42.42–$45.92 | 4.18× | 0.70 | $53.54 | $144,437 | 0.48× |
| MoU base case | 18% | 0.75× | $22.37 | $22.35 | $21.41–$23.24 | 1.92× | 0.70 | $22.30 | $66,088 | 0.22× |
| MoU bear | 12% | 0.71× | $20.25 | $19.73 | $18.98–$20.48 | 1.55× | 0.70 | $18.50 | $52,937 | 0.18× |
| **Probability-weighted** | | | | **$40.17** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $+5.68
- **Downside (worst scenario − price):** $-30.39
- **Expected value vs current** (weighted FV − price): $-9.95 (-19.9%)
- **Position:** TRIM/SHORT (overvalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
