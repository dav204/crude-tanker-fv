# HAFN — Scenario Fair Value (product margin / glut framework)

- **Current price:** $8.47
- **Analyst target:** $10.00
- **NAV / share (reference, unflexed):** $4.64 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $5.59 (-34.0% vs price)
- **Breakeven TCE (scenario-invariant):** $159,436/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** TRIM/SHORT (overvalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| refinery_squeeze | 25% | 1.25× | $6.25 | $7.69 | $7.22–$8.24 | 4.13× | 0.70 | $11.05 | $94,143 | 0.59× |
| moderate_correction | 30% | 1.25× | $6.25 | $6.84 | $6.55–$7.17 | 2.63× | 0.70 | $8.21 | $58,011 | 0.36× |
| Glut base case | 30% | 0.86× | $3.71 | $3.77 | $3.55–$4.03 | 1.33× | 0.60 | $3.87 | $26,100 | 0.16× |
| demand_softening | 15% | 0.79× | $3.25 | $3.21 | $2.99–$3.45 | 1.05× | 0.50 | $3.16 | $20,944 | 0.13× |
| structural_decline | 0% | 0.67× | $2.48 | $2.37 | $2.17–$2.59 | 0.89× | 0.50 | $2.26 | $17,661 | 0.11× |
| **Probability-weighted** | | | | **$5.59** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $-0.78
- **Downside (worst scenario − price):** $-6.10
- **Expected value vs current** (weighted FV − price): $-2.88 (-34.0%)
- **Position:** TRIM/SHORT (overvalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
