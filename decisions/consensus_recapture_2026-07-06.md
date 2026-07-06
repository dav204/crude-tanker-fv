# Consensus-pair recapture — 2026-07-06 sitting (trigger all_sectors_consensus_pair_recapture)

First recapture under the WORKFLOWS packet procedure, run 4 days ahead of the
Jul-10 due date. **One sitting, one source: the Pareto Shipping Daily of
2026-07-03** (the newest edition carrying the full share-price/P/NAV/P/E
table; its date matches the committed Friday close in prices_daily.yaml, so
price file, FX and consensus all sit on one vintage). Extraction was
triple-verified — three independent methods (layout-parse, 300-dpi visual
read, pypdf raw-stream parse) agreed unanimously on all 66 cells.

## What was rebased (18 of 22 names, as_of → 2026-07-03)

Full pairs (price + pnav + fwd P/E): DHT 17.20/1.14/9.3 · ECO 53.10/1.35/9.4 ·
FRO 36.80/1.37/9.4 · INSW 82.40/1.11/12.0 · TNK 67.60/0.73/8.4 ·
STNG 73.00/0.69/11.1 · HAFN 7.00/0.86/8.7 · TRMD 27.70/0.82/9.3 ·
CMBT 14.60/0.73/8.9 · GNK 24.50/0.89/14.2 · SBLK 25.20/0.78/6.4 ·
FLNG 29.30/1.35/14.1 · CAPT 13.31/0.69/15.5 (kr 130.7 × 0.101838) ·
BRUT 5.30/0.72/19.0 (kr 52.0 ×) — the Apr-22 worst-case vintage closed.

APPROX names (pnav retained, px + P/E rebased): ASC 14.90/—/13.2 ·
NAT 5.80/—/19.2 · CCEC 21.60/—/8.1 (Pareto printed no CCEC pnav this
edition) · MPCC 2.44/—/7.7 (kr 24.0 ×).

**Left untouched — flag, don't fake:** TEN, SB, GSL, CMDB are absent from
this edition's (unusually short, ~32-name) table; their pairs stay at their
documented vintages (TEN Jun-10, SB Jun-26, GSL Jun-12, CMDB Jun-10). TEN
re-enters the stale list until an edition carries it again.

## Gate results

- **EV / NAV / bands: all 22 stable** — live prices already flowed via
  prices_daily.yaml, so the recapture moved only the broker-relative layer.
- **k_broker second-difference: 5 UNEXPLAINED** (the event itself — consensus
  NAVs moved vs our marks over the month): INSW Δk −0.19 (pnav 0.98→1.11;
  Pareto's NAV came DOWN toward the tool — spread 29→20pp), FRO −0.10,
  ECO −0.09, HAFN +0.11, TNK +0.08. SANITY OK on all five. To be accepted
  via ratify with this sitting's cause.
- **Two vintage-pinned tests re-pinned** (dated comments): DHT price
  16.40→17.20; the INSW hybrid-discrimination test now pins the PROPERTY
  (k above the 1.25 pure-play ceiling, double-digit spread) not the vintage.

## Threshold decision — RESOLVED: 42 days (owner, 2026-07-06)

The 14d watchlist freshness threshold guaranteed standing digest flags
between sittings. Owner set **42d** at review (six weeks — monthly rhythm
plus slack; between the recommended 30d and the quarterly cadence). The
quarterly recapture trigger (due 2026-10-02) and the staleness-floor
trigger remain the hard backstops; `WATCHLIST_STALE_DAYS` carries the
dated rationale. Under 42d, TEN/SB/GSL/CMDB (left at Jun-10..26 vintages)
start flagging from ~late July if no intervening edition carries them —
which is the wanted behavior going into the Jul-28 earnings cluster.
