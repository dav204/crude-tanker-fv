# BRUT — Scenario Fair Value (three-phase MoU framework)

- **Current price:** $5.27
- **Analyst target:** $4.56
- **NAV / share (reference, unflexed):** $4.92 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $5.51 (+4.6% vs price)
- **Breakeven TCE (scenario-invariant):** $254,855/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** HOLD (fairly valued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Escalation | 28% | 1.25× | $7.71 | $8.54 | $8.22–$8.92 | 8.44× | 0.70 | $10.48 | $337,500 | 1.32× |
| Pre-MoU baseline | 59% | 1.00× | $4.92 | $4.74 | $4.62–$4.87 | 2.78× | 0.70 | $4.33 | $111,200 | 0.44× |
| MoU base case | 0% | 0.90× | $3.80 | $3.58 | $3.48–$3.67 | 2.31× | 0.70 | $3.06 | $92,250 | 0.36× |
| MoU bear | 13% | 0.80× | $2.69 | $2.46 | $2.38–$2.54 | 1.64× | 0.70 | $1.93 | $65,775 | 0.26× |
| **Probability-weighted** | | | | **$5.51** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $+3.28
- **Downside (worst scenario − price):** $-2.81
- **Expected value vs current** (weighted FV − price): $+0.24 (+4.6%)
- **Position:** HOLD (fairly valued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
