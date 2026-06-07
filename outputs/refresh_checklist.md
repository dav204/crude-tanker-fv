# Refresh Checklist — 2026-Q1 (target quarter)

- **Today:** 2026-06-04
- **Target quarter:** 2026-Q1
- **Workflow:** work through the sections below, then run `python -m crude_tanker_fv.pipeline` to refresh outputs.

## Status summary

- ✓ **Balance sheets:** 11 of 11 present for 2026-Q1
- ✓ **Market data:** 5 of 5 fresh (< 30 days)
- ⚠ **Watchlist:** 7 of 11 clean — 0 stale, 4 APPROX consensus_pnav

## 1. Missing quarterly balance sheets

_All watchlist tickers have a balance sheet on file for 2026-Q1. ✓_

## 2. Stale market data

_All market data files were updated within 30 days. ✓_

## 3. Watchlist freshness

| Ticker | as_of status | Detail |
|---|---|---|
| DHT | ✓ | as_of 2026-05-29 (6d ago) |
| ECO | ✓ | as_of 2026-05-29 (6d ago) |
| FRO | ✓ | as_of 2026-05-29 (6d ago) |
| INSW | ✓ | as_of 2026-05-29 (6d ago) |
| TNK | ✓ | as_of 2026-05-29 (6d ago) |
| NAT | ⚠ APPROX | as_of 2026-05-29 (6d ago); consensus_pnav flagged APPROX in comment — replace with Pareto / broker figure |
| FLNG | ✓ | as_of 2026-05-30 (5d ago) |
| CCEC | ✓ | as_of 2026-06-01 (3d ago) |
| STNG | ⚠ APPROX | as_of 2026-05-29 (6d ago); consensus_pnav flagged APPROX in comment — replace with Pareto / broker figure |
| TRMD | ⚠ APPROX | as_of 2026-05-29 (6d ago); consensus_pnav flagged APPROX in comment — replace with Pareto / broker figure |
| ASC | ⚠ APPROX | as_of 2026-05-29 (6d ago); consensus_pnav flagged APPROX in comment — replace with Pareto / broker figure |

_4 ticker(s) carry APPROX consensus_pnav comments — replace with authoritative broker NAV print (Pareto / Cleaves / Clarksons) when the Q-end research notes land._

## 4. Per-ticker file age table

| Ticker | Fleet (≤90d) | BS for 2026-Q1 | Cost (≤180d) | Dividend (≤180d) |
|---|---|---|---|---|
| DHT | ✓ 6d | ✓ 6d ago | ✓ 6d | ✓ 6d |
| ECO | ✓ 6d | ✓ 6d ago | ✓ 6d | ✓ 6d |
| FRO | ✓ 6d | ✓ 6d ago | ✓ 6d | ✓ 6d |
| INSW | ✓ 6d | ✓ 6d ago | ✓ 6d | ✓ 6d |
| TNK | ✓ 6d | ✓ 6d ago | ✓ 6d | ✓ 6d |
| NAT | ✓ 3d | ✓ 3d ago | ✓ 3d | ✓ 3d |
| FLNG | ✓ 3d | ✓ 3d ago | ✓ 3d | ✓ 3d |
| CCEC | ✓ 3d | ✓ 3d ago | ✓ 3d | ✓ 3d |
| STNG | ✓ 3d | ✓ 3d ago | ✓ 3d | ✓ 3d |
| TRMD | ✓ 0d | ✓ 0d ago | ✓ 0d | ✓ 0d |
| ASC | ✓ 3d | ✓ 3d ago | ✓ 3d | ✓ 3d |

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
| TRMD | https://www.torm.com/investors/ | https://www.torm.com/investors/announcements/ | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001655891&type=6-K | https://www.torm.com/our-fleet/ |
| ASC | https://ardmoreshipping.com/investors/ | https://ardmoreshipping.com/press-releases/ | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001577437&type=6-K | https://ardmoreshipping.com/our-fleet/ |
