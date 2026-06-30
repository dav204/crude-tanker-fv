# MB LNG Weekly — first cross-check vs FLNG / CCEC (2026-06-29)

The LNG Weekly (the formerly-missing 4th MB feed) now arrives; this is its first fold into
the FLNG/CCEC cross-check. **MB is a cross-check, NOT a calibration input** (CLAUDE.md / VIE
discipline) — nothing promoted, no input changed. Source: MB LNG Weekly 26/2026 (2026-06-25).

## MB LNG marks (extracted)

- **Spot charter ($/day):** Steam ~$20k · DFDE/TFDE ~$59k · modern 2-stroke ~$88k.
- **Term charter ($/day, delivered +1mo):** Steam 1Y $20k · DFDE/TFDE 1Y $57k / 3Y $47k ·
  modern 1Y $76k / 3Y $77k / 7Y $81k / 10Y $83k.
- **Newbuilding:** ~**$248M** (174k 2-stroke), ~$225M (alt spec).
- **2nd-hand:** 138k **20yr Steam = $21M** (near-obsolete old steam tonnage).

## Cross-check vs the tool (FLNG/CCEC are modern 2-stroke fleets)

| Mark | Tool | MB | Read |
|---|--:|--:|---|
| LNGC newbuild | $260M | ~$248M (modern) | tool ~5% high (15% vs the $225M alt) |
| LNG through-cycle TC (`historical_tce_means`) | $85k | $76–83k modern term (1Y–10Y) | tool at/ABOVE the top of MB's term structure |
| LNGC 12M TC | $60k | $59k DFDE spot / $88k modern spot | matches DFDE; well below modern spot |
| Old-age (20yr) | curve ~$100M interp | $21M (steam) | tool steam-BLIND — over-values old steam |

## Findings (flagged, not actioned)

1. **Modest rich-tilt on the tool's modern-LNG marks vs MB:** newbuild ~5% high, the $85k
   through-cycle anchor sits at/above MB's modern 10Y term ($83k). Directionally the tool reads
   LNG slightly richer than MB — consistent with FLNG/CCEC carrying `structural-unavailable` /
   no-validated-rate status on the scorecard. Within cross-check tolerance; no §6 restatement.
2. **The tool's LNG curve does not distinguish steam vs modern 2-stroke** — MB's $21M for a 20yr
   steam vs the curve's ~$100M interpolation shows the old-age leg is steam-blind. **FLNG/CCEC are
   modern, so unexposed**, but any future old-steam LNG holder would be over-marked. Logged as a
   known limit (LIMITATIONS.md candidate), not a fix.
3. **Cadence established:** FLNG/CCEC now have a recurring MB LNG cross-check (rates + newbuild +
   the steam/modern split). Promotion remains human-only.

## Not done (owner-gated)
- No change to LNGC/MGC curve or LNG TC anchors (cross-check only). If the ~5% newbuild gap or the
  $85k-vs-$83k anchor is to be acted on, that is a deliberate per-class methodology decision (same
  bar as VIE), not a cross-check auto-update.
