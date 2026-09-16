# TNK — Scenario Fair Value (three-phase MoU framework)

- **Current price:** $100.30
- **Analyst target:** $75.00
- **NAV / share (reference, unflexed):** $84.60 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $83.24 (-17.0% vs price)
- **Breakeven TCE (scenario-invariant):** $252,518/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** TRIM/SHORT (overvalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Escalation | 28% | 1.25× | $97.07 | $102.30 | $99.65–$105.34 | 4.21× | 0.70 | $114.50 | $127,619 | 0.51× |
| Pre-MoU baseline | 59% | 0.88× | $78.75 | $77.01 | $75.89–$78.19 | 1.67× | 0.70 | $72.93 | $50,962 | 0.20× |
| MoU base case | 0% | 0.82× | $75.74 | $73.20 | $71.85–$74.55 | 1.42× | 0.60 | $69.39 | $43,568 | 0.17× |
| MoU bear | 13% | 0.78× | $73.60 | $70.46 | $69.32–$71.59 | 1.22× | 0.60 | $65.74 | $37,440 | 0.15× |
| **Probability-weighted** | | | | **$83.24** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $+2.00
- **Downside (worst scenario − price):** $-29.84
- **Expected value vs current** (weighted FV − price): $-17.06 (-17.0%)
- **Position:** TRIM/SHORT (overvalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
