# CAPT — Scenario Fair Value (three-phase MoU framework)

- **Current price:** $13.24
- **Analyst target:** $18.90
- **NAV / share (reference, unflexed):** $15.03 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $16.20 (+22.4% vs price)
- **Breakeven TCE (scenario-invariant):** $0/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** BUY (undervalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Escalation | 25% | 1.25× | $21.93 | $22.69 | $22.32–$23.12 | 7.04× | 0.70 | $24.46 | $248,485 | 104718886491544266388931608576.00× |
| Pre-MoU baseline | 45% | 1.11× | $18.04 | $18.31 | $18.09–$18.57 | 4.15× | 0.70 | $18.95 | $145,663 | 61386842960494846950600867840.00× |
| MoU base case | 18% | 0.75× | $8.16 | $8.14 | $8.03–$8.26 | 1.90× | 0.70 | $8.11 | $66,585 | 28060778417353760902616186880.00× |
| MoU bear | 12% | 0.71× | $6.91 | $6.86 | $6.73–$6.99 | 1.50× | 0.60 | $6.79 | $52,268 | 22027330539227225492480327680.00× |
| **Probability-weighted** | | | | **$16.20** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $+9.45
- **Downside (worst scenario − price):** $-6.38
- **Expected value vs current** (weighted FV − price): $+2.96 (+22.4%)
- **Position:** BUY (undervalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
