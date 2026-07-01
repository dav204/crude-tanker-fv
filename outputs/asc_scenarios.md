# ASC — Scenario Fair Value (product margin / glut framework)

- **Current price:** $16.00
- **Analyst target:** $17.95
- **NAV / share (reference, unflexed):** $17.80 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $16.83 (+5.2% vs price)
- **Breakeven TCE (scenario-invariant):** $18,010/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** BUY (undervalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| refinery_squeeze | 25% | 1.16× | $20.31 | $19.77 | $19.20–$20.43 | 2.23× | 0.70 | $18.50 | $35,750 | 1.98× |
| moderate_correction | 30% | 1.04× | $18.47 | $17.63 | $17.23–$18.12 | 1.72× | 0.70 | $15.69 | $27,500 | 1.53× |
| Glut base case | 30% | 0.93× | $16.66 | $15.38 | $14.94–$15.92 | 1.34× | 0.60 | $13.45 | $21,500 | 1.19× |
| demand_softening | 15% | 0.82× | $15.07 | $13.25 | $12.82–$13.75 | 1.02× | 0.50 | $11.42 | $16,250 | 0.90× |
| structural_decline | 0% | 0.70× | $13.16 | $11.32 | $10.93–$11.79 | 0.88× | 0.50 | $9.48 | $14,000 | 0.78× |
| **Probability-weighted** | | | | **$16.83** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $+3.77
- **Downside (worst scenario − price):** $-4.68
- **Expected value vs current** (weighted FV − price): $+0.83 (+5.2%)
- **Position:** BUY (undervalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
