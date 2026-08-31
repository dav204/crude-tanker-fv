# 2343 — Scenario Fair Value (Bulk Set A (China-driven))

- **Current price:** $0.53
- **Analyst target:** $0.44
- **NAV / share (reference, unflexed):** $0.41 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $0.38 (-29.2% vs price)
- **Breakeven TCE (scenario-invariant):** $40,554/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** TRIM/SHORT (overvalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| China acceleration | 20% | 1.06× | $0.43 | $0.43 | $0.42–$0.44 | 1.55× | 0.70 | $0.43 | $20,868 | 0.51× |
| Moderate growth (base) | 40% | 0.95× | $0.39 | $0.38 | $0.37–$0.39 | 1.21× | 0.60 | $0.37 | $16,288 | 0.40× |
| China property drag | 25% | 0.92× | $0.37 | $0.37 | $0.35–$0.38 | 1.12× | 0.50 | $0.36 | $15,031 | 0.37× |
| Coordinated slowdown | 15% | 0.84× | $0.33 | $0.31 | $0.30–$0.32 | 0.90× | 0.50 | $0.29 | $12,186 | 0.30× |
| **Probability-weighted** | | | | **$0.38** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $-0.10
- **Downside (worst scenario − price):** $-0.22
- **Expected value vs current** (weighted FV − price): $-0.16 (-29.2%)
- **Position:** TRIM/SHORT (overvalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
