# DHT — Scenario Fair Value (three-phase MoU framework)

- **Current price:** $17.08
- **Analyst target:** $16.00
- **NAV / share (reference, unflexed):** $13.10 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $14.92 (-12.7% vs price)
- **Breakeven TCE (scenario-invariant):** $379,413/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** TRIM/SHORT (overvalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Escalation | 25% | 1.25× | $16.78 | $19.44 | $18.75–$20.24 | 8.44× | 0.70 | $25.64 | $337,500 | 0.89× |
| Pre-MoU baseline | 45% | 1.11× | $14.73 | $16.05 | $15.67–$16.50 | 4.74× | 0.70 | $19.15 | $189,500 | 0.50× |
| MoU base case | 18% | 0.74× | $9.31 | $9.77 | $9.54–$9.99 | 2.12× | 0.70 | $10.84 | $84,875 | 0.22× |
| MoU bear | 12% | 0.70× | $8.62 | $8.96 | $8.79–$9.14 | 1.63× | 0.70 | $9.76 | $65,250 | 0.17× |
| **Probability-weighted** | | | | **$14.92** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $+2.36
- **Downside (worst scenario − price):** $-8.12
- **Expected value vs current** (weighted FV − price): $-2.16 (-12.7%)
- **Position:** TRIM/SHORT (overvalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
