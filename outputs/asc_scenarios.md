# ASC — Scenario Fair Value (product margin / glut framework)

- **Current price:** $16.38
- **Analyst target:** $17.95
- **NAV / share (reference, unflexed):** $15.93 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $15.05 (-8.1% vs price)
- **Breakeven TCE (scenario-invariant):** $43,209/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** TRIM/SHORT (overvalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| refinery_squeeze | 25% | 1.16× | $18.59 | $18.05 | $17.64–$18.54 | 2.23× | 0.70 | $16.80 | $35,750 | 0.83× |
| moderate_correction | 30% | 1.04× | $16.64 | $15.92 | $15.62–$16.27 | 1.72× | 0.70 | $14.23 | $27,500 | 0.64× |
| Glut base case | 30% | 0.93× | $14.74 | $13.54 | $13.23–$13.94 | 1.34× | 0.60 | $11.75 | $21,500 | 0.50× |
| demand_softening | 15% | 0.82× | $13.06 | $11.31 | $11.05–$11.68 | 1.02× | 0.50 | $9.56 | $16,250 | 0.38× |
| structural_decline | 0% | 0.70× | $11.04 | $9.41 | $9.29–$9.72 | 0.88× | 0.50 | $7.79 | $14,000 | 0.32× |
| **Probability-weighted** | | | | **$15.05** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $+1.67
- **Downside (worst scenario − price):** $-6.97
- **Expected value vs current** (weighted FV − price): $-1.33 (-8.1%)
- **Position:** TRIM/SHORT (overvalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
