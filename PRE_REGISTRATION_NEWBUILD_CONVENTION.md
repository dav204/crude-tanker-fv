# Pre-registration — newbuild NAV convention (on-curve §9.6), pass 1: SB + SBLK

**Status: registered AHEAD of recompute.** Committed before any pipeline run on the
wired inputs. Predictions below are computed from the sourced 6-K schedules via the
*current* loaders (hand-built newbuild list, unmodified YAMLs); the wired pipeline must
reproduce them. A miss is investigated at the **input**, never by widening a band.

## §0 — Context: this is a book-wide defect; this pass fixes 2 of 12 names

The newbuild NAV convention is inconsistent across the book. nav.py computes a newbuild's
NAV contribution as `fleet_value(on-curve delivered_PV) − newbuild_capex_commitments +
newbuild_advances_paid`. Correct economic NAV = **delivered-market PV − remaining
obligation**, reachable two self-consistent ways:

- **A (BRUT/§9.6):** newbuild on the curve at delivered-market PV; `commitments` = REMAINING; `advances` = 0 (sunk into delivered value).
- **B (advances-gross):** on the curve; `commitments` = TOTAL contract; `advances` = paid. Algebraically identical to A.

The **error** is any name with nonzero newbuild fields but **no on-curve delivered value**.
The current book map (2026-Q1):

| Convention | Names | NB NAV contribution |
|---|---|---|
| on-curve OK (A/B) | BRUT, CAPT, FRO, MPCC | delivered_PV − remaining ✓ |
| advances-only (over-add) | **SB** (+100), CMBT (+760), TEN (+400) | +advances, no asset, no obligation |
| commitment-net (under-mark) | **SBLK** (−96), ASC, DHT, ECO, HAFN, NAT, STNG, TRMD, CCEC (−2,252) | −commitment, no asset |

Two sub-cases gate the treatment:
- **Fixable** (newbuild classes HAVE a curve mark): SB, SBLK, DHT, NAT, STNG, TRMD, HAFN, ASC → must go on-curve (A).
- **Structural** (no curve mark — Group-B LNG/container, fabrication forbidden): CCEC, CMBT → cannot go on-curve, but MUST be commitment-net, never advances-only.

This pass standardizes **SB + SBLK** (the two dry-bulk Kamsarmax peers, owner-scoped) onto
A. The remaining names are a registered follow-up queue (§4), each its own pre-registered
change — **never a batch fix to chase the guard green.**

## §1 — Mechanism applied

For SB and SBLK: add the 8 Kamsarmax newbuilds to the manifest as age-0 (`age: 0`)
vessels at their disclosed `dwt`, each with `years_to_delivery` from the 6-K delivery
schedule (PV-discounted by `1.11^(−ytd)` per nav.py §9.6); set `newbuild_capex_commitments`
= the disclosed REMAINING contracted price; set `newbuild_advances_paid` = **0**. Kamsarmax
(82,000–82,500 dwt) routes to the **Pana** class (curve age-0 / Resale = $46.0M, dwt-scaled
off the 82k baseline). No `yard` field (consistent with each name's existing on-water
fleet, which carries no yard discount). Commitment is subtracted at face (asset PV'd) —
the §9.6 convention as implemented for BRUT/CAPT.

## §2 — Sourced inputs (6-K, as-of 2026-03-31 — the NAV quarter-end)

**SB (Safe Bulkers) — CIK 1434754, Q1-2026 6-K `f061826sb6k.htm` (accession 0001317861-26-000033).**
Orderbook CHANGED between quarter-end and filing: at **2026-03-31 → 8 newbuilds**, "$97.8M
paid, **$227.5M remaining** capital expenditure requirements"; by June 12 → 11 (4 ordered in
Q2: 2 May Kam + 1 June Kam + 1 June Cape, all 2029; minus *Katerina* delivered April).
**Value the 8-NB March-31 state** ("trust the report at quarter-end"). The 8 March-31
Kamsarmaxes (all Pana class; no Capesize — that was a June order):

| # | dwt | delivery | years_to_delivery (from 2026-03-31) |
|---|---|---|---|
| Katerina | 82,000 | Apr 2026 | 0.04 |
| ×3 | 82,000 | 2026 (within-year midpoint) | 0.50 |
| ×2 | 82,000 | 2027 (midpoint) | 1.30 |
| ×1 | 82,500 | Q3 2028 (Jan-2026 Chinese order) | 2.38 |
| ×1 | 82,500 | Q1 2029 (Jan-2026 Chinese order) | 2.88 |

`newbuild_capex_commitments → 227,500,000` (was 0); `newbuild_advances_paid → 0` (was
100,040,000). Residual imprecision: the 6 pre-2026 hulls disclose delivery YEAR only;
within-year midpoint ytd used (sensitivity in §3).

**SBLK (Star Bulk) — CIK 1386716, Q1-2026 6-K `ex99-1.htm` (accession 0000950157-26-000639).**
Per-vessel "Under Construction" table — 8 × 82,000 dwt Kamsarmax (all Pana class):

| # | Vessel | yard | delivery | years_to_delivery |
|---|---|---|---|---|
| 1–2 | Star Emma, Star Evelina | Qingdao | Q2 2026 | 0.13 |
| 3–5 | Star Ellie, Star Bella, Star Kyra | Hengli | Q3 2026 | 0.38 |
| 6–8 | Star Irini, Star Aline, Star Affi… | Qingdao | Q4 2026 | 0.63 |

Note 6 (exact): "the total aggregate **remaining** contracted price … for the eight vessels
… was $195,556" ($k) — *remaining*, not total (total ≈ $295.6M ÷ 8 = $36.9M/Kamsarmax, a
sensible newbuild price). `newbuild_capex_commitments` stays **195,556,000** (already the
remaining — the prior YAML comment mislabeled it "total"); `newbuild_advances_paid → 0`
(was 99,999,000).

## §3 — Predicted NAV deltas + halt bands (registered AHEAD)

| Name | delivered_PV | new NB NAV | old NB NAV | NAV/sh | predicted | HALT band |
|---|---|---|---|---|---|---|
| **SB** | $327.5M | +$100.0M (−$227.5M, adv 0) | +$100.0M | 9.92 → 9.92 | **FLAT (−0.01%)** | beyond ±1.5% / ±$0.15/sh → investigate schedule |
| **SBLK** | $352.6M | +$157.1M (−$195.556M) | −$95.6M | 27.34 → 29.49 | **+$2.15/sh (+7.9%)** | outside +6.5%…+9.5% → investigate |

**AMENDMENT 1 (post-wiring, prediction-arithmetic correction — NOT band-widening).** SB
landed at **10.22 (+3.0%)**, outside the FLAT ±1.5% band; halt + investigate the input. Cause
found: the hand-prediction above used a **bare** vessel and omitted the **eco+scrubber
premium** `vessel_market_value` applies (+$4.3M on a $46M Pana age-0). Modern eco newbuilds
DO carry that premium, and **BRUT/CAPT/FRO set eco+scrubber=true on every NB row** — so
eco=true is the correct, *required-for-consistency* input (valuing SB's NBs on a different
basis than BRUT's would reintroduce the very inconsistency this fixes), not a knob turned to
fit. Re-derived WITH the premium: delivered_PV **SB $358.1M / SBLK $385.6M**; pipeline **SB
10.22 (+3.0%), SBLK 29.77 (+8.9%)** — reproduced exactly, and the all-names control confirms
**only SB + SBLK moved**. Corrected reads: **SB modestly UP +3.0%** (eco premium tips the
~flat balance up), **SBLK +8.9%**. The flat-vs-up *asymmetry* (back-loaded vs prompt) stands;
SB is "modestly up," not "flat." Recorded transparently: my registered band was missed because
my prediction arithmetic omitted a premium the correct input carries, not because an input was
wrong — the input is confirmed sound and BRUT-consistent.

**AMENDMENT 2 (eco/scrubber spec verified against each name's OWN 6-K — supersedes A1's
"BRUT-consistent" justification, which was the peer-flag trap).** A1 justified eco+scrubber=true
"for consistency with BRUT/CAPT/FRO." On owner challenge, that is the peer-number trap: BRUT's
spec is not evidence about SB's ships. Decomposing the premium — Pana age-0 **eco +$2.30M /
scrubber +$2.00M**, independent — and verifying each flag against each name's own filing
(adversarial workflow vs the live 6-Ks; both verdicts survived the refute):
- **eco** = the §3.1 mechanical rule (post-2014 build ⇒ eco), derivable from the disclosed
  delivery date. SB *and* SBLK deliver 2026+ ⇒ eco=true, rule-grounded and consistent book-wide.
- **scrubber** has NO build-year rule — must trace to an explicit NEWBUILD statement in the
  name's own filing. **SB: scrubber=FALSE** — SB's 6-K discloses scrubbers only on the existing
  45-vessel fleet, makes no newbuild scrubber claim, 2 NBs are dual-fuel methanol (no scrubber).
  **SBLK: scrubber=TRUE** — Note 6, "remaining contracted price, including scrubber installation
  costs, for the eight vessels under construction" (newbuild-specific).
Corrected outcome: **SB +1.6%** ($10.31→$10.47, eco-only) — the +1.4% scrubber portion was a
fabricated peer-borrowed flag, now removed; the registered "flat" prediction was closer to right
than +3.0% suggested. **SBLK +9.0%** unchanged (both flags disclosure-grounded). Combined SB
move (Thread-1 +5% + newbuild +1.6%) ≈ **+6.6%**, not +8% — still robustly cheap, wider margin.
**Durable fix:** `inputs/market_data/newbuild_specs.yaml` (per-name eco/scrubber + filing
citation) + a provenance guard asserting every on-curve NB's flags trace to disclosure, plus a
scrubber-verification xfail queue. **It also caught a latent instance: BRUT/CAPT/FRO carry
scrubber=true on VLCC/Suezmax newbuilds, never verified against their filings — now queued (their
VLCC scrubber premium dwarfs SB's). This guard is the precondition for the DHT pass.** Meta-lesson
recorded: when a prediction misses, suspect the input — and check it against the PRIMARY SOURCE,
not against what the peer does (crude age-0 $145M mislabel; now SB's scrubber flag).

**The headline finding: identical 8-Kamsarmax programs, opposite NAV direction.** SB ~flat
because its book is back-end-loaded (1 in 2028, 1 in 2029) — the PV discount on delivered
value offsets the embedded ordering gain (contracted ≈ $40.7M/NB vs $46M resale). SBLK up
because its book is prompt (all Q2–Q4 2026) — almost no PV haircut, embedded value flows
through. This is the canonical "cannot borrow the peer's number" case. SB ~flat is the
**second** input-driven reversal on SB (first: Post-Panamax split; the initial intuition
was "up"). If SB comes out anything but ~flat, that is the finding.

## §4 — Structural guard (three clauses; owner-specified) + the work queue

A name is `on-curve` / `commitment-net` / `advances-only` / `no-NB` by its balance-sheet
fields + on-curve newbuild presence. The guard:

1. **Fixable → must be on-curve.** A NB-carrying name whose newbuild classes have a curve
   mark MUST be `on-curve`. Hard-fail `advances-only` or `commitment-net`. (The real
   comparability guard; locks each name green-forever once fixed.)
2. **Structural → commitment-net, never advances-only.** A NB-carrying name on the
   enumerated structural-exempt list (no curve mark) is exempt from clause 1 but MUST be
   `commitment-net`; hard-fail `advances-only` (CMBT's defect). CCEC (already
   commitment-net) passes.
3. **Exemption enumerated in data.** Exempt from clause 1 only if on the structural list
   (`basis_status` Group-B sleeves). Any NB name neither on-curve nor structural-listed →
   hard-fail (the MR-hole guard: an unclassified name cannot land advances-only silently).

**Operational form:** the not-yet-converted names are the visible work queue, encoded as
`xfail(strict=True)` so the suite (and the in-suite drift gate) stays operable while the
queue reds honestly. A name leaves the queue ONLY via its own pre-registered fix; removing
a marker without fixing the name → strict xpass → hard fail. A new unclassified NB name →
immediate hard fail. **This pass removes SB + SBLK from the queue** (they become live green
assertions). Remaining queue after this pass: DHT, NAT, STNG, TRMD, HAFN, ASC (fixable,
each its own future pre-reg), CMBT (advances-only → commitment-net, its own change). CCEC
passes as-is; its "is the liability right / should there be an offsetting asset" question is
logged as a SEPARATE methodology item, not bundled (and CCEC is scorecard-suppressed anyway).

## §5 — Control / falsification

Only SB and SBLK manifests + balance sheets change. Therefore in the all-names diff:
**only SB, SBLK, and aggregate/median rows derived from them may move.** The on-curve four
(BRUT/CAPT/FRO/MPCC) and CCEC stay green on the guard; **no other name's NAV may move** (no
curve/mark/scenario change). If any other name's NAV moves → halt and investigate.

## §6 — Pass/fail gates

1. `pytest -q` green incl. the new three-clause guard (SB+SBLK live-green; queue xfail).
2. Pipeline reproduces §3: SB within ±1.5%, SBLK +6.5%…+9.5%. Else investigate the input.
3. All-names diff: only SB/SBLK (+ their aggregates) move (§5).
4. `/reconcile sb sblk` SANITY = OK (±50% bug gate).
5. Decision logs `sb_log.md` / `sblk_log.md` annotated (methodology/convention change, not
   a market move). **SB combined-effect note (one place):** SB has now moved twice on
   adjacent bases — Thread-1 dry-bulk age-0 (+5%, less cheap on NAV denominator) and this
   newbuild-convention (~flat). Net: SB modestly less cheap than pre-Thread-1, still
   robustly cheap on both bases. State the combined effect explicitly in the scorecard.
6. PAUSE for owner review before re-ratify (separate attributable step).

---

## AMENDMENT 3 — CAPT scrubber over-broad correction (Tier-1 verification result)

**Registered AHEAD of the VLCC/LR2 recompute.** The Aframax slice landed via PR #3
(`AFRA_2018`, scrubber=false, merged). This registers the remaining slice.

**Finding (adversarially verified vs CAPT's own sources — Pareto initiation 2026-04-20
per-vessel ledger + Euronext Information Document §7.3.2 + Q1-2026 earnings release):** CAPT's
blanket `scrubber=true` was OVER-BROAD. Verified split is **18 of 30 scrubber-fitted (~60%)**:
VLCC 6/12, Suezmax 10/10, Aframax 0/4, LR2 2/4. The 12 LNG-dual-fuel vessels carry NO scrubber.

**Manifest correction (the VLCC/LR2 slice; Aframax 0/4 already done in PR #3):**
- `VLCC_nb_2027` (count 7, scrubber true) → 3 scrubber-true + 4 LNG-only (scrubber false).
- `VLCC_nb_2028` (count 4, scrubber true) → 2 scrubber-true + 2 LNG-only (scrubber false).
- `LR2_2026` (count 2, scrubber true, on-water) → scrubber false (Androklos/Athinagoras LNG-only).
8 vessels (6 VLCC + 2 LR2) lose the fabricated scrubber premium.

**Predicted NAV — ON THE ANCHORED (HEADLINE) BASIS** (process fix: `compute_nav` on raw inputs
is UN-ANCHORED; the headline/drift-gate uses `use_transaction_anchored` default-on):

| Slice | Anchored (headline) | Un-anchored (diagnostic) |
|---|---|---|
| Aframax (PR #3, merged) | +0.08% | −0.27% |
| VLCC/LR2 (this slice) | −0.71% | −0.70% |
| **Combined CAPT** | **−0.63% (−$0.099/sh)** | −0.97% |

The Aframax sign flips between bases (anchoring steepens the Aframax 10yr leg $68M→$61M); the
VLCC/LR2 slice agrees on both (flat scrubber premium). **Re-ratify keys off the anchored −0.63%.**

**Registry + guard:** CAPT → `scrubber: mixed`, `scrubber_nb_count: 13` (NB scrubber-fitted:
5 VLCC + 8 Suezmax), `scrubber_verified: true`, sourced to the ledger. The provenance guard gains
a mixed-name branch (NB scrubber COUNT must match the registered count — the contradiction check
for non-uniform names). CAPT clears the scrubber-verification queue (BRUT/CAPT/FRO all verified).

**Gate:** only CAPT moves; SANITY OK; combined −0.63% annotated + re-ratified once.

---

## CONVENTION QUEUE — pass 1: DHT (registered AHEAD of recompute)

DHT Holdings — first fixable convention-queue name. Currently **commitment-net −$21.8M**
(advances $55.676M − commitment $77.481M, NO on-curve asset): DHT Impala's ~$175M delivered
value is entirely missing from NAV (the SBLK pattern). Tool NAV is **−12.9% BELOW broker**
($13.10 vs $15.05), so the §9.6 fix moves DHT TOWARD consensus, not away.

**Sourced inputs (adversarially verified vs Q1-2026 6-K, acc 0000950157-26-000576, Note 5 —
both figures EXACT to the in-repo balance sheet, nothing overturned):**
- **DHT Impala** — the ONLY vessel under construction at 2026-03-31 (the other 3 of the 4-VLCC
  program delivered in Q1). VLCC, ~300k dwt (VLCC is flat-per-class, dwt immaterial to value).
- Delivery **June 2026** → `years_to_delivery ≈ 0.25` from 2026-03-31.
- Remaining commitment **$77,481,000** (Note 5 future-payments, due within 12 months) — stays.
- Advances **$55,676,000** ("Vessels under construction" carrying amount) → **0** (sunk into the
  on-curve delivered value, the BRUT/§9.6 convention).
- **scrubber = true** — Note 5: "four large VLCCs, fitted with exhaust gas cleaning systems"
  (Impala is one). eco = true (§3.1 post-2014 build). NB scrubber verified; the operating-fleet
  100%-scrubber claim is NOT in this 6-K — DHT stays in the Tier-2 operating-scrubber audit queue.

**Mechanism:** add DHT Impala to the manifest as a 1× VLCC age-0 row (ytd 0.25, scrubber+eco),
set `newbuild_advances_paid → 0`, keep `newbuild_capex_commitments 77,481,000`.

**Predicted NAV — ANCHORED (headline) basis** (the move is purely the age-0 delivered value,
which anchoring does NOT change, so identical $/sh on both bases — no sign-flip risk):

| Basis | DHT NAV/sh | Δ |
|---|---|---|
| **Anchored (headline / re-ratify)** | 13.10 → 13.88 | **+$0.786 / +6.0%** |
| Un-anchored (diagnostic) | 15.29 → 16.07 | +$0.786 / +5.1% |

Moves DHT from −12.9% to ~−7.5% vs broker (toward consensus). **HALT band:** outside +5%…+7%
anchored → investigate the input.

**Gate:** only DHT moves; SANITY OK (still below broker); +6% annotated; PAUSE for owner review
before re-ratify. Registry: DHT → eco/scrubber true, NB scrubber_verified true (operating still queued).
