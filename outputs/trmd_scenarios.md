# TRMD — Scenario Fair Value (product margin / glut framework)

- **Current price:** $28.86
- **Analyst target:** $25.00
- **NAV / share (reference, unflexed):** $30.34 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $28.65 (-0.7% vs price)
- **Breakeven TCE (scenario-invariant):** $33,189/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** HOLD (fairly valued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| refinery_squeeze | 15% | 1.25× | $39.53 | $45.39 | $43.03–$48.13 | 4.48× | 0.70 | $59.05 | $105,995 | 3.19× |
| moderate_correction | 25% | 1.16× | $36.16 | $38.00 | $36.55–$39.65 | 2.79× | 0.70 | $42.30 | $64,204 | 1.93× |
| Glut base case | 45% | 0.78× | $22.29 | $21.26 | $20.19–$22.49 | 1.31× | 0.60 | $19.72 | $27,034 | 0.81× |
| demand_softening | 15% | 0.73× | $20.34 | $18.49 | $17.42–$19.66 | 1.05× | 0.50 | $16.63 | $21,897 | 0.66× |
| structural_decline | 0% | 0.65× | $17.48 | $15.22 | $14.29–$16.26 | 0.88× | 0.50 | $12.96 | $18,404 | 0.55× |
| **Probability-weighted** | | | | **$28.65** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $+16.53
- **Downside (worst scenario − price):** $-13.64
- **Expected value vs current** (weighted FV − price): $-0.21 (-0.7%)
- **Position:** HOLD (fairly valued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
