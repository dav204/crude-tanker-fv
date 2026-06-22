# CCEC — Scenario Fair Value (LNG glut-cycle framework)

- **Current price:** $20.03
- **Analyst target:** $25.17
- **NAV / share (reference, unflexed):** $28.10 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $35.91 (+79.3% vs price)
- **Breakeven TCE (scenario-invariant):** $0/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** BUY (undervalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Tight resurgence | 25% | 1.25× | $52.98 | $49.70 | $49.52–$49.91 | 1.78× | 0.70 | $42.05 | $137,383 | 116960116913023156721041801216.00× |
| Moderate tightening | 25% | 1.13× | $41.36 | $41.36 | $41.21–$41.56 | 1.00× | 0.50 | $41.36 | $74,327 | 63277725525540146176478674944.00× |
| Glut base case | 38% | 0.96× | $24.44 | $28.84 | $28.70–$29.00 | 0.75× | 0.40 | $31.77 | $54,921 | 46756590879536243279954706432.00× |
| Glut intensifies | 12% | 0.84× | $12.48 | $18.18 | $18.07–$18.33 | 0.56× | 0.40 | $21.98 | $41,075 | 34969035859578036982393077760.00× |
| Structural reset | 0% | 0.72× | $0.69 | $7.81 | $7.69–$7.92 | 0.51× | 0.40 | $12.55 | $38,068 | 32409379119087867786887692288.00× |
| **Probability-weighted** | | | | **$35.91** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $+29.67
- **Downside (worst scenario − price):** $-12.22
- **Expected value vs current** (weighted FV − price): $+15.88 (+79.3%)
- **Position:** BUY (undervalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
