# CAPT — Scenario Fair Value (three-phase MoU framework)

- **Current price:** $19.71
- **Analyst target:** $18.90
- **NAV / share (reference, unflexed):** $17.32 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $18.57 (-5.8% vs price)
- **Breakeven TCE (scenario-invariant):** $349,105/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** TRIM/SHORT (overvalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Escalation | 28% | 1.25× | $25.26 | $25.92 | $25.43–$26.48 | 7.18× | 0.70 | $27.45 | $257,867 | 0.74× |
| Pre-MoU baseline | 59% | 0.99× | $17.09 | $16.84 | $16.62–$17.07 | 2.58× | 0.70 | $16.23 | $91,518 | 0.26× |
| MoU base case | 0% | 0.89× | $13.96 | $13.73 | $13.53–$13.92 | 2.13× | 0.70 | $13.18 | $75,695 | 0.22× |
| MoU bear | 13% | 0.80× | $10.82 | $10.62 | $10.49–$10.76 | 1.53× | 0.70 | $10.16 | $54,436 | 0.16× |
| **Probability-weighted** | | | | **$18.57** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $+6.21
- **Downside (worst scenario − price):** $-9.09
- **Expected value vs current** (weighted FV − price): $-1.14 (-5.8%)
- **Position:** TRIM/SHORT (overvalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
