# PVOS 1.1 Runtime Productization Planning Package

## Package Identity

| Field | Value |
|---|---|
| Deliverable | `PVOS_1_1_RUNTIME_PRODUCTIZATION_PLANNING_PACKAGE` |
| Product | PVOS 1.1 |
| Planning Type | Product Runtime planning; no implementation authority |
| Source Authority | Owner-provided planning objective |
| Repository Baseline | `main` at `01aa9143f7da7b472d9760a21daa75c6c0ec31ad` |
| Status | READY_FOR_PM_RUNTIME_PLANNING_REVIEW |

## Objective

Plan the bounded evolution from the existing engineer-operated CLI evidence path:

```text
CLI
  ↓
Layout Core
  ↓
Result
  ↓
Evidence
```

to a reviewable Product Runtime workflow:

```text
Engineer Input
  ↓
PVOS Runtime Workflow
  ↓
Deterministic Layout
  ↓
Result Presentation
  ↓
Validation Evidence
```

The intended outcome is a complete planning basis for later governed Issues. This Package does not authorize Product code changes, create a new Product capability, change the Product Scope, or perform Product Acceptance.

## Source Basis

| Source | Planning Use | Boundary |
|---|---|---|
| PVOS 1.0 Product Acceptance | Owner-provided source basis for the next Product planning stage | Repository record currently requires reconciliation; see Dependencies |
| PVOS 1.1 Implementation Foundation | Merged baseline, Golden Dataset, Runtime workflow, Legacy review, and Python Short Track evidence | Evidence only; merge does not expand Product Scope |
| `PRODUCT/PVOS_RUNTIME_WORKFLOW.md` | Existing CLI, in-process Runtime, engineer workflow, errors, and results | Defines current state; no JSON adapter, UI, or service claim |
| `PRODUCT/PVOS_1_1_RUNTIME_PRODUCTIZATION.md` | C# Mainline ownership and Product evidence workflow | Python remains external validation only |
| `PRODUCT/PRODUCT_BLUEPRINT.md` | Existing capability IDs, dependency order, and Product boundaries | Blueprint remains unchanged and retains its recorded status |
| `PM/PVOS_1_1_ACCEPTANCE_EVIDENCE_FRAMEWORK_2026-08-07.md` | Evidence contract, PASS/FAIL/BLOCKED model, and PM gate | Validation PASS does not perform Product Acceptance |
| `PM/PVOS_1_1_IMPLEMENTATION_BASELINE_LOCK_2026-08-07.md` | Locked source hashes, Capability boundary, and exclusions | No silent release allocation or status promotion |

## Scope

### 1. Runtime Input Contract Review

Review the current in-memory `LayoutRequest` boundary without prescribing a new implementation.

| Review Area | Planning Question | Existing Boundary to Preserve | Expected Planning Output |
|---|---|---|---|
| Input structure | Are request identity, geometry, selected partition, Local Axis, module definition, and required validation inputs explicit? | Current typed C# request; no new serialization contract implied | Field inventory, required/optional finding, and gap list |
| Project data boundary | What minimum engineer-supplied context is required for one deterministic layout run? | One bounded layout request; no Canonical Project Model promotion, persistence model, or project database | Project-context boundary finding |
| Module parameters | Are dimensions, orientation, gaps, edge margin, and rated power explicit and validated? | Existing `ModuleDefinition` and `LAY-001`; no Module Catalog | Parameter and validation matrix |
| Layout parameters | Are selected partition, Local Axis, containment, ordering, and deterministic expectations explicit? | Existing `GEO-002`, `AXS-001`, and `LAY-002`–`LAY-004` | Runtime precondition matrix |

Engineer Input means an explicit, reviewable input contract for the existing C# Mainline. It does not authorize runtime JSON, DXF, AutoCAD extraction, a new Project Model, or a second engine.

### 2. Runtime Execution Workflow

Define the execution contract from entry through result handling.

| Workflow Element | Required Definition | Existing Boundary |
|---|---|---|
| Execution entry | Actor, entry point, accepted input state, repository/build identity, and invocation result | Existing C# execution surface under `PLT-001` |
| Workflow sequence | Validate request → resolve selected partition → apply Local Axis → generate deterministic candidates → enforce containment → order panels → create result | Preserve current deterministic behavior; no optimization or orchestration layer |
| Error handling | Invalid input, unavailable dependency, execution error, no-fit warning, and validation failure must have explicit dispositions | Use existing errors/warnings where evidenced; no new diagnostic subsystem is implied |
| Result handling | Identify result identity, status, panel geometry, count, installed capacity, warnings, errors, and transfer to presentation/evidence | `LayoutResult` remains the Product result source |

The planned workflow must distinguish:

- Product validation errors from a valid no-fit result;
- Product execution results from infrastructure or environment blockers;
- runtime result fields from presentation formatting;
- validation evidence from PM Product Acceptance.

### 3. Product Presentation Boundary

Presentation is a read-only consumer of `LayoutResult`.

| Presentation Rule | Acceptance Boundary |
|---|---|
| Source | Every displayed Product value is traceable to the Runtime result or immutable validation metadata |
| Geometry | Display ordered panel geometry without moving, filtering, scoring, or recalculating placement |
| Summary | Display result status, partition, count, installed capacity, warnings, and errors without recalculation |
| Determinism | Presentation ordering preserves Runtime ordering and stable panel identifiers |
| Error state | Presentation exposes bounded errors and warnings without converting them into a successful result |
| Exclusion | No UI framework, interaction model, rendering engine, or delivery channel is selected by this Package |

### 4. Acceptance Preparation

Prepare one traceable Runtime acceptance matrix before any implementation Issue is considered complete.

| Acceptance Area | Required Criterion | Primary Existing Capability |
|---|---|---|
| Input completeness | All required engineer inputs are explicit, validatable, and mapped to the current request boundary | `GEO-001`, `GEO-002`, `AXS-001`, `LAY-001` |
| Deterministic execution | Identical valid inputs produce identical ordered results | `LAY-002`–`LAY-004`, `QUA-001` |
| Containment | Only complete panels inside the selected partition are returned | `LAY-003` |
| Result integrity | Geometry, count, installed capacity, warnings, and errors are internally consistent | `RES-001`–`RES-004` |
| Presentation integrity | Presentation exposes the Runtime result without recalculating placement or Product values | `VIS-001` |
| Executable workflow | Entry, sequence, error path, result path, and engineer evidence path are repeatable | `PLT-001`, `QUA-002` |
| Governed acceptance | Evidence terminates at one explicit PM disposition | `QUA-003` |

## Out of Scope

- UI implementation or selection of a UI framework.
- Cloud service, web service, network API, database, job runner, or deployment platform.
- Full AutoCAD integration or changes to the existing AutoCAD Product Host.
- DXF import/export or other file-adapter implementation.
- Electrical design, string design, structural analysis, or energy modelling.
- Construction planning, installation planning, or project management workflows.
- Optimization, AI placement, automatic roof recognition, or multi-product orchestration.
- PVOS 2.x scope, capability, release allocation, or commitment.
- Canonical Project Model, Module Catalog, Constraint Engine, or any Legacy Asset promotion.
- EOS, Certified Governance, Product Blueprint, Product Scope, Capability status, or release-status modification.
- Product code development under this Planning Package.

## Dependencies

| Dependency | Required State Before Execution | Evidence / Action |
|---|---|---|
| PVOS 1.0 Product Acceptance | Acceptance authority and accepted boundary must be unambiguous | Owner identifies this as source basis; `PM/PVOS_1_0_PM_PRODUCT_ACCEPTANCE_RECORD.md` currently states `PENDING PM DECISION`, so PM must reconcile the durable record before execution |
| PVOS 1.1 Implementation Foundation | Merged and addressable by immutable commit | Merge commit `01aa9143f7da7b472d9760a21daa75c6c0ec31ad` |
| Product Baseline Lock | Source hashes and no-scope-expansion boundary remain valid | `PM/PVOS_1_1_IMPLEMENTATION_BASELINE_LOCK_2026-08-07.md` |
| Runtime workflow evidence | Current input, execution, result, and engineer workflow remain the starting point | `PRODUCT/PVOS_RUNTIME_WORKFLOW.md`; `PRODUCT/PVOS_1_1_RUNTIME_PRODUCTIZATION.md` |
| Golden regression evidence | Existing Dataset and assertions remain unchanged unless separately approved | `VALIDATION/golden-dataset-v1.json`; `VALIDATION/GOLDEN_REGRESSION_FOUNDATION.md` |
| Acceptance framework | Evidence record fields and PM authority remain applicable | `PM/PVOS_1_1_ACCEPTANCE_EVIDENCE_FRAMEWORK_2026-08-07.md` |

If the Product Acceptance record cannot be reconciled, execution stops at the affected entry gate; the planning review may still proceed.

## Execution Order

| Order | Planning Work Package | Primary Output | Entry Gate | Exit Gate |
|---:|---|---|---|---|
| 1 | Runtime Input Contract Review | Input field inventory, project-data boundary, parameter matrix, gaps | Dependencies identified | No new Product Scope or model introduced |
| 2 | Runtime Execution Workflow | Entry, sequence, error handling, and result-handling contract | Work Package 1 reviewed | Every path ends in result, failure, or blocker evidence |
| 3 | Product Presentation Boundary | Read-only presentation contract and non-recalculation rules | Runtime result boundary explicit | Displayed values trace directly to Runtime results |
| 4 | Runtime Acceptance Preparation | Criteria-to-evidence matrix and repeatable validation plan | Work Packages 1–3 complete | Each criterion has method, expected result, evidence source, and PM gate |
| 5 | PM Runtime Planning Review | ACCEPTED, REJECTED, or MORE EVIDENCE REQUIRED disposition | Complete Planning Package | PM disposition recorded; implementation Issues remain separate |

Execution must remain sequential. A BLOCKED, rejected, or conflicting boundary stops only the affected work package and its dependents.

## Acceptance Criteria

| ID | Criterion | Verification Method |
|---|---|---|
| RTP-AC-001 | Runtime input structure identifies every existing required request component without adding a Product model | Map fields to current C# types and Product capabilities |
| RTP-AC-002 | Project data boundary is limited to one explicit deterministic layout operation | Review boundary against Product Scope and Baseline Lock |
| RTP-AC-003 | Module and layout parameters have explicit validation expectations | Parameter-to-rule inspection and bounded negative cases |
| RTP-AC-004 | Execution entry, actor, prerequisites, sequence, and terminal states are unambiguous | Workflow walkthrough using one valid and bounded invalid/no-fit paths |
| RTP-AC-005 | Errors, warnings, environment blockers, and valid results remain distinguishable | Result/error disposition matrix review |
| RTP-AC-006 | Result fields preserve deterministic geometry, ordering, count, capacity, warnings, and errors | Existing C# tests plus Golden regression comparison |
| RTP-AC-007 | Presentation displays Runtime output without recalculating placement or summary values | Field-level traceability from `LayoutResult` to presentation evidence |
| RTP-AC-008 | Identical approved input reproduces identical ordered output | Repeat execution and exact/criterion-level comparison |
| RTP-AC-009 | Evidence records use PASS, FAIL, BLOCKED, or NOT RUN and include immutable commit identity | Acceptance Evidence Framework inspection |
| RTP-AC-010 | No UI, Cloud, full AutoCAD integration, electrical, construction, Legacy promotion, or PVOS 2.x work enters the changed-file scope | Pull Request diff and excluded-scope audit |
| RTP-AC-011 | PM retains the sole Product Acceptance disposition | Acceptance record review |

Passing these planning criteria makes a future execution package eligible for PM review. It does not itself accept the Product or authorize implementation.

## Required Evidence

| Evidence ID | Required Evidence | Minimum Contents |
|---|---|---|
| RTP-EV-001 | Runtime Input Contract Review | Existing type/field source, capability mapping, validation rule, gap, and exclusion |
| RTP-EV-002 | Project Data Boundary Record | Included engineer context, excluded persistence/adapter/model claims, and owner |
| RTP-EV-003 | Runtime Workflow Definition | Entry, ordered steps, terminal states, errors, warnings, and result handling |
| RTP-EV-004 | Presentation Traceability Matrix | Presented field, `LayoutResult` source, formatting rule, and proof of no recalculation |
| RTP-EV-005 | Runtime Acceptance Matrix | Acceptance ID, claim, method, expected result, actual result, status, risks, and PM gate |
| RTP-EV-006 | Build and Unit-Test Evidence | Immutable commit, commands, environment, counts, and results |
| RTP-EV-007 | Golden Regression Evidence | Dataset ID, six asset hashes, CLI comparison, stable panel IDs, and result |
| RTP-EV-008 | Error and No-Fit Evidence | Bounded invalid-input, execution-error/blocker, and valid no-fit dispositions |
| RTP-EV-009 | Scope Integrity Evidence | Complete changed-file list and zero unauthorized-scope finding |
| RTP-EV-010 | PM Runtime Review Record | ACCEPTED, REJECTED, or MORE EVIDENCE REQUIRED; conditions, risks, reviewer, time, commit, Issues, and PR |

## Planning Constraints

- Each future execution Issue must map to one existing primary Capability ID.
- Planning may describe required outcomes and evidence but must not prescribe or implement new architecture.
- Python validation remains an external Short Track consumer and cannot replace the C# Mainline.
- Legacy sources remain evidence-only unless a separate Product Baseline Change is approved.
- No implementation begins until PM approves the execution decomposition and exact changed-file boundaries.

## Package Result

READY_FOR_PM_RUNTIME_PLANNING_REVIEW
