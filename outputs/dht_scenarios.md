# DHT — Scenario Fair Value (three-phase MoU framework)

- **Current price:** $18.76
- **Analyst target:** $16.00
- **NAV / share (reference, unflexed):** $15.01 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $14.48 (-22.8% vs price)
- **Breakeven TCE (scenario-invariant):** $358,707/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** TRIM/SHORT (overvalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Escalation | 25% | 1.25× | $19.09 | $21.71 | $20.99–$22.54 | 8.44× | 0.70 | $27.83 | $337,500 | 0.94× |
| Pre-MoU baseline | 57% | 0.82× | $11.99 | $12.55 | $12.28–$12.83 | 2.65× | 0.70 | $13.84 | $106,100 | 0.30× |
| MoU base case | 5% | 0.74× | $10.82 | $11.20 | $10.95–$11.42 | 2.12× | 0.70 | $12.09 | $84,875 | 0.24× |
| MoU bear | 13% | 0.70× | $10.05 | $10.32 | $10.14–$10.50 | 1.63× | 0.70 | $10.94 | $65,250 | 0.18× |
| **Probability-weighted** | | | | **$14.48** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $+2.95
- **Downside (worst scenario − price):** $-8.44
- **Expected value vs current** (weighted FV − price): $-4.28 (-22.8%)
- **Position:** TRIM/SHORT (overvalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
