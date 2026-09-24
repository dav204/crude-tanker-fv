# TNK — Scenario Fair Value (three-phase MoU framework)

- **Current price:** $94.54
- **Analyst target:** $75.00
- **NAV / share (reference, unflexed):** $84.60 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $87.59 (-7.3% vs price)
- **Breakeven TCE (scenario-invariant):** $192,341/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** TRIM/SHORT (overvalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Escalation | 28% | 1.25× | $97.07 | $102.30 | $99.65–$105.34 | 4.21× | 0.70 | $114.50 | $127,619 | 0.66× |
| Pre-MoU baseline | 59% | 1.00× | $84.60 | $84.09 | $82.61–$85.65 | 2.16× | 0.70 | $82.90 | $66,573 | 0.35× |
| MoU base case | 0% | 0.90× | $79.61 | $78.10 | $76.83–$79.36 | 1.76× | 0.70 | $74.56 | $54,058 | 0.28× |
| MoU bear | 13% | 0.80× | $74.63 | $71.81 | $70.58–$73.03 | 1.31× | 0.60 | $67.57 | $40,216 | 0.21× |
| **Probability-weighted** | | | | **$87.59** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $+7.76
- **Downside (worst scenario − price):** $-22.73
- **Expected value vs current** (weighted FV − price): $-6.95 (-7.3%)
- **Position:** TRIM/SHORT (overvalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
