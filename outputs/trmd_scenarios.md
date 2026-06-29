# TRMD — Scenario Fair Value (product margin / glut framework)

- **Current price:** $26.31
- **Analyst target:** $25.00
- **NAV / share (reference, unflexed):** $25.43 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $27.32 (+3.8% vs price)
- **Breakeven TCE (scenario-invariant):** $48,537/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** HOLD (fairly valued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| refinery_squeeze | 25% | 1.25× | $34.45 | $40.58 | $38.25–$43.30 | 4.51× | 0.70 | $54.89 | $107,069 | 2.21× |
| moderate_correction | 30% | 1.16× | $31.17 | $33.30 | $31.87–$34.93 | 2.81× | 0.70 | $38.28 | $64,765 | 1.33× |
| Glut base case | 30% | 0.78× | $17.49 | $16.84 | $15.78–$18.04 | 1.31× | 0.60 | $15.85 | $27,118 | 0.56× |
| demand_softening | 15% | 0.73× | $15.59 | $14.21 | $13.17–$15.37 | 1.05× | 0.50 | $12.84 | $21,983 | 0.45× |
| structural_decline | 0% | 0.65× | $12.81 | $11.03 | $10.11–$12.05 | 0.88× | 0.50 | $9.25 | $18,472 | 0.38× |
| **Probability-weighted** | | | | **$27.32** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $+14.27
- **Downside (worst scenario − price):** $-15.28
- **Expected value vs current** (weighted FV − price): $+1.01 (+3.8%)
- **Position:** HOLD (fairly valued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
