# SBLK — Scenario Fair Value (Bulk Set A (China-driven))

- **Current price:** $26.35
- **Analyst target:** $34.50
- **NAV / share (reference, unflexed):** $29.34 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $27.69 (+5.1% vs price)
- **Breakeven TCE (scenario-invariant):** $14,427/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** BUY (undervalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| China acceleration | 20% | 1.15× | $34.98 | $34.64 | $33.79–$35.49 | 1.81× | 0.70 | $33.84 | $30,572 | 2.12× |
| Moderate growth (base) | 40% | 0.99× | $29.07 | $28.20 | $27.33–$29.06 | 1.37× | 0.60 | $26.89 | $22,948 | 1.59× |
| China property drag | 25% | 0.91× | $26.17 | $25.20 | $24.25–$26.15 | 1.16× | 0.50 | $24.23 | $18,823 | 1.30× |
| Coordinated slowdown | 15% | 0.83× | $23.04 | $21.22 | $20.48–$21.96 | 0.97× | 0.50 | $19.41 | $15,996 | 1.11× |
| **Probability-weighted** | | | | **$27.69** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $+8.29
- **Downside (worst scenario − price):** $-5.13
- **Expected value vs current** (weighted FV − price): $+1.34 (+5.1%)
- **Position:** BUY (undervalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
