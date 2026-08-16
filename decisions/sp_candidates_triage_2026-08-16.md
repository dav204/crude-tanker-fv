# S&P candidate triage — 2026-08-16 (2 candidates, scan window 8/10→8/13)

Review discharged per the FLEET-TRANSACTION flag ("review, promote/dismiss, then
`sp_scan --mark-reviewed`"). Dedup sweep run per the WORKFLOWS unnamed-print rule (the
8/09 four-duplicate lesson) BEFORE any disposition. Promotion itself is human-only;
what follows is one dismissal and one staged recommendation.

## 1. Suezmax — CMBT "Bristol" (2024-built, 156,851 dwt) — DISMISS from the fit queue, WATCH the price

- Pareto 8/11 sentence carries only the **gain** (~$57m, Q4). Primary source checked per the
  absence-isn't-evidence rule: CMB.TECH's own 2026-08-11 08:00 CET fleet update (GlobeNewswire
  3342412) discloses the ~$56.9m Q4 gain and Q4 delivery — **no sale price, no purchaser**.
  The staged 8/13 6-K (0000919574-26-005129) does not mention Bristol (it is the H1 filing).
- **No disclosed price ⇒ not promotable.** Back-solving price = book + gain is exactly the
  back-solve the §9.9 rule prohibits. A 2024-built suezmax print would be a rare near-age-0
  datapoint — worth having, not worth fabricating.
- WATCH: the price may surface at CMBT's Q2 announcement (8/27, earnings train) or the Q3/Q4
  report; the vessel exits the CMBT manifest at Q4 delivery (subsequent-events note first, per
  the snapshot rule). This retires the 8/13 archive-audit OPEN PRINT FLAG for Bristol.
- Context for the eventual print: CMBT 2026 tanker disposal gains now ~$620m incl. the Jun
  Brest/Brugge sister pair (+$100.5m) — the suezmax fit will want the whole cluster together.

## 2. Pana — two unnamed Kamsarmaxes (2019-built $38.2m / 2012-built $23.5m, "reportedly", Pareto 8/10) — RECOMMEND PROMOTE (owner round)

- **Dedup sweep CLEAN**: `transactions/pana.yaml` holds 2008/2010/2015/2016-built prints only —
  no 2019 or 2012 kamsarmax, no $38.2/23.5 figures, no same-pair phrasing. Not a re-report of
  anything on file.
- Per-vessel split disclosed (two prices, two build years) — passes the no-aggregate rule.
  In-window (8/10). Unnamed ⇒ carries the re-report risk forward: on promotion, note as
  unconfirmed/unnamed per the file's own convention, and the NEXT scan's dailies get the
  round-trip check.
- Both prints are FIRM vs Pareto generics ($38.2 vs $34.8; $23.5 vs $20.1 — ~+10%/+17%), with
  Pareto's own caveat that a Japanese-build premium "should probably be expected" — the 2025-09-19
  precedent priced that premium at ~10%, so these are consistent with firm-but-explainable, not
  anomalous.
- **Staged for the owner's next promotion round** (transactions edits are human-gated; a marks
  promotion is its own drift-gate event and does not belong inside week-close night). PLAN.md
  Monday sitting carries it.

## Mechanics

`sp_scan --mark-reviewed` advances `candidates_reviewed` 224 → 226 (the review is this record;
promotion pending ≠ review pending). FLEET-TRANSACTION flag clears.
