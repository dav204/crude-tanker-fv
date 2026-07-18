# 2343 — Scenario Fair Value (Bulk Set A (China-driven))

- **Current price:** $0.40
- **Analyst target:** $0.44
- **NAV / share (reference, unflexed):** $0.39 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $0.38 (-2.8% vs price)
- **Breakeven TCE (scenario-invariant):** $18,543/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** HOLD (fairly valued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| China acceleration | 20% | 1.13× | $0.45 | $0.44 | $0.43–$0.46 | 1.55× | 0.70 | $0.44 | $20,878 | 1.13× |
| Moderate growth (base) | 40% | 1.01× | $0.40 | $0.39 | $0.37–$0.40 | 1.21× | 0.60 | $0.37 | $16,296 | 0.88× |
| China property drag | 25% | 0.98× | $0.38 | $0.37 | $0.36–$0.39 | 1.12× | 0.50 | $0.36 | $15,035 | 0.81× |
| Coordinated slowdown | 15% | 0.88× | $0.34 | $0.32 | $0.30–$0.33 | 0.90× | 0.50 | $0.29 | $12,190 | 0.66× |
| **Probability-weighted** | | | | **$0.38** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $+0.05
- **Downside (worst scenario − price):** $-0.08
- **Expected value vs current** (weighted FV − price): $-0.01 (-2.8%)
- **Position:** HOLD (fairly valued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
