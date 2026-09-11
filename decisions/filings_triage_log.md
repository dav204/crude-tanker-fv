# Filings triage log (append-only, one line per accession)

Started 2026-09-11. Every EDGAR / MFN arrival the sentinel flags (`FILING-LANDED`,
`FILING-UNREADABLE`) is dispositioned here by the daily triage task, and acked in the local
ledger `state/filings_triaged.json` (`python -m crude_tanker_fv.filings ack …`) so it stops
flagging. This file is the tracked record; the ledger is the operational ack. It is NOT a
per-name decision log, so the drift gate never reads it — a value-bearing filing still gets
its entry in `decisions/<ticker>_log.md` and this line points at it.

Dispositions: `record-only` (nothing to do), `calendar` (a date to seed), `print` (a
transaction print for the S&P queue), `refresh-trigger` (a balance-sheet / fleet event queued
for the next vintage), `unreadable` (image-only exhibit handled or judged not value-bearing),
`owner` (needs the owner — the only kind that pages).

| Triaged | Ticker | Accession | Filed | What it is | Disposition | Record |
|---|---|---|---|---|---|---|
| 2026-09-11 | CMBT | 0000919574-26-006196 | 2026-09-08 | SGM convening notice 8 Oct 2026 + "Publication Q3 2026 results – 26 November 2026" | calendar: seed CMBT 2026-11-26 at the Q3 re-seed; SGM record-only | decisions/cmbt_log.md 2026-09-10 |
| 2026-09-11 | SB | 0001317861-26-000044 | 2026-09-08 | Press release: contemplated private placement of common stock (the announcement) | record-only: superseded by 000045 (the completed placement) | decisions/sb_log.md 2026-09-10 |
| 2026-09-11 | SB | 0001317861-26-000045 | 2026-09-09 | Private placement completed: 12,000,000 shares at €6.70, €80.4M gross, settlement 11 Sep | refresh-trigger: share count + cash at the Q3 vintage (113,833,473 shares) | decisions/sb_log.md 2026-09-10 |
| 2026-09-11 | SB | 0001317861-26-000047 | 2026-09-10 | Results of the 2026 AGM: three Class III directors elected (Adamopoulos, Holth, Hajioannou); Deloitte ratified for FY2026 | record-only: governance routine, no capital or fleet action | this line |
| 2026-09-11 | OMC | mfn-4c2c88c8-0598-5d71-92fc-d70ad83ccc56 | 2026-09-10 | Financial calendar | calendar: annual report 2027-02-25 at the Q3 re-seed | PLAN.md (Q3 calendar re-seed item) |
| 2026-09-11 | BRUT | mfn-72ed759b-6d7d-467c-a5f6-9370e4b804c5 | 2026-09-10 | Ex cash distribution US$0.025 today on Euronext | record-only: the strip already carries the declared distribution; ex-date is not a valuation event | this line |
| 2026-09-11 | CAPT | mfn-e278809a-f124-40cb-bd60-916cc3c5b1af | 2026-09-10 | Ex dividend date | record-only: declared dividend already in the strip; ex-date is not a valuation event | this line |
| 2026-09-11 | CMBT | 0000919574-26-006193 | 2026-09-04 | H1-2026 half-year report; both exhibits staged as image-only shells | unreadable: 86 page images recovered by hand 2026-09-07; the Q2 pair landed 2026-09-10 | decisions/cmbt_q2_landing_2026-09-10.md |
| 2026-09-11 | CMDB | 0001140361-26-032939 | 2026-08-14 | Notice of the 2026 AGM (virtual, 8 Oct 2026 12:00 CET): elect one Class I director, ratify EY Hellas; ex99-2 is the proxy card (image-only) | unreadable: not value-bearing; nothing to recover | this line |
