# Routine execution and persistent permissions

2026-09-22: scheduled tasks were repeatedly parking on approvals even after the owner selected Auto.
The installed prompts used discarded `allowed-tools` frontmatter, and local settings contained exact
approvals for dated commands rather than their stable entrypoints. The governor task's working folder
was the parent Projects directory, so repository-local permissions alone did not cover it.

The shipped permission manifest covers producer/governor reads, routine draft/report writes, scoped
wrappers, existing specifically authorized maintenance modules, issuer source domains and read-only
broker/Gmail tools. It adds no live-order submission, generic shell, credential-read or bypass grant.
Apply additively to user settings and Projects settings, preserving existing deny/ask rules and other
projects' configuration. Exact absolute wrapper paths prevent cwd ambiguity. Installer backups are
outside both repos; never copy credential/config contents into a tracked report.

Canonical source: https://code.claude.com/docs/en/desktop-scheduled-tasks (checked 2026-09-22).
The task's permission mode belongs to the Desktop task configuration, not SKILL.md. User settings allow
rules apply to scheduled sessions. In Manual mode an unapproved action waits; tools marked
requiresUserInteraction can still require approval on every invocation. File-level and shell grants
cannot remove that connector behavior. Do not claim that a static allowlist inspection proves a future
scheduled run completed. Verify the next actual run receipt and parked-task monitor.

Prompt bodies can be edited at ~/.claude/scheduled-tasks/<name>/SKILL.md and apply on the next run.
The weekly governor and filing triage use one constrained landing command for routine persistence.
The native five-minute worker handles deterministic handoff and delivery independently of Claude's
permission-mode selection. It catches up after wake; the Mac must be awake for local work to execute.

Activation checks: shadow publication/checker result reviewed; full tests and graph checks recorded;
permissions installed additively; tracked/installed prompt bodies match; worker launchd label loaded;
worker receipt and backlog visible. Rollback: create state/operations/disabled, unload the worker if
needed, and restore the backed-up permission/prompt files. Preserve all outboxes and publication data.
