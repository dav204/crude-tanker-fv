# LR1 contract-floor + `resale-corroborated` taxonomy — pre-registration

**RULED 2026-07-15 (owner verbatim: "rule the LR1 fork — taxonomy (b) + contract-floor,
post-Stage-A").** Fork (i) of `decisions/lr1_level_evidence_2026-07-15.md` + its §4
taxonomy option (b). **Frozen ahead; execution POST-STAGE-A** (the tanker-forward Stage-A
promotion ≤ 2026-08-15 runs first — one FV-moving event in flight at a time). Folded with
the `decisions/mr_secondhand_resumption_2026-07-15.md` §5 extract-refresh rider into ONE
post-Stage-A **anchor-refresh round** (one attributable step, one drift review); ordering
vs the D-M2 sweep confirmed by the owner at Stage-A close (default: anchor round first —
routine dated-source maintenance before a methodology sweep).

## 0. What was ruled

1. **Level fix (fork i):** LR1 age-0 → the dated broker **NB-contract floor**; 5yr → the
   dated intermodal 5yr. Clears the curve inversion (wired age-0 59 < dated 5yr 60 < dated
   NB 61) with zero derivation — the exact Handysize contract-floor precedent (2026-07-15).
2. **Taxonomy (b):** a new scoped basis status **`resale-corroborated`** so a class with NO
   broker Resale line anywhere can stop pinning the tier of names whose holdings in that
   class cannot mathematically feel the missing mark.

## 1. Registered inputs — METHOD fixed now, marks re-dated at execution

Reference marks today: age-0 **$61.0M** = xclusiv 2026-07-13 Panamax-tanker NB (the LOWER
and hence more conservative of the two current contract prints; MB 2026-06-26 $64M is the
cross-check, kept unwired per convention); 5yr **$60.0M** = intermodal W29 (mark date
2026-07-10, issue 07-14; unchanged w/w).

**Freshness rule:** execution is ~4+ weeks out. At execution, re-pull the then-current
xclusiv NB and intermodal 5yr and wire THOSE values under the same method (contract-floor
age-0, dated 5yr). The §3 bands are registered at today's reference marks and **recompute
mechanically** (deltas are linear in the node moves — formula in §3); a re-computed band is
not a re-registration. If either source has gone stale (>1 quarter) at execution, HALT —
the method requires two current dated marks.

## 2. The wiring (execution step, all in one attributable commit)

- `vessel_value_curves.yaml` LR1: `newbuild` 59.0M → **61.0M**★, `five_year_benchmark`
  53.5M → **60.0M**★ (★ = execution-date re-pull, §1). `ten_year_benchmark` 42.0M
  **UNTOUCHED** — no current 10yr print; the 12–17yr LR1 books (TRMD/HAFN/TEN/INSW-old)
  mark off the 10yr→scrap segment, which stays **broker-static** (recorded limitation,
  same posture as Handy-Bulk mid-age; a future intermodal/xclusiv 10yr line retires it).
  Monotonicity after wiring: 61 ≥ 60 ≥ 42 ≥ 7.7 ✓ (the inversion clears).
- `newbuild_contract_prices.yaml` `prompt_resale` LR1: add **61.0M**★, contract-floor
  labeled (Handysize precedent: prompt resale ≥ contract in this market, so contract is a
  conservative floor).
- `newbuild_contract` LR1: **stays OMITTED** (reversing the PLAN note "wire with the LR1
  ruling"). Rationale: with age-0 itself on the contract floor, contract-vs-resale parity
  is degenerate (ratio ≡ 1.0 at age-0) — wiring it would force an equality-exemption into
  the `newbuild_contract >= prompt_resale` HALT invariant, weakening a real guard to buy a
  meaningless diagnostic. Revisit only when an independent LR1 resale mark exists.
- `basis_status.yaml` LR1: `pending-sourceable` → **`resale-corroborated`**.
- **Taxonomy (b) implementation:**
  - `loaders.VALID_BASIS_STATUS` += `resale-corroborated`.
  - Scorecard severity order: `structural-unavailable` > `pending-sourceable` >
    `unverified-no-current-xclusiv-line` > `resale-corroborated` > `resale-uniform`.
  - **Rollup rule (the scoped part):** `resale-corroborated` counts as uniform-EQUIVALENT
    for a name **iff every hull the name holds in that class has age ≥ 10** (the wired
    age-0/5yr nodes influence ages < 10 only — [0,5] and [5,10] segments); otherwise it
    degrades to `pending-sourceable` for that name. Qualification for the STATUS itself
    (class-level): no broker prints a Resale line for the class (verified sweep on record)
    AND both a dated contract floor and a dated second-house 5yr, current ≤ 1 quarter.
  - **Today LR1 is the ONLY qualifying class** — the definition self-limits: product
    Handysize fails (no dated second-house 5yr exists — no broker tabulates the class at
    all), Handymax fails (no marks of any kind), VLGC fails (no dated broker 5yr line).
    This is a scoped status, NOT a general loosening; qualification is per-class,
    pre-registered, never back-filled.
  - `AGE0_BASIS["LR1"]` → dated exception string citing this ruling + both marks; NEW guard
    `test_resale_corroborated_class_marks`: every `resale-corroborated` class's age-0 ==
    its registered contract floor AND 5yr == its registered dated 5yr (both with dates).
  - NEW guard (the young-hull honesty lock): **INSW's rollup must read `pending-sourceable`
    while it holds age<10 LR1** (ages 0/1 today); TRMD/HAFN roll up uniform-equivalent.
    A new young LR1 hull arriving in any manifest auto-degrades that name — test-enforced,
    not attention-dependent.
- `provenance.TIER_SUBREASON`: **TRMD `basis-pending` REMOVED** → tier derives
  **VALIDATED-TIGHT** (the 7th). Named review checkpoints AT THE BOUNDARY (owner eyeball
  before the re-ratify, Thread-1 §6 pattern):
  1. **Cap check (2343 comparator):** TRMD's LR1 sleeve = **$342.3M = 8.7% of fleet value
     / 10.5% of NAV** (computed 2026-07-15) vs 2343's 51%-of-hulls cap trigger —
     sub-material, and the sleeve's marks sit on the 10yr/scrap nodes this wiring doesn't
     touch. No `UNANCHORED_VALUE_CLASS_CAP` entry recommended; owner confirms.
  2. **Sign-stability read:** TRMD is weight-sign-unstable (EV family −10.1/+8.4). Under
     the tier rule TIGHT needs traced inputs + strong corroboration — TRMD's external
     corroboration is the book's best (k 1.03) — and sign-stability is a W-frag/handoff
     caveat, not a tier input. But the owner flagged it 7/13; it prints beside the tier
     either way. Owner confirms TIGHT lands with the W-frag caveat visible.
  3. TRMD sits in the Stage-A eyeball inventory (post-re-tilt BUY) — the anchor round runs
     AFTER Stage A precisely so these don't overlap.

## 3. Predicted movers (registered at today's reference marks; recompute at execution)

Verified through `compute_nav` on the live manifests (not hand math alone; both agree):

| Name | ΔNAV | Δ% asset NAV | mechanism |
|---|--:|--:|---|
| **INSW** | **+$7.80M** (+$0.157/sh on 49.7M sh) | +0.27% | 1 age-0 hull +$2.0M; 2 age-1 hulls +$2.9M each (0.8×Δage0 + 0.2×Δ5yr) |
| **TEN** | **+$1.17M** (+$0.039/sh) | +0.04% | ages 9.5/9.6 pair on the [5,10] segment ((10−a)/5 × Δ5yr) |
| TRMD | $0.00 exactly | 0 | LR1s age 13–14, past the 10yr node |
| HAFN | $0.00 exactly | 0 | LR1s age 12–17 |
| all others | 0 | 0 | no LR1 tonnage |

Delta formula for the execution-date recompute: per hull, Δv = Δage0·(1−a/5) + Δ5yr·(a/5)
for a<5; Δv = Δ5yr·((10−a)/5) for 5≤a<10; 0 for a≥10.

Both movers are far sub-drift-bar; **no re-ratify expected** unless bundled with the
extract-refresh rider's movers in the same round (then one combined ratify with per-name
annotation). **basis/tier outcomes:** TRMD nav_basis → uniform-equivalent → **TIGHT** (the
step's purpose); INSW nav_basis STAYS `pending-sourceable` (young hulls — the degradation
rule binding on purpose, its INSW-side resolution is a real LR1 Resale line, nothing else);
TEN/HAFN composites unchanged (structural / Handysize+pool).

**Halt conditions:** any name outside this table moves; INSW/TEN move outside ±20% of the
formula-recomputed bands; any band flip not pre-listed; TRMD or HAFN move at all (they are
the controls — a nonzero move means the rollup or curve wiring is wrong).

## 4. What this does NOT do

- Does not touch the LR1 `ten_year` node (§2 limitation) or any other class.
- Does not give INSW a basis upgrade (young hulls stay honestly pending).
- Does not create a general path around `resale-uniform` — §2's qualification rules keep
  `resale-corroborated` a one-class status today, extendable only by a new pre-registration.
- Does not execute before Stage A closes. Nothing in this document moves a number today.
