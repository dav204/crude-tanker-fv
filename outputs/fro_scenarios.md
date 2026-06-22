# FRO — Scenario Fair Value (three-phase MoU framework)

- **Current price:** $40.93
- **Analyst target:** $30.50
- **NAV / share (reference, unflexed):** $24.08 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $28.68 (-29.9% vs price)
- **Breakeven TCE (scenario-invariant):** $469,143/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** TRIM/SHORT (overvalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Escalation | 25% | 1.25× | $33.23 | $40.09 | $38.18–$42.29 | 7.64× | 0.70 | $56.07 | $279,119 | 0.59× |
| Pre-MoU baseline | 45% | 1.12× | $28.42 | $31.67 | $30.57–$32.92 | 4.42× | 0.70 | $39.26 | $160,315 | 0.34× |
| MoU base case | 18% | 0.75× | $14.92 | $15.51 | $14.87–$16.12 | 2.00× | 0.70 | $16.91 | $72,279 | 0.15× |
| MoU bear | 12% | 0.70× | $13.18 | $13.42 | $12.94–$13.90 | 1.54× | 0.70 | $13.98 | $55,765 | 0.12× |
| **Probability-weighted** | | | | **$28.68** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $-0.84
- **Downside (worst scenario − price):** $-27.51
- **Expected value vs current** (weighted FV − price): $-12.25 (-29.9%)
- **Position:** TRIM/SHORT (overvalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
