# SBLK — Scenario Fair Value (Bulk Set A (China-driven))

- **Current price:** $28.14
- **Analyst target:** $34.50
- **NAV / share (reference, unflexed):** $30.64 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $28.62 (+1.7% vs price)
- **Breakeven TCE (scenario-invariant):** $16,990/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** HOLD (fairly valued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| China acceleration | 20% | 1.15× | $36.21 | $35.72 | $34.87–$36.58 | 1.81× | 0.70 | $34.58 | $30,465 | 1.79× |
| Moderate growth (base) | 40% | 0.99× | $30.17 | $29.14 | $28.28–$30.00 | 1.37× | 0.60 | $27.59 | $22,876 | 1.35× |
| China property drag | 25% | 0.91× | $27.22 | $26.08 | $25.13–$27.03 | 1.16× | 0.50 | $24.94 | $18,788 | 1.11× |
| Coordinated slowdown | 15% | 0.82× | $24.00 | $22.03 | $21.29–$22.77 | 0.97× | 0.50 | $20.06 | $15,957 | 0.94× |
| **Probability-weighted** | | | | **$28.62** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $+7.58
- **Downside (worst scenario − price):** $-6.11
- **Expected value vs current** (weighted FV − price): $+0.48 (+1.7%)
- **Position:** HOLD (fairly valued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
