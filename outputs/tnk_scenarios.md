# TNK — Scenario Fair Value (three-phase MoU framework)

- **Current price:** $100.92
- **Analyst target:** $75.00
- **NAV / share (reference, unflexed):** $84.60 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $87.59 (-13.2% vs price)
- **Breakeven TCE (scenario-invariant):** $259,053/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** TRIM/SHORT (overvalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Escalation | 28% | 1.25× | $97.07 | $102.30 | $99.65–$105.34 | 4.21× | 0.70 | $114.50 | $127,619 | 0.49× |
| Pre-MoU baseline | 59% | 1.00× | $84.60 | $84.09 | $82.61–$85.65 | 2.16× | 0.70 | $82.90 | $66,573 | 0.26× |
| MoU base case | 0% | 0.90× | $79.61 | $78.10 | $76.83–$79.36 | 1.76× | 0.70 | $74.56 | $54,058 | 0.21× |
| MoU bear | 13% | 0.80× | $74.63 | $71.81 | $70.58–$73.03 | 1.31× | 0.60 | $67.57 | $40,216 | 0.16× |
| **Probability-weighted** | | | | **$87.59** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $+1.38
- **Downside (worst scenario − price):** $-29.11
- **Expected value vs current** (weighted FV − price): $-13.33 (-13.2%)
- **Position:** TRIM/SHORT (overvalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
