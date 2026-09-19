# TRMD — Scenario Fair Value (product margin / glut framework)

- **Current price:** $38.23
- **Analyst target:** $25.00
- **NAV / share (reference, unflexed):** $32.30 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $35.14 (-8.1% vs price)
- **Breakeven TCE (scenario-invariant):** $85,226/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** TRIM/SHORT (overvalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| refinery_squeeze | 25% | 1.25× | $41.82 | $47.75 | $45.34–$50.56 | 4.28× | 0.70 | $61.59 | $100,485 | 1.18× |
| moderate_correction | 30% | 1.23× | $40.93 | $42.53 | $41.05–$44.23 | 2.70× | 0.70 | $46.27 | $61,324 | 0.72× |
| Glut base case | 30% | 0.82× | $25.42 | $24.27 | $23.15–$25.55 | 1.31× | 0.60 | $22.53 | $26,600 | 0.31× |
| demand_softening | 15% | 0.76× | $23.08 | $21.09 | $19.99–$22.32 | 1.04× | 0.50 | $19.11 | $21,454 | 0.25× |
| structural_decline | 0% | 0.65× | $18.98 | $16.73 | $15.75–$17.81 | 0.88× | 0.50 | $14.48 | $18,059 | 0.21× |
| **Probability-weighted** | | | | **$35.14** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $+9.52
- **Downside (worst scenario − price):** $-21.50
- **Expected value vs current** (weighted FV − price): $-3.09 (-8.1%)
- **Position:** TRIM/SHORT (overvalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
