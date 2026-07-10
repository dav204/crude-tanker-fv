# ASC — Scenario Fair Value (product margin / glut framework)

- **Current price:** $15.32
- **Analyst target:** $17.95
- **NAV / share (reference, unflexed):** $17.80 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $16.28 (+6.3% vs price)
- **Breakeven TCE (scenario-invariant):** $11,815/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** BUY (undervalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| refinery_squeeze | 15% | 1.16× | $20.31 | $19.77 | $19.20–$20.43 | 2.23× | 0.70 | $18.50 | $35,750 | 3.03× |
| moderate_correction | 25% | 1.04× | $18.47 | $17.63 | $17.23–$18.12 | 1.72× | 0.70 | $15.69 | $27,500 | 2.33× |
| Glut base case | 45% | 0.93× | $16.66 | $15.38 | $14.94–$15.92 | 1.34× | 0.60 | $13.45 | $21,500 | 1.82× |
| demand_softening | 15% | 0.82× | $15.07 | $13.25 | $12.82–$13.75 | 1.02× | 0.50 | $11.42 | $16,250 | 1.38× |
| structural_decline | 0% | 0.70× | $13.16 | $11.32 | $10.93–$11.79 | 0.88× | 0.50 | $9.48 | $14,000 | 1.18× |
| **Probability-weighted** | | | | **$16.28** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $+4.45
- **Downside (worst scenario − price):** $-4.00
- **Expected value vs current** (weighted FV − price): $+0.96 (+6.3%)
- **Position:** BUY (undervalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
