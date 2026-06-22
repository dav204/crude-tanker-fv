# STNG — Scenario Fair Value (product margin / glut framework)

- **Current price:** $80.58
- **Analyst target:** $94.00
- **NAV / share (reference, unflexed):** $80.35 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $79.99 (-0.7% vs price)
- **Breakeven TCE (scenario-invariant):** $62,640/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** HOLD (fairly valued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| refinery_squeeze | 25% | 1.25× | $98.87 | $105.66 | $101.79–$110.17 | 4.98× | 0.70 | $121.51 | $123,868 | 1.98× |
| moderate_correction | 30% | 1.17× | $93.06 | $93.31 | $90.92–$96.02 | 3.03× | 0.70 | $93.87 | $73,542 | 1.17× |
| Glut base case | 30% | 0.76× | $62.87 | $58.60 | $56.85–$60.61 | 1.29× | 0.60 | $52.21 | $28,442 | 0.45× |
| demand_softening | 15% | 0.72× | $59.37 | $53.32 | $51.58–$55.24 | 1.04× | 0.50 | $47.28 | $23,333 | 0.37× |
| structural_decline | 0% | 0.65× | $54.43 | $47.75 | $46.20–$49.45 | 0.88× | 0.50 | $41.06 | $19,525 | 0.31× |
| **Probability-weighted** | | | | **$79.99** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $+25.08
- **Downside (worst scenario − price):** $-32.83
- **Expected value vs current** (weighted FV − price): $-0.59 (-0.7%)
- **Position:** HOLD (fairly valued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
