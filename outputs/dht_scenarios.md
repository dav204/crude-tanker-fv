# DHT — Scenario Fair Value (three-phase MoU framework)

- **Current price:** $18.89
- **Analyst target:** $16.00
- **NAV / share (reference, unflexed):** $12.93 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $14.77 (-21.8% vs price)
- **Breakeven TCE (scenario-invariant):** $529,540/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** TRIM/SHORT (overvalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Escalation | 25% | 1.25× | $16.58 | $19.25 | $18.57–$20.05 | 8.44× | 0.70 | $25.49 | $337,500 | 0.64× |
| Pre-MoU baseline | 45% | 1.11× | $14.55 | $15.89 | $15.50–$16.33 | 4.74× | 0.70 | $19.02 | $189,500 | 0.36× |
| MoU base case | 18% | 0.74× | $9.19 | $9.66 | $9.42–$9.88 | 2.12× | 0.70 | $10.76 | $84,875 | 0.16× |
| MoU bear | 12% | 0.70× | $8.51 | $8.86 | $8.68–$9.04 | 1.63× | 0.70 | $9.68 | $65,250 | 0.12× |
| **Probability-weighted** | | | | **$14.77** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $+0.36
- **Downside (worst scenario − price):** $-10.03
- **Expected value vs current** (weighted FV − price): $-4.12 (-21.8%)
- **Position:** TRIM/SHORT (overvalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
