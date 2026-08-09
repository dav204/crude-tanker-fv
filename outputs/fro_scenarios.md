# FRO — Scenario Fair Value (three-phase MoU framework)

- **Current price:** $39.74
- **Analyst target:** $30.50
- **NAV / share (reference, unflexed):** $25.34 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $24.22 (-39.0% vs price)
- **Breakeven TCE (scenario-invariant):** $416,150/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** TRIM/SHORT (overvalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Escalation | 25% | 1.25× | $34.80 | $41.59 | $39.68–$43.79 | 7.66× | 0.70 | $57.42 | $281,002 | 0.68× |
| Pre-MoU baseline | 57% | 0.82× | $18.52 | $19.56 | $18.87–$20.30 | 2.46× | 0.70 | $22.00 | $89,867 | 0.22× |
| MoU base case | 5% | 0.75× | $15.85 | $16.41 | $15.76–$17.01 | 2.00× | 0.70 | $17.71 | $72,716 | 0.17× |
| MoU bear | 13% | 0.70× | $14.06 | $14.26 | $13.78–$14.74 | 1.55× | 0.70 | $14.73 | $56,124 | 0.13× |
| **Probability-weighted** | | | | **$24.22** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $+1.85
- **Downside (worst scenario − price):** $-25.48
- **Expected value vs current** (weighted FV − price): $-15.52 (-39.0%)
- **Position:** TRIM/SHORT (overvalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
