# PVOS 1.2 Runtime Workflow Enhancement

## Control

| Field | Value |
|---|---|
| Execution Source | GitHub Issue #85 — PVOS-503 |
| Dependency | PVOS-502 / commit `e39cb29f409e7b6887ec06ff549b233645019ddc` |
| Product Authority | Existing C# Core → Layout → CLI Mainline |
| Status | READY_FOR_PM_REVIEW |

## Objective

Define a traceable engineer workflow from bounded Project Input to a Result Package while preserving all existing Runtime and presentation contracts. This specification does not introduce a new Runtime surface or Product behavior.

## Workflow

```text
Caller-owned Project Input
        ↓ mapping / validation boundary
Current in-memory LayoutRequest
        ↓
Existing C# LayoutEngine.Generate
        ↓
Runtime-owned LayoutResult
        ↓ read-only packaging
Result Package + Validation Evidence
```

## Project Input Mapping

“Project Input” is caller-owned data for one operation, not a persisted project or Canonical Project Model.

| Project Input Concern | Current Runtime Contract | Rule |
|---|---|---|
| Request identity | `LayoutRequest.Id` | Required; no inferred identity |
| Roof and partitions | `GeometrySet` / `Partition` | Caller supplies explicit millimetre geometry |
| Selected partition | `SelectedPartitionId` | Exactly one explicit selection; no fallback |
| Local orientation | `LocalAxis` | Explicit origin/rotation; no automatic orientation |
| Module parameters | `ModuleDefinition` | Explicit dimensions, power, gaps, margin and orientation |

## Execution and Validation Sequence

| Order | Step | Owner | Failure Boundary |
|---:|---|---|---|
| 1 | Resolve immutable Product/evidence commit | Engineer / automation | Missing commit is BLOCKED |
| 2 | Construct one typed `LayoutRequest` | Caller | Mapping failure stops before Runtime |
| 3 | Execute existing Runtime validation | C# Mainline | Invalid input returns Rejected result |
| 4 | Execute deterministic placement | C# `LayoutEngine` | Runtime owns panels and diagnostics |
| 5 | Capture `LayoutResult` unchanged | Workflow | No downstream repair or fallback |
| 6 | Build Result Package references | Packaging boundary | Packaging failure does not alter result |
| 7 | Validate Golden/regression evidence | C# tests / Python support tool | PASS, FAIL or BLOCKED remains explicit |

## Result Package Contract

| Field | Source | Packaging Rule |
|---|---|---|
| Evidence commit | Git | Exact immutable SHA |
| Request / partition identity | `LayoutResult` | Copy unchanged |
| Status | `LayoutResult.Status` | Copy unchanged; never promote Rejected |
| Panels | `LayoutResult.Panels` | Preserve membership, order, IDs, rows, columns and corners |
| Panel count | `LayoutResult.PanelCount` | Copy; do not recount as Product authority |
| Capacity | `LayoutResult.InstalledCapacityKwp` | Copy; formatting only |
| Warnings / errors | Runtime collections | Preserve code, message, row and order |
| Golden manifest | Validation registry | Reference path/version/hash findings |
| Validation report | External validator | Reference result/fingerprint; not Product output |

The Result Package may be a review document or evidence envelope. This specification does not authorize a new serialization format, API, database or UI.

## Compatibility

- Existing CLI behavior and output remain valid.
- Existing typed C# contracts remain unchanged.
- Existing Golden-001 through 006 remain static review evidence, not Runtime JSON inputs.
- Existing C# tests remain Product behavior evidence.
- Python remains an external observer and cannot create or modify a Result Package’s Product values.

## Boundary Verification

| Check | Result |
|---|---|
| Product code modified | No |
| Presentation recalculates placement | No |
| Canonical Project Model introduced | No |
| Persistence, UI, API, Cloud or adapter introduced | No |
| PVOS 1.1 decision, EOS or Governance changed | No |

READY_FOR_PM_REVIEW — RUNTIME WORKFLOW ENHANCEMENT DEFINED
