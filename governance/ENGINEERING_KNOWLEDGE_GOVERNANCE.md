# Engineering Knowledge Governance

## Purpose

Govern discovery, classification, provenance, review, preservation, and reuse of durable engineering knowledge.

## Responsibility

Maintain the unique engineering-knowledge identity, authority, lifecycle, and reuse contract without approving product scope or architecture.

## Information Domain

Engineering Knowledge

## Owner

Engineering

## Knowledge Record Contract

| Field | Requirement |
|---|---|
| Knowledge ID | Unique stable identifier |
| Title | Source title without inferred expansion |
| Knowledge Type | Specification, Implementation Note, Index, Decision, Test, Dataset, Guide, or Gap |
| Domain | Engineering subject area |
| Repository and Path | Authoritative or candidate location |
| Provenance | Commit, branch, tag, PR, Issue, producer, and snapshot date as available |
| Authority | Baseline, historical, branch-only, experimental, deprecated-for-recovery, or gap |
| Review Status | Pending, Reviewed, Accepted, Rejected, or Superseded |
| Related Capability IDs | EOS capabilities informed by the record |
| Related Decisions | Qualified Decision IDs or `None registered` |
| Evidence | Evidence records supporting classification and claims |
| Reuse Conditions | Permitted use and required review boundary |
| Supersession | Explicit successor or `None evidenced` |

## Classification Model

| Classification | Meaning |
|---|---|
| BASELINE | Present on the governed default branch or accepted through governed review |
| BRANCH_ONLY | Recoverable from a branch but not part of the default-branch baseline |
| HISTORICAL | Retained as a dated tag, commit, or superseded lineage |
| EXPERIMENTAL | Proposed or open work not accepted into the baseline |
| DEPRECATED_FOR_RECOVERY | No longer an independent recovery source; retention is still governed |
| GAP | Required knowledge is missing, ambiguous, conflicting, or unverifiable |

Classification describes evidence status. It does not approve product capability, architecture, implementation, or deletion.

## Knowledge Precedence

1. Accepted default-branch records and merged review evidence establish current repository knowledge.
2. Immutable commits and tags establish historical snapshots.
3. Open PRs and branch-only records establish candidates, not current truth.
4. Issues establish intent and acceptance criteria, not completed implementation.
5. Chat, model memory, and tool-local state are non-authoritative working context.
6. Conflicting generations remain separately classified until an accountable decision resolves them.

## Existing Governed Knowledge Map

| Knowledge ID | Asset | Type | Classification | Provenance / Evidence | Reuse Boundary |
|---|---|---|---|---|---|
| EK-PVOS-001 | `ENGINEERING/PE-GEO-001_SPEC.md` | Specification | BASELINE | PVOS repository path and Git history | Use for explicit roof and partition geometry within its approved scope |
| EK-PVOS-002 | `ENGINEERING/PE-GEO-002_SPEC.md` | Specification | BASELINE | PVOS repository path and Git history | Use for supplied partition selection within its approved scope |
| EK-PVOS-003 | `ENGINEERING/PE-AXS-001_SPEC.md` | Specification | BASELINE | PVOS repository path and Git history | Use for local-axis behaviour within its approved scope |
| EK-PVOS-004 | `ENGINEERING/PE-LAY-001_SPEC.md` | Specification | BASELINE | PVOS repository path and Git history | Use for module parameters within its approved scope |
| EK-PVOS-005 | `ENGINEERING/PE-LAY-002_SPEC.md` | Specification | BASELINE | PVOS repository path and Git history | Use for deterministic placement within its approved scope |
| EK-PVOS-006 | `ENGINEERING/ENG-001_IMPLEMENTATION_NOTES.md` | Implementation Note | BASELINE | PVOS repository path and Git history | Inform implementation evidence; specifications retain normative precedence |
| EK-PM-001 | `PM/PRODUCT_KNOWLEDGE_INDEX.md` | Index | BASELINE | Snapshot classification dated 2026-08-03 | Discover existing knowledge; does not approve or reconcile candidates |
| EK-PM-002 | `PM/BRANCH_PRODUCT_KNOWLEDGE_MAP.md` | Index | BASELINE | Issue #4 recovery evidence and snapshot date | Locate branch knowledge while preserving branch status |
| EK-PM-003 | `PM/BRANCH_RECOVERY_INDEX.md` | Index | BASELINE | Recovery disposition and immutable commit references | Guide recovery priority; not deletion authority |
| EK-PM-004 | `PM/ARCHITECTURE_INDEX.md` | Index | BASELINE | Architecture-family and ADR source references | Discover architecture evidence; Decision Registry governs decision identity |
| EK-GAP-017 | `PM/GAP_ANALYSIS.md` — `GAP-017` | Gap | GAP | PVOS default-branch contracts and implementation explicitly have no governed Engineering Input Acquisition pipeline; confirmed 2026-08-08 | Use to govern experimental input acquisition work; does not establish a permanent adapter architecture or Product behavior |

## Existing Gap Summary

- Product knowledge is distributed across PVOS and PvLayoutPlugin; repository ownership remains unresolved as `GAP-012`.
- Two ADR namespaces overlap and remain branch-only; qualified identities are recorded without approval promotion.
- Several engineering domains have multiple generations across baseline, tags, and branches.
- DXF Import and DXF Export remain unverified knowledge gaps in the existing Product Knowledge Index.
- Governed Engineering Input Acquisition is missing as `GAP-017`; no CAD-to-JSON, DWG/DXF import, or real-project input pipeline is established.
- Branch-only knowledge requires accountable recovery or baseline decisions before use as current product truth.

## Engineering Knowledge First Control

Before creating or changing equivalent engineering knowledge:

1. search the default branch, indexes, relevant branches, tags, Issues, PRs, and registered decisions;
2. classify every relevant source and preserve provenance;
3. reuse or extend the authoritative asset when one exists;
4. record conflicts or missing evidence as gaps;
5. obtain a separate authorised Issue for recovery, promotion, replacement, or architecture approval.

## Review and Reuse

- Engineering may prepare and validate knowledge; accountable PM/Owner governance controls product and architecture acceptance.
- Reuse must cite the Knowledge ID, immutable or governed source, classification, and applicable scope.
- Branch-only or historical knowledge may inform analysis but cannot be represented as current baseline.
- A successor does not erase earlier evidence; supersession is explicit and traceable.

## Update Trigger

Engineering knowledge is added, reclassified, reviewed, superseded, recovered, or found to conflict with another governed source.

## Related Documents

- [Evidence Governance](EVIDENCE_GOVERNANCE.md)
- [Architecture Decision Registry](ARCHITECTURE_DECISION_REGISTRY.md)
- [EOS v1.0 Capability Matrix](EOS_V1_CAPABILITY_MATRIX.md)
- [Governance Information Architecture](GOVERNANCE_INFORMATION_ARCHITECTURE.md)
- [Product Knowledge Index](../PM/PRODUCT_KNOWLEDGE_INDEX.md)
- [Branch Product Knowledge Map](../PM/BRANCH_PRODUCT_KNOWLEDGE_MAP.md)

## Status

Formal engineering-knowledge governance established on the governed default branch. Individual knowledge records retain their own review status and authority.
