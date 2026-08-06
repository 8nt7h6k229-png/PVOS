# Handover Version Policy

## Purpose

Define version identification and succession rules for handover records.

## Responsibility

Maintain the unique handover version-control policy.

## Information Domain

Handover

## Owner

PM

## Update Trigger

Handover versioning, succession, or retention requirements change.

## Version Identifier

AIStudioCore handover versions use:

```text
YYYY-MM-DD.N
```

- `YYYY-MM-DD` is the governed snapshot date.
- `N` is a positive daily sequence beginning at `1`.
- Example: `2026-08-06.1`.

The Handover ID remains stable as `AISTUDIOCORE-HANDOVER`; the version identifies a specific immutable snapshot.

## Version Rules

1. Create a new version when governed status, evidence, queue state, accountable next action, or closing state changes materially.
2. Never overwrite the meaning of an earlier published version.
3. Increment `N` for another snapshot on the same date; begin at `.1` on a new date.
4. A correction after review creates a successor version and records the corrected version; it does not silently replace history.
5. Exactly one version may be designated `Current` in the authoritative repository state.

## Succession Record

Every successor identifies:

- previous version;
- change reason;
- authorizing GitHub Issue or accountable review;
- effective snapshot; and
- whether the previous version is `Superseded`, `Rejected`, or retained as historical evidence.

## Retention

- All reviewed, rejected, superseded, and closed versions remain recoverable through Git history.
- Draft local copies are not authoritative versions until persisted as governed repository evidence.
- Daily Governed Closing freezes the closing version; later corrections require a new version and explicit authority.

## Current-Version Control

`AISTUDIOCORE_HANDOVER.md` represents the current working snapshot. Git history and related review records preserve earlier versions. A `Current` designation is a pointer to authority, not permission to erase prior evidence.

## Related Documents

- [Handover Standard](HANDOVER_STANDARD.md)
- [Handover Lifecycle](HANDOVER_LIFECYCLE.md)
- [AIStudioCore Handover](AISTUDIOCORE_HANDOVER.md)
- [Governance Information Architecture](GOVERNANCE_INFORMATION_ARCHITECTURE.md)

## Status

Formal handover version policy established — awaiting PM review.
