# NAT — Scenario Fair Value (three-phase MoU framework)

- **Current price:** $5.85
- **Analyst target:** $6.00
- **NAV / share (reference, unflexed):** $2.07 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $2.78 (-52.5% vs price)
- **Breakeven TCE (scenario-invariant):** $404,139/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** TRIM/SHORT (overvalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Escalation | 25% | 1.25× | $3.11 | $4.07 | $3.80–$4.38 | 5.36× | 0.70 | $6.32 | $148,750 | 0.37× |
| Pre-MoU baseline | 45% | 1.11× | $2.53 | $3.10 | $2.93–$3.30 | 3.63× | 0.70 | $4.45 | $100,750 | 0.25× |
| MoU base case | 18% | 0.77× | $1.12 | $1.27 | $1.18–$1.37 | 1.73× | 0.70 | $1.63 | $47,875 | 0.12× |
| MoU bear | 12% | 0.73× | $0.97 | $1.15 | $1.05–$1.26 | 1.48× | 0.60 | $1.42 | $41,000 | 0.10× |
| **Probability-weighted** | | | | **$2.78** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $-1.78
- **Downside (worst scenario − price):** $-4.70
- **Expected value vs current** (weighted FV − price): $-3.07 (-52.5%)
- **Position:** TRIM/SHORT (overvalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
