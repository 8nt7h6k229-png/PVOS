# PVOS CLI / Runtime / Engineer Workflow

## Authority and Boundary

| Field | Value |
|---|---|
| Execution Source | GitHub Issue #62 — PVOS-104 |
| Planning Source | DPP-PVOS-1.1-PRODUCT-EVOLUTION-2026-08-07 — Owner Approved |
| Primary Capability | PLT-001 — Standalone Core and CLI |
| Dependency Evidence | PVOS-103 / Issue #61 / commit `1b2bf3bdf3c3cadb000111dda3b6806ac148e2fe` |
| Status | READY_FOR_PM_REVIEW |

This document describes the existing standalone PVOS workflow. It does not implement a new Runtime, UI, adapter, orchestration layer, file format, integration, or Product capability.

## Existing Execution Surfaces

| Surface | Existing Asset | Role | Evidence State |
|---|---|---|---|
| Domain | `src/PVOS.Core` | Immutable geometry, request, result, and Local Axis types | Existing |
| Layout Runtime | `src/PVOS.Layout` | In-process deterministic `LayoutEngine.Generate` execution | Existing |
| CLI | `src/PVOS.Cli` | Compiled runnable example using the existing Runtime | Existing |
| Validation | `tests/PVOS.Tests` | xUnit geometry and layout validation | Existing |
| Golden Demo | `DEMO/` | Static review evidence for one approved deterministic scenario | Existing review evidence |
| AutoCAD Host | PvLayoutPlugin repository | Separate recognized Product host | Existing asset; standalone integration unverified |

“Runtime” in this workflow means the current in-process .NET call from a constructed `LayoutRequest` to `LayoutEngine.Generate`. It does not mean the historical branch-only Runtime Dashboard, auto-execution system, web service, job runner, or Product UI.

## CLI Workflow

```text
Engineer invokes dotnet run
        ↓
PVOS.Cli constructs explicit geometry, partition, Local Axis, and module inputs
        ↓
CLI constructs LayoutRequest
        ↓
LayoutEngine.Generate executes in process
        ↓
LayoutResult is written to standard output
        ↓
Engineer compares output with governed Demo evidence
```

### CLI Contract

| Step | Actor | Input | Output | Evidence |
|---:|---|---|---|---|
| 1 | Engineer | Governed repository and .NET 8 SDK | Restored solution | `PVOS.sln`; project files |
| 2 | Engineer | Existing source and dependencies | Release assemblies | Release build result |
| 3 | Engineer | Existing CLI example | In-memory `LayoutRequest` | `src/PVOS.Cli/Program.cs` |
| 4 | CLI | `LayoutRequest` | `LayoutResult` | `LayoutEngine.Generate` |
| 5 | CLI | `LayoutResult` | Deterministic console text | `DEMO/DEMO-001_OUTPUT.txt` |
| 6 | Engineer | Actual and expected outputs | Comparison finding | Demo-001 Revalidation Report |

Approved execution command:

```powershell
dotnet run --project .\src\PVOS.Cli\PVOS.Cli.csproj --configuration Release
```

The current CLI uses source-defined example input. It does not read `DEMO/demo-input.json`; that JSON is a static review capture, not a runtime adapter.

## Runtime Workflow

```text
Caller creates explicit LayoutRequest
        ↓
Runtime validates request and selected partition inputs
        ↓
Partition geometry transforms into its explicit Local Axis
        ↓
Deterministic row-major candidates are generated
        ↓
Only fully contained panels are retained
        ↓
Panels transform back to global coordinates
        ↓
LayoutResult returns status, ordered panels, count, kWp, warnings, and errors
```

### Runtime Input and Output Boundary

| Boundary | Current Definition |
|---|---|
| Input | In-memory typed `LayoutRequest` with explicit geometry, selected partition, Local Axis, and module parameters |
| Invocation | Synchronous in-process call to `LayoutEngine.Generate` |
| Output | Typed `LayoutResult` containing status, ordered panel geometry, count, installed capacity, warnings, and errors |
| Determinism | Identical valid inputs must reproduce identical ordered results |
| Persistence | None claimed |
| Network API | None claimed |
| File adapter | None claimed |
| UI | None claimed |

## Engineer Workflow

| Stage | Engineer Action | Required Check | Resulting Evidence |
|---|---|---|---|
| Inspect | Read Product scope, specifications, Capability Tree, and existing implementation | Confirm requested work fits an existing Capability | Scope finding |
| Restore | Run `dotnet restore .\PVOS.sln` | Dependency restore succeeds | Restore output |
| Build | Run Release build with `--no-restore` | 0 build errors | Build output |
| Validate | Run Release tests | Existing suite passes or failures are recorded | Test result |
| Execute | Run the existing CLI | Process exits successfully | Console result |
| Compare | Compare result with governed evidence | Exact or criterion-level comparison | Validation finding |
| Review | Assemble changed files, commands, outputs, and risks | No hidden scope change | PM review package |
| Accept | PM reviews bounded evidence | Explicit disposition required | PM Product Acceptance record |

## Known Runtime Boundaries

- No runtime JSON input or output adapter is established.
- No AutoCAD-to-standalone-PVOS end-to-end integration is verified.
- No DXF import, DXF export, database, network service, web interface, desktop UI, or cloud execution is established.
- No Runtime Dashboard, automatic execution bridge, optimization loop, AI placement, electrical engine, structural engine, or construction workflow is included.
- Demo SVG and PNG are review artifacts and do not recalculate placement.
- Historical Runtime and workflow documents remain branch-only evidence and do not define this current workflow.

## Validation

| Check | Result |
|---|---|
| Existing CLI path resolves | PASS |
| Existing Runtime project reference chain resolves | PASS — CLI → Layout → Core |
| Existing build and tests execute | PASS — Issue #61 evidence |
| Inputs, outputs, actors, and evidence are explicit | PASS |
| Unverified integrations remain labeled | PASS |
| Product code or Blueprint changed | No |

## Status

READY_FOR_PM_REVIEW — EXISTING RUNTIME WORKFLOW DEFINED — NO NEW RUNTIME IMPLEMENTED

---

## PVOS-302 Runtime Execution Workflow Definition

### Execution Authority

| Field | Value |
|---|---|
| Execution Source | GitHub Issue #73 — PVOS-302 |
| Planning Source | `PPP-PVOS-1.1-RUNTIME-PRODUCTIZATION-2026-08-07` — Owner Approved |
| Dependency | PVOS-301 / Issue #72 / commit `8740663e35efac61672aa7c1330f5e279497bae3` |
| Primary Capability | `PLT-001` |
| Runtime Authority | Existing C# `PVOS.Core` → `PVOS.Layout` → `PVOS.Cli` Mainline |

This extension formalizes the engineer execution workflow already evidenced above. It does not introduce a new Runtime, entry surface, orchestration service, API, UI, adapter, or Product capability.

### Execution Entry Contract

| Entry Element | Requirement | Evidence / Disposition |
|---|---|---|
| Actor | Engineer or bounded external validator operating the governed repository | Actor may invoke and observe; it may not calculate Product results |
| Repository identity | One resolvable immutable Git commit | Record `git rev-parse HEAD`; unavailable identity is BLOCKED |
| Runtime input | One in-memory `LayoutRequest` satisfying `PVOS_RUNTIME_INPUT_CONTRACT.md` | Invalid input returns a Rejected `LayoutResult` |
| Mainline | Current C# Core, Layout, and CLI projects | Python remains external and cannot replace Mainline |
| Build state | Required dependencies restored and Release assemblies available | Restore/build failure is an environment or build failure, not a Product result |
| Invocation | Direct in-process `LayoutEngine.Generate` by the existing CLI or approved caller | No runtime JSON, network, service, job, or UI entry implied |
| Evidence baseline | Golden Dataset manifest and expected CLI output for the bounded Demo | Missing evidence is BLOCKED |

### Ordered Workflow Sequence

| Order | Runtime / Engineer Step | Input | Output | Failure Boundary |
|---:|---|---|---|---|
| 1 | Resolve repository and evidence identity | Governed checkout | Immutable commit and asset paths | BLOCKED when identity or required evidence is unavailable |
| 2 | Restore and build existing Mainline | Solution and dependencies | Release assemblies | Build evidence FAIL/BLOCKED; no Product result inferred |
| 3 | Construct one typed request | Explicit engineer input | `LayoutRequest` | Missing construction dependency stops invocation |
| 4 | Validate request | `LayoutRequest` | Error collection or valid request | Validation errors produce Rejected result |
| 5 | Resolve selected partition | Geometry plus selected ID | Exactly one partition | Unknown/non-unique selection produces Rejected result |
| 6 | Transform boundary to explicit Local Axis | Selected partition and Axis | Local placement boundary | Invalid Axis is rejected during validation |
| 7 | Derive bounded placement range and pitches | Boundary and Module definition | Deterministic candidate sequence | No optimization or alternative search |
| 8 | Apply complete containment | Ordered candidates | Accepted panel collection and row decisions | Rejected candidates may produce bounded warnings |
| 9 | Assign stable order and identifiers | Accepted candidates | `PNL-000001` onward in row-major order | Ordering is owned by Runtime |
| 10 | Build Runtime result | Panels, power, row decisions | Accepted `LayoutResult`, including valid empty result | Result fields are not recalculated downstream |
| 11 | Present result | `LayoutResult` | Console or bounded review evidence | Presentation is read-only |
| 12 | Validate evidence | Actual result, commit, Golden Dataset | PASS, FAIL, BLOCKED, or NOT RUN record | Validation does not perform Product Acceptance |

### Terminal State Model

| Terminal State | Product Status | Panels / Capacity | Messages | Meaning |
|---|---|---|---|---|
| Accepted with panels | `Accepted` | One or more ordered panels; capacity from panel count × rated power / 1000 | May include containment/partial-row warnings | Valid Product result |
| Accepted no-fit | `Accepted` | Zero panels; zero capacity | `PLC_NO_PANEL_FITS`, `PLC_EMPTY_PLACEMENT_RESULT` | Valid deterministic result, not an input error |
| Rejected input | `Rejected` | Zero panels; zero capacity | One or more validation errors; no warnings | Product request did not meet the current input contract |
| Execution/build failure | No Product status asserted | No result asserted | Process/build evidence | Toolchain or execution failure; record FAIL or BLOCKED |
| Evidence unavailable | Existing result not accepted or rejected by this absence | No inference | Missing commit, manifest, or required artifact | Validation BLOCKED |

### Error Handling

| Error Class | Detection Owner | Required Handling | Prohibited Handling |
|---|---|---|---|
| Input validation | C# `LayoutEngine.Validate` | Accumulate current bounded errors and return Rejected result | Silent repair, inferred defaults, or exception-to-success conversion |
| Valid no-fit | C# warning construction | Return Accepted empty result with existing warnings | Treating no-fit as invalid input or adding panels |
| Containment rejection | C# Layout Engine | Exclude incomplete candidate and retain warning evidence when applicable | Presentation filtering or geometry adjustment |
| Build/test/CLI process failure | Engineer / validation runner | Record command, exit status, stderr, and FAIL/BLOCKED disposition | Representing infrastructure failure as Product rejection |
| Missing evidence | Validation runner | Stop affected evidence item as BLOCKED | Regenerating or replacing Golden evidence without approval |
| Unexpected exception | Invoking surface | Preserve process/error evidence and stop affected path | Fabricating a `LayoutResult` or continuing to PM acceptance |

The current Product engine returns bounded validation errors through `LayoutResult`. This definition does not create an exception taxonomy, retry policy, logging subsystem, telemetry platform, or new error codes.

### Result Handling

| Result Element | Runtime Ownership | Downstream Rule |
|---|---|---|
| `RequestId` | Copied from request identity | Preserve exactly for traceability |
| `PartitionId` | Selected partition for valid input; request selection for rejected input when available | Do not substitute or infer |
| `Status` | Runtime validation/execution | Display exactly; presentation cannot promote Rejected to Accepted |
| `Panels` | Runtime placement and ordering | Preserve collection, IDs, order, rows, columns, candidate index, and corners |
| `PanelCount` | Runtime property derived from panel collection | Display value; presentation does not recount as Product authority |
| `InstalledCapacityKwp` | Runtime calculation | Display without recalculation |
| `Warnings` | Runtime bounded warning construction | Preserve code, message, and optional row |
| `Errors` | Runtime validation result | Preserve code and message; do not suppress or reinterpret |

Result presentation and validation may format or compare values, but only the C# Runtime creates Product results.

### Engineer Evidence Sequence

```text
Git commit identity
        ↓
Restore / Release build
        ↓
Existing C# tests
        ↓
Existing C# CLI execution
        ↓
Golden Dataset and output comparison
        ↓
Issue-linked evidence and changed-file scope
        ↓
PM review
```

Every executed command records its actual result. A PASS in one layer cannot conceal a failure or blocker in another layer.

### PVOS-302 Verification

| Check | Result |
|---|---|
| Execution entry and prerequisites explicit | PASS |
| Ordered workflow and terminal states explicit | PASS |
| Input rejection and valid no-fit distinguished | PASS |
| Process failure and Product result distinguished | PASS |
| Result ownership and downstream rules explicit | PASS |
| C# Mainline changed | No |
| New Runtime or scope introduced | No |

READY_FOR_PM_REVIEW — RUNTIME EXECUTION WORKFLOW DEFINED — C# MAINLINE PRESERVED
