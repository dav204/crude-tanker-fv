# SB — Scenario Fair Value (Bulk Set A (China-driven))

- **Current price:** $6.36
- **Analyst target:** $7.10
- **NAV / share (reference, unflexed):** $10.31 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $9.67 (+52.0% vs price)
- **Breakeven TCE (scenario-invariant):** $0/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** BUY (undervalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| China acceleration | 20% | 1.17× | $12.58 | $12.08 | $11.93–$12.23 | 1.96× | 0.70 | $10.90 | $27,627 | 67923404147052299229864132608.00× |
| Moderate growth (base) | 40% | 1.00× | $10.26 | $9.77 | $9.62–$9.92 | 1.49× | 0.60 | $9.04 | $20,849 | 51260638366433016868157521920.00× |
| China property drag | 25% | 0.93× | $9.36 | $8.84 | $8.71–$8.96 | 1.28× | 0.60 | $8.04 | $17,572 | 43203084920576762876428025856.00× |
| Coordinated slowdown | 15% | 0.83× | $8.04 | $7.58 | $7.45–$7.70 | 1.07× | 0.50 | $7.11 | $14,822 | 36441846657548672926914445312.00× |
| **Probability-weighted** | | | | **$9.67** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $+5.72
- **Downside (worst scenario − price):** $+1.22
- **Expected value vs current** (weighted FV − price): $+3.31 (+52.0%)
- **Position:** BUY (undervalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
