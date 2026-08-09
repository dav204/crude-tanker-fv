# 2343 — Scenario Fair Value (Bulk Set A (China-driven))

- **Current price:** $0.48
- **Analyst target:** $0.44
- **NAV / share (reference, unflexed):** $0.41 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $0.40 (-17.4% vs price)
- **Breakeven TCE (scenario-invariant):** $32,599/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** TRIM/SHORT (overvalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| China acceleration | 20% | 1.12× | $0.47 | $0.46 | $0.45–$0.47 | 1.55× | 0.70 | $0.45 | $20,876 | 0.64× |
| Moderate growth (base) | 40% | 1.00× | $0.41 | $0.40 | $0.39–$0.41 | 1.21× | 0.60 | $0.39 | $16,295 | 0.50× |
| China property drag | 25% | 0.97× | $0.40 | $0.39 | $0.37–$0.40 | 1.12× | 0.50 | $0.38 | $15,037 | 0.46× |
| Coordinated slowdown | 15% | 0.87× | $0.35 | $0.33 | $0.32–$0.34 | 0.90× | 0.50 | $0.31 | $12,191 | 0.37× |
| **Probability-weighted** | | | | **$0.40** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $-0.02
- **Downside (worst scenario − price):** $-0.15
- **Expected value vs current** (weighted FV − price): $-0.08 (-17.4%)
- **Position:** TRIM/SHORT (overvalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
