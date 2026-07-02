# STNG — Scenario Fair Value (product margin / glut framework)

- **Current price:** $69.53
- **Analyst target:** $94.00
- **NAV / share (reference, unflexed):** $77.47 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $70.90 (+2.0% vs price)
- **Breakeven TCE (scenario-invariant):** $21,075/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** HOLD (fairly valued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| refinery_squeeze | 15% | 1.25× | $95.03 | $101.87 | $98.12–$106.23 | 5.13× | 0.70 | $117.81 | $128,615 | 6.10× |
| moderate_correction | 25% | 1.17× | $89.74 | $90.08 | $87.79–$92.68 | 3.10× | 0.70 | $90.86 | $76,023 | 3.61× |
| Glut base case | 45% | 0.76× | $60.60 | $56.40 | $54.74–$58.28 | 1.29× | 0.60 | $50.09 | $28,816 | 1.37× |
| demand_softening | 15% | 0.71× | $57.37 | $51.47 | $49.82–$53.28 | 1.05× | 0.50 | $45.57 | $23,715 | 1.13× |
| structural_decline | 0% | 0.65× | $52.87 | $46.33 | $44.88–$47.93 | 0.88× | 0.50 | $39.79 | $19,823 | 0.94× |
| **Probability-weighted** | | | | **$70.90** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $+32.34
- **Downside (worst scenario − price):** $-23.20
- **Expected value vs current** (weighted FV − price): $+1.37 (+2.0%)
- **Position:** HOLD (fairly valued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
