# FFA forward curve vs synthesised dry-bulk strip

FFA legs: mean of the last 5 clean parsed days (2026-06-03 → 2026-06-11), `state/ffa_ocr_curves.json`.
Strip legs: Bulk Set A probability-weighted scenario MIDs (`sectors.dry_bulk`, weights china_acceleration 0.20, moderate_growth 0.40, china_property_drag 0.25, coordinated_slowdown 0.15).

Diagnostic only — see scripts/ffa_vs_strip.py header for caveats
(index vs earned-TCE premia, risk premium in the traded curve).

| Class | Tenor | FFA | Strip PW mid | Strip vs FFA | Nearest scenario |
|---|---|---|---|---|---|
| cape | q3 | $31,631 | $33,150 | +4.8% | moderate_growth ($35,000) |
| cape | q4 | $31,420 | $31,700 | +0.9% | moderate_growth ($33,000) |
| cape | cal27 | $26,505 | $27,800 | +4.9% | moderate_growth ($29,000) |
| pana | q3 | $20,788 | $19,300 | -7.2% | moderate_growth ($20,000) |
| pana | q4 | $19,500 | $18,750 | -3.8% | moderate_growth ($19,000) |
| pana | cal27 | $15,615 | $15,938 | +2.1% | moderate_growth ($15,750) |
| supra_ultra | q3 | $18,830 | $18,300 | -2.8% | moderate_growth ($18,500) |
| supra_ultra | q4 | $17,465 | $17,550 | +0.5% | moderate_growth ($17,500) |
| supra_ultra | cal27 | $13,592 | $14,862 | +9.3% | china_property_drag ($14,125) |

## Read

- **cape**: strip runs +3.5% vs the traded curve on average — market-consistent (±10%).
- **pana**: strip runs -3.0% vs the traded curve on average — market-consistent (±10%).
- **supra_ultra**: strip runs +2.3% vs the traded curve on average — market-consistent (±10%).

Curve shape (market statement for the Bulk Set A weight diagnostic):
- cape: Q3-26 $31,631 → Cal27 $26,505 (-16.2% — backwardated)
- pana: Q3-26 $20,788 → Cal27 $15,615 (-24.9% — backwardated)
- supra_ultra: Q3-26 $18,830 → Cal27 $13,592 (-27.8% — backwardated)
