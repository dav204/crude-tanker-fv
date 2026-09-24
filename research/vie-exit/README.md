# VIE exit trial operations

Read PREREGISTRATION.md before comparing valuations. Source selection, production
activation and cancellation require owner review. This directory contains no
licensed PDFs or credentials.

Commands from the producer root:

```
sh scripts/routine_task.sh vie run
sh scripts/routine_task.sh vie report
```

`run` is local-only, locked and restartable. The existing five-minute delivery
worker calls it with `--if-due` once per 24h; the weekly independent harvester and
MB task call it after new reports arrive. It writes only state/vie_exit. A
procurement hold exits zero as an intentional research hold; a failed stage exits
nonzero and stays visible in receipts and the operational registry. No extra mail
is sent. Existing registry delivery deduplicates unchanged operational conditions.

`state/vie_exit/documents.json` is the complete durable queue, not a display-limited
view. Each PDF hash has source appearances, cited page candidates, extraction
warnings, pending status and committed disposition evidence. Read original pages
before deciding absent fields. Raw text scanning is partial extraction, not a
validated table parser. All new documents require visual/table triage. Record
vessel/event identity before counting a repeated candidate as independent evidence.
Disposition then acknowledgment:

```
sh scripts/routine_task.sh vie ack DOCUMENT_SHA256 decisions/DISPOSITION.md
```

The committed disposition must contain the exact document hash. Acknowledgment
closes only that document. It does not promote a transaction or financial input.
Changed PDF bytes create a new pending record; old unacknowledged PDFs never expire.

Normalized curve JSON is version 1. See tests/test_vie_trial.py for a synthetic
example. Actual provider-specific retrieval and export mapping must be implemented
from the contracted sample, not guessed from an API name. The import seam validates
raw hash, benchmark evidence, dates, quote convention and full panel coverage:

```
sh scripts/routine_task.sh vie import-record state/PROVIDER_RECORD.json
```

Original OCR captures preserve unknown benchmark/time fields and cannot pass as a
matched replacement. Attestation must cite original provider evidence; do not fill
unknown timestamps from filename time. The trial's provider, holiday calendar,
contracts and start date remain unset until confirmation. Conflicting same-time
revisions remain blocked pending an explicit reviewed resolution. Day receipts
measure source completeness only, not equivalence or final adoption.

Rollback: set research/vie-exit/trial.json enabled=false. Keep all records and the
previous accepted publication. This does not disable the delivery worker itself.
Installed MB prompt of record: automation/mb-weekly-harvest.md. Existing scoped
routine_task.sh permission covers the new local command; no shell wildcard or
permission-mode change is required. A successful manual run is not unattended proof.
