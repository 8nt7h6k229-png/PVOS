# Planning Package Governance

## Purpose

Define the Daily Planning Package as the approved daily Source of Truth for bounded EOS work.

## Responsibility

Maintain the unique planning authority, mandatory input contract, queue-order commitment, and publication gate for each governed day.

## Information Domain

Planning

## Owner

PM

## Authority Boundary

- The Owner-approved Daily Planning Package is the daily Source of Truth.
- PM owns package preparation, validation, prioritisation, and Issue Queue publication.
- A Planning Package authorises PM to construct the Queue; it does not directly authorise Codex execution.
- Only a PM-authorised GitHub Issue in the published Queue is Codex's Execution Source.
- Chat, a Work Order, local files, or an unpublished package cannot substitute for that GitHub Issue.

## Package Contract

| Field | Requirement |
|---|---|
| Package ID | Unique daily package identifier |
| Date | Governed work date in `YYYY-MM-DD` form |
| Status | Must be `APPROVED` before publication |
| Approved By | Accountable Owner identity |
| Objective | One bounded daily outcome |
| Repository | Existing target in `owner/name` form |
| Issue Queue | One or more ordered Issue definitions |
| Execution Policy | Source of Truth, Execution Source, and execution mode |
| Stop Conditions | At minimum: Blocked, Rejected, Governance Conflict |
| Daily Success Criteria | Conditions for PM Deliverable, Owner Review, and Daily Governed Closing |

## Issue Definition Contract

Every planned Issue contains:

- unique Issue ID and title;
- one or more EOS Capability IDs;
- objective;
- dependencies referring only to earlier Queue items;
- scope and out-of-scope boundaries;
- deliverables;
- acceptance criteria;
- required evidence; and
- `READY` queue status.

## Approval Gate

1. PM prepares the complete package from current handover, governance rules, Capability Matrix, decisions, evidence, and approved Blueprint references.
2. Owner approval changes the package status to `APPROVED`.
3. Any missing mandatory field, unresolved duplicate, forward dependency, or non-approved status stops publication.
4. The PM GitHub Issue Builder validates the full package before the first GitHub mutation.
5. Successful publication returns a Queue Ready record with ordered Issue numbers and URLs.

An approval applies only to the recorded package version. A material change requires renewed accountable approval and a new traceable package version.

## Execution Policy

```text
Approved Daily Planning Package (daily Source of Truth)
    ↓
Published GitHub Issue Queue
    ↓
One GitHub Issue (sole Codex Execution Source)
    ↓
Codex evidence
    ↓
PM Review
```

`One-Pass Execution` means Codex proceeds through the ordered Queue while each predecessor reaches its authorised review boundary and no stop condition exists. It does not bypass dependencies, PM Review, Owner Review, or Daily Governed Closing.

## Stop Conditions

| Condition | Required response |
|---|---|
| Blocked | Stop the dependent Queue and report the missing dependency or authority |
| Rejected | Stop the dependent Queue and preserve the rejecting authority and evidence |
| Governance Conflict | Stop executor inference and request PM/Owner resolution |

## Daily Success Criteria

The Daily Planning Package reaches its execution success boundary only when:

1. all planned GitHub Issues exist in the published Queue;
2. every Issue is `READY_FOR_PM_REVIEW` or has an explicit stop condition;
3. PM prepares the governed PM Deliverable;
4. Owner Review is recorded; and
5. Daily Governed Closing is explicitly recorded.

Codex may satisfy executor deliverables but may not declare criteria 3–5 complete.

## Current Approved Example

- Package: `DPP-2026-08-06-EOS-V1-FOUNDATION`
- Input: `issue_builder/packages/2026-08-06_daily_planning_package.json`
- Queue Ready evidence: `issue_builder/packages/2026-08-06_issue_queue_ready.json`
- Published Queue: GitHub Issues #36 through #44.

## Update Trigger

The planning authority, package contract, approval gate, publication validation, stop conditions, or daily success criteria changes.

## Related Documents

- [PM GitHub Issue Builder](PM_GITHUB_ISSUE_BUILDER.md)
- [Execution Queue Governance](EXECUTION_QUEUE_GOVERNANCE.md)
- [EOS v1.0 Capability Matrix](EOS_V1_CAPABILITY_MATRIX.md)
- [AIStudioCore Handover](AISTUDIOCORE_HANDOVER.md)

## Status

Formal Planning Package governance established — awaiting PM review.
