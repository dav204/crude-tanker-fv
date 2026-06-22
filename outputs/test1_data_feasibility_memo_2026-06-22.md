# Test-1 data reconstruction — feasibility & build plan

**Date:** 2026-06-22. **Question:** do the offered data resources (Sharadar via factor-portfolio,
the `shipping_harvester` parsers, existing EDGAR/Yahoo infra) make the ex-post falsification test
(Test 1, the deferred "Option C / C3" from the epistemic memo) feasible — and worth building?
**Basis:** a 3-agent feasibility workflow (harvester / EDGAR-Sharadar / fleet-slow-roll) + a direct
offline Sharadar coverage check against factor-portfolio's cache. **No code changed.**

---

## Headline verdict

**Yes — it makes a *defensible MVP* of Test 1 genuinely buildable at modest effort. No — it does
not lift the statistical power ceiling.** Two findings drive everything:

1. **A sign test does not need the expensive full reconstruction.** Test 1 asks whether
   `sign(EV%)` predicts next-quarter return *relative to sector*. Fleet- and balance-sheet
   staleness perturb EV% **magnitude, not sign**, except for (a) HOLD-band names (|EV%| < ~10%) and
   (b) the newbuild-heavy "max-torque" names (CAPT/BRUT/MPCC/TEN). The signal that moves EV%'s
   *sign* is the **price-vs-NAV gap + cycle position** — both driven by **market-data marks + price**,
   the cheap, reusable, per-quarter-varying components. So you can slow-roll the expensive parts.
2. **The power ceiling is set by quarter-COUNT, which the offered data doesn't change.** Trustworthy
   harvester marks exist only **2024Q1→present** (the one era its parsers were tuned against — same
   span as the existing backtest data), and pre-2024 is blocked on both per-era parser work *and* the
   pre-2024 Pareto P/NAV archive gap. At ~6 quarter-blocks the test stays **~50–70% powered — it can
   catch a gross sign-inversion, not certify skill** (unchanged from the epistemic memo).

**So the honest reason to build it is not the (underpowered) first result** — it's that (i) the MVP
shares infrastructure with the ongoing accuracy gate (Option B), (ii) it can falsify the tool on the
one branch that matters (anti-predictive EV%), and (iii) **its power compounds forward** — every new
quarter adds a block, so the same pipeline becomes genuinely powered in ~2–3 years just by running.

> **CORRECTION (2026-06-22, owner pushback — supersedes the "power ceiling is unliftable" framing above).**
> Three things I over-stated:
> 1. **The pre-2024 limit is NOT a data-availability wall — it's broker-archive backfill effort.** The
>    harvester's crawler pages *back* through the aggregators' WordPress category archives
>    (`crawl.py`), so historical vessel-value + TC marks are obtainable as far back as the free
>    HSN/Capital Link mirrors hold issues. The "2024Q1" limit was *current parser tuning*, not
>    availability. Real gate = per-era parser development (~4–5 houses × format eras) + the **empirical
>    archive depth** of the free mirrors (unknown until a crawl — plausibly ~2015–18, possibly patchy).
> 2. **Pareto P/NAV is NOT needed for the engine falsification test.** Verified: `consensus_pnav` is
>    absent from `scenarios.py`/`nav.py`/`blend.py`/`dividend_strip.py`/`cycle.py`; EV% =
>    `weighted_FV − price` (`scenarios.py:177`) and the band keys off `ev_pct` alone (`:322`). The
>    engine computes its own NAV. Pareto is only the *optional* "beats-naive-benchmark" comparator.
> 3. **FRO quarterly stopping at 2023 is a pull-scope artifact** (factor-portfolio's universe-gated
>    pull), not a Sharadar availability gap — a direct SF1 ticker query would fill it.
>
> **Revised:** a properly-*powered* engine EV% test is **feasible**, gated on (a) per-era broker-weekly
> parser work and (b) the archive-depth unknown — NOT on a data wall and NOT on Pareto. **The decisive
> cheap next diagnostic is an archive-depth probe.**

### ARCHIVE-DEPTH PROBE RESULT (2026-06-22, live WP-REST probe — decisive)

Probed the aggregators' WordPress archives directly (oldest/newest/count per category):

| Source / house | Issues | Oldest | Newest |
|---|---|---|---|
| HSN `weekly-shipbrokers-reports` (all houses) | 3,434 | **2018-07-19** | 2026-06-22 |
| Capital Link — Allied (values/TC/demo) | 309 | 2019-08-09 | 2026-06-18 |
| Capital Link — Intermodal (values/TC/spot) | 220 | 2019-08-27 | 2026-06-12 |
| Capital Link — Weber (TC/spot) | 266 | 2019-08-09 | 2026-06-16 |
| Capital Link — Banchero (values/TC/spot) | 190 | 2019-11-12 | 2026-05-19 |

(Fearnleys slug renamed — n/a, not a value house.) **The free archives — including the vessel-*value*
houses — reach back to ~2018–2019: ~28–32 quarters at ~weekly cadence.** So the powered branch is live.
A powered engine EV% test over **~28–32 quarters × ~17 names ≈ 480–540 name-quarters** is feasible —
**powered against a *moderate* within-sector edge (IC ≈ 0.15–0.20), still blind to a *small* one
(≤0.10)** — versus the ~6-block MVP that could only catch a gross sign-inversion. **Data availability
is no longer the limit; the binding constraint is now squarely per-era broker-weekly PARSER
DEVELOPMENT** (the harvester's format-version dispatch scaffolds it, but only the 2024+ era is tuned, so
2018–2023 needs per-house per-era keyword maps + a real-issue check each) **plus the run env** (3.10+
interpreter + deps; this Mac is 3.9.6). FFA + historical_tce_means stay on the engine's synthesis path.

### FORMAT-DRIFT PROBE RESULT (2026-06-22 — sizes the parser work; refines the estimate UP)

Pulled one issue per value-house per ~2yr (2021/2023/2025) from HSN, rendered with `pdftotext -layout`,
diffed layouts (artifacts in `state/fdprobe/`). The PDFs are **text-based** (no blanket image wall) and
the value/TC/scrap tables parse — but the per-house detail makes this **more than "one parser per
house":**

| House | Value age-anchors | Period TC | Eras | Risk |
|---|---|---|---|---|
| Allied (QuantumSea) | Resale/5/**10**/15yr, all 8 classes (richest) + NB | table | 2 (stats→Market-Review, rebrand ~2022) | HSN feed **stops Feb-2024** |
| Intermodal | 5yr + NB only — **no 10yr** | table | 1 (stable) | no 10yr, no LR2 |
| Bancosta | single Baltic benchmark — **no age split** | table (incl. LR2) | 1 schema | **2025 font-cipher → OCR** |
| Xclusiv | Resale/5/**10**/15yr, rich + NB | **prose-only** | 2 (full redesign 2023→25) | TC = prose-regex |

Four findings that drive the effort up:
1. **No single house is clean + complete + deep — you must COMBINE houses** (the harvester's multi-broker
   resolution is built for this): Allied/Xclusiv for the value age-curve, Intermodal/Bancosta for TC. So
   **~4–6 (house × era) parsers**, not one.
2. **The 10-year anchor is scarce** — only Allied & Xclusiv tabulate it; Allied's free feed thins after
   Feb-2024 and Xclusiv redesigned in 2025. The 10yr leg is the thinnest historical coverage.
3. **An OCR sub-workstream is real, not hypothetical:** Bancosta 2025's `pdftotext` output is a
   per-section substitution cipher (font with no ToUnicode) → rasterize+tesseract (the FFA-widget path)
   or per-section glyph maps. Other houses may hit this in some eras.
4. **LR2 value isn't tabulated by ANY free house** (all fold it into Aframax) → historical LR2 marks stay
   on transactions / Aframax-proxy.

**Honest effort (revised): ~2–4 weeks of focused engineering** for a robust 2021–2025 multi-house
backfill (parser tuning ×~6 + an OCR path + multi-broker resolution + class-name mapping + the 3.10+
env/dwt shim + validation + pinning the 2024 era boundaries) — bounded, but **not a few days**, with
real risks (OCR eras, 10yr scarcity, Allied thinning). This refines the earlier "tens of hours" UP.

**STRUCTURED-FEED ALTERNATIVE (likely far cheaper — worth checking before committing the weeks).** The
entire broker-weekly slog is a *free-data workaround*. A paid structured historical vessel-value feed —
**Clarksons SIN or VesselsValue** — would deliver the age-anchor marks (NB/5yr/10yr by class) as a clean
time series, collapsing the ~2–4 week parser+OCR effort into a data pull (the same way Sharadar
collapsed the balance-sheet layer). If the owner has or can get that access, it is the better
market-data path for the powered engine test. **Open question for the owner.**

**Net:** the powered engine test is feasible but is a real multi-week build (or a paid-feed pull) — which
makes the cheap, already-cached **value-premium proxy test the clear first move**, and the powered engine
test a deliberate, separately-scoped investment to make *after* the proxy clears (or once a structured
vessel-value feed is in hand).

---

## The Sharadar coverage question — answered (offline, from factor-portfolio's cache)

The D2 agent flagged "does Sharadar cover these FPIs?" as the binding unknown. **Resolved offline**
against factor-portfolio's `v2-validation-first` branch, whose `data/cache/sharadar/` is a
**near-full-universe per-ticker pull down to microcaps** (the owner's recollection was right — the
`_500m_` file I checked first was cap-filtered and undercounted):

- **Covered — 17 of 20, verified** (per-ticker `prices_`/`sec_`/`secq_` files present): all 5 crude
  flagships (DHT, FRO, ECO, INSW, TNK) **plus** NAT, STNG, HAFN, TRMD, ASC, FLNG, CCEC, SBLK, GNK,
  CMDB, GSL, TEN. **HAFN and CMDB are in** (the two I'd left uncertain).
- **Absent — only the 3 Oslo-only names:** CAPT, BRUT, MPCC (no US listing → not a US SEC filer).
- **History is deep:** annual fundamentals run NAT→1997, DHT/TNK→2006, TEN→2002, CCEC/GSL→2007–08.

**Balance-sheet core is confirmed populated for the FPIs (offline) — this kills my earlier
"DHT/FRO/ECO are 6-K-heavy for the basics" worry.** `sec_DHT/FRO/ECO.csv` (annual ARY) each carry
`StockholdersEquity`, `CashAndCashEquivalents`, `LongTermDebtNoncurrent` + `DebtCurrent`,
`EntityCommonStockSharesOutstanding`, `NetIncome`, `OperatingIncome`, `GrossProfit`, D&A, dividends —
Sharadar standardizes the FPI 20-F/6-K filings whose raw `us-gaap` XBRL was too thin for the direct
pull. (SG&A / interest / tax aren't in factor-portfolio's field map but are available in SF1 with an
extended pull.)

**The one real nuance:** the cached *quarterly* (ARQ) files hold only **flow** fields
(revenue/eps/ncfo/capex) — **zero balance-sheet fields in any `secq_`**. That's a factor-portfolio
pull-choice (their factors rebalanced annually), **not** a Sharadar limitation: SF1 ARQ carries the
quarterly BS line items live, so getting point-in-time quarterly cash/debt/shares is a **one-line
field-map extension to the reusable fetcher**, not a blocker. **Two edge caveats to verify live:**
FRO's quarterly cache stops 2023 (the known FRO XBRL truncation — recent FRO quarters may need 6-K),
and NAT/TEN have *empty* quarterly cache (annual-reporting FPIs — quarterly BS may be sparse in
Sharadar too). None of these touch the four clean crude flagships DHT/ECO/INSW/TNK.

**Reusable Sharadar code (factor-portfolio):** `fetch/sharadar.py` (paginated SF1 ARQ fetch, field
maps, `SIGN_FLIP`, `datekey` no-look-ahead, emits `(period_end, filed, field, value, dimension)` —
same shape as this repo's `backtest/fetch_sec_bookvalue.py`) and `providers/sharadar_provider.py`
(`fundamental_series_at(ticker, asof, field, dimension="ARQ")` — point-in-time accessor built in).
Key sourced from `~/.config/factor-portfolio.env` (same secrets pattern as here). Direct lift.

---

## What each component costs (the real map)

| Component | Source (point-in-time) | Cost | Notes |
|---|---|---|---|
| **Prices / returns / dividends** (the dependent variable) | Yahoo via `backtest/fetch_prices.py`; **already have** `yahoo_*.csv` + `dividends_*.csv` for 17 names | **~done** | Forward total return computable now. |
| **Balance-sheet CORE** (cash, total_debt, shares, G&A, interest, tax, equity) | **Sharadar SF1 ARQ** (`datekey`≤asof) — reuse factor-portfolio; covers ~15 names incl. all crude flagships | **Low** | The big win: extends the clean BS basics from the 9 raw-XBRL names to ~15 via Sharadar. |
| **Balance-sheet SHIPPING-SPECIFIC** (working_capital composite, newbuild_capex_commitments, newbuild_advances_paid, lease split, sleeve debt, per-class opex_per_day) | **6-K/20-F parse only — never in XBRL or Sharadar for ANY name** | **High *if* done per-quarter** | **The MVP slow-rolls / holds these at nearest-prior-filing** — they move slowly and only affect EV% magnitude, not sign, for the stable majority. |
| **Market data** (vessel_value_curves, twelve_month_tc, spot_tce) | **`shipping_harvester`** → factor adapter → engine schema | **Medium** | Trustworthy 2024Q1+ only. Needs: a **Python 3.10+ env** (this Mac is 3.9.6; harvester uses `slots=True`/`X\|None`) + 4 missing deps; a **class-rename + `dwt`-injection shim** (harvester emits `Capesize`/no-dwt; engine wants `Cape`/requires dwt); **per-broker keyword tuning** vs one real issue each (~8–14h). FFA + historical_tce_means stay on the engine's existing mean-reversion synthesis. |
| **Fleet manifest** | **Slow-roll** one base per name + disclosed deltas (the manifests are already class-count representations, not vessel censuses) | **Low–Med** | Full per-quarter reserved for the ≤4 NB-heavy names + any name-quarter where MVP lands |EV%| < 10%. |
| **Engine "as-of-quarter" plumbing** | new — the engine currently hard-anchors the strip/scenario quarter (`QUARTER_KEYS`, `scenarios.py`, `dividend_strip`) to "now" | **Med–High (the sneaky one)** | To compute historical `EV%(i,q)` the engine must accept an as-of quarter and route scenarios/strip/cycle relative to it. This is the least-obvious but real build component. |
| **Naive P/NAV benchmark** (for comparison) | Pareto P/NAV — have 2024-08→now; pre-2024 is the archive gap | n/a for MVP | Only needed if extending pre-2024 for power. |

---

## The MVP, precisely

**"Vintaged-market + slow-rolled fleet/BS" historical `EV%`:**
- **Market data + price:** properly vintaged per quarter (harvester ≤ quarter-end; Yahoo close).
- **Balance-sheet core:** Sharadar SF1 `datekey`≤asof (the share-count leakage that *can* flip a
  levered name is the one BS field worth getting point-in-time — Sharadar fixes it cheaply).
- **Balance-sheet shipping-specific + fleet:** held at nearest-prior-filing / slow-rolled, ages
  rolled deterministically, `years_to_delivery` recomputed at T.
- **Scope:** run the ~12 stable pure-play/dry-bulk names (where the sign is robust to staleness);
  flag — don't trust — the ≤4 NB-heavy names and any |EV%| < 10% name-quarter for targeted full
  reconstruction. Drop the 3 pure-Oslo names (no Sharadar, no SEC) from the SEC-fed path.
- **No-look-ahead spine** (the discipline already exists, generalize it): EDGAR `acceptanceDateTime`
  for filings, the existing earliest-`filed` guard + `loaders.bvps_at` `LookaheadError`, Sharadar
  `datekey`, harvester `report_date`, Oslo publication date — every datum stamped with when it became
  public, every as-of run filtering to `stamp ≤ quarter-end`.
- **Pre-register** (per the clean git-order discipline the backtest already used): the hypothesis,
  the pooled within-sector **sign / hit-rate statistic** with **quarter-block bootstrap** CIs, and
  the decision rule — **FAILs the tool only on the anti-predictive branch** (p̂ ≤ 0.40, CI upper < 0.50);
  INCONCLUSIVE is the pre-stated expected outcome at this n.

---

## The deep-history payoff — a *properly-powered* proxy test (new, post-cache-check)

The near-full-universe Sharadar pull (17 names, fundamentals + prices back to ~2006–08, NAT to 1997)
**doesn't lift the engine-EV% power ceiling** — that's still capped by the pre-2024 *vessel-marks*
and *Pareto-P/NAV* gaps, which Sharadar doesn't touch. But it makes a genuinely powered **value-
premium proxy test** feasible for the first time: cross-sectional cheapness (P/B, or a P/NAV proxy
from depreciated-cost book) → forward sector-relative return, over **~17 names × ~70+ quarters
≈ 1,000+ name-quarters**. That is the Amendment-2 idea done right — same signal *family* the engine
relies on, on the *actual* shipping universe with deep clean data, instead of 9 names × 31 quarters.
It tests the **premise** (does cheapness predict returns in shipping?) not the **engine's marks**, so
it's a complement, not a substitute, for the MVP — but unlike everything else here it can actually
reach significance. Worth running precisely because it's cheap (data's already cached) and powered.

## Recommendation

1. **Do the cheap verification first** (minutes): extend the reusable ARQ field map to pull quarterly
   `cashneq`/`debt`/`shares` and confirm population for the 17 covered names (the annual BS fields are
   already verified present offline; this just confirms the quarterly grain). FRO-post-2023 and
   NAT/TEN quarterly are the only spots to watch.
2. **Build the MVP** — it's now a modest, mostly-reuse project (Sharadar lift + existing price data +
   slow-roll harness + the engine as-of-quarter plumbing + pre-registration), *not* the months-long
   full reconstruction. Build it for the value-of-the-pipeline (shared with the ongoing gate; catches
   gross anti-predictive inversion; compounds power forward), with eyes open that the first read will
   be INCONCLUSIVE-by-design.
3. **Target the *powered* engine test — the probe made it viable.** The critical-path work is now
   well-defined and is all effort, not unknowns: **(a)** per-era broker-weekly parser development for
   the value houses (Allied/Intermodal/Banchero + Weber TC) across the 2018–2023 format eras (the
   2024+ era is tuned; the harvester's format-version dispatch is built for exactly this) + a 3.10+
   run env; **(b)** crawl/download/quarter-select the ~2018→present issues; **(c)** the engine
   "as-of-quarter" plumbing; **(d)** pre-register the within-sector sign test. No Pareto needed. This
   is a real but bounded build (tens of hours, dominated by the per-era parser tuning + the GMS scrap
   image-table risk), and it yields a test powered against a moderate edge — the genuine validation the
   epistemic memo asked for. The cheaper **MVP** (2024Q1+, ~6 blocks) and the **value-premium proxy
   test** (deep Sharadar, powered, but tests the premise not the marks) remain as the lower-effort
   fallbacks / complements.

This supersedes the "C3 — deferred, blocked on data" line in `outputs/epistemic_soundness_memo_2026-06-22.md`:
C3 is **no longer fully blocked** — the MVP is buildable; what remains blocked is only the
*powered* (pre-2024) version.

---

## OWNER DECISION (to fill in)

- **Scope:** ☐ build the MVP (12 stable names, 2024Q1→present) ☐ MVP + targeted full-reconstruction for NB-heavy/HOLD-band ☐ hold for now
- **Sharadar field-population probe:** ☐ I'll run it with my key ☐ you run it (need go-ahead) ☐ skip
- **Pre-2024 power extension:** ☐ scope it separately later ☐ not worth it ☐ start the archive recovery now
- **Environment for harvester:** ☐ create a 3.10+ venv in this repo ☐ run it from factor-portfolio's env ☐ tbd
- **Notes:**
