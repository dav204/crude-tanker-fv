# HAFN — Scenario Fair Value (product margin / glut framework)

- **Current price:** $7.44
- **Analyst target:** $10.00
- **NAV / share (reference, unflexed):** $5.22 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $5.77 (-22.5% vs price)
- **Breakeven TCE (scenario-invariant):** $116,528/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** TRIM/SHORT (overvalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| refinery_squeeze | 25% | 1.25× | $6.88 | $8.28 | $7.83–$8.80 | 4.45× | 0.70 | $11.53 | $102,307 | 0.88× |
| moderate_correction | 30% | 1.16× | $6.25 | $6.88 | $6.61–$7.19 | 2.79× | 0.70 | $8.34 | $62,277 | 0.53× |
| Glut base case | 30% | 0.78× | $3.78 | $3.81 | $3.61–$4.04 | 1.33× | 0.60 | $3.85 | $26,743 | 0.23× |
| demand_softening | 15% | 0.73× | $3.42 | $3.26 | $3.06–$3.48 | 1.06× | 0.50 | $3.10 | $21,600 | 0.19× |
| structural_decline | 0% | 0.65× | $2.89 | $2.65 | $2.47–$2.84 | 0.89× | 0.50 | $2.41 | $18,173 | 0.16× |
| **Probability-weighted** | | | | **$5.77** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $+0.84
- **Downside (worst scenario − price):** $-4.79
- **Expected value vs current** (weighted FV − price): $-1.67 (-22.5%)
- **Position:** TRIM/SHORT (overvalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
