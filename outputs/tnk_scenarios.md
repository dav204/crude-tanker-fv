# TNK — Scenario Fair Value (three-phase MoU framework)

- **Current price:** $79.95
- **Analyst target:** $75.00
- **NAV / share (reference, unflexed):** $81.48 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $76.95 (-3.8% vs price)
- **Breakeven TCE (scenario-invariant):** $54,688/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** HOLD (fairly valued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Escalation | 25% | 1.25× | $93.96 | $99.39 | $96.74–$102.44 | 4.21× | 0.70 | $112.08 | $127,619 | 2.33× |
| Pre-MoU baseline | 57% | 0.80× | $71.73 | $70.63 | $69.51–$71.82 | 1.67× | 0.70 | $68.08 | $50,962 | 0.93× |
| MoU base case | 5% | 0.76× | $69.32 | $67.52 | $66.17–$68.87 | 1.42× | 0.60 | $64.81 | $43,568 | 0.80× |
| MoU bear | 13% | 0.72× | $67.62 | $65.15 | $64.01–$66.28 | 1.22× | 0.60 | $61.44 | $37,440 | 0.68× |
| **Probability-weighted** | | | | **$76.95** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $+19.44
- **Downside (worst scenario − price):** $-14.81
- **Expected value vs current** (weighted FV − price): $-3.00 (-3.8%)
- **Position:** HOLD (fairly valued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
