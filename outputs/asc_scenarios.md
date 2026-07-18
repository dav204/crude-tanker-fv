# ASC — Scenario Fair Value (product margin / glut framework)

- **Current price:** $15.40
- **Analyst target:** $17.95
- **NAV / share (reference, unflexed):** $17.82 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $16.85 (+9.4% vs price)
- **Breakeven TCE (scenario-invariant):** $12,385/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** BUY (undervalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| refinery_squeeze | 25% | 1.16× | $20.33 | $19.79 | $19.22–$20.46 | 2.23× | 0.70 | $18.52 | $35,750 | 2.89× |
| moderate_correction | 30% | 1.04× | $18.49 | $17.65 | $17.25–$18.14 | 1.72× | 0.70 | $15.70 | $27,500 | 2.22× |
| Glut base case | 30% | 0.93× | $16.68 | $15.40 | $14.96–$15.94 | 1.34× | 0.60 | $13.46 | $21,500 | 1.74× |
| demand_softening | 15% | 0.82× | $15.09 | $13.26 | $12.83–$13.77 | 1.02× | 0.50 | $11.43 | $16,250 | 1.31× |
| structural_decline | 0% | 0.70× | $13.18 | $11.34 | $10.94–$11.80 | 0.87× | 0.50 | $9.49 | $14,000 | 1.13× |
| **Probability-weighted** | | | | **$16.85** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $+4.39
- **Downside (worst scenario − price):** $-4.06
- **Expected value vs current** (weighted FV − price): $+1.45 (+9.4%)
- **Position:** BUY (undervalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
