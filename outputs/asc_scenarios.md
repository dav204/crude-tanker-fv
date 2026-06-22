# ASC — Scenario Fair Value (product margin / glut framework)

- **Current price:** $17.07
- **Analyst target:** $17.95
- **NAV / share (reference, unflexed):** $15.93 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $15.15 (-11.3% vs price)
- **Breakeven TCE (scenario-invariant):** $41,676/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** TRIM/SHORT (overvalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| refinery_squeeze | 25% | 1.16× | $18.59 | $18.21 | $17.61–$18.91 | 2.23× | 0.70 | $17.30 | $35,750 | 0.86× |
| moderate_correction | 30% | 1.04× | $16.64 | $15.95 | $15.53–$16.46 | 1.72× | 0.70 | $14.34 | $27,500 | 0.66× |
| Glut base case | 30% | 0.93× | $14.74 | $13.64 | $13.18–$14.21 | 1.34× | 0.60 | $11.99 | $21,500 | 0.52× |
| demand_softening | 15% | 0.82× | $13.06 | $11.46 | $11.00–$11.99 | 1.02× | 0.50 | $9.85 | $16,250 | 0.39× |
| structural_decline | 0% | 0.70× | $11.04 | $9.42 | $9.00–$9.91 | 0.88× | 0.50 | $7.81 | $14,000 | 0.34× |
| **Probability-weighted** | | | | **$15.15** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $+1.14
- **Downside (worst scenario − price):** $-7.65
- **Expected value vs current** (weighted FV − price): $-1.92 (-11.3%)
- **Position:** TRIM/SHORT (overvalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
