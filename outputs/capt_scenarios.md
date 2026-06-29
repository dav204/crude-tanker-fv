# CAPT — Scenario Fair Value (three-phase MoU framework)

- **Current price:** $12.79
- **Analyst target:** $18.90
- **NAV / share (reference, unflexed):** $11.58 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $13.62 (+6.5% vs price)
- **Breakeven TCE (scenario-invariant):** $127,839/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** BUY (undervalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Escalation | 25% | 1.25× | $17.62 | $20.11 | $19.34–$21.00 | 6.95× | 0.70 | $25.95 | $243,572 | 1.91× |
| Pre-MoU baseline | 45% | 1.11× | $14.20 | $15.49 | $15.02–$16.03 | 4.11× | 0.70 | $18.50 | $143,089 | 1.12× |
| MoU base case | 18% | 0.75× | $5.58 | $5.75 | $5.50–$5.99 | 1.89× | 0.70 | $6.14 | $65,512 | 0.51× |
| MoU bear | 12% | 0.71× | $4.48 | $4.85 | $4.58–$5.12 | 1.48× | 0.60 | $5.40 | $51,434 | 0.40× |
| **Probability-weighted** | | | | **$13.62** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $+7.32
- **Downside (worst scenario − price):** $-7.94
- **Expected value vs current** (weighted FV − price): $+0.83 (+6.5%)
- **Position:** BUY (undervalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
