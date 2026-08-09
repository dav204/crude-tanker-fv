# STNG — Scenario Fair Value (product margin / glut framework)

- **Current price:** $76.08
- **Analyst target:** $94.00
- **NAV / share (reference, unflexed):** $76.22 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $73.56 (-3.3% vs price)
- **Breakeven TCE (scenario-invariant):** $72,587/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** HOLD (fairly valued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| refinery_squeeze | 25% | 1.25× | $91.49 | $92.63 | $90.21–$95.46 | 4.72× | 0.70 | $95.30 | $115,401 | 1.59× |
| moderate_correction | 30% | 1.17× | $86.34 | $83.90 | $82.37–$85.65 | 2.90× | 0.70 | $78.22 | $69,118 | 0.95× |
| Glut base case | 30% | 0.77× | $62.26 | $57.60 | $56.39–$59.01 | 1.30× | 0.60 | $50.60 | $27,775 | 0.38× |
| demand_softening | 15% | 0.72× | $59.22 | $53.04 | $51.83–$54.38 | 1.04× | 0.50 | $46.86 | $22,653 | 0.31× |
| structural_decline | 0% | 0.65× | $54.85 | $48.39 | $47.31–$49.60 | 0.88× | 0.50 | $41.94 | $18,994 | 0.26× |
| **Probability-weighted** | | | | **$73.56** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $+16.55
- **Downside (worst scenario − price):** $-27.69
- **Expected value vs current** (weighted FV − price): $-2.52 (-3.3%)
- **Position:** HOLD (fairly valued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
