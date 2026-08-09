# SBLK — Scenario Fair Value (Bulk Set A (China-driven))

- **Current price:** $28.90
- **Analyst target:** $34.50
- **NAV / share (reference, unflexed):** $33.04 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $30.76 (+6.4% vs price)
- **Breakeven TCE (scenario-invariant):** $11,773/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** BUY (undervalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| China acceleration | 20% | 1.15× | $38.76 | $38.11 | $37.23–$38.98 | 1.81× | 0.70 | $36.58 | $30,480 | 2.59× |
| Moderate growth (base) | 40% | 0.99× | $32.56 | $31.30 | $30.42–$32.19 | 1.37× | 0.60 | $29.42 | $22,886 | 1.94× |
| China property drag | 25% | 0.91× | $29.52 | $28.10 | $27.13–$29.08 | 1.16× | 0.50 | $26.69 | $18,793 | 1.60× |
| Coordinated slowdown | 15% | 0.82× | $26.22 | $23.96 | $23.20–$24.72 | 0.97× | 0.50 | $21.70 | $15,962 | 1.36× |
| **Probability-weighted** | | | | **$30.76** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $+9.21
- **Downside (worst scenario − price):** $-4.94
- **Expected value vs current** (weighted FV − price): $+1.86 (+6.4%)
- **Position:** BUY (undervalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
