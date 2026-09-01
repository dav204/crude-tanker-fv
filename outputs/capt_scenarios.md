# CAPT — Scenario Fair Value (three-phase MoU framework)

- **Current price:** $16.46
- **Analyst target:** $18.90
- **NAV / share (reference, unflexed):** $17.32 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $17.56 (+6.7% vs price)
- **Breakeven TCE (scenario-invariant):** $63,532/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** BUY (undervalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Escalation | 25% | 1.25× | $25.26 | $25.92 | $25.43–$26.48 | 7.18× | 0.70 | $27.45 | $257,867 | 4.06× |
| Pre-MoU baseline | 62% | 0.96× | $15.99 | $15.65 | $15.47–$15.85 | 2.36× | 0.70 | $14.86 | $84,322 | 1.33× |
| MoU base case | 0% | 0.86× | $12.87 | $12.62 | $12.45–$12.79 | 1.93× | 0.70 | $12.02 | $68,539 | 1.08× |
| MoU bear | 13% | 0.79× | $10.79 | $10.58 | $10.45–$10.72 | 1.51× | 0.70 | $10.08 | $53,686 | 0.85× |
| **Probability-weighted** | | | | **$17.56** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $+9.46
- **Downside (worst scenario − price):** $-5.88
- **Expected value vs current** (weighted FV − price): $+1.10 (+6.7%)
- **Position:** BUY (undervalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
