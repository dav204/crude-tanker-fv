# ECO — Scenario Fair Value (three-phase MoU framework)

- **Current price:** $54.94
- **Analyst target:** $45.00
- **NAV / share (reference, unflexed):** $34.35 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $32.09 (-41.6% vs price)
- **Breakeven TCE (scenario-invariant):** $369,687/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** TRIM/SHORT (overvalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Escalation | 25% | 1.25× | $46.64 | $55.62 | $52.86–$58.78 | 6.88× | 0.70 | $76.55 | $242,053 | 0.65× |
| Pre-MoU baseline | 45% | 0.82× | $25.51 | $26.29 | $25.25–$27.41 | 2.35× | 0.70 | $28.12 | $81,360 | 0.22× |
| MoU base case | 18% | 0.75× | $22.21 | $22.23 | $21.29–$23.12 | 1.92× | 0.70 | $22.29 | $66,165 | 0.18× |
| MoU bear | 12% | 0.71× | $20.10 | $19.62 | $18.87–$20.37 | 1.55× | 0.70 | $18.49 | $52,987 | 0.14× |
| **Probability-weighted** | | | | **$32.09** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $+0.68
- **Downside (worst scenario − price):** $-35.32
- **Expected value vs current** (weighted FV − price): $-22.85 (-41.6%)
- **Position:** TRIM/SHORT (overvalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
