# ECO — Scenario Fair Value (three-phase MoU framework)

- **Current price:** $47.70
- **Analyst target:** $45.00
- **NAV / share (reference, unflexed):** $33.70 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $39.32 (-17.6% vs price)
- **Breakeven TCE (scenario-invariant):** $299,841/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** TRIM/SHORT (overvalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Escalation | 25% | 1.25× | $45.83 | $54.21 | $51.83–$56.95 | 6.89× | 0.70 | $73.77 | $242,648 | 0.81× |
| Pre-MoU baseline | 45% | 1.11× | $39.05 | $43.17 | $41.75–$44.78 | 4.18× | 0.70 | $52.79 | $144,901 | 0.48× |
| MoU base case | 18% | 0.75× | $21.71 | $22.15 | $21.34–$22.93 | 1.92× | 0.70 | $23.19 | $66,282 | 0.22× |
| MoU bear | 12% | 0.71× | $19.63 | $19.62 | $18.97–$20.27 | 1.55× | 0.70 | $19.59 | $53,064 | 0.18× |
| **Probability-weighted** | | | | **$39.32** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $+6.51
- **Downside (worst scenario − price):** $-28.08
- **Expected value vs current** (weighted FV − price): $-8.38 (-17.6%)
- **Position:** TRIM/SHORT (overvalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
