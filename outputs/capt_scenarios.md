# CAPT — Scenario Fair Value (three-phase MoU framework)

- **Current price:** $12.79
- **Analyst target:** $18.90
- **NAV / share (reference, unflexed):** $15.03 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $16.77 (+31.1% vs price)
- **Breakeven TCE (scenario-invariant):** $0/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** BUY (undervalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Escalation | 25% | 1.25× | $21.93 | $23.95 | $23.17–$24.84 | 7.04× | 0.70 | $28.65 | $248,485 | 104718886491544283981117652992.00× |
| Pre-MoU baseline | 45% | 1.11× | $18.04 | $18.90 | $18.42–$19.43 | 4.15× | 0.70 | $20.91 | $145,663 | 61386842960494855746693890048.00× |
| MoU base case | 18% | 0.75× | $8.16 | $8.04 | $7.79–$8.28 | 1.90× | 0.70 | $7.76 | $66,585 | 28060778417353765300662697984.00× |
| MoU bear | 12% | 0.71× | $6.91 | $6.95 | $6.68–$7.22 | 1.50× | 0.60 | $7.01 | $52,268 | 22027330539227229890526838784.00× |
| **Probability-weighted** | | | | **$16.77** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $+11.16
- **Downside (worst scenario − price):** $-5.84
- **Expected value vs current** (weighted FV − price): $+3.98 (+31.1%)
- **Position:** BUY (undervalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
