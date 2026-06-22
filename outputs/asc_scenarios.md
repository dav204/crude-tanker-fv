# ASC — Scenario Fair Value (product margin / glut framework)

- **Current price:** $17.07
- **Analyst target:** $17.95
- **NAV / share (reference, unflexed):** $15.93 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $15.05 (-11.8% vs price)
- **Breakeven TCE (scenario-invariant):** $51,701/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** TRIM/SHORT (overvalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| refinery_squeeze | 25% | 1.16× | $18.59 | $18.05 | $17.64–$18.54 | 2.23× | 0.70 | $16.80 | $35,750 | 0.69× |
| moderate_correction | 30% | 1.04× | $16.64 | $15.92 | $15.62–$16.27 | 1.72× | 0.70 | $14.23 | $27,500 | 0.53× |
| Glut base case | 30% | 0.93× | $14.74 | $13.54 | $13.23–$13.94 | 1.34× | 0.60 | $11.75 | $21,500 | 0.42× |
| demand_softening | 15% | 0.82× | $13.06 | $11.31 | $11.05–$11.68 | 1.02× | 0.50 | $9.56 | $16,250 | 0.31× |
| structural_decline | 0% | 0.70× | $11.04 | $9.41 | $9.29–$9.72 | 0.88× | 0.50 | $7.79 | $14,000 | 0.27× |
| **Probability-weighted** | | | | **$15.05** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $+0.98
- **Downside (worst scenario − price):** $-7.66
- **Expected value vs current** (weighted FV − price): $-2.02 (-11.8%)
- **Position:** TRIM/SHORT (overvalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
