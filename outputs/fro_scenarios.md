# FRO — Scenario Fair Value (three-phase MoU framework)

- **Current price:** $40.93
- **Analyst target:** $30.50
- **NAV / share (reference, unflexed):** $24.08 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $29.18 (-28.7% vs price)
- **Breakeven TCE (scenario-invariant):** $472,015/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** TRIM/SHORT (overvalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Escalation | 25% | 1.25× | $33.23 | $40.56 | $38.74–$42.67 | 7.64× | 0.70 | $57.67 | $279,119 | 0.59× |
| Pre-MoU baseline | 45% | 1.12× | $28.42 | $32.23 | $31.17–$33.43 | 4.42× | 0.70 | $41.12 | $160,315 | 0.34× |
| MoU base case | 18% | 0.75× | $14.92 | $15.97 | $15.35–$16.55 | 2.00× | 0.70 | $18.43 | $72,279 | 0.15× |
| MoU bear | 12% | 0.70× | $13.18 | $13.86 | $13.40–$14.32 | 1.54× | 0.70 | $15.46 | $55,765 | 0.12× |
| **Probability-weighted** | | | | **$29.18** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $-0.37
- **Downside (worst scenario − price):** $-27.07
- **Expected value vs current** (weighted FV − price): $-11.75 (-28.7%)
- **Position:** TRIM/SHORT (overvalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
