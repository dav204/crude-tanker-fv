# STNG — Scenario Fair Value (product margin / glut framework)

- **Current price:** $76.15
- **Analyst target:** $94.00
- **NAV / share (reference, unflexed):** $76.22 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $76.73 (+0.8% vs price)
- **Breakeven TCE (scenario-invariant):** $68,460/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** HOLD (fairly valued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| refinery_squeeze | 25% | 1.25× | $91.49 | $92.63 | $90.21–$95.46 | 4.72× | 0.70 | $95.30 | $115,401 | 1.69× |
| moderate_correction | 30% | 1.25× | $91.49 | $88.46 | $86.94–$90.22 | 2.90× | 0.70 | $81.41 | $69,118 | 1.01× |
| Glut base case | 30% | 0.85× | $67.24 | $61.89 | $60.68–$63.30 | 1.30× | 0.60 | $53.86 | $27,775 | 0.41× |
| demand_softening | 15% | 0.79× | $63.28 | $56.46 | $55.26–$57.81 | 1.04× | 0.50 | $49.65 | $22,653 | 0.33× |
| structural_decline | 0% | 0.67× | $55.86 | $49.25 | $48.16–$50.45 | 0.88× | 0.50 | $42.64 | $18,994 | 0.28× |
| **Probability-weighted** | | | | **$76.73** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $+16.48
- **Downside (worst scenario − price):** $-26.90
- **Expected value vs current** (weighted FV − price): $+0.58 (+0.8%)
- **Position:** HOLD (fairly valued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
