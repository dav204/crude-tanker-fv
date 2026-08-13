# TNK — Scenario Fair Value (three-phase MoU framework)

- **Current price:** $80.89
- **Analyst target:** $75.00
- **NAV / share (reference, unflexed):** $84.60 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $83.72 (+3.5% vs price)
- **Breakeven TCE (scenario-invariant):** $49,193/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** HOLD (fairly valued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Escalation | 25% | 1.25× | $97.07 | $102.30 | $99.65–$105.34 | 4.21× | 0.70 | $114.50 | $127,619 | 2.59× |
| Pre-MoU baseline | 57% | 0.93× | $81.07 | $79.05 | $77.93–$80.23 | 1.67× | 0.70 | $74.35 | $50,962 | 1.04× |
| MoU base case | 5% | 0.86× | $77.68 | $74.87 | $73.52–$76.22 | 1.42× | 0.60 | $70.65 | $43,568 | 0.89× |
| MoU bear | 13% | 0.81× | $75.28 | $71.90 | $70.77–$73.04 | 1.22× | 0.60 | $66.83 | $37,440 | 0.76× |
| **Probability-weighted** | | | | **$83.72** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $+21.41
- **Downside (worst scenario − price):** $-8.99
- **Expected value vs current** (weighted FV − price): $+2.83 (+3.5%)
- **Position:** HOLD (fairly valued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
