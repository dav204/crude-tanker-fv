# ECO — Scenario Fair Value (three-phase MoU framework)

- **Current price:** $61.86
- **Analyst target:** $45.00
- **NAV / share (reference, unflexed):** $39.54 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $37.31 (-39.7% vs price)
- **Breakeven TCE (scenario-invariant):** $401,319/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** TRIM/SHORT (overvalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Escalation | 25% | 1.25× | $52.08 | $60.70 | $57.95–$63.87 | 6.91× | 0.70 | $80.80 | $244,039 | 0.61× |
| Pre-MoU baseline | 57% | 0.82× | $30.51 | $30.97 | $29.92–$32.08 | 2.36× | 0.70 | $32.04 | $81,874 | 0.20× |
| MoU base case | 5% | 0.75× | $27.13 | $26.84 | $25.90–$27.73 | 1.93× | 0.70 | $26.15 | $66,554 | 0.17× |
| MoU bear | 13% | 0.71× | $24.97 | $24.18 | $23.43–$24.93 | 1.56× | 0.70 | $22.32 | $53,242 | 0.13× |
| **Probability-weighted** | | | | **$37.31** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $-1.16
- **Downside (worst scenario − price):** $-37.68
- **Expected value vs current** (weighted FV − price): $-24.55 (-39.7%)
- **Position:** TRIM/SHORT (overvalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
