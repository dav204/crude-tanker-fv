# HAFN — Scenario Fair Value (product margin / glut framework)

- **Current price:** $7.49
- **Analyst target:** $10.00
- **NAV / share (reference, unflexed):** $5.56 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $6.56 (-12.5% vs price)
- **Breakeven TCE (scenario-invariant):** $95,853/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** TRIM/SHORT (overvalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| refinery_squeeze | 25% | 1.25× | $7.21 | $8.86 | $8.33–$9.48 | 4.45× | 0.70 | $12.71 | $102,092 | 1.07× |
| moderate_correction | 30% | 1.25× | $7.21 | $7.86 | $7.53–$8.24 | 2.79× | 0.70 | $9.38 | $62,164 | 0.65× |
| Glut base case | 30% | 0.86× | $4.62 | $4.60 | $4.36–$4.88 | 1.33× | 0.60 | $4.58 | $26,726 | 0.28× |
| demand_softening | 15% | 0.79× | $4.17 | $4.01 | $3.77–$4.28 | 1.06× | 0.50 | $3.85 | $21,583 | 0.23× |
| structural_decline | 0% | 0.67× | $3.37 | $3.15 | $2.93–$3.38 | 0.89× | 0.50 | $2.92 | $18,160 | 0.19× |
| **Probability-weighted** | | | | **$6.56** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $+1.37
- **Downside (worst scenario − price):** $-4.34
- **Expected value vs current** (weighted FV − price): $-0.93 (-12.5%)
- **Position:** TRIM/SHORT (overvalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
