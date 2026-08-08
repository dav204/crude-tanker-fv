# STNG — Scenario Fair Value (product margin / glut framework)

- **Current price:** $76.08
- **Analyst target:** $94.00
- **NAV / share (reference, unflexed):** $77.13 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $76.87 (+1.0% vs price)
- **Breakeven TCE (scenario-invariant):** $57,165/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** HOLD (fairly valued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| refinery_squeeze | 25% | 1.25× | $94.62 | $101.53 | $97.78–$105.89 | 5.12× | 0.70 | $117.66 | $128,267 | 2.24× |
| moderate_correction | 30% | 1.17× | $89.33 | $89.75 | $87.46–$92.35 | 3.09× | 0.70 | $90.71 | $75,841 | 1.33× |
| Glut base case | 30% | 0.76× | $60.37 | $56.22 | $54.56–$58.11 | 1.29× | 0.60 | $50.01 | $28,788 | 0.50× |
| demand_softening | 15% | 0.71× | $57.14 | $51.31 | $49.67–$53.12 | 1.04× | 0.50 | $45.48 | $23,687 | 0.41× |
| structural_decline | 0% | 0.65× | $52.65 | $46.18 | $44.72–$47.78 | 0.88× | 0.50 | $39.70 | $19,801 | 0.35× |
| **Probability-weighted** | | | | **$76.87** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $+25.45
- **Downside (worst scenario − price):** $-29.90
- **Expected value vs current** (weighted FV − price): $+0.79 (+1.0%)
- **Position:** HOLD (fairly valued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
