# TRMD — Scenario Fair Value (product margin / glut framework)

- **Current price:** $29.41
- **Analyst target:** $25.00
- **NAV / share (reference, unflexed):** $25.43 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $26.68 (-9.3% vs price)
- **Breakeven TCE (scenario-invariant):** $80,541/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** TRIM/SHORT (overvalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| refinery_squeeze | 25% | 1.25× | $34.45 | $39.10 | $37.29–$41.20 | 4.51× | 0.70 | $49.95 | $107,069 | 1.33× |
| moderate_correction | 30% | 1.16× | $31.17 | $32.74 | $31.63–$34.00 | 2.81× | 0.70 | $36.38 | $64,765 | 0.80× |
| Glut base case | 30% | 0.78× | $17.49 | $16.68 | $15.87–$17.61 | 1.31× | 0.60 | $15.46 | $27,118 | 0.34× |
| demand_softening | 15% | 0.73× | $15.59 | $13.84 | $13.04–$14.73 | 1.05× | 0.50 | $12.09 | $21,983 | 0.27× |
| structural_decline | 0% | 0.65× | $12.81 | $10.86 | $10.33–$11.64 | 0.88× | 0.50 | $8.91 | $18,472 | 0.23× |
| **Probability-weighted** | | | | **$26.68** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $+9.69
- **Downside (worst scenario − price):** $-18.55
- **Expected value vs current** (weighted FV − price): $-2.73 (-9.3%)
- **Position:** TRIM/SHORT (overvalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
