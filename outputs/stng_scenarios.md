# STNG — Scenario Fair Value (product margin / glut framework)

- **Current price:** $75.60
- **Analyst target:** $94.00
- **NAV / share (reference, unflexed):** $80.35 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $73.13 (-3.3% vs price)
- **Breakeven TCE (scenario-invariant):** $2,725,019/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** HOLD (fairly valued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| refinery_squeeze | 25% | 1.25× | $98.87 | $90.78 | $90.78–$90.78 | 4.98× | 0.70 | $71.91 | $123,868 | 0.05× |
| moderate_correction | 30% | 1.17× | $93.06 | $85.52 | $85.52–$85.52 | 3.03× | 0.70 | $67.92 | $73,542 | 0.03× |
| Glut base case | 30% | 0.76× | $62.87 | $56.57 | $56.57–$56.57 | 1.29× | 0.60 | $47.13 | $28,442 | 0.01× |
| demand_softening | 15% | 0.72× | $59.37 | $52.04 | $52.04–$52.04 | 1.04× | 0.50 | $44.72 | $23,333 | 0.01× |
| structural_decline | 0% | 0.65× | $54.43 | $47.88 | $47.88–$47.88 | 0.88× | 0.50 | $41.32 | $19,525 | 0.01× |
| **Probability-weighted** | | | | **$73.13** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $+15.18
- **Downside (worst scenario − price):** $-27.72
- **Expected value vs current** (weighted FV − price): $-2.47 (-3.3%)
- **Position:** HOLD (fairly valued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
