# NAT — Scenario Fair Value (three-phase MoU framework)

- **Current price:** $5.20
- **Analyst target:** $6.00
- **NAV / share (reference, unflexed):** $2.07 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $2.86 (-44.9% vs price)
- **Breakeven TCE (scenario-invariant):** $334,239/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** TRIM/SHORT (overvalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Escalation | 25% | 1.25× | $3.11 | $4.17 | $3.90–$4.48 | 5.36× | 0.70 | $6.65 | $148,750 | 0.45× |
| Pre-MoU baseline | 45% | 1.11× | $2.53 | $3.19 | $3.02–$3.39 | 3.63× | 0.70 | $4.75 | $100,750 | 0.30× |
| MoU base case | 18% | 0.77× | $1.12 | $1.34 | $1.24–$1.43 | 1.73× | 0.70 | $1.83 | $47,875 | 0.14× |
| MoU bear | 12% | 0.73× | $0.97 | $1.19 | $1.09–$1.30 | 1.48× | 0.60 | $1.52 | $41,000 | 0.12× |
| **Probability-weighted** | | | | **$2.86** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $-1.03
- **Downside (worst scenario − price):** $-4.01
- **Expected value vs current** (weighted FV − price): $-2.34 (-44.9%)
- **Position:** TRIM/SHORT (overvalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
