# FRO — Scenario Fair Value (three-phase MoU framework)

- **Current price:** $47.21
- **Analyst target:** $30.50
- **NAV / share (reference, unflexed):** $26.04 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $28.30 (-40.1% vs price)
- **Breakeven TCE (scenario-invariant):** $755,089/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** TRIM/SHORT (overvalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Escalation | 25% | 1.25× | $35.19 | $41.29 | $39.55–$43.30 | 7.70× | 0.70 | $55.53 | $283,063 | 0.37× |
| Pre-MoU baseline | 62% | 0.96× | $24.73 | $25.15 | $24.51–$25.82 | 2.47× | 0.70 | $26.11 | $90,381 | 0.12× |
| MoU base case | 0% | 0.86× | $20.98 | $21.11 | $20.51–$21.66 | 2.00× | 0.70 | $21.39 | $73,107 | 0.10× |
| MoU bear | 13% | 0.79× | $18.47 | $18.36 | $17.92–$18.80 | 1.55× | 0.70 | $18.10 | $56,366 | 0.07× |
| **Probability-weighted** | | | | **$28.30** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $-5.92
- **Downside (worst scenario − price):** $-28.85
- **Expected value vs current** (weighted FV − price): $-18.91 (-40.1%)
- **Position:** TRIM/SHORT (overvalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
