# ASC — Scenario Fair Value (product margin / glut framework)

- **Current price:** $15.12
- **Analyst target:** $17.95
- **NAV / share (reference, unflexed):** $15.93 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $15.15 (+0.2% vs price)
- **Breakeven TCE (scenario-invariant):** $25,023/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** HOLD (fairly valued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| refinery_squeeze | 25% | 1.16× | $18.59 | $18.21 | $17.61–$18.91 | 2.23× | 0.70 | $17.30 | $35,750 | 1.43× |
| moderate_correction | 30% | 1.04× | $16.64 | $15.95 | $15.53–$16.46 | 1.72× | 0.70 | $14.34 | $27,500 | 1.10× |
| Glut base case | 30% | 0.93× | $14.74 | $13.64 | $13.18–$14.21 | 1.34× | 0.60 | $11.99 | $21,500 | 0.86× |
| demand_softening | 15% | 0.82× | $13.06 | $11.46 | $11.00–$11.99 | 1.02× | 0.50 | $9.85 | $16,250 | 0.65× |
| structural_decline | 0% | 0.70× | $11.04 | $9.42 | $9.00–$9.91 | 0.88× | 0.50 | $7.81 | $14,000 | 0.56× |
| **Probability-weighted** | | | | **$15.15** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $+3.09
- **Downside (worst scenario − price):** $-5.70
- **Expected value vs current** (weighted FV − price): $+0.03 (+0.2%)
- **Position:** HOLD (fairly valued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
