# News digest — 2026-09-12

## Run header

- **Window swept:** **2026-09-07 → 2026-09-12** (6 calendar days; 5 business days — 9/07,
  9/08, 9/09, 9/10, 9/11). Previous digest established by globbing `outputs/news_digest_*.md`:
  the newest is `news_digest_2026-09-07.md`, so the window opens the day that digest was
  written. No default lookback needed.
- **Names swept:** 25/25 of `inputs/watchlist.yaml` — 2343, ASC, BRUT, BWLP, CAPT, CCEC,
  CMBT, CMDB, DHT, ECO, FLNG, FRO, GNK, GSL, HAFN, INSW, LPG, MPCC, NAT, SB, SBLK, STNG,
  TEN, TNK, TRMD. Plus **OMC** — not a watchlist name, swept only because it is polled by
  `newsweb_poll` and is the other half of the pending BRUT carry ruling (see NOTE below).
- **Depth weighting.**
  - **DEEP — APPROX-P/NAV set** (read from `reconcile.APPROX_PNAV_TICKERS`, not hardcoded):
    NAT, ASC, CCEC, TEN, CMDB, MPCC, GSL, SB, 2343.
  - **DEEP — non-US-listed** (identified from the `yahoo_symbol` suffix): BRUT, CAPT, MPCC,
    BWLP (.OL), 2343 (.HK).
  - **DEEP — live-event names** (from decision-log heads): SB (placement settling in-window),
    SBLK (final-price 6-K explicitly flagged "Watch" by its own log), BWLP (open newbuild-
    programme fork + stale TP), CMBT (SGM gating the $0.64 distribution), BRUT (post-demerger
    carry ruling pending), CAPT (post-report-day prereg).
  - **LIGHTER — broker-covered US remainder:** DHT, ECO, FRO, INSW, TNK, FLNG, STNG, HAFN,
    TRMD, GNK, LPG.
- **Sources searched.**
  - **Local issuer channel FIRST** (per the standing instruction): `state/edgar_manifest.jsonl`
    plus the staged bodies under `inputs/filings/<ticker>/` — **15 in-window arrivals read as
    primary text** (9 SEC 6-K/exhibits, 6 NewsWeb/MFN releases).
  - **All five MFN issuer feeds fetched directly** — `bruton-limited`, `capital-tankers`,
    `mpc-container-ships`, `bw-lpg`, `omc-tankers` (slugs read from the `mfn_slug:` keys in
    `inputs/data_sources.yaml`, never guessed). All five returned. This is what makes the
    Oslo negatives below PRIMARY-SOURCED rather than inferred.
  - **HKEXnews** for 2343 — see COVERAGE LIMITS; the load-bearing evidence for 2343 is the
    local `state/hkex_poll.json`, not the web search.
  - `inputs/research_pareto/` — the four new in-window Shipping Dailies (9/08, 9/09, 9/10 read
    front-to-back with `pdftotext -layout`; 9/07 was already read by the previous digest) plus
    the 9/11 Container Weekly. **Three of the seven MATERIAL items below came from here.**
  - WebSearch/WebFetch for the names and events the local channels structurally cannot see —
    17 queries/fetches. One of them (CCEC) produced a MATERIAL item no local channel saw.

### COVERAGE LIMITS — read before trusting any "nothing found" below

- **Both local channels were demonstrably alive for the whole window, including today.**
  `state/edgar_poll.json` shows all **22 CIKs** last polled **2026-09-12T17:20:05Z**;
  `state/newsweb_poll.json` shows all **5 MFN feeds** polled **2026-09-12T17:20:23Z**;
  `state/hkex_poll.json` shows 2343 polled **2026-09-12T17:20:20Z**. The most recent run log
  reads `polled 22 names: 0 new … polled 1 names: 0 new … polled 5 names: 0 new`. I checked
  `state/edgar_poll.err` for in-window failures and found **none** — the 31 `LANE FAILED`
  entries in that file are all older than the window (the newest is `2026-09-03T08:40:45Z`,
  a newsweb `rc=1`, which pre-dates 9/07). So "no filing for name X" below is a
  **channel-backed negative**, not silence of unknown cause.
- **The TEN channel gap flagged in the 9/07 digest (its owner-summary item 3) is CLOSED.**
  TEN's CIK **0001166663** now appears in `state/edgar_poll.json` and was polled today. The
  residual caveat is real but different in kind: TEN files its half-year 6-K **weeks late**
  (its own 9/10 release check records "Not on EDGAR (the H1-2025 6-K lagged three weeks)"),
  so the lane exists but **cannot produce a timely TEN negative**. TEN's in-window event was
  caught by web search, not by the lane.
- **EDGAR was NOT enumerated directly.** I did not call `browse-edgar` or `efts` — both return
  HTTP 403 to WebFetch (re-confirmed as still true by prior runs; I did not re-test, because
  the sentinel had already staged the in-window US filings locally, which is better evidence
  than an enumeration). **No claim below rests on my having walked EDGAR, because I did not.**
- **HKEXnews `titlesearch.xhtml` returned "Total records found: 0"** for 2343 over 9/01–9/12.
  I do **not** treat that as the evidence — a 0-record return from a JS-backed search page is
  indistinguishable from a bad query. The 2343 negative below rests on the **local poller**:
  it ran today, and 2343's newest staged filing is the **8/31 Monthly Return** (`hkex-12308484`),
  which is *before* the window opens.
- **The BRUT MFN fetch summary omitted the 9/07 "Financial calendar" release** that the local
  channel has staged (`newsweb_2026-09-07_349fe45a…txt`). The local primary text is
  authoritative and the release is real; what this shows is that the MFN summariser can drop a
  short item. Read the MFN negatives below as "nothing *large* after the stated date", and note
  that in each case the local poller independently agrees.
- **The BWLP research note behind M1 is NOT in the local archive.** The 9/10 daily says "See
  link to report sent out this morning here", but no BW LPG company report PDF landed in
  `inputs/research_pareto/2026/09/`. **Everything in M1 is quoted from the daily's summary of
  that report, not from the report.** The TP and rating are verbatim from the daily; the
  reasoning behind them is not on file.
- **The 'Barcelona Spirit' fixture (M4) could not be corroborated outside Pareto.** A targeted
  search for the hull name, the rate and the charterer returned nothing. Pareto's own wording
  is hedged ("Talk of…", "appears to have fixed"). Treat as **LEAD-QUALITY / single-source
  broker market talk**, not an issuer-confirmed fixture.
- `globenewswire.com` fetched successfully this run (one call, the CCEC release — no timeout).
  `splash247` and `hellenicshippingnews` were not fetched; nothing below depends on them.

### Archive check (STEP 4)

**ONE UNACCEPTED GAP IN-WINDOW, and it fires a re-look condition the owner wrote himself.**

- Present: Shipping Dailies for **9/07, 9/08, 9/09, 9/10**. Present: a **Container Weekly dated
  9/11**.
- **MISSING: the 2026-09-11 (Friday) Shipping Daily.** One business day — below the
  `limit_business_days: 3` threshold, so the sentinel will not flag it, and there is **no entry
  for it in `inputs/archive_gaps.yaml`**. News read from 9/11 is therefore **UNSUPPORTED, not
  absent.**
- **This is the THIRD Friday to drop: 8/14, 8/21, 9/11.** The accepted 8/21 entry states its own
  trip-wire verbatim: *"NOTE THE PATTERN: second consecutive FRIDAY absence (8/14, also accepted
  sub-threshold) … re-look only if a third Friday drops."* **A third Friday has now dropped.**
  The condition is met; the re-look is owed. (9/04 was present, so the run is not consecutive —
  but the entry's condition is "a third Friday", not "three in a row".)
- **Aggravating, and the reason I am not calling this source-quiet myself: the Pareto lane was
  ALIVE on 9/11.** A Container Weekly landed that same day. On 8/14 and 8/21 nothing at all
  arrived, which is consistent with sender-side non-publication; on 9/11 the sender published
  *something* and the daily specifically is what is missing. That is a **different failure
  shape** and it deserves its own channel-side walk rather than inheriting the 8/21 reasoning.
  I am not accepting it — accepting a gap is the owner's call and needs channel-side evidence.
- **Bookkeeping defect, out of window but surfaced by the above:** the 8/21 entry's prose calls
  **8/14** "also accepted sub-threshold", but there is **no 8/14 entry in `accepted[]`**. The
  file's own rule is that a gap "either gets BACKFILLED or gets accepted here, dated and
  reasoned — never left to age out silently". 8/14 is currently accepted only in a neighbour's
  prose, which `_accepted_gap` cannot read.
- Corroborating, not a separate finding: `outputs/sp_print_candidates.md` has an mtime of
  **9/10 10:00** and reads "Scanned 1 reports (2026-09-10 → 2026-09-10)", even though the
  mechanical chain ran today at 11:01. That is consistent with **no new daily having arrived
  since 9/10** — the same hole, seen from the mechanical side.

---

## MATERIAL

### M1 · BWLP — **Pareto UPGRADES BW LPG to BUY, TP NOK 262 / $28.5**, and the watchlist has been waiting for exactly this note

**Date:** 2026-09-10.
**Source:** `inputs/research_pareto/2026/09/2026-09-10_Periodical-ShippingDaily-2026-09-10-529696.pdf`,
"Research focus: BWLPG – Running yield rivalling the VLCC names", verbatim: *"At ~1.2x a
conservative NAV and (at least) a 20% running yield for H2, we upgrade BW LPG to BUY (HOLD),
with TP NOK 262 / $28.5; 1.2x our forward NAV and ~8x EV/EBITDA on (modest) 2027 estimates."*
The daily also discloses that Pareto acted as Co-Bookrunner in the $300m BW LPG CB issue.

**Model surface touched.** `inputs/watchlist.yaml` → `BWLP.analyst_target: 17.52`. That figure's
own comment reads: *"Pareto TP NOK 172 (BUY, 2025-09-02 — **STALE**, latest explicit TP in the
corpus) … **refresh at the next BWLP research note**."* **This is that note**, a year later.
NOK 172 → **NOK 262** is a **+52%** move in the anchor. At the repo's Aug-28 FX (0.106791) NOK 262
≈ **$27.98**; Pareto states $28.5 themselves, presumably on a fresher rate.

**What I think it means.** This is the single cleanest owner action in the window: a named, dated,
explicit broker target replacing one the watchlist already flags as stale, on a DEEP name. It also
**sharpens the open BWLP newbuild fork** (`decisions/bwlp_nb_order_fork_2026-08-31.md`): Pareto is
pricing "1.2x our forward NAV" while `inputs/fleet_manifests/bwlp.yaml` line 90 still carries
`vessels_under_construction: 0` for the 8-hull ~$940M HHI order. A *forward* NAV almost certainly
includes those hulls; the model's NAV definitionally excludes them. **The two NAVs are not the
same object**, and the TP refresh should not be wired without settling that.

**What I am NOT sure of.** (a) Pareto's forward-NAV basis — I have the daily's summary, **not the
report** (see COVERAGE LIMITS); I cannot say whether their NAV is YE-26 or NTM, or how they treat
the newbuilds. (b) Whether `analyst_target` is the right field: BWLP's comment treats it as a real
research TP (unlike GNK/CMDB where it is a broker NAV), so NOK 262 fits the field's meaning — but
the pair rule means the price leg and FX vintage must move with it, not after it. (c) The $28.5
USD figure implies an FX of ~0.1088, not the repo's 0.106791 — **do not mix them**.

**Decision-log status: UNREAD.** No occurrence of "262", "upgrade" or "BUY (HOLD)" in
`decisions/bwlp_log.md`.

---

### M2 · SBLK — the **final Athens offering price lands at €24.50 / $28.40**, 6× oversubscribed; the log's own "Watch" is now satisfied

**Date:** 2026-09-11 (6-K `0000950157-26-001003`, filed after the close).
**Source:** `inputs/filings/SBLK/0000950157-26-001003_6-K_ex99-1.htm` — primary text, read locally.

**What happened.** *"The final offering price of the Company's New Shares was determined at €24.50
(US$ 28.40) per New Share"*; **4,400,000** New Shares allocated; demand *"amounted to 26,788,512
shares … a total value of €656.3 million, resulting in the Public Offering being oversubscribed by
over 6 times."* FX stated as €1 = 1.1592 USD (ECB, 11.09.2026). Allocation detail by investor
category is promised for **Tuesday 15 September**.

**Model surfaces touched.** (a) Share count — gross proceeds 4.4m × €24.50 = **€107.8m (~$125m)**.
(b) `inputs/watchlist.yaml` `SBLK.current_price: 30.4` (Pareto 28 Aug) — the clearing price $28.40
is 6.6% below that static. (c) The pinned SBLK flip margin and the open discretionary leg.

**What I think it means.** The `sblk_log.md` 9/10 entry closes with *"Watch: the ≥9/11 final-price
6-K."* **It has arrived.** That entry pre-registered the effect at the **$28.2 midpoint** — the
actual $28.40 is within a whisker, so the pre-registered ≈ −0.6% NAV/sh conclusion should hold
essentially unchanged, i.e. **still under the 2pp gate**. Pareto (9/09) independently pegs the
range at **0.80–0.89× NAV**, so $28.40 ≈ **0.85× Pareto NAV**. The 6× oversubscription is the
genuinely new information and it cuts against Pareto's own puzzlement (9/09: CEO Pappas *"don't
need capital"*, *"won't seek the highest possible valuation"* — Pareto called the below-NAV pricing
*"a little puzzling"*). It was priced well below where it could have cleared.

**What I am NOT sure of.** The **post-offering share count is still UNVERIFIED**. The 9/10 log entry
is explicit that the count walk must start from the 6/30 **outstanding** 111,671,386 and that
post-6/30 repurchases are undisclosed. **This 6-K does not state a new total count** — unlike SB's
(M5), which does. So the count remains derived, not sourced.

**Decision-log status: UNREAD.** No occurrence of "24.50", "28.40", "oversubscrib" or "656.3" in
`decisions/sblk_log.md`; the newest triage row in `decisions/filings_triage_log.md` is 9/10.

---

### M3 · CCEC — a **vessel delivery, a charter and a $52.8m ECA loan** that no local channel saw

**Date:** 2026-09-09.
**Source:** GlobeNewswire 3359057 (issuer-originated wire), *"Capital Clean Energy Carriers Corp.
Announces the Delivery of Its Third Handy Liquefied CO2 Multi-Gas Carrier 'Alkimos'"*.
**Date verified at the issuer's own wire, not an aggregator** — release date 9/09, delivery date
9/09, internal dates forward-looking (TC through May 2027). Not a re-publication.

**What happened.** HMG/C **Alkimos** delivered **9 September 2026**; commenced a time charter *"with
an expected duration through May 2027"*; financed with cash on hand plus a **12-year ECA-backed loan
of $52.8 million**, with up to **$8.1m** further borrowing capacity if the vessel secures longer-term
employment. Alkimos is *"the third latest-generation HMG/C delivered to the Company, bringing the
total number of vessels on the water to 21."* Under-construction census now: *"six additional
latest-generation LNG/Cs, four MG/Cs, one HMG/C and one LNG dual-fuel bunkering vessel"*, delivering
Q1-2027 → Q1-2029.

**Model surfaces touched.** `inputs/fleet_manifests/ccec.yaml` — the manifest is AS-OF **2026-06-30**
and its header carries the 7/29 census *"seven latest-generation LNG/Cs, four MG/Cs and two HMG/Cs
and one LNGB/V (50%)"*. The new census moves **HMG/C 2 → 1** (Alkimos out) and **LNG/C 7 → 6**. The
LNG/C decrement is **already accounted for** in the manifest header (*"LNG/C Alcaios I ~7/31"* is
recorded as a post-6/30 delivery that stays an NB row). **So Alkimos is the one genuinely new
delivery**, and it moves a hull from the NB book into the water. Also touches the balance sheet
(+$52.8m drawn debt, an asset on the water) and the vessels-on-water count (21).

**What I think it means.** This is exactly the class of item this sweep exists for. **CCEC filed no
6-K for it** — there is no CCEC arrival in `state/edgar_manifest.jsonl` anywhere in the window — so
the EDGAR sentinel, the NewsWeb poller and the Pareto dailies were all structurally blind to it. It
reached the model's surface only through a web search. CCEC is an **APPROX-P/NAV name** (no Pareto
coverage, `consensus_pnav: 0.90` "kept at ~book"), which makes manifest accuracy the main thing
holding its valuation together.

**What I am NOT sure of.** (a) Whether the repo's LNG/gas curves carry an HMG/C (liquefied-CO2
multi-gas) class at all, or whether Alkimos needs the Group-B "under-construction at delivered
market value" convention retired for this hull and a real on-the-water mark chosen. (b) The **charter
rate is not disclosed** — only the tenor — so this is a schedule/manifest determinant, **not** a
curve input. (c) I did not verify the 21-on-the-water figure against a count of `ccec.yaml` rows;
the manifest is not shaped as a flat per-hull list (my row-count probe returned 0), so that
reconciliation needs someone who knows the file's schema.

**Decision-log status: UNREAD.** No occurrence of "Alkimos", "52.8", "multi-gas" or "CO2" in
`decisions/ccec_log.md`, and no "Alkimos" row in `inputs/fleet_manifests/ccec.yaml`.

---

### M4 · TNK — a **1-year suezmax fixture at $100,000/day**, and Pareto calling its own TNK NAV "outdated"

**Date:** 2026-09-08.
**Source:** `inputs/research_pareto/2026/09/2026-09-08_Periodical-ShippingDaily-2026-09-08-529264.pdf`,
headline *"TNK: Talk of suezmax TC that would set a new benchmark"*.

**What happened.** Verbatim: *"TNK now appears to have fixed its 2011-built suezmax 'Barcelona
Spirit' for a year at $100,000/day. The charterer is Mercuria, start-up imminently."* Pareto's own
arithmetic around it: the vessel *"will generate ~$34m of EBITDA over the next 12 months, which
compares with the $60m value we have in our $96/share NAV. Adding ~$10m of value per ship also adds
~$10/share of NAV in TNK."* And separately: *"We currently assume $54k/45k for suez/afra in 2027.
Lifting this to $80/70k would push our EPS from $11.4 to $20.4."*

**Model surfaces touched.** (a) **The suezmax 1-year TC curve** — a stated rate with a stated tenor
on a named hull is the shape that can supersede a curve input. (b) **`inputs/watchlist.yaml`
`TNK.consensus_pnav: 0.91`** at `current_price: 88.2` implies a broker NAV of **88.2 / 0.91 =
$96.9/sh** — which is, to within rounding, **the very $96/share NAV Pareto has just described as
"outdated"**. (c) Suezmax vessel marks: Pareto is carrying this hull at $60m and saying a
comparable move is worth ~$10m/ship.

**What I think it means.** Two separable things, and the second is the more important one. The
fixture is a **promotable candidate** (P1). But the **anchor finding** is that TNK's broker-NAV
anchor of record is now **disowned by its own author**, and disowned in a known direction — Pareto
say the name *"has re-priced sharply recently and is now in line with our (outdated) NAV for the
first time in a while"*, and that adding ~$10m/ship adds ~$10/sh. So the watchlist's TNK broker NAV
is **biased low**, by roughly 10% on the source's own sensitivity. That is a live distortion in the
tool-vs-broker spread for TNK, and it is not a stale-price problem the pair rule catches — the
*price* leg is fine; it is the NAV the P/NAV was quoted against that has gone stale.

**What I am NOT sure of.** (a) **Single-source and hedged** — "Talk of", "appears to have fixed";
no issuer confirmation and no independent corroboration found (see COVERAGE LIMITS). Promoting a
curve input on market talk would be the wrong call. (b) Whether the $96/sh is the same NAV the
0.91× P/NAV was struck against, or a different Pareto vintage — they are consistent to a dollar,
which is suggestive but not proof. (c) Whether one benchmark-setting fixture at a geopolitical peak
should move a *curve* at all, versus being recorded as a top-of-market observation.

**Decision-log status: UNREAD.** No occurrence of "Barcelona Spirit", "Mercuria" or "100,000/day"
in `decisions/tnk_log.md`, and the item is absent from `decisions/sp_queue_triage_2026-09-07.md`
(correctly — it is a fixture, not an S&P print, so that queue does not own it; but nothing else
picked it up either).

---

### M5 · SB — the placement **completes and is confirmed at 113,833,473 shares**, and Pareto publishes a **first-ever external NAV** for an APPROX name

**Date:** 2026-09-10 (AGM results) and **2026-09-11** (Athens admission); plus Pareto 9/09.
**Sources:** `inputs/filings/SB/0001317861-26-000048_6-K_f091126sb6k.htm` (primary, local);
`inputs/filings/SB/0001317861-26-000047_6-K_f091026sb6k.htm`; the 9/09 Shipping Daily.

**What happened — the count is now SOURCED.** The 9/11 6-K states: *"Following the Private
Placement, the Company's issued capital of common stock consists of **113,833,473 shares** of common
stock with a nominal value of $0.001 each."* Trading in the 12,000,000 New Shares commences on
Euronext Athens **Monday 14 September**.

**What happened — the external NAV.** Pareto, 9/09, on the placement: *"We do not have coverage of
the name but peg back-of-the-envelope NAV at **$11 – 12/sh** (thus trading at ~0.75x NAV)."*

**Model surfaces touched.** (a) The SB Q3 balance-sheet pre-registration in `decisions/sb_log.md`
(9/10) predicted *"count 113,833,473"* — **an issuer filing has now confirmed that exact number**,
converting a derived figure into a sourced one. (b) `inputs/watchlist.yaml` `SB.consensus_pnav: 1.13`
— an **APPROX P/BV proxy**, whose comment says plainly *"SB stays ABSENT from Pareto's table — own-
basis lane, cannot ride the Pareto sweep."* Pareto has now published an SB NAV anyway. (c) The
repo's own tool NAV/sh for SB is **$10.72**, sitting just below Pareto's $11–12 range.

**What I think it means.** The count confirmation is small but clean — it removes an UNVERIFIED tag
from a pre-registered build, and it is the kind of thing that is free to bank now and annoying to
reconstruct later. The Pareto NAV is the more interesting one: SB's APPROX status rests on the claim
that no broker NAV exists. **One now does**, and it brackets the tool's own $10.72 from above. That
does not make SB Pareto-anchored — Pareto say explicitly they do not cover it and that the figure is
back-of-the-envelope — but it is the first external check the APPROX proxy has ever had, and it is
mildly confirmatory of the tool.

**What I am NOT sure of.** (a) Whether a self-described "back-of-the-envelope" figure from a
non-covering broker should touch `consensus_pnav` **at all** — my instinct is no, and that it belongs
in the log as a cross-check, not in the anchor. (b) The AGM (three Class III directors elected,
Deloitte ratified) is governance routine and I see no valuation content in it. (c) Pareto's "~0.75x
NAV" was struck against the pre-placement tape, not the 9/09 close of $8.36 the log records.

**Decision-log status: the placement itself is READ** (`decisions/sb_log.md` 9/10, and three rows in
`decisions/filings_triage_log.md`). **The 9/11 Athens-admission 6-K and the Pareto NAV are UNREAD** —
no occurrence of "113,833,473" outside the 9/10 pre-registration, and no occurrence of the Pareto
$11–12 figure anywhere.

---

### M6 · PRODUCT TANKERS — **two MR prints ~10% above broker marks**, a sector-wide mark move, and a defect in the existing S&P triage

**Date:** 2026-09-09.
**Source:** 9/09 Shipping Daily, *"Product tankers: MRs sold ~10% above our generic quotes"*.

**What happened.** Verbatim: *"A 2014-built vessel (Korean) is said to have gone to Turkish interests
for **$35.5m**. We had her at **$31.6m**. A Japanese-built MR (2018) was sold for **$45.5m** to Greek
buyers with a drydock due before YE. This compares to our generic quote of **$40.9m**."* And the
sector move: *"Brokers have started to reverse the downwards revisions they made over the summer, and
**0 - 10Y old MRs are up $2m during the last two weeks** (sitting just $1m below their 10Y highs)."*
Plus a peer-group frame: *"we peg our product tanker peer group at **EV/GAV ~0.9x** on average – with
TORM / HAFNI at 1.01 – 1.03x, DIS at 0.85x and **STNG at 0.75x**. Increasing asset values by 10%
boosts the NAVs in TORM, HAFNI, DIS and STNG to DKK 247 – 0.91x (DKK 221), NOK 85 – 0.95x (NOK 78),
€10.4 – 0.69x (€9.2) and **$115.6 – 0.71x ($106.4)**, respectively."*

**Model surfaces touched.** The MR / product marks curve (ASC, HAFN, TRMD, STNG). Note the useful
cross-check: Pareto's current STNG NAV of **$106.4** reconciles almost exactly with the watchlist's
implied broker NAV (`77.4 / 0.73 = $106.03`) — **the STNG anchor is healthy**, unlike TNK's in M4.

**A defect in the existing triage, which is why this is MATERIAL and not just WATCH.**
`decisions/sp_queue_triage_2026-09-07.md` (addendum dated 9/10) triaged **only one** of the two
prints, and mis-paired its comparator:

> `| 5 | 9/09 · MR, Japanese-built 2018, "$45.5m to Greek buyers…"; Pareto "We had her at $31.6m" |`

**$31.6m is Pareto's mark for the *2014 Korean* hull that sold for $35.5m** — not for the 2018
Japanese hull, whose comparator is the **$40.9m generic quote**. So: (a) the **2014 Korean / $35.5m
print is missing from the queue entirely**, and (b) the retained row overstates the gap as
$45.5m-vs-$31.6m (+44%) when the true gap is $45.5m-vs-$40.9m (**+11.2%**). The correct pair of gaps
is **+12.3%** and **+11.2%** — which, pleasingly, is exactly the "~10%" the headline claims, and a
much less dramatic number than the row implies.

**What I think it means.** The triage's *disposition* was right — **UNNAMED, not promotable** — and
that stands for both hulls. But an inflated gap sitting in a queue is a landmine for whoever reads
it next at the "next MR curve read" the row itself schedules.

**What I am NOT sure of.** Neither hull is named and neither buyer is identified beyond nationality,
so **neither is promotable** and I am not proposing otherwise. Whether the +$2m/two-week sector move
is itself enough to trigger an MR curve re-read is a judgement I don't have the standing to make.

**Decision-log status: partially read, with the defect above.**

---

### M7 · BRUT — the financial calendar implies a **reporting-cadence change** the calendar file does not carry

**Date:** 2026-09-07 (NewsWeb/MFN, staged locally).
**Source:** `inputs/filings/BRUT/newsweb_2026-09-07_349fe45a-29ad-54a5-9fa5-f3141236f3b0.txt`.

**Carry-over, flagged honestly:** the 9/07 digest already reported this release as its item M8
(including the 19 Nov date), and it is **still UNREAD** a week later. I am not re-reporting it as a
new find. **What is new here is one observation the previous digest did not make.**

**The observation.** The calendar lists *"19.11.2026 - Quarterly Report - Q3"* and *"18.02.2027 -
Quarterly Report - Q4"*. But `inputs/earnings_calendar.yaml` carries BRUT as
`disclosure_type: Oslo newsweb (**half-yearly**)`, with its confirmed window being the 8/13
half-yearly report. **Bruton appears to be moving from half-yearly to quarterly reporting** — which
changes not just a date but the *number* of report-day events BRUT generates, and BRUT is a name with
a **pending post-demerger carry ruling** and a prereg history of being frozen across a report day.

**What I am NOT sure of.** Whether the Euronext Growth Oslo regime actually requires this, or whether
Bruton is electing quarterly reporting voluntarily post-demerger. Either way the calendar file's
`disclosure_type` for BRUT is now describing the wrong cadence. Also note `earnings_calendar.yaml`
still reads `quarter: 2026-Q2` with `last_date_sweep: 2026-09-10` — the Q3 re-seed has not run, so
this may simply be waiting for it.

---

## PROMOTABLE CANDIDATES

| # | Name | Item | Fields present | Fields MISSING — why it is a candidate, not a print |
|---|---|---|---|---|
| **P1** | **TNK** | 'Barcelona Spirit' fixed **1 year @ $100,000/day** to **Mercuria**, start imminent (Pareto 9/08) | hull name · class **suezmax** · built **2011** · **rate** · **tenor** · charterer | **Issuer confirmation.** Pareto's own wording is *"Talk of…"* / *"appears to have fixed"*, and no independent corroboration was found. **LEAD-QUALITY.** A fixture this far above the curve should not move a curve input on single-source market talk. |
| **P2** | **CCEC** | **HMG/C Alkimos** delivered **2026-09-09**, TC through **May 2027**, **$52.8m** 12-yr ECA loan (+$8.1m accordion) | hull name · class · **delivery date** · charter tenor · financing amount + tenor | **Charter rate not disclosed**, and no price — so this is a **manifest/schedule + balance-sheet** determinant, *not* a marks or curve input. Issuer-sourced and date-verified; the cleanest item in the window. |
| **P3** | product / MR | 2014-built **Korean** MR → Turkish interests, **$35.5m** (Pareto mark $31.6m; **+12.3%**) | class · built year · **price** · buyer nationality | **No hull name, no IMO, no named buyer.** Not promotable. **Not currently in the S&P queue at all** — see M6. |
| **P4** | product / MR | 2018 **Japanese**-built MR → Greek buyers, **$45.5m**, drydock due before YE (generic quote $40.9m; **+11.2%**) | class · built year · **price** · buyer nationality | **No hull name, no IMO.** Not promotable. Already in the queue as row 5, but **with the wrong comparator** — see M6. |

---

## WATCH

- **W1 · BWLP's newbuild programme is now financed, re-rated, and still off the model.**
  `inputs/fleet_manifests/bwlp.yaml:90` still reads `vessels_under_construction: 0` for the 8-hull
  ~$940M HHI order. As of this window it is funded by a $300m convertible (9/02) **and** the broker
  has upgraded on a "forward NAV" that presumably contains those hulls (M1). This was owner-summary
  item 2 in the 9/07 digest and has not moved; the fork doc `bwlp_nb_order_fork_2026-08-31.md` is
  still the open decision.
- **W2 · The 2343 Monthly Return (8/31, `hkex-12308484`) is staged and UNREAD, and it answers an
  open rider.** The watchlist's 2343 block carries an explicit **RE-DERIVATION RIDER**: *"the H1
  buyback (~9.5M sh for ~$3.5M…) — VERIFY whether 5,165.247803M is the 30-Jun post-buyback count
  before the next re-derivation."* An HKEX **Monthly Return is precisely the document that states the
  issued share count.** It is on disk at
  `inputs/filings/2343/12308484_2026083101113.pdf` (67KB) and `decisions/2343_log.md` has no mention
  of it. Out of window (8/31), so not MATERIAL — but it is a cheap answer to a question the watchlist
  is actively asking.
- **W3 · CMBT's SGM agenda is still not retrieved.** The 8 October SGM (record date 9/24, freeze
  9/23–9/25) is READ (`cmbt_log.md` 9/10), and that entry correctly notes the SGM is *"the gate the
  log flagged for the $0.64 distribution"* and that *"the agenda is not in the 6-K — settles at the
  convening notice on cmb.tech."* It still has not been settled. A distribution gated on a meeting
  three weeks out is worth knowing the agenda of.
- **W4 · Carry-overs from the 9/07 digest that remain UNREAD in the decision logs.** I checked each:
  - **SBLK's 133-hull Arrow Research per-vessel appraisal** (30-Jun-2026 effective) — no occurrence
    of "Arrow Research" or "apprais" in `decisions/sblk_log.md`. This was owner-summary item 1 and the
    previous digest called it *"the most valuable single dataset this sweep has ever turned up for a
    dry-bulk validator."* Still untouched.
  - **LPG (Dorian) Hanwha 3× Panamax VLGC order + the $368.4m facility** — no occurrence of "Hanwha",
    "368.4" or "213.4" in `decisions/lpg_log.md`.
  - **CAPT `analyst_target: 18.90`** — still the superseded NOK 180 target in `inputs/watchlist.yaml`.
  - **STNG's three fixtures (P1–P3 last week)** — no fixture entry found in `decisions/stng_log.md`.
- **W5 · GOOD NEWS, recorded so it is not re-flagged: the TEN channel gap is closed.** TEN's CIK is
  now in the EDGAR poller (see COVERAGE LIMITS). The residual is the multi-week 6-K lag, which is a
  property of the issuer, not of the channel.
- **W6 · Dividend/ex-date mechanics, all record-only, listed so the sweep is auditable rather than
  silent:** BWLP ex-div 9/07 Oslo / 9/08 NYSE (NOK 8.8914 / US$0.95); HAFN ex-div 9/07 Oslo / 9/08
  NYSE (US$0.5003 — already in `hafn_log.md`); BRUT ex cash distribution US$0.025 on 9/10; CAPT ex-div
  NOK 3.00 on 9/10; NAT ex-div $0.27 on 9/10 (record 9/10, pay 9/24); INSW ex-div $5.05 on 9/10. Per
  the repo's own triage convention an ex-date is not a valuation event.
- **W7 · TRMD share count moved, trivially.** 9/11 6-K: capital increase of **31,483 Class A shares**
  on RSU exercise at DKK 179.80; share capital now **102,421,267 A-shares**. That is **+0.031%** —
  immaterial to NAV/sh, but it is a sourced count and `decisions/trmd_log.md` does not carry it.

---

## NO-ACTION — names swept clean, with the basis for each negative

Each line states what was actually searched. None of these is a bare "nothing found".

| Name | Basis for the negative |
|---|---|
| **MPCC** | **PRIMARY-SOURCED.** `mfn.se/all/a/mpc-container-ships.json` fetched directly: newest release is **8/26** (Q2 results + dividend key-info). Nothing in-window. Local poller agrees (polled 9/12, 0 new). |
| **CAPT** | **PRIMARY-SOURCED.** MFN feed fetched: newest release **9/10** (ex-div), which is staged locally and triaged record-only. Nothing after it. |
| **BRUT** | **PRIMARY-SOURCED.** MFN feed fetched: newest release **9/10** (ex-distribution). Only in-window items are the 9/07 calendar (M7, carry-over) and the 9/10 ex-date (W6). |
| **BWLP** | MFN feed fetched: newest release **9/07** (ex-div, the `ob`/`mfn` twin correctly counted as ONE event). The material BWLP item this window is the **broker** note (M1), not an issuer release. |
| **OMC** | **PRIMARY-SOURCED.** MFN feed fetched: the feed contains **exactly two releases ever** — 8/28 (first day of trading) and **9/09** (financial calendar, AR 2027-02-25, already triaged to PLAN.md). No carry-ruling-relevant disclosure. |
| **2343** | **CHANNEL-BACKED.** `hkex_poll.json` polled **2026-09-12T17:20Z**; newest staged 2343 filing is the **8/31 Monthly Return**, before the window. HKEXnews web search returned 0 records but is **not** relied on (see COVERAGE LIMITS). |
| **DHT, ECO, FRO, INSW, NAT, ASC, STNG, FLNG, GNK, GSL, CMDB, LPG** | **CHANNEL-BACKED:** zero in-window arrivals in `state/edgar_manifest.jsonl`, with all 22 CIKs polled daily through **9/12** and **no in-window lane failures** in `edgar_poll.err`. **PLUS** web searches over the window for NAT, CCEC/GSL/CMBT, STNG/ASC/INSW/DHT, ECO/FRO/FLNG/LPG and GSL/MPCC — the only in-window hits were dividend ex-dates (W6) and CCEC's delivery (M3, which is *not* clean and is reported above). LPG's order + facility are **9/02–9/04**, i.e. the *previous* window, already reported as that digest's M3. |
| **CMBT** | In-window arrival read: the 9/08 SGM notice — READ and triaged (W3). Nothing else. The 9/04 H1 unreadability flagged last week is **RESOLVED** (86 page images recovered by hand 9/07; Q2 pair landed 9/10). |
| **HAFN, TRMD, SB, SBLK** | In-window arrivals all read as primary text and reported above (M2, M5, W6, W7). |
| **TEN** | **WEAKEST NEGATIVE IN THE SET — read with care.** TEN's Q2/H1 results released **9/10** and are handled (`decisions/ten_h1_release_check_2026-09-10.md`, `ten_shadow_build_2026-09-11.md`). Web search confirms Q2 EPS **$3.14** vs consensus $2.93, H1 net income $228m / $7.12 per share, and a **$3.1bn / 26-newbuilding** renewal programme said to have appreciated ~30% since contracting. I did **not** re-verify these against the issuer release, because the repo already has a verifier-checked read of it. TEN's 6-K has not landed and the issuer lags weeks, so no timely lane negative is possible for TEN. |

---

## OWNER SUMMARY — ranked

1. **BWLP's stale TP now has its replacement (M1).** `analyst_target: 17.52` carries a comment that
   literally says *"refresh at the next BWLP research note"*; the note arrived 9/10 with **BUY, TP
   NOK 262 / $28.5**. Highest-value, lowest-ambiguity item in the window — **but do not wire it
   without first settling W1**, because Pareto's "forward NAV" and the model's NAV are not the same
   object while `vessels_under_construction: 0` stands.
2. **The 9/11 Friday archive gap trips the owner's own re-look condition.** Third Friday (8/14, 8/21,
   9/11), unaccepted, and — unlike the first two — **the Pareto lane was alive that day** (a Container
   Weekly landed). Different failure shape, so it should not inherit the 8/21 acceptance. Needs a
   channel-side walk, which only the owner can authorise. Secondary: **8/14 has no `accepted[]` entry
   at all**, only a mention in 8/21's prose.
3. **CCEC delivered a ship and nothing local saw it (M3).** Alkimos, 9/09, with financing and a
   charter tenor, on an APPROX name whose valuation leans hard on manifest accuracy. This is the
   BRUT/MPCC failure shape caught in the same week it happened — which is the whole point of the
   sweep. Wire at the next CCEC refresh.
4. **SBLK's final price closes an explicitly pre-registered watch (M2).** $28.40 vs a $28.2
   pre-registered midpoint means the ≈−0.6% NAV/sh call should stand unchanged; 6× oversubscription
   is the new colour. Cheap to close out. The **post-offering count is still unsourced**.
5. **Fix the S&P queue row before anyone acts on it (M6).** One of two MR prints is missing, and the
   retained row's comparator is off by a hull — it reads as a +44% gap when the real one is +11.2%.
   The disposition (unnamed → not promotable) is correct and unchanged; only the numbers are wrong.
6. **TNK's broker NAV anchor is disowned by its own author (M4).** Pareto call their $96/sh
   "outdated" and quantify the direction (~+$10/sh). The watchlist's implied broker NAV is $96.9.
   The tool-vs-broker spread for TNK is currently reading against a mark its source has retracted.
   The 'Barcelona Spirit' fixture (P1) is attractive but is **single-source market talk** — the
   anchor issue is the part that is safe to act on.
7. **Bank SB's confirmed share count (M5).** 113,833,473 is now stated in an issuer filing, exactly
   as pre-registered. Free to convert from derived to sourced. Pareto's $11–12 SB NAV is worth a log
   line as the first external check the APPROX proxy has ever had — and, in my view, **not** worth
   touching `consensus_pnav` for.
8. **Four carry-overs from last week are still unread (W4)** — the SBLK Arrow appraisal above all,
   plus Dorian's order, CAPT's superseded target, and STNG's fixtures. The appraisal in particular
   does not decay, but it also does not promote itself.

---

*Review-only run. This digest is the only file written. No pipeline, no promotion, no ingest, no
git, no YAML touched. Nothing here has reached the model — every item above requires a human
promotion decision.*
