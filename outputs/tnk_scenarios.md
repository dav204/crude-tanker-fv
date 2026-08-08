# TNK — Scenario Fair Value (three-phase MoU framework)

- **Current price:** $77.25
- **Analyst target:** $75.00
- **NAV / share (reference, unflexed):** $84.60 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $79.87 (+3.4% vs price)
- **Breakeven TCE (scenario-invariant):** $8,968/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** HOLD (fairly valued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Escalation | 25% | 1.25× | $97.07 | $102.30 | $99.65–$105.34 | 4.21× | 0.70 | $114.50 | $127,619 | 14.23× |
| Pre-MoU baseline | 57% | 0.80× | $74.86 | $73.57 | $72.45–$74.75 | 1.67× | 0.70 | $70.55 | $50,962 | 5.68× |
| MoU base case | 5% | 0.76× | $72.46 | $70.39 | $69.04–$71.74 | 1.42× | 0.60 | $67.28 | $43,568 | 4.86× |
| MoU bear | 13% | 0.72× | $70.76 | $68.02 | $66.88–$69.16 | 1.22× | 0.60 | $63.91 | $37,440 | 4.17× |
| **Probability-weighted** | | | | **$79.87** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $+25.05
- **Downside (worst scenario − price):** $-9.23
- **Expected value vs current** (weighted FV − price): $+2.62 (+3.4%)
- **Position:** HOLD (fairly valued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
