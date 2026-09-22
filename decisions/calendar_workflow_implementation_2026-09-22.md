# Calendar/workflow implementation — 2026-09-22

Scope: A5, A6, remaining A9. Scenario weights, cycle bands, payout rules, portfolio
rulings and orders are unchanged. VIE replacement remains a separate workstream.

## Calendar valuation and promotion

Dated month/quarter/year normalization replaces the September positional assumption.
Ambiguous years, conflicting quotes, missing required panels and invalid calculations
freeze. Quoted quarters take precedence. A remaining-month mean includes no next-quarter
month. Annual residuals preserve the quoted quarters and allocate integer remainders to
the earliest unquoted quarter. Ruled tail steps precede labelled flat carry-forward.
The 12M proxy identifies its actual two quoted quarters; Post-Panamax and Handy-Bulk
mapping/rounding and the independent Handy TC remain unchanged.

Live valuations export an explicit date, projection quarter, per-class source provenance,
sleeve horizons and derived scenario extensions. Fleet/coverage arrays have explicit
origins and fingerprints. An edited schedule without a reviewed calendar mapping blocks.
Historical scenario replay retains its explicit historical vintage. Sector horizons and
full-quarter/terminal discount conventions are unchanged. Weight-family freshness and
surface freshness now include the projection quarter, so an overnight rollover cannot
leave yesterday's quarter stamped current merely because Git did not change.

The preregistration and full-book comparison are separate committed records. September
replays exactly across all 25 names, including NAV, weighted FV, intervals, positions,
tiers, cycle values and sign stability. The October/January constant-source cases are
hypothetical sensitivity runs, not forecasts or accepted publications. They show nonzero
valuation effects and preserve all binding gates. See calendar_comparison_2026-09-22.md
and outputs/calendar_handoff_comparison_2026-09-22.json for all rows and family transitions.

## Operational status

work_items.yaml is an operational projection, not a financial determinant or replacement
acknowledgment ledger. Its adapters read committed forks/triggers, durable filing state,
structured shadow reports and governor events. Manual completion requires committed
cited evidence; missing, conflicting or stale evidence becomes UNKNOWN with a repair
item. Locked updates commit only the registry. The weekly report no longer infers shadow
status from narrative prose or uses an obsolete AUTOPILOT_LOG to infer authority.

The initial projection was inspected before notification activation: existing owner
restrictions remain visible, G-2 stays owner-blocked, G-3 stays agent repair, TEN Q2 and
fork registration are done from committed evidence, and TEN/TRMD candidate gates remain.
The filing queue still contains 100 pending accessions, oldest arrival July 14, with no
invalid records in the inspected snapshot. No accession was acknowledged by this change.
Between-review notifications compare stable conditions; the activation observation is
seeded from this inspected state, so it does not resend the already-known inventory.
Unresolved items remain in every weekly report. New conditions/transitions still notify.

Future shadow builds must commit a structured blocker sidecar with named resolver and
blocking decision IDs after their narrative report. Missing sidecars are unknown. The
canonical shadow/filing prompts are tracked and installed together. Persistent grants
are in the permission manifest and user/parent/repo settings, not prompt frontmatter.

## Quarterly execution

The guard was deployed first at governor 5e279dd. Q3 completion is sourced from the
September 21 owner-rulings review with a committed evidence hash. The real production
CLI returned skip_completed with no research, email or weekly healthcheck. Repeated skips
now have unique receipts. Prepared packs reuse their report and delivery queue; only an
explicit refresh creates a replacement. Recovery updates pack delivery state. Weekly and
quarterly active markers and healthcheck behavior are separate.

The permission manifest matches the installed user, Projects-folder and governor grants.
The task's actual configured folder is /Users/dan_personal/Projects. This establishes
configuration synchronization, not unattended acceptance.

**Open acceptance blocker: quarterly:scheduler-proof (resolver: agent).** The actual
scheduled smoke completed, and all five read-only IBKR calls succeeded without a prompt.
The application permission log, however, proves that its heredoc persistence call waited
11 minutes for a one-time Bash approval, despite the agent claiming no approvals. The
UI error did not mean no run had started. See the governor's committed
monitor/QUARTERLY_SMOKE_EVIDENCE_2026-09-22.md. Payloads now use a narrowly owned inbox
Write followed by a simple wrapper invocation with --probe-file/--report-file. A fresh
scheduled run plus permission-log inspection is required before closing this blocker.
The normal guarded prompt is restored after each probe; no real test email or order is sent.

## Validation and rollback

Focused calendar/registry/graph/prompt checks and governor tests use isolated artifacts.
The isolated end-to-end publication was accepted, generated 13 consumer events, recorded
an incomplete failed delivery, then completed after mocked retry. Both SMTP and healthcheck
transports were mocked. Reconciliation: 25 names, zero SANITY failures. Drift: 25 rows,
zero unexplained changes. Final suite totals are appended below after completion.

Pause the worker using state/operations/disabled before a calendar rollback. The prior
accepted snapshot and all receipts remain in their immutable stores; installation also
backs up the accepted pointer, machine state and installed prompts under
~/.config/fv-calendar-backups/20260922/. calendar_policy.yaml enabled:false holds October
promotion and restores legacy projection behavior; do not publish a legacy-quarter result
as a new live valuation. work_items.yaml integration_enabled:false stops task projection
updates/notifications while retaining the evidence and an explicit disabled report note.

### Final isolated validation

Clean source b19e343: regeneration and the full producer suite passed: **996 passed,
12 expected failures**, with one existing system LibreSSL warning (441.72 seconds).
Governor: **21 passed** with notification and healthcheck transports mocked. The 31
pre-existing per-name handoff fields match the prior production publication for all 25
names; calendar/provenance fields are additive. Source stamp b19e343 has no dirty suffix.
The final source includes commit-failure recovery, malformed-registry retention, unchanged
condition deduplication and recovery/recurrence notification tests.

The weekly prompt no longer duplicates old financial targets: it reads current cards,
CADENCE and recorded owner rulings, retaining conflicts as unknown. The permission manifest
was compared against user, Projects-folder, producer and governor settings: zero missing
grants in all four. This does not close quarterly:scheduler-proof.
