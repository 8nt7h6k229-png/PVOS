# Execution Queue Governance

## Purpose

Define GitHub Issues as the sole execution source for Codex within Engineering Operating System v1.0.

## Responsibility

Maintain the unique execution-source control that admits approved Planning Package work to Codex through the GitHub Issue Execution Queue.

## Information Domain

Work Orders

## Owner

PM

## Authority

- The approved Planning Package is the daily Source of Truth.
- A PM-authorized GitHub Issue in the target repository is the sole Execution Source for Codex.
- Planning Package entries, PM Work Orders, chat instructions, and local files do not directly authorize execution.
- Work Orders remain governance and coverage records; they do not replace the GitHub Issue.

## Governed Information Flow

```text
Planning Package (daily Source of Truth)
    ↓
GitHub Issue (Execution Queue; sole Codex Execution Source)
    ↓
Codex
    ↓
Evidence
    ↓
PM Review
```

## Execution Queue Entry

A GitHub Issue is executable only when it is open, PM-authorized, and identifies:

- objective;
- Capability ID;
- scope and out-of-scope boundaries;
- deliverables;
- acceptance criteria;
- required evidence; and
- execution-ready status.

Missing or conflicting authorization remains a PM review condition and is not resolved by executor inference.

## Execution Control

1. Codex verifies the GitHub repository, Issue number, open state, and execution-ready content before changing governed assets.
2. Codex executes only the Issue scope and preserves its Capability ID traceability.
3. Codex returns the Issue-required evidence and verification results.
4. Codex stops at `READY_FOR_PM_REVIEW`; only PM may approve, reject, close, or advance governed status.

## Evidence Linkage

Execution evidence must identify the authorizing GitHub Issue and the affected Capability IDs. Repository changes, verification results, and review status remain traceable to that Issue.

## Update Trigger

The approved execution source, Issue entry contract, evidence linkage, or PM review boundary changes.

## Related Documents

- [PM GitHub Issue Builder](PM_GITHUB_ISSUE_BUILDER.md)
- [EOS v1.0 Capability Matrix](EOS_V1_CAPABILITY_MATRIX.md)
- [Governance Information Architecture](GOVERNANCE_INFORMATION_ARCHITECTURE.md)
- [Governance Rules Registry](GOVERNANCE_RULES_REGISTRY.md)

## Status

Foundation established by [GitHub Issue #32](https://github.com/8nt7h6k229-png/PVOS/issues/32) — awaiting PM review.
