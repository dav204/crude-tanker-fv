# TEN [WHOLE-CO] — Scenario Fair Value (three-phase MoU framework)

> **Valuation basis:** WHOLE-COMPANY 3-SLEEVE = crude (72.9%) + product (15.7%) + lng (11.4%) AGGREGATED (METHODOLOGY §11.6). Off-curve shuttle-contracted-book sleeve sits at the corporate level (`shuttle_contracted_book`) and flows through NAV uniformly across scenarios. Compared to the WHOLE-COMPANY tape price.

- **Current price:** $44.00
- **Analyst target:** $51.50
- **NAV / share (reference, unflexed):** $88.56 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $49.37 (+12.2% vs price)
- **Breakeven TCE (scenario-invariant):** $0/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** BUY (undervalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Escalation | 10% | 1.25× | $120.93 | $81.38 | $81.09–$81.72 | 4.40× | 0.70 | $73.76 | $150,475 | 84653118661268134380403949568.00× |
| Pre-MoU baseline | 15% | 1.04× | $99.10 | $66.98 | $66.80–$67.18 | 2.82× | 0.70 | $61.13 | $92,388 | 51975254898356244316621373440.00× |
| MoU base case | 50% | 0.75× | $63.25 | $43.32 | $43.20–$43.45 | 1.42× | 0.60 | $41.61 | $48,120 | 27070771698831309773427703808.00× |
| MoU bear | 25% | 0.71× | $55.35 | $38.10 | $37.98–$38.23 | 1.16× | 0.50 | $37.40 | $37,780 | 21253880657204307861899837440.00× |
| **Probability-weighted** | | | | **$49.37** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $+37.38
- **Downside (worst scenario − price):** $-5.90
- **Expected value vs current** (weighted FV − price): $+5.37 (+12.2%)
- **Position:** BUY (undervalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
