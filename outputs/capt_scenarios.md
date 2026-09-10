# CAPT — Scenario Fair Value (three-phase MoU framework)

- **Current price:** $19.11
- **Analyst target:** $18.90
- **NAV / share (reference, unflexed):** $17.32 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $17.56 (-8.1% vs price)
- **Breakeven TCE (scenario-invariant):** $341,733/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** TRIM/SHORT (overvalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Escalation | 25% | 1.25× | $25.26 | $25.92 | $25.43–$26.48 | 7.18× | 0.70 | $27.45 | $257,867 | 0.75× |
| Pre-MoU baseline | 62% | 0.96× | $15.99 | $15.65 | $15.47–$15.85 | 2.36× | 0.70 | $14.86 | $84,322 | 0.25× |
| MoU base case | 0% | 0.86× | $12.87 | $12.62 | $12.45–$12.79 | 1.93× | 0.70 | $12.02 | $68,539 | 0.20× |
| MoU bear | 13% | 0.79× | $10.79 | $10.58 | $10.45–$10.72 | 1.51× | 0.70 | $10.08 | $53,686 | 0.16× |
| **Probability-weighted** | | | | **$17.56** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $+6.81
- **Downside (worst scenario − price):** $-8.53
- **Expected value vs current** (weighted FV − price): $-1.55 (-8.1%)
- **Position:** TRIM/SHORT (overvalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
