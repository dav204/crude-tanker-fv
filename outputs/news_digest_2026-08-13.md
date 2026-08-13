# News digest — 2026-08-13

Agent web-sweep (the AGENT half of `/news-pull`), first run under the scheduled task
`crude-fv-weekly-news-pull`. **Review-only — nothing here is promoted; this file is the
only write of the run.** Promotion of any item is a human follow-up (promote → rerun →
drift loop).

## Run header

- **Run date:** 2026-08-13
- **Window swept:** **2026-06-21 → 2026-08-13** (~7.5 weeks). Prior digest =
  `outputs/news_digest_2026-06-21.md`. This is the first sweep since the 8-week lapse
  that PLAN.md records (the agent half ran 6/10 and 6/21, was deferred 6/14 under the
  crude-edge freeze, and was never re-docketed while the mechanical job of the same name
  reported `ok` every Saturday).
- **Names swept:** 25/25 — the full `inputs/watchlist.yaml` roster.
  DHT · ECO · FRO · INSW · TNK · NAT · FLNG · CCEC · STNG · HAFN · TRMD · ASC · TEN ·
  CMDB · SBLK · GNK · CAPT · MPCC · GSL · BRUT · CMBT · SB · LPG · BWLP · 2343.
- **Depth weighting:** DEEP pass on the 9 APPROX names read live from
  `reconcile.APPROX_PNAV_TICKERS` = {NAT, ASC, CCEC, TEN, CMDB, MPCC, GSL, SB, 2343};
  DEEP on the 4 Oslo/Euronext-quoted names (BRUT, MPCC, CAPT, BWLP — no EDGAR lane);
  DEEP on the live-event names (GNK tender, INSW, BRUT, CMBT, SBLK, FRO, TRMD); lighter
  pass on the broker-covered remainder.
- **Sources searched:** web search over issuer releases and their syndicators
  (GlobeNewswire, Business Wire, PR Newswire, MFN.se / modular-finance, Oslo NewsWeb
  message pages, live.euronext.com company-news pages), trade press (TradeWinds,
  Splash247, Argus, Marine Log, Container News, Baird Maritime, Hellenic Shipping News,
  Shipping Herald, Cyprus Shipping News), SEC EDGAR 6-K/8-K/10-Q landing pages, and
  aggregators (StockTitan, TipRanks, Investing.com, MarketScreener, Simply Wall St,
  stockanalysis.com). Repo-side: `inputs/watchlist.yaml`, `src/.../reconcile.py`,
  `inputs/archive_gaps.yaml`, `PLAN.md`, and the heads of
  `decisions/{brut,gnk,capt,mpcc,2343}_log.md`.

### Coverage limits of THIS run — read before trusting any "nothing found"

1. **No primary-document fetches.** `.claude/settings.json` allowlists `WebFetch` by
   domain; every issuer/exchange/trade-press domain needed here (globenewswire.com,
   live.euronext.com, mfn.se, newsweb.oslobors.no, splash247.com, tradewindsnews.com,
   pacificbasin.com, mpc-container.com, globalshiplease.com …) is **not** on that list, so
   a fetch would have raised a permission prompt with no human awake — the exact failure
   that kills these runs. **Every figure below therefore comes from search-engine
   summaries of those pages, not from the page itself.** Treat all of it as
   *lead-quality*: verify against the primary release before any figure touches a
   manifest, a balance sheet, or a curve input. Adding the issuer/newswire domains to the
   `WebFetch` allowlist would upgrade this whole lane and is the single highest-value fix
   for next week's run.
2. **No directory enumeration.** `Glob`/`Grep` were not available to this session and
   shell is off-limits per the task's tool discipline. So: the previous-digest date was
   established by targeted `Read`s (2026-06-21 exists; 2026-08-01 and 2026-08-08 do not)
   corroborated by PLAN.md's own account of the lapse — **not** by listing `outputs/`. A
   digest between those dates under an unexpected filename would have been missed.
   Likewise §Archive gaps below is read from the repo's own records rather than from a
   listing of `inputs/research_pareto/**`.
3. **Roster note:** the task prompt names **ODL** as an Oslo/Euronext name to sweep.
   There is **no ODL row in `inputs/watchlist.yaml`** and no ODL entry in
   `APPROX_PNAV_TICKERS`. Either the name was never onboarded or it was dropped; ODL was
   **not** swept. Worth a one-line owner ruling so the prompt and the roster agree.

### Archive gaps — Pareto coverage over this window is thin BY SOURCE, and now evidenced

Could not enumerate `inputs/research_pareto/**` directly (limit 2 above). From the repo's
own records (`PLAN.md` 2026-08-13 PM + `decisions/brut_log.md` 2026-08-13 PM +
`inputs/archive_gaps.yaml`):

- The new 8b ARCHIVE-GAP check reports **5 gaps** in the live tree, including the 6-day
  **7/03 → 7/14** hole that hid the BRUT 7/07 release, plus **7/15–19**, **7/21–27**,
  **7/29–8/02**.
- The 8/13 PM owner-directed audit ruled these **SOURCE-QUIET, not un-backfilled**: an
  uncapped Rocket.Chat history walk (`--since 2026-07-01`, 2,379 messages) found **zero
  Pareto-lane posts** in the window while the sibling FFA lane ingested normally, and the
  archive equals the channel exactly for 7/01 → 8/13. **Nothing exists to backfill.**
- **But `inputs/archive_gaps.yaml` still carries `accepted: []`.** The evidence for
  acceptance exists and is dated; the acceptance entries have not been written. Until they
  are, the gaps stay formally unaccepted and the check keeps firing. (Not written here —
  review-only, and acceptance is an owner judgment by that file's own header.)
- **Consequence for this digest:** roughly 7/03 → 8/02 has thin *Pareto* coverage for
  reasons on the source's side, which is precisely why the web-side sweep below is
  load-bearing for that stretch. Items in that stretch are reported from issuer/trade
  sources, not from the Pareto archive.

---

## MATERIAL — needs an owner decision or a model-input change

### M1 · 2343 (Pacific Basin) — 2026-08-06 Interim Results are OUT and appear unread
**What happened.** H1-2026 interim results released 2026-08-06: revenue ~$1.105bn (+8.5%
y/y), profit attributable ~$105m (+310% y/y), underlying profit $94.9m (vs $21.9m),
EBITDA $197.8m, basic EPS HK16.1c; **interim dividend HK15.5c** (vs HK1.6c a year
earlier); net cash $157m; buyback continuing. Handysize TCE $14,150/day and Supramax
$16,550/day, both stated as beating the indices.
**Source.** Issuer interim announcement 2026-08-06, via TipRanks / BigGo / Simply Wall St
summaries of it (primary: pacificbasin.com IR — not fetchable this run).
**Model surface.**
- `inputs/balance_sheets/2343` — 2343 is the book's only **semi-annual** reporter and its
  manifest header vintage is **31-Dec-2025**. A **30-Jun-2026** sheet now exists. This is
  the first vintage refresh available since onboarding, and the pair guard will want the
  manifest moved with it.
- `inputs/watchlist.yaml` `2343.consensus_pnav: 0.98` — the comment says in terms:
  *"VALUE VINTAGE Dec-2025 vs a Jul-2026 price … the true current pnav runs LOWER
  (~0.87-0.9). **Re-derive at the 2026 Interim.**"* The Interim is the trigger and it has
  fired.
- `inputs/dividend_policies/2343` — HK15.5c interim, a ~10× step up.
**What I think it means.** The stalest anchor in the book just got its scheduled refresh,
and the direction (strong H1, large dividend step-up, net cash) argues the Dec-2025
composite understates today. **What I am NOT sure of:** whether the interim report
republishes the **per-class composite broker fleet values** that the AR2025 p.6 anchor was
built from (US$1,958.3M @ 31-Dec-2025). If it does not, the re-derivation needs a
different basis and that is a methodology call, not a data refresh.
**Status.** No entry at the head of `decisions/2343_log.md` (newest = 8/10 auto run) —
this looks **unread**, not merely un-actioned.

### M2 · MPCC — 2026-06-25 issuer release: 4 ships bought, $375m loan, 2 divestments
**What happened.** Oslo, 25 June 2026: MPCC agreed to acquire **four 2023–24 built,
7,000 TEU eco-conventional container vessels for $340m total**, each delivered with a
**three-year fixed-rate time charter to a top-5 liner** (stated $180m revenue / $140m
expected EBITDA across the charter period). Funded via a **$375m senior secured term
loan** underwritten by Société Générale with BNP Paribas, Crédit Agricole and ING in the
syndicate. **Delivery expected October–November 2026.** The same release forward-fixed two
existing vessels and agreed to **divest two non-strategic vessels**.
**Source.** Oslo NewsWeb message 676947 (2026-06-25), syndicated via modular-finance /
TradingView, MarketScreener, MarineLink, Container/Breakbulk trade press.
**Model surface.** `inputs/fleet_manifests/mpcc` (+4 hulls with Oct–Nov-2026 delivery
dates, −2 disposals, 2 charter-coverage changes); `inputs/balance_sheets/mpcc` (+$375m
secured debt and the associated commitment); container TC/coverage inputs.
**What I think it means.** This is a ~$340m transaction against a name whose watchlist
market cap basis is $2.44/sh — materially fleet-changing, and it lands **4 days into the
window**. `decisions/mpcc_log.md` head shows only the 8/13 Pareto-text triage and auto
runs, so this reads as **unread in the log**. **It is the same shape as the BRUT miss** —
an Oslo issuer release with no EDGAR lane and no issuer-release channel watching NewsWeb.
That missing channel is the load-bearing remediation surface PLAN.md already named; this
is a second instance of it, seven weeks old.
**What I am NOT sure of:** whether the two divested vessels are named/priced in the full
release (the summaries do not name them), and whether the $340m is allocated per vessel.

### M3 · GNK — the Diana tender EXPIRED 2026-07-24; the watchlist anchor is now dead
**What happened.** Diana Shipping's tender offer for all Genco shares it did not already
own **expired 2026-07-24 at 5:00pm NY**, and Diana **determined not to extend or
reinstate** it. As of 7/10, 11,081,926 shares had been validly tendered — 29.7% of
non-Diana held shares, 25.4% of shares outstanding. Diana had earlier extended (6/29,
7/13) and floated a revised proposal at **$27.34 implied** ($24.80 cash + one Diana
share at a $2.54 30-day VWAP). Genco's board reiterated its Comprehensive Value Strategy
and that any offer must compensate for full NAV plus a control premium.
**Source.** Genco statement 2026-07-27 (GlobeNewswire / gencoshipping.com IR); Diana
releases 6/29, 7/13, 7/27; SC TO-T/A amendments via StockTitan.
**Model surface.** `inputs/watchlist.yaml` `GNK.analyst_target: 24.80` is explicitly
pinned to the **live** tender — its comment reads *"Diana Shipping LIVE CASH TENDER
$24.80/sh … deadline Jun 26 2026"* and carries a **DEAL CAVEAT** that price is pinned to
tender odds, not NAV, "until the tender resolves." **It has resolved.**
**What I think it means.** Two things now need an owner call: (a) re-point
`analyst_target` off the dead tender — Pareto's own **$28.4/sh NAV (8/06, 0.9×)** is
already recorded in `decisions/gnk_log.md` and is the natural replacement; (b) retire the
deal caveat, which unblocks reading GNK's EV-vs-price without deal noise for the first
time since onboarding. Note the model currently prints GNK **TRIM/SHORT** at a +10.8pp
broker spread — a read that was explicitly not trustworthy while the caveat stood.
**What I am NOT sure of:** whether Diana retains a stake and intends a fresh approach;
that would re-introduce deal noise on a different footing.

### M4 · FRO — the two-VLCC price IS disclosed: $270m aggregate, $135m per ship
**What happened.** Issuer release **2026-08-04, "FRO – Sale of two VLCCs"**: agreement to
sell **two 2017-built VLCCs for an aggregate $270m** ($135m per ship), delivery to the
buyer expected **Q3-2026**; net cash proceeds after debt repayment ~**$179m**; expected
**~$110m gain in Q3-2026**; and the board resolved to return the ~$179m via a **one-time
special dividend of $0.80/share**.
**Source.** GlobeNewswire issuer release 2026-08-04; corroborated by Splash247, Argus,
IndexBox, Cyprus Shipping News. SEB is quoted calling $135m/ship market-clearing and
supportive of recently raised broker VLCC valuations.
**Model surface.**
- **§9.9 VLCC transaction anchor** — 2 × VLCC, built 2017 (age 9), **$135.0m each**. This
  is a promotable-shaped print (see P1) and it lands directly in the class the Stage-A
  work is built on.
- `inputs/fleet_manifests/fro` — −2 hulls on Q3-2026 delivery.
- `inputs/dividend_policies/fro` — a one-time $0.80/share special.
**What I think it means.** This closes PLAN.md's **OPEN PRINT FLAG**, which recorded
*"FRO 2×2017-built VLCCs (8/04, 'extreme prices', **NO price disclosed yet** — watch MB
W33/W34 + FRO Q2)"*. The price was **in the issuer release on the day**; the repo's read
came off a Pareto paragraph that did not carry it. This is a textbook **absence-isn't-
evidence** catch — a structured figure that a single source dropped, recorded as "not yet
disclosed."
**What I am NOT sure of:** the **vessel names** are not in the release summaries. Under
the 2026-08-09 WORKFLOWS rule (4 unnamed-print duplicates caught that round), an unnamed
print must be swept against the class file before promotion.

### M5 · INSW — a new four-ship LR1 newbuild order alongside the Q2 print
**What happened.** Q2-2026 (released 2026-08-06, call 8/10): record net income and
adjusted net income **$295m**, record adjusted EBITDA **$345m**, record quarterly FCF
**$261m**; H1 vessel-sale gains **$88.1m**; H1 profit $581m. Board declared the **largest
quarterly dividend in company history, $5.05/share** (declared 8/07, record 9/10, payable
9/24). Separately, INSW **contracted four scrubber-fitted, dual-fuel-LNG-ready LR1s at
K Shipbuilding (Korea), $244m aggregate, delivery H2-2028.**
**Source.** INSW 8-K exhibit on sec.gov (EDGAR), plus Business Wire/Morningstar and
10-Q coverage.
**Model surface.** The Q2 financials were pre-registered and landed 8/10 with the band
HIT, so those are on record. The item that may not be is the **LR1 quartet**: under §9.6
newbuilds are valued at delivered market **less remaining commitment**, PV-discounted
`1.11^(−years_to_delivery)` — so a $244m aggregate commitment with an H2-2028 delivery is
a real NAV input, and it needs a per-vessel commitment figure with a citation before it
can go on curve (`NAV_FIGURE_ESTIMATE_QUEUE` discipline).
**What I think it means.** Verify-don't-assume: confirm whether the 8/10 refresh carried
the newbuild book, or only the balance sheet and fleet-on-the-water. **What I am NOT sure
of:** whether the $244m is stated per-vessel anywhere, or only in aggregate.

### M6 · GSL — 15 newbuilds ordered, $1.33bn; dividend raised to $2.50 annualised
**What happened.** Q2-2026 (2026-08-05): operating revenue $198.7m, net income to common
$89.3m ($2.48 EPS); H1 revenue $396.8m. **Ordered 15 mid-size, ultra-high-reefer,
wide-beam latest-generation newbuilds, aggregate contract price $1.33bn**, >75% covered by
expected adjusted EBITDA from initial charters. Added **$1.45bn of contracted revenue in
H1**, taking total contracted revenue at 30-Jun-2026 to **$3.2bn** over a TEU-weighted 3.3
years; charter cover 100% of 2026 and 90% of 2027. Dividend **$0.625/qtr**, annualised
raised to **$2.50**.
**Source.** GSL 6-K on sec.gov (EDGAR) + GlobeNewswire release 2026-08-05.
**Model surface.** `inputs/fleet_manifests/gsl` gains a 15-ship newbuild book (§9.6
treatment, per-vessel commitments needed); `inputs/balance_sheets/gsl`;
`inputs/dividend_policies/gsl`; and — the sharp edge — **`GSL.consensus_pnav: 0.75` is a
P/B proxy on a DEPRECIATED-COST book**, flagged WEAK at onboarding. A $1.33bn forward
commitment sits outside that book entirely, so the proxy degrades further rather than
merely ageing.
**What I think it means.** GSL is an APPROX name whose only anchor just got materially
less representative. Worth an explicit owner note on whether the P/B proxy survives the
newbuild book or needs a different basis. **What I am NOT sure of:** the delivery schedule
across the 15 hulls, which drives the PV discount and is not in the summaries.

### M7 · TNK — four fleet-renewal transactions inside the window
**What happened.** Q2-2026 (2026-07-29): GAAP net income $225.9m, adjusted $193.6m — the
highest quarterly adjusted net income in TNK's history; Suezmax spot TCE $109,171/day,
Aframax/LR2 $74,149/day; fixed quarterly dividend $0.25 (record 8/10, payable 8/21), H1
dividends $1.50/share including the $1.00 special declared in May. Fleet renewal:
**bought 3 × 2016-built Aframaxes for $141.5m** and **2 Suezmax newbuilding contracts for
$190.0m**; **sold a 2009-built Suezmax for $53.5m** and a **2013-built VLCC for $84.5m**.
**Source.** TNK 6-K on sec.gov (EDGAR) + GlobeNewswire / teekay.com release 2026-07-29.
**Model surface.** `inputs/fleet_manifests/tnk` (−2 on the water, +3 Aframax, +2 Suezmax
newbuild contracts under §9.6); `inputs/balance_sheets/tnk`; and two §9.9-shaped prints
(see P2).
**What I am NOT sure of:** the Aframax trio is **en bloc at $141.5m with no disclosed
per-vessel split** — §9.9 excludes aggregates with no split, and there is no back-solve.
The two disposals appear to be individually priced, which is what makes them candidates.

### M8 · CMBT — Bristol sold; **gain disclosed, price not** (so: not promotable)
**What happened.** Fleet update **2026-08-11**: sale of the **Suezmax Bristol, 2024-built,
156,851 dwt**, generating a capital gain of **~$56.9m in Q4-2026** based on net sale price
and book value; vessel delivers to its new owner in Q4-2026. With Bristol, CMB.TECH has
declared roughly **$620m of tanker sale gains across 2026**. Q2-2026 results are scheduled
**2026-08-27**.
**Source.** CMBT 6-K (EDGAR) + GlobeNewswire "CMB.TECH fleet update" 2026-08-11;
TradeWinds and Splash247 corroborate the $57m gain framing.
**Model surface.** `inputs/fleet_manifests/cmbt` — −1 Suezmax at Q4-2026 delivery;
`inputs/balance_sheets/cmbt` at the Q2 pair.
**What I think it means.** PLAN.md expected this in the Saturday 8/15 print queue. It
should go into the queue as a **fleet/manifest** item, **not** as a transaction anchor:
the release discloses a **gain against book**, not a net sale price. Backing a price out of
gain-plus-book is exactly the back-solve §9.9 forbids. If CMBT discloses the price at the
8/27 Q2, it becomes a clean 2-year-old Suezmax print — a young node the Suezmax fit would
value.

### M9 · CCEC — Alcaios I delivered 7/31 on an 18-month TC, funded by a $170m SLB refi
**What happened.** Q2-2026 (2026-07-29): revenue $104.9m (+8% y/y), net income $29.0m
(vs $29.7m), contracted backlog **$2.9bn firm / $4.3bn with options**, dividend $0.15
(77th consecutive). **2026-07-31: took delivery of the LNG carrier Alcaios I**, which
immediately commenced a previously announced **18-month index-linked time charter**. The
acquisition was funded with cash on hand plus **$170.0m of total proceeds raised through
refinancing two existing sale-and-leaseback facilities** (for the LNG/Cs Aristos I and
Aristarchos).
**Source.** GlobeNewswire releases 2026-07-29 (Q2) and 2026-08-03 (Alcaios I delivery);
CCEC 6-K via StockTitan.
**Model surface.** `inputs/fleet_manifests/ccec` (+1 LNGC on the water from 7/31, with a
charter);`inputs/balance_sheets/ccec` — and note the **ECO precedent in CLAUDE.md**: a
sale-leaseback belongs in *borrowings* with no separate operating-lease line, so a
**refinancing of two SLB facilities** is the case where a double-count is easiest to
introduce. CCEC is an APPROX name (no Pareto P/NAV) routed through `sectors.lng`.

---

## PROMOTABLE CANDIDATES — flagged only; promotion is the human loop

**Standing rule applied (WORKFLOWS, 2026-08-09):** sweep the class file before promoting
**any** unnamed print — that round caught 4 unnamed-print duplicates that were all
re-reports.

| # | Name | Vessel / class | Built | Price | Date | Notes |
|---|------|----------------|-------|-------|------|-------|
| P1 | FRO | 2 × VLCC (**unnamed**) | 2017 | **$135.0m each** ($270m agg.) | 2026-08-04 | Q3-26 delivery. Clean per-ship price. Unnamed → duplicate-sweep required. Closes PLAN's open flag. |
| P2a | TNK | Suezmax (**unnamed**) | 2009 | **$53.5m** | 2026-07-29 (Q2 disclosure) | Single-vessel, individually priced. |
| P2b | TNK | VLCC (**unnamed**) | 2013 | **$84.5m** | 2026-07-29 (Q2 disclosure) | Single-vessel, individually priced. |
| P3 | STNG | **STI Solidarity**, LR2 | 2015 | **$60.0m** | Q2-2026 | **Named, single, priced — the cleanest print of the window.** |

**Surfaced but NOT promotable, with the reason (recorded so it isn't re-derived):**

- **STNG en-bloc lots — no per-vessel split, no back-solve (§9.9).** Q2: STI Opera /
  STI Aqua / STI Regina (2014 MRs) **$105.0m combined**; STI Osceola / STI Seneca /
  STI Black Hawk (2015 MRs) **$105.0m combined**; STI Park / STI Sloane / STI Madison
  (2014 LR2s) **$195.0m combined**. July: four LR2s **$285.8m combined**, and one MR at
  **$35.0m** (single-vessel and priced, but neither named nor year-dated in the summaries —
  promotable *if* the 6-K names it).
- **CMBT Bristol** (2024 Suezmax, 156,851 dwt) — **gain disclosed, price not**. See M8.
- **CMDB Bermondi** (2009-built, 55,469 dwt, sale agreed, concludes Q3-2026) — **no price
  disclosed**.
- **DHT Bauhinia** (2007 VLCC, **$51.5m**) — agreement dates to **January 2026**
  (pre-window); only the *delivery* fell in July 2026. Almost certainly already on record;
  listed for completeness, not as new.
- **LPG: Corsair** (2014 VLGC, net proceeds **$80.8m**) and **Constellation** (2015 VLGC,
  net proceeds **$85.6m**), both completed July 2026 — **VLGC is not one of the 8 fitted
  §9.9 classes** (VLCC/Suezmax/Aframax/LR2/MR/Cape/Pana/Supra-Ultra), and CLAUDE.md is
  explicit that classes don't get added without a comparable sample. Recorded as sector
  marks only.

### Fixtures with stated rate + tenor (can supersede curve inputs)

- **DHT Jaguar — 3-year TC at $75,000/day**, fixed July 2026, to a global energy company.
  A VLCC *term* print inside the window; bears on the LR2/VLCC term-vs-front reading the
  Stage-A deck rests on.
- **BRUT Mount Vision — 3+1+1yr index-linked, $95,000/day fixed for the first 9 months**;
  **BRUT Mount Horizon — $106,000/day**, joins mid-Nov-2026. **Both already on record**
  (brut_log 2026-08-13); repeated here only because they are the window's other term
  VLCC prints and Horizon ≈ the ruled $105,700 Stage-A single print.
- **MPCC — 4 vessels each on a 3-year fixed-rate TC to a top-5 liner.** Per-ship rate is
  **not disclosed**; the release gives $180m revenue over the period, which implies
  ~$41.1k/day/ship gross — **my arithmetic (180e6 ÷ 4 ÷ 3 ÷ 365), a derived figure, not a
  disclosed one.** Do not treat it as a print.

---

## WATCH — moves a falsifier or a thesis, no action demanded yet

- **BWLP (Oslo primary, deep pass) — a large negative mark ahead of the 8/28 Q2.**
  Pre-announced Product Services segment update: gross trading result ≈ **−$19m** after a
  **−$146m mark-to-market** on open cargo contracts and hedges; estimated segment net ≈
  **−$31m**. Shipping side ~85% of Q2 days fixed at ~**$81,000**, stated well above
  breakeven. **Q2 results 2026-08-28.** Also still open from onboarding: `BWLP.analyst_target`
  rests on a **Pareto TP NOK 172 dated 2025-09-02** — flagged stale at onboarding, to be
  refreshed at the next BWLP note.
- **SBLK — Q2 (8/05–8/06) lands on top of a frozen disposition.** Net income $144.9m,
  TCE $24,486/day, adjusted $1.21 EPS on $357.4m revenue (vs $0.98/$281.0m consensus);
  **dividend $0.90**, record 8/21, 22nd consecutive. Took delivery of **3 Kamsarmax
  newbuilds in Q2 with 5 more through H2-2026**; **sold 3 older vessels** ($60.3m proceeds
  in Q2, a further $31.5m expected in Q3 — **per-vessel prices not disclosed**). Cash rose
  $409.4m → $565.3m. Bears directly on the **SBLK BUY→HOLD one-word disposition the owner
  still owes** (PLAN.md: band-mech is purely 12M composition, ΔNAV 0.0).
- **ECO — record Q2 corroborates the Stage-A VLCC tape.** Fleet-wide TCE **$181,000/day**;
  **spot VLCC $213,600/day**, spot Suezmax $174,900/day; adjusted EPS $5.91 (H1 $8.28);
  adjusted EBITDA $252m; **dividend $5.25** (89% of net income, 17th consecutive) —
  **ex-div Oslo 8/13, NYSE 8/14**, payable 8/21. Nissos Vous delivered July, completing the
  18-ship fleet (8 VLCC / 10 Suezmax). The Q2 spot VLCC print sits just above the verified
  $206.6k QTD figure that drove the Stage-A front breach — corroboration, not contradiction.
  **PLAN.md already flags the ex-div: do not read the price drop as drift**, and the staged
  8/07 watchlist-rebase draft pre-dates the ex-date.
- **ASC (APPROX) — Q2 7/29.** Adjusted $48.3m / **$1.18 EPS**; net income $60.5m including
  a **$12.2m gain on the sale of the Ardmore Engineer**; **dividend $0.79** (payable 9/15,
  record 8/28), 15th straight. **Exercised options for two more Handysize newbuilds,
  taking the order to four** — a §9.6 newbuild-book addition.
- **SB (APPROX; the book's lone TIGHT BUY) — Q2 7/28.** Adjusted EBITDA $50.3m, adjusted
  EPS $0.28, average 45.13 vessels, TCE **$20,642/day**; **dividend raised to $0.075**
  (19th consecutive, record 8/13, payable 8/26); fleet 46 vessels. **Agreed to acquire two
  newbuild 82,500 dwt Chinese Kamsarmaxes** (Q3-2028 and Q1-2029). Dry-bulk manifest `dwt`
  is load-bearing (§11.7.10/11) — 82,500 dwt is a Kamsarmax against the Pana 82k baseline,
  so it must be entered exactly, not rounded into a Panamax cohort.
- **CMDB (APPROX) — Q2 8/03.** Adjusted net income $9.8m ($0.40/sh), net income $5.2m
  ($0.21/sh); H1 adjusted $22.2m; voyage revenue $111.6m (H1 $223.1m); liquidity $331.5m
  with **cash exceeding debt by $108.9m**; fleet 30 vessels / ~2,665,000 dwt. The **Cargill
  International transaction completed**, no pending transfers of the related trading book.
  CMDB's `analyst_target` and `consensus_pnav` are both **book-derived** — a 30-Jun-2026
  book is now available to re-derive both.
- **TEN (APPROX; the §15 governance archetype) — semi-annual dividend $1.00 paid 7/30.**
  No Q2 report inside the window (TEN reports Q2 later in the year). The payout is a
  strip-terminal datapoint for a name whose `governance_discount_pct` is judgmental.
- **NAT (APPROX; the §12 archetype) — no Q2 in window** (expected late Aug / early Sep).
  Q1 (6/14, just before the window) beat at $0.22 EPS with the quarterly dividend **raised
  $0.17 → $0.22** (115th straight), fleet ~90% booked at **$68,000/day** for Q2 with opex
  below $10,000/day. Reported alongside: **two Suezmax newbuilds added for 2028 delivery** —
  I could **not** pin the order date, so I cannot say whether it falls in this window.
  Worth confirming against the manifest.
- **TRMD — Q2 due 2026-08-26** (matches the standing calendar). From Q1: FY-2026 guidance
  upgraded to TCE **$1,150–1,450m** / EBITDA **$800–1,100m**; **six MR resales purchased**
  (first two delivering Q1-2027, two more later in 2027, final two in 2028) — a newbuild-book
  input if not already carried.
- **HAFN — half-year report scheduled 2026-08-28.** A fleet line surfaced in search
  (Q2: sold and delivered one LR1, one MR and three Handys, with a further MR committed and
  pending delivery) that I could **not** tie to a dated primary release. **Treat as
  unverified** until the 8/28 report.
- **FLNG — Q2 results 2026-08-19** (invitation issued). Charter items seen but **not
  datable inside this window** from the summaries: a new 2-year TC for Flex Aurora with up
  to six option years; 2-year extension options exercised on Flex Resolute and Flex
  Courageous; a 15-year charter commenced for Flex Constellation. FY-2026 guidance:
  revenue ex-EUA $345–370m, TCE $73,000–78,000/day, adjusted EBITDA $255–280m, 91.2%
  coverage for the rest of 2026. **Verify dates at the 8/19 release** before treating any
  of it as in-window.
- **STNG — balance sheet transformed.** As of 7/28: unrestricted cash $2.0bn plus $483.2m
  undrawn revolver, gross debt $655m → **net cash ~$1.31bn**, after redeeming $200m of
  7.5% senior notes and making $389.1m of unscheduled secured prepayments. Q2 net income
  $387.5m ($8.47 basic EPS), record adjusted EBITDA $300.5m, dividend $0.45. **Repurchased
  1,994,236 shares at an average $77.72** — above the $73.00 watchlist price vintage
  (3-Jul Pareto pair).
- **CAPT — pre-window but §9.6-shaped, worth a provenance check.** On **2026-06-15/16**
  (i.e. *before* this window opens, and inside the 6/21 digest's own window), CAPT
  announced the acquisition of **three scrubber-fitted VLCC newbuilding contracts** from
  Capital Maritime at the original contract price of **$122.0m + $0.7m each**, building at
  Hengli (Dalian), delivering **Sep / Oct / Nov 2027**. **Upfront $37.3m per vessel
  ($111.8m) payable by 30-Jun-2026; balance $85.4m per vessel ($256.2m) due on delivery.**
  Indicative appraisals $150.0m each. **13 options retained** (11 VLCC + 2 Suezmax) at the
  original contract price until 31-Dec-2026. Every §9.6 input (remaining commitment,
  delivery date) is disclosed here — worth confirming it is in the CAPT manifest with
  citations rather than as an estimate. Pareto's in-window CAPT color is already triaged in
  `decisions/capt_log.md` (8/13).
- **DHT — a newbuild order and a term fixture.** June 2026: agreement with **Hanwha** for a
  VLCC with a scrubber, **delivery August 2028**. July 2026: **DHT Jaguar fixed on a
  3-year TC at $75,000/day** (see fixtures). Q2 (8/04): EPS $1.23, revenue $285.0m (+96%),
  net income $198.3m, fleet-wide TCE **$126,700/day**; **dividend $1.22**, 66th consecutive
  (record 8/17, payable 8/24).
- **BRUT — already fully on record as of today; nothing found after the 8/13 AM entry.**
  The 7/07 chain (Mount Vision delivered 7/08, sale-leaseback signed on the 4 NTS hulls,
  **demerger announced**, interim CEO Svensen), the **8/12 AGM** (routine slate + share
  premium reduced **US$226,039,548** into contributed surplus effective 8/12), and the H1
  release + Pareto 8/13 read are all captured in `decisions/brut_log.md`. Independent
  corroboration this sweep: MFN.se / modular-finance syndication of the 7/07 release, the
  Euronext Growth Oslo listing of the 8-ship spin **by late August**, BRUT's own uplisting
  to Expand/Oslo Børs targeted **end-September**, and the $1.47bn / $216m equity program
  figures. **Open owner item unchanged:** how the model carries a structural split
  (one 12-ship NAV today vs pre/post-demerger entities), which compounds with the 8/16
  deck re-expression.

---

## NO-ACTION — swept, nothing in the window that touches the model

State of coverage per name, so this reads as coverage rather than inference. Every line
below means: **searched the sources listed in the run header over 2026-06-21 → 2026-08-13,
nothing found that moves a model surface** — not "no news exists."

- **FLNG** — searched, nothing in-window that is datable and model-moving; the Q2 release
  lands 8/19 (see WATCH).
- **HAFN** — searched, no dated in-window primary surfaced; half-year report 8/28 (WATCH).
- **TRMD** — searched, nothing in-window beyond the Q1 guidance already carried; Q2 8/26.
- **NAT** — searched, no in-window issuer release found; Q2 expected late Aug / early Sep.
- **TEN** — searched, only the 7/30 semi-annual dividend; no Q2, no corporate action.
- **LPG** — searched; the two VLGC disposals are logged above as out-of-scope-by-class,
  and the FQ1-2027 print (8/05: adjusted $2.52 EPS, revenue $187.9m, record TCE
  $75,926/day, **$1.00 irregular dividend** paid ~8/12, one dual-fuel Panamax VLGC ordered
  from HD Hyundai for Q3-2029) contains nothing else that touches a model surface.
- **CAPT** — searched; the only material item is pre-window (WATCH).
- **BRUT** — searched; everything found is already on record (WATCH).
- **ECO / DHT / STNG / SB / ASC / CMDB / SBLK / INSW / GSL / TNK / CCEC / CMBT / GNK /
  MPCC / 2343 / FRO / BWLP** — all carry an item above; none swept clean.

**Names with a genuinely clean sweep this window: none.** Every one of the 25 produced at
least a dated datapoint. That is itself the finding: a 7.5-week gap in this lane is not a
quiet period, and the two items that had gone unread the longest (M1 2343, M2 MPCC) are
both in the class the sweep exists to cover — no broker doing the work, no EDGAR lane.

---

## Owner summary — what I'd action first

1. **M2 MPCC (6/25)** — seven weeks unread, ~$340m of fleet change plus $375m of debt, and
   structurally identical to the BRUT miss. It is the second proof that the **missing
   NewsWeb issuer-release channel** is the load-bearing gap.
2. **M1 2343 (8/06)** — the book's stalest anchor hit its own stated re-derivation trigger.
3. **M4 FRO (8/04)** — the price exists; the open flag saying it does not should be closed.
4. **M3 GNK (7/24)** — a watchlist anchor pinned to a tender that no longer exists.
5. **Two process items:** write the evidence-backed accepted-gap entries into
   `inputs/archive_gaps.yaml` (the 8/13 RC walk supports them, the file is still empty);
   and consider allowlisting the issuer/newswire `WebFetch` domains so next week's sweep
   can read primaries instead of search summaries.
