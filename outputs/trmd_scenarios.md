# TRMD — Scenario Fair Value (product margin / glut framework)

- **Current price:** $29.49
- **Analyst target:** $25.00
- **NAV / share (reference, unflexed):** $30.22 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $33.58 (+13.9% vs price)
- **Breakeven TCE (scenario-invariant):** $37,671/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** BUY (undervalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| refinery_squeeze | 25% | 1.25× | $39.37 | $45.25 | $42.89–$48.00 | 4.46× | 0.70 | $58.97 | $105,540 | 2.80× |
| moderate_correction | 30% | 1.25× | $39.37 | $40.85 | $39.40–$42.50 | 2.78× | 0.70 | $44.30 | $63,966 | 1.70× |
| Glut base case | 30% | 0.85× | $24.66 | $23.31 | $22.24–$24.53 | 1.31× | 0.60 | $21.28 | $26,998 | 0.72× |
| demand_softening | 15% | 0.78× | $22.25 | $20.10 | $19.04–$21.27 | 1.05× | 0.50 | $17.95 | $21,860 | 0.58× |
| structural_decline | 0% | 0.66× | $17.87 | $15.55 | $14.62–$16.59 | 0.88× | 0.50 | $13.23 | $18,376 | 0.49× |
| **Probability-weighted** | | | | **$33.58** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $+15.76
- **Downside (worst scenario − price):** $-13.94
- **Expected value vs current** (weighted FV − price): $+4.09 (+13.9%)
- **Position:** BUY (undervalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
