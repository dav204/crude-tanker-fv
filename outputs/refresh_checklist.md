# Refresh Checklist — 2026-Q1 (target quarter)

- **Today:** 2026-06-21
- **Target quarter:** 2026-Q1
- **Workflow:** work through the sections below, then run `python -m crude_tanker_fv.pipeline` to refresh outputs.

## Status summary

- ✓ **Balance sheets:** 19 of 19 present for 2026-Q1
- ✓ **Market data:** 5 of 5 fresh (< 30 days)
- ⚠ **Watchlist:** 1 of 19 clean — 7 stale, 11 APPROX consensus_pnav
- ✓ **Earnings:** no reports outstanding

## 0. Earnings calendar (report-day refresh runbook in CLAUDE.md)

| Ticker | Status | Detail |
|---|---|---|
| ASC | — | 2026-07-28 → 2026-07-30 (expected). Q1-26 May-7; Q2-25 Jul-30 (announced ~2wk ahead) |
| CAPT | — | 2026-08-17 → 2026-08-31 (expected). First-ever results (Q1-26) came May-27; Oslo H1-report cadence implies late Aug. No published calendar yet — watch the dailies. |
| CCEC | — | 2026-07-29 → 2026-08-06 (expected). Q1-26 May-7; Q2-25 Jul-31 |
| CMDB | — | 2026-08-04 → 2026-08-10 (expected). Q1-26 release May-13; H1-25 Aug-8; announces ~1-2wk ahead |
| DHT | — | 2026-08-05 → 2026-08-06 (expected). Q1-26 May-5; Q2-25 Aug-6 (announced Jul-23) |
| ECO | — | 2026-08-04 (confirmed). company financial calendar (half-yearly 04.08.2026; Q1 slot matched actual) |
| FLNG | — | 2026-08-20 → 2026-08-28 (confirmed). calendar slot 28.08.2026, but 2025 release came Aug-20 — window opened accordingly |
| FRO | — | 2026-08-26 → 2026-08-31 (expected). Q1-26 May-22; Q2-25 Aug-29 (last Friday of Aug) |
| GNK | — | 2026-08-04 → 2026-08-06 (expected). Q1-26 May-6; Q2-25 Aug-6 (announced Jul-21). Diana tender deadline Jun-26 precedes. |
| GSL | — | 2026-08-04 → 2026-08-06 (expected). Q2-25 Aug-5 pre-market; Q1-26 followed 10-day-notice pattern (notice May-12, release May-22) |
| HAFN | — | 2026-08-28 (confirmed). published 2025-2027 financial calendar (Q1-26 slot matched actual) |
| INSW | — | 2026-08-04 → 2026-08-07 (expected). Q1-26 May-7; Q2-25 Aug-6 |
| MPCC | — | 2026-08-26 (confirmed). company financial calendar (fetched 2026-06-12): Q2 26.08.2026, Q3 25.11.2026 |
| NAT | — | 2026-08-26 → 2026-08-31 (expected). Q1-26 May-28; Q2-25 Aug-28; nat.bm calendar has no Q2 date yet |
| SBLK | — | 2026-08-05 (confirmed). starbulk.com financial calendar (Q1 May-20 slot matched actual) |
| STNG | — | 2026-07-28 → 2026-07-30 (expected). Q1-26 May-5; Q2-25 Jul-30 (announced Jul-18) |
| TEN | — | 2026-09-08 → 2026-09-17 (expected). H1 reporter — Q2/H1-25 reported Sep-10; Q1-26 May-21. September, NOT August. |
| TNK | — | 2026-07-29 → 2026-07-31 (expected). Q2-25 released Jul-30 after close, call next morning; announces ~8d ahead |
| TRMD | — | 2026-08-26 (confirmed). TORM Financial Calendar 2026 company announcement |

## 1. Missing quarterly balance sheets

_All watchlist tickers have a balance sheet on file for 2026-Q1. ✓_

## 2. Stale market data

_All market data files were updated within 30 days. ✓_

## 3. Watchlist freshness

| Ticker | as_of status | Detail |
|---|---|---|
| DHT | ⚠ stale | as_of 2026-06-04 (17d ago, threshold 14d) |
| ECO | ⚠ stale | as_of 2026-06-04 (17d ago, threshold 14d) |
| FRO | ⚠ stale | as_of 2026-06-04 (17d ago, threshold 14d) |
| INSW | ⚠ stale | as_of 2026-06-04 (17d ago, threshold 14d) |
| TNK | ⚠ stale | as_of 2026-06-04 (17d ago, threshold 14d) |
| NAT | ⚠ APPROX | as_of 2026-06-04 (17d ago); consensus_pnav flagged APPROX in comment — replace with Pareto / broker figure |
| FLNG | ⚠ APPROX | as_of 2026-06-04 (17d ago); consensus_pnav flagged APPROX in comment — replace with Pareto / broker figure |
| CCEC | ⚠ APPROX | as_of 2026-06-04 (17d ago); consensus_pnav flagged APPROX in comment — replace with Pareto / broker figure |
| STNG | ⚠ APPROX | as_of 2026-06-04 (17d ago); consensus_pnav flagged APPROX in comment — replace with Pareto / broker figure |
| HAFN | ⚠ APPROX | as_of 2026-06-04 (17d ago); consensus_pnav flagged APPROX in comment — replace with Pareto / broker figure |
| TRMD | ⚠ APPROX | as_of 2026-06-04 (17d ago); consensus_pnav flagged APPROX in comment — replace with Pareto / broker figure |
| ASC | ⚠ APPROX | as_of 2026-06-04 (17d ago); consensus_pnav flagged APPROX in comment — replace with Pareto / broker figure |
| TEN | ⚠ APPROX | as_of 2026-06-10 (11d ago); consensus_pnav flagged APPROX in comment — replace with Pareto / broker figure |
| CMDB | ⚠ APPROX | as_of 2026-06-10 (11d ago); consensus_pnav flagged APPROX in comment — replace with Pareto / broker figure |
| SBLK | ⚠ stale | as_of 2026-06-05 (16d ago, threshold 14d) |
| GNK | ⚠ stale | as_of 2026-06-04 (17d ago, threshold 14d) |
| CAPT | ✓ | as_of 2026-06-10 (11d ago) |
| MPCC | ⚠ APPROX | as_of 2026-06-12 (9d ago); consensus_pnav flagged APPROX in comment — replace with Pareto / broker figure |
| GSL | ⚠ APPROX | as_of 2026-06-12 (9d ago); consensus_pnav flagged APPROX in comment — replace with Pareto / broker figure |

_11 ticker(s) carry APPROX consensus_pnav comments — replace with authoritative broker NAV print (Pareto / Cleaves / Clarksons) when the Q-end research notes land._

## 4. Per-ticker file age table

| Ticker | Fleet (≤90d) | BS for 2026-Q1 | Cost (≤180d) | Dividend (≤180d) |
|---|---|---|---|---|
| DHT | ✓ 23d | ✓ 23d ago | ✓ 23d | ✓ 23d |
| ECO | ✓ 23d | ✓ 23d ago | ✓ 23d | ✓ 23d |
| FRO | ✓ 23d | ✓ 23d ago | ✓ 23d | ✓ 23d |
| INSW | ✓ 23d | ✓ 23d ago | ✓ 23d | ✓ 23d |
| TNK | ✓ 23d | ✓ 23d ago | ✓ 23d | ✓ 23d |
| NAT | ✓ 20d | ✓ 20d ago | ✓ 20d | ✓ 20d |
| FLNG | ✓ 20d | ✓ 20d ago | ✓ 20d | ✓ 20d |
| CCEC | ✓ 20d | ✓ 20d ago | ✓ 20d | ✓ 20d |
| STNG | ✓ 16d | ✓ 16d ago | ✓ 16d | ✓ 20d |
| HAFN | ✓ 16d | ✓ 16d ago | ✓ 17d | ✓ 17d |
| TRMD | ✓ 17d | ✓ 17d ago | ✓ 17d | ✓ 17d |
| ASC | ✓ 16d | ✓ 16d ago | ✓ 20d | ✓ 20d |
| TEN | ✓ 9d | ✓ 14d ago | ✓ 15d | ✓ 15d |
| CMDB | ✓ 11d | ✓ 11d ago | ✓ 11d | ✓ 11d |
| SBLK | ✓ 12d | ✓ 12d ago | ✓ 12d | ✓ 12d |
| GNK | ✓ 11d | ✓ 11d ago | ✓ 11d | ✓ 11d |
| CAPT | ✓ 10d | ✓ 10d ago | ✓ 10d | ✓ 10d |
| MPCC | ✓ 9d | ✓ 9d ago | ✓ 9d | ✓ 9d |
| GSL | ✓ 9d | ✓ 9d ago | ✓ 9d | ✓ 9d |

_Thresholds: fleet manifest 90d (vessel sales/purchases happen quarterly); cost + dividend 180d (rarely change but should be re-validated annually)._

## 5. IR URL playbook (all watchlist)

For ad-hoc lookups outside the refresh cycle:

| Ticker | IR home | Press releases | SEC EDGAR | Fleet page |
|---|---|---|---|---|
| DHT | https://www.dhtankers.com/investors/ | https://www.dhtankers.com/news-releases/ | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001331284&type=6-K | https://www.dhtankers.com/fleetlist/ |
| ECO | https://www.okeanisecotankers.com/investors/ | https://www.okeanisecotankers.com/news/ | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&company=okeanis&type=20-F | https://www.okeanisecotankers.com/our-fleet/ |
| FRO | https://www.frontline.bm/investors/ | https://www.frontline.bm/news/ | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000913290&type=6-K | https://www.frontline.bm/fleet-list/ |
| INSW | https://www.intlseas.com/investors/ | https://www.intlseas.com/press-releases/ | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001650044&type=10-Q | https://www.intlseas.com/fleet/ |
| TNK | https://www.teekay.com/investors/ | https://www.teekay.com/blog/category/teekay-tankers-news/ | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001419945&type=10-Q | https://www.teekay.com/teekay-tankers/fleet/ |
| NAT | https://www.nat.bm/investors/ | https://www.nat.bm/news/ | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001000177&type=6-K | https://www.nat.bm/fleet/ |
| FLNG | https://www.flexlng.com/investors/ | https://www.flexlng.com/press-releases/ | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001738202&type=6-K | https://www.flexlng.com/our-fleet/ |
| CCEC | https://www.capclnenrg.com/investors/ | https://www.capclnenrg.com/news/ | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001736035&type=6-K | https://www.capclnenrg.com/fleet/ |
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
| GSL | — | — | — | https://www.globalshiplease.com/fleet/ships-contract-cover |
