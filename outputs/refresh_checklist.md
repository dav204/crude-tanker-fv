# Refresh Checklist — 2026-Q2 (target quarter)

- **Today:** 2026-08-13
- **Target quarter:** 2026-Q2
- **Workflow:** work through the sections below, then run `python -m crude_tanker_fv.pipeline` to refresh outputs.

## Status summary

- ⚠ **Balance sheets:** 14 of 25 present for 2026-Q2 — missing: FRO, NAT, FLNG, HAFN, TRMD, TEN, CAPT, MPCC, BRUT, CMBT, BWLP
- ✓ **Market data:** 5 of 5 fresh (< 30 days)
- ⚠ **Watchlist:** 14 of 25 clean — 0 stale, 11 APPROX consensus_pnav
- ⚠ **Earnings:** REFRESH DUE: BRUT — upcoming/check: NAT, TRMD, MPCC, CMBT
- ✓ **§13.3 reweight triggers:** none due — upcoming: crude_day60_toll_cliff

## 0a. Scenario-weight re-evaluation triggers (`inputs/reweight_triggers.yaml`)

| Trigger | Status | Detail |
|---|---|---|
| crude_day60_toll_cliff | 🟡 | [crude+product] due in 3d (2026-08-16). Islamabad Memorandum toll-free window expires (~Jun-17 + 60d; the released text makes Hormuz toll-free for 60 days only — Iran asserts a fee |
| all_sectors_consensus_pair_recapture | — | [all] due 2026-10-02. Watchlist consensus vintages (as_of) are 23-72d old (BRUT worst) vs the 14d freshness threshold — the pure sentinel + the Action issue carry |
| all_sectors_quarterly_staleness_floor | — | [all] due 2026-10-02. Any sector's locked weight set older than one quarter (roll this due forward to decision-date + 1 quarter on every reweight). Backstop, not  |
| container_mb_refresh | — | [containerships] due 2026-09-07. Monthly re-capture of the container determinants (Ctr-* TC + value assessments) from the newest staged MB Container Weekly — the §11.8 sourc |
| crude_brent_reopening | — | [crude] standing event-watch. Standing event-watch: Brent sustained above pre-war ($72.48, Feb-27-2026 reference) + $10/bbl — macro confirmation the stand-down is failing |
| crude_ceasefire_mediation_watch | — | [crude] done |
| crude_doha_round2_outcome | — | [crude] done |
| crude_doha_round3_watch | — | [crude] done |
| crude_doha_talks_resumption | — | [crude] done |
| crude_mou_implementation_check | — | [crude] done |
| crude_pause_talks_watch | — | [crude] done |
| crude_transit_normalization | — | [crude] standing event-watch. Standing event-watch: mine-clearance confirmation / UKMTO-JMIC advisories lifted / war-risk insurance premia normalize. Premia level current |
| drybulk_spot_daily_resumes | — | [dry_bulk] done |
| handy_bulk_txn_refit | — | [dry_bulk] standing event-watch. Standing event-watch (§11.7.11 Option B, owner-ratified 2026-07-14): the dry-Handysize classified print sample reaches >=10 human-classified |
| lpg_anchor_annual_review | — | [lpg] due 2027-06-30. The VLGC 10-yr through-cycle TCE anchor (~$40,000/day, as_of 2026-07-07, WO3 decisions/lpg_methodology_2026-07-07.md) is a TRAILING 10-yr av |
| lpg_v1_lock_rerun | — | [lpg] due 2026-11-13. Dorian trio per-vessel sale splits (Corsair 2014 + two unnamed 2015-built VLGCs, $256M en bloc agreed Jun-23-2026, deliveries "by" Q4-2026). |
| ppmx_txn_refit | — | [dry_bulk] standing event-watch. Standing event-watch (PPMX §9.9 seed, owner-ruled 2026-07-18): the Post-Panamax classified print sample reaches >=8 in-window prints includi |
| product_glut_arrival_timing | — | [product] due 2026-10-02. The product family's central live uncertainty (reviewer rider 1): does the clean-tonnage glut arrive on the 2027 schedule the glut_base leg  |
| tanker_forward_print_lands | — | [crude+product] standing event-watch. Standing event-watch (reviewer condition, 2026-07-02; RE-ARMED to original text at Stage A per prereg §8.4): any tanker FFA or 1-year T/C fo |
| vlgc_realized_tce_refresh | — | [lpg] standing event-watch. Standing event-watch (WO3 Phase 3, 2026-07-09): any new VLGC realized-TCE disclosure (Dorian / BW LPG quarterly reports — next cluster ~Aug- |

## 0. Earnings calendar (report-day refresh runbook in CLAUDE.md)

| Ticker | Status | Detail |
|---|---|---|
| BRUT | 🔴 DUE | report window open (2026-08-13, confirmed) and no 2026-Q2 balance sheet on file — refresh due. RE-VERIFIED 2026-07-21 via the Euronext company-information calendar (exchange-published): Half-yearly Report 13/08/2026; AGM 12/08/2026. No timing stated. (Issuer legal name Bruton Limited.) Original NewsWeb filing not retrievable — calendar-grade source. |
| CMBT | 🟡 | reports in 14d (2026-08-27, confirmed). CMB.TECH PR (GlobeNewswire 2026-06-29): Q2-2026 announcement Aug-27; SEEDED 2026-07-03 (was absent from the Jun-11 sweep) |
| MPCC | 🟡 | reports in 13d (2026-08-26, confirmed). MFN financial calendar announcement (2025-12-30): half-yearly/Q2 report 26.08.2026 |
| NAT | 🟡 | reports in 13d (2026-08-26 → 2026-08-31, expected). SWEPT 2026-08-09: aggregators (MarketBeat et al.) point ~Aug-31; NO issuer date-PR yet (NAT pattern: terse GlobeNewswire report-day releases, thin advance notice). Window held 8/26-8/31, aggregator grade. |
| TRMD | 🟡 | reports in 13d (2026-08-26, confirmed). TORM 'Financial Calendar 2026' announcement (2025-12-19): Q2 Aug-26; adherence validated on Q1 (May-13 = actual) |
| 2343 | — | 2026-08-06 (confirmed). Aug-6 now FORMALLY confirmed: HKEX board-meeting notice filed 2026-07-24 (hkex-12255247, staged inputs/filings/2343/12255247_2026072400392.pdf) — Board meets 6 Aug 2026 to approve H1-2026 interims + consider interim dividend. Supersedes the IR-calendar-only basis. |
| ASC | — | 2026-07-29 (confirmed). CONFIRMED 2026-07-28 sweep: issuer PR 'Ardmore Shipping Announces Second Quarter 2026 Conference Call' (StockTitan/PRNewswire) — Q2 results PRE-MARKET Wed Jul-29, call 10:00 ET same day, replay to Aug-5. Was expected/no-PR at the 7/22 sweep. |
| BWLP | — | 2026-08-28 (confirmed). Q2-2026 date CONFIRMED by the issuer: 6-K 0001213900-26-078478 ex-99.1 (7/16 Product Services pre-announcement) states 'the BW LPG Q2 2026 results ... will be released on 28 August 2026'. (Was cadence-derived 8/25-8/28, seeded 2026-07-10.) |
| CAPT | — | 2026-09-01 (confirmed). Oslo Bors Newspoint financial calendar (published 2026-03-12): HALF-YEARLY report Sep-1-2026 — the Jun-11 sweep missed this calendar; replaces the expected Aug-17..31 window |
| CCEC | — | 2026-07-29 (confirmed). CONFIRMED 2026-07-22 by the issuer's date-setting announcement PR (GlobeNewswire 2026-07-22, Athens), landed exactly on the predicted ~Jul-22-24 pattern: 'Capital Clean Energy Carriers Corp. Schedules Second Quarter 2026 Earnings Release, Conference Call and Webcast' — Q2 results BEFORE the Nasdaq open Wed Jul-29; interactive call same day 9:00 a.m. ET. ALSO the governance CCEC t2 print-gate venue (window 7/29-8/06 in the gov prereg; the print lands at its OPEN). |
| CMDB | — | 2026-08-03 (confirmed). RESULTS ANNOUNCED 2026-08-03 (Q2 6-K acc 0001171843-26-005131 - landed at the WIDENED-START edge as the window note anticipated) - refreshed at the 8/9 drain close. |
| DHT | — | 2026-08-05 (confirmed). CONFIRMED 2026-07-28 sweep: GlobeNewswire 2026-07-22 + dhtankers.com — Q2 results AFTER CLOSE Wed Aug-5, call Thu Aug-6 8:00 ET. Landed on the ~2wk-ahead date-PR pattern. |
| ECO | — | 2026-08-04 (confirmed). RE-VERIFIED 2026-07-21 unchanged: official financial calendar (GlobeNewswire 2025-12-19 + okeanisecotankers.com): '04.08.2026 - Half-yearly Report', all releases AFTER NYSE close. Q2 webcast invitation expected ~end-July (Q1 pattern ~5d ahead). |
| FLNG | — | 2026-08-28 (confirmed). RE-VERIFIED 2026-07-21: flexlng.com calendar still '28.08.2026 - Half-yearly Report 2026'; no updated/earlier date announced (press feed ends 5/13 Q1). EARLY-RELEASE RISK stands (2025 came ~1wk early) — re-check mid-Aug for the earnings-release notice. |
| FRO | — | 2026-08-31 (confirmed). frontlineplc.cy/calendar (announced 2026-05-22): Q2-2026 report Aug-31; narrowed from the expected Aug-26..31 window |
| GNK | — | 2026-08-05 (confirmed). OFFICIAL PR 2026-07-14 (GlobeNewswire 3327275): Q2 results AFTER CLOSE Wed Aug-5; call Thu Aug-6 8:30 ET. Swept 2026-07-21. |
| GSL | — | 2026-08-05 (confirmed). RESULTS ANNOUNCED 2026-08-05 (earnings-release 6-K) + H1 interim 8/6 (acc 0001140361-26-031697) - refreshed at the 8/8 drain; the short-notice pattern note stands for Q3. |
| HAFN | — | 2026-08-28 (confirmed). Hafnia Financial Calendar 2025-2027 (IR PDF): Q2-26 Aug-28; calendar adherence validated on the Q1-26 slot (May-27 = actual) |
| INSW | — | 2026-08-10 (confirmed). CONFIRMED 2026-08-09 sweep: official Business Wire date-PR 2026-07-24 - Q2 results BEFORE market open Monday Aug-10, call 9:00 ET. Supersedes the aggregator 8/4-8/7 window. |
| LPG | — | 2026-08-05 (confirmed). RESULTS ANNOUNCED 2026-08-05 (FQ1-2027 10-Q acc 0001596993-26-000035 + earnings-release 8-K) - refreshed at the 8/8 drain; entry historical until the Q3 re-seed. |
| SB | — | 2026-07-28 (confirmed). CONFIRMED 2026-07-28 sweep: sets-date PR GlobeNewswire 2026-07-22 'Safe Bulkers, Inc. Sets Date for the Second Quarter 2026 Results' — results AFTER CLOSE Tue Jul-28 (TONIGHT), call Wed Jul-29 10:30 ET. The 7/22 sweep just missed it (PR landed same day, later). No August slip. |
| SBLK | — | 2026-08-05 (confirmed). RESULTS ANNOUNCED 2026-08-05 (earnings-release 6-K acc 0000950157-26-000846) + interim 6-K 8/7 - refreshed at the 8/8 drain; entry historical until the Q3 re-seed. |
| STNG | — | 2026-07-30 (confirmed). OFFICIAL PR 2026-07-20 (scorpiotankers.com/GlobeNewswire): Q2 results IN THE MORNING (pre-market) Thu Jul-30; call same day 8:00 ET. Swept 2026-07-21. |
| TEN | — | 2026-09-08 → 2026-09-17 (expected). SWEPT 2026-08-09: no date-PR yet - consistent with the ~2wk-ahead pattern for a September H1 reporter; re-sweep ~late Aug. (H1 reporter - Q2 lands in SEPTEMBER; the standing cadence quirk.) |
| TNK | — | 2026-07-29 (confirmed). OFFICIAL joint Teekay Group PR 2026-07-14 (GlobeNewswire 3327260): Q2 results AFTER CLOSE Wed Jul-29; call Thu Jul-30 11:00 ET. Swept 2026-07-21. |

## 1. Missing quarterly balance sheets

For each missing name below, pull the 2026-Q2 results from the listed IR URLs and populate `inputs/balance_sheets/{ticker}_2026-Q2.yaml`:

### FRO
- **Press releases:** https://www.frontline.bm/news/
- **SEC EDGAR filings:** https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000913290&type=6-K
- **Fleet page:** https://www.frontline.bm/fleet-list/
- **Reporting pattern:** Q-end results typically late second month of following quarter (Q1 ≈ late May; Q4 ≈ late Feb)
- **Notes:** Cyprus-domiciled FPI dual-listed Oslo + NYSE. Press release posted simultaneously to both exchanges; SEC 6-K is the authoritative archive. Watch for material newbuild contracts disclosed between quarters.

### NAT
- **Press releases:** https://www.nat.bm/news/
- **SEC EDGAR filings:** https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001000177&type=6-K
- **Fleet page:** https://www.nat.bm/fleet/
- **Reporting pattern:** Q-end results typically mid-second month of following quarter (Q1 ≈ mid-May)
- **Notes:** Bermuda-domiciled FPI; small-cap so analyst coverage is thin — Pareto / Cleaves are the consensus_pnav anchors. Watch for vessel sales/purchases (active fleet turnover).

### FLNG
- **Press releases:** https://www.flexlng.com/press-releases/
- **SEC EDGAR filings:** https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001772253&type=6-K
- **Fleet page:** https://www.flexlng.com/our-fleet/
- **Reporting pattern:** Q-end results typically mid-second month of following quarter (Q1 ≈ mid-May; Q1 2026 was 2026-05-13)
- **Notes:** Bermuda-domiciled FPI dual-listed NYSE + Oslo. TC backlog table on the IR site is the source for charter coverage refresh (separate from fleet table).

### HAFN
- **Press releases:** https://www.hafniabw.com/investors/announcements/
- **SEC EDGAR filings:** https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001815779&type=6-K
- **Fleet page:** https://www.hafniabw.com/our-fleet/
- **Reporting pattern:** Q-end results typically late second month of following quarter (Q1 2026 was 2026-05-27); Oslo Bors filing same day
- **Notes:** Bermuda-incorporated, Singapore-headquartered, IFRS reporter. Dual-listed
NYSE (HAFN) + Oslo (HAFNI via Norwegian deposit receipts). Files 6-K via
SEC. BW Group owns 44.18% (controlling-but-not-majority); free float ~55%.
Q1 2026 detailed interim PDF (s201.q4cdn.com/891122012/files/doc_financials/
2026/q1/Hafnia-Limited-Q1-2026-Investor-Presentation-vF2.pdf) contains
per-vessel scrubber/eco flags, granular G&A breakdown, itemized disposal
prices, and exact diluted share count — pull from PDF each quarter.
Watch items: Handysize segment WIND-DOWN (22 hulls + 4 in pending sale);
8 firm MR newbuilds at Hyundai (2028-2029 delivery); large TORM equity
stake ($395M) generates dividend income but isn't reflected in our schema
via dedicated line; Hafnia operates the world's largest product tanker
POOL — "spot" earnings are pool-derived (net of pool admin fees);
BW Group ownership dynamics affect free float and consensus P/NAV reads.


### TRMD
- **Press releases:** https://www.torm.com/investors/announcements/
- **SEC EDGAR filings:** https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001655891&type=6-K
- **Fleet page:** https://www.torm.com/our-fleet/
- **Reporting pattern:** Q-end results typically early-mid second month of following quarter (Q1 2026 was 2026-05-08; Q4 results released in March with FY outlook)
- **Notes:** UK-incorporated, dual-listed Nasdaq Copenhagen (TRMD A) + Nasdaq New York (TRMD).
Files 6-K via SEC. UK tonnage tax regime (~1.5% effective rate).
Single Class A common share class; one controlling shareholder ~65%.
Q1 2026 interim report PDF (s202.q4cdn.com/126069760/files/doc_financials/...)
contains the per-vessel fleet detail, bank-vs-lease debt split, and held-for-sale
book values that the 6-K summary doesn't break out — refresh from PDF each quarter.
Watch items: SLB exposure (down to 2 vessels at Q1 2026 vs 16+ in 2024 peak),
NB resale program (currently 8 outstanding: 2 Q2 2026 + 6 2027-2028), dividend
payout ratio variability (58-82% of NI; quarterly Board discretion, not formula).


### TEN
- **Press releases:** https://www.tenn.gr/news-events/
- **SEC EDGAR filings:** https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001166663&type=6-K
- **Fleet page:** https://www.tenn.gr/fleet/
- **Reporting pattern:** Q-end results typically late second month of following quarter (Q1 2026 was 2026-05-22).
Monthly DATA KIT published mid-month with per-vessel TC rates and NB schedule —
refresh from data kit each month (independent of 6-K cadence).
Annual 20-F filed early April with full audited balance sheet detail.
AGM proxy 6-K (typically April) names directors and certifies preferred share counts.

- **Notes:** Bermuda-incorporated FPI; 3-sleeve hybrid (crude + product + lng) with the DP2
shuttle sleeve OFF-CURVE via shuttle_contracted_book (METHODOLOGY §11.6).
First name in THREE_SLEEVE_TICKERS.
Key per-quarter refresh items:
  - Data kit per-vessel TC rates (especially shuttle vessels Brasil 2014, Rio 2016,
    Athens 04, Paris 24 — drive shuttle_contracted_book NPV)
  - NB orderbook schedule + advances paid (19 vessels, $2,403M total contract)
  - Total debt roll-forward (data kit narrates Q1 movements; 6-K confirms)
  - Common dividend declaration (semi-annual, Board discretion)
Watch items:
  - DP2 shuttle extension events (Apr 2026 announced extension for Brasil/Rio
    @ "increased rate" through H2 2033 — current shuttle NPV uses $60k/day APPROX
    ext rate; refresh when actual rate disclosed)
  - 10-yr-old VLCC Ulysses sold May 2026 ($83M free cash) — already reflected in
    fleet manifest age
  - 2 Suezmax 2007-built repurchase Apr 2026 (Arctic, Antarctic from 5y bareboat)
  - Series E ($118.6M) + Series F ($168.7M) preferred — stable; rates fixed


### CAPT
- **Press releases:** https://www.capitaltankers.com/news/
- **Fleet page:** https://www.capitaltankers.com/fleet/
- **Reporting pattern:** Oslo H1/quarterly releases; first results May-27-2026. Pareto covers (initiation 2026-04-19, BUY TP NOK 180) — the dailies + linked reports are the richest running source.
- **Notes:** Capital Tankers (Marinakis ~75%), listed Oslo 2026-03-17, IPO at NOK 134. 30 firm vessels (21 NB through mid-28) + 13 options to YE'26. Onboarded 2026-06-11. IR URLs unverified-by-fetch at onboarding — verify on first issuer-report pull (Q2 refresh).

### MPCC
- **Fleet page:** https://www.mpc-container.com/fleet/our-fleet/
- **Reporting pattern:** Oslo quarterly via MFN; Q1-26 published 2026-05-27. Pareto covers (HOLD TP NOK 25, 2026-05-28 review on disk via linked-report harvest) on EV/EBITDA — publishes NO NAV (§11.8.2).
- **Notes:** Onboarded 2026-06-12 (1st container validator). Fleet-employment table in the earnings deck is the per-vessel source (rates + redelivery windows); built years NOT disclosed there — cohort age estimates pending the issuer fleet list. 17-ship NB program (2 in Uthalden JV, excluded).

### BRUT
- **Press releases:** https://bruton-ltd.com/news/
- **Fleet page:** https://bruton-ltd.com/fleet/
- **Reporting pattern:** HALF-YEARLY reporter — H1-2026 due 2026-08-13 (owner- confirmed); no Q1/Q3 interims. Pareto covers (initiation 2026-04-22, BUY TP NOK 66) — the dailies + the initiation are the running source until H1.
- **Notes:** Bruton Ltd — pure-play VLCC newbuild vehicle (Magni Partners / Tor Olav Trøim; Koch ~26% / Trøim ~20% / float ~54%), listed Oslo late-2024. 12 firm VLCC NB (8 NTS 300k + 4 CIMC Raffles 319k), 0 on the water, deliveries Jul-2026 → Q3-2029. Onboarded 2026-06-22 via the §9.6 time-to-delivery discount (raw delivered-less-commitment NAV was +116% vs Pareto; PV- discounting the NB deliveries lands it at +30.6%, SANITY OK).

### CMBT
- **Press releases:** https://cmb.tech/news
- **SEC EDGAR filings:** https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001604481&type=6-K
- **Fleet page:** https://cmb.tech/fleet
- **Reporting pattern:** NYSE/Euronext Brussels FPI (ex-Euronav). 20-F annual (FY2025 filed 2026-04-21, body eurn-20251231.htm) + 6-K quarterly results. Q1-2026 6-K filed 2026-05-19 (accession 0000919574-26-003591, Ex-99.1 d12164570_ex99-1.htm). The 20-F carries the full per-vessel fleet table (built years/yards) across all segments; the 6-K carries the segment counts + balance sheet.
- **Notes:** Onboarded 2026-06-26. First crude+dry_bulk+containerships MULTI_SLEEVE hybrid (METHODOLOGY §11.9). CIK 1604481 (legacy eurn- XBRL roots). Five-segment conglomerate post the 20-Aug-2025 Golden Ocean merger (+95.95M shares -> 290.17M ex-treasury); dry bulk ~72% of vessel value. Saverys/CMB NV control 56.56% economic / 61.59% voting (§15: declined haircut, tripwires — see decisions/cmbt_log.md). PARETO-ANCHORED — Pareto publishes a monthly CMB.TECH P/NAV + NAV/sh (11-Jun-2026: price $14.90, P/NAV 0.74x, NAV ~$20/sh, fwd P/E 9.7x). EDGAR fetch needs a contact UA (fetch_pdf.py patched 2026-06-26); chemical/offshore/FSO/HFS/newbuild book off-curve.

### BWLP
- **Press releases:** https://www.bwlpg.com/media/press-releases/
- **SEC EDGAR filings:** https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001649313&type=6-K
- **Fleet page:** https://www.bwlpg.com/fleet/
- **Reporting pattern:** NYSE FPI + Oslo primary (Bermuda inc., Singapore HQ) — 20-F annual (FY2025 filed 2026-03-31, acc 0001104659-26-037215) + quarterly 6-K interim reports (Q1-2026: acc 0001213900-26-064314, ex99-2 is the full IFRS interim report with the India/Product-Services sub-balance-sheets). Oslo announcements mirror to 6-Ks.
- **Notes:** Onboarded 2026-07-10 (WO3 Phase 4, 2nd LPG/VLGC validator). CIK 1649313. 39 economically-owned VLGCs (28 parent + 3 lease-financed [inside borrowings] + 8 via 52%-owned BW LPG India — 48% NCI deducted via preferred_equity, NAV-basis derivation in the balance-sheet YAML); chartered-in book excluded. Product Services (81%-owned trading arm) = WC-heavy, earnings outside the strip (conservative known limit). §15: BW Group (Sohmen) 31.99% bloc — screen run, N/A-gated at ~1.0x P/NAV, tripwires not haircut. Watch: 8x90cbm Panamax-VLGC NB (~$940M, signed 2026-05-30) enters §9.6 at the Q2 refresh; R-2 kill-switch (VLGC orderbook >38%) sensitivity.

## 2. Stale market data

_All market data files were updated within 30 days. ✓_

## 3. Watchlist freshness

| Ticker | as_of status | Detail |
|---|---|---|
| DHT | ✓ | as_of 2026-07-03 (41d ago) |
| ECO | ✓ | as_of 2026-07-03 (41d ago) |
| FRO | ✓ | as_of 2026-07-03 (41d ago) |
| INSW | ✓ | as_of 2026-07-03 (41d ago) |
| TNK | ✓ | as_of 2026-07-03 (41d ago) |
| NAT | ⚠ APPROX | as_of 2026-07-03 (41d ago); consensus_pnav flagged APPROX in comment — replace with Pareto / broker figure |
| FLNG | ✓ | as_of 2026-07-03 (41d ago) |
| CCEC | ⚠ APPROX | as_of 2026-07-03 (41d ago); consensus_pnav flagged APPROX in comment — replace with Pareto / broker figure |
| STNG | ⚠ APPROX | as_of 2026-07-03 (41d ago); consensus_pnav flagged APPROX in comment — replace with Pareto / broker figure |
| HAFN | ✓ | as_of 2026-07-03 (41d ago) |
| TRMD | ⚠ APPROX | as_of 2026-07-03 (41d ago); consensus_pnav flagged APPROX in comment — replace with Pareto / broker figure |
| ASC | ⚠ APPROX | as_of 2026-07-03 (41d ago); consensus_pnav flagged APPROX in comment — replace with Pareto / broker figure |
| TEN | ⚠ APPROX | as_of 2026-06-10 (64d ago); consensus_pnav flagged APPROX in comment — replace with Pareto / broker figure |
| CMDB | ⚠ APPROX | as_of 2026-06-10 (64d ago); consensus_pnav flagged APPROX in comment — replace with Pareto / broker figure |
| SBLK | ✓ | as_of 2026-07-03 (41d ago) |
| GNK | ✓ | as_of 2026-07-03 (41d ago) |
| CAPT | ✓ | as_of 2026-07-03 (41d ago) |
| MPCC | ⚠ APPROX | as_of 2026-07-03 (41d ago); consensus_pnav flagged APPROX in comment — replace with Pareto / broker figure |
| GSL | ⚠ APPROX | as_of 2026-06-12 (62d ago); consensus_pnav flagged APPROX in comment — replace with Pareto / broker figure |
| BRUT | ✓ | as_of 2026-07-03 (41d ago) |
| CMBT | ⚠ APPROX | as_of 2026-07-03 (41d ago); consensus_pnav flagged APPROX in comment — replace with Pareto / broker figure |
| SB | ⚠ APPROX | as_of 2026-06-26 (48d ago); consensus_pnav flagged APPROX in comment — replace with Pareto / broker figure |
| LPG | ✓ | as_of 2026-07-03 (41d ago) |
| BWLP | ✓ | as_of 2026-07-03 (41d ago) |
| 2343 | ✓ | as_of 2026-07-14 (30d ago) |

_11 ticker(s) carry APPROX consensus_pnav comments — replace with authoritative broker NAV print (Pareto / Cleaves / Clarksons) when the Q-end research notes land._

## 4. Per-ticker file age table

| Ticker | Fleet (≤90d) | BS for 2026-Q2 | Cost (≤180d) | Dividend (≤180d) |
|---|---|---|---|---|
| DHT | ✓ 3d | ✓ 5d ago | ✓ 76d | ✓ 76d |
| ECO | ✓ 5d | ✓ 5d ago | ✓ 76d | ✓ 76d |
| FRO | ✓ 52d | ✗ missing | ✓ 76d | ✓ 76d |
| INSW | ✓ 3d | ✓ 3d ago | ✓ 76d | ✓ 76d |
| TNK | ✓ 5d | ✓ 5d ago | ✓ 76d | ✓ 76d |
| NAT | ✓ 43d | ✗ missing | ✓ 73d | ✓ 73d |
| FLNG | ✓ 73d | ✗ missing | ✓ 73d | ✓ 73d |
| CCEC | ✓ 5d | ✓ 5d ago | ✓ 73d | ✓ 73d |
| STNG | ✓ 5d | ✓ 5d ago | ✓ 69d | ✓ 73d |
| HAFN | ✓ 43d | ✗ missing | ✓ 70d | ✓ 70d |
| TRMD | ✓ 42d | ✗ missing | ✓ 70d | ✓ 70d |
| ASC | ✓ 5d | ✓ 5d ago | ✓ 73d | ✓ 73d |
| TEN | ✓ 29d | ✗ missing | ✓ 68d | ✓ 68d |
| CMDB | ✓ 4d | ✓ 4d ago | ✓ 64d | ✓ 64d |
| SBLK | ✓ 4d | ✓ 4d ago | ✓ 65d | ✓ 65d |
| GNK | ✓ 5d | ✓ 5d ago | ✓ 64d | ✓ 64d |
| CAPT | ✓ 44d | ✗ missing | ✓ 63d | ✓ 63d |
| MPCC | ✓ 44d | ✗ missing | ✓ 62d | ✓ 62d |
| GSL | ✓ 5d | ✓ 5d ago | ✓ 62d | ✓ 62d |
| BRUT | ✓ 43d | ✗ missing | ✓ 52d | ✓ 52d |
| CMBT | ✓ 47d | ✗ missing | ✓ 48d | ✓ 48d |
| SB | ✓ 5d | ✓ 5d ago | ✓ 45d | ✓ 46d |
| LPG | ✓ 5d | ✓ 5d ago | ✓ 34d | ✓ 34d |
| BWLP | ✓ 34d | ✗ missing | ✓ 34d | ✓ 34d |
| 2343 | ✓ 5d | ✓ 5d ago | ✓ 30d | ✓ 30d |

_Thresholds: fleet manifest 90d (vessel sales/purchases happen quarterly); cost + dividend 180d (rarely change but should be re-validated annually)._

## 5. IR URL playbook (all watchlist)

For ad-hoc lookups outside the refresh cycle:

| Ticker | IR home | Press releases | SEC EDGAR | Fleet page |
|---|---|---|---|---|
| DHT | https://www.dhtankers.com/investors/ | https://www.dhtankers.com/news-releases/ | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001331284&type=6-K | https://www.dhtankers.com/fleetlist/ |
| ECO | https://www.okeanisecotankers.com/investors/ | https://www.okeanisecotankers.com/news/ | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001964954&type=6-K | https://www.okeanisecotankers.com/our-fleet/ |
| FRO | https://www.frontline.bm/investors/ | https://www.frontline.bm/news/ | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000913290&type=6-K | https://www.frontline.bm/fleet-list/ |
| INSW | https://www.intlseas.com/investors/ | https://www.intlseas.com/press-releases/ | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001679049&type=10-Q | https://www.intlseas.com/fleet/ |
| TNK | https://www.teekay.com/investors/ | https://www.teekay.com/blog/category/teekay-tankers-news/ | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001419945&type=10-Q | https://www.teekay.com/teekay-tankers/fleet/ |
| NAT | https://www.nat.bm/investors/ | https://www.nat.bm/news/ | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001000177&type=6-K | https://www.nat.bm/fleet/ |
| FLNG | https://www.flexlng.com/investors/ | https://www.flexlng.com/press-releases/ | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001772253&type=6-K | https://www.flexlng.com/our-fleet/ |
| CCEC | https://www.capclnenrg.com/investors/ | https://www.capclnenrg.com/news/ | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001392326&type=6-K | https://www.capclnenrg.com/fleet/ |
| STNG | https://www.scorpiotankers.com/investors/ | https://www.scorpiotankers.com/press-releases/ | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001483934&type=6-K | https://www.scorpiotankers.com/our-fleet/ |
| HAFN | https://www.hafniabw.com/investors/ | https://www.hafniabw.com/investors/announcements/ | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001815779&type=6-K | https://www.hafniabw.com/our-fleet/ |
| TRMD | https://www.torm.com/investors/ | https://www.torm.com/investors/announcements/ | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001655891&type=6-K | https://www.torm.com/our-fleet/ |
| ASC | https://ardmoreshipping.com/investors/ | https://ardmoreshipping.com/press-releases/ | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001577437&type=6-K | https://ardmoreshipping.com/our-fleet/ |
| TEN | https://www.tenn.gr/ | https://www.tenn.gr/news-events/ | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001166663&type=6-K | https://www.tenn.gr/fleet/ |
| CMDB | https://www.costamarebulkers.com/ | https://www.costamarebulkers.com/news/ | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0002033535&type=6-K | https://www.costamarebulkers.com/fleet/ |
| SBLK | https://www.starbulk.com/investor-relations/ | https://www.starbulk.com/investor-relations/news-releases/ | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001386716&type=6-K | https://www.starbulk.com/fleet/ |
| GNK | https://www.gencoshipping.com/ | https://www.gencoshipping.com/press-releases/ | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001326200&type=10-Q | https://www.gencoshipping.com/our-fleet/ |
| CAPT | https://www.capitaltankers.com/ | https://www.capitaltankers.com/news/ | — | https://www.capitaltankers.com/fleet/ |
| MPCC | — | — | — | https://www.mpc-container.com/fleet/our-fleet/ |
| GSL | — | — | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001430725&type=6-K | https://www.globalshiplease.com/fleet/ships-contract-cover |
| BRUT | https://bruton-ltd.com/ | https://bruton-ltd.com/news/ | — | https://bruton-ltd.com/fleet/ |
| CMBT | https://cmb.tech/investors | https://cmb.tech/news | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001604481&type=6-K | https://cmb.tech/fleet |
| SB | https://www.safebulkers.com/ | https://www.safebulkers.com/sbpress.html | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001434754&type=6-K | https://www.safebulkers.com/fleet.html |
| LPG | https://ir.dorianlpg.com/ | https://ir.dorianlpg.com/news-events/press-releases | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001596993&type=10-K | https://www.dorianlpg.com/fleet |
| BWLP | https://www.bwlpg.com/investors/ | https://www.bwlpg.com/media/press-releases/ | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001649313&type=6-K | https://www.bwlpg.com/fleet/ |
| 2343 | https://www.pacificbasin.com/en/ir/ | https://www.pacificbasin.com/en/ir/news.php | — | https://www.pacificbasin.com/en/fleet/fleet.php |
