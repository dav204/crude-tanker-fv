# TRMD — Scenario Fair Value (product margin / glut framework)

- **Current price:** $32.62
- **Analyst target:** $25.00
- **NAV / share (reference, unflexed):** $32.30 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $35.79 (+9.7% vs price)
- **Breakeven TCE (scenario-invariant):** $43,444/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** BUY (undervalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| refinery_squeeze | 25% | 1.25× | $41.82 | $47.75 | $45.34–$50.56 | 4.28× | 0.70 | $61.59 | $100,485 | 2.31× |
| moderate_correction | 30% | 1.25× | $41.82 | $43.32 | $41.84–$45.02 | 2.70× | 0.70 | $46.83 | $61,324 | 1.41× |
| Glut base case | 30% | 0.85× | $26.56 | $25.25 | $24.14–$26.53 | 1.31× | 0.60 | $23.29 | $26,600 | 0.61× |
| demand_softening | 15% | 0.78× | $24.00 | $21.87 | $20.77–$23.10 | 1.04× | 0.50 | $19.75 | $21,454 | 0.49× |
| structural_decline | 0% | 0.66× | $19.46 | $17.14 | $16.16–$18.22 | 0.88× | 0.50 | $14.81 | $18,059 | 0.42× |
| **Probability-weighted** | | | | **$35.79** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $+15.13
- **Downside (worst scenario − price):** $-15.48
- **Expected value vs current** (weighted FV − price): $+3.17 (+9.7%)
- **Position:** BUY (undervalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
