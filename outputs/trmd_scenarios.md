# TRMD — Scenario Fair Value (product margin / glut framework)

- **Current price:** $30.19
- **Analyst target:** $25.00
- **NAV / share (reference, unflexed):** $30.30 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $31.87 (+5.6% vs price)
- **Breakeven TCE (scenario-invariant):** $42,981/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** BUY (undervalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| refinery_squeeze | 25% | 1.25× | $39.48 | $45.34 | $42.98–$48.09 | 4.47× | 0.70 | $59.02 | $105,736 | 2.46× |
| moderate_correction | 30% | 1.16× | $36.10 | $37.95 | $36.51–$39.60 | 2.79× | 0.70 | $42.28 | $64,068 | 1.49× |
| Glut base case | 30% | 0.78× | $22.27 | $21.25 | $20.18–$22.47 | 1.31× | 0.60 | $19.71 | $27,013 | 0.63× |
| demand_softening | 15% | 0.73× | $20.32 | $18.47 | $17.40–$19.64 | 1.05× | 0.50 | $16.62 | $21,876 | 0.51× |
| structural_decline | 0% | 0.65× | $17.45 | $15.20 | $14.27–$16.24 | 0.88× | 0.50 | $12.94 | $18,388 | 0.43× |
| **Probability-weighted** | | | | **$31.87** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $+15.15
- **Downside (worst scenario − price):** $-14.99
- **Expected value vs current** (weighted FV − price): $+1.68 (+5.6%)
- **Position:** BUY (undervalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
