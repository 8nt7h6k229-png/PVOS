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

---

## PVOS-304 Runtime Acceptance Framework

### Runtime Acceptance Authority

| Field | Value |
|---|---|
| Execution Source | GitHub Issue #75 — PVOS-304 |
| Planning Source | `PPP-PVOS-1.1-RUNTIME-PRODUCTIZATION-2026-08-07` — Owner Approved |
| Dependency | PVOS-303 / Issue #74 / commit `1434c8c74b68ea2c0816118825d6bf791c78010c` |
| Primary Capability | `QUA-002` |
| Acceptance Authority | PM |
| Executor Boundary | Prepare criteria, execute validation, and preserve evidence only |

This section specializes the existing Acceptance Evidence Framework for the bounded Runtime Productization workflow. It creates no new acceptance authority, Product Capability, Product Scope, or release status.

### Runtime Acceptance Gate

```text
Approved Runtime Input Contract
        ↓
Repeatable Runtime Execution Workflow
        ↓
Deterministic C# result
        ↓
Read-only Result Presentation
        ↓
Regression and scope-integrity evidence
        ↓
PM disposition
```

All required criteria must have an actual result and evidence baseline before PM review. A PASS from tests, the CLI, Golden regression, Python validation, or a Pull Request does not replace PM disposition.

### Runtime Acceptance Criteria Matrix

| Criterion | Claim | Validation Method | Expected Result | Required Evidence | PM Gate |
|---|---|---|---|---|---|
| `RTA-001` | Runtime input is one bounded typed request | Map `LayoutRequest` fields to `PVOS_RUNTIME_INPUT_CONTRACT.md` and current C# types | Request identity, geometry, one selected partition, Axis, and Module boundary are explicit | Input inventory, immutable commit, changed files | PM accepts input boundary |
| `RTA-002` | Project data remains bounded to one layout operation | Inspect exclusions and absence of persistence/model/adapter claims | No Canonical Project Model, persistence, runtime JSON, or project database is introduced | Boundary review and protected-scope diff | PM accepts Project Data Boundary |
| `RTA-003` | Module and Layout parameters use current validation rules | Inspect `ModuleDefinition`, Axis, selection, and current validation codes; execute bounded tests | Required values pass; invalid values return current Rejected result | Code references, test names/results, validation mapping | PM accepts parameter validation evidence |
| `RTA-004` | Runtime entry and ordered sequence are repeatable | Execute documented restore/build/test/CLI sequence | Each step records success, failure, or blocker without hidden continuation | Commands, environment, exit results, workflow definition | PM accepts executable workflow |
| `RTA-005` | Invalid input, valid no-fit, execution failure, and evidence blocker are distinct | Inspect and, where existing test evidence permits, execute each bounded disposition | Rejected input, Accepted no-fit, non-Product process failure, and BLOCKED evidence remain distinguishable | Terminal-state matrix and relevant test/output evidence | PM accepts error/result handling |
| `RTA-006` | Placement remains deterministic | Repeat identical existing scenario and compare ordered output | Identical panel membership, IDs, order, rows, columns, geometry, count, capacity, warnings, and errors | Existing C# tests, CLI captures, Golden comparison | PM accepts determinism |
| `RTA-007` | Complete containment remains enforced | Execute current containment and no-fit tests | Only complete contained panels are returned | Test results and Runtime evidence | PM accepts containment |
| `RTA-008` | Result integrity is internally consistent | Inspect `LayoutResult`; compare count, capacity, panels, warnings, and errors with bounded evidence | Runtime-owned values agree with existing contract and Golden evidence | Result mapping and regression report | PM accepts result integrity |
| `RTA-009` | Presentation is read-only | Trace every presented field to `LayoutResult` or immutable validation metadata | No placement, count, capacity, warning, or error recalculation | `PVOS_RUNTIME_PRESENTATION_BOUNDARY.md` and CLI inspection | PM accepts presentation integrity |
| `RTA-010` | Golden evidence remains immutable and reproducible | Validate manifest paths and SHA-256; compare CLI output after newline normalization | All registered hashes and bounded expected output match | Dataset ID, manifest, hashes, CLI result | PM accepts Golden regression |
| `RTA-011` | Python remains external Short Track validation | Execute PVPY-001 through PVPY-008 and inspect changed files | All required checks have bounded results; no Python layout logic or C# replacement | Python report, tests, scope inspection | PM accepts external validation evidence |
| `RTA-012` | Unauthorized scope remains absent | Review complete branch diff | No Product code, Product Scope, Blueprint, EOS, Governance, Legacy promotion, UI, Cloud, full AutoCAD, Electrical, Construction, or PVOS 2.x change | Changed-file list and protected-path diff | PM accepts scope integrity |

### Regression Requirements

| Requirement ID | Requirement | PASS Boundary | FAIL / BLOCKED Boundary |
|---|---|---|---|
| `RTR-001` | Immutable evidence identity | Review commit resolves and is recorded | BLOCKED when identity is unavailable |
| `RTR-002` | C# Release build | Build exits 0 with zero errors | FAIL on build error; BLOCKED when toolchain/dependency is unavailable |
| `RTR-003` | Existing C# test suite | All discovered tests pass and counts are recorded | FAIL on any failed test; BLOCKED when tests cannot execute |
| `RTR-004` | Existing C# CLI | Release CLI exits 0 and emits Runtime-owned result text | FAIL on non-zero process or contradictory result |
| `RTR-005` | Golden text comparison | Exact match after CRLF/LF normalization only | FAIL on content mismatch |
| `RTR-006` | Golden asset integrity | Every manifest asset exists and SHA-256 matches | FAIL on mismatch; BLOCKED when a required asset is missing |
| `RTR-007` | Stable panel identity | `PNL-000001` through `PNL-000010` are unique and ordered for current Dataset | FAIL on missing, duplicate, or reordered identity |
| `RTR-008` | Python Short Track | PVPY-001 through PVPY-008 execute in stable order with explicit result | Overall result follows existing FAIL/BLOCKED precedence |
| `RTR-009` | Repeated-run consistency | Repeated approved input produces the same bounded Product fields | FAIL on Product-field difference; timestamps are excluded |
| `RTR-010` | Changed-file scope | Only approved Runtime Productization evidence files change | FAIL on unauthorized tracked path |

Regression is evidence for the current bounded Dataset and workflow. It does not establish excluded scenarios, runtime JSON, UI, integration, or PVOS 2.x behavior.

### Runtime Evidence Requirements

Every Runtime acceptance record includes:

| Field | Requirement |
|---|---|
| Runtime Evidence ID | Unique identifier for the criterion or regression run |
| Criterion ID | One `RTA-001` through `RTA-012` identifier |
| Product Capability | Existing Capability ID and unchanged classification |
| Evidence Commit | Immutable reviewed commit |
| Environment | OS, .NET SDK, Python version when applicable, and relevant configuration |
| Input Baseline | Runtime Input Contract and Dataset identity |
| Execution | Exact command or documented inspection method |
| Expected Result | Bounded criterion stated before interpretation |
| Actual Result | Observed output, count, hash, diff, or finding |
| Result | PASS, FAIL, BLOCKED, or NOT RUN |
| Evidence Paths | Repository paths, Issue, PR, commit, test, or external report |
| Risks and Conditions | Known exclusions and unresolved conditions |
| Executor | Evidence preparer |
| PM Disposition | ACCEPTED, REJECTED, or MORE EVIDENCE REQUIRED, recorded by PM |

### Result and Failure Isolation

| Result | Runtime Acceptance Effect |
|---|---|
| PASS | Criterion is eligible for PM review; no automatic Product status change |
| FAIL | Return only the affected criterion and its dependents for correction/evidence |
| BLOCKED | Stop the affected criterion because authority, dependency, environment, or evidence is unavailable |
| NOT RUN | Criterion cannot support acceptance |

- A failed presentation criterion does not invalidate an independently evidenced input criterion.
- A Golden hash mismatch blocks claims dependent on that asset; it does not authorize artifact replacement.
- An infrastructure blocker does not become a Product rejection.
- A Product validation error is evidence of bounded rejection behavior, not necessarily a test failure.
- Unauthorized scope is a gate failure even when functional tests pass.

### PM Runtime Review Record

PM records exactly one disposition for the reviewed Runtime package:

| Field | Required Value |
|---|---|
| Runtime Review ID | Unique identity |
| Product / Version | PVOS 1.1 bounded Runtime Productization target |
| Evidence Commit and PR | Immutable commit and review surface |
| Criteria Results | `RTA-001` through `RTA-012`, each with result and evidence |
| Regression Results | `RTR-001` through `RTR-010` |
| Excluded Scope Confirmation | Explicit zero-promotion / zero-expansion finding |
| Conditions and Risks | Retained limitations and follow-up needs |
| Disposition | ACCEPTED, REJECTED, or MORE EVIDENCE REQUIRED |
| PM Identity and Time | Accountable reviewer and timestamp |

PM acceptance of this Runtime package does not modify Product Scope or admit a new Product capability unless a separately governed baseline decision explicitly does so.

### PVOS-304 Verification

| Check | Result |
|---|---|
| Input, execution, result, presentation, regression, and scope criteria defined | PASS |
| Every criterion maps method, expected result, evidence, and PM gate | PASS |
| Regression requirements are explicit and reproducible | PASS |
| PASS, FAIL, BLOCKED, and NOT RUN semantics preserved | PASS |
| PM remains acceptance authority | PASS |
| Product Acceptance performed by executor | No |

READY_FOR_PM_REVIEW — RUNTIME ACCEPTANCE FRAMEWORK PREPARED — PM DISPOSITION PENDING
