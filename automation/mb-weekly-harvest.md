---
name: crude-fv-mb-weekly-harvest
description: Saturday 08:30: harvest the four MB Shipbrokers weekly PDFs (Container / Tanker / Dry Bulk / LNG) from Gmail into inputs/research_mb/ via the repo's mb_harvest.py — the "agent half" of WORKFLOWS.md §MB, previously done by hand.
---

You are running the weekly MB Shipbrokers harvest for the repo at /Users/dan_personal/Projects/crude-tanker-fv. This is the "agent half" described in WORKFLOWS.md under the MB feeds section; the mechanical half is scripts/mb_harvest.py. Do it exactly as follows, read-only in Gmail, and never send, reply, label, or trash anything.

1. Use the Gmail connector: search_threads with query `from:mbshipbrokers.com newer_than:10d`. Four feeds arrive Thursdays/Fridays: subjects "MB Shipbrokers | Container Weekly N, YYYY", "… Tanker Weekly N, YYYY", "… Dry Bulk Weekly N, YYYY", "… LNG Carrier Weekly N, YYYY".

2. For each matching thread, call get_thread with messageFormat PLAIN_TEXT. In the plaintext body, the "Download report" button is the FIRST link of the form https://cdn.flxml.eu/lt-<digits>-<hex> that appears right after the words "Click below to open/download the report". The later lt- links are sign-up / privacy / LinkedIn — do not use those. Take the message date (YYYY-MM-DD, from the `date` field) and the exact subject.

3. Write a TSV to /Users/dan_personal/Projects/crude-tanker-fv/state/mb_links.tsv with one line per report: `<YYYY-MM-DD>\t<subject>\t<download url>` (tab-separated, no header).

4. From the repo root run:
   sh /Users/dan_personal/Projects/crude-tanker-fv/scripts/routine_task.sh mb /Users/dan_personal/Projects/crude-tanker-fv/state/mb_links.tsv
   It fetches each link via scripts/fetch_pdf.py, validates the %PDF magic, and archives under inputs/research_mb/<feed>/<YYYY>/ with the repo's naming (e.g. 2026-09-04_Tanker_Weekly_36_2026.pdf). It is idempotent and skips files already archived, so re-running is safe. Use the .venv interpreter only (Python 3.9); never bare pytest, never the .venv310 interpreter.

5. Run the local independent-source scan:
   sh /Users/dan_personal/Projects/crude-tanker-fv/scripts/routine_task.sh vie run
   This archives extraction receipts and a durable review queue in state/vie_exit. A blocked FFA procurement is an expected research hold, not a failed report download. Review candidate records against their cited PDF pages; do not promote financial inputs.

6. Verify: list inputs/research_mb/*/2026/ and confirm each of the four feeds has a file dated within the last 10 days. Then run
   sh /Users/dan_personal/Projects/crude-tanker-fv/scripts/routine_task.sh sentinel
   and confirm no STALE-INPUT mb:* flag remains (the sentinel's exit code 2 just means other flags exist — read the text). The archive directory is gitignored; do not commit anything.

7. Report in a few lines: which weeks were harvested (feed, week number, date, bytes), anything skipped as already present, and any feed that had no email in the window (say so plainly — a missing feed is a finding, not a failure to hide). If a download returns something that is not a PDF, report the URL and the first bytes; do not retry more than twice.

Only the documented wrappers may write their owned archive and state paths. Do not run the pipeline, promote, or ingest anything — reading and promoting the new issues is a separate, human-gated step.
Persistent execution rules (2026-09-22): the user/working-folder settings grant the documented routine operations even in Manual mode. Frontmatter does not grant permissions. Use the exact documented commands and owned paths. A denied operation is a workflow defect; never broaden scope or change permission mode to get around it.
