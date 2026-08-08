# ASC — Scenario Fair Value (product margin / glut framework)

- **Current price:** $16.71
- **Analyst target:** $17.95
- **NAV / share (reference, unflexed):** $17.37 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $17.11 (+2.4% vs price)
- **Breakeven TCE (scenario-invariant):** $21,597/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** HOLD (fairly valued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| refinery_squeeze | 25% | 1.16× | $20.38 | $20.52 | $19.84–$21.32 | 2.23× | 0.70 | $20.85 | $35,750 | 1.66× |
| moderate_correction | 30% | 1.04× | $18.18 | $17.93 | $17.44–$18.51 | 1.72× | 0.70 | $17.36 | $27,500 | 1.27× |
| Glut base case | 30% | 0.93× | $16.02 | $15.46 | $14.93–$16.11 | 1.34× | 0.60 | $14.61 | $21,500 | 1.00× |
| demand_softening | 15% | 0.82× | $14.11 | $13.12 | $12.60–$13.73 | 1.02× | 0.50 | $12.12 | $16,250 | 0.75× |
| structural_decline | 0% | 0.70× | $11.82 | $10.75 | $10.26–$11.31 | 0.87× | 0.50 | $9.67 | $14,000 | 0.65× |
| **Probability-weighted** | | | | **$17.11** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $+3.81
- **Downside (worst scenario − price):** $-5.96
- **Expected value vs current** (weighted FV − price): $+0.40 (+2.4%)
- **Position:** HOLD (fairly valued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
