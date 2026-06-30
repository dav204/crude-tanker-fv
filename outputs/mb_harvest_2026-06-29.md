# MB Shipbrokers harvest + Thread-1A LR1 correction (2026-06-29)

## Harvest — all available MB reports pulled from the inbox

Before today the repo had only **Week 24/2026** (Container/Tanker/Dry Bulk; LNG had not
yet started). Searched Gmail (read-only) for all `*@mbshipbrokers.com` weeklies, harvested
the `cdn.flxml.eu` "Download report" links, fetched via `scripts/fetch_pdf.py`, archived
under `inputs/research_mb/<feed>/2026/` (gitignored broker cache, like the harvester PDFs).

**8 new reports archived — all 4 feeds now current through Week 26:**

| Feed | Wk 24 | Wk 25 | Wk 26 |
|---|---|---|---|
| Container | had | **+** | **+** |
| Tanker | had | **+** | **+** |
| Dry Bulk | had | **+** | **+** |
| **LNG** | (not subscribed) | **+ (1st issue)** | **+** |

The **LNG Weekly — the missing 4th feed — now arrives** (first issue Week 25, 2026-06-18;
the subscription confirmed mid-Week-24, so there is genuinely no Wk-24 LNG). FLNG/CCEC now
have a live MB LNG cross-check (previously only the stale Jan-2025 one-off).

All PDFs verified `%PDF`, 0.7–1.5 MB each. The email bodies are images (per CLAUDE.md); the
PDFs are the artifact. Promotion of any print/mark is HUMAN-ONLY (cross-check, not calibration).

## Thread-1A correction — MB DOES cover LR1 (my harvester-only sweep missed it)

My Thread-1A sweep covered the six `shipping_harvester` brokers, not the MB archive. The **MB
Tanker Weekly (current, 2026-06-26)** tabulates LR1 secondhand:

- **LR1 (ECO):** Newbuild ~**$64M**, 5-year ~**$58M** (the $58M aligns with the note's MB-LR1-5yr
  = 1.08× our fit). **No Resale (age-0) line** — MB gives NB + 5yr only, same as intermodal.
- **LR2 (ECO):** NB ~$79M / 5yr ~$82M (5yr > NB inversion, as the note flagged).
- **Handymax:** **absent** — MB's tanker class list is VLCC/Suezmax/Aframax/LR2/LR1/MR. No
  product-Handymax row anywhere. Confirms Handymax is the genuinely hard gap.

**Net effect on the Thread-1A registration:**
- LR1 is **broker-covered and current** (MB Tanker), correcting "only stale-2023 intermodal."
  BUT MB gives **NB + 5yr, not a Resale anchor**, so wiring LR1's **age-0 Resale** still needs a
  Resale derivation (a 5yr→Resale uplift) — a judgment, deferred. LR1 stays `pending-sourceable`.
- **Two discipline caveats before any LR1 wiring:** (1) MB is a **cross-check, not a calibration
  input** (CLAUDE.md, VIE discipline) — using it to *set* an age-0 mark is a methodology decision,
  not a casual update; (2) the value table is an image/column layout `pypdf` flattens — a
  label-verified read (OCR or `pdfplumber` w/ coordinates) is required, NOT an auto-parse, because
  a column/label mix-up is exactly the bug that caused the crude cascade.
- **Handymax** unchanged: no broker secondhand value table covers it (chem-tanker specialist needed).

## Owner follow-ups (none applied)
1. **LNG feed** now live — fold MB LNG into the FLNG/CCEC cross-check cadence.
2. **LR1 wiring** — if desired: decide MB-as-calibration (methodology), do a label-verified value
   read, derive the Resale anchor from NB/5yr. Then it can leave `pending-sourceable`.
3. **MB weekly cadence** — automate the Gmail harvest (interactive/authed session; not cron).
