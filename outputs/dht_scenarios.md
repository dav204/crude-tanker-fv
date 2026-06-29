# DHT — Scenario Fair Value (three-phase MoU framework)

- **Current price:** $17.65
- **Analyst target:** $16.00
- **NAV / share (reference, unflexed):** $12.51 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $14.42 (-18.3% vs price)
- **Breakeven TCE (scenario-invariant):** $459,855/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** TRIM/SHORT (overvalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Escalation | 25% | 1.25× | $16.05 | $18.84 | $18.15–$19.64 | 8.44× | 0.70 | $25.35 | $337,500 | 0.73× |
| Pre-MoU baseline | 45% | 1.11× | $14.08 | $15.52 | $15.13–$15.96 | 4.74× | 0.70 | $18.89 | $189,500 | 0.41× |
| MoU base case | 18% | 0.74× | $8.87 | $9.41 | $9.18–$9.63 | 2.12× | 0.70 | $10.67 | $84,875 | 0.18× |
| MoU bear | 12% | 0.70× | $8.21 | $8.63 | $8.45–$8.81 | 1.63× | 0.70 | $9.60 | $65,250 | 0.14× |
| **Probability-weighted** | | | | **$14.42** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $+1.19
- **Downside (worst scenario − price):** $-9.02
- **Expected value vs current** (weighted FV − price): $-3.23 (-18.3%)
- **Position:** TRIM/SHORT (overvalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
