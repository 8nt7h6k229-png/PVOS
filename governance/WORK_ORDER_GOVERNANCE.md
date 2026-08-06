# Work Order Governance

## Purpose

Define a Work Order as a bounded PM governance and Capability-coverage contract derived from approved planning.

## Responsibility

Maintain the unique Work Order content, traceability, review, and closing contract without acting as Codex's Execution Source.

## Information Domain

Work Orders

## Owner

PM

## Authority Boundary

- The approved Daily Planning Package is the daily Source of Truth.
- A Work Order records PM intent, scope, deliverables, evidence, acceptance, and governance coverage.
- A PM-authorised GitHub Issue is the sole Codex Execution Source.
- A Work Order becomes executable only after PM publishes a corresponding GitHub Issue containing the complete execution contract.
- Chat, document presence, priority, or Work Order status cannot directly dispatch Codex.

## Required Work Order Contract

| Field | Requirement |
|---|---|
| Work Order ID | Unique stable identifier |
| Title | Bounded governance outcome |
| Priority | PM-assigned execution priority |
| Owner | Accountable PM owner |
| Executor | Named executor; does not confer authority by itself |
| Planning Package | Approved source package ID and version |
| Capability Mapping | At least one valid EOS Capability ID |
| Repository Target | Existing authorised repository |
| Objective | One independent objective |
| Existing Assets | Assets that must be inspected first |
| Dependencies | Governed predecessor Work Orders or Issues |
| Scope | Explicitly authorised work |
| Out of Scope | Explicit prohibited expansion |
| Deliverables | Reviewable outputs |
| Acceptance Criteria | PM review conditions |
| Required Evidence | Durable evidence contract |
| Closing Rule | Executor stop state and accountable closing authority |
| Execution Issue | Corresponding GitHub repository and Issue number once published |

## Traceability Matrix

| From | Required Link | To |
|---|---|---|
| Daily Planning Package | Package ID and approval | Work Order |
| Work Order | Capability ID | EOS v1.0 Capability Matrix |
| Work Order | Repository and Issue number | GitHub Execution Queue |
| GitHub Issue | Work Order ID or package Queue identity | Work Order / Planning Package |
| Codex evidence | GitHub Issue number and Capability ID | Execution Source and capability |
| PM Review | Evidence and Work Order acceptance criteria | Review disposition |
| Handover | Work Order, Issue, evidence, and review states | Current governed continuity record |

Every Work Order must map to at least one Capability ID and exactly one current authorising GitHub Issue for a given execution attempt. Re-execution requires a new or explicitly re-authorised Issue state; it must not rely on stale chat context.

## Status Model

| Status | Meaning |
|---|---|
| DRAFT | PM preparation; not authorised for queue publication |
| APPROVED_FOR_PUBLICATION | Planning and Work Order content approved for Issue generation |
| QUEUED | Corresponding GitHub Issue exists and is `READY` |
| EXECUTION_ACTIVE | Codex is executing the authorising Issue |
| READY_FOR_PM_REVIEW | Required executor evidence has been returned |
| BLOCKED | Required dependency or authority is absent |
| REJECTED | Accountable review rejected the Work Order evidence or result |
| GOVERNANCE_CONFLICT | Governing requirements conflict and executor inference is prohibited |
| CLOSED | PM/Owner governed closing has been explicitly recorded |

The executor may advance only to `READY_FOR_PM_REVIEW` or a stop condition. `CLOSED` remains an accountable governance action.

## Publication Control

1. PM derives the Work Order from an approved Planning Package.
2. PM validates every required field and Capability mapping.
3. The PM GitHub Issue Builder publishes the full Issue contract.
4. PM verifies the Issue number and Queue order, then records `QUEUED`.
5. Codex verifies the GitHub Issue before execution.

Missing fields, missing Capability mapping, repository mismatch, or absent GitHub Issue stops publication or execution.

## Review and Closing Boundary

- Codex returns deliverables, verification, changed-file summary, Git state, and risks against the Issue and Work Order acceptance criteria.
- PM decides whether the evidence satisfies the Work Order.
- Owner review and Daily Governed Closing remain separate gates.
- Merge or Issue closure does not silently establish Daily Governed Closing.

## Update Trigger

The Work Order contract, traceability requirements, status model, publication gate, or closing authority changes.

## Related Documents

- [Planning Package Governance](PLANNING_PACKAGE_GOVERNANCE.md)
- [Execution Queue Governance](EXECUTION_QUEUE_GOVERNANCE.md)
- [PM GitHub Issue Builder](PM_GITHUB_ISSUE_BUILDER.md)
- [EOS v1.0 Capability Matrix](EOS_V1_CAPABILITY_MATRIX.md)
- [Handover Standard](HANDOVER_STANDARD.md)

## Status

Formal Work Order governance established — awaiting PM review.
