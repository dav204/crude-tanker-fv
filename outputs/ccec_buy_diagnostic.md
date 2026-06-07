# CCEC — BUY-Actionability Diagnostic (Set B-revised lock, 2026-06-01)

**Purpose:** the user-specified pre-action review for the CCEC BUY signal that
emerged from the Set B → Set B-revised LNG weight lock (METHODOLOGY §11.3 v3).
The Ras Laffan + Cheniere reweighting flipped CCEC HOLD → BUY (EV −1.0% →
+14.1%); this doc validates the signal before it's treated as fully actionable.

Three sub-checks per the close-out spec:
  1. Newbuild orderbook valuation vs publicly disclosed contract prices —
     sanity check on the upside torque driver.
  2. CCEC PW FV across Set A (v1 placeholder), Set B-revised (v3 current),
     and a bearish alternative — classify the BUY as weight-robust or
     weight-driven.
  3. CCEC `k_broker` spread review — classify as mark-driven or
     mark-validated.

**Headline verdict at the bottom.**

---

## 1. Newbuild orderbook valuation vs disclosed contract prices

CCEC's newbuild book totals **$2,251.5M outstanding** (Q1 2026 6-K). Per the
balance sheet breakdown (`inputs/balance_sheets/ccec_2026-Q1.yaml`):

| Programme | Vessels | Total committed | Per vessel (contract) |
|---|---:|---:|---:|
| LNG (X-DF2.1 174k cbm) | 9 | $1,855.1M | **$206.1M** |
| Gas (2× LCO2 incl. Amadeus + 6× dual-fuel MGC) | 8 | $396.4M | **$49.6M** |
| **Total** | **17** | **$2,251.5M** | — |

**Tool curve values at delivered market (`vessel_value_curves.yaml`, eco-inclusive modern spec):**

| Class | Curve NB | Eco premium | Modern-spec NB | At-market (CCEC fleet) |
|---|---:|---:|---:|---:|
| LNGC (X-DF2.1) | $260.0M | +5% (§3.1) | $273.0M | 9 × $273M = **$2,457M** |
| MGC (dual-fuel modern) | $65.0M | — | $65.0M | 8 × $65M = **$520M** |
| **Total NB at delivered market** | — | — | — | **$2,977M** |

**NB embedded option value:** $2,977M (at market) − $2,251.5M (contract) =
**+$725.5M** of cheaply-contracted NB value. Divided by 50.4M diluted shares,
that's **+$14.40/share** of embedded NB upside already baked into CCEC's NAV.

**Cross-check vs CCEC tool NAV per share ($28.10):** the $14.40/sh NB option
component is ~51% of NAV — directly explains why CCEC has roughly 2× FLNG's
scenario torque (FLNG has zero NB book; its $28.45/sh NAV is entirely the
mature in-water LNGC fleet).

**Are the contract prices defensible vs the published market?**

- **LNG X-DF2.1 NBs at $206M contract** vs industry market ~$250-275M for
  2024-2025 Korean-yard X-DF2.1 orders (sources: VesselsValue / Clarksons SIN
  / Pareto Shipping Daily 2024-Q4 → 2025-Q1 prints). CCEC contracted these
  during the 2023-early-2024 ordering window before the X-DF2.1 premium
  fully crystallised. Contract prices are ~25-30% below current market —
  consistent with the tool's curve treatment ($273M delivered market).
- **Gas NBs at $49.6M contract** vs MGC market $55-65M for modern dual-fuel
  / LCO2 22-40k cbm. ~20-25% below current market — consistent with the
  tool's $65M curve.

**Verdict on sub-check 1: NB orderbook valuation is consistent with the
publicly disclosed contract prices and the published curve marks.** The NB
embedded option value is real and material — not a model artefact. Sanity
check passes.

---

## 2. Weight-robustness classification across three weight sets

Per-scenario CCEC FV (unchanged across weight sets — only weights change):

| Scenario | CCEC FV |
|---|---:|
| tight_resurgence | $48.52 |
| moderate_tightening | $35.36 |
| glut_base | $19.76 |
| glut_intensifies | $9.59 |
| structural_reset | $1.05 |

**Three weight sets evaluated:**

| Scenario | Set A (v1 placeholder) | Set B-revised (v3 current) | Set B-bear (sensitivity stress) |
|---|---:|---:|---:|
| tight_resurgence | 0.10 | **0.15** | 0.05 |
| moderate_tightening | 0.15 | **0.25** | 0.10 |
| glut_base | 0.50 | **0.45** | 0.45 |
| glut_intensifies | 0.25 | **0.15** | 0.30 |
| structural_reset | 0.00 | **0.00** | 0.10 |

- *Set A* is the v1 crude-inherited placeholder (METHODOLOGY §11.3) — the
  most-bearish historical lock that ever shipped.
- *Set B-revised* is the current production lock.
- *Set B-bear* is a deliberate stress: 5pp off tight, 5pp off moderate, 10pp
  onto glut_intensifies + 10pp onto a newly-activated structural_reset. It's
  what the world looks like if Ras Laffan restarts cleanly + transition
  accelerates faster than expected. (Not a forecast — a stress.)

**Per-set PW FV and position (CCEC at $23.18, HOLD band $22.02-$24.34):**

| Weight set | PW FV | EV% | Position |
|---|---:|---:|---|
| Set A (v1 placeholder) | $22.43 | −3.2% | HOLD |
| Set B (v2, prior — reference) | $22.94 | −1.0% | HOLD |
| **Set B-revised (v3, current)** | **$26.45** | **+14.1%** | **BUY** |
| Set B-bear (sensitivity stress) | $17.84 | −23.1% | TRIM/SHORT |

**Classification:**

- Across the four evaluated weight sets, CCEC's position is BUY in **1 of 4**,
  HOLD in **2 of 4**, TRIM/SHORT in **1 of 4**.
- **The BUY signal is weight-driven, not weight-robust.** It requires the
  Set B-revised constructive tilt (constructive total 0.85) to hold; under
  any of the more glut-weighted sets the call is HOLD or worse.

**Verdict on sub-check 2: CCEC's BUY is weight-driven.** A reasonable
alternative weight set (Set A — what the framework was running with weeks
ago) produces HOLD, not BUY. The call depends on the Ras Laffan + Cheniere
narrative continuing to be the central case. If the empirical environment
shifts back toward glut (Ras Laffan restarts cleanly, US Gulf Coast fully
ramps without disruption), Set B-revised becomes stale and CCEC's signal
reverts to HOLD or below.

---

## 3. k_broker spread classification (mark-driven vs mark-validated)

From the most recent broker-NAV sweep (`outputs/broker_nav_sweep.md`):

| Metric | Value |
|---|---:|
| Consensus P/NAV | 0.90× |
| `k_broker` (uniform mark premium to broker NAV) | 0.98 |
| Tool EV (at tool vessel marks) | +14.1% |
| Broker EV (at broker-equivalent marks) | +5.0% |
| **Spread (broker − tool)** | **−9pp** |
| Read | **mark-validated** (narrow) |

`k_broker = 0.98` says broker NAV consensus sits ~2% BELOW tool NAV — close
enough that the call is the same direction at both marks (BUY at tool stays
BUY at broker, though the broker EV is +5.0% which is right at the BUY
threshold; under marginally more conservative broker marks it could slip to
HOLD). The −9pp spread is narrow vs the mark-driven bucket (ASC +40pp, NAT
+53pp, INSW +22pp).

**Verdict on sub-check 3: CCEC is mark-validated.** The vessel-mark uncertainty
is small — the tool's LNGC + MGC curves agree with broker consensus on the
fleet's value. The call is not mark-driven; it's weight-driven.

---

## Headline verdict

The CCEC BUY signal under Set B-revised is:

- ✓ **NB orderbook valuation: validated.** $725M / +$14.40/sh of embedded NB
  option value is consistent with disclosed contract prices vs current market
  ($206M LNG contract vs $273M curve; $49.6M gas contract vs $65M curve).
  This is the real underlying mechanism explaining CCEC's 1.9× FLNG torque.
- ⚠ **Weight-robustness: WEIGHT-DRIVEN BUY.** Position is BUY only under
  Set B-revised. Under Set A (v1 placeholder), Set B (v2 prior), and a
  bearish stress, position is HOLD / HOLD / TRIM/SHORT. The BUY depends on
  the LNG-tight thesis (Ras Laffan + Cheniere absorption) continuing to be
  central, not a secondary view.
- ✓ **Mark-spread: MARK-VALIDATED.** k_broker 0.98, spread −9pp. Tool and
  broker agree on vessel marks. The signal's risk is on the scenario
  probability assignment, not on the vessel-mark calibration.

**Position-sizing recommendation per §6 CCEC entry:** size CCEC's BUY smaller
than a weight-robust BUY would warrant. Treat as a leveraged expression of
the LNG-tight thesis — if the empirical supply environment changes (Ras
Laffan restart, sustained spot reversion to the glut range), the call should
be re-evaluated promptly via the `lng_weight_robustness.md` quarterly
diagnostic.

**Triggers to re-evaluate Set B-revised** (per METHODOLOGY §13.3):
- Ras Laffan Trains 4 & 6 restart cleanly + capacity fully restored
- Cheniere Stage 3 Train 6 reaches sustained operations without supply
  disruption elsewhere
- LNG spot reverts to the glut_base forward range ($40-75k seasonally) for a
  full quarter
- Sanctioned-flow regime change materially affects LNG trade routing

When any of those land, re-run `python scripts/lng_weight_comparison.py`
with the candidate alternative weight set, regenerate this diagnostic, and
reassess CCEC's position.
