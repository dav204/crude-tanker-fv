# Epistemic-soundness memo — the "independence from Pareto" finding

**Date:** 2026-06-22. **Status:** owner DECISION pending (see end). **No code/doc changed yet.**
**Basis:** the critical finding from `outputs/METHODOLOGY_AUDIT_2026-06-22.md`, then verified and
quantified by a 7-agent workflow (4 read-only verifiers + prosecution/defense/remedy panel). The
verifiers' file-level findings were re-checked by hand on the four load-bearing claims.

---

## 1. What the verification established (and where it corrected my audit)

The critical finding mostly **holds**, but verification sharpened it on four points and **corrected
one overstatement of mine**. Honest scorecard:

| Sub-claim | Verdict after verification |
|---|---|
| "~76% of marks mined from Pareto" | **CONFIRMED exactly: 97/128 in-window prints = 75.8%.** But it's **tiered** — and worst where corroboration is thinnest: dry-bulk **86.8%**, product **87.5%**, vs crude **only 53.5%**. The crude pure-plays (DHT/FRO/INSW — the flagship names) are the *best*-corroborated tier (FRO/TNK/PSHG/CMB.TECH filings + Compass + trade press). |
| "Every validation gate is Pareto-relative" | **CONFIRMED with one refinement.** Exactly **one** broker-relative, build-failing, every-run gate exists — Sanity ±50% — and it's a *bug floor*, not an accuracy bar (a −36% INSW passes by design). Two GATE-tier checks reference **nothing** broker-derived (cross-foot manifest test; locked-weights/terminal pins) — but those are internal-consistency, not accuracy. |
| "No ongoing accuracy gate" | **FULLY CONFIRMED — the hardest, most actionable point.** Calibration-lock (±5/10%) is **one-time, manual, never auto-invoked** (the only in-repo reference is a commented-out command). Drift (>2pp) is **ALERT-only against a gitignored, self-overwriting baseline** (`state/.gitignore` = `*`). After a sector launches, **no automated check stops a drifted number from shipping on accuracy grounds.** |
| "Backtest null reframed as small-sample" | **CONFIRMED, with precision.** Pre-registration genuinely preceded results (clean git order, all 2026-06-14). The one *powered* test (Amendment-2, N_q=31) returned a clean negative (IC −0.038, t=−0.42, split-half stable; the lone +0.138 collapses to −0.04 sector-neutral) — **but it tests a P/B proxy on a different universe that excludes DHT/FRO/ECO**, so it is not a refutation of *this engine*. The `REPORT.md` itself is admirably blunt ("meaningful evidence against the tool functioning as a cross-sectional stock-picker"). **The laundering happens downstream** — CLAUDE.md/PLAN.md collapse all three results into "expected for a 4-name universe," which is true of Test 0 / Amend-1 but quietly reframes the *powered* Amend-2 null through a small-sample frame that doesn't fit it. |
| "Wide spreads are features → marks non-falsifiable" | **MY OVERSTATEMENT — corrected.** The marks are non-falsifiable **by broker disagreement** (by design) and the k-band (1.05–1.25) is **decorative** (DHT 1.30 and FRO 1.27 sit above it yet keep "mark-validated"; labels are post-hoc). BUT the marks **are** falsifiable off the broker axis, and the teeth have bitten **3 times**: the ±50% sanity gate forced a real engine change on BRUT (+116% FAIL → the §9.6 PV discount); disclosed-transaction refits cut the Suezmax/NAT curve *against* broker direction (gap widened −35%→−45%) and retracted the VLCC validation ("overstated… 9% below the curve"; DHT NAV −11.5%). So "no spread could ever prove a mark wrong" is **false** — a transaction print is a spread against a mark, and it has overturned marks. |

**New facts surfaced by verification:**
- **A closed shared-source loop for six names** — DHT, FRO, INSW, SBLK, GNK, STNG draw **both** their `consensus_pnav` diagnostic **and** their calibration prints from Pareto. For these, tool-vs-Pareto agreement is one source counted twice, not two votes.
- **Extraction is clean pypdf text-scan (not OCR)** — so no character-garble risk — but the *same* scanner is documented-blind to the PDF `/Annots` layer and has demonstrably under-sampled (multiple "sentence-splitter miss" back-fills). The reliability risk is *recall* (prints missed), bounded by the solver's `[scrap×1.5, NB×0.95]` clamp, not *precision*.

---

## 2. The honest verdict for a position-taker

Reconciling the prosecution and defense (both argued only from verified facts):

**The tool is not an independent oracle, and tool-and-Pareto agreement is not two votes** — for the
six shared-source names it is one source counted twice, and 76% of the calibration substrate is that
one vendor. **But "Pareto tracking-error" overstates it** in two ways that matter: (i) the crude
flagship is only ~54% Pareto and is genuinely cross-checked against issuer filings; (ii) the marks
demonstrably move *against* Pareto when transactions say so. The accurate description is:

> **A structured, auditable, forward-looking re-expression of largely-Pareto-sourced data through a
> fixed, transaction-anchored transform (age-curve NAV + dividend strip) plus a judgmental cycle /
> governance overlay — falsifiable by disclosed transactions and gross sanity errors, but not by
> broker disagreement, and not yet shown to predict returns.**

That is a legitimate and genuinely useful **second opinion** — the decomposition and audit trail let
you interrogate *why* a name is cheap (NB convention, age curve, specific prints), which a single
P/NAV cannot. It is **not** a validated signal you can size positions off mechanically. The project's
own LIMITATIONS §6 already says this; the gap is that the *headline* framing ("independent…
transaction-validated") promises more than the body delivers.

---

## 3. Two concrete defects found en route (cheap, unambiguous)

- **B-1 — VLCC fit contamination.** The Sinokor aggregate row (`vlcc.yaml:104-109`, age 12, $71M)
  is labeled "DOCUMENTATION ONLY — excluded from fit," but it sits in the `prints:` list and
  `fit_curve_anchors` filters on the age window [3,17] only (`transactions.py:172-179`) — there is
  **no exclusion flag in code**. Age 12 is in-window, so the $71M aggregate **is** in the VLCC
  regression, pulling the age-10 anchor down, contrary to the stated owner intent. (The second doc
  row, age 0, is correctly excluded by the age filter — which is *why* this one slipped through:
  exclusion is currently an accident of the age window, not a real mechanism.) Affects every
  VLCC-heavy name. *Fix: honor an `in_fit: false` / `quality_flag: documentation` flag in the loader,
  or move documentation rows to a separate key; add a test.*
- **B-2 — downstream backtest language.** `REPORT.md` is honest; **CLAUDE.md's project-stance note
  and PLAN.md** are the ones that reframe the powered Amend-2 null as "expected for a 4-name
  universe." *Fix: restate to match the REPORT — "the real-P/NAV crude tests are inconclusive by
  design; the one powered test is a negative on a P/B proxy / different universe, so not a clean
  refutation of this engine, but not support either."*

---

## 4. Remedy options (each independently decidable)

### Option A — Honest framing restatement  *(LOW cost · HIGHEST integrity ROI · recommended now)*
Adopt the verified-grounded replacement paragraph for `README.md` + `LIMITATIONS.md` §1 (drafted in
full in the workflow output; states what "independent" does and does not mean, the 76%/shared-source
dependence, and "auditable opinion, not backtested forecast"). Retire the unqualified
**"transaction-validated" → "transaction-anchored (single-vendor-sourced)"** in headline copy. Add a
one-glance **corroboration-tier tag** to `delta_report.md` (`crude ~54% Pareto` vs `dry-bulk ~87%
single-source` vs `APPROX — no broker coverage`) so a dry-bulk or APPROX `EV%` is never read with the
same confidence as a cross-checked crude pure-play. *This is the actual fix for a "manage-don't-fix"
overclaim: make the claim accurate. No engine change.*

### Option B — Ongoing accuracy gate  *(MEDIUM cost · durable · recommended next)*
Replace the one-time lock + gitignored soft-drift with a **committed, dual-reference drift gate**
(`baselines/reconcile_baseline.yaml` tracked in git; `tests/test_drift_gate.py`;
`scripts/ratify_baseline.sh`). It tracks the tool's **own** `EV%`/`NAV`/`position_band` against its
**committed prior** (Pareto-free), plus `k_broker` on its **second difference** (spread *change*, never
level — so it never says "get closer to Pareto"; a stable INSW 1.64 stays green). A >2pp move or a
band flip with **no dated `decisions/<ticker>_log.md` annotation** fails pytest — converting the
honor-system annotation discipline (CLAUDE.md step 3) into a machine-enforced gate and giving drift a
durable, shared anchor for the first time. APPROX names tracked on self-consistency only.

### Option C — Ex-post falsification test  *(HIGH cost · underpowered · phase it)*
The genuinely feasible test (per the backtest's own conclusion) is a **pooled within-sector sign
test** on the engine's own `EV%`: does `sign(EV%)` predict next-quarter return *relative to sector*?
Honest power at ~20 names × 6 quarter-blocks is **~50–70% vs a moderate effect, blind to a small
one** — it can mainly catch a *gross sign inversion* (EV% anti-predictive), which is the only thing
that should FAIL the tool. It is **blocked on point-in-time `CompanyInputs` reconstruction** (historical
balance-sheet + mark/FFA/spot vintages the repo doesn't hold). Phased recommendation: **(c1)**
pre-register Test 1 now (cheap, mirrors the clean git-order discipline they already used); **(c2)** build
only the cheap "published-P/NAV-cheapness" fallback now, clearly labeled *"not the engine"*; **(c3)**
defer the engine-vintage reconstruction — the only genuinely-powered upgrade needs owner-supplied
pre-2024 P/NAV for DHT/FRO/ECO (→ ~22+ quarters).

---

## 5. Recommendation

Do **A + the two bug fixes now** (low cost, directly closes the integrity gap the finding names),
**B next** (the one place code genuinely raises the floor), and **phase C** (pre-register + cheap
fallback now; defer the expensive reconstruction). None of this changes the valuation engine; it
right-sizes the *claims* and adds the missing *guardrails* — which is exactly what a structural,
manage-don't-fix finding calls for.

---

## OWNER DECISION (to fill in)

- **D-1 (framing, Option A):** adopt restatement + retire "transaction-validated" + tier tags?  ☐ yes ☐ edit ☐ no
- **D-2 (gate, Option B):** build the committed dual-reference drift gate?  ☐ yes ☐ later ☐ no
- **D-3 (ex-post, Option C):** ☐ pre-register Test 1 only ☐ + cheap P/NAV fallback ☐ + fund full reconstruction ☐ none
- **D-4 (bugs):** fix B-1 (VLCC Sinokor exclusion) ☐ yes ☐ no · correct B-2 (backtest language) ☐ yes ☐ no
- **Notes:**
