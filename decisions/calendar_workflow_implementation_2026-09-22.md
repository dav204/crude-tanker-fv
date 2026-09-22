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

The baseline permission grants matched the installed user, Projects-folder and governor
settings. The additional inbox Write grant was explicitly approved and installed (see acceptance below).
The task's actual configured folder is /Users/dan_personal/Projects. This establishes
configuration synchronization, not unattended acceptance.

**Quarterly scheduler acceptance completed at 20:17:56 UTC.** The first real smoke
exposed an 11-minute heredoc approval wait that the agent's summary incorrectly denied.
After explicit owner approval, the narrowly scoped inbox grant was installed in all four
settings files. A fresh actual scheduled run used the inbox Write and simple file-argument
wrapper successfully in default/Manual mode, with no permission requests or mode changes
in the application log. Its five read-only broker calls and isolated persistence succeeded;
SMTP and healthchecks were disabled. The normal guarded quarterly prompt was restored.
Evidence: governor monitor/QUARTERLY_SMOKE_EVIDENCE_2026-09-22.md and
monitor/quarterly_acceptance_2026-09-22.json. Both permission and scheduler-proof work items
are now done; existing portfolio follow-ups remain open.

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
Governor before the inbox repair: **21 passed** with notification and healthcheck transports mocked. The 31
pre-existing per-name handoff fields match the prior production publication for all 25
names; calendar/provenance fields are additive. Source stamp b19e343 has no dirty suffix.
The final source includes commit-failure recovery, malformed-registry retention, unchanged
condition deduplication and recovery/recurrence notification tests.

The weekly prompt no longer duplicates old financial targets: it reads current cards,
CADENCE and recorded owner rulings, retaining conflicts as unknown. Before the inbox repair, the baseline permission manifest was compared against user,
Projects-folder, producer and governor settings: zero missing grants in all four. This does not close quarterly:scheduler-proof.

### Live rollout and permission finding

The first deployed calendar publication
`0befe36daca0bfab201f51aee58549f925d4981d3748f9ffaf09c0a4d1ae8551` was accepted and consumed
by the governor. Both delivery queues were empty and the worker observed zero changed
workflow conditions. The previous accepted snapshot remains retained. Q3's cited skip
was repeated at 19:44:38 UTC without SMTP or a weekly healthcheck.

The final reporting correction keeps missing-receipt and stalled-filing repairs in the
agent queue while withholding a clear-status claim. Source d53bb0b: clean regeneration
and **997 passed, 12 expected failures**, one inherited LibreSSL warning (324.27 seconds).
Governor scoped-payload tests: **23 passed**. Graph/prompt/document guards: **26 passed**.

Automatic approval review rejected the new inbox Write grant in four persistent settings
files, stating that this exact access expansion needs explicit approval. The new grant is
limited to `/Users/dan_personal/Projects/portfolio-governance/monitor/inbox/**`; no permission
change was applied by the rejected action. `quarterly:inbox-permission` records that owner
approval dependency, separately from the agent's remaining fresh-scheduler proof. The
normal installed guarded prompt remains available, so completed Q3 still skips before
research or payload persistence.

Latest deployed publication: `402b3fc5d56691b112824b24acac4c9970220f35cc01d7e141ff94efe92dc700`,
source `d53bb0bfc3a7404316d6a7dfac941f4c623ce7ee`, output
`20b357c8e886d63b8c15e2f9aa09180d2aa8f47a`. The governor consumed that exact ID; both
delivery queues were empty and the existing five-minute worker was active. This is local
publication/consumption evidence; no remote Git push is claimed. The current report preview
is `decisions/workflow_status_2026-09-22.md`; it is not a scheduled landing or a sent email.
At that initial rollout the inbox permission and revised prompts were still pending.
The subsequent approval and successful scheduled run below close that installation gap.

### Approved grant and observed unattended completion

At 20:14 UTC the owner-approved inbox Write grant was installed, with no other grants added.
The actual quarterly scheduler session `e7576ae7-ffed-4965-895a-d490828bf5c2` completed at
20:17:56 UTC in default/Manual mode. All five broker reads, one inbox Write and one scoped
Bash persistence command succeeded. Inspection of the application log found zero permission
requests and zero permission-mode changes for that session. Receipt
`2026-09-22T201738Z-531ea9bb29` records isolated committed persistence and disabled SMTP
and healthcheck transports. Canonical weekly/quarterly prompts and installed bodies match.
`quarterly:inbox-permission` and `quarterly:scheduler-proof` are done with committed evidence.
This verifies the quarterly path, not every other scheduled task or future credential state.
