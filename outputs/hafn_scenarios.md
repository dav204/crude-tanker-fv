# HAFN — Scenario Fair Value (scenario framework)

- **Current price:** $7.70
- **Analyst target:** $10.00
- **NAV / share (reference, unflexed):** $5.34 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $5.41 (-29.7% vs price)
- **Breakeven TCE (scenario-invariant):** $123,511/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** TRIM/SHORT (overvalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| refinery_squeeze | 15% | 1.25× | $7.03 | $8.41 | $7.97–$8.93 | 4.50× | 0.70 | $11.63 | $103,742 | 0.84× |
| moderate_correction | 25% | 1.16× | $6.40 | $7.01 | $6.74–$7.32 | 2.81× | 0.70 | $8.44 | $63,026 | 0.51× |
| Glut base case | 45% | 0.82× | $4.11 | $4.18 | $4.00–$4.38 | 1.57× | 0.70 | $4.35 | $33,196 | 0.27× |
| demand_softening | 15% | 0.74× | $3.57 | $3.42 | $3.21–$3.65 | 1.13× | 0.50 | $3.27 | $23,465 | 0.19× |
| structural_decline | 0% | 0.65× | $2.96 | $2.74 | $2.56–$2.94 | 0.95× | 0.50 | $2.52 | $19,575 | 0.16× |
| **Probability-weighted** | | | | **$5.41** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $+0.71
- **Downside (worst scenario − price):** $-4.96
- **Expected value vs current** (weighted FV − price): $-2.29 (-29.7%)
- **Position:** TRIM/SHORT (overvalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
