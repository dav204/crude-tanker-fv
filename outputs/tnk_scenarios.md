# TNK — Scenario Fair Value (three-phase MoU framework)

- **Current price:** $70.80
- **Analyst target:** $75.00
- **NAV / share (reference, unflexed):** $77.49 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $73.74 (+4.1% vs price)
- **Breakeven TCE (scenario-invariant):** $0/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** HOLD (fairly valued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Escalation | 25% | 1.25× | $88.98 | $85.73 | $85.00–$86.56 | 4.23× | 0.70 | $78.14 | $134,462 | 80828652917818906266705068032.00× |
| Pre-MoU baseline | 45% | 1.04× | $79.39 | $75.85 | $75.38–$76.36 | 2.82× | 0.70 | $67.59 | $89,226 | 53636079707758463809688174592.00× |
| MoU base case | 18% | 0.75× | $66.18 | $61.24 | $60.87–$61.60 | 1.41× | 0.60 | $53.83 | $44,895 | 26987875093063146125188399104.00× |
| MoU bear | 12% | 0.72× | $64.57 | $59.60 | $59.29–$59.90 | 1.20× | 0.60 | $52.14 | $38,245 | 22990210439213473939660472320.00× |
| **Probability-weighted** | | | | **$73.74** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $+14.93
- **Downside (worst scenario − price):** $-11.20
- **Expected value vs current** (weighted FV − price): $+2.94 (+4.1%)
- **Position:** HOLD (fairly valued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
