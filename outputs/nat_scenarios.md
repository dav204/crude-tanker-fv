# NAT — Scenario Fair Value (three-phase MoU framework)

- **Current price:** $8.25
- **Analyst target:** $6.00
- **NAV / share (reference, unflexed):** $2.76 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $3.24 (-60.8% vs price)
- **Breakeven TCE (scenario-invariant):** $898,495/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** TRIM/SHORT (overvalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Escalation | 28% | 1.25× | $3.69 | $4.43 | $4.20–$4.70 | 5.36× | 0.70 | $6.16 | $148,750 | 0.17× |
| Pre-MoU baseline | 59% | 1.00× | $2.76 | $2.93 | $2.82–$3.05 | 2.58× | 0.70 | $3.33 | $71,500 | 0.08× |
| MoU base case | 0% | 0.90× | $2.39 | $2.48 | $2.39–$2.58 | 2.10× | 0.70 | $2.70 | $58,250 | 0.06× |
| MoU bear | 13% | 0.80× | $2.02 | $2.03 | $1.96–$2.10 | 1.56× | 0.70 | $2.06 | $43,225 | 0.05× |
| **Probability-weighted** | | | | **$3.24** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $-3.82
- **Downside (worst scenario − price):** $-6.22
- **Expected value vs current** (weighted FV − price): $-5.01 (-60.8%)
- **Position:** TRIM/SHORT (overvalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
