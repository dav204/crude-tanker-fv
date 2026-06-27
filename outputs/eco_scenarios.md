# ECO — Scenario Fair Value (three-phase MoU framework)

- **Current price:** $49.88
- **Analyst target:** $45.00
- **NAV / share (reference, unflexed):** $33.88 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $39.59 (-20.6% vs price)
- **Breakeven TCE (scenario-invariant):** $304,990/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** TRIM/SHORT (overvalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Escalation | 25% | 1.25× | $46.06 | $55.11 | $52.36–$58.28 | 6.90× | 0.70 | $76.23 | $242,955 | 0.80× |
| Pre-MoU baseline | 45% | 1.11× | $39.25 | $43.45 | $41.80–$45.31 | 4.18× | 0.70 | $53.24 | $145,045 | 0.48× |
| MoU base case | 18% | 0.75× | $21.85 | $21.92 | $20.98–$22.81 | 1.92× | 0.70 | $22.09 | $66,342 | 0.22× |
| MoU bear | 12% | 0.71× | $19.76 | $19.32 | $18.58–$20.07 | 1.55× | 0.70 | $18.31 | $53,103 | 0.17× |
| **Probability-weighted** | | | | **$39.59** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $+5.23
- **Downside (worst scenario − price):** $-30.56
- **Expected value vs current** (weighted FV − price): $-10.29 (-20.6%)
- **Position:** TRIM/SHORT (overvalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
