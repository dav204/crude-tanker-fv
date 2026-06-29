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
