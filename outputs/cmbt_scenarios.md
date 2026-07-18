# CMBT [WHOLE-CO] — Scenario Fair Value (three-phase MoU framework)

> **Valuation basis:** WHOLE-COMPANY MULTI-SLEEVE = crude (24.0%) + dry_bulk (72.8%) + containerships (3.2%) AGGREGATED (METHODOLOGY §11.9). Off-curve segments (chemical / offshore / FSO / held-for-sale / newbuild book) sit at the corporate level and flow through NAV uniformly across sleeves. Compared to the WHOLE-COMPANY tape price.

- **Current price:** $14.96
- **Analyst target:** $16.59
- **NAV / share (reference, unflexed):** $16.12 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $14.09 (-5.8% vs price)
- **Breakeven TCE (scenario-invariant):** $56,513/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** TRIM/SHORT (overvalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Escalation | 25% | 1.25× | $21.12 | $21.38 | $20.67–$22.13 | 6.37× | 0.70 | $21.98 | $82,205 | 1.45× |
| Pre-MoU baseline | 45% | 0.82× | $14.72 | $13.81 | $13.32–$14.31 | 2.25× | 0.70 | $12.45 | $41,310 | 0.73× |
| MoU base case | 18% | 0.76× | $12.00 | $10.83 | $10.36–$11.29 | 1.85× | 0.70 | $9.56 | $32,641 | 0.58× |
| MoU bear | 12% | 0.72× | $10.30 | $8.87 | $8.49–$9.25 | 1.53× | 0.70 | $7.27 | $27,910 | 0.49× |
| **Probability-weighted** | | | | **$14.09** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $+6.42
- **Downside (worst scenario − price):** $-6.09
- **Expected value vs current** (weighted FV − price): $-0.87 (-5.8%)
- **Position:** TRIM/SHORT (overvalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
