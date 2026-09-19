# FRO — Scenario Fair Value (three-phase MoU framework)

- **Current price:** $51.42
- **Analyst target:** $30.50
- **NAV / share (reference, unflexed):** $26.04 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $29.38 (-42.9% vs price)
- **Breakeven TCE (scenario-invariant):** $886,430/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** TRIM/SHORT (overvalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Escalation | 28% | 1.25× | $35.19 | $41.29 | $39.55–$43.30 | 7.70× | 0.70 | $55.53 | $283,063 | 0.32× |
| Pre-MoU baseline | 59% | 0.99× | $25.66 | $26.15 | $25.48–$26.86 | 2.61× | 0.70 | $27.28 | $95,274 | 0.11× |
| MoU base case | 0% | 0.89× | $22.08 | $22.26 | $21.64–$22.85 | 2.16× | 0.70 | $22.69 | $79,076 | 0.09× |
| MoU bear | 13% | 0.79× | $18.50 | $18.37 | $17.93–$18.80 | 1.55× | 0.70 | $18.06 | $56,527 | 0.06× |
| **Probability-weighted** | | | | **$29.38** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $-10.13
- **Downside (worst scenario − price):** $-33.05
- **Expected value vs current** (weighted FV − price): $-22.04 (-42.9%)
- **Position:** TRIM/SHORT (overvalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
