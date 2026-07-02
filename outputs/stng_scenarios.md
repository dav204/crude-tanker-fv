# STNG — Scenario Fair Value (product margin / glut framework)

- **Current price:** $75.60
- **Analyst target:** $94.00
- **NAV / share (reference, unflexed):** $77.47 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $77.13 (+2.0% vs price)
- **Breakeven TCE (scenario-invariant):** $53,301/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** HOLD (fairly valued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| refinery_squeeze | 25% | 1.25× | $95.03 | $101.87 | $98.12–$106.23 | 5.13× | 0.70 | $117.81 | $128,615 | 2.41× |
| moderate_correction | 30% | 1.17× | $89.74 | $90.08 | $87.79–$92.68 | 3.10× | 0.70 | $90.86 | $76,023 | 1.43× |
| Glut base case | 30% | 0.76× | $60.60 | $56.40 | $54.74–$58.28 | 1.29× | 0.60 | $50.09 | $28,816 | 0.54× |
| demand_softening | 15% | 0.71× | $57.37 | $51.47 | $49.82–$53.28 | 1.05× | 0.50 | $45.57 | $23,715 | 0.44× |
| structural_decline | 0% | 0.65× | $52.87 | $46.33 | $44.88–$47.93 | 0.88× | 0.50 | $39.79 | $19,823 | 0.37× |
| **Probability-weighted** | | | | **$77.13** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $+26.27
- **Downside (worst scenario − price):** $-29.27
- **Expected value vs current** (weighted FV − price): $+1.53 (+2.0%)
- **Position:** HOLD (fairly valued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
