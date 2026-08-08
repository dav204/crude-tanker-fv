# ECO — Scenario Fair Value (three-phase MoU framework)

- **Current price:** $61.86
- **Analyst target:** $45.00
- **NAV / share (reference, unflexed):** $37.65 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $35.69 (-42.3% vs price)
- **Breakeven TCE (scenario-invariant):** $421,886/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** TRIM/SHORT (overvalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Escalation | 25% | 1.25× | $49.72 | $58.46 | $55.71–$61.63 | 6.85× | 0.70 | $78.85 | $240,384 | 0.57× |
| Pre-MoU baseline | 57% | 0.82× | $28.97 | $29.51 | $28.46–$30.62 | 2.35× | 0.70 | $30.77 | $80,927 | 0.19× |
| MoU base case | 5% | 0.75× | $25.73 | $25.51 | $24.57–$26.40 | 1.92× | 0.70 | $24.99 | $65,838 | 0.16× |
| MoU bear | 13% | 0.71× | $23.67 | $22.94 | $22.19–$23.68 | 1.55× | 0.70 | $21.24 | $52,773 | 0.13× |
| **Probability-weighted** | | | | **$35.69** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $-3.40
- **Downside (worst scenario − price):** $-38.92
- **Expected value vs current** (weighted FV − price): $-26.17 (-42.3%)
- **Position:** TRIM/SHORT (overvalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
