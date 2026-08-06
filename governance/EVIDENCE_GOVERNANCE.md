# Evidence Governance

## Purpose

Define durable, traceable evidence for governed claims, execution, decisions, reviews, acceptance, and closing.

## Responsibility

Maintain the unique evidence identity, provenance, linkage, validation, review-status, and retention contract.

## Information Domain

Evidence

## Owner

PM

## Evidence Record Contract

| Field | Requirement |
|---|---|
| Evidence ID | Unique stable identifier |
| Evidence Type | Repository State, Change, Test, Runtime, Decision, Review, Approval, Gap, or Closing |
| Claim | Exact assertion supported or challenged |
| Source | Authoritative repository path, URL, commit, PR, Issue, or review record |
| Provenance | Producer, method, timestamp or governed snapshot boundary |
| Repository | `owner/name` when repository evidence is used |
| Git Reference | Branch, immutable commit SHA, tag, or explicit `Not applicable` |
| Execution Issue | Authorising GitHub Issue number |
| Capability IDs | One or more affected EOS Capability IDs |
| Work Order / Package | Related governance record, when applicable |
| Verification Method | Deterministic check, inspection, comparison, or accountable review |
| Verification Result | Observed result, including failure details |
| Executor Status | Captured, Validated, Failed, or Gap |
| PM Review Status | Pending, Accepted, Rejected, or Superseded |
| Related Decisions | Qualified Decision IDs or `None registered` |
| Retention Reference | Durable location or Git-history preservation method |

## Evidence Types

| Type | Examples | Minimum authority |
|---|---|---|
| Repository State | branch, commit, tree, diff, file inventory | Git/GitHub record |
| Change | changed-file list, patch, commit | immutable commit or reviewable diff |
| Test | command, environment, count, pass/fail output | reproducible test result |
| Runtime | deterministic execution output | identified input, version, and method |
| Decision | registered decision source and status | Architecture Decision Registry or accountable decision record |
| Review | PM or Owner disposition | identified reviewer and record |
| Approval | explicit accountable approval | durable approval record |
| Gap | missing, conflicting, or unverifiable evidence | inspected sources and stated uncertainty |
| Closing | PM Deliverable, Owner Review, Daily Closing | explicit accountable closing record |

## Status Model

| Status | Meaning | Who may establish it |
|---|---|---|
| Captured | Evidence source and claim are recorded | Producer / Codex |
| Validated | Stated verification method passed | Verifier / Codex |
| Failed | Verification method did not pass | Verifier / Codex |
| Gap | Required evidence is absent, ambiguous, or conflicting | Inspector / Codex / PM |
| Pending | Awaiting accountable PM review | System / PM |
| Accepted | PM accepts evidence for the stated claim and review boundary | PM |
| Rejected | PM rejects evidence for the stated claim | PM |
| Superseded | A later accepted record replaces its governed use; history remains | PM |

Codex may report `Captured`, `Validated`, `Failed`, or `Gap`. Codex must not assign PM `Accepted`, `Rejected`, or `Superseded` status.

## Minimum READY_FOR_PM_REVIEW Evidence

Every executor submission includes:

1. authorising GitHub Issue and Capability IDs;
2. Existing Asset Inspection Report;
3. created, updated, reused, and unchanged asset summary as applicable;
4. verification methods, commands or review procedure, and observed results;
5. Git working tree, branch, commit, and Pull Request state as applicable;
6. acceptance-criteria evaluation;
7. known risks, evidence gaps, and active stop conditions; and
8. explicit executor status limited to `READY_FOR_PM_REVIEW`, `BLOCKED`, `REJECTED`, or `GOVERNANCE_CONFLICT` as authorised.

Missing minimum evidence prevents a complete PM review package. It does not silently satisfy acceptance.

## Execution-to-Review Flow

```text
GitHub Issue
    ↓
Codex produces and validates evidence
    ↓
Evidence records link Issue + Capability + repository state
    ↓
READY_FOR_PM_REVIEW
    ↓
PM accepts, rejects, or requests additional evidence
```

## Integrity Rules

- Evidence must support the exact claim stated; proximity is not proof.
- Branch-only, draft, historical, and untracked sources retain those classifications.
- A mutable branch name alone is insufficient when an immutable commit can be recorded.
- Failed tests and conflicting observations remain visible.
- Evidence is never fabricated, backdated, silently overwritten, or self-approved.
- History is preserved when a record is corrected or superseded.

## Retention

Repository evidence is retained through Git history and review records. External evidence must use a durable reference and record access limitations. Local-only output is working evidence until persisted or attached to an authorised GitHub record.

## Update Trigger

The evidence schema, status authority, minimum PM-review package, integrity rules, or retention requirements change.

## Related Documents

- [Engineering Knowledge Governance](ENGINEERING_KNOWLEDGE_GOVERNANCE.md)
- [Execution Queue Governance](EXECUTION_QUEUE_GOVERNANCE.md)
- [Work Order Governance](WORK_ORDER_GOVERNANCE.md)
- [Handover Standard](HANDOVER_STANDARD.md)
- [Architecture Decision Registry](ARCHITECTURE_DECISION_REGISTRY.md)
- [EOS v1.0 Capability Matrix](EOS_V1_CAPABILITY_MATRIX.md)

## Status

Formal evidence governance established — awaiting PM review.
