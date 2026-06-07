# NAT — Scenario Fair Value (three-phase MoU framework)

- **Current price:** $5.20
- **Analyst target:** $6.00
- **NAV / share (reference, unflexed):** $2.63 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $2.28 (-56.1% vs price)
- **Breakeven TCE (scenario-invariant):** $287,175/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** TRIM/SHORT (overvalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Escalation | 10% | 1.25× | $3.80 | $4.79 | $4.52–$5.10 | 5.36× | 0.70 | $7.07 | $148,750 | 0.52× |
| Pre-MoU baseline | 15% | 1.11× | $3.15 | $3.74 | $3.56–$3.93 | 3.63× | 0.70 | $5.12 | $100,750 | 0.35× |
| MoU base case | 50% | 0.77× | $1.55 | $1.72 | $1.62–$1.81 | 1.73× | 0.70 | $2.09 | $47,875 | 0.17× |
| MoU bear | 25% | 0.73× | $1.38 | $1.54 | $1.43–$1.64 | 1.48× | 0.60 | $1.77 | $41,000 | 0.14× |
| **Probability-weighted** | | | | **$2.28** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $-0.41
- **Downside (worst scenario − price):** $-3.66
- **Expected value vs current** (weighted FV − price): $-2.92 (-56.1%)
- **Position:** TRIM/SHORT (overvalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
