# PLAN.md — operational handoff

Read CLAUDE.md, then this file. Operational work is now in **work_items.yaml**, projected
from domain authorities by `sh scripts/routine_task.sh tasks show`. It includes owner
rulings, agent work, armed triggers, fork windows, shadow blockers, quarterly follow-ups,
filing backlog and workflow-repair tasks. Do not duplicate live statuses in this file.

The old roadmap is retained in `decisions/workflow_migration_2026-09-22.md` as migration
provenance. TEN's Q2 landing and fork registration were already committed and are closed
in the operational view; TEN's remaining candidate gates are still governed separately.

## Current implementation

A5/A6/A9: quarterly duplicate guard installed first; calendar construction and timeline
alignment need the full-book comparison before activation; task status must use evidence.
Actual unattended quarterly smoke completion is required, not just static permission grants.
See `decisions/calendar_workflow_prereg_2026-09-22.md` and the implementation record.

## Authorities

- Valuation: METHODOLOGY.md, committed inputs, accepted-publication snapshots.
- Financial decisions: fork/trigger registers and governor cards/owner rulings.
- Filing queue: complete manifest minus acknowledged accession identities.
- Owner completion: governor reviews/completed_quarters.json with committed review evidence.
- Operational status: work_items.yaml; missing/conflicting evidence is UNKNOWN.
- Automation and ownership: graph.yaml and its rendered OPERATING.md.

The ordinary verification path remains isolated regeneration, producer tests,
reconciliation and drift checks. No portfolio decision or order is delegated by this work.
