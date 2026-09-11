# CMBT [WHOLE-CO] — Scenario Fair Value (three-phase MoU framework)

> **Valuation basis:** WHOLE-COMPANY MULTI-SLEEVE = crude (23.8%) + dry_bulk (73.1%) + containerships (3.1%) AGGREGATED (METHODOLOGY §11.9). Off-curve segments (chemical / offshore / FSO / held-for-sale / newbuild book) sit at the corporate level and flow through NAV uniformly across sleeves. Compared to the WHOLE-COMPANY tape price.

- **Current price:** $19.38
- **Analyst target:** $16.59
- **NAV / share (reference, unflexed):** $16.46 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $13.54 (-30.1% vs price)
- **Breakeven TCE (scenario-invariant):** $205,068/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** TRIM/SHORT (overvalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Escalation | 28% | 1.25× | $19.22 | $19.64 | $18.95–$20.39 | 6.47× | 0.70 | $20.62 | $83,364 | 0.41× |
| Pre-MoU baseline | 59% | 0.93× | $14.03 | $13.23 | $12.74–$13.72 | 2.27× | 0.70 | $11.93 | $41,550 | 0.20× |
| MoU base case | 0% | 0.85× | $11.47 | $10.41 | $9.95–$10.87 | 1.87× | 0.70 | $9.13 | $32,817 | 0.16× |
| MoU bear | 13% | 0.79× | $9.87 | $8.53 | $8.15–$8.91 | 1.53× | 0.70 | $6.92 | $27,996 | 0.14× |
| **Probability-weighted** | | | | **$13.54** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $+0.26
- **Downside (worst scenario − price):** $-10.85
- **Expected value vs current** (weighted FV − price): $-5.84 (-30.1%)
- **Position:** TRIM/SHORT (overvalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
