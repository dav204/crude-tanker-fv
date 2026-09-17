# DHT — Scenario Fair Value (three-phase MoU framework)

- **Current price:** $22.89
- **Analyst target:** $16.00
- **NAV / share (reference, unflexed):** $15.01 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $16.32 (-28.7% vs price)
- **Breakeven TCE (scenario-invariant):** $869,198/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** TRIM/SHORT (overvalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Escalation | 28% | 1.25× | $19.09 | $21.53 | $20.85–$22.31 | 8.44× | 0.70 | $27.21 | $337,500 | 0.39× |
| Pre-MoU baseline | 59% | 0.98× | $14.63 | $14.86 | $14.61–$15.12 | 2.65× | 0.70 | $15.39 | $106,100 | 0.12× |
| MoU base case | 0% | 0.87× | $12.85 | $12.99 | $12.76–$13.20 | 2.12× | 0.70 | $13.32 | $84,875 | 0.10× |
| MoU bear | 13% | 0.80× | $11.70 | $11.78 | $11.60–$11.95 | 1.63× | 0.70 | $11.96 | $65,250 | 0.08× |
| **Probability-weighted** | | | | **$16.32** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $-1.37
- **Downside (worst scenario − price):** $-11.12
- **Expected value vs current** (weighted FV − price): $-6.57 (-28.7%)
- **Position:** TRIM/SHORT (overvalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
