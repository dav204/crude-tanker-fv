# TNK — Scenario Fair Value (three-phase MoU framework)

- **Current price:** $96.31
- **Analyst target:** $75.00
- **NAV / share (reference, unflexed):** $84.60 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $82.48 (-14.4% vs price)
- **Breakeven TCE (scenario-invariant):** $210,849/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** TRIM/SHORT (overvalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Escalation | 25% | 1.25× | $97.07 | $102.30 | $99.65–$105.34 | 4.21× | 0.70 | $114.50 | $127,619 | 0.61× |
| Pre-MoU baseline | 62% | 0.88× | $78.75 | $77.01 | $75.89–$78.19 | 1.67× | 0.70 | $72.93 | $50,962 | 0.24× |
| MoU base case | 0% | 0.82× | $75.74 | $73.20 | $71.85–$74.55 | 1.42× | 0.60 | $69.39 | $43,568 | 0.21× |
| MoU bear | 13% | 0.78× | $73.60 | $70.46 | $69.32–$71.59 | 1.22× | 0.60 | $65.74 | $37,440 | 0.18× |
| **Probability-weighted** | | | | **$82.48** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $+5.99
- **Downside (worst scenario − price):** $-25.85
- **Expected value vs current** (weighted FV − price): $-13.83 (-14.4%)
- **Position:** TRIM/SHORT (overvalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
