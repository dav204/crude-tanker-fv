# STNG — Scenario Fair Value (scenario framework)

- **Current price:** $75.60
- **Analyst target:** $94.00
- **NAV / share (reference, unflexed):** $83.87 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $73.40 (-2.9% vs price)
- **Breakeven TCE (scenario-invariant):** $0/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** HOLD (fairly valued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| refinery_squeeze | 15% | 1.25× | $103.26 | $94.90 | $94.90–$94.90 | 5.07× | 0.70 | $75.40 | $126,845 | 115876821158387407478530768896.00× |
| moderate_correction | 25% | 1.17× | $97.33 | $89.52 | $89.52–$89.52 | 3.07× | 0.70 | $71.29 | $75,098 | 68604217347936657381051596800.00× |
| Glut base case | 45% | 0.80× | $68.59 | $63.42 | $63.42–$63.42 | 1.60× | 0.70 | $51.36 | $37,171 | 33956559507511532268071944192.00× |
| demand_softening | 15% | 0.73× | $62.65 | $54.95 | $54.95–$54.95 | 1.13× | 0.50 | $47.25 | $25,916 | 23675086748061584272314597376.00× |
| structural_decline | 0% | 0.65× | $56.72 | $49.93 | $49.93–$49.93 | 0.94× | 0.50 | $43.14 | $21,469 | 19612775719331516833800912896.00× |
| **Probability-weighted** | | | | **$73.40** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $+19.30
- **Downside (worst scenario − price):** $-25.67
- **Expected value vs current** (weighted FV − price): $-2.20 (-2.9%)
- **Position:** HOLD (fairly valued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
