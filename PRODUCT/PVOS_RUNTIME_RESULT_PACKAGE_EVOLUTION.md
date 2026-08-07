# PVOS Runtime Result Package Evolution Review

## Control

| Field | Value |
|---|---|
| Execution Source | GitHub Issue #91 — PVOS-603 |
| Dependency | PVOS-602 / commit `71dae955ecf559ffc261bbd62c3c7738cd1c1b1f` |
| Mode | Contract-readiness review; no delivery-surface authority |
| Status | READY_FOR_PM_REVIEW |

## Objective

Evaluate a stable Result Package evidence structure while preserving the existing C# Runtime as the sole Product-result authority. This Review does not approve an API, serialization format, database, service, UI or Cloud implementation.

## Candidate Logical Structure

| Section | Candidate Contents | Authoritative Source |
|---|---|---|
| Package identity | Logical contract version, evidence commit, creation time | Package process / Git |
| Request reference | Request and selected partition identities | `LayoutResult` |
| Runtime result | Status, panels, count, capacity, warnings and errors | `LayoutResult` only |
| Evidence references | Golden manifest version/assets, C# test result, validator report fingerprint | Validation evidence |
| Compatibility declaration | Consumer version expectation and known limitations | Separately reviewed package contract |
| Risk / non-claims | Excluded behavior and unresolved integrations | Acceptance evidence |

This is a logical review model, not an approved JSON schema or Product interface.

## Field Lineage Rules

| Product Value | Lineage | Consumer Rule |
|---|---|---|
| Status | `LayoutResult.Status` | Copy unchanged; never promote Rejected |
| Partition | `LayoutResult.PartitionId` | Copy; do not infer another selection |
| Panels | `LayoutResult.Panels` | Preserve membership and order |
| Panel identity/order | Panel ID, PlacementOrder, CandidateIndex, Row, Column | Do not sort, renumber or deduplicate |
| Geometry | Runtime panel corners | Do not move, rotate, clip, snap or recompute |
| Panel count | `LayoutResult.PanelCount` | Copy; recounting is not Product authority |
| Capacity | `InstalledCapacityKwp` | Copy; display formatting only |
| Warnings/errors | Runtime collections | Preserve code, message, row and order |

## Evidence Packaging

- Evidence commit must be an immutable full SHA.
- Golden evidence must identify manifest version and integrity result.
- C# validation must identify configuration, test count and result.
- Python evidence may identify tool version, PVPY results and deterministic report fingerprint.
- Evidence absence is BLOCKED and must not change a valid Runtime result.
- Evidence packaging may reference artifacts; it may not rewrite admitted Golden assets.

## Versioning Considerations

| Change Class | Candidate Rule |
|---|---|
| Patch | Evidence-description clarification with no field or semantic change |
| Minor | Additive optional evidence metadata; older consumers may ignore it |
| Major | Product-value field, semantic, required-field or compatibility change; requires separate baseline authority |

No version number or compatibility promise becomes binding until a separate Result Package Contract Proposal is approved.

## Compatibility Review

| Consumer | Compatibility Boundary |
|---|---|
| Existing CLI | Remains an execution/presentation surface; no package dependency introduced |
| C# tests | Remain Product behavior and regression authority |
| Python validator | May observe evidence references; cannot create Product values |
| PM reviewer | May use package evidence for decisions; PASS is not automatic acceptance |
| Future adapter/UI/service | Not approved; must not be inferred from this Review |

## Allowed Disposition

**ELIGIBLE_FOR_SEPARATE RESULT PACKAGE CONTRACT PROPOSAL.**

The logical structure, lineage and versioning questions are sufficiently bounded for a separate proposal-planning decision. This disposition does not authorize an API, file format, implementation or Product Scope change.

## Boundary Verification

| Check | Result |
|---|---|
| Product code or C# contracts modified | No |
| API or serialization commitment created | No |
| UI, Cloud, database or service started | No |
| Runtime-owned values recalculated | No |
| PVOS 1.1/1.2, EOS or Governance status modified | No |
| Canonical or Legacy asset promoted | No |
| PVOS 2.x scope opened | No |

READY_FOR_PM_REVIEW — RESULT PACKAGE PROPOSAL ELIGIBILITY PREPARED
