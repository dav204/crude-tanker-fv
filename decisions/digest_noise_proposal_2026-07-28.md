# Digest signal/noise proposal — 2026-07-28 (owner: "how do we ensure stale flags stop cluttering the daily digest")

**Status: PROPOSED — owner sign-off wanted on the spec; implementation deliberately
POST-Q2-cluster (~week of 8/3) so a notifier regression can't land mid-earnings-week.**

## The diagnosis (today's digest as the specimen)

33 rows, of which ~6 carried decision-relevant signal. Four structural causes:

1. **Calendar recitation** — every EARNINGS-DUE row repeats its FULL multi-line basis
   verbatim daily for up to 14 days (13 rows today, mostly unchanged since the 7/21 sweep).
2. **Self-duplication** — EARNINGS-UNCONFIRMED re-lists names that already have an
   EARNINGS-DUE row (9 duplicate rows today).
3. **One-shot failures persist until the job's own next run** — FETCH-FAILED news-pull
   (a Saturday job) shows Saturday's error all week, even after the failing STEP
   (rocketchat-ingest) demonstrably recovered Monday.
4. **No new-vs-standing distinction** — a flag seen for the 6th consecutive day renders
   identically to one that fired this morning. The reader does the diffing by memory.

## The spec (four changes, each independently shippable)

1. **Three-section digest.**
   - `NEW / CHANGED` — flags appearing for the first time, or whose content materially
     changed since the previous digest. This is the section that pages attention.
   - `STANDING (n)` — unchanged flags compressed to one line each: tag, age, and a
     ≤80-char stub ("UNINGESTED-PRINTS marks-trail — 11d, unchanged"). Full text lives
     in the sentinel log, not the email.
   - `CALENDAR (next 14d)` — one line per name: "SB TONIGHT AC ✓ · TNK 7/29 AC ✓ ·
     CCEC 7/29 pre-open ✓ · …" with ✓=confirmed, ?=expected. Full basis renders only
     in NEW/CHANGED when a date confirms, moves, or a window opens.
   - Mechanism: persist the prior digest's flag set (id + content hash) in
     `state/sentinel_state.json` (file already exists); diff at assembly. Pure
     presentation change — flag DETECTION untouched, PAGE routing untouched.
2. **Merge EARNINGS-UNCONFIRMED into the name's EARNINGS-DUE row** as a suffix
   ("— UNCONFIRMED, sweep due"), one row per name.
3. **FETCH-FAILED recovery awareness** — if the automation ledger shows a later
   success of the same job OR of the failing step named in the error note, the flag
   renders in STANDING as "RECOVERED-PENDING-RERUN (next scheduled run <when>)"
   instead of a headline failure. A failure with no subsequent success stays NEW.
4. **Aging escalation** — STANDING items carry their age; anything unresolved past
   7 days is re-promoted to NEW/CHANGED once weekly (Mondays), so compression can't
   become burial. (Today's marks-trail 11d row is exactly the case this protects.)

## What this deliberately does NOT change

Flag detection logic, thresholds, PAGE-vs-digest routing (`inputs/notify.yaml`), the
dead-man ping, sentinel-lite. Noise is a RENDERING problem; the checks are correct.

## Guards at implementation

Unit tests for the differ (new / changed / standing classification), the
UNCONFIRMED-merge, the FETCH-FAILED downgrade rule (ledger-driven), and the 7-day
re-promotion; plus one golden-digest snapshot test so future edits to assembly are
diffed consciously.

**Decision (owner):** [ ] approve spec → implement post-cluster · [ ] amend · [ ] drop
