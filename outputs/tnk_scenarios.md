# TNK — Scenario Fair Value (three-phase MoU framework)

- **Current price:** $85.13
- **Analyst target:** $75.00
- **NAV / share (reference, unflexed):** $84.60 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $83.93 (-1.4% vs price)
- **Breakeven TCE (scenario-invariant):** $93,157/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** HOLD (fairly valued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Escalation | 25% | 1.25× | $97.07 | $102.30 | $99.65–$105.34 | 4.21× | 0.70 | $114.50 | $127,619 | 1.37× |
| Pre-MoU baseline | 62% | 0.93× | $81.07 | $79.05 | $77.93–$80.23 | 1.67× | 0.70 | $74.35 | $50,962 | 0.55× |
| MoU base case | 0% | 0.86× | $77.68 | $74.87 | $73.52–$76.22 | 1.42× | 0.60 | $70.65 | $43,568 | 0.47× |
| MoU bear | 13% | 0.81× | $75.28 | $71.90 | $70.77–$73.04 | 1.22× | 0.60 | $66.83 | $37,440 | 0.40× |
| **Probability-weighted** | | | | **$83.93** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $+17.17
- **Downside (worst scenario − price):** $-13.23
- **Expected value vs current** (weighted FV − price): $-1.20 (-1.4%)
- **Position:** HOLD (fairly valued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
