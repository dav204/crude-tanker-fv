# ASC — Scenario Fair Value (scenario framework)

- **Current price:** $16.00
- **Analyst target:** $17.95
- **NAV / share (reference, unflexed):** $15.96 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $14.50 (-9.4% vs price)
- **Breakeven TCE (scenario-invariant):** $38,252/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** TRIM/SHORT (overvalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| refinery_squeeze | 15% | 1.16× | $18.62 | $18.08 | $17.67–$18.57 | 2.23× | 0.70 | $16.82 | $35,750 | 0.93× |
| moderate_correction | 25% | 1.04× | $16.67 | $15.94 | $15.65–$16.30 | 1.72× | 0.70 | $14.25 | $27,500 | 0.72× |
| Glut base case | 45% | 0.93× | $14.76 | $13.57 | $13.25–$13.96 | 1.34× | 0.60 | $11.77 | $21,500 | 0.56× |
| demand_softening | 15% | 0.82× | $13.08 | $11.33 | $11.07–$11.70 | 1.02× | 0.50 | $9.58 | $16,250 | 0.42× |
| structural_decline | 0% | 0.70× | $11.05 | $9.43 | $9.30–$9.73 | 0.88× | 0.50 | $7.80 | $14,000 | 0.37× |
| **Probability-weighted** | | | | **$14.50** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $+2.08
- **Downside (worst scenario − price):** $-6.57
- **Expected value vs current** (weighted FV − price): $-1.50 (-9.4%)
- **Position:** TRIM/SHORT (overvalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
