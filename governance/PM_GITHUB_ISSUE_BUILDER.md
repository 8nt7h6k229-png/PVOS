# PM GitHub Issue Builder

## Purpose

Convert one approved Daily Planning Package into a validated, ordered GitHub Issue Execution Queue.

## Responsibility

Maintain the unique input contract and publication control for PM-generated daily Issue queues.

## Information Domain

Work Orders

## Owner

PM

## Input Contract

The builder accepts one UTF-8 JSON document with:

- `package_id` — unique Daily Planning Package identifier;
- `date` — package date in `YYYY-MM-DD` form;
- `status` — must be `APPROVED`;
- `approved_by` — accountable approver;
- `repository` — target in `owner/name` form; and
- `issues` — one or more ordered Issue definitions.

Every Issue definition requires:

- `issue_id`;
- `title`;
- `capability_ids`;
- `objective`;
- `scope`;
- `out_of_scope`;
- `deliverables`;
- `acceptance_criteria`;
- `required_evidence`;
- `dependencies`; and
- `status`, which must be `READY`.

Dependencies reference earlier `issue_id` values in the same package. This preserves publication order and prevents unresolved forward dispatch.

## Validation Gate

The entire package is validated before the first GitHub mutation. Publication stops when:

- the package is not approved;
- a mandatory field is absent or empty;
- an Issue ID is duplicated;
- a dependency is missing, self-referential, or ordered after its dependent Issue;
- an Issue status is not `READY`; or
- the target repository is malformed or conflicts with the command-line repository.

Validation failure publishes zero Issues.

## Batch Publication Flow

```text
Approved Daily Planning Package JSON
    ↓
Full-package validation
    ↓
Ordered Issue rendering
    ↓
GitHub API batch publication
    ↓
Queue Ready JSON summary
    ↓
Codex reads each GitHub Issue as its sole Execution Source
```

The builder invokes the authenticated GitHub CLI API. `--publish` is mandatory for mutation; without it the builder performs a dry run.

Before each mutation, the builder searches the target repository for the package `Issue ID`. A retry reuses exactly one matching Issue and stops if duplicate matches make queue identity ambiguous.

## Usage

```text
python governance/issue_builder/pm_issue_builder.py PACKAGE.json
python governance/issue_builder/pm_issue_builder.py PACKAGE.json --publish --output queue-ready.json
```

Dry-run output contains rendered Issue titles and bodies without Issue numbers. Published output contains Issue numbers and URLs in queue order.

## Queue Ready Output

The output JSON contains:

- package and repository identity;
- `DRY_RUN` or `QUEUE_READY` status;
- ordered Issue ID, number, title, URL, Capability IDs, and resolved dependencies; and
- concise console lines suitable for PM review.

## Failure Boundary

Validation is atomic; publication is not. A GitHub API failure after publication begins may leave a partial queue. The builder stops immediately, reports already-created Issues, and does not delete or close them automatically.

## Verification

- Unit tests cover approved input, required-field rejection, unapproved input, duplicate IDs, dependency ordering, rendering, dry run, and mocked batch publication.
- Unit tests also cover idempotent retry using an existing Issue ID.
- A demonstration package provides a two-Issue ordered queue.
- A live demonstration must use explicitly labeled demonstration Issues and retain their URLs as evidence.

## Related Documents

- [Execution Queue Governance](EXECUTION_QUEUE_GOVERNANCE.md)
- [Governance Information Architecture](GOVERNANCE_INFORMATION_ARCHITECTURE.md)
- [EOS v1.0 Capability Matrix](EOS_V1_CAPABILITY_MATRIX.md)

## Status

Implemented by [GitHub Issue #33](https://github.com/8nt7h6k229-png/PVOS/issues/33) — awaiting PM review.
