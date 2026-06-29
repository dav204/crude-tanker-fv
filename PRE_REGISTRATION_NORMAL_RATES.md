# P1 normal-rate layer — pre-registration

**Frozen 2026-06-29, ahead of any computation.** This document is committed
*before* `normal_rates.py` is built and *before* a single rate is computed. Its
purpose is to make the parity anchor an out-of-sample construction, not a fit to
a level already in mind. Inputs, predictions (with halt conditions), and
validation gates are pinned here; if a computed value lands outside its
registered band, the response is to investigate the **input**, not adjust the
output. Signed off by owner 2026-06-29 (two rounds of pushback incorporated:
opex definition, ±$500 bands, Cape NB re-centering, PV-salvage scrap, ≥12q
mean-reversion floor).

## 0. Framing — the deliverable is the divergence, not one blessed anchor

P1 produces, per vessel class, **two tagged normal-rate bases** and surfaces the
**divergence between them** as the under-/over-ordered signal. The justified leg
shows SB's RONAV at **parity** *and* at **historical-mean**, side by side.
- Cheap on both bases → robust.
- Flips between them → "the call depends on the normalization philosophy" — a
  real finding, not a failure.

`cycle.py` stays **frozen** (owner decision D1): cycle position keeps reading
today's `historical_tce_means.yaml` exactly as now. **No headline FV moves in P1.**
Migrating cycle position onto the new basis is a separate, pre-registered,
delta-reviewed, re-ratified change (out of scope here).

## 1. The two bases

- **`parity`** — replacement economics (the rate that lets a newbuild earn its
  cost of capital). Inputs registered in §3. This is the headline basis for the
  justified leg (it closes the §17 loop: parity is the rate that makes
  justified-P/NAV = 1.0 for a newbuild).
- **`historical_mean`** — realized through-cycle mean (a mean-reversion target).
  v1 = the current `historical_tce_means.yaml` values, tagged with their real
  basis (`tc_10yr_mean` / `archive_22mo_median` / `fy_calendar_avg`). The true
  realized-mean route (Baltic $/day series) is **deferred and gated** (§5a, §7).

The two share the **computation layer, not the value** — each consumer picks the
basis right for its job (cycle = mean-reversion target; RONAV = equilibrium
earnings).

## 2. Parity formula (registered exactly)

```
required_TCE/day = opex/day + (NB − scrap·(1+WACC)^(−N)) · CRF / operating_days
CRF              = WACC / (1 − (1+WACC)^(−N))
```

**Scrap enters at PRESENT VALUE** (`scrap·(1+WACC)^(−N)`), not undiscounted. The
capital recovery factor amortizes the *net* capital sunk; salvage is a year-N cash
inflow and must be discounted to year 0. Naive `(NB − scrap)·CRF` double-credits
the time value, under-charges capital, and lands Kamsarmax at $13.1k — outside its
own registered band (§4). The NPV=0 form gives $14.8k, which reproduces the band
committed before deriving it. **`normal_rates.py` carries a one-line comment at the
scrap term** — naive-CRF-salvage is a common "simplification" error a future
reader/agent will be tempted to reintroduce.

## 3. Registered inputs (frozen)

### 3a. WACC (asset hurdle — distinct from the §17 equity discount `r` = 11%)
- **Default 0.08; gridded {0.07, 0.08, 0.09, 0.10}.**
- Build: `WACC = 0.11·CoE_wt(0.42) + after-tax CoD·debt_wt(0.58)`.
- **Normalized base rate committed to ~3.0% long-run** (NOT today's ~4% SOFR — a
  through-cycle anchor needs a through-cycle base or it drifts with the rate
  environment). Margin = secured ship-mortgage **+300bp**; tax shield ≈ 0
  (tonnage-tax FPIs). → CoD ≈ 6.0%, after-tax ≈ 6.0%. → `0.11·0.42 + 0.060·0.58 =
  0.081`, headline **0.08**.
- The **7-10% grid already spans the 3%-vs-4%-base disagreement** (8.1% vs 8.6%),
  so the point commit to a 3% base is not load-bearing beyond what the sensitivity
  already stresses.

### 3b. Opex — definition pinned BEFORE weighting
1. **Reduce each name's disclosed per-class opex to ONE definition:** cash vessel
   opex incl. routine maintenance, **excl. management fees**, **excl. capitalized
   special-survey / dry-dock**. (SB's ~€950/day related-party manager fee is
   exactly what gets stripped first; leaving it in and fleet-weighting against a
   peer that excludes it would launder a definitional gap.)
2. **Then fleet-weight** the normalized figures across every watchlist name
   carrying the class (dry-bulk: SB/SBLK/GNK for Cape, Pana; SB for Post-Panamax;
   the crude/product/lng/container validators for their classes). Fleet-weighted,
   not modern-eco-subset (understates through-cycle opex), not bare median
   (ignores tonnage mix).
3. **Then** apply the outlier rule: exclude any name's normalized class-opex >25%
   from the cross-name median, and log the exclusion. (Definitional normalization
   first means this fires on *errors*, not on bundling differences.)

The per-name normalized opex inputs are read at compute time; this rule is frozen
before the spread is seen.

### 3c. Constants
- **N = 25 yr** (matches the `scrap_25yr` anchor). **Do not co-tune N with WACC** —
  both stiffen the CRF; tuning together double-counts.
- **operating_days = 360** (~98.6% utilization).
- **op_days reconciliation:** parity's 360 (~98.6%) vs the dividend strip's 2%
  off-hire (~98%, `DEFAULT_OFFHIRE_RATE`) **differ intentionally** — parity is a
  steady-state *newbuild* (no special survey for years), the strip is the actual
  aging fleet with scheduled drydocks, so the parity vessel legitimately runs
  marginally hotter. Registered so the two utilization numbers are not silently
  inconsistent (the smaller cousin of the P0 basis bug).

### 3d. Newbuild price + scrap (per class, from `vessel_value_curves.yaml`)
Read from the registered model curves, e.g. Cape NB **$74M** / scrap $13M; Pana
(Kamsarmax 82k) NB **$38M** / scrap $7.5M; Post-Panamax NB $38.5M / scrap $8M.
**Cape NB is $74M — the current replacement cost** (corroborated: Xclusiv broker
NB $75.5M; MB 208k Newcastlemax NB $81.5M). The brief's sanity check used a
**stale $63M**; a replacement-cost anchor must use the current number, so $74M is
registered (this is what re-centered the Cape prediction below — see §4).

## 4. Predictions (the falsifiable core) + halt conditions

At the registered **8% WACC**, with §3 inputs and the §2 PV-salvage formula:

| Class | NB | Predicted parity TCE/day | Halt band (±$500) |
|---|--:|--:|---|
| **Capesize** | $74M | ~$25.3k | **$24.8–25.8k** |
| **Kamsarmax (Pana 82k)** | $38M | ~$14.8k | **$14.5–15.5k** |

**If Cape lands outside $24.8–25.8k or Kamsarmax outside $14.5–15.5k → HALT and
investigate the registered input (opex, op_days, NB, scrap, formula) — do NOT
widen the band or adjust the output.** Honor the halt if it fires.

Every other class (Post-Panamax, Supra-Ultra, VLCC/Suezmax/Aframax, MR/LR,
LNGC/MGC, Ctr-\*) is computed in the same pass but carries **no pre-committed
level band** (priors existed only for Cape/Kamsarmax). No band is back-filled
after seeing the number; each is validated by §5 instead.

## 5. Validation gates (pass/fail, registered now, per basis)

### 5a. `historical_mean` basis → mean-reversion gate
- Test: does `(current 12M TC ÷ anchor)` predict the **sign** of the subsequent
  forward realized-rate change (ratio > 1 → rate falls; < 1 → rises)?
- **Pass = sign-consistent in ≥70% of ≥12 quarterly observations per class**, else
  the anchor is **rejected** for that class. (≥12, not 8: the Baltic series run
  40+ quarters, and 6/8 sign-consistency is ~14%-by-chance — too thin to mean
  anything.)
- **Data-gated:** needs the $/day Baltic series (deferred, §7). Registered now,
  *run* when the data lands. Until then the historical basis = current
  `historical_tce_means` values, flagged "unvalidated — pending Baltic series."

### 5b. `parity` basis → level + divergence-sign (NOT mean-reversion)
- **(a) Level:** the §4 Cape/Kamsarmax prediction (within band = pass).
- **(b) Divergence-sign cross-check:** the sign of `(historical_mean − parity)` per
  class must match an **independently observed orderbook-to-fleet ratio**. This
  gate passes ONLY once an actual orderbook ratio is placed next to the divergence
  per class — otherwise "historical < parity ⇒ under-ordered" and "under-ordered
  ⇒ thin orderbook" are the same claim wearing two hats (the circularity the
  cross-check exists to break). **Data-gated** like 5a. The provisional read
  (below) is NOT a pass.

## 6. Provisional signal (pending §5b — NOT a result)

Both dry-bulk classes read **historical < parity** (Cape $23.65k vs ~$25.3k, −7%;
Kamsarmax $11.9k vs ~$14.8k, **−24%**) → both structurally **under-ordered**,
Kamsarmax acutely. This is internally coherent and matches the qualitative thin
aging-Kamsarmax orderbook — but it is the **prediction**, not the confirmation;
§5b confirms it only against an independently observed orderbook ratio. **If the
Kamsarmax orderbook is NOT commensurately thin, that impugns the parity inputs**
(the more interesting finding).

**The SB stake.** SB is ~80% Pana-class by value, so whether its RONAV rises on
the parity basis is largely whether the Kamsarmax $11.9k → ~$14.8k (−24%) lift is
real. If §5b confirms the under-ordering, SB's "cheap on both bases" becomes
*more* robust — parity says the segment is structurally below replacement and
should re-rate up. If the historical basis holds and parity is rejected by §5b,
SB drifts to fair. Both are real outcomes; the pre-reg is now tight enough to
trust whichever the data picks.

## 7. Deferred (registered, run later)

- The $/day Baltic series (Cape→BCI 5TC, Pana→BPI 4TC, Supra-Ultra→BSI 10TC,
  containers→New ConTex/HARPEX) + the §5a mean-reversion run + the §5b
  orderbook-to-fleet ratios.
- Convergence: migrating cycle position onto the new historical-mean basis
  (separate pre-registered, delta-reviewed, re-ratified change).

---

# Amendment 1 (2026-06-29) — `newbuild_contract` input + per-class bands + resale invariant

**Frozen ahead of the recompute** (commit precedes results, as the original). Reason: the
original registered the parity NB price as the `vessel_value_curves.yaml` `newbuild` field —
a **conceptual conflation**. That field is the age-0 prompt/**resale** value (correct for NAV
marks); parity needs newbuild-**contract** replacement cost. They converge in some segments and
diverge where orderbooks run hot (2026 crude: 5yr tonnage trades *above* newbuild contracts). The
original Cape halt passed honestly-but-incompletely — Cape resale ≈ contract, so the wrong input
and the right input coincided. A level band cannot distinguish "correct input" from "wrong input
that happens to match here," so the fix is structural.

## A1.1 New registered input — `newbuild_contract` (distinct from the curve's resale `newbuild`)

In a new `inputs/market_data/newbuild_contract_prices.yaml` (parity-only; the NAV curve is
untouched). Broker contract for **every** class (no keep-vs-correct tolerance rule). VLCC resolved
on **reliability** (Clarksons, the authoritative newbuild-price benchmark) not repo-residence.

| Class | `newbuild_contract` | source (dated) |
|---|--:|---|
| VLCC | $128M | Clarksons benchmark Jun-2026 (xclusiv $131.5M corrob.) |
| Suezmax | $88M | Clarksons/market Jun-2026 |
| Aframax | $73M | market newbuilding cost Jun-2026 (xclusiv $75M corrob.) |
| LR2 | $73M | ≈ Aframax |
| MR | $52M | xclusiv 2026Q2 (2026-06-22) |
| Cape | $75.5M | xclusiv 2026Q2 (2026-06-22) |
| Pana (Kamsarmax) | $37.5M | xclusiv 2026Q2 |
| Supra-Ultra (Ultramax) | $34.5M | xclusiv 2026Q2 |

**Dry-bulk verification (the fact SB rests on):** repo curve `newbuild` Cape $74M / Kamsarmax $38M
are within −2% / +1% of these broker **contracts** (NOT the resale $81.5M / $46M) — i.e. the
dry-bulk curve field was already contract-basis, which is *why* SB's robust-cheap survived. Now
registered on the broker contract directly, SB's Pana parity moves $14,831→$14,701 (noise).

## A1.2 Frozen per-class parity bands (halt conditions, ±$500) — predicted before recompute

| Class | predicted | band | | Class | predicted | band |
|---|--:|---|---|---|--:|---|
| VLCC | $41,718 | $41.2–42.2k | | MR | $21,315 | $20.8–21.8k |
| Suezmax | $31,278 | $30.8–31.8k | | Cape | $25,753 | $25.3–26.3k |
| Aframax | $27,487 | $27.0–28.0k | | Pana | $14,701 | $14.2–15.2k |
| LR2 | $27,079 | $26.6–27.6k | | Supra-Ultra | $13,738 | $13.2–14.2k |

Every trusted class now carries an out-of-sample gate — complete, not crude-deep. Outside ⇒
investigate input.

## A1.3 Resale invariant — an INPUT-BASIS halt (gates the error a level band can't)

A level band gates the parity *level* against a prediction derived *from* the NB input — it cannot
catch an input that is wrong in a way self-consistent with its own prediction (resale-as-contract).
So register, per class, a dated broker **prompt-resale** reference and the invariant:

```
HALT (input-basis) if newbuild_contract ≥ prompt_resale[class]
```

Pointed at a clean **single-basis** broker resale reference — NOT `curve.newbuild`, whose basis is
inconsistent (resale for crude, contract for dry-bulk/MR), which would false-flag the corrected
Cape/MR. Kept as the slack inequality (resale strictly above contract is the hot/normal-market norm;
contract may legitimately approach resale in a soft patch — do not tighten to a margin). `prompt_resale`
is itself a dated registered input (xclusiv 2026Q2 resale for dry-bulk: Cape $81.5M, Kamsarmax $46M,
Ultramax $43M; broker resale for crude: VLCC $145M, Suezmax $95M, Aframax/LR2 $88.9M, MR $54M) so a
stale-high ceiling cannot quietly launder a stale-high contract.

**Validation:** passes all eight corrected classes; **fires on the original bug** — $175M-as-contract
≥ VLCC resale $145M → FLAG, with no one going to look. This is what makes "the system catches the
third instance" true.

## A1.4 Unvalidated — no gate (do not read as load-bearing)

- **Post-Panamax** — no broker contract mark; parity unvalidated.
- **LNGC / MGC / Ctr-\*** — no contract spot-check, AND the resale-vs-contract gap is *largest* where
  orderbooks run hot (membrane LNG worst), so inflated on the parity side by the same conflation, on
  top of boom-tilt on the historical side. **No validated normal rate on either basis** — suppressed
  from the headline subsector vector.

## A1.5 Pre-registered expected outcome (falsifiable; halt if it misses)

Crude under-ordering should **collapse** on contract NB: VLCC parity ≈ historical (−4%, not −26%);
crude parity median (~$31k) falls *below* the crude historical median (~$36.5k) → crude reads
**rich-or-fair on both bases**; the prior "crude flips to fair on parity" was the resale artifact and
should **reverse**. **SB / dry-bulk cheap stands** (verified ≈ contract). If crude does NOT collapse,
or SB flips on either basis — stop and investigate.

## A1.6 NAV-layer thread (logged as its own finding, weighted substantive — NOT a footnote)

The first conflation (parity borrowed the resale field) is fixed here by giving parity its own input.
But the verification exposed a **second, deeper** one: `curve.newbuild` — the age-0 **NAV** mark — has
**no consistent basis across sectors** (contract-ish for dry-bulk/MR at Cape $74M, resale at VLCC
$175M, and the VLCC value is plausibly stale-high even *as* resale vs a ~$145M prompt mark). So
cross-sector NAV comparisons inherit that inconsistency, and it sits **upstream of every crude P/NAV
and RONAV on both bases** — plausibly why crude justified reads look off in ways the parity fix alone
won't fully resolve. Separate P2-style NAV-curve thread (NOT bundled into P1); the questions it must
answer: (a) is the curve's age-0 field resale or contract, per sector, made consistent; (b) is VLCC
$175M stale-high even as resale.
