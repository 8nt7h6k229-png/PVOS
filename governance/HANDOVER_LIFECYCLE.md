# Handover Lifecycle

## Purpose

Define the governed states and transitions of a handover record.

## Responsibility

Maintain the unique handover lifecycle definition.

## Information Domain

Handover

## Owner

PM

## Update Trigger

A handover state, transition, review gate, or closing condition changes.

## Lifecycle States

| State | Meaning | Accountable Actor |
|---|---|---|
| EXECUTION_ACTIVE | Authorized Issue Queue execution is in progress | Codex under PM authorization |
| READY_FOR_PM_REVIEW | Required executor evidence is available; no approval or closing is implied | PM |
| PM_DELIVERABLE_READY | PM has reviewed execution evidence and prepared the governed deliverable | PM |
| OWNER_REVIEW | PM Deliverable is presented for Owner decision | Owner |
| DAILY_CLOSING_READY | Owner review is accepted and closing prerequisites are evidenced | PM / closing authority |
| CLOSED | Daily Governed Closing has been explicitly recorded | Closing authority |
| BLOCKED | Work cannot proceed because a required dependency or authority is absent | PM disposition required |
| REJECTED | Accountable review rejected the evidence or deliverable | Rejecting authority |
| GOVERNANCE_CONFLICT | Two governing requirements conflict and executor inference is prohibited | Owner / PM resolution required |

## Permitted Mainline

```text
EXECUTION_ACTIVE
    ↓
READY_FOR_PM_REVIEW
    ↓
PM_DELIVERABLE_READY
    ↓
OWNER_REVIEW
    ↓
DAILY_CLOSING_READY
    ↓
CLOSED
```

This lifecycle records the approved governance state sequence. It does not alter the Operating Cycle.

## Transition Gates

| Transition | Minimum evidence |
|---|---|
| EXECUTION_ACTIVE → READY_FOR_PM_REVIEW | Issue-required deliverables, verification, changed-file summary, Git state, and known risks |
| READY_FOR_PM_REVIEW → PM_DELIVERABLE_READY | PM evidence review and explicit PM deliverable record |
| PM_DELIVERABLE_READY → OWNER_REVIEW | PM submission to Owner with unresolved gaps visible |
| OWNER_REVIEW → DAILY_CLOSING_READY | Explicit Owner acceptance and satisfied daily success criteria |
| DAILY_CLOSING_READY → CLOSED | Explicit Daily Governed Closing record |

## Stop-State Control

- Any active state may enter `BLOCKED`, `REJECTED`, or `GOVERNANCE_CONFLICT` when its condition is evidenced.
- Codex stops subsequent dependent Queue execution when a stop state occurs.
- Only the accountable actor may resolve a stop state and authorize re-entry to the mainline.
- A stop state is never equivalent to `CLOSED`.

## Prohibited Transitions

- Codex may not advance beyond `READY_FOR_PM_REVIEW`.
- Merge, Issue closure, or elapsed time does not automatically advance handover state.
- No state may skip PM Deliverable, Owner Review, or Daily Governed Closing gates.

## Related Documents

- [Handover Standard](HANDOVER_STANDARD.md)
- [Handover Version Policy](HANDOVER_VERSION_POLICY.md)
- [AIStudioCore Handover](AISTUDIOCORE_HANDOVER.md)
- [Governance Information Architecture](GOVERNANCE_INFORMATION_ARCHITECTURE.md)

## Status

Formal handover lifecycle established — awaiting PM review.
