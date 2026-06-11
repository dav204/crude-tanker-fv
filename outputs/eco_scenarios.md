# ECO — Scenario Fair Value (three-phase MoU framework)

- **Current price:** $50.57
- **Analyst target:** $45.00
- **NAV / share (reference, unflexed):** $33.71 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $39.33 (-22.2% vs price)
- **Breakeven TCE (scenario-invariant):** $346,455/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** TRIM/SHORT (overvalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Escalation | 25% | 1.25× | $45.84 | $54.22 | $51.84–$56.97 | 6.89× | 0.70 | $73.77 | $242,625 | 0.70× |
| Pre-MoU baseline | 45% | 1.11× | $39.06 | $43.18 | $41.76–$44.79 | 4.18× | 0.70 | $52.80 | $144,890 | 0.42× |
| MoU base case | 18% | 0.75× | $21.72 | $22.16 | $21.35–$22.94 | 1.92× | 0.70 | $23.19 | $66,277 | 0.19× |
| MoU bear | 12% | 0.71× | $19.64 | $19.63 | $18.98–$20.27 | 1.55× | 0.70 | $19.59 | $53,061 | 0.15× |
| **Probability-weighted** | | | | **$39.33** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $+3.65
- **Downside (worst scenario − price):** $-30.94
- **Expected value vs current** (weighted FV − price): $-11.24 (-22.2%)
- **Position:** TRIM/SHORT (overvalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
