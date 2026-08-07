# PVOS Runtime Input Contract

## Authority and Boundary

| Field | Value |
|---|---|
| Execution Source | GitHub Issue #72 — PVOS-301 |
| Planning Source | `PPP-PVOS-1.1-RUNTIME-PRODUCTIZATION-2026-08-07` — Owner Approved |
| Primary Capability | `LAY-001` |
| C# Evidence | `src/PVOS.Core/Domain.cs`; `src/PVOS.Layout/LayoutEngine.cs` |
| Contract Type | Definition of existing in-memory boundary; no new serialization or Product model |
| Status | READY_FOR_PM_REVIEW |

## Purpose

Define the input required for one deterministic PVOS layout operation so an engineer, the existing C# Runtime, and validation evidence use the same bounded interpretation. This document records current behavior and does not modify Product Scope, C# types, or validation logic.

## Project Data Boundary

One Runtime operation consumes exactly one in-memory `LayoutRequest`. The request carries the minimum context needed to perform deterministic placement:

```text
Request identity
  + explicit roof and partition geometry
  + exactly one selected partition identity
  + Local Axis belonging to that partition
  + module definition and placement spacing
        ↓
Existing C# LayoutEngine.Generate
```

“Project data” in this contract means the data supplied for that one operation. It does not establish a persisted project, Project database, Canonical Project Model, file format, runtime JSON adapter, AutoCAD document contract, or multi-run lifecycle.

## Input Structure

### Layout Request

| Field | Current C# Type | Requirement | Capability | Validation Boundary |
|---|---|---|---|---|
| `Id` | `string` | Non-empty placement request identifier | `LAY-001` | `PLC_REQUEST_INVALID` |
| `Geometry` | `GeometrySet` | Accepted explicit geometry is required | `GEO-001` | `PLC_DEPENDENCY_MISSING` and geometry validations |
| `SelectedPartitionId` | `string` | Identifies exactly one supplied partition | `GEO-002` | `SEL_SELECTION_REQUIRED`, `SEL_PARTITION_UNKNOWN` |
| `Axis` | `LocalAxis` | Accepted axis belonging to the selected partition | `AXS-001` | `PLC_DEPENDENCY_MISSING` and axis validations |
| `Module` | `ModuleDefinition` | Accepted dimensions, power, orientation, gaps, and margin | `LAY-001` | `PLC_DEPENDENCY_MISSING` and module validations |

The Runtime accepts the typed request directly. `DEMO/demo-input.json` remains static review evidence and is not an executable Runtime input.

### Explicit Geometry and Partition Data

| Object / Field | Requirement | Current Validation |
|---|---|---|
| `GeometrySet.RequestId` | Non-empty geometry request identifier | `GEO_REQUEST_ID_REQUIRED` |
| `GeometrySet.Id` | Existing geometry-set identity carried by the typed object | No separate validation code currently evidenced |
| `GeometrySet.RoofId` | Non-empty roof identifier | `GEO_IDENTIFIER_REQUIRED` |
| `GeometrySet.Roof` | Exactly one explicit polygon | `GEO_ROOF_REQUIRED` plus polygon validation |
| `GeometrySet.Partitions` | At least one supplied partition | `GEO_PARTITION_COLLECTION_EMPTY` |
| `GeometrySet.CoordinateSystemId` | Non-empty coordinate-system identifier | `GEO_COORDINATE_SYSTEM_REQUIRED` |
| `GeometrySet.LinearUnit` | Exact value `mm` | `GEO_UNIT_INVALID` |
| `Partition.Id` | Non-empty and unique across roof/partition identities | `GEO_IDENTIFIER_REQUIRED`, `GEO_IDENTIFIER_DUPLICATE` |
| `Partition.Boundary` | Simple polygon with at least three distinct finite vertices, non-zero edges and area, fully inside roof | `GEO_VERTEX_COUNT_INVALID`, `GEO_COORDINATE_INVALID`, `GEO_ZERO_LENGTH_EDGE`, `GEO_AREA_INVALID`, `GEO_POLYGON_NOT_SIMPLE`, `GEO_PARTITION_OUTSIDE_ROOF` |

Geometry is caller-supplied. The Runtime does not detect roofs, generate partitions, repair polygons, infer units, or import source-specific formats.

## Module Parameters

| Field | Required Value / Rule | Current Validation |
|---|---|---|
| `RequestId` | Non-empty | `MOD_REQUEST_ID_REQUIRED` |
| `Id` | Non-empty module identifier | `MOD_ID_REQUIRED` |
| `PhysicalWidthMm` | Finite and greater than zero | `MOD_WIDTH_INVALID` |
| `PhysicalLengthMm` | Finite and greater than zero | `MOD_LENGTH_INVALID` |
| `RatedPowerWp` | Finite and greater than zero | `MOD_RATED_POWER_INVALID` |
| `Orientation` | Defined `ModuleOrientation` value | `MOD_ORIENTATION_INVALID` |
| `ColumnGapMm` | Finite and non-negative | `MOD_COLUMN_GAP_INVALID` |
| `RowGapMm` | Finite and non-negative | `MOD_ROW_GAP_INVALID` |
| `EdgeMarginMm` | Finite and non-negative | `MOD_EDGE_MARGIN_INVALID` |
| `LinearUnit` | Exact value `mm` | `MOD_LINEAR_UNIT_INVALID` |
| `PowerUnit` | Exact value `Wp` | `MOD_POWER_UNIT_INVALID` |

`EffectiveWidthMm`, `EffectiveLengthMm`, `ColumnPitchMm`, and `RowPitchMm` are derived by the existing C# `ModuleDefinition`. They are not independent engineer inputs and must not be supplied or recalculated by presentation.

## Layout Parameters

| Parameter | Input Source | Runtime Use | Boundary |
|---|---|---|---|
| Selected partition | `SelectedPartitionId` | Chooses exactly one supplied placement boundary | No automatic selection or partition generation |
| Local Axis partition reference | `LocalAxis.PartitionId` | Must equal selected partition | `AXS_PARTITION_REFERENCE_MISMATCH` on mismatch |
| Local Axis origin | `LocalAxis.Origin` | Establishes explicit placement frame | Both coordinates finite; no inferred origin |
| Local Axis rotation | `LocalAxis.RotationDegrees` | Rotates between global and local coordinates | Finite value; no automatic orientation search |
| Coordinate system | Geometry and Axis identifiers | Must match exactly | `AXS_COORDINATE_SYSTEM_MISMATCH` |
| Linear unit | Axis value | Exact `mm` | `AXS_UNIT_INVALID` |
| Edge margin | Module definition | Insets the local bounding range | Non-negative; no rule-derived setback |
| Row/column gaps | Module definition | Establish deterministic pitch | Non-negative; no optimization |
| Orientation | Module definition | Selects effective width/length mapping | Only current enum values |

Grid search, scoring, shading, obstacle processing, electrical rules, structural constraints, walkways, and construction parameters are not Runtime inputs in this boundary.

## Validation Input Contract

### Preconditions

1. A non-null `LayoutRequest` is supplied.
2. All geometry, selection, Axis, and module dependencies are present.
3. Required identifiers are non-empty and references are consistent.
4. Geometry is finite, simple, non-degenerate, and bounded as currently validated.
5. Units and numeric parameters satisfy the exact current rules.

### Result of Input Validation

| Condition | Runtime Disposition |
|---|---|
| All validations pass | Continue deterministic placement |
| One or more validations fail | Return `LayoutResult` with `Status = Rejected`, zero panels, zero installed capacity, no warnings, and the collected errors |
| Valid request but no panel fits | Return `Status = Accepted` with zero panels and the existing no-fit warnings; this is not an input rejection |

Validation accumulates current bounded errors. This contract does not add error codes, precedence, exception behavior, automatic correction, or recovery behavior.

## Capability and Evidence Mapping

| Boundary | Capability | Current Evidence |
|---|---|---|
| Explicit polygon geometry | `GEO-001` | `Domain.cs`, geometry tests, Product specifications |
| Supplied partition selection | `GEO-002` | `LayoutRequest`, `LayoutEngine.ValidateSelection`, tests |
| Explicit partition Local Axis | `AXS-001` | `LocalAxis`, `AxisTransform`, tests |
| Module and spacing parameters | `LAY-001` | `ModuleDefinition`, module validation, Demo-001 |
| Deterministic grid inputs | `LAY-002` | derived pitches and existing Layout Engine |
| Containment boundary | `LAY-003` | supplied partition boundary and containment tests |
| Stable ordered output prerequisite | `LAY-004` | selected partition, Local Axis, module inputs, Demo-001 |

## Explicit Exclusions

- No new Product input, Product Capability, serialization schema, or persistence lifecycle.
- No Canonical Project Model, Module Catalog, Constraint Engine, Legacy promotion, or adapter.
- No runtime JSON, UI, Cloud, full AutoCAD integration, DXF, Electrical, Construction, or PVOS 2.x work.
- No Product Scope, Product Blueprint, Capability status, EOS, or Governance change.

## Verification

| Check | Result |
|---|---|
| Existing input objects and fields inventoried | PASS |
| Existing validation rules and codes mapped | PASS |
| Project Data Boundary limited to one operation | PASS |
| Module and Layout parameters explicit | PASS |
| Runtime JSON or new Product model introduced | No |
| C# Product code changed | No |

## Result

READY_FOR_PM_REVIEW — RUNTIME INPUT CONTRACT DEFINED — PRODUCT SCOPE UNCHANGED
