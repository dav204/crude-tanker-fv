# PLAN.md — current sprint plan (Week 5)

Rewritten at each Week close (CLAUDE.md "Week-close checklist"). This file
is the handoff: a new agent starting the sprint reads CLAUDE.md first,
then this. Week 4 closed 2026-06-12 — containerships shipped (§11.8
locked + wired, MPCC + GSL live, 19 names / 5 sectors / 274 tests,
calibration lock N/A-by-construction recorded honestly) and the §5
permission red-team ran in the first allowlist-active session (deny
rules enforce; ask tier is NOT testable in autonomous sessions — see
the CLAUDE.md 2026-06-12 Step-3 changelog entry).

## Week 5 theme: hardening + the event window — no new sector

Containers closed the last big sector with data in hand. Week 5 pays the
methodology debt the sprint accreted (B4–B6, owner-directed 2026-06-12),
processes the GNK deal events (AGM Jun-18 → tender deadline Jun-26), and
lands the FFA-OCR go/no-go. New-sector work (LPG, offshore) stays out
until a data corpus exists; the MB weeklies, when they start landing,
re-open the container anchor vintage and add cross-checks for the
existing sectors.

### Step 1 — B4: §9.9 mark-driven classification restated (half session)

The §6/§9.9 mark-driven taxonomy was written when k_broker meant "broker
premium over our independent curve" (pre the 2026-06-09 txn-anchored
default flip). k_broker now reads as the broker premium over TRANSACTION
levels (uniform ~1.12-1.14 on validated crude pure-plays). Restate the
classification language + thresholds against the post-default semantics
so "mark-driven" vs "mark-validated" is defined on the txn-anchored
baseline, not the retired one. No mark changes — language, thresholds,
and §6 entry wording only; re-pin any affected locked tests with
rationale.

### Step 2 — B5: anchor-basis commensurability (one session)

Live now because Container Set A's cycle anchors are FY21-25
calendar-average basis (the MB weekly table) while dry bulk's are
22-month archive medians and tanker/product anchors are TC-anchored
10-year means — three bases that don't numerically compose (same
discipline as the §10 TC-vs-spot rule). Build, per the owner brief:
an `anchor_basis` column in the cycle-anchor YAMLs; a
MIXED-ANCHOR-BASIS flag wherever a cross-sector pairing mixes bases
(delta report + reconcile surfaces); a §10 paragraph documenting the
non-composability. Tests for the flag.

### Step 3 — B6 [DECIDE-WITH-OWNER]: §9.2 terminal value (memo only)

Write the one-page options memo; the OWNER picks. Options to lay out:
keep 1.0× NAV at strip end / 0.9× mid-cycle discount / 1.1× structural
undersupply / cycle-position-conditional multiple. Evidence inputs:
`outputs/terminal_value_sensitivity.md` (TNK + STNG flip at 0.9×, FLNG
flips at 1.1×; other names multiple-robust) and the new containers 10q
horizon, which moves more weight onto the terminal. Deliverable = memo
+ recorded owner decision; implementation only if the decision changes
the convention.

### Step 4 — the event window (calendar-driven)

- **Sat Jun-13 + Jun-20**: weekly digests (`/news-pull` after the 08:00
  mechanical chain). Tripwires armed across TEN/CMDB/CAPT/TNK/CCEC.
- **Jun-18 GNK AGM**: morning-after read is pre-planned in gnk_log.
- **Jun-26 tender deadline**: on lapse, GNK price re-anchors, the
  deal-arb framing comes OFF, and EV/position reads revert to
  NAV-discount signals — annotate gnk_log either way.
- **FFA-OCR decision (carried from Week 4)**: owner reviews the 16
  flagged queue days (~10 min human pass), then record the
  diagnostic-cycle decision — does the FFA curve stay diagnostic or
  start informing the dry-bulk strip? Stage 2 (2020-2026 backfill)
  rides on this.

### Step 5 — small carry items

- **§5 ask-tier verification, INTERACTIVE session required**: confirm
  git push / watchlist-edit / fetch_links / curl actually PROMPT when a
  human is at the keyboard. The 2026-06-12 autonomous session proved
  deny rules enforce but could not test prompts (ask-class auto-approves
  under the autonomous permission mode).
- **fetch_links argparse**: it silently ignores unknown flags (`--help`
  ran a real download pass on 2026-06-12 — harmless, dedupe held, but
  wrong interface behaviour for an ask-gated network module). Tiny fix.

### Q2-refresh carry-forwards (parked until reports land; the earnings
calendar + preflight §0 drive the timing)

- **MPCC (reports 2026-08-26, confirmed)**: replace cohort built-year
  ESTIMATES + NB delivery quarters with the issuer fleet list; watch
  Q2-26 6-Ks for clean per-vessel prices on the three handed-over sale
  prints (§11.8.5(b) ledger row); refresh the company-implied NAV
  anchor if restated.
- **GSL (Aug-04/06 expected)**: Series B preferred count post-ATM (the
  $109M pref deduction is the sensitive input); the Jun-26 $917M NB
  order's charter attachments — undisclosed charterers are a
  dimension-6 tripwire; 20-F Item 6 board-rights verify.
- **TEN (SEPTEMBER, H1 reporter)**: TCM fee-load computation (§15
  calibration anchor due at Q2 data); ten_log Q2-vintage kit deltas
  (Ulysses sale, Sola TS step-up, charter rolls) get applied at this
  refresh, not before.
- **CMDB**: watch for the Astros sale price — clean age-8 Ultramax
  print if disclosed per-vessel.

## Standing threads (not Week 5 step work)

- **MB Shipbrokers weeklies — subscription pending first delivery.**
  Dan signed up 2026-06-11 for all four (Container / Dry Bulk / LNG /
  Tanker). **Dan will say when they land.** Until then the container
  anchor vintage stays frozen at 2026-04-01 (§11.8.5(a), LIMITATIONS
  §3). On first delivery: ingest route TBD (Gmail is read-only via
  sanctioned API per guardrails); the three non-container weeklies are
  fresh independent cross-checks for EXISTING sectors — run a once-over
  against current anchors when they arrive.
- **OWNER ACTIONS pending (re-flagged at Week 4 close):** detach the
  brokerage MCP connector from this project — order-writing surfaces
  were STILL reachable in the 2026-06-12 Step-3 session (PR #2 §6 Q4
  decision; run /mcp to locate the scope); optionally same for Gmail.
  Ratify-or-revise the A1 horizon interpretation (wired as 10 strip
  quarters = end-2028; the brief said "~12q from report date").
- **Hormuz weight revisit trigger** — standing; preempts everything if
  physical-transit confirmation lands.
- **Deferred by owner**: orchestration of the /news-pull agent half
  (scheduled cloud agent); Task-3 weight adjuster; demand-destruction
  overlay; FFA Stage 2 (pending the Step-4 decision).

## Definition of done (Week 5)

B4 + B5 shipped with tests (suite grows from 274); B6 memo written and
the owner decision recorded; GNK AGM + tender outcomes processed and
logged; FFA-OCR diagnostic decision recorded; both weekly digests run;
§5 ask-tier verified interactively; Week-close checklist run (docs
audited, Appendix A entry, PLAN.md rewritten for Week 6); clean git
state + push.
