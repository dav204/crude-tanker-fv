# HAFN — Scenario Fair Value (product margin / glut framework)

- **Current price:** $9.38
- **Analyst target:** $10.00
- **NAV / share (reference, unflexed):** $4.64 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $5.47 (-41.7% vs price)
- **Breakeven TCE (scenario-invariant):** $199,301/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** TRIM/SHORT (overvalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| refinery_squeeze | 25% | 1.25× | $6.25 | $7.69 | $7.22–$8.24 | 4.13× | 0.70 | $11.05 | $94,143 | 0.47× |
| moderate_correction | 30% | 1.22× | $6.06 | $6.67 | $6.37–$7.00 | 2.63× | 0.70 | $8.08 | $58,011 | 0.29× |
| Glut base case | 30% | 0.83× | $3.52 | $3.61 | $3.39–$3.87 | 1.33× | 0.60 | $3.75 | $26,100 | 0.13× |
| demand_softening | 15% | 0.76× | $3.10 | $3.08 | $2.86–$3.33 | 1.05× | 0.50 | $3.06 | $20,944 | 0.11× |
| structural_decline | 0% | 0.65× | $2.37 | $2.28 | $2.08–$2.49 | 0.89× | 0.50 | $2.18 | $17,661 | 0.09× |
| **Probability-weighted** | | | | **$5.47** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $-1.69
- **Downside (worst scenario − price):** $-7.10
- **Expected value vs current** (weighted FV − price): $-3.91 (-41.7%)
- **Position:** TRIM/SHORT (overvalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
