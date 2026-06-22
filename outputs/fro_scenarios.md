# FRO — Scenario Fair Value (three-phase MoU framework)

- **Current price:** $40.93
- **Analyst target:** $30.50
- **NAV / share (reference, unflexed):** $24.22 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $28.82 (-29.6% vs price)
- **Breakeven TCE (scenario-invariant):** $466,274/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** TRIM/SHORT (overvalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Escalation | 25% | 1.25× | $33.41 | $40.26 | $38.35–$42.46 | 7.64× | 0.70 | $56.24 | $279,339 | 0.60× |
| Pre-MoU baseline | 45% | 1.12× | $28.58 | $31.83 | $30.72–$33.08 | 4.42× | 0.70 | $39.41 | $160,425 | 0.34× |
| MoU base case | 18% | 0.75× | $15.02 | $15.62 | $14.97–$16.22 | 2.00× | 0.70 | $17.01 | $72,327 | 0.16× |
| MoU bear | 12% | 0.70× | $13.28 | $13.52 | $13.04–$14.00 | 1.54× | 0.70 | $14.07 | $55,801 | 0.12× |
| **Probability-weighted** | | | | **$28.82** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $-0.67
- **Downside (worst scenario − price):** $-27.41
- **Expected value vs current** (weighted FV − price): $-12.11 (-29.6%)
- **Position:** TRIM/SHORT (overvalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
