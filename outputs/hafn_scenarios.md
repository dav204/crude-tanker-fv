# HAFN — Scenario Fair Value (product margin / glut framework)

- **Current price:** $7.65
- **Analyst target:** $10.00
- **NAV / share (reference, unflexed):** $5.57 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $6.23 (-18.6% vs price)
- **Breakeven TCE (scenario-invariant):** $98,762/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** TRIM/SHORT (overvalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| refinery_squeeze | 25% | 1.25× | $7.22 | $8.87 | $8.33–$9.49 | 4.45× | 0.70 | $12.72 | $102,177 | 1.03× |
| moderate_correction | 30% | 1.15× | $6.59 | $7.31 | $6.99–$7.69 | 2.79× | 0.70 | $9.00 | $62,209 | 0.63× |
| Glut base case | 30% | 0.79× | $4.15 | $4.21 | $3.96–$4.48 | 1.33× | 0.60 | $4.29 | $26,733 | 0.27× |
| demand_softening | 15% | 0.73× | $3.79 | $3.70 | $3.45–$3.96 | 1.06× | 0.50 | $3.60 | $21,590 | 0.22× |
| structural_decline | 0% | 0.65× | $3.26 | $3.06 | $2.84–$3.29 | 0.89× | 0.50 | $2.85 | $18,165 | 0.18× |
| **Probability-weighted** | | | | **$6.23** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $+1.22
- **Downside (worst scenario − price):** $-4.59
- **Expected value vs current** (weighted FV − price): $-1.42 (-18.6%)
- **Position:** TRIM/SHORT (overvalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
