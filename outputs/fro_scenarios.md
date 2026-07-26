# FRO — Scenario Fair Value (three-phase MoU framework)

- **Current price:** $39.29
- **Analyst target:** $30.50
- **NAV / share (reference, unflexed):** $24.11 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $22.80 (-42.0% vs price)
- **Breakeven TCE (scenario-invariant):** $430,349/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** TRIM/SHORT (overvalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Escalation | 25% | 1.25× | $33.27 | $40.10 | $38.19–$42.31 | 7.63× | 0.70 | $56.05 | $278,816 | 0.65× |
| Pre-MoU baseline | 45% | 0.82× | $17.52 | $18.59 | $17.90–$19.33 | 2.46× | 0.70 | $21.10 | $89,224 | 0.21× |
| MoU base case | 18% | 0.75× | $14.94 | $15.52 | $14.88–$16.13 | 2.00× | 0.70 | $16.90 | $72,236 | 0.17× |
| MoU bear | 12% | 0.70× | $13.20 | $13.43 | $12.95–$13.91 | 1.54× | 0.70 | $13.97 | $55,754 | 0.13× |
| **Probability-weighted** | | | | **$22.80** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $+0.81
- **Downside (worst scenario − price):** $-25.86
- **Expected value vs current** (weighted FV − price): $-16.49 (-42.0%)
- **Position:** TRIM/SHORT (overvalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
