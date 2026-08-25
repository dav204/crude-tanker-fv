# News digest — 2026-08-24

## Run header

- **Window swept:** **2026-08-16 → 2026-08-24** (9 days). Prior digest established by
  listing `outputs/` — `news_digest_{2026-06-10, 06-21, 08-13, 08-16}.md` are the only
  four on disk; 08-16 is the head, so the window opens where its Run 2 closed.
- **Names swept:** 25/25, the full `inputs/watchlist.yaml` roster —
  DHT · ECO · FRO · INSW · TNK · NAT · FLNG · CCEC · STNG · HAFN · TRMD · ASC · TEN ·
  CMDB · SBLK · GNK · CAPT · MPCC · GSL · BRUT · CMBT · SB · LPG · BWLP · 2343.
- **Depth weighting.**
  - **DEEP — non-US issuers** (no EDGAR sentinel; this sweep is their only channel):
    BRUT, MPCC, CAPT, BWLP (`.OL`), 2343 (`.HK`). All five read at the **primary issuer
    feed**, not the trade press.
  - **DEEP — APPROX-pNAV names** (`APPROX_PNAV_TICKERS` read live from
    `src/crude_tanker_fv/reconcile.py:69`, not hardcoded — the set is
    `{NAT, ASC, CCEC, TEN, CMDB, MPCC, GSL, SB, 2343}`): NAT read at `nat.bm` primary;
    CMDB read at its staged 6-K; the rest via the EDGAR lane + search.
  - **DEEP — live-event names:** GNK (Diana), BRUT (demerger), FRO (open P1 print),
    2343 (Interim Report), CMBT (Q2 8/27).
  - **Lighter — broker-covered US remainder:** DHT, ECO, INSW, TNK, FLNG, STNG, HAFN,
    TRMD, ASC, SBLK, GSL, SB, LPG, CMBT, TEN, CCEC — covered by the local EDGAR manifest
    plus targeted search.
- **Sources searched.** Primary: `mfn.se/all/a/{bruton-limited, capital-tankers,
  mpc-container-ships, bw-lpg}.json`; `nat.bm`; the staged filing bodies under
  `inputs/filings/` (BRUT, MPCC, ECO, STNG, CMDB, FLNG, HAFN, TRMD, 2343). Syndicated
  primary: manilatimes (GlobeNewswire mirror). Search sweeps: Genco/Diana, FRO S&P,
  CMB.TECH, CCEC/LPG/ASC, general week-33/34 S&P and newbuilding tape. Repo-side:
  `state/{edgar_manifest.jsonl, edgar_poll.log, edgar_poll.json, newsweb_poll.json,
  hkex_poll.json, price_refresh.log, price_refresh.err, sentinel.log}`,
  `inputs/{watchlist, archive_gaps, data_sources, earnings_calendar}.yaml`,
  `inputs/research_{pareto,mb,issuer}/`, `inputs/market_data/prices_daily.yaml`,
  `inputs/{fleet_manifests,balance_sheets,dividend_policies}/`, and the heads of
  `decisions/{brut, gnk, fro, cmbt, 2343}_log.md`.

### COVERAGE LIMITS of this run — read before trusting any "nothing found" below

1. **The three ingest lanes were DOWN for most of this window and recovered ~2 hours
   before this run.** `state/edgar_poll.log` shows **unbroken `SKIPPED: network not up
   (sec.gov unresolvable)` from before 08-24T01:12Z through 08-24T19:24Z**, and today's
   sentinel line records **`FETCH-FAILED edgar-poll: 100 consecutive skipped-no-network
   runs`**. The lane came back on the run stamped `21:00:31Z` in
   `state/edgar_manifest.jsonl`, which staged **5 new filings / 9 docs at once** —
   ECO 8/17, STNG 8/17, CMDB 8/18, FLNG 8/19, HAFN 8/21, TRMD 8/24, 2343 8/21 (×3),
   BRUT 8/20 (×2), MPCC 8/19. **So the local channel is now caught up and I read it
   directly** — but it was blind for days, and nothing downstream has consumed the burst.
   This is the good news of the run: the catch-up landed *before* the sweep, not after.
2. **The price lane has NOT recovered.** `state/price_refresh.err` shows **seven
   consecutive daily stand-downs, 2026-08-18 through 2026-08-24**, all
   `SKIPPED: network not up (query1.finance.yahoo.com unresolvable after ~30s)`.
   `inputs/market_data/prices_daily.yaml` is stamped `fetched_at: 2026-08-19T04:46:23Z`
   and carries only 08-18/08-19 `asof` values. The sentinel is flagging it correctly
   (`PRICE-BASIS fetch is 5d old — cron missed?`, and `FETCH-FAILED price-refresh: 7
   consecutive`). **See M2 — this collides with M1 tomorrow.**
3. **Measured fetch results this run** (fresh, not copied from prior digests):
   - `globenewswire.com` — **`timeout of 60000ms exceeded`, twice**, on the GNK 8/17 open
     letter. This is now the **fourth consecutive run** the domain has timed out. I
     retried once then fell back to the **manilatimes GlobeNewswire mirror**, which
     returned the full release text. **The GNK figures in M4 are syndicator-sourced, not
     issuer-primary** — treated as such below.
   - `nat.bm/press-releases/` — **HTTP 404**; the site root `nat.bm` fetched fine and
     carries the release list. Use the root, not that path.
   - All four `mfn.se` slugs fetched cleanly, first try.
   - `sec.gov`/`efts.sec.gov` **not attempted for enumeration** — prior runs measured 403
     and the local manifest is the better instrument. **I am not claiming EDGAR was
     enumerated**; the US-listed negatives below rest on the local poller, which as of
     `20:20Z` reports `polled 22 names: 0 new filing(s)`.
   - `splash247.com` / `hellenicshippingnews.com` — appeared in search results but were
     **not fetched** (prior-measured 403); their content below is search-summary only and
     is marked LEAD-QUALITY.
   - Staged PDFs (2343) were read locally with `pdftotext`, not fetched.
4. **Tooling:** `Glob`/`Grep` were again absent this session; read-only `Bash`
   (`ls`, `find`, `grep`, `head`, `cat`, `sed`, `pdftotext`, a stdlib `python3`
   HTML-to-text one-liner) was used for repo inspection per the standing allowance.
   No writes besides this file, no `git`, no project code executed.

### ARCHIVE GAPS — unaccepted holes inside this window

- **`inputs/research_pareto/2026/08/` ends at 2026-08-18.** Missing business days in or
  adjacent to the window: **08-14 (carried from the last digest), 08-19, 08-20, 08-21,
  and 08-24.** That is a **run of three consecutive business days (08-19..08-21)**, which
  meets `archive_gaps.yaml: limit_business_days: 3`. **None of these are accepted** in
  `inputs/archive_gaps.yaml` — its five accepted entries all sit in June/July.
  **Consequence: every Pareto-lane "nothing found" for 08-19 onward is UNSUPPORTED, not
  absent.** This is flagged owner-side via `STALE-INPUT harvester: newest broker issue
  2026-08-12 (12d; limit 10d)`, so the lane silence is visible — but the *gap* is not yet
  adjudicated. I did not backfill and did not add an accepted entry; both are owner calls.
- **The MB S&P lane is 17 days silent.** `inputs/research_mb/tanker_weekly/2026/` ends at
  **W32 (2026-08-07)**; `lng_weekly` ends **W32 (2026-08-06)**. **W33 and W34 — which
  cover this entire window — are absent locally.** Today's sentinel confirms:
  `STALE-INPUT mb:{tanker,dry_bulk,container}_weekly: newest 2026-08-07 (17d)`,
  `mb:lng_weekly: newest 2026-08-06 (18d)`. **This is the exact channel the open FRO P1
  print was waiting on** (see P3). Any "no new S&P prints this window" claim is therefore
  **unsupported for weeks 33–34**, and I have not made one.

---

## MATERIAL

### M1 · BRUT — the demerger is **EXECUTED, not pending**. Ex-date is **TOMORROW (2026-08-25)**.

**What happened.** Two releases, both **2026-08-20**, read from the **issuer feed as
primary** and confirmed byte-for-byte against the locally staged bodies
`inputs/filings/BRUT/newsweb_2026-08-20_{a04debcc…, 792b2c10…}.txt`:

1. *"Resolved distribution in kind of shares/NDRs in OMC Tankers Ltd."* — the board has
   **resolved** the distribution. Bruton has **already contributed** to OMC Tankers:
   - **the last four New Times Shipyard newbuilding contracts**, deliveries targeted
     **January, March, June and August 2029**, **aggregate commitments USD 472 million,
     of which USD 47.2 million paid**;
   - **the four Yantai CIMC Raffles contracts**, deliveries targeted **January, March,
     May and July 2028**, **aggregate commitments USD 499 million, of which USD 49.9
     million paid**;
   - **USD 50 million in cash**.
   - *"Except for approximately USD 82 thousand of trade payables and the remaining
     shipyard obligations, no indebtedness has been transferred."*
   - Consideration: **61,923,808 shares in OMC Tankers** issued to Bruton.
   - OMC Tankers **has applied for admission to Euronext Growth Oslo and is expected to
     be admitted to trading on 28 August 2026.**
2. *"Key Information in connection with a distribution of shares in OMC Tankers Ltd."* —
   the dated timetable. **Ratio 1:1** (one OMC NDR per Bruton NDR; 61,923,808 NDRs
   issued). **Date of approval 20 Aug · Last day including the right 24 Aug (TODAY) ·
   Ex-date 25 Aug · Record date 26 Aug · Distribution 27 Aug · First day of OMC trading
   28 Aug.** Distribution made from the **Contributed Surplus** account.

**Source.** `https://mfn.se/a/bruton-limited/bruton-limited-brut-resolved-distribution-in-kind-of-shares-ndrs-in-omc-tankers-ltd`
and `…/bruton-limited-brut-key-information-in-connection-with-a-distribution-of-shares-in-omc-tankers-ltd`
(issuer feed, both 2026-08-20). Independently present in `state/edgar_manifest.jsonl`
with `source: "newsweb"`.

**Model surfaces this touches — this is the largest single item in the window.**
- **`inputs/fleet_manifests/brut.yaml`** — the manifest is a **12-VLCC** vehicle
  (`fleet_summary.VLCC_count: 12`, `newbuilds_committed: 12`). **Eight of those twelve
  leave.** Mapping the release to the manifest rows: the four CIMC hulls are the
  `VLCC_cimc_2028` row (`count: 4`), and the four departing NTS hulls are
  `VLCC_endeavour / VLCC_odyssey / VLCC_venture / VLCC_voyager`. **BRUT retains four** —
  Vision, Horizon, Frontier, Summit.
- **`fleet_schedule.VLCC: [1, 2, 2, 2, 3, 4, 4, 6]`** — the 8-quarter on-water ramp is
  built on all twelve. The 2028+ tail (`3, 4, 4, 6`) is largely the departing hulls, so
  **the strip's forward earning fleet is overstated from q1'28 onward** once the
  distribution completes.
- **Remaining commitment.** The manifest header carries **"~$1,370M remaining commitment
  ($1,484M total − $114M paid)"**. The release moves **$971M of total commitment and
  $97.1M of payments** out — i.e. **~$873.9M of remaining commitment departs**, leaving
  BRUT with **~$496M** on four hulls. *(That subtraction is my arithmetic off the
  release's own figures, not a sourced issuer statement — flagged as such.)*
- **`inputs/balance_sheets/brut_2026-Q2.yaml`** — **$50M of cash leaves.** The Q2 sheet
  correctly holds the demerger as a **subsequent event** (its header lists all five
  post-6/30 events and notes the board approval was *"conditional on that entity's
  listing"*). **That condition is now resolved**, which is precisely the trigger the
  sheet was waiting on.
- **`inputs/watchlist.yaml` BRUT block** — `current_price: 6.32`, `consensus_pnav: 0.86`,
  `analyst_target: 7.13`. All three are **pre-demerger, whole-company** figures. Pareto's
  NOK 66 NAV values twelve hulls.
- **§15 going-concern screen.** `decisions/brut_log.md` recorded the H1 screen as
  *"branch (a)-with-progress"*, resting explicitly on *"eight hulls remain unfinanced at
  the snapshot **and the demerger that would move them is conditional on a listing that
  has not occurred**."* **The listing is now expected 28 August.** The load-bearing clause
  of that screen expires this week.

**Is it UNREAD in the log?** **Yes.** `decisions/brut_log.md`'s newest entry is the
`2026-08-16T20:06:34` auto-run; there is **no annotation of the 8/20 releases**. The log's
own reserved-to-owner item (b) — *"How the model carries the DEMERGER … a 12-ship NAV
stops being the right object once it completes"* — is **now due, with a date on it.**

**What I am NOT sure of.** (a) **I cannot size the NAV split without running the model,
and I did not run it.** NAV here is a small difference of large numbers (the manifest's own
"max torque" caveat: a 10% asset move shifts NAV ~40%), so the departing 8 hulls' NAV
contribution is **not** 8/12 of $9.62 — it is (8 delivered-market marks, PV-discounted)
minus $873.9M commitment, plus the $50M cash. **This must be computed, not estimated.**
(b) Whether the owner wants BRUT carried as the **post-demerger 4-ship entity** or as a
**stub + OMC claim** through 27 Aug is a methodology decision I have no authority over.
(c) The release gives **no per-vessel prices or delivered-market marks**, so nothing here
is promotable to `vlcc.yaml`.

---

### M2 · **The dead price feed and the BRUT ex-date collide tomorrow.** Highest-urgency item.

**What happened.** Two independently-true facts that are dangerous together:

- **BRUT trades ex-distribution on 2026-08-25** (M1). On that print, BRUT.OL loses the
  market value of 8 of 12 hulls plus $50M cash from its share price. **This is a
  distribution, not a re-rating.**
- **`price_refresh` has stood down seven consecutive days** (08-18 … 08-24, all
  `network not up`), so the newest committed price is the **08-18 NOK 63.6 / $6.7621**
  entry in `prices_daily.yaml`.

**Why this is the thing to act on first.** When the network returns, the next successful
refresh will fetch a BRUT price that is **ex-distribution**, and hand it to a pipeline
whose manifest still carries **twelve** hulls. The repo has already been bitten by exactly
this class of event twice, and both precedents are on file:

- **The TEN $44 incident** (`CLAUDE.md`, `decisions/ten_log.md` 2026-06-10) — a price that
  did not match its paired vintage silently moved broker NAV.
- **The 2343 static-fallback release** (`decisions/2343_log.md` 2026-08-16) — a stale
  static plus a ±30% guard produced a **band exit (HOLD → TRIM/SHORT, −21.5pp EV)** that
  was *"the mechanism, not the market."*

Here the mechanism would be worse than either: a **large, entirely mechanical** price drop
against an **unchanged 12-ship NAV of $9.62**, on a name currently reading **BUY at +52.5%
EV**. The likely outputs are a **spurious EV spike**, a possible **±30% static-guard trip**
(the watchlist static is $6.32), and a **drift-gate red** that will present as an
unexplained move. `POSITION_UNRELIABLE` is already set on BRUT, which helps, but the gate
and the guard do not read that flag.

**What I think this means.** The correct order of operations is **manifest-and-sheet first,
price second** — the reverse of what will happen by default if the cron simply recovers.
The repo's own doctrine covers this: *"Gate expectations scale by determinant LEG"* — a
demerger is a **fleet+balance-sheet+price JOINT** event, so a price-only absorb predicts
the wrong thing. Per `CLAUDE.md`, **revert `prices_daily.yaml` before any promote/ingest
regen** so the price vintage is not laundered into the demerger sourcing event.

**What I am NOT sure of.** Whether the network stand-down is a machine/DNS condition that
will clear on its own or needs intervention — the EDGAR lane recovered by itself at
~21:00Z today after ~100 skips, which suggests it may, but `price_refresh`'s next
scheduled attempt is ~02:00Z and I have no way to confirm it will succeed. **I took no
action on any of this** — no fetch, no revert, no edit. Review-only.

---

### M3 · 2343 — the 8/21 **Interim Report** publishes **per-class fleet values**, retiring a deferral the watchlist pinned to **March 2027**.

**What happened.** `inputs/filings/2343/12293993_2026082100526.pdf` (HKEXnews, filed
**2026-08-21**, staged locally today) is Pacific Basin's full **Interim Report 2026**. It
contains a **per-class composite-broker fleet valuation table** at **30-Jun-2026**:

| Class | Vessels | Est. market value (US$M) | Net book value (US$M) |
|---|---|---|---|
| Handysize | 58 | 952.6 | 747.4 |
| Supramax/Ultramax | 48 | 1,100.0 | 795.7 |
| Capesize (bareboat-out) | 1 | 18.0 | 13.9 |
| **Total** | **107** | **2,070.6** | **1,557.0** |

Footnoted *"based on latest composite broker valuation estimates"*; the table **excludes
6 Handysize and 4 Ultramax newbuildings on order**.

**Why this matters.** `inputs/watchlist.yaml`'s 2343 block states the NAV was re-derived
at the 8/06 interim results and adds: *"NOTE the Interim gives a **SINGLE AGGREGATE**;
AR2025 gave per-class values, so **a future per-class refinement needs AR2026
(~Mar-2027)** — which is also the next re-derivation venue."* **That is now wrong.** The
per-class split arrived in the **Interim Report** on 8/21, seven months early. The
**aggregate is unchanged at 2,070.6**, so the existing `consensus_pnav: 0.91` derivation
still reproduces exactly — **this adds resolution without moving the anchor**, which is
the safest possible form of a refinement.

**Also in the same document, and NOT in the 8/06 results announcement's scope:**
- **Newbuild programme reshaped and expanded.** *"replacing four dual-fuel Ultramax orders
  with four fuel-efficient conventionally fuelled Ultramax newbuildings, while also
  securing a new option to acquire two dual-fuel vessels"*; and Handysize orders with JNS
  **increased from four to six**, 40,000 dwt open-hatch logs-fitted, **delivering 2028**.
- **Buyback:** **~9.5 million shares repurchased in H1-2026 for ~US$3.5 million**, under a
  programme of **up to US$40 million for 2026**. This moves the **NAV/share denominator**.
- **Interim dividend HK15.5 cents/share**, ~100% of net profit ex-disposal gains, **record
  date 2026-08-24 (today)**, payable **2026-09-03**. Net cash **US$157.2 million**.

**Source.** Locally staged HKEX PDF above (primary). The two companion 8/21 filings
(`hkex-12294027`, `hkex-12294023`) are **shareholder notification letters about the
publication of the Interim Report — administrative, no model content**; I read both to
confirm that rather than assuming it.

**Is it UNREAD?** `decisions/2343_log.md`'s head is the 8/16 auto-run; **no annotation of
the 8/21 Interim Report.**

**What I am NOT sure of.** The manifest header already says *"NB programme RESHAPED at the
Interim"*, so **some** of the newbuild change was captured at the 8/06 pass — I could not
determine from the manifest comment alone whether the **JNS four→six increase** and the
**two dual-fuel option** were part of it. Worth a diff against the 8/06 announcement
before treating the NB lines as new. The per-class table, by contrast, is unambiguously
new — the watchlist comment says in its own words that 8/06 gave a single aggregate.

---

### M4 · GNK — Genco's **8/17 open letter** puts **forward dividend guidance** on the record. The log is still un-annotated for the whole Diana sequence.

**What happened.** **2026-08-17**, *"Genco Shipping & Trading Limited Issues Open Letter to
Shareholders Following Withdrawal by Diana Shipping Inc. of its Offer"*. Content:
- **Q2 2026 declared: $0.80/share** (already known to the repo — `gnk_log.md` line 259).
- **NEW: Q3+Q4 2026 cumulative dividends projected at "more than $2.00 per share"**, with
  **Q3 alone projected above $1.00/share — an increase of more than 560% year-over-year.**
- **NAV stated at ~$27.50/share**, *"based on independent broker valuations and sell-side
  analyst median estimates."*
- Cumulative **$8.715/share across 28 consecutive quarterly payments** since 2021.
- Genco's counter-framework to Diana was **$27.50 cash + three Diana shares**, dividends
  retained through closing; Genco says Diana *"misleadingly inflated"* that to $36.91.

**Source.** GlobeNewswire release 3345811 — **the primary timed out twice** (60s), so the
text above is from the **manilatimes GlobeNewswire mirror**
(`manilatimes.net/2026/08/17/tmt-newswire/globenewswire/…/2406509`). **Syndicator-sourced;
verify at the issuer before promoting any figure.**

**Model surfaces.**
- **`inputs/dividend_policies/gnk.yaml`** — the file's sourcing comment is anchored to the
  **Q1 2026 10-Q (filed 2026-05-06)** and its newest figure is **$0.35/share**. It encodes
  `policy_type: variable`, `payout_ratio: 1.00`, no base, no floor. **The structural form
  is probably still right** — a formulaic ~100%-of-cash-flow policy should *produce* a
  rising dividend in a strengthening market without any parameter change. **But the
  forward strip is half of what this tool values**, and a guided **>560% YoY** step is a
  strong test of whether `payout_ratio: 1.00` reproduces the issuer's own projection.
  That is a cross-check worth running, not necessarily an edit.
- **`analyst_target: 28.40`** — the watchlist deliberately carries **Pareto's NAV $28.4**,
  not a price target. Genco's own **$27.50** NAV claim now sits **1.9x closer** to that
  than Diana's deal price ever did. A useful independent corroboration of the anchor.
- **The GNK watchlist comment is still false as written.** It says *"A NON-BINDING
  INDICATIVE PROPOSAL REMAINS LIVE"* and registers a re-check for *"either outcome (deal
  agreed / Diana walks)"*. **Diana walked on 2026-08-14.** The prior digest flagged this;
  it is **still unfixed**, now ten days on.

**Is it UNREAD?** **Yes, doubly.** `decisions/gnk_log.md`'s head is the `2026-08-16` auto-run
with `**Decision:** _[pending annotation]_`. The newest Diana text in the file is the
**pre-withdrawal** tender/proposal block (lines 224–232, still describing the proposal as
continuing). **Neither the 8/14 withdrawal nor the 8/17 letter is annotated.**

**Also note:** **2026-08-24 — today — was the response date Genco's board had set.** I
found no release from either side dated 8/18–8/24 beyond the 8/17 letter. Diana remains
Genco's largest shareholder and said it will *"continue to monitor."*

**What I am NOT sure of.** Whether the >$1.00 Q3 figure is a formal guidance number or
advocacy framing inside a contested-M&A letter. It appears in a document written to
persuade shareholders that rejecting Diana was right, which is a reason for caution about
the **>560%** framing specifically. Treat the dividend figures as **LEAD-QUALITY pending
the issuer primary or the Q3 declaration.**

---

### M5 · ECO — insider selling by a board-member-associated fund, disclosed 8/17.

**What happened.** 6-K `0001104659-26-097930` (filed 2026-08-17, staged locally),
*"Okeanis Eco Tankers Corp. — Mandatory notification of trade"*: a fund managed by **QVT
Financial LP**, *"legal person closely associated with primary insider and Member of the
Board of Directors, Daniel Gold"*, sold:
- **2026-08-13: 8,539 shares @ USD 65.04**
- **2026-08-14: 68,420 shares @ USD 59.99**

QVT retains **1,347,038 shares**. The release also restates the sailing fleet as **six
scrubber-fitted Suezmaxes and eight scrubber-fitted VLCCs**.

**Model surface.** **None directly** — and I want to be explicit about one thing it must
**not** touch: **those two prices are transaction prints in filing prose, and per
`CLAUDE.md` they must never be typed into `current_price`.** They are recorded here only
as a governance/sentiment datapoint. The fleet restatement (6 Suezmax + 8 VLCC) is a free
cross-check against `inputs/fleet_manifests/eco.yaml`.

**What I am NOT sure of.** The one-day move from $65.04 to $59.99 (−7.8%) across the two
sale dates is notable, but I have no committed prices after 08-19 to corroborate a trend
(M2), so I am not reading anything into it.

---

### M6 · FLNG — **Q2 2026 results landed 8/19; the repo has no Q2 balance sheet for the name.**

**What happened.** 6-K `0001628280-26-057820` + `…-057822` (filed 2026-08-19, staged
locally). Q2 2026: **vessel operating revenues $106.8M** (Q1: $80.5M), **net income
$44.9M**, **EPS $0.83**, **cash $397.4M**, **vessels & equipment net $2,077.1M**,
**long-term debt $1,793.7M**, **TCE rate $86,119/day** (Q1: $65,729), **adjusted EBITDA
$79.0M**. **Dividend declared $0.75/share for Q2.** Revenue and TCE both *"the highest
since the fourth quarter 2021."*

**Model surface.** `inputs/balance_sheets/` contains **`flng_2026-Q1.yaml` and no
`flng_2026-Q2.yaml`.** Of the names still lacking a Q2 sheet (BWLP, CAPT, CMBT, FRO, HAFN,
MPCC, NAT, TEN, TRMD), **FLNG is the only one that has actually reported** — the others
are all still ahead of their dates. So FLNG is the one clean, unblocked Q2 refresh
available right now, with a full balance sheet in the staged filing.

**What I am NOT sure of.** Whether a Q2 refresh for FLNG is wanted ahead of the broader
Q2 cluster transition — that is a sequencing call, not a data question. Flagging
availability only.

---

## PROMOTABLE CANDIDATES

*Candidates only. Promotion is human-only; I have promoted nothing.*

- **P1 · 2343 per-class fleet market values (30-Jun-2026)** — **strongest candidate this
  window.** Handysize **58 / $952.6M**, Supramax-Ultramax **48 / $1,100.0M**, Capesize
  **1 / $18.0M**, total **107 / $2,070.6M**; net book $1,557.0M. Composite broker basis,
  issuer-published, **same 30-Jun vintage as the landed 2026-Q2 sheet**. Aggregate is
  **unchanged**, so this is a resolution upgrade that cannot move the anchor. Source:
  staged `inputs/filings/2343/12293993_2026082100526.pdf`. **Retires the watchlist's
  "needs AR2026 (~Mar-2027)" note.**
- **P2 · BRUT/OMC commitment split (2026-08-20)** — NTS four: **$472M total / $47.2M
  paid**; CIMC four: **$499M total / $49.9M paid**; **$50M cash**; ~$82k trade payables;
  no other indebtedness transferred. Issuer-primary, exact figures. **Not a vessel print**
  — it carries no per-vessel price or delivered-market mark, so it feeds the
  manifest/balance-sheet demerger decision, **not** `vlcc.yaml`.
- **P3 · FRO — 2 × VLCC (2017-built), $135.0m each / $270m aggregate, 2026-08-04 —
  CARRIED OVER, STILL OPEN, and its promotion channel is the thing that's missing.**
  `decisions/fro_log.md` (line ~203) registers the OPEN PRINT FLAG: *"promote only when a
  per-vessel price lands (**MB W33/W34** or the FRO Q2 report)."* **MB W33 and W34 are
  both absent locally** (archive-gaps section above) — so the flag could not clear this
  week for a structural reason, not because nothing happened. **Vessel names remain
  unconfirmed.** FRO reports **Q2 on 2026-08-31**, which is the other named venue.
- **No new S&P prints carrying vessel + class + built-year + price** were found for
  watchlist names in this window. **This is a weak negative, not a clean one** — the MB
  lane that carries these is 17 days silent, and the week-33/34 broker reports surfaced in
  search (`hellenicshippingnews` W33 8/17, `compassmar` 8/17) are **403/PDF and were not
  read**. Search-summary figures seen but **NOT promotable, LEAD-QUALITY only**: August
  averages VLCC ~$131.5m / Suezmax ~$93.0m / Aframax ~$78.0m; dry-bulk print
  *"PRINCESS ETERNITY 182K/2022 JMU — USD 78m"* (not a watchlist name).

---

## WATCH

- **BRUT §15 going-concern screen expires this week.** The H1 screen's stated basis —
  eight unfinanced hulls, demerger conditional on a listing *"that has not occurred"* — is
  overtaken by the 28 Aug admission. `governance_discount_pct` stays 0 by the 7/01
  survival-binary doctrine, but **the screen's reasoning needs re-writing, not just
  re-running.**
- **BRUT tier call.** `decisions/brut_log.md` reserved PROVISIONAL to the owner, with the
  remaining binding reason *"going-concern §15 + max-torque."* Post-demerger the entity is
  4 hulls with ~$496M commitment instead of 12 with ~$1,370M — **materially less torque.**
- **GNK dividend guidance vs `dividend_policies/gnk.yaml`** (M4) — cross-check that
  `payout_ratio: 1.00` reproduces the guided Q3/Q4 path.
- **GNK watchlist comment is factually stale** — *"A NON-BINDING INDICATIVE PROPOSAL
  REMAINS LIVE"*. Diana withdrew 8/14. Flagged in the last digest, still open.
- **2343 share count is moving** — 9.5M shares bought back in H1 for ~$3.5M against a
  $40M-for-2026 programme. NAV/share denominator drift; the `consensus_pnav: 0.91`
  derivation is a price/NAV-per-share ratio and should be recomputed, never edited alone.
- **Board changes, no NAV impact, recorded for completeness:**
  **STNG** — Marianne Økland resigned effective 8/15; **Andrea Lupo Lanzara** appointed
  Class III director effective 8/17 (6-K `0001628280-26-057375`). Explicitly *"not the
  result of any disagreement."*
  **TRMD** — **Jann Brown** appointed to the board effective **1 Oct 2026**; **Annette
  Malm Justad** promoted to Senior Independent Director (6-K `0000919574-26-005684`,
  filed **8/24**, the newest filing in the window).
- **CMDB** — 6-K `0001171843-26-005609` (8/18) carries the **unaudited interim condensed
  consolidated financials for the six months ended 30-Jun-2026**. `cmdb_2026-Q2.yaml`
  already exists (built at the 8/14 6-K). **Worth confirming the sheet was built from the
  full statements and not only the 8/14 release** — CMDB is an APPROX name whose
  `consensus_pnav` is a **P/BV proxy**, so its book value per share *is* the anchor.
- **Reporting inside the next week** (from `inputs/earnings_calendar.yaml` + today's
  sentinel): **NAT 8/26–8/31 (expected, still no issuer date-PR)** · **TRMD 8/26
  (confirmed)** · **MPCC 8/26 (confirmed; earnings-call invite issued 8/19)** ·
  **CMBT 8/27 (confirmed)** · **FLNG 8/28 → already reported early, 8/19** ·
  **HAFN 8/28 (confirmed; presentation notice issued 8/21)** · **BWLP 8/28 (confirmed;
  notice issued 8/14)** · **CAPT 9/01 (confirmed)** · **FRO 8/31 (confirmed)**.
  The sentinel also flags **`EARNINGS-SWEEP-STALE`** — `meta.last_date_sweep` is
  2026-08-09, >7d, with windows opening inside 21d.
- **CMBT *Bristol*** — 2024-built Suezmax sale, **~$57m gain, no price disclosed**
  (8/11, pre-window; `cmbt_log.md` line 204). **Still not promotable** — a gain without a
  price is not a print. Q2 on **8/27** is the venue where a price may appear.

---

## NO-ACTION — one line per name swept clean

Coverage basis abbreviations: **[F]** = issuer feed read as primary (mfn.se / nat.bm /
HKEXnews); **[M]** = local EDGAR/newsweb/HKEX manifest + poller, `polled 22 names: 0 new`
at 20:20Z today; **[S]** = targeted web search over the window.

- **DHT** — [M][S] no filing, no release, no S&P print found 08-16→08-24. Nothing found.
- **INSW** — [M][S] no filing or release in window. Nothing found.
- **TNK** — [M][S] no filing or release in window. Nothing found.
- **NAT** — **[F]** `nat.bm` read directly: newest press release is **2026-07-23**
  (*"An optimistic summer message from NAT"*). **Primary-sourced silent** for the whole
  window. Reports 8/26–8/31. *(Note: `nat.bm/press-releases/` 404s — use the site root.)*
- **CCEC** — [M][S] nothing dated in window; newest items found are June deliveries.
- **ASC** — [M][S] no filing or release in window. Nothing found.
- **TEN** — [M][S] no filing or release in window. Nothing found.
- **SBLK** — [M][S] no filing or release in window. *(Diana's plan to sell 16 Genco
  vessels to Star Bulk appears in Genco's contested-M&A commentary; with Diana's offer
  withdrawn it is moot, and it was never an SBLK disclosure.)*
- **GSL** — [M][S] no filing or release in window. Nothing found.
- **SB** — [M][S] no filing or release in window. Nothing found.
- **LPG** — [M][S] no filing or release in window. Nothing found.
- **CAPT** — **[F]** `mfn.se/all/a/capital-tankers.json` read directly: newest release is
  **2026-08-13** (M/T *Aristodimos* delivery, already actioned last digest). **The issuer
  feed shows nothing after 08-13** — a primary-sourced negative, not an inferred one.
  Half-yearly report **2026-09-01**.
- **BWLP** — **[F]** `mfn.se/all/a/bw-lpg.json`: newest release **2026-08-14**, the Q2
  results-date notice (28 Aug). Nothing in window. Feed appears twinned (`ob` + `mfn`
  copies of the same item — counted once).
- **MPCC** — **[F]** `mfn.se/all/a/mpc-container-ships.json`: single in-window item, the
  **8/19 Q2 earnings-call invitation** (report **8/26**). Administrative; no model surface.
  Confirmed against the staged body `inputs/filings/MPCC/newsweb_2026-08-19_…txt`.
- **ECO / STNG / TRMD / CMDB / FLNG / HAFN** — filings found and read; see M5, M6 and WATCH.
  No *further* undisclosed items in window.
- **CMBT** — [M][S] nothing dated 08-16→08-24; the 8/03 fleet update and 8/11 *Bristol*
  sale are pre-window and already logged. Q2 **8/27**.
- **FRO** — [M][S] nothing new in window; the open 8/04 P1 is carried, unchanged (P3).

**Caveat binding every line above:** the Pareto lane is missing **08-19..08-21 (+08-14,
08-24)** and the MB S&P lane is missing **W33–W34**. Items that would have reached me
*only* through those two channels — chiefly **broker stance/target changes and
broker-reported S&P prints** — are **unsupported, not absent.**

---

## OWNER SUMMARY — ranked

1. **BRUT: decide the demerger carry BEFORE the ex-date price lands (M1 + M2).** Ex-date
   is **tomorrow, 25 Aug**; distribution 27 Aug; OMC lists 28 Aug. Eight of twelve hulls,
   **~$873.9M of remaining commitment and $50M of cash leave the company.** The price feed
   is seven days dead, so the ex-date drop will arrive as a **single unexplained price
   step** against a manifest that still says twelve. Order of operations matters:
   **manifest + balance sheet first, price second**, and per `CLAUDE.md` revert
   `prices_daily.yaml` before any promote/ingest regen. This is the one item with a
   deadline you cannot move.
2. **Annotate `decisions/gnk_log.md` — it is three events behind.** The 8/14 Diana
   withdrawal, the 8/17 open letter, and today's lapsed 8/24 response date are all
   unrecorded, and the **watchlist comment still asserts the proposal "REMAINS LIVE."**
   That sentence has been false for ten days and was flagged in the last digest.
3. **Adjudicate the Pareto archive gap 08-19..08-21** (three consecutive business days,
   at `limit_business_days`). Backfill or accept with channel-side evidence per
   `archive_gaps.yaml`'s own standard — **do not let it age out silently**, which is the
   exact failure mode that file exists to prevent. Same question for **MB W33/W34**, which
   is separately blocking the FRO P1 print.
4. **Promote the 2343 per-class fleet values (P1)** — free resolution at an unchanged
   aggregate, and it **retires a deferral the watchlist had pinned to March 2027.** While
   there, correct that comment and note the H1 buyback's effect on the share count.
5. **Investigate the `price_refresh` DNS stand-down (7 consecutive days).** The EDGAR /
   newsweb / HKEX lanes self-recovered at ~21:00Z today after ~100 skips; the price lane
   has not. Every downstream valuation is running on an **08-18/08-19 price vintage**.
6. **FLNG Q2 refresh is unblocked** (M6) — reported 8/19, full balance sheet staged, and
   it is the only Q2-reported name without a Q2 sheet.
7. **Housekeeping:** run the earnings date sweep (`EARNINGS-SWEEP-STALE`, last swept
   08-09) — **NAT's window opens in 2 days with no issuer date on file.**
