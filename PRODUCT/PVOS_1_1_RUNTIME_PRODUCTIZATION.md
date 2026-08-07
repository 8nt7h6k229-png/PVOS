# PVOS 1.1 Runtime Productization

## Authority and Dependency

| Field | Value |
|---|---|
| Execution Source | GitHub Issue #68 — PVOS-203 |
| Planning Source | PVOS 1.1 Implementation Planning Package — Owner Approved |
| Dependency | PVOS-202 / commit `b1cd9565af81a4db3ff3230988f3e234b82ff488` |
| Mainline | Existing C# `PVOS.Core` → `PVOS.Layout` → `PVOS.Cli` |
| Status | READY_FOR_PM_IMPLEMENTATION_REVIEW |

## Productization Boundary

Runtime Productization defines how the existing deterministic C# execution surface becomes a repeatable engineer-operated Product evidence workflow. It does not create a new Runtime, Product capability, file adapter, API, user interface, service, or deployment channel.

## Three-Layer Workflow

```text
CLI execution surface
        ↓
Engineer validation workflow
        ↓
Governed Product evidence workflow
```

### 1. CLI Execution Surface

| Contract | Existing Definition |
|---|---|
| Entry point | `src/PVOS.Cli/PVOS.Cli.csproj` |
| Engine ownership | C# `PVOS.Layout.LayoutEngine` |
| Input | Source-defined typed `LayoutRequest` for Demo-001 |
| Output | Deterministic UTF-8 console representation of `LayoutResult` |
| Exit | Process exit status and standard output |
| Reference output | `DEMO/DEMO-001_OUTPUT.txt` |

The CLI remains a compiled C# execution surface. It is not replaced or reimplemented by Python.

### 2. Engineer Validation Workflow

| Order | Engineer Action | Command / Evidence | Gate |
|---:|---|---|---|
| 1 | Resolve repository identity | `git rev-parse HEAD` | Immutable commit recorded |
| 2 | Restore dependencies | `dotnet restore .\PVOS.sln` | Restore succeeds |
| 3 | Build Mainline | `dotnet build .\PVOS.sln --configuration Release --no-restore` | Zero build errors |
| 4 | Execute regression tests | `dotnet test .\PVOS.sln --configuration Release --no-build --no-restore` | Existing suite passes |
| 5 | Execute CLI | `dotnet run --project .\src\PVOS.Cli\PVOS.Cli.csproj --configuration Release --no-build` | Exit code zero |
| 6 | Validate Golden Dataset | `VALIDATION/golden-dataset-v1.json` | Paths, hashes, and assertions match |
| 7 | Preserve findings | Validation report or Issue Evidence | PASS, FAIL, or BLOCKED recorded |

Failure stops the affected validation path. It does not authorize the engineer or validator to rewrite Golden Assets or modify Product behavior.

### 3. Product Evidence Workflow

```text
Approved Planning Package
        ↓
GitHub Issue execution source
        ↓
Bounded implementation and immutable commit
        ↓
Build, test, CLI, and Golden regression evidence
        ↓
Pull Request review
        ↓
PM Product Acceptance decision
```

| Product Gate | Required Evidence | Authority |
|---|---|---|
| Scope gate | Product Baseline Lock and exact changed-file set | Existing Product sources / PM |
| Implementation gate | Issue-linked commit within approved boundary | Executor |
| Regression gate | Build, test, CLI, manifest, and Golden comparison results | Executor prepares evidence |
| Review gate | Pull Request diff and remaining risks | PM review |
| Acceptance gate | Explicit ACCEPTED, REJECTED, or MORE EVIDENCE REQUIRED record | PM only |

## Runtime Ownership

| Concern | Owner |
|---|---|
| Geometry and request/result types | C# `PVOS.Core` |
| Deterministic placement | C# `PVOS.Layout` |
| Executable example surface | C# `PVOS.Cli` |
| Golden evidence registry | `VALIDATION/golden-dataset-v1.json` |
| External regression orchestration | Python Short Track, when executed under PVOS-205 |
| Product Acceptance | PM |

External validation may invoke and observe the C# CLI. It may not import internal C# APIs, calculate layout, substitute result fields, or become a second PVOS Engine.

## Artifact Lifecycle

| Artifact | Source | Retention Boundary |
|---|---|---|
| Product source | `src/` | C# Mainline is authoritative for Product behavior |
| Unit tests | `tests/` | Existing executable validation |
| Golden assets | `DEMO/` | Immutable review baseline unless separately approved |
| Golden manifest | `VALIDATION/golden-dataset-v1.json` | Machine-readable evidence registry |
| Generated assemblies | local `bin/` and `obj/` | Build artifacts; not Product evidence commits |
| Validation report | explicit caller-selected path | Run evidence; timestamps excluded from deterministic comparison |

## Explicit Exclusions

- No runtime JSON request or result adapter.
- No AutoCAD end-to-end integration claim.
- No DXF, database, network, service, desktop UI, web UI, Cloud, or dashboard.
- No automatic workflow orchestration beyond the bounded validator.
- No Legacy Asset promotion or Canonical Project Model implementation.
- No Product Scope, Capability status, release allocation, EOS, Governance, or PVOS 2.x change.

## Verification

| Check | Result |
|---|---|
| CLI, engineer, and Product workflows explicitly connected | PASS |
| C# Mainline remains Product behavior authority | PASS |
| Golden Dataset dependency included | PASS |
| External validation boundary explicit | PASS |
| New Runtime or Product capability implemented | No |

## Result

READY_FOR_PM_IMPLEMENTATION_REVIEW — RUNTIME PRODUCT WORKFLOW DEFINED — C# MAINLINE PRESERVED
