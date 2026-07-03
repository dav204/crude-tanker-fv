# ECO — Scenario Fair Value (three-phase MoU framework)

- **Current price:** $53.11
- **Analyst target:** $45.00
- **NAV / share (reference, unflexed):** $34.35 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $25.73 (-51.6% vs price)
- **Breakeven TCE (scenario-invariant):** $343,913/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** TRIM/SHORT (overvalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Escalation | 10% | 1.25× | $46.64 | $55.62 | $52.86–$58.78 | 6.88× | 0.70 | $76.55 | $242,053 | 0.70× |
| Pre-MoU baseline | 20% | 0.82× | $25.51 | $26.29 | $25.25–$27.41 | 2.35× | 0.70 | $28.12 | $81,360 | 0.24× |
| MoU base case | 45% | 0.75× | $22.21 | $22.23 | $21.29–$23.12 | 1.92× | 0.70 | $22.29 | $66,165 | 0.19× |
| MoU bear | 25% | 0.71× | $20.10 | $19.62 | $18.87–$20.37 | 1.55× | 0.70 | $18.49 | $52,987 | 0.15× |
| **Probability-weighted** | | | | **$25.73** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $+2.51
- **Downside (worst scenario − price):** $-33.49
- **Expected value vs current** (weighted FV − price): $-27.38 (-51.6%)
- **Position:** TRIM/SHORT (overvalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
