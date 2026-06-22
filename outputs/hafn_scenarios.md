# HAFN — Scenario Fair Value (product margin / glut framework)

- **Current price:** $7.23
- **Analyst target:** $10.00
- **NAV / share (reference, unflexed):** $5.22 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $5.91 (-18.2% vs price)
- **Breakeven TCE (scenario-invariant):** $95,336/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** TRIM/SHORT (overvalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| refinery_squeeze | 25% | 1.25× | $6.88 | $8.58 | $8.03–$9.21 | 4.45× | 0.70 | $12.52 | $102,307 | 1.07× |
| moderate_correction | 30% | 1.16× | $6.25 | $7.01 | $6.67–$7.39 | 2.79× | 0.70 | $8.77 | $62,277 | 0.65× |
| Glut base case | 30% | 0.78× | $3.78 | $3.87 | $3.63–$4.15 | 1.33× | 0.60 | $4.00 | $26,743 | 0.28× |
| demand_softening | 15% | 0.73× | $3.42 | $3.36 | $3.12–$3.63 | 1.06× | 0.50 | $3.31 | $21,600 | 0.23× |
| structural_decline | 0% | 0.65× | $2.89 | $2.72 | $2.50–$2.96 | 0.89× | 0.50 | $2.55 | $18,173 | 0.19× |
| **Probability-weighted** | | | | **$5.91** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $+1.35
- **Downside (worst scenario − price):** $-4.51
- **Expected value vs current** (weighted FV − price): $-1.32 (-18.2%)
- **Position:** TRIM/SHORT (overvalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
