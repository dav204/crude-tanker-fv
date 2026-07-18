# DHT — Scenario Fair Value (three-phase MoU framework)

- **Current price:** $17.41
- **Analyst target:** $16.00
- **NAV / share (reference, unflexed):** $13.58 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $13.10 (-24.8% vs price)
- **Breakeven TCE (scenario-invariant):** $354,792/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** TRIM/SHORT (overvalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Escalation | 25% | 1.25× | $17.48 | $20.25 | $19.53–$21.08 | 8.44× | 0.70 | $26.70 | $337,500 | 0.95× |
| Pre-MoU baseline | 45% | 0.82× | $10.71 | $11.37 | $11.10–$11.65 | 2.65× | 0.70 | $12.91 | $106,100 | 0.30× |
| MoU base case | 18% | 0.74× | $9.59 | $10.07 | $9.82–$10.29 | 2.12× | 0.70 | $11.20 | $84,875 | 0.24× |
| MoU bear | 12% | 0.70× | $8.86 | $9.22 | $9.04–$9.40 | 1.63× | 0.70 | $10.06 | $65,250 | 0.18× |
| **Probability-weighted** | | | | **$13.10** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $+2.84
- **Downside (worst scenario − price):** $-8.19
- **Expected value vs current** (weighted FV − price): $-4.31 (-24.8%)
- **Position:** TRIM/SHORT (overvalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
