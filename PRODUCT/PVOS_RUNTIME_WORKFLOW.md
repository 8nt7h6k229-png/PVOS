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
