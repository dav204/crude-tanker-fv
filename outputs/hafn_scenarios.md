# HAFN — Scenario Fair Value (product margin / glut framework)

- **Current price:** $7.02
- **Analyst target:** $10.00
- **NAV / share (reference, unflexed):** $5.57 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $5.61 (-20.1% vs price)
- **Breakeven TCE (scenario-invariant):** $79,286/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** TRIM/SHORT (overvalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| refinery_squeeze | 15% | 1.25× | $7.22 | $8.87 | $8.33–$9.49 | 4.45× | 0.70 | $12.71 | $102,307 | 1.29× |
| moderate_correction | 25% | 1.16× | $6.59 | $7.32 | $6.99–$7.69 | 2.79× | 0.70 | $9.00 | $62,277 | 0.79× |
| Glut base case | 45% | 0.78× | $4.15 | $4.21 | $3.96–$4.48 | 1.33× | 0.60 | $4.28 | $26,743 | 0.34× |
| demand_softening | 15% | 0.73× | $3.79 | $3.70 | $3.45–$3.96 | 1.06× | 0.50 | $3.60 | $21,600 | 0.27× |
| structural_decline | 0% | 0.65× | $3.26 | $3.06 | $2.84–$3.29 | 0.89× | 0.50 | $2.85 | $18,173 | 0.23× |
| **Probability-weighted** | | | | **$5.61** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $+1.85
- **Downside (worst scenario − price):** $-3.96
- **Expected value vs current** (weighted FV − price): $-1.41 (-20.1%)
- **Position:** TRIM/SHORT (overvalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
