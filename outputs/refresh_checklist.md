# Refresh Checklist — 2026-Q2 (target quarter)

- **Today:** 2026-09-15
- **Target quarter:** 2026-Q2
- **Workflow:** work through the sections below, then run `python -m crude_tanker_fv.pipeline` to refresh outputs.

## Status summary

- ⚠ **Balance sheets:** 24 of 25 present for 2026-Q2 — missing: TEN
- ✓ **Market data:** 4 of 4 fresh (< 30 days)
- ⚠ **Watchlist:** 14 of 25 clean — 0 stale, 11 APPROX consensus_pnav
- ⚠ **Earnings:** REFRESH DUE: TEN
- ✓ **§13.3 reweight triggers:** none due — upcoming: crude_geopolitics_weekly

## 0a. Scenario-weight re-evaluation triggers (`inputs/reweight_triggers.yaml`)

| Trigger | Status | Detail |
|---|---|---|
| crude_geopolitics_weekly | 🟡 | [crude+product] due in 2d (2026-09-17). ONE weekly check, two legs, PRIMARY SOURCES ONLY (CENTCOM releases, the UKMTO incident log, dated wires; broker paraphrase corroborates, nev |
| container_mb_refresh | — | [containerships] due 2026-10-02. Monthly re-capture of the container determinants (Ctr-* TC + value assessments) from the newest staged MB Container Weekly — the §11.8 sourc |
| handy_bulk_txn_refit | — | [dry_bulk] standing event-watch. Standing event-watch (§11.7.11 Option B, owner-ratified 2026-07-14): the dry-Handysize classified print sample reaches >=10 human-classified |
| lpg_anchor_annual_review | — | [lpg] due 2027-06-30. The VLGC 10-yr through-cycle TCE anchor (~$40,000/day, as_of 2026-07-07, WO3 decisions/lpg_methodology_2026-07-07.md) is a TRAILING 10-yr av |
| lpg_v1_lock_rerun | — | [lpg] due 2026-11-13. Dorian trio per-vessel sale splits (Corsair 2014 + two unnamed 2015-built VLGCs, $256M en bloc agreed Jun-23-2026, deliveries "by" Q4-2026). |
| ppmx_txn_refit | — | [dry_bulk] standing event-watch. Standing event-watch (PPMX §9.9 seed, owner-ruled 2026-07-18): the Post-Panamax classified print sample reaches >=8 in-window prints includi |
| product_glut_arrival_timing | — | [product] due 2026-10-02. The product family's central live uncertainty (reviewer rider 1): does the clean-tonnage glut arrive on the 2027 schedule the glut_base leg  |
| tce_means_semiannual_review | — | [all] due 2026-12-07. EVERY entry in inputs/market_data/historical_tce_means.yaml is a TRAILING 10-year mean, so every one of them DRIFTS as the window rolls — it |

## 0. Earnings calendar (report-day refresh runbook in CLAUDE.md)

| Ticker | Status | Detail |
|---|---|---|
| TEN | 🔴 DUE | report OUT (2026-09-10, confirmed) and no 2026-Q2 balance sheet on file — refresh due. RESULTS ANNOUNCED 2026-09-10 (recorded at the 2026-09-10 sweep): issuer PR GlobeNewswire 3359616, 09:15 ET "TEN, Ltd. Reports Profits for the First Half and Second Quarter of 2026" — pre-open exactly as the 8/20 date-PR (GlobeNewswire 3348799) promised: "prior to the open of the market in New York on Thursday, September 10, 2026"; call 10:00 ET same day. No 6-K on EDGAR yet at sweep time (last 6-K 2026-05-22) — the PR-first/6-K-later pattern; subsequent-event flag for the H1 refresh: 9/01 PR 3354219 sale of two first-generation Suezmaxes (named Alaska/Archangel in the 9/10 PR). Entry historical until the Q3 re-seed; H1 refresh queued (decisions/ten_h1_refresh_packet_2026-09-07.md, ten_h1_release_check_2026-09-10.md). |
| 2343 | — | 2026-08-06 (confirmed). Aug-6 now FORMALLY confirmed: HKEX board-meeting notice filed 2026-07-24 (hkex-12255247, staged inputs/filings/2343/12255247_2026072400392.pdf) — Board meets 6 Aug 2026 to approve H1-2026 interims + consider interim dividend. Supersedes the IR-calendar-only basis. |
| ASC | — | 2026-07-29 (confirmed). CONFIRMED 2026-07-28 sweep: issuer PR 'Ardmore Shipping Announces Second Quarter 2026 Conference Call' (StockTitan/PRNewswire) — Q2 results PRE-MARKET Wed Jul-29, call 10:00 ET same day, replay to Aug-5. Was expected/no-PR at the 7/22 sweep. |
| BRUT | — | 2026-08-13 (confirmed). RE-VERIFIED 2026-07-21 via the Euronext company-information calendar (exchange-published): Half-yearly Report 13/08/2026; AGM 12/08/2026. No timing stated. (Issuer legal name Bruton Limited.) Original NewsWeb filing not retrievable — calendar-grade source. |
| BWLP | — | 2026-08-28 (confirmed). Q2-2026 date CONFIRMED by the issuer: 6-K 0001213900-26-078478 ex-99.1 (7/16 Product Services pre-announcement) states 'the BW LPG Q2 2026 results ... will be released on 28 August 2026'. (Was cadence-derived 8/25-8/28, seeded 2026-07-10.) |
| CAPT | — | 2026-09-01 (confirmed). Oslo Bors Newspoint financial calendar (published 2026-03-12): HALF-YEARLY report Sep-1-2026 — the Jun-11 sweep missed this calendar; replaces the expected Aug-17..31 window. RE-VERIFIED 2026-08-31 sweep (in-14d early-release check): issuer scheduling release 8/26 (newsweb mfn c5ae112b, on file inputs/filings/CAPT/) confirms results BEFORE Euronext Growth Oslo open Tue Sep-1, call 14:30 CET / 8:30 ET — no early-release risk. |
| CCEC | — | 2026-07-29 (confirmed). CONFIRMED 2026-07-22 by the issuer's date-setting announcement PR (GlobeNewswire 2026-07-22, Athens), landed exactly on the predicted ~Jul-22-24 pattern: 'Capital Clean Energy Carriers Corp. Schedules Second Quarter 2026 Earnings Release, Conference Call and Webcast' — Q2 results BEFORE the Nasdaq open Wed Jul-29; interactive call same day 9:00 a.m. ET. ALSO the governance CCEC t2 print-gate venue (window 7/29-8/06 in the gov prereg; the print lands at its OPEN). |
| CMBT | — | 2026-08-27 (confirmed). CMB.TECH PR (GlobeNewswire 2026-06-29): Q2-2026 announcement Aug-27; SEEDED 2026-07-03 (was absent from the Jun-11 sweep) |
| CMDB | — | 2026-08-03 (confirmed). RESULTS ANNOUNCED 2026-08-03 (Q2 6-K acc 0001171843-26-005131 - landed at the WIDENED-START edge as the window note anticipated) - refreshed at the 8/9 drain close. |
| DHT | — | 2026-08-05 (confirmed). CONFIRMED 2026-07-28 sweep: GlobeNewswire 2026-07-22 + dhtankers.com — Q2 results AFTER CLOSE Wed Aug-5, call Thu Aug-6 8:00 ET. Landed on the ~2wk-ahead date-PR pattern. |
| ECO | — | 2026-08-04 (confirmed). RE-VERIFIED 2026-07-21 unchanged: official financial calendar (GlobeNewswire 2025-12-19 + okeanisecotankers.com): '04.08.2026 - Half-yearly Report', all releases AFTER NYSE close. Q2 webcast invitation expected ~end-July (Q1 pattern ~5d ahead). |
| FLNG | — | 2026-08-19 (confirmed). MOVED TO AUG-19 — the early-release risk this entry carried FIRED (9 days early, vs ~1wk in 2025). CONFIRMED 2026-08-18 at the issuer primary: flexlng.com 'Flex LNG - Invitation to the 2026 Second Quarter Presentation' — Q2 results ~07:00 CEST (~01:00 ET) Wed Aug-19, webcast 15:00 CEST. Prereg band frozen pre-print: decisions/flng_q2_prereg_2026-08-18.md [25.40, 29.80]. Supersedes the 28.08 calendar entry. |
| FRO | — | 2026-08-31 (confirmed). frontlineplc.cy/calendar (announced 2026-05-22): Q2-2026 report Aug-31; narrowed from the expected Aug-26..31 window |
| GNK | — | 2026-08-05 (confirmed). OFFICIAL PR 2026-07-14 (GlobeNewswire 3327275): Q2 results AFTER CLOSE Wed Aug-5; call Thu Aug-6 8:30 ET. Swept 2026-07-21. |
| GSL | — | 2026-08-05 (confirmed). RESULTS ANNOUNCED 2026-08-05 (earnings-release 6-K) + H1 interim 8/6 (acc 0001140361-26-031697) - refreshed at the 8/8 drain; the short-notice pattern note stands for Q3. |
| HAFN | — | 2026-08-28 (confirmed). Hafnia Financial Calendar 2025-2027 (IR PDF): Q2-26 Aug-28; calendar adherence validated on the Q1-26 slot (May-27 = actual) |
| INSW | — | 2026-08-10 (confirmed). CONFIRMED 2026-08-09 sweep: official Business Wire date-PR 2026-07-24 - Q2 results BEFORE market open Monday Aug-10, call 9:00 ET. Supersedes the aggregator 8/4-8/7 window. |
| LPG | — | 2026-08-05 (confirmed). RESULTS ANNOUNCED 2026-08-05 (FQ1-2027 10-Q acc 0001596993-26-000035 + earnings-release 8-K) - refreshed at the 8/8 drain; entry historical until the Q3 re-seed. |
| MPCC | — | 2026-08-26 (confirmed). MFN financial calendar announcement (2025-12-30): half-yearly/Q2 report 26.08.2026 |
| NAT | — | 2026-08-27 (confirmed). REPORT LANDED 2026-08-27 (recorded at the 2026-08-31 sweep): 6-K acc 0000919574-26-005786 filed 8/27 = the Q2-2026 dividend + earnings report (ex-1 PR dated Aug-27) — caught by the hourly EDGAR poller exactly per the standing NAT pattern (terse report-day release, no pre-announcement; the 8/18 sweep's aggregator SPLIT ~8/27 vs ~8/31 resolved to the 8/27 side). Entry historical until the Q3 re-seed; Q2 refresh queued. |
| SB | — | 2026-07-28 (confirmed). CONFIRMED 2026-07-28 sweep: sets-date PR GlobeNewswire 2026-07-22 'Safe Bulkers, Inc. Sets Date for the Second Quarter 2026 Results' — results AFTER CLOSE Tue Jul-28 (TONIGHT), call Wed Jul-29 10:30 ET. The 7/22 sweep just missed it (PR landed same day, later). No August slip. |
| SBLK | — | 2026-08-05 (confirmed). RESULTS ANNOUNCED 2026-08-05 (earnings-release 6-K acc 0000950157-26-000846) + interim 6-K 8/7 - refreshed at the 8/8 drain; entry historical until the Q3 re-seed. |
| STNG | — | 2026-07-30 (confirmed). OFFICIAL PR 2026-07-20 (scorpiotankers.com/GlobeNewswire): Q2 results IN THE MORNING (pre-market) Thu Jul-30; call same day 8:00 ET. Swept 2026-07-21. |
| TNK | — | 2026-07-29 (confirmed). OFFICIAL joint Teekay Group PR 2026-07-14 (GlobeNewswire 3327260): Q2 results AFTER CLOSE Wed Jul-29; call Thu Jul-30 11:00 ET. Swept 2026-07-21. |
| TRMD | — | 2026-08-26 (confirmed). TORM 'Financial Calendar 2026' announcement (2025-12-19): Q2 Aug-26; adherence validated on Q1 (May-13 = actual) |

## 1. Missing quarterly balance sheets

For each missing name below, pull the 2026-Q2 results from the listed IR URLs and populate `inputs/balance_sheets/{ticker}_2026-Q2.yaml`:

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


## 2. Stale market data

_All market data files were updated within 30 days. ✓_

## 3. Watchlist freshness

| Ticker | as_of status | Detail |
|---|---|---|
| DHT | ✓ | as_of 2026-08-28 (18d ago) |
| ECO | ✓ | as_of 2026-08-28 (18d ago) |
| FRO | ✓ | as_of 2026-08-28 (18d ago) |
| INSW | ✓ | as_of 2026-08-28 (18d ago) |
| TNK | ✓ | as_of 2026-08-28 (18d ago) |
| NAT | ⚠ APPROX | as_of 2026-08-28 (18d ago); consensus_pnav flagged APPROX in comment — replace with Pareto / broker figure |
| FLNG | ✓ | as_of 2026-08-28 (18d ago) |
| CCEC | ⚠ APPROX | as_of 2026-08-28 (18d ago); consensus_pnav flagged APPROX in comment — replace with Pareto / broker figure |
| STNG | ⚠ APPROX | as_of 2026-08-28 (18d ago); consensus_pnav flagged APPROX in comment — replace with Pareto / broker figure |
| HAFN | ✓ | as_of 2026-08-28 (18d ago) |
| TRMD | ⚠ APPROX | as_of 2026-08-28 (18d ago); consensus_pnav flagged APPROX in comment — replace with Pareto / broker figure |
| ASC | ⚠ APPROX | as_of 2026-08-28 (18d ago); consensus_pnav flagged APPROX in comment — replace with Pareto / broker figure |
| TEN | ⚠ APPROX | as_of 2026-09-09 (6d ago); consensus_pnav flagged APPROX in comment — replace with Pareto / broker figure |
| CMDB | ⚠ APPROX | as_of 2026-09-09 (6d ago); consensus_pnav flagged APPROX in comment — replace with Pareto / broker figure |
| SBLK | ✓ | as_of 2026-08-28 (18d ago) |
| GNK | ✓ | as_of 2026-08-28 (18d ago) |
| CAPT | ✓ | as_of 2026-08-28 (18d ago) |
| MPCC | ⚠ APPROX | as_of 2026-08-28 (18d ago); consensus_pnav flagged APPROX in comment — replace with Pareto / broker figure |
| GSL | ⚠ APPROX | as_of 2026-06-12 (95d ago); consensus_pnav flagged APPROX in comment — replace with Pareto / broker figure |
| BRUT | ✓ | as_of 2026-08-28 (18d ago) |
| CMBT | ⚠ APPROX | as_of 2026-08-28 (18d ago); consensus_pnav flagged APPROX in comment — replace with Pareto / broker figure |
| SB | ⚠ APPROX | as_of 2026-08-28 (18d ago); consensus_pnav flagged APPROX in comment — replace with Pareto / broker figure |
| LPG | ✓ | as_of 2026-08-28 (18d ago) |
| BWLP | ✓ | as_of 2026-08-28 (18d ago) |
| 2343 | ✓ | as_of 2026-08-28 (18d ago) |

_11 ticker(s) carry APPROX consensus_pnav comments — replace with authoritative broker NAV print (Pareto / Cleaves / Clarksons) when the Q-end research notes land._

## 4. Per-ticker file age table

| Ticker | Fleet (≤90d) | BS for 2026-Q2 | Cost (≤180d) | Dividend (≤180d) |
|---|---|---|---|---|
| DHT | ✓ 36d | ✓ 38d ago | ✓ 109d | ✓ 109d |
| ECO | ✓ 38d | ✓ 38d ago | ✓ 109d | ✓ 109d |
| FRO | ✓ 15d | ✓ 15d ago | ✓ 109d | ✓ 109d |
| INSW | ✓ 36d | ✓ 36d ago | ✓ 109d | ✓ 109d |
| TNK | ✓ 38d | ✓ 38d ago | ✓ 109d | ✓ 109d |
| NAT | ✓ 15d | ✓ 15d ago | ✓ 106d | ✓ 106d |
| FLNG | ✓ 21d | ✓ 21d ago | ✓ 106d | ✓ 106d |
| CCEC | ✓ 38d | ✓ 38d ago | ✓ 106d | ✓ 106d |
| STNG | ✓ 38d | ✓ 38d ago | ✓ 102d | ✓ 106d |
| HAFN | ✓ 15d | ✓ 15d ago | ✓ 103d | ✓ 103d |
| TRMD | ✓ 17d | ✓ 17d ago | ✓ 103d | ✓ 103d |
| ASC | ✓ 38d | ✓ 38d ago | ✓ 106d | ✓ 106d |
| TEN | ✓ 62d | ✗ missing | ✓ 101d | ✓ 101d |
| CMDB | ✓ 37d | ✓ 37d ago | ✓ 97d | ✓ 97d |
| SBLK | ✓ 37d | ✓ 37d ago | ✓ 98d | ✓ 98d |
| GNK | ✓ 38d | ✓ 38d ago | ✓ 97d | ✓ 97d |
| CAPT | ✓ 14d | ✓ 14d ago | ✓ 96d | ✓ 96d |
| MPCC | ✓ 15d | ✓ 15d ago | ✓ 95d | ✓ 95d |
| GSL | ✓ 38d | ✓ 38d ago | ✓ 95d | ✓ 95d |
| BRUT | ✓ 17d | ✓ 17d ago | ✓ 85d | ✓ 85d |
| CMBT | ✓ 5d | ✓ 5d ago | ✓ 81d | ✓ 81d |
| SB | ✓ 38d | ✓ 38d ago | ✓ 78d | ✓ 79d |
| LPG | ✓ 38d | ✓ 38d ago | ✓ 67d | ✓ 67d |
| BWLP | ✓ 5d | ✓ 15d ago | ✓ 67d | ✓ 67d |
| 2343 | ✓ 38d | ✓ 38d ago | ✓ 63d | ✓ 63d |

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
