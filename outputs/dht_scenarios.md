# DHT — Scenario Fair Value (three-phase MoU framework)

- **Current price:** $16.65
- **Analyst target:** $16.00
- **NAV / share (reference, unflexed):** $12.93 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $15.08 (-9.4% vs price)
- **Breakeven TCE (scenario-invariant):** $334,603/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** TRIM/SHORT (overvalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Escalation | 25% | 1.25× | $16.58 | $19.63 | $18.95–$20.43 | 8.44× | 0.70 | $26.76 | $337,500 | 1.01× |
| Pre-MoU baseline | 45% | 1.11× | $14.55 | $16.23 | $15.84–$16.67 | 4.74× | 0.70 | $20.14 | $189,500 | 0.57× |
| MoU base case | 18% | 0.74× | $9.19 | $9.89 | $9.65–$10.10 | 2.12× | 0.70 | $11.51 | $84,875 | 0.25× |
| MoU bear | 12% | 0.70× | $8.51 | $9.07 | $8.90–$9.25 | 1.63× | 0.70 | $10.38 | $65,250 | 0.20× |
| **Probability-weighted** | | | | **$15.08** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $+2.98
- **Downside (worst scenario − price):** $-7.58
- **Expected value vs current** (weighted FV − price): $-1.57 (-9.4%)
- **Position:** TRIM/SHORT (overvalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
