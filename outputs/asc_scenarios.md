# ASC — Scenario Fair Value (product margin / glut framework)

- **Current price:** $17.36
- **Analyst target:** $17.95
- **NAV / share (reference, unflexed):** $17.37 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $16.38 (-5.7% vs price)
- **Breakeven TCE (scenario-invariant):** $28,607/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** TRIM/SHORT (overvalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| refinery_squeeze | 25% | 1.10× | $19.30 | $19.55 | $18.87–$20.35 | 2.23× | 0.70 | $20.12 | $35,750 | 1.25× |
| moderate_correction | 30% | 1.00× | $17.29 | $17.13 | $16.64–$17.71 | 1.72× | 0.70 | $16.77 | $27,500 | 0.96× |
| Glut base case | 30% | 0.89× | $15.32 | $14.84 | $14.32–$15.49 | 1.34× | 0.60 | $14.12 | $21,500 | 0.75× |
| demand_softening | 15% | 0.79× | $13.58 | $12.66 | $12.14–$13.27 | 1.02× | 0.50 | $11.73 | $16,250 | 0.57× |
| structural_decline | 0% | 0.68× | $11.41 | $10.39 | $9.90–$10.95 | 0.88× | 0.50 | $9.37 | $14,000 | 0.49× |
| **Probability-weighted** | | | | **$16.38** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $+2.19
- **Downside (worst scenario − price):** $-6.97
- **Expected value vs current** (weighted FV − price): $-0.98 (-5.7%)
- **Position:** TRIM/SHORT (overvalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
