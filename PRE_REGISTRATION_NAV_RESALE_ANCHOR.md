# Thread 1 — uniform prompt-resale age-0 NAV anchor — pre-registration

**Frozen ahead of the recompute** (commit precedes results, the project discipline).
This is the **headline-NAV-moving** execution of the NAV-layer thread registered as
`PRE_REGISTRATION_NORMAL_RATES.md` §A1.6 — a P2-style change (drift-gated + re-ratified),
NOT a diagnostic amendment. It closes the last known *systematic* comparability defect:
`curve.newbuild` (the age-0 NAV mark) is on **inconsistent bases across sectors**.

## 0. Framing — what is and isn't in scope

- **In scope:** the **age-0** curve anchor (`vessel_value_curves.yaml` `newbuild`) only,
  made uniformly **prompt-resale** across all sectors, from a single dated source.
- **Out of scope (unchanged):** the **mid-age** leg (ages 5/10), which is governed by
  §9.9 transaction anchoring (S&P prints — already a market/resale basis); `cycle.py`
  (frozen, D1); the parity normal-rate layer (its own `newbuild_contract` input, A1.1).
- **The deliverable is the corrected, *comparable* book** — not a target number. A miss
  on any registered gate halts and sends us to the **input**, never the band.

## 1. The defect (confirmed)

`curve.newbuild` means different things by sector. Dry-bulk dwt-scaled classes carry
**contract** replacement cost; everyone else carries **resale**. The schema comment
("age 0 (prompt/resale value)") is true for crude/product/LNG/container, false for dry-bulk.

| Class | curve age-0 (now) | basis (now) | dated resale (A1.3) | contract (A1.1) |
|---|--:|---|--:|--:|
| VLCC | $175M | resale (stale-high) | $145M | $128M |
| Suezmax | $108M | resale (stale-high) | $95M | $88M |
| Aframax | $90M | resale | $88.9M | $73M |
| LR2 | $90M | resale | $88.9M | $73M |
| MR | $49.5M | resale (stale-low) | $54M | $52M |
| Cape | $74M | **contract** | $81.5M | $75.5M |
| Pana (Kamsarmax) | $38M | **contract** | $46M | $37.5M |
| Supra-Ultra (Ultramax) | $38M | **contract** | $43M | $34.5M |
| Post-Panamax | $38.5M | mixed/implicit | $46M | $37.5M (= Kamsarmax) |

This sits **upstream of every crude/dry-bulk P/NAV and RONAV on both bases**, so cross-name
comparisons inherit the inconsistency. (A1.6 logged this; this doc executes it.)

## 2. The fix + single-source consolidation

Set the age-0 anchor to the **dated prompt-resale** value, uniformly, for the 9 classes that
carry a dated mark. The `prompt_resale:` block in `newbuild_contract_prices.yaml` (registered
A1.3, committed 2026-06-29) becomes the **single canonical dated source** feeding **both**:
(a) the NAV age-0 anchor (this thread), and (b) the parity resale-invariant ceiling (A1.3).

A test (`test_curve_age0_equals_prompt_resale`) asserts `curve.newbuild == prompt_resale[class]`
for the 9 marked classes, so the two can never silently drift apart (fix the *class* of error).

## 3. Registered inputs (dated; from A1.3 — repeated for self-containment)

VLCC $145M, Suezmax $95M, Aframax $88.9M, LR2 $88.9M, MR $54M (crude/product, broker resale
Jun-2026 / xclusiv 2026Q2); Cape $81.5M, Pana $46M, Supra-Ultra $43M (xclusiv 2026Q2 resale);
Post-Panamax $46M (= Kamsarmax resale, the replacement-equivalent). No new sourcing in this
thread — these marks are already dated and committed.

**Group A (sourceable, deferred to Thread 1A):** LR1, Handysize, Handymax — no dated resale mark
yet; left on current basis, flagged `pending-sourceable`. **Group B (structural):** LNGC, MGC,
Ctr-Feeder/Intermediate/Large — no clean resale market; left as-is, flagged `structural`, never
manufactured. (See §8.)

## 4. Structural guard #2 — crude depreciation-rate plausibility (run BEFORE wiring)

The concern (raised in review): VLCC age-0 resale $145M vs the **static** 5yr $138M is a −4.8%
drop, implausibly thin, and the resale mark was *constructed as* "5yr + delivery premium," so the
two could be a stale pair masking each other. **Resolved by running the check against the
PRODUCTION (transaction-anchored) curve actually used** — not the static YAML:

| Class | new age-0 | production 5yr (txn-anchored) | new→5yr dep% | clamp binds? |
|---|--:|--:|--:|---|
| VLCC | $145M | **$113.2M** | **21.9%** ✓ | no (113 < 137.8 ceil) |
| Suezmax | $95M | $86.3M | **9.2%** (thinnest) | no |
| Aframax | $88.9M | $78.7M | 11.5% ✓ | no |
| LR2 | $88.9M | $77.8M | 12.5% ✓ | no |
| MR | $54M | $46.1M | 14.7% ✓ | no |
| Cape | $81.5M | $63.1M | 22.6% ✓ | no |
| Pana | $46M | $35.5M | 22.9% ✓ | no |
| Supra-Ultra | $43M | $29.3M | 32.0% ✓ | no |
| Post-Panamax | $46M | $34.0M | 26.1% ✓ | no |

**Finding:** the "−4.8% thin" figure was a **static-YAML artifact**. Production anchors the VLCC
5yr to **$113.2M** from real S&P prints — *independent* of the broker resale mark — giving a
healthy **21.9%** slope. The "not-independent" failure mode cannot occur in production (5yr from
transaction prints, age-0 from broker resale: different data). The clamp `[scrap×1.5, newbuild×0.95]`
does **not bind** for any class after the change (anchored 5yr below the new ceiling everywhere),
so the age-0 edit does not perturb the mid-age.

- **Registered floor: 8%** new→5yr depreciation on the **production** curve. All 9 pass.
- **Suezmax 9.2%** is the thinnest; it clears the floor and is a genuine transaction-anchored slope
  from independent sources (anchored 5yr $86.3M vs broker resale $95M), not a stale-mark artifact.
  Noted, not halted.
- **Answer to A1.6(b):** VLCC $175M was stale-high; $145M is the current dated mark and is **not**
  stale relative to the production 5yr. ✓
- **Out of scope (logged):** the *static* un-anchored 5yr ($138M) is itself stale-high (production
  corrects it to $113M via §9.9); refreshing the static mid-age baseline is a §9.9-adjacent item,
  NOT bundled here. Consequence: the un-anchored baseline diagnostic (use_transaction_anchored=False)
  will show a thin 0–5 crude slope — a known property of that diagnostic, not the production mark.

## 5. Structural guard #1 — monotonicity + single-source consistency

- `test_curve_anchors_monotonic`: `newbuild ≥ five_year ≥ ten_year ≥ scrap` per class on the static
  curve. Necessary, not sufficient (checks ordering, not spacing — §4 covers spacing). All 9 changes
  verified monotone by hand.
- `test_curve_age0_equals_prompt_resale`: the single-source invariant (§2).

## 6. Undelivered-newbuild-hull basis — resolved explicitly (with code/manifest evidence)

Verified in `nav.py` (ll.84–100) + `brut.yaml` + `capt.yaml`: undelivered hulls
(`years_to_delivery > 0`) are carried at the **age-0 delivered-market value on the curve**
(= `curve.newbuild` = the resale anchor), PV-discounted by `1.11^(−ytd)`, with the remaining
contract obligation held **separately** as a balance-sheet commitment. This is the locked
§3.1/§9.6 convention (FRO/BRUT/CAPT precedent), which **explicitly rejects** sunk-cost/contract
marking ("delivered market less remaining commitment, NOT sunk cost").

- **Conclusion:** the curve age-0 point *correctly* applies to undelivered hulls as their
  delivered-market value, so **BRUT moves and is the largest single mover — the prediction holds.**
  Marking those hulls at `newbuild_contract` instead would be the sunk-cost approach §9.6 forbids
  and would double-count the obligation already on the balance sheet. **Named review checkpoint at
  the boundary** — the owner can object before re-ratify.
- **Defect found:** the `nav.py` docstring (ll.12–14, "Vessels still under construction are NOT
  valued on the curve") is **stale** — contradicted by the code and both manifests. Fixed in this
  thread (it documents the very path Thread 1 moves).

## 7. Mechanism + predicted mover set (falsifiable) + halt conditions

**Mechanism (registered):** in the production curve the age-0 anchor governs **only the 0→5yr
interpolation segment**. A vessel's mark changes **iff age < 5** (scaled by `1 − age/5`); newbuilds
(age 0, incl. undelivered) take the full delta (PV-modulated); vessels **≥5yr are unaffected**
(transaction-anchored mid-age). So a name moves **only to the extent it holds young (<5yr / newbuild)
corrected-class tonnage** — a far more *surgical* effect than "all crude/dry-bulk names move."

Per-class age-0 delta: VLCC −17%, Suezmax −12%, Aframax/LR2 −1%, MR +9%, Cape +10%, Pana +21%,
Supra-Ultra +13%, Post-Panamax +20%.

**Predicted to MOVE (9 names; young corrected tonnage, from the manifest age scan):**
- **DOWN (crude young/newbuild):** **BRUT** (12 VLCC newbuilds — largest, max-torque), **CAPT**
  (27 young crude — large), **FRO** (18 young VLCC), **ECO** (6), **DHT** (3), **TEN** (11, net down).
- **UP (dry-bulk young):** **CMBT** (40 young, net up but **mixed** — 30 dry-bulk up vs 10 crude
  down), **SB** (13 young Pana/PPMX — **modest**; its old Pana/Post-Panamax bulk is unaffected),
  **GNK** (2 — tiny).

**MUST NOT MOVE — the hard control (13 names):**
- **No corrected tonnage:** FLNG, CCEC (LNG), MPCC, GSL (container).
- **Corrected tonnage all ≥5yr** (already transaction-anchored at mid-age, so nothing reprices):
  ASC, CMDB, HAFN, INSW, NAT, SBLK, STNG, TNK, TRMD.

**Halt conditions:**
1. **Control gate:** if ANY of the 13 control names moves (>0.5% NAV) → HALT, investigate the wiring.
2. **Sign gate:** every mover must match its predicted net sign (crude-young down, dry-bulk-young up;
   CMBT net-up-but-mixed) → a sign violation HALTS.
3. Magnitudes are age-weighted and **reported at the boundary**, not pre-banded per name (priors
   exist only at the class level — no band is back-filled after seeing the number).

**Honest correction registered:** the roadmap's "dry-bulk NAV up / SB much less cheap" is **modest
and surgical** — SBLK (135 mature ships) is FLAT, SB moves only on its young sliver. The basis fix is
nonetheless **complete**: dry-bulk mid-age was already market-basis via transaction prints; only age-0
was on contract, and only young hulls touch age-0.

## 8. `basis_status` — single per-class source of truth

A per-class `basis_status` (in the curve data or a dedicated `basis_status.yaml`), values
`resale-uniform` / `pending-sourceable` / `structural-unavailable`. The per-name rollup (Thread 4)
**derives from** it — `resale-uniform` only if all a name's tonnage is corrected; any Group-A
tonnage ⇒ `pending`; any Group-B ⇒ `structural`. Pinned at class level so it cannot drift from the
wiring. **This is independent of mover status** — a FLAT name (e.g. SBLK) is still `resale-uniform`;
INSW is still `pending-sourceable` (holds LR1).

## 9. Pass/fail gates (summary)

- `pytest -q` green incl. the two new structural-guard tests.
- All-names `git diff outputs/`: mover set ⊆ the 9 predicted; the 13 control names unchanged.
- `/reconcile --all` SANITY all OK / n-a-APPROX (±50% bug gate).
- Guard #2 floor (8% production depreciation) holds for all 9 (already verified, §4).
- Drift gate: intended movers "explained" (post-annotation, against the hardened X9 detector), then
  re-ratified as a **separate** attributable step **after owner review**.

## 10. Re-ratify discipline

Headline-moving ⇒ after the boundary review: `./scripts/ratify_baseline.sh "Thread 1: uniform
prompt-resale age-0 NAV anchor"` → review the baseline diff → human commit. Not before review.
