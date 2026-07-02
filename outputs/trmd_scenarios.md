# TRMD — Scenario Fair Value (product margin / glut framework)

- **Current price:** $26.06
- **Analyst target:** $25.00
- **NAV / share (reference, unflexed):** $30.34 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $31.90 (+22.4% vs price)
- **Breakeven TCE (scenario-invariant):** $12,733/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** BUY (undervalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| refinery_squeeze | 25% | 1.25× | $39.53 | $45.39 | $43.03–$48.13 | 4.48× | 0.70 | $59.05 | $105,995 | 8.32× |
| moderate_correction | 30% | 1.16× | $36.16 | $38.00 | $36.55–$39.65 | 2.79× | 0.70 | $42.30 | $64,204 | 5.04× |
| Glut base case | 30% | 0.78× | $22.29 | $21.26 | $20.19–$22.49 | 1.31× | 0.60 | $19.72 | $27,034 | 2.12× |
| demand_softening | 15% | 0.73× | $20.34 | $18.49 | $17.42–$19.66 | 1.05× | 0.50 | $16.63 | $21,897 | 1.72× |
| structural_decline | 0% | 0.65× | $17.48 | $15.22 | $14.29–$16.26 | 0.88× | 0.50 | $12.96 | $18,404 | 1.45× |
| **Probability-weighted** | | | | **$31.90** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $+19.33
- **Downside (worst scenario − price):** $-10.84
- **Expected value vs current** (weighted FV − price): $+5.84 (+22.4%)
- **Position:** BUY (undervalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
