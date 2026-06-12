# TNK — Scenario Fair Value (three-phase MoU framework)

- **Current price:** $72.50
- **Analyst target:** $75.00
- **NAV / share (reference, unflexed):** $77.45 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $73.70 (+1.7% vs price)
- **Breakeven TCE (scenario-invariant):** $39,706/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** HOLD (fairly valued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Escalation | 25% | 1.25× | $88.93 | $85.68 | $84.96–$86.51 | 4.23× | 0.70 | $78.11 | $134,449 | 3.39× |
| Pre-MoU baseline | 45% | 1.04× | $79.35 | $75.81 | $75.35–$76.33 | 2.82× | 0.70 | $67.57 | $89,216 | 2.25× |
| MoU base case | 18% | 0.75× | $66.15 | $61.21 | $60.85–$61.58 | 1.41× | 0.60 | $53.81 | $44,893 | 1.13× |
| MoU bear | 12% | 0.72× | $64.54 | $59.57 | $59.27–$59.88 | 1.20× | 0.60 | $52.12 | $38,243 | 0.96× |
| **Probability-weighted** | | | | **$73.70** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $+13.18
- **Downside (worst scenario − price):** $-12.93
- **Expected value vs current** (weighted FV − price): $+1.20 (+1.7%)
- **Position:** HOLD (fairly valued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
