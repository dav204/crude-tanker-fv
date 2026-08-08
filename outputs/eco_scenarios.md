# ECO — Scenario Fair Value (three-phase MoU framework)

- **Current price:** $61.86
- **Analyst target:** $45.00
- **NAV / share (reference, unflexed):** $34.42 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $32.57 (-47.4% vs price)
- **Breakeven TCE (scenario-invariant):** $466,032/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** TRIM/SHORT (overvalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Escalation | 25% | 1.25× | $46.73 | $55.63 | $52.88–$58.80 | 6.87× | 0.70 | $76.39 | $241,382 | 0.52× |
| Pre-MoU baseline | 57% | 0.82× | $25.57 | $26.31 | $25.26–$27.42 | 2.35× | 0.70 | $28.01 | $81,186 | 0.17× |
| MoU base case | 5% | 0.75× | $22.27 | $22.24 | $21.31–$23.14 | 1.92× | 0.70 | $22.19 | $66,033 | 0.14× |
| MoU bear | 13% | 0.71× | $20.16 | $19.63 | $18.88–$20.38 | 1.55× | 0.70 | $18.41 | $52,901 | 0.11× |
| **Probability-weighted** | | | | **$32.57** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $-6.23
- **Downside (worst scenario − price):** $-42.23
- **Expected value vs current** (weighted FV − price): $-29.29 (-47.4%)
- **Position:** TRIM/SHORT (overvalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
