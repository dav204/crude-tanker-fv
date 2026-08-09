# SBLK — Scenario Fair Value (Bulk Set A (China-driven))

- **Current price:** $28.90
- **Analyst target:** $34.50
- **NAV / share (reference, unflexed):** $32.39 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $30.22 (+4.6% vs price)
- **Breakeven TCE (scenario-invariant):** $13,931/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** HOLD (fairly valued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| China acceleration | 20% | 1.15× | $38.02 | $37.45 | $36.57–$38.32 | 1.81× | 0.70 | $36.12 | $30,554 | 2.19× |
| Moderate growth (base) | 40% | 0.99× | $31.92 | $30.75 | $29.87–$31.64 | 1.37× | 0.60 | $29.00 | $22,939 | 1.65× |
| China property drag | 25% | 0.91× | $28.92 | $27.60 | $26.62–$28.57 | 1.16× | 0.50 | $26.27 | $18,823 | 1.35× |
| Coordinated slowdown | 15% | 0.82× | $25.69 | $23.51 | $22.75–$24.27 | 0.97× | 0.50 | $21.32 | $15,992 | 1.15× |
| **Probability-weighted** | | | | **$30.22** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $+8.55
- **Downside (worst scenario − price):** $-5.39
- **Expected value vs current** (weighted FV − price): $+1.32 (+4.6%)
- **Position:** HOLD (fairly valued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
