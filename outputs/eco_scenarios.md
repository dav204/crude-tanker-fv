# ECO — Scenario Fair Value (three-phase MoU framework)

- **Current price:** $49.88
- **Analyst target:** $45.00
- **NAV / share (reference, unflexed):** $32.16 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $38.18 (-23.5% vs price)
- **Breakeven TCE (scenario-invariant):** $326,486/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** TRIM/SHORT (overvalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Escalation | 25% | 1.25× | $43.90 | $53.40 | $50.65–$56.57 | 6.93× | 0.70 | $75.55 | $245,110 | 0.75× |
| Pre-MoU baseline | 45% | 1.11× | $37.34 | $41.93 | $40.28–$43.79 | 4.20× | 0.70 | $52.64 | $146,058 | 0.45× |
| MoU base case | 18% | 0.75× | $20.54 | $20.88 | $19.94–$21.77 | 1.93× | 0.70 | $21.67 | $66,764 | 0.20× |
| MoU bear | 12% | 0.71× | $18.52 | $18.34 | $17.59–$19.08 | 1.56× | 0.70 | $17.91 | $53,380 | 0.16× |
| **Probability-weighted** | | | | **$38.18** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $+3.52
- **Downside (worst scenario − price):** $-31.54
- **Expected value vs current** (weighted FV − price): $-11.70 (-23.5%)
- **Position:** TRIM/SHORT (overvalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
