# CAPT — Scenario Fair Value (three-phase MoU framework)

- **Current price:** $14.68
- **Analyst target:** $18.90
- **NAV / share (reference, unflexed):** $15.48 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $16.02 (+9.1% vs price)
- **Breakeven TCE (scenario-invariant):** $80,462/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** BUY (undervalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Escalation | 25% | 1.25× | $22.49 | $24.43 | $23.66–$25.32 | 7.00× | 0.70 | $28.97 | $246,259 | 3.06× |
| Pre-MoU baseline | 62% | 0.96× | $14.30 | $13.99 | $13.71–$14.30 | 2.32× | 0.70 | $13.27 | $81,132 | 1.01× |
| MoU base case | 0% | 0.86× | $11.59 | $11.17 | $10.92–$11.41 | 1.90× | 0.70 | $10.20 | $66,149 | 0.82× |
| MoU bear | 13% | 0.80× | $9.77 | $9.52 | $9.25–$9.79 | 1.50× | 0.60 | $9.15 | $51,983 | 0.65× |
| **Probability-weighted** | | | | **$16.02** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $+9.75
- **Downside (worst scenario − price):** $-5.16
- **Expected value vs current** (weighted FV − price): $+1.34 (+9.1%)
- **Position:** BUY (undervalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
