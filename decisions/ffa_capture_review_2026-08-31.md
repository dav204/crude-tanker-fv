# FFA OCR queue review — 2026-08-31 (digest UNINGESTED-PRINTS lane)

**Finding: the four flagged rows since the promoted 24-Aug print (8/25, 8/27, 8/28, 8/31)
are month-end STRUCTURE, not bad captures.** The 8/31 source image (reviewed at the
rendered PNG, per the by-hand rule) shows the widget now prints FOUR tenors per panel —
Sep / Q4 / Q1 / Cal27 — because the Aug month contract rolled off; the parser's 5-tenor
grid expectation (m1/m2/Qn/Qf/Cal) is what flags. The 8/31 row's table cells are also
column-scrambled by the alphabetical-sort artifact (the known 7/13 trap) — use the image
values below, not the queue row.

**Image-verified 2026-08-31 print (complete at the source's own 4-tenor structure):**
- Cape: Sep 45,250 · Q4 44,475 · Q1-27 30,125 · Cal27 33,300
- Pmax: Sep 21,900 · Q4 22,900 · Q1-27 18,200 · Cal27 18,175
- Smax: Sep 19,875 · Q4 20,933 · Q1-27 16,000 · Cal27 16,125

**Vs the ratified 24-Aug promote:** 12M proxies (Qn+Qf)/2 — Cape 37,300 (+5.3%), Pana
20,550 (+4.9%), Supra 18,467 (+4.3%); Cal27s +2.8/+1.8/+2.7%. The dry rally extends,
all legs sub-±10%.

**Disposition (no promotion — owner-run, and today's round already closed):** this is the
staged Rider-4 promotion candidate for the next owner round. At promotion: the 12M-proxy
mapping rule needs its month-end variant ruled (q1 = Sep alone with no m2 to mean — a
mapping note, not a judgment call to make silently), and the Handy-Bulk ×0.90 pair
re-derives with it (nearest-10 rounding — see the 8/31 correction). Parser follow-up
(non-blocking, backlog): teach ffa_ocr the month-end 4-tenor grid so it stops flagging
structurally-complete captures.
