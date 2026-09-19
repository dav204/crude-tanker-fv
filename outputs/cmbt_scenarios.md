# CMBT [WHOLE-CO] — Scenario Fair Value (three-phase MoU framework)

> **Valuation basis:** WHOLE-COMPANY MULTI-SLEEVE = crude (23.8%) + dry_bulk (73.1%) + containerships (3.1%) AGGREGATED (METHODOLOGY §11.9). Off-curve segments (chemical / offshore / FSO / held-for-sale / newbuild book) sit at the corporate level and flow through NAV uniformly across sleeves. Compared to the WHOLE-COMPANY tape price.

- **Current price:** $20.29
- **Analyst target:** $16.59
- **NAV / share (reference, unflexed):** $13.36 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $10.81 (-46.7% vs price)
- **Breakeven TCE (scenario-invariant):** $325,779/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** TRIM/SHORT (overvalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Escalation | 28% | 1.25× | $15.80 | $16.45 | $15.76–$17.19 | 6.47× | 0.70 | $17.97 | $83,364 | 0.26× |
| Pre-MoU baseline | 59% | 1.00× | $11.13 | $10.68 | $10.17–$11.20 | 2.65× | 0.70 | $10.02 | $44,171 | 0.14× |
| MoU base case | 0% | 0.90× | $8.54 | $7.86 | $7.38–$8.33 | 2.17× | 0.70 | $7.10 | $35,031 | 0.11× |
| MoU bear | 13% | 0.80× | $6.68 | $5.67 | $5.29–$6.05 | 1.59× | 0.70 | $4.47 | $28,380 | 0.09× |
| **Probability-weighted** | | | | **$10.81** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $-3.84
- **Downside (worst scenario − price):** $-14.62
- **Expected value vs current** (weighted FV − price): $-9.48 (-46.7%)
- **Position:** TRIM/SHORT (overvalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
