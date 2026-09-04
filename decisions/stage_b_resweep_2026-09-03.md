# Stage B tanker re-anchor — CORRECTED sweep, for owner ruling (window closes 2026-09-04)

**Status:** SWEEP COMPLETE, NOTHING PROMOTED. Stage B cannot execute mechanically: its own
pre-registration fires a **registered §5 HALT** (§4 below), and the rule leaves five
questions unwritten (§6). Both are owner input by construction.

**Authority:** `PRE_REGISTRATION_TANKER_CLUSTER_REANCHOR.md` §6 — *"Recompute the §3 medians
with the tail included. Execute a second promotion only if any class-bucket median moves
>±10% vs the Stage-A anchor; otherwise commit a record-no-change note and stand down."*
Anchors under test are the Stage-A holds of 2026-08-10.

**Why this supersedes the first pass:** an adversarial verification rejected the first sweep
for an incomplete evidence base. Two qualifying disclosures were missing, one of them the
venue `inputs/reweight_triggers.yaml` names FIRST. Both are re-verified verbatim here.

## 1. The two disclosures the first pass missed (verified at source)

**CAPT's Q3 booking IS class-split.** `inputs/research_pareto/2026/09/2026-09-02_CapitalTankers-CompanyReport-QuarterlyReview-2026-09-02-528090.pdf`, verbatim:

> "Into Q3, 71% / 82% of suez / aframax days have been booked at $130,240 / $105,765/day,
> respectively. Including the VLCC on TC closer to $100,000/day – 79% of total fleet days are
> fixed at $113,681/day."

The first pass excluded this as un-split. It is split, and it is the single largest mover in
the Aframax bucket. (Unreconciled: `decisions/capt_log.md:133` records a fleetwide *78% @
$115,268* against Pareto's *79% @ $113,681* — UNVERIFIED which is the issuer's own figure;
the CAPT 9/01 release settles it. It does not affect the class-split legs used here.)

**TRMD's Stage-B basis was never swept** — and the trigger card names it first.
`decisions/trmd_log.md:288-292`, verbatim:

> "STAGE-B BASIS CAPTURED (condition 5) — the report's own coverage table, as of 2026-08-18:
> Q3-26 LR2 83% @ $49,255 · **LR1 61% @ $32,608 — the FIRST direct LR1 front print, the
> anchor-round class** · MR 71% @ $35,247 · total 73% @ $38,606"

**Also corrected:** MB's `LR2[TC1]` and `LR1[TC5]` are **clean** assessments
(`decisions/stage_a_computation_draft_2026-08-09.md:61-63`), so the first pass's
"Afra + LR2[TC1] → +11.27%" variant is void — it routed a clean assessment into the dirty
bucket while using the same series for LR2_clean elsewhere. HAFN's "Q3 QTD 80% @ 30.7k
fleet-wide" (`decisions/hafn_log.md:1558`) IS correctly excluded as un-split — recorded here
as considered, not silently dropped.

## 2. Corrected bucket table (medians of qualifying fixtures; anchors = Stage A 2026-08-10)

| Bucket | Anchor | Pool | Median | Δ | Verdict |
|---|--:|---|--:|--:|---|
| **Aframax/LR2-dirty front** | 59,900 | 59,900 · 81,000 (FRO LR2) · **105,765 (CAPT)** | 81,000 | **+35.23%** | **BREACH** |
| ⤷ if FRO's LR2 does not route dirty | 59,900 | 59,900 · 105,765 | 82,833 | **+38.28%** | **BREACH** |
| **LR2_clean front** | 65,000 | 65,000 · **49,255 (TRMD)** | 57,128 | **−12.11%** | **BREACH — NEW** |
| **LR1_clean front** | 46,400 | **32,608 (TRMD)** | 32,608 | **−29.72%** | **BREACH — NEW** |
| **Suezmax 12M** | 58,050 | 74,500 · 80,000 | 77,250 | **+33.07%** | **BREACH** |
| **VLCC front** | 179,650 | 206,600 · 152,700 · 156,900 · 125,400 | 154,800 | **−13.83%** | **BREACH** |
| **LR1 term** | 38,000 dirty / 20,250 clean | 26,250 (Kk Marlin, *extension*) | 26,250 | −30.9% / +29.6% | **BREACH either way** |
| LR2_clean term | 28,000 | N=0 fixtures; MB 3yr 40,000 | 40,000 | +42.86% | BREACH **iff assessments count** (Q-3) |
| Aframax/LR2 12M | 51,450 | 52,500 · 55,000 · 57,000 · 60,000 | 56,000 | +8.84% | holds — **knife-edge**; 57,000 (+10.79%) with assessments |
| Suezmax front | 118,900 | 104,800 · 117,400 · 117,600 · **130,240** · 133,000 | 117,600 | −1.09% | holds |
| MR front | 29,300 | 29,000 · 29,600 · **35,247** | 29,600 | +1.02% | holds |
| VLCC 12M · VLCC term · Afra term · MR 12M · MR term · LR1_clean 12M · LR2_clean 12M · Handy* | — | — | — | 0 to +5.8% | hold |

**Six buckets breach on fixtures alone.** There is no reading under which Stage B stands down.

## 3. What changed vs the first pass, and why it matters

The first pass put **STNG, TRMD, HAFN and ASC on the forward-invariance list** — names that
must move EXACTLY 0.0. With the clean-product breaches (LR2_clean −12.11%, LR1_clean
−29.72%) **those names are MOVERS**. That is the single most consequential correction: an
invariance claim that is false is exactly the shape of error that ships a wrong number under
a green gate.

The halt tripwire also moves. The first pass named **BRUT**, which cannot fire it: BRUT
carries `POSITION_UNRELIABLE` and `weight_sign_stable: false`, so it can never display BUY.
The genuinely exposed name is **STNG** — HOLD, `weight_sign_stable: true`, and the book's
largest LR2_clean holder — whose direction under a clean-front cut must be established
before, not after, the regen.

**Dedupe correction to the standing record.** `decisions/sp_promotion_round_2026-09-01.md`
calls the Suezmax 12M evidence "triple-corroborated (Sea Topaz 80.0k, Monte Urbasa 74.5k,
this 74.5k)". The Pareto 9/01 item — *"a 1Y TC at $74,500/day for a 2018-built suezmax"* — is
**Monte Urbasa re-reported by a second house**, not a third hull. It is N=2 with one
double-report. The bucket breaches either way; the corrected value differs by ~3.7%.

## 4. The registered §5 HALT — this is not discretionary

§5 re-check on the corrected set:

| Check | Band | Corrected | Verdict |
|---|---|--:|---|
| VLCC front | 120–155k | 154,800 | INSIDE — the Stage-A BREACH-HIGH resolves |
| VLCC term-implied | 55–90k | 55,050 | INSIDE — the Stage-A BREACH-LOW resolves |
| Suez/VLCC 12M ratio | 0.55–0.80 | 0.731 | inside |
| **Aframax/Suez 12M ratio** | **0.75–1.05** | **0.666** | **BREACH-LOW** |

At every candidate Aframax 12M the ratio stays out of band: held 51,450 → 0.666;
fixtures-only 56,000 → 0.725; assessment-inclusive 57,000 → 0.738. §5 says a landing outside
a registered band **"halts for input investigation, never output adjustment."** So the
structural check independently points at the Aframax 12M being wrong — and the pre-registration
forbids solving that by tuning the output. **This is a mandatory stop requiring your input.**

## 5. Predicted impact — NOT YET FROZEN

Deliberately not frozen, because the scope question (Q-1) changes which determinants move.
What is already established: `src/crude_tanker_fv/nav.py` holds no reference to the rate
files (verified by grep), so **ΔNAV is EXACTLY 0.0 on every name** whatever the scope — any
nonzero NAV is a halt. Movers will be the crude tanker names (VLCC/Suezmax/Aframax classes)
**plus the product names STNG/TRMD/HAFN/ASC** via the clean legs. The invariance list is
whatever carries none of the moved classes, and must be derived after Q-1 is answered.

## 6. OPEN FORKS — one word each, recommendation given

| # | Question | Rec | If silent |
|---|---|---|---|
| **S-1** | Scope: promote **only the breaching buckets**, or re-promote the whole recomputed §§1–4 set as one coherent event (how Stage A was executed)? §6 is silent — this is the load-bearing one. | **whole set** | nothing promotes |
| **S-2** | Do broker **assessments** count alongside fixtures for the band test? Decides Aframax 12M (holds at +8.84% vs breaches at +10.79%) and LR2_clean term. | **fixtures only, assessments as corroboration** | fixtures only |
| **S-3** | Is a charter **"Extension"** a qualifying print? Affects Kk Marlin (LR1 term 5yr) and Challenge Pollux (MR 12M). | **no — an extension re-prices an existing relationship** | excluded |
| **S-4** | Does FRO's **LR2 route dirty**? The repo's own convention says yes (`watchlist.yaml:222`, `fro.yaml:65` "modeled as Aframax"). Changes the Aframax front from +35.23% to +38.28%. | **yes, keep the convention** | dirty |
| **S-5** | The §5 **Aframax/Suez BREACH-LOW halt**: investigate the Aframax 12M input before promoting anything, or promote the clean breaches now and carry the Aframax investigation separately? | **investigate first — it is the registered instruction** | halt holds |
| **S-6** | Sea Topaz (2026-built scrubber NB, 80,000) — carry a **`spec-premium` tag** as Mount Horizon does? | **yes** | untagged |

Answer S-1 through S-6 and the promotion executes against this document with a frozen
predicted-impact block written before the regen. Nothing moves until then.
