# STNG — Scenario Fair Value (product margin / glut framework)

- **Current price:** $76.08
- **Analyst target:** $94.00
- **NAV / share (reference, unflexed):** $76.42 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $73.73 (-3.1% vs price)
- **Breakeven TCE (scenario-invariant):** $71,456/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** HOLD (fairly valued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| refinery_squeeze | 25% | 1.25× | $91.74 | $92.85 | $90.42–$95.68 | 4.73× | 0.70 | $95.43 | $115,652 | 1.62× |
| moderate_correction | 30% | 1.17× | $86.58 | $84.11 | $82.59–$85.87 | 2.91× | 0.70 | $78.35 | $69,249 | 0.97× |
| Glut base case | 30% | 0.77× | $62.41 | $57.72 | $56.50–$59.13 | 1.30× | 0.60 | $50.68 | $27,795 | 0.39× |
| demand_softening | 15% | 0.72× | $59.35 | $53.14 | $51.94–$54.49 | 1.04× | 0.50 | $46.93 | $22,673 | 0.32× |
| structural_decline | 0% | 0.65× | $54.98 | $48.50 | $47.41–$49.70 | 0.88× | 0.50 | $42.02 | $19,010 | 0.27× |
| **Probability-weighted** | | | | **$73.73** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $+16.77
- **Downside (worst scenario − price):** $-27.58
- **Expected value vs current** (weighted FV − price): $-2.35 (-3.1%)
- **Position:** HOLD (fairly valued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
