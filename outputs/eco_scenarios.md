# ECO — Scenario Fair Value (three-phase MoU framework)

- **Current price:** $47.70
- **Analyst target:** $45.00
- **NAV / share (reference, unflexed):** $39.93 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $32.53 (-31.8% vs price)
- **Breakeven TCE (scenario-invariant):** $207,393/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** TRIM/SHORT (overvalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Escalation | 10% | 1.25× | $53.62 | $61.59 | $59.21–$64.33 | 6.99× | 0.70 | $80.19 | $248,732 | 1.20× |
| Pre-MoU baseline | 15% | 1.10× | $45.43 | $49.10 | $47.70–$50.68 | 4.11× | 0.70 | $57.66 | $143,391 | 0.69× |
| MoU base case | 50% | 0.75× | $26.37 | $26.56 | $25.75–$27.34 | 1.94× | 0.70 | $27.02 | $67,474 | 0.33× |
| MoU bear | 25% | 0.70× | $23.36 | $22.90 | $22.09–$23.71 | 1.43× | 0.60 | $22.20 | $48,681 | 0.23× |
| **Probability-weighted** | | | | **$32.53** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $+13.89
- **Downside (worst scenario − price):** $-24.80
- **Expected value vs current** (weighted FV − price): $-15.17 (-31.8%)
- **Position:** TRIM/SHORT (overvalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
