# CCEC — Scenario Fair Value (LNG glut-cycle framework)

- **Current price:** $20.03
- **Analyst target:** $25.17
- **NAV / share (reference, unflexed):** $28.10 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $29.63 (+47.9% vs price)
- **Breakeven TCE (scenario-invariant):** $0/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** BUY (undervalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Tight resurgence | 25% | 1.25× | $52.98 | $48.52 | $48.52–$48.52 | 1.78× | 0.70 | $38.10 | $137,383 | 116960116913023156721041801216.00× |
| Moderate tightening | 25% | 1.13× | $41.36 | $35.36 | $35.36–$35.36 | 1.00× | 0.50 | $29.36 | $74,327 | 63277725525540146176478674944.00× |
| Glut base case | 38% | 0.96× | $24.44 | $19.76 | $19.76–$19.76 | 0.75× | 0.40 | $16.64 | $54,921 | 46756590879536243279954706432.00× |
| Glut intensifies | 12% | 0.84× | $12.48 | $9.59 | $9.59–$9.59 | 0.56× | 0.40 | $7.66 | $41,075 | 34969035859578036982393077760.00× |
| Structural reset | 0% | 0.72× | $0.69 | $-0.45 | $-0.45–$-0.45 | 0.51× | 0.40 | $-1.21 | $38,068 | 32409379119087867786887692288.00× |
| **Probability-weighted** | | | | **$29.63** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $+28.49
- **Downside (worst scenario − price):** $-20.48
- **Expected value vs current** (weighted FV − price): $+9.60 (+47.9%)
- **Position:** BUY (undervalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
