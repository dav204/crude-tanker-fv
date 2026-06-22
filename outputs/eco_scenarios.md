# ECO — Scenario Fair Value (three-phase MoU framework)

- **Current price:** $52.48
- **Analyst target:** $45.00
- **NAV / share (reference, unflexed):** $33.71 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $39.41 (-24.9% vs price)
- **Breakeven TCE (scenario-invariant):** $343,849/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** TRIM/SHORT (overvalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Escalation | 25% | 1.25× | $45.84 | $54.89 | $52.14–$58.06 | 6.89× | 0.70 | $75.99 | $242,625 | 0.71× |
| Pre-MoU baseline | 45% | 1.11× | $39.06 | $43.25 | $41.61–$45.11 | 4.18× | 0.70 | $53.03 | $144,890 | 0.42× |
| MoU base case | 18% | 0.75× | $21.72 | $21.79 | $20.85–$22.68 | 1.92× | 0.70 | $21.95 | $66,277 | 0.19× |
| MoU bear | 12% | 0.71× | $19.64 | $19.20 | $18.45–$19.95 | 1.55× | 0.70 | $18.17 | $53,061 | 0.15× |
| **Probability-weighted** | | | | **$39.41** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $+2.41
- **Downside (worst scenario − price):** $-33.28
- **Expected value vs current** (weighted FV − price): $-13.07 (-24.9%)
- **Position:** TRIM/SHORT (overvalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
