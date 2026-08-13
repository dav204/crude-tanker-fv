# SBLK — Scenario Fair Value (Bulk Set A (China-driven))

- **Current price:** $27.89
- **Analyst target:** $34.50
- **NAV / share (reference, unflexed):** $32.78 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $29.79 (+6.8% vs price)
- **Breakeven TCE (scenario-invariant):** $8,480/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** BUY (undervalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| China acceleration | 20% | 1.12× | $37.27 | $36.79 | $35.92–$37.67 | 1.81× | 0.70 | $35.67 | $30,537 | 3.60× |
| Moderate growth (base) | 40% | 0.96× | $31.40 | $30.31 | $29.42–$31.20 | 1.37× | 0.60 | $28.67 | $22,925 | 2.70× |
| China property drag | 25% | 0.89× | $28.52 | $27.26 | $26.29–$28.23 | 1.16× | 0.50 | $26.00 | $18,813 | 2.22× |
| Coordinated slowdown | 15% | 0.81× | $25.40 | $23.27 | $22.51–$24.03 | 0.97× | 0.50 | $21.14 | $15,984 | 1.88× |
| **Probability-weighted** | | | | **$29.79** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $+8.90
- **Downside (worst scenario − price):** $-4.62
- **Expected value vs current** (weighted FV − price): $+1.90 (+6.8%)
- **Position:** BUY (undervalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
