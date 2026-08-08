# DHT — Scenario Fair Value (three-phase MoU framework)

- **Current price:** $18.76
- **Analyst target:** $16.00
- **NAV / share (reference, unflexed):** $13.83 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $13.51 (-28.0% vs price)
- **Breakeven TCE (scenario-invariant):** $437,369/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** TRIM/SHORT (overvalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Escalation | 25% | 1.25× | $17.61 | $20.37 | $19.65–$21.20 | 8.44× | 0.70 | $26.81 | $337,500 | 0.77× |
| Pre-MoU baseline | 57% | 0.82× | $11.03 | $11.67 | $11.41–$11.95 | 2.65× | 0.70 | $13.17 | $106,100 | 0.24× |
| MoU base case | 5% | 0.74× | $9.94 | $10.40 | $10.16–$10.63 | 2.12× | 0.70 | $11.48 | $84,875 | 0.19× |
| MoU bear | 13% | 0.70× | $9.23 | $9.57 | $9.39–$9.76 | 1.63× | 0.70 | $10.36 | $65,250 | 0.15× |
| **Probability-weighted** | | | | **$13.51** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $+1.61
- **Downside (worst scenario − price):** $-9.19
- **Expected value vs current** (weighted FV − price): $-5.25 (-28.0%)
- **Position:** TRIM/SHORT (overvalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
