# Baseline-ratify review — 2343 onboarding + the 2026-07-14 price vintage

**The decision:** re-anchor `baselines/reconcile_baseline.yaml` via
`./scripts/ratify_baseline.sh "2343 onboarding + 2026-07-14 price vintage"`.
This page consolidates everything the ratify absorbs. Baseline being replaced:
2026-07-13T17:30Z (yesterday's four-flip ratify, RATIFY_LOG).

## What the gate shows (drift_gate @ HEAD 155cd11, 2026-07-14)

**25 rows: 1 new (2343) + 10 UNEXPLAINED + 14 stable. ΔNAV is +0.0% on EVERY row** —
no valuation input moved for any existing name (the delta report printed FV/PW/NAV
"no change" across the book at the onboarding run). Everything below is the Jul-13 →
Jul-14 price tape read through pinned consensus vintages, plus the new name.

### 1. The new row — 2343 (the onboarding itself)
First tracking entry; the full record is `decisions/2343_log.md` (pre-registered bands →
first-run results, all four PASSED) and the verdict row in `outputs/book_scorecard.md`
(GOVERNED-WIDE·pending-anchor · HOLD · SANITY −2.0% n/a-APPROX). Nothing to accept beyond
"start tracking it".

### 2. The two BAND FLIPS (the only judgment cells — eyeballed individually, not batched)
- **CMDB BUY→HOLD** — price +$0.49 to $19.56 on the 7/14 tape; FV/NAV byte-unchanged;
  EV +2.8% fell under the BUY band. Shallow boundary crossing. Eyeball note:
  `decisions/cmdb_log.md` 2026-07-14. Recross watch armed.
- **SBLK BUY→HOLD** — price +$0.19 to $26.54; FV/NAV byte-unchanged; EV +4.3% (was +5.7%),
  just under the band. SBLK stays weight-sign-stable-positive (WO4). Eyeball note:
  `decisions/sblk_log.md` 2026-07-14. Recross watch armed.

### 3. The eight EV%-only rows (routine price-vintage drift, all ΔNAV 0.0)
ASC +3.5pp · TEN +3.0 · TNK +2.5 (k −0.05 at the second-difference edge, price-mechanical
through the pinned Jul-3 P/NAV — the STNG 7/10 precedent) · STNG +2.4 · TRMD +2.1 ·
BWLP −2.4 · MPCC −2.4 · CAPT −2.1. All are the tape vs pinned consensus pairs; none is a
position event; none crosses a band.

## What the ratify does NOT touch
The FY25 final-dividend/buyback post-snapshot outflows, the scrubber-aggregate omission, and
the Handy-Bulk un-anchored cap are documented input-level limits (2343_log "known limits"),
not drift — they ride with the name until the Interim/IR resolves them.

## Suggested reading order (5 minutes)
1. This page.
2. `decisions/2343_log.md` — the bands-vs-results section (the onboarding's honesty check).
3. The 2343 row + price-basis header in `outputs/book_scorecard.md`.
4. The two flip notes (cmdb_log / sblk_log, 2026-07-14 entries).

**On your go** ("ratify" or run it yourself): `./scripts/ratify_baseline.sh
"2343 onboarding + 2026-07-14 price vintage"` — clears both designed drift reds
(suite → fully green), then push at your convenience.
