# STNG — Scenario Fair Value (product margin / glut framework)

- **Current price:** $87.66
- **Analyst target:** $94.00
- **NAV / share (reference, unflexed):** $76.22 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $75.97 (-13.3% vs price)
- **Breakeven TCE (scenario-invariant):** $158,643/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** TRIM/SHORT (overvalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| refinery_squeeze | 25% | 1.25× | $91.49 | $92.63 | $90.21–$95.46 | 4.72× | 0.70 | $95.30 | $115,401 | 0.73× |
| moderate_correction | 30% | 1.25× | $91.49 | $88.46 | $86.94–$90.22 | 2.90× | 0.70 | $81.41 | $69,118 | 0.44× |
| Glut base case | 30% | 0.82× | $65.14 | $60.07 | $58.86–$61.48 | 1.30× | 0.60 | $52.48 | $27,775 | 0.18× |
| demand_softening | 15% | 0.76× | $61.56 | $55.01 | $53.81–$56.36 | 1.04× | 0.50 | $48.47 | $22,653 | 0.14× |
| structural_decline | 0% | 0.65× | $54.85 | $48.39 | $47.31–$49.60 | 0.88× | 0.50 | $41.94 | $18,994 | 0.12× |
| **Probability-weighted** | | | | **$75.97** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $+4.97
- **Downside (worst scenario − price):** $-39.27
- **Expected value vs current** (weighted FV − price): $-11.69 (-13.3%)
- **Position:** TRIM/SHORT (overvalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
