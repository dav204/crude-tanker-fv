# DHT — Scenario Fair Value (three-phase MoU framework)

- **Current price:** $23.27
- **Analyst target:** $16.00
- **NAV / share (reference, unflexed):** $15.01 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $16.56 (-28.8% vs price)
- **Breakeven TCE (scenario-invariant):** $905,605/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** TRIM/SHORT (overvalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Escalation | 28% | 1.25× | $19.09 | $21.53 | $20.85–$22.31 | 8.44× | 0.70 | $27.21 | $337,500 | 0.37× |
| Pre-MoU baseline | 59% | 1.00× | $15.00 | $15.25 | $14.99–$15.53 | 2.78× | 0.70 | $15.82 | $111,200 | 0.12× |
| MoU base case | 0% | 0.90× | $13.37 | $13.54 | $13.29–$13.77 | 2.31× | 0.70 | $13.94 | $92,250 | 0.10× |
| MoU bear | 13% | 0.80× | $11.74 | $11.82 | $11.64–$11.99 | 1.64× | 0.70 | $12.01 | $65,775 | 0.07× |
| **Probability-weighted** | | | | **$16.56** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $-1.74
- **Downside (worst scenario − price):** $-11.45
- **Expected value vs current** (weighted FV − price): $-6.71 (-28.8%)
- **Position:** TRIM/SHORT (overvalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
