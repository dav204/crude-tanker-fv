# Thread 1B — crude resale LEVEL confirmation — pre-registration

**Frozen ahead of sourcing** (commit precedes any dated mark). A small, isolated
step — NOT a re-opening of Thread 1. Thread 1 is landed, attributed, and correct
for the basis *slope*; this confirms the *level* of one load-bearing input and
either clears the provisional flag or triggers a deliberate, attributed correction.
**This step gates Thread 4** — no crude name is treated as "settled" on the scorecard
until it clears.

## 0. The open question (why this exists)

Guard #2 validated the crude depreciation **slope** (VLCC age-0 $145M → production
5yr $113M = 22%, the 5yr from independent S&P prints). It did **not** validate the
**level** of $145M — it structurally cannot, because the 5yr anchor is independent
of the resale mark by construction, so guard #2 only tests the *shape* between them.
A1.5 separately flagged that the crude resale series may carry inflation (the original
$175M was stale-high *as resale*, above the then-current ~$145M). So $145M sits
**slope-validated, level-unconfirmed**, and it is the canonical NAV age-0 anchor.

## 1. Why the level is load-bearing (measured sensitivity)

Per-name NAV sensitivity to the VLCC resale level (`compute_nav`, production curve):

| Name | dNAV per −$1M VLCC | NAV move for the −$7M ($145→$138) example |
|---|--:|--:|
| **BRUT** | **−3.89%/$1M** | **−27.2%** (4.34 → 3.16) |
| CAPT | −0.70%/$1M | −4.9% |
| FRO | −0.23%/$1M | −1.6% |
| DHT | −0.16%/$1M | −1.1% |
| ECO | −0.03%/$1M | −0.2% |

So the level question is overwhelmingly a **BRUT** question (100% age-0 VLCC newbuilds,
max-torque). It also underpins the FRO 1.52× broker divergence and the "broker is
stale-high" interpretation, both of which assume $145M is current.

## 2. Inputs to confirm (the wired age-0 levels)

VLCC $145M, Suezmax $95M, Aframax $88.9M, LR2 $88.9M, MR $54M — against a **dated,
current broker prompt-resale source** (xclusiv / Clarksons / dated shipping-news quote),
each with a date. No proxy, no fabrication (same discipline as Threads 3/5).

## 3. Halt thresholds (predicted AHEAD; honor the halt if it fires)

- **Book-wide, per crude class:** if a dated mark differs from the wired value by **>2%**
  (VLCC ±$2.9M, Suezmax ±$1.9M, Aframax/LR2 ±$1.8M, MR ±$1.1M), **HALT** — re-pre-register
  the corrected level, recompute, re-ratify as a deliberate Thread-1-style correction.
  Within ±2% → the class is confirmed.
- **BRUT carve-out (because −3.89%/$1M):** a within-±2% VLCC revision still moves BRUT >2%
  (the drift bar) once it exceeds ~±$0.5M. So **BRUT's** level-provisional flag clears ONLY
  if the dated VLCC mark confirms within **±0.5% (±$0.7M)** of $145M. Any larger *confirmed*
  revision — even one inside the book-wide ±2% — triggers a BRUT-specific recompute +
  decision-log note, not a silent pass.
- The threshold gates the **input**, not the output: a miss sends us to source the corrected
  level, never to widen the band.

## 4. What clears the flag vs what corrects

- **All crude classes confirm within threshold** → the `LEVEL-PROVISIONAL` flag clears on
  BRUT/CAPT/FRO and in the baseline cause; BRUT's −53.8% hardens from slope-validated to
  fully-validated; the FRO "broker stale-high" reading is confirmed (broker high because
  $145M is current).
- **Any class outside threshold** → a *new* pre-registered correction: register the dated
  level + predicted per-name move, recompute, re-ratify with attribution. Caught as a
  deliberate correction, never a surprise.

## 5. Data posture

Needs a dated current broker resale source. If sourced → run §3/§4. If not available here →
registered-pending (write the data contract, request the marks), exactly like Threads 3/5.
Until it clears, every crude name carries the level-provisional flag into Thread 4.

---

# Amendment A (2026-06-29) — basis decision + the guard-#2 lag (post-sourcing)

A best-effort web sweep returned dated (May 12 2026, Signal Ocean, via Cyprus Shipping
News / Splash247 / Seatrade) VLCC values. **Three simultaneously-true prices, not one
number:** newbuild contract ~$129M; orderly **5yr secondhand ~$138M** ($9M over newbuild);
**prompt / immediately-available ~$156–174.5M** (21–35% premium, "$45.5M excess"). The
initial read ("prompt $156–174.5M > wired $145M ⇒ $145M too low") was **wrong** — it treated
a scarcity print as a NAV basis.

## A.1 Basis decision (owner, resolving the §0 fork)

**Age-0 NAV anchor = orderly delivered-secondhand value, age-curve-anchored — EXCLUDING the
immediate-availability scarcity premium (a fleet cannot realize it; you can't liquidate 20
ships into a spot-scarcity bid without becoming the marginal seller and collapsing the
premium) and EXCLUDING newbuild-contract replacement cost (that lives in parity, Amendment 1).**
The three prices map cleanly: **newbuild → parity; orderly secondhand → NAV; prompt-scarcity →
neither.** On current dated data the orderly delivered level is **~$138M** for the VLCC 5yr with
age-0 modestly above — i.e. the honest age-0 is **at or slightly below the wired $145M, not
above it.** **Direction: crude marks DOWN, not up; BRUT down further.** The original stale-high
instinct (A1.5) is **confirmed**, not reversed. The $156–174.5M prompt number is a red herring
for NAV.

Anti-trap note: BRUT's −3.89%/$1M torque means it is the wrong place to *read* the level off —
the size of the consequence on one max-torque name must not pull the input toward the softer
answer. Set the level by orderly-delivered economics; BRUT goes wherever that sends it.

## A.2 Do NOT wire off secondary ranges — require the authoritative mark

The above are secondary outlets quoting *ranges/relatives* in a Hormuz-distorted market, and
even the ~$138M 5yr is itself somewhat spike-elevated (5yr trading above newbuild is the
distortion in the secondhand market). So: **register the basis decision now; require a dated
xclusiv/Clarksons VLCC (and crude) resale mark — with its definition confirmed (orderly vs
prompt-inclusive) — BEFORE re-wiring.** If the authoritative orderly mark is ~$138M → wire it,
BRUT moves down, flag clears as a deliberate pre-registered downward correction. If it quotes
prompt → strip the immediacy premium first. The number wired must be a clean orderly-disposal
mark, never a scarcity print or a secondary-source range.

## A.3 Guard-#2 LAG — registered as its own item (independent of the level)

Guard #2 passed using the **transaction-anchored** VLCC 5yr of **$113M** (145→113 = 22% slope,
healthy). But the **live firm 5yr is ~$138M** — so the transaction prints **lag** the spiked
market, and the *current-market* 0→5 slope is 145→138 ≈ **5% (thin)** — the original Problem-1
concern, real after all and masked by recency-lagging prints. Sized (lift VLCC 5yr 113→138):

| | DHT | ECO | FRO | (newbuild-heavy BRUT/CAPT: unaffected — sit at age-0) |
|---|--:|--:|--:|---|
| NAV impact | +3.4% | +11.2% | +8.9% | |

So the production crude curve **under-marks mid-age crude** by up to ~11% **if** the live 5yr is
the orderly level. This is a **curve-SHAPE** finding, independent of the age-0 level, touching
all crude mid-age tonnage, and it points the **opposite** way from the age-0 correction (the two
partially offset; net per name depends on age mix — newbuild-heavy net down, mid-age-heavy net up).

**Methodology tension to resolve (owner):** the §9.9 transaction-anchoring philosophy says actual
S&P prints ARE the headline marks (CLAUDE.md) — but those prints lag a spiking firm market. Does
NAV override the lagging transaction-anchored 5yr toward the firm broker quote, or hold the
transaction marks as the truer *orderly* level (the firm spike being non-recurring)? This needs
the same authoritative crude resale **curve** (age-0 AND mid-age) to resolve. Registered-pending;
does NOT resolve by wiring a secondary number. Tracked as Thread 1C.
