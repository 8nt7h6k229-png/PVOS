# Handover Standard

## Purpose

Define the required structure of governed handover records.

## Responsibility

Maintain the unique handover content and evidence standard.

## Information Domain

Handover

## Owner

PM

## Update Trigger

The required handover structure or evidence fields change.

## Required Handover Contract

Every governed handover record contains:

| Field | Requirement |
|---|---|
| Handover ID | Unique stable identifier |
| Version | Version conforming to `HANDOVER_VERSION_POLICY.md` |
| Status | Current state from `HANDOVER_LIFECYCLE.md` |
| Owner | Accountable PM owner |
| Effective Snapshot | Date and time boundary represented by the record |
| Planning Package | Approved daily Source of Truth |
| Execution Queue | Ordered GitHub Issues and dependencies |
| Capability Coverage | EOS Capability IDs affected by current work |
| Repository State | Repository, branch, commit, and Pull Request evidence |
| Completed Execution | Items at `READY_FOR_PM_REVIEW` or later, without implying governed closing |
| Active and Pending Work | Current item, next item, and dependency state |
| Decisions | Related registered decisions or explicit `None registered` |
| Evidence | Durable links or repository paths supporting every status claim |
| Gaps and Risks | Missing, rejected, uncertain, or conflicting information |
| Stop Conditions | `Blocked`, `Rejected`, or `Governance Conflict`, when present |
| Next Accountable Action | Actor, action, and entry condition |
| Closing State | PM Deliverable, Owner Review, and Daily Governed Closing status |

## Evidence Standard

- A status claim must cite a GitHub Issue, commit, Pull Request, governed repository path, test result, or accountable review record.
- Chat text and tool-local state may provide working context but are not durable evidence by themselves.
- Missing evidence is recorded as a gap; it is not replaced by inference.
- `Completed` execution means the executor deliverable reached its acceptance boundary. It does not mean PM approval, Owner approval, merge, Issue closing, or Daily Governed Closing.

## Responsibility Boundaries

| Actor | Responsibility |
|---|---|
| Codex | Prepare the record and execution evidence; stop at the Issue-authorized review state |
| PM | Validate evidence, prepare the PM Deliverable, and control review-state transitions |
| Owner | Accept, reject, or return the PM Deliverable |
| Daily Governed Closing authority | Close only after the approved prerequisites are evidenced |

## Conformance

A handover conforms only when all required fields are present, links resolve, its version is unique, and its lifecycle transition is permitted. Nonconformance is reported as a governance gap and does not silently advance state.

## Related Documents

- [Evidence Governance](EVIDENCE_GOVERNANCE.md)
- [Handover Version Policy](HANDOVER_VERSION_POLICY.md)
- [Handover Lifecycle](HANDOVER_LIFECYCLE.md)
- [AIStudioCore Handover](AISTUDIOCORE_HANDOVER.md)
- [Governance Information Architecture](GOVERNANCE_INFORMATION_ARCHITECTURE.md)

## Status

Formal handover content and evidence standard established — awaiting PM review.
