# ASC — Scenario Fair Value (product margin / glut framework)

- **Current price:** $18.62
- **Analyst target:** $17.95
- **NAV / share (reference, unflexed):** $17.37 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $16.28 (-12.6% vs price)
- **Breakeven TCE (scenario-invariant):** $41,416/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** TRIM/SHORT (overvalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| refinery_squeeze | 25% | 1.10× | $19.16 | $19.42 | $18.74–$20.22 | 2.23× | 0.70 | $20.03 | $35,750 | 0.86× |
| moderate_correction | 30% | 0.99× | $17.17 | $17.03 | $16.54–$17.61 | 1.72× | 0.70 | $16.69 | $27,500 | 0.66× |
| Glut base case | 30% | 0.88× | $15.23 | $14.76 | $14.24–$15.41 | 1.34× | 0.60 | $14.06 | $21,500 | 0.52× |
| demand_softening | 15% | 0.79× | $13.51 | $12.60 | $12.08–$13.21 | 1.02× | 0.50 | $11.68 | $16,250 | 0.39× |
| structural_decline | 0% | 0.67× | $11.36 | $10.35 | $9.86–$10.91 | 0.88× | 0.50 | $9.33 | $14,000 | 0.34× |
| **Probability-weighted** | | | | **$16.28** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $+0.80
- **Downside (worst scenario − price):** $-8.28
- **Expected value vs current** (weighted FV − price): $-2.34 (-12.6%)
- **Position:** TRIM/SHORT (overvalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
