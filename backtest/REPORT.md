# Crude backtest — Test 0 report & verdict

**Date:** 2026-06-14 · **Test:** 0 (naive published P/NAV, no engine) ·
**Metric:** the one pre-registered in `PRE_REGISTRATION.md` (committed before
any number below was computed — see git history, commit a1fd637).

---

## VERDICT (against the pre-registered primary metric): **INCONCLUSIVE**

Mean quarterly cross-sectional Spearman IC of published P/NAV vs 1-quarter-
forward, equal-weight-crude-neutral total return:

> **mean IC = +0.095, t-stat = +0.35, Nq = 6 quarters, 4 names/quarter.**

Against the locked decision rule: not EDGE (needs t ≥ 2.0), not NO-EDGE (the
point estimate is positive, not ≤ 0). It lands in the pre-registered
**INCONCLUSIVE** bucket — a faintly positive, wholly insignificant signal.
**This is the outcome the pre-registration warned was most likely regardless of
whether edge exists, and the power analysis below shows it was essentially
guaranteed by the design, not informative about edge.**

Do **not** read "+0.095, 4-of-6 quarters positive" as encouraging. At this N it
is noise. Do **not** read it as "no edge" either — the test cannot see an edge
of plausible size. Both over-readings are wrong; the honest word is
*inconclusive*.

---

## The numbers

Window: real published Pareto P/NAV exists **2024-08-22 → 2026-06-11**. Universe
with real published P/NAV: **DHT, FRO, ECO, TNK** (NAT prints `na` — Pareto does
not publish its P/NAV — so NAT is excluded from the primary, per pre-reg). Six
non-overlapping forward quarters (2024Q3→Q4 … 2025Q4→2026Q1).

| Signal quarter | n | published P/NAV (DHT/ECO/FRO/TNK) | next-q total return % | EW-crude % | Spearman IC |
|---|---|---|---|---|--:|
| 2024-09-30 | 4 | 0.94 / 1.19 / 1.15 / 0.77 | −13.9 / −33.6 / −36.4 / −31.3 | −28.8 | +0.60 |
| 2024-12-31 | 4 | 0.85 / 0.81 / 0.80 / 0.57 | +14.8 / +5.7 / +6.0 / −3.2 | +5.8 | −0.80 |
| 2025-03-31 | 4 | 1.07 / 0.92 / 0.93 / 0.63 | +4.3 / −0.3 / +11.6 / +12.0 | +6.9 | +0.40 |
| 2025-06-30 | 4 | 1.05 / 0.87 / 0.99 / 0.66 | +10.5 / +34.7 / +38.9 / +21.8 | +26.5 | +0.20 |
| 2025-09-30 | 4 | 1.13 / 1.11 / 1.26 / 0.73 | +2.2 / +15.6 / −4.3 / +5.7 | +4.8 | +0.80 |
| 2025-12-31 | 4 | 1.10 / 1.17 / 1.10 / 0.77 | +53.4 / +53.9 / +64.8 / +37.7 | +52.5 | −0.63 |

Sign convention: positive IC = cheap (low P/NAV) predicted outperformance.

**Benchmarks (pre-specified).**
- **Equal-weight crude** forward quarterly returns ranged **−28.8% to +52.5%**.
  The sector's common move dwarfs intra-sector dispersion — the cross-sectional
  picking the tool aims to do operates on a thin residual after a huge beta.
- **Naive P/NAV** *is* the signal under test here, so "beat naive P/NAV" is the
  identity at Test 0; that bar binds in Test 1 (tool EV% vs this same IC).

**Exploratory (not the verdict; researcher-DOF, reported for completeness):**
- Cheap-minus-rich quarterly spread (long below-median P/NAV, short above):
  **+2.6%/quarter, t = +0.44** — positive, insignificant.
- The signal was "right" (positive IC) in 4 of 6 quarters and badly wrong in 2.
  Suggestive in the most hand-wavy sense; meaningless at N = 6.

---

## Why it is inconclusive: the design is underpowered by the *universe*, not just the window

This is the most important finding, and it is structural:

- A **4-name** cross-section makes the quarterly Spearman IC take only 11
  discrete values (−1.0, −0.8, …, +0.8, +1.0). Its quarter-to-quarter standard
  deviation here is **0.66** — enormous relative to any realistic mean IC.
- Quarters required to reach |t| = 2 at a *true* mean IC of:

  | true IC | quarters needed | ≈ years |
  |--:|--:|--:|
  | 0.05 | ~699 | ~175 |
  | 0.10 | ~175 | ~44 |
  | 0.20 | ~44 | ~11 |
  | 0.30 | ~19 | ~5 |
  | 0.50 | ~7 | ~2 |

  Realistic equity cross-sectional ICs are ~0.03–0.10. Detecting that on a
  4-name universe needs **decades to centuries** of quarterly data. **Extending
  the history (the obvious next move) does not fix this — the binding constraint
  is that there are only four crude names to rank.** A crude-subsector-only,
  rank-IC precondition test is, in effect, not answerable with statistical
  confidence at any feasible sample size.

So "inconclusive" here is not "we need a bit more data." It is "this specific
test cannot resolve the question, and a longer crude-only history won't change
that."

---

## Caveats (locked in the pre-registration, restated)

- **Survivorship.** Universe = today's crude names. Names that delisted or
  failed are absent; any value signal looks better on survivors than it was in
  real time. Bias is upward on any positive finding.
- **Tiny N / narrow universe.** 6 quarters × 4 names. Underpowered by design
  (above).
- **Single vendor each side** — Pareto (signal), Yahoo (returns). No
  cross-vendor validation.
- **No look-ahead** — asserted in the loader and tested (`test_backtest.py`):
  every signal feeding quarter *t* is dated ≤ *t*; a 45-day staleness guard
  drops a name once its feed goes quiet (this is why a stale P/NAV never gets
  carried forward).

---

## What it would take to get a real verdict — and what I need from you

The crude-only rank-IC test is a dead end for *power* reasons. Three honest
ways forward, cheapest first. **None has been run — this is the decision point.**

1. **Widen the cross-section to the full shipping P/NAV panel (cheapest, no new
   data).** The extraction fixes made this run already pulled real published
   P/NAV for **~20 shipping names** (tankers, dry bulk, LNG, LPG, containers:
   DHT, FRO, ECO, TNK, INSW, STNG, HAFN, TRMD, SBLK, GNK, FLNG, GLNG, BWLP,
   LPG, MPCC, …). A 15–20-name cross-section per quarter is **adequately
   powered** and would answer the *real* precondition — "does cheap-on-P/NAV
   predict relative returns in shipping equities at all?" — with the same
   machinery. It is broader than "crude subsector," so it is a different
   (new) pre-registration, but it is the only cheap test that *can* return a
   confident yes/no. **Recommended next step.**
2. **P/B proxy over a longer window (more quarters, lower fidelity).** Yahoo
   fundamentals give book value back ~2020; price/book is the "depreciated-book
   NAV" proxy. It buys time-depth but **not** cross-section width, so for the
   crude-only universe it stays underpowered; it helps only if combined with (1)
   or run as a pooled (name + quarter) panel regression rather than rank-IC.
   Fidelity caveat stands (book ≠ market NAV across the cycle).
3. **Test 1 (the engine) — currently blocked on data.** The valuation core is
   pure and ready, but only **2026-Q1** vintage inputs exist in-repo. Running
   `value_company` as-of past quarters needs historical balance sheets +
   period vessel-mark / FFA / spot-TC vintages, which are not in the repo and
   must be supplied or reconstructed. **What I'd need from you:** for each name
   and quarter to test, the quarter-end balance sheet (cash, debt, leases,
   shares, NB commitments) and the period's market data — or authorization to
   reconstruct from SEC/6-K filings + broker archives. Without it, Test 1 cannot
   run honestly, and I will not fabricate vintages.

**I did not fabricate any data.** Signal = real Pareto prints; returns = real
Yahoo adjusted closes. Where data does not exist (pre-2024 P/NAV, NAT P/NAV,
historical engine vintages), the report says so rather than inventing it.

---

# Amendment 1 — wide USD shipping panel (run 2026-06-14)

Owner chose to widen the universe for a powered read (pre-registered as
Amendment 1 before this was computed — commit ae991f7). Universe: 16 USD-listed
shipping names with real published Pareto P/NAV across 5 sectors (crude DHT/FRO/
ECO/TNK/INSW/CMBT; product STNG/TRMD/HAFN; dry-bulk SBLK/GNK/HSHP; LNG GLNG/FLNG;
LPG LPG/NVGS). All confirmed correct USD entities by price-match to Pareto.

## VERDICT (Amendment-1 primary, sector-neutral pooled IC): **INCONCLUSIVE**

| signal quarter | pooled n | sectors | IC sector-neutral | IC raw-panel | EW-panel % |
|---|--:|--:|--:|--:|--:|
| 2024-09-30 | 12 | 4 | +0.538 | +0.151 | −24.5 |
| 2024-12-31 | 12 | 4 | −0.510 | −0.041 | −2.8 |
| 2025-03-31 | 13 | 4 | +0.351 | +0.332 | +8.0 |
| 2025-06-30 | 13 | 4 | +0.241 | +0.493 | +25.6 |
| 2025-09-30 | 13 | 4 | +0.211 | −0.002 | +0.2 |
| 2025-12-31 | 16 | 5 | −0.591 | −0.579 | +41.1 |

> **sector-neutral pooled IC: mean = +0.040, t = +0.21, Nq = 6.**
> raw whole-panel IC: mean = +0.059, t = +0.39 (secondary, cross-sector confounded).

Per the locked rule: INCONCLUSIVE (positive, far from t ≥ 2). **The point
estimate is now even closer to zero than crude-only (+0.04 vs +0.095)** — a
wider, cleaner cross-section did not surface a signal.

Exploratory per-sector (≥3 names/quarter): crude +0.048 (t 0.18), product
+0.272 (t 1.04), dry-bulk **−0.592 (t −1.62)** — in dry bulk cheap-on-P/NAV
*negatively* predicted returns over 4 quarters, but n=4 and the period is
distorted by the GNK/Diana tender (GNK price was deal-pinned, not NAV-driven).
Noise; not actionable.

## What widening proved — the binding constraint is now TIME, not the universe

Widening did its job on the cross-section: per-quarter IC sd fell **0.66 → 0.47**
(12–16 names/quarter vs 4). But Nq is still **6** — the real published-P/NAV
history only spans 2024-08 → 2026-06. With the wider cross-section, quarters to
reach |t| = 2:

| true IC | quarters needed | ≈ years | (have) |
|--:|--:|--:|--:|
| 0.10 | ~89 | ~22 | 6 |
| 0.20 | ~22 | ~6 | 6 |
| 0.30 | ~10 | ~2.5 | 6 |

So a powered verdict is now **feasible** — it needs ~5–6 years of quarters
(≈22), not the centuries the crude-only test implied. The only thing missing is
**P/NAV history before 2024-08**, which the repo does not have.

## Combined verdict and the one decision left

Both the crude-only primary and the wide-panel primary return **INCONCLUSIVE**,
with point estimates near zero (+0.095 and +0.040). On the ~1.5 years of real
published P/NAV that exist, **there is no detectable cross-sectional edge — and
the data is too short to call "no edge" with confidence.** Sector beta (panel
quarters −24% to +41%) and single events (GNK tender) dominate the tape.

To convert "inconclusive" into a real verdict, the scarce dimension is
**quarters of P/NAV history**, and there are exactly two honest ways to get them:

1. **P/B proxy back to ~2018–2020 (buildable now).** Yahoo fundamentals give
   quarterly book value; price/book is the sanctioned "depreciated-book NAV"
   proxy. It extends the panel to ~22–30 quarters — enough to detect an IC of
   ~0.15–0.20 if one exists — at the cost of fidelity (book ≠ market NAV across
   the cycle; flagged). This is the cheapest path to a *powered* read.
2. **Pre-2024 published P/NAV, if you can supply it.** An archived Pareto (or
   Clarksons / VesselsValue) P/NAV series back to ~2018 would give the powered
   test on the *real* signal rather than a proxy. The repo has nothing before
   2024-08; I will not fabricate it. If you have a subscription archive or an
   export, that is the highest-fidelity route.

Test 1 (engine EV% vs naive P/NAV) remains both unjustified (no non-zero Test-0
signal to beat) and data-blocked (only 2026-Q1 vintage inputs in-repo).

---

# Amendment 2 — P/B proxy from SEC book value, 2018–2026 (run 2026-06-14)

Built to buy the scarce TIME dimension. Yahoo fundamentals were too shallow
(quarterly to 2025 only) so they were rejected; **SEC EDGAR XBRL** book value
was used instead (official, deep), with each fact's **filed date** as the
no-look-ahead lag, and the **as-first-reported** value (earliest filing, not
restatements). Universe = the 9 names with deep us-gaap XBRL: crude TNK/INSW;
dry-bulk SBLK/GNK/HSHP; LNG GLNG/FLNG; LPG LPG/NVGS. **No product sector, only
2 crude (no DHT/FRO/ECO) — see fidelity caveats.** 31 non-overlapping quarters,
6–9 names each.

## VERDICT (Amendment-2 primary, sector-neutral P/B IC): **NO DETECTABLE EDGE (powered null)**

> sector-neutral pooled IC: **mean = −0.038, t = −0.42, Nq = 31.**
> Split-half stable: early −0.056, late −0.021. Essentially zero throughout.

This is the first **adequately powered** test in the whole exercise (31 quarters
× ~7 names). A within-sector value edge of plausible size (IC ≥ ~0.15) would
likely have surfaced; it did not. Per the locked rule this is NO-EDGE
territory — the point estimate is ~0/slightly negative with a powered sample.

**The one positive number, and why it is not edge.** The raw whole-panel IC is
**+0.138 (t = 1.98)** — borderline-significant and tempting. But it is the exact
cross-sector confound the pre-registration named: it rewards being cheap-on-P/B
*and in a sector that outperformed*. **Neutralize sectors and it collapses to
−0.04.** So the apparent signal is **sector allocation, not security
selection** — and security selection (peer-relative picking) is what the tool
claims to do. Reported, not credited.

**Fidelity caveats (locked before the run; they bound how far this verdict
reaches):** book ≠ market NAV (TNK trades ~3× book but ~0.8× NAV — P/B ranks
need not equal P/NAV ranks), so this is evidence about a *value premium in
shipping*, not a direct test of the P/NAV marks; the universe is bulk/gas-heavy
with no product and only 2 crude (excludes the canonical DHT/FRO/ECO); a
filed-date reporting lag makes the proxy signal intrinsically staler than daily
P/NAV; survivorship persists (and biases *toward* finding a value premium — we
found none, which makes the null, if anything, conservative).

---

# Amendment 3 — Sharadar deep-history P/B proxy on the actual watchlist (run 2026-06-22)

Amendment 2's powered null ran on a 9-name SEC-XBRL panel that **excluded the
crude flagships DHT/FRO/ECO and all of product** — not the tool's universe.
Sharadar standardizes the FPI 20-F/6-K filings, so the powered P/B proxy now
runs on **17 of the 20 watchlist names — all five crude flagships + full product
+ dry-bulk + LNG — over deep history** (NAT→1997, DHT/CCEC→2006). Cache
provenance: factor-portfolio `v2-validation-first@7723092`. Method, universe,
staleness, decision rule, and bootstrap seed all locked in PRE_REGISTRATION.md
Amendment 3 **before** any IC was computed (committed `db9c4f6`, prior to the
runner). Window 2008-03-31 → 2025-12-31, **72 usable quarters** (≥4 pooled
names; sector cells grow 1→4; GSL is a containerships singleton → raw-panel
only). Negative-book quarters (e.g. FRO 2013–14 pre-recapitalization) are
filtered by the `bv≤0` guard.

## VERDICT (Amendment-3 primary, sector-neutral P/B IC): **INCONCLUSIVE — a *powered* near-null**

> sector-neutral pooled IC: **mean = +0.036, t = +0.62, Nq = 72.**
> quarter-block bootstrap 95% CI (block 4, B 10000, seed 20260622):
> **[−0.079, +0.151]** — straddles zero.
> Split-half: **early +0.090 (t 1.01), late −0.018 (t −0.24)** — the faint
> positive is front-loaded and gone in the recent decade.

This is the most powered test in the exercise (72 quarters × up to 16
sector-pooled names). At this N a within-sector edge of plausible size
(IC ≈ 0.15) would clear t ≥ 2; the point estimate is ~0 and the CI excludes a
*moderate* edge while remaining blind to a *small* one (≤0.10). Per the locked
rule it is INCONCLUSIVE (positive point estimate, t < 2) — but, unlike Tests 0/1
and Amendment 1, an **adequately powered** INCONCLUSIVE: it bounds the effect
rather than merely failing to find one.

**The raw whole-panel read is also weak.** Secondary cross-sector-confounded IC
**+0.059 (t = 1.36)** — not significant, and weaker than Amendment 2's tempting
+0.138; the sector-tilt that flattered the bulk/gas panel does not reappear on
the broader universe.

**Fidelity caveats (locked before the run).** Book ≠ market NAV (the
load-bearing one — a name can trade ~2× book yet ~0.8× NAV, so P/B ranks need
not equal P/NAV ranks); the book leg updates annually (within-year P/B moves via
price); single vendor both legs; survivorship (today's 17 names, amplified by
deep history, biasing *toward* finding a premium — none found, so the null is
conservative). **This tests the value-premium *premise*, not the engine's NAV
marks** — it is a complement to, not a substitute for, the deferred powered
engine EV% test.

---

# Test 1 — engine EV% ex-post (POWERED backfill, run 2026-06-23)

The first test of the tool's **own** signal (not a cheapness proxy): the engine's
probability-weighted **EV%**, computed strictly as-of each quarter
(`PRE_REGISTRATION_TEST1.md`, `DATA_CONTRACT_TEST1.md`). The 2026-06-22 build was
faithful but underpowered (Nq 5, INCONCLUSIVE). This run is the data backfill that
adds power.

## VERDICT (Test-1 primary, sector-neutral pooled IC of EV%-cheapness): **INCONCLUSIVE**

Universe: **tanker + dry only** (3 sectors: crude, product, dry_bulk; 11–14 names/q).
LNG/container names (FLNG, CCEC, GSL) are **excluded** — no free house tabulates
their vessel values, so they can't be vintaged (see "2019–2020 quality" below).

| Window | Quarters | mean IC | t | bootstrap 95% CI | sign hit-rate | verdict |
|---|--:|--:|--:|---|--:|---|
| **2019Q3–2026Q1 (full)** | **23** | **−0.020** | **−0.30** | **[−0.135, +0.100]** | 46% | INCONCLUSIVE |
| 2021Q3–2026Q1 (clean) | 19 | +0.015 | +0.22 | — | 46% | INCONCLUSIVE |

Up from Nq 5 (+0.005). Both windows are **~zero** — marginally positive in the
2021+ clean window, marginally negative including the lower-quality 2019–2020
quarters. **Neither is anti-predictive** — the verdict never approaches the
pre-registered FAIL threshold (IC<0 AND t≤−2.0), and the sign hit-rate stays above
the 40% trip. So the powered test **does not impeach the engine**, and it does not
clear EDGE (IC>0 AND t≥2.0) either. INCONCLUSIVE remains the honest read, now at
**~4.5× the original quarter count** with a tightened CI [−0.135, +0.100] (excludes a
*large* effect, |IC|>0.13; still blind to a small/moderate one), and power compounds
forward. *(The number is remarkably stable across every build-out step: 2021Q3–2025Q4
alone +0.040; +2024/2026 gaps → +0.019; +Intermodal TC → +0.011; +2019–2020 TC and the
LNG/container exclusion → +0.015 clean / −0.020 full. The verdict survives each
refinement — it is not an artifact of any single data choice.)*

## What changed — the data backfill

The binding constraint was broker-weekly vessel-mark coverage. Established this run:
- **The free HSN archive effectively starts 2021**, not 2018 (2019–2020 are a void;
  the feasibility memo's "reaches 2018" was a category total-count misread). Capital
  Link's live API is bot-gated.
- **Xclusiv parsers rebuilt on poppler text** (pdfplumber scrambled these issues'
  glyph order) for BOTH eras: the 2021–2023 *flat-row* secondhand (~42 marks/q, all 10
  classes incl. the crude flagships) and the 2024+ *transposed/grouped* secondhand (a
  block-walk on the 4-age-row structure with a floating class label; ~40 marks/q, 8
  clean classes — replaces the fragile geometry pass, which silently missed
  2024Q1/Q2/Q4 + 2026). Result: contiguous vessel_value 2021Q3→2026Q1.
- **2019–2020 recovered from the Wayback Machine** (Allied *Weekly Market Report*,
  not the no-value SnP supplement) → 4 quarters (2019Q3/Q4, 2020Q2/Q3), Allied
  Weekly parser built. Single-vendor by era: Xclusiv 2021–2025, Allied 2019–2020
  (matches the locked single-vendor caveat).
- **Intermodal TC enrichment** — the designated period-TC source (DATA_CONTRACT) now
  feeds the forward: a poppler-text parser on Intermodal's stable 'TC Rates' table
  (1yr TC by class, k/K case = tanker/dry; TC-only, no vessel_value, so the value
  spine stays single-vendor). This (a) **fills 2025Q3–2026Q1 TC**, which Xclusiv
  stopped printing (the forward there was pinned to the through-cycle mean), and (b)
  adds **cross-broker TC reconciliation** vs Xclusiv prose for 2021–2025Q2 (89 groups,
  mean spread 16%, 43 disagreements — recorded as the discrimination diagnostic).
  **Robustness:** shifting the entire TC source to Intermodal + filling the gap moved
  the IC only −0.014 → −0.021 — confirming the pre-registered claim that TC perturbs
  EV% *magnitude, not sign*. The verdict is not an artifact of the TC fallback.
- **2019–2020 quality + no-look-ahead enforcement.** Two fixes: (i) the Allied Weekly
  'period market TC rates' table (the `12 months` row) now feeds 2019–2020 TC, so those
  quarters are TC-anchored not pinned to the through-cycle mean; (ii) names whose vessel
  values *no free house tabulates* — LNG/container (**FLNG, CCEC, GSL**) — are now
  **excluded** from every vintage (`build_vintage.UNCOVERED_SECTORS`). Previously their
  NAV fell back to LIVE 2026 curves (a multi-year look-ahead, worst in 2019–2020),
  violating the no-look-ahead spine; they can't be vintaged from the free archive, so
  Test 1 is scoped to the tanker+dry universe it *can* vintage. Also fixed a precedence
  bug exposed here: HSN Allied is spotty/stale and was overriding the Xclusiv value
  spine for 2022Q4+ via `allied`-first precedence — now **xclusiv-first for value,
  intermodal-first for TC**, with Allied the fallback (so it only wins the 2019–2020
  quarters where Xclusiv/Intermodal are absent).

## Caveats specific to this run

- **Single-vendor marks** (locked): one value series per quarter — Xclusiv (2021+) or
  Allied (2019–2020). No cross-vendor *value* validation (TC is cross-checked).
- **Scope = tanker + dry.** LNG/container (FLNG/CCEC/GSL) are excluded (no vintaged
  vessel marks); the sector-neutral IC pools crude + product + dry_bulk (3 cells).
- **Coverage contiguous** 2021Q3→2026Q1, and 2019Q3/Q4 + 2020Q2/Q3 carry real vintaged
  VV **and** TC. Remaining thin legs: LR2 is folded into Aframax by every free house (no
  separate LR2 mark → product names lean on the Aframax proxy); 2019–2020 are patchy
  within-quarter (one Allied Weekly per quarter, sometimes mid-quarter dated).

## Relation to the proxy tests

Amendment 3 (powered P/B *proxy*, Nq 72) excluded a *moderate* within-sector value
premium on a book proxy. Test 1 now tests the **engine's market-NAV EV% directly**
and lands in the same place — no detectable cross-sectional edge, but not
anti-predictive — on the actual tool signal rather than a proxy. Consistent stories;
both INCONCLUSIVE/near-null, neither a refutation of the marks.

---

# FINAL combined verdict

| Test | Signal | Universe | Powered? | Sector-neutral IC | t |
|---|---|---|---|--:|--:|
| 0 | published P/NAV | 4 crude | no (Nq 6, n 4) | +0.095 | 0.35 |
| Amend-1 | published P/NAV | 16 shipping | partial (Nq 6) | +0.040 | 0.21 |
| Amend-2 | P/B proxy (SEC XBRL) | 9 shipping (no DHT/FRO/ECO, no product) | yes (Nq 31) | −0.038 | −0.42 |
| Amend-3 | **P/B proxy (Sharadar)** | **17 watchlist (all crude + product)** | **yes (Nq 72)** | **+0.036** | **+0.62** |

**Across every peer-relative (sector-neutral) test, cheap-on-NAV(-proxy) shows
no detectable power to rank shipping winners.** The two real-P/NAV tests are
underpowered; the two powered proxy tests — Amendment 2 (book proxy, narrow
universe) and Amendment 3 (book proxy, the *actual* universe + deep history) —
both land on ~0 with the right sign-and-significance to **exclude a moderate
within-sector value premium**, and the only positive readings anywhere are
cross-sector sector-tilts that wash out under neutralization or fail to replicate.

**What this does and does not establish.**
- It is **meaningful evidence against** the tool functioning as a cross-
  sectional stock-picker on a NAV-*proxy*: the precondition (cheapness predicts
  peer-relative return) is now a *powered* near-null on the **actual watchlist
  universe** (Amendment 3, Nq 72, all crude + product), not just the narrow
  bulk/gas panel — and remains unproven in the underpowered real-P/NAV tests.
- It is **still not a clean refutation of the engine specifically:** every
  powered test uses a **book proxy** (depreciated cost), not the tool's
  market-NAV marks — and book diverges from NAV precisely across the cycle. The
  real-P/NAV crude test could not be powered with available data, and **Test 1
  (the tool's own EV%) has not been run** — its powered version needs the
  pre-2024 broker-weekly vessel-mark backfill (scoped in
  `outputs/test1_data_feasibility_memo_2026-06-22.md`), the one branch that
  could actually validate/refute the marks.

**Status (not a freeze gate).** The 2026-06-14 development freeze was **lifted
2026-06-21 by owner decision**; this backtest is a recorded ex-post diagnostic,
not a development gate (CLAUDE.md project stance). Amendment 3's powered
near-null is the empirical basis for the README/LIMITATIONS §1 line **"no
demonstrated ex-post cross-sectional edge"** — it bounds the value-premium
*premise* on the right universe. The two reads that would move the *engine*
verdict remain open:
1. **Powered engine EV% test (Test 1)** — needs the pre-2024 broker-weekly
   parser backfill (or a structured Clarksons/VesselsValue feed) + the engine
   as-of-quarter plumbing. The decisive, highest-fidelity next step.
2. **Real pre-2024 P/NAV** for the crude pure-plays → a powered test on the
   actual published signal and names; needs an owner-supplied archive.

No data was fabricated anywhere in this exercise.

## Reproduce

```
PYTHONPATH=. .venv/bin/python -m backtest.fetch_prices         # Yahoo price/div cache
PYTHONPATH=. .venv/bin/python -m backtest.fetch_sec_bookvalue  # SEC book-value cache
PYTHONPATH=. .venv/bin/python -m pytest backtest/test_backtest.py -q
PYTHONPATH=. .venv/bin/python -m backtest.run_test0            # Test 0  (crude P/NAV)
PYTHONPATH=. .venv/bin/python -m backtest.run_wide             # Amend-1 (wide P/NAV)
PYTHONPATH=. .venv/bin/python -m backtest.run_proxy            # Amend-2 (P/B proxy, SEC XBRL)
PYTHONPATH=. .venv/bin/python -m backtest.run_proxy_powered    # Amend-3 (P/B proxy, Sharadar; needs FACTOR_PORTFOLIO_ROOT)
```
