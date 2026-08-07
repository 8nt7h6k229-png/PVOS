# PM Verification Framework

## Purpose

Provide an evidence-based, accountable framework for PM verification of EOS capabilities while preserving the distinction between executor completion and PM verification.

## Responsibility

Define verification inputs, checks, result records, accountable decisions, and status-transition evidence for EOS-001 through EOS-016.

## Information Domain

Governance

## Owner

PM

## Verification Authority Boundary

- Codex may collect, validate, and present evidence and may recommend a result.
- Only PM may record `Verified` for an EOS capability.
- A `Completed` capability remains `Completed` until an explicit PM Verification Record accepts it.
- Missing, rejected, conflicting, or non-durable evidence cannot satisfy verification.
- Merge, elapsed time, Issue state, or executor commentary never implies PM verification.

## Required Inputs

| Input | Minimum Requirement |
|---|---|
| Capability definition | Unique Capability ID, purpose, outputs, dependencies, verification method, and current status |
| Execution authority | Approved Planning Package and authorizing GitHub Issue |
| Deliverable evidence | Durable repository path and immutable commit identity |
| Verification evidence | Reproducible checks mapped to acceptance criteria |
| Dependency evidence | Direct dependencies and their current PM verification state |
| Scope evidence | Changed-file set and explicit out-of-scope confirmation |
| Review context | Known risks, gaps, conflicts, and prior PM dispositions |

## Verification Checks

1. **Identity:** Capability ID exists exactly once in the EOS Capability Matrix.
2. **Authority:** Work traces to an approved Planning Package and one authorized GitHub Issue.
3. **Deliverable:** Required output exists at a registered authoritative location.
4. **Acceptance:** Every Issue acceptance criterion has durable evidence.
5. **Reproducibility:** Verification commands, inputs, and results can be repeated where applicable.
6. **Dependencies:** Each dependency is resolved or explicitly accepted as a controlled risk by PM.
7. **Scope:** No unapproved Product, Blueprint, Operating Cycle, Workspace, or architecture change is hidden in the evidence.
8. **Consistency:** Capability Catalog, definition, Completion Matrix, coverage, File Registry, and GIA references agree.
9. **Risk:** Every known gap or conflict is visible and has an accountable disposition requirement.
10. **Persistence:** Evidence is committed and available through the review branch or accepted default branch.

## Verification Result Model

| Result | Meaning | Capability Effect |
|---|---|---|
| Prepared | Executor evidence package is ready for PM review | No status change |
| Verified | PM accepts all required evidence and records the decision | Capability may move to `Verified` |
| Verified with Conditions | PM accepts evidence subject to explicit retained conditions | Capability may move to `Verified` only if PM records that effect |
| More Evidence Required | Required evidence is incomplete or non-reproducible | Remains `Completed` or earlier state |
| Rejected | PM rejects the capability evidence | PM records required corrective disposition |
| Governance Conflict | Governing sources conflict and inference is prohibited | Stop pending accountable resolution |

## PM Verification Record

Every PM decision records:

| Field | Requirement |
|---|---|
| Verification ID | Unique identifier |
| Capability ID | Exactly one EOS-001 through EOS-016 |
| Result | One result from the Verification Result Model |
| Evidence Commit | Immutable Git commit |
| Evidence Paths | Registered repository paths |
| Acceptance Findings | Criterion-by-criterion result |
| Dependency Findings | Verified, conditionally accepted, or unresolved dependencies |
| Conditions and Risks | Explicit retained gaps |
| Verified By | PM identity |
| Verified Time | Accountable decision timestamp |
| Related Issue and PR | Execution and review traceability |

## Sixteen-Capability Coverage

| Capability | Primary Verification Focus |
|---|---|
| EOS-001 | Nine-domain GIA completeness and unique responsibilities |
| EOS-002 | Registry uniqueness, path resolution, and GIA alignment |
| EOS-003 | Approved Rule IDs, sources, approvers, and revisions |
| EOS-004 | Decision identity, authority, provenance, and gaps |
| EOS-005 | Handover content contract completeness |
| EOS-006 | Version succession and retention controls |
| EOS-007 | Lifecycle states, gates, and prohibited transitions |
| EOS-008 | One current handover and accurate accountable state |
| EOS-009 | Unique verified workspace registrations |
| EOS-010 | Approved daily Source of Truth and input validation |
| EOS-011 | Work Order boundaries and Issue traceability |
| EOS-012 | Evidence provenance, durability, and review state |
| EOS-013 | Knowledge provenance, classification, and reuse boundary |
| EOS-014 | Blueprint identity, integrity, and authority classification |
| EOS-015 | Capability catalog, dependencies, status, coverage, and audit consistency |
| EOS-016 | GitHub Issue as sole execution source and Queue traceability |

## Review Flow

```text
Codex evidence preparation
        ↓
READY_FOR_PM_REVIEW
        ↓
PM verification checks
        ↓
Explicit PM Verification Record
        ↓
Capability status update, if authorized by PM result
```

No automated step may replace the explicit PM Verification Record.

## Update Trigger

Verification inputs, checks, result states, record fields, capability coverage, or accountable authority changes through an approved source.

## Related Documents

- [EOS v1.0 Capability Matrix](EOS_V1_CAPABILITY_MATRIX.md)
- [Evidence Governance](EVIDENCE_GOVERNANCE.md)
- [Governance Rules Registry](GOVERNANCE_RULES_REGISTRY.md)
- [Execution Queue Governance](EXECUTION_QUEUE_GOVERNANCE.md)
- [Handover Lifecycle](HANDOVER_LIFECYCLE.md)

## Status

Framework established — awaiting PM verification.
