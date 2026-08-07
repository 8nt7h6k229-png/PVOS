# PVOS 1.1 Acceptance Evidence Framework — 2026-08-07

## Authority and Boundary

| Field | Value |
|---|---|
| Execution Source | GitHub Issue #60 — PVOS-102 |
| Planning Source | DPP-PVOS-1.1-PRODUCT-EVOLUTION-2026-08-07 — Owner Approved |
| Capability Coverage | QUA-002, QUA-003; existing bounded Product capabilities |
| Dependency Evidence | PVOS-101 / Issue #59 / commit `5ee79a7d7a24687ad5c4bc8d42f37f92d5a88071` |
| Framework State | READY_FOR_PM_REVIEW |

This framework closes the traceability path from an existing Product Capability to evidence, validation, and an accountable acceptance decision. It creates no Capability, changes no Product status, modifies no Product code, and does not perform Product Acceptance.

## Acceptance Evidence Closed Loop

```text
Capability identity and current classification
        ↓
Evidence source and immutable review baseline
        ↓
Repeatable validation method and expected boundary
        ↓
Recorded validation result and retained risks
        ↓
PM Product Acceptance decision
        ↓
Accepted, Rejected, or More Evidence Required
```

An implementation, test pass, Demo, merge, elapsed time, or document presence cannot replace the PM decision.

## Evidence Record Contract

| Field | Requirement |
|---|---|
| Evidence ID | Unique identifier within the acceptance package |
| Capability ID | Existing ID from `PRODUCT_CAPABILITY_TREE.md` |
| Capability Classification | Exact current status; no promotion by this record |
| Claim | One bounded behavior or support claim |
| Evidence Source | Repository path, Issue, PR, commit, test, or generated artifact |
| Evidence Baseline | Immutable commit and relevant input version |
| Validation Method | Repeatable command or documented inspection procedure |
| Expected Result | Criterion derived from existing Product evidence |
| Actual Result | Observed output without interpretation expansion |
| Result | PASS, FAIL, BLOCKED, or NOT RUN |
| Risks and Conditions | Known exclusions, gaps, or environment constraints |
| Reviewer | Executor for preparation; PM for acceptance |

## Capability-to-Acceptance Mapping

| Capability | Existing Evidence | Validation | Acceptance Criterion | PM Gate |
|---|---|---|---|---|
| GEO-001 | `PE-GEO-001_SPEC.md`; Core geometry types | Inspect explicit polygon input and run geometry tests | Only caller-provided explicit geometry is accepted | PM accepts bounded geometry evidence |
| GEO-002 | `PE-GEO-002_SPEC.md`; selected partition request | Inspect selected-partition input and exclusion behavior | Exactly the supplied selected partition drives placement | PM accepts partition-selection evidence |
| AXS-001 | `PE-AXS-001_SPEC.md`; `AxisTransform.cs`; tests | Validate origin/rotation transformation and repeatability | Explicit Local Axis controls placement without inferred origin | PM accepts Local Axis evidence |
| LAY-001 | `PE-LAY-001_SPEC.md`; domain input types | Validate module dimensions, gaps, margin, and power inputs | Only specified valid module parameters enter layout | PM accepts input-contract evidence |
| LAY-002 | `PE-LAY-002_SPEC.md`; `LayoutEngine.cs`; tests | Repeat identical valid request | Candidate generation and ordering are identical | PM accepts deterministic-grid evidence |
| LAY-003 | Layout specification and boundary tests | Validate fit and no-fit boundary cases | Only complete contained panels are accepted | PM accepts containment evidence |
| LAY-004 | Layout engine, tests, Demo-001 | Compare panel IDs and ordered geometry | Accepted panels have stable order and identity | PM accepts ordered-placement evidence |
| RES-001 | `Domain.cs`; Demo JSON/SVG/PNG | Reconcile panel corner geometry | Four global-coordinate corners exist for each panel | PM accepts result-geometry evidence |
| RES-002 | `Domain.cs`; tests; Demo summary | Compare count with returned panels | Count equals panel collection length | PM accepts count evidence |
| RES-003 | `Domain.cs`; tests; Demo summary | Recalculate count × rated power ÷ 1000 | Installed capacity matches approved formula | PM accepts capacity evidence |
| RES-004 | `Domain.cs`; fit/no-fit tests | Run zero-panel and fit cases | Warning appears only at the approved no-fit boundary | PM accepts warning evidence |
| VIS-001 | Demo JSON, SVG, PNG, and summary | Inspect that all approved result fields are reviewable | Presentation exposes the result without recalculation | PM accepts presentation evidence |
| PLT-001 | `PVOS.sln`; CLI; unit tests | Build, test, and execute existing CLI | Standalone bounded workflow is runnable and testable | PM accepts execution-surface evidence |
| QUA-001 | Unit tests; repeated Demo execution | Compare repeated outputs byte-for-byte where applicable | Identical inputs reproduce identical ordered results | PM accepts determinism evidence |
| QUA-002 | Geometry/layout tests and review artifacts | Run existing validation suite and preserve outputs | Required validation evidence is reproducible and traceable | PM accepts evidence sufficiency |
| QUA-003 | Issue chain, review branch, PR, acceptance record | Confirm all included mappings and retained exclusions | PM records exactly one accountable disposition | PM owns Product Acceptance |

## Validation Result Model

| Result | Meaning | Acceptance Effect |
|---|---|---|
| PASS | Evidence matches the bounded criterion | Eligible for PM review; not automatically accepted |
| FAIL | Observed result contradicts the criterion | Return only the affected capability or evidence item |
| BLOCKED | Required authority, dependency, environment, or evidence is unavailable | Stop affected item and record blocker |
| NOT RUN | Validation has not been executed | Cannot support acceptance |

## PM Product Acceptance Record

PM records:

| Field | Required Value |
|---|---|
| Acceptance ID | Unique Product acceptance identifier |
| Product and Version | Exact bounded Product target |
| Evidence Commit | Immutable review commit |
| Included Capability Results | Criterion-level PASS/FAIL/BLOCKED findings |
| Excluded Scope Confirmation | No excluded, deferred, branch-only, or PVOS 2.x claim promoted |
| Conditions and Risks | Explicit retained items |
| Disposition | ACCEPTED, REJECTED, or MORE EVIDENCE REQUIRED |
| PM Identity and Time | Accountable reviewer and timestamp |
| Related Issues and PR | Execution and review chain |

## Acceptance Authority Boundary

- Codex may collect evidence, execute validation, and prepare findings.
- PM alone records Product Acceptance.
- A PASS validation result does not alter Product Capability status.
- Failure returns only the affected evidence item; it does not invalidate unrelated accepted evidence.
- Python validation under PVOS-105 remains a Short Track validation surface and cannot change PVOS behavior.
- Historical evidence under PVOS-106 remains review-only and cannot enter the Product Baseline without a separate decision.

## Acceptance Findings

- PASS — Existing bounded Product capabilities map to evidence and validation methods.
- PASS — Every mapping terminates at an explicit PM gate.
- PASS — Failure and blocker behavior are item-specific.
- PASS — No Product Acceptance or capability promotion was performed.

## Status

READY_FOR_PM_REVIEW — ACCEPTANCE EVIDENCE FRAMEWORK PREPARED — PRODUCT ACCEPTANCE PENDING
