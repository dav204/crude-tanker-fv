# TRMD — Scenario Fair Value (product margin / glut framework)

- **Current price:** $29.49
- **Analyst target:** $25.00
- **NAV / share (reference, unflexed):** $30.22 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $31.80 (+7.8% vs price)
- **Breakeven TCE (scenario-invariant):** $38,395/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** BUY (undervalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| refinery_squeeze | 25% | 1.25× | $39.37 | $45.25 | $42.89–$48.00 | 4.46× | 0.70 | $58.97 | $105,540 | 2.75× |
| moderate_correction | 30% | 1.16× | $36.00 | $37.87 | $36.42–$39.52 | 2.78× | 0.70 | $42.22 | $63,966 | 1.67× |
| Glut base case | 30% | 0.78× | $22.21 | $21.20 | $20.13–$22.42 | 1.31× | 0.60 | $19.68 | $26,998 | 0.70× |
| demand_softening | 15% | 0.73× | $20.26 | $18.42 | $17.36–$19.60 | 1.05× | 0.50 | $16.59 | $21,860 | 0.57× |
| structural_decline | 0% | 0.65× | $17.40 | $15.16 | $14.22–$16.20 | 0.88× | 0.50 | $12.91 | $18,376 | 0.48× |
| **Probability-weighted** | | | | **$31.80** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $+15.76
- **Downside (worst scenario − price):** $-14.33
- **Expected value vs current** (weighted FV − price): $+2.31 (+7.8%)
- **Position:** BUY (undervalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
