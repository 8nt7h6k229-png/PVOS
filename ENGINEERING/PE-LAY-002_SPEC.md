# PE-LAY-002 - Deterministic Placement Engineering Specification

Work item: [PE-LAY-002 / PVOS Issue #25](https://github.com/8nt7h6k229-png/PVOS/issues/25)

Primary Capability: [`LAY-002` - Deterministic Layout Grid](../PRODUCT/PRODUCT_CAPABILITY_TREE.md)

Backlog Item: [`PE-LAY-002`](../PRODUCT/PRODUCT_BACKLOG.md)

Dependencies: [PE-GEO-001](PE-GEO-001_SPEC.md), [PE-GEO-002](PE-GEO-002_SPEC.md), [PE-AXS-001](PE-AXS-001_SPEC.md), and [PE-LAY-001](PE-LAY-001_SPEC.md)

Status: Proposed for PM approval

## 1. Purpose

This specification defines the observable, deterministic engineering contract that transforms one valid placement request into one placement result.

It governs the ordered grid, candidate evaluation, complete-boundary containment, accepted panel geometry, count, installed capacity, warnings, validation, errors, and behavior-level acceptance evidence. It does not prescribe an algorithm, API, data structure, software architecture, library, language, UI, renderer, or storage mechanism.

Evidence:

- [PV Layout MVP Specification, sections 3, 5, 8, and 9](../PRODUCT/PV_LAYOUT_MVP_SPEC.md) defines the sequence, grid envelope, candidate order, full containment, ordered global panel geometry, count, capacity, and no-fit result.
- [PVOS 1.0 Product Baseline](../PM/PRODUCT_BASELINE.md) identifies deterministic rectangular placement and its result as existing baseline capability.
- [Product Capability Tree, LAY-002 through LAY-004 and RES-001 through RES-004](../PRODUCT/PRODUCT_CAPABILITY_TREE.md) separates grid, containment, placement, and result outcomes.
- The four approved dependency specifications define the only accepted geometry, selection, Local Axis, and module-parameter inputs.

## 2. Scope

### Included

- one immutable placement request;
- dependency-reference and cross-reference validation;
- the local grid envelope and ordered candidate sequence;
- complete candidate rectangles in local coordinates;
- deterministic containment decisions;
- accepted and rejected candidate classifications;
- stable accepted-panel identifiers and placement order;
- ordered panel geometry transformed to global coordinates;
- accepted panel count and installed capacity;
- non-blocking placement warnings;
- placement states, validation errors, and acceptance tests.

### Excluded

- geometry creation, repair, partition generation, or partition selection;
- Local Axis creation, recommendation, or modification;
- module definition, catalog selection, or orientation optimization;
- clipping, reshaping, overlap search, collision solving, obstacles, setbacks, shading, walkways, or alternate arrangements;
- DXF or any import or export behavior;
- UI, visualization, rendering, construction drawing, or reporting format;
- AI, optimization, roof detection, electrical design, structural design, and source-code implementation.

## 3. Engineering Context

PE-LAY-002 consumes only final `Accepted` results from its four dependencies. It does not re-own their validation rules or silently repair their data.

```text
Accepted geometry + Accepted selection + Accepted Local Axis + Accepted module
                                  |
                     One placement request
                                  |
                   Deterministic placement result
```

Although this specification returns the complete approved placement result, its Primary Capability remains `LAY-002`. The contained decisions and result fields are traceable supporting outcomes already approved as `LAY-003`, `LAY-004`, and `RES-001` through `RES-004`; this document does not create or promote a capability.

## 4. Input Contract

Exactly one placement request contains:

| Input | Cardinality | Requirement |
|---|---:|---|
| Placement request identifier | Exactly one | Non-empty and unique for the logical request |
| Accepted geometry result reference | Exactly one | Resolves to final `Accepted` PE-GEO-001 evidence |
| Accepted selection result reference | Exactly one | Resolves to final `Accepted` PE-GEO-002 evidence |
| Selected partition identifier and geometry | Exactly one | Matches the Accepted selection without mutation |
| Accepted Local Axis result reference | Exactly one | Resolves to final `Accepted` PE-AXS-001 evidence for that partition |
| Accepted module result reference | Exactly one | Resolves to final `Accepted` PE-LAY-001 active definition |
| Coordinate-system identifier | Exactly one | Matches geometry, selection, Axis, and result context |
| Linear unit | Exactly one | Millimetres |

The Accepted module supplies effective local X/Y dimensions, column and row gaps, edge margin, pitches, rated power, and their units. The request shall not override any accepted dependency value.

The selected partition is the sole placement boundary. Roof geometry supplies its accepted context but is not an additional placement boundary.

Changing any dependency reference, geometry, Axis, module parameter, coordinate system, or unit requires a new placement request identifier.

## 5. Output Contract

Every validated request produces exactly one result containing:

| Output | Requirement |
|---|---|
| Placement request identifier | Correlates to the request when available |
| Placement status | Exactly one status defined in section 10 |
| Validation errors | Stable ordered collection; empty for an Accepted result |
| Placement warnings | Stable ordered collection; warnings do not invalidate an Accepted result |
| Panel geometry collection | Ordered accepted panels only; empty for a valid no-fit result |
| Accepted panel count | Non-negative integer equal to collection cardinality |
| Installed capacity | Non-negative kWp derived only from accepted count and rated module power |

Each accepted panel contains:

- a unique deterministic panel identifier;
- its one-based accepted placement order;
- the originating candidate sequence index and row/column position;
- four ordered corner points in the original global coordinate system; and
- the selected partition, Local Axis, and active module references needed for traceability.

A Rejected result contains no accepted panel geometry, count, or capacity presented as a valid placement outcome. It may include diagnostic request references and errors only.

No visualization, rendering, DXF, import, or export representation is part of the result.

## 6. Placement Workflow

The observable sequence is:

```text
Accepted Layout Request
        |
Generate Placement Grid
        |
Evaluate Candidate Panels
        |
Boundary Containment
        |
Accept or Reject Candidate
        |
Panel Geometry Collection
        |
Panel Count
        |
Installed Capacity
        |
Placement Result
```

Rules:

1. The complete request is validated before placement begins.
2. Invalid input produces a Rejected result and no partial placement result.
3. Valid input produces one finite, deterministic candidate sequence.
4. Every generated candidate receives exactly one containment decision in sequence order.
5. Only accepted candidates become panels.
6. Accepted candidates retain their relative candidate order.
7. Panel geometry is transformed to global coordinates without mutating any source.
8. Count, capacity, and warnings are derived after all candidate decisions.
9. A valid request is Accepted even when zero panels fit.

## 7. Grid Generation Rules

1. The selected partition is interpreted through the Accepted Local Axis in local coordinates.
2. Its local axis-aligned bounding rectangle establishes minimum and maximum local X/Y extents.
3. The local grid envelope begins at minimum local X and minimum local Y plus the Accepted edge margin.
4. Its maximum limits are maximum local X and maximum local Y minus the Accepted edge margin.
5. Candidate rectangles use the Accepted effective width along local X and effective length along local Y.
6. Column pitch is the Accepted effective width plus Accepted column gap.
7. Row pitch is the Accepted effective length plus Accepted row gap.
8. Rows are ordered from lower to higher local Y.
9. Within a row, columns are ordered from lower to higher local X.
10. A candidate is generated only where its complete local rectangle fits within the grid envelope, including boundary contact.
11. Candidate sequence index is one-based and follows row order, then column order.
12. Identical accepted inputs produce the same envelope, row/column positions, rectangles, and candidate sequence.
13. No alternate origin, Axis, orientation, pitch, or arrangement is searched.

These rules define required outcomes, not a loop structure, numeric library, spatial index, or generation algorithm.

## 8. Boundary Containment Rules

1. The Accepted selected partition is the sole containment boundary.
2. Each complete candidate rectangle is evaluated against that partition.
3. A candidate is contained when every part of its rectangle lies inside or on the partition boundary.
4. Boundary contact is contained and does not cause rejection.
5. Any candidate portion outside the partition causes rejection of the whole candidate.
6. A rejected candidate is not clipped, reshaped, moved, rotated, retried, or optimized.
7. Edge margin restricts the grid envelope; it is not a substitute for partition containment.
8. Every candidate receives one stable decision: `Accepted` or `Rejected`.
9. Identical candidate and partition inputs produce the same decision.
10. Geometry, vertex order, identifiers, coordinate system, units, Axis, and module parameters remain immutable.

Numerical acceptance shall follow the approved geometry and Local Axis contracts. This specification introduces no new tolerance, polygon repair, or boundary expansion.

## 9. Accepted Panel Rules

### Candidate classifications

- An **accepted candidate** is a complete generated rectangle that satisfies section 8.
- A **rejected candidate** is a generated rectangle that fails section 8. It remains decision evidence but never becomes panel output.

### Panel identity and order

1. Each accepted candidate becomes exactly one panel.
2. Panels retain the relative order of accepted candidates.
3. Placement order is a contiguous one-based integer sequence with no gaps.
4. Panel identifiers are `PNL-` followed by the six-digit, zero-padded placement order, beginning with `PNL-000001`.
5. Rejected candidates consume no placement order and no panel identifier.
6. Identical requests produce identical panel identifiers and order.

### Panel geometry

1. A panel is the accepted candidate rectangle transformed from local to global coordinates by the Accepted Local Axis contract.
2. Its four corners are ordered: local lower-left, lower-right, upper-right, upper-left, after transformation to global coordinates.
3. Corner order, cardinality, and rectangle dimensions remain stable under transformation.
4. The panel geometry is fully contained by the selected partition under the approved rule.
5. Source candidate, partition, Axis, and module data remain unchanged.

## 10. Placement Result

### Placement status

| Status | Meaning | Final |
|---|---|---:|
| `Not Evaluated` | A request context exists but validation has not completed. | No |
| `Evaluated` | Inputs are valid and candidate decisions are being accumulated; not eligible downstream. | No |
| `Accepted` | Validation and placement completed, including a valid zero-panel result. | Yes |
| `Rejected` | Validation failed or deterministic placement could not complete. | Yes |

Valid progression is `Not Evaluated` to `Evaluated` to `Accepted`, or `Not Evaluated`/`Evaluated` to `Rejected`. A final result is immutable and shall not be silently rewritten.

### Panel count

`accepted panel count` equals the number of panel geometries and accepted candidate decisions. Rejected candidates are excluded.

### Installed capacity

`installed capacity (kWp) = accepted panel count * rated module power (Wp) / 1000`

No inverter, string, efficiency, loss, electrical-routing, or rounding factor changes this value. Zero accepted panels produce exactly zero kWp.

### Result consistency

An Accepted result shall be internally consistent across candidate decisions, panel collection, identifiers, count, capacity, warnings, references, coordinate system, and units. Identical valid requests produce identical ordered result content.

## 11. Validation Rules

Validation shall deterministically verify:

1. exactly one non-empty placement request identifier exists;
2. every required dependency reference exists and resolves to a final `Accepted` result;
3. selection, partition, geometry set, roof, Axis, and module references agree;
4. coordinate-system identifiers agree and linear units are millimetres;
5. selected partition geometry is unchanged from the Accepted selection;
6. Local Axis data is unchanged and valid for the selected partition;
7. active module parameters are unchanged and satisfy PE-LAY-001;
8. effective dimensions and pitches are finite and positive, and gaps/margin are non-negative;
9. grid envelope and candidate sequence are finite and deterministic;
10. candidate sequence indices and row/column positions are unique and ordered;
11. every candidate has exactly one containment decision;
12. panel identifiers and placement orders are unique, contiguous, and deterministic;
13. each output panel corresponds to one accepted candidate and no rejected candidate;
14. count and capacity match section 10;
15. warnings match section 12;
16. placement status is valid; and
17. no source dependency or geometry mutation occurred.

All deterministically observable errors are returned in stable code order for identical input. Any error produces `Rejected`; warnings do not.

## 12. Warning Conditions

Each warning contains a stable code, placement request identifier, relevant count or row when applicable, and human-readable text consistent with the code.

| Warning code | Condition | Behavior |
|---|---|---|
| `PLC_NO_PANEL_FITS` | The usable grid envelope cannot generate a candidate, or no generated candidate is contained | Required on the valid zero-panel result |
| `PLC_EMPTY_PLACEMENT_RESULT` | Accepted panel count is zero | Same observable zero-result condition as no-fit; emitted after `PLC_NO_PANEL_FITS` |
| `PLC_UNUSED_AREA_REMAINS` | At least one generated candidate is rejected by partition containment | Reports unused candidate opportunity only; no polygon-area calculation is implied |
| `PLC_PARTIAL_ROW` | A generated row contains both accepted and rejected candidates | Reports that row's mixed decisions; no alternative filling is attempted |

Warning rules:

1. Warnings never invalidate an otherwise Accepted placement.
2. `PLC_NO_PANEL_FITS` and `PLC_EMPTY_PLACEMENT_RESULT` occur together exactly when count is zero.
3. They do not occur when count is positive.
4. `PLC_UNUSED_AREA_REMAINS` is not a measurement of residual polygon area; it is supported only by an observed rejected candidate.
5. One `PLC_PARTIAL_ROW` warning is emitted per qualifying row in ascending row order.
6. A row with only accepted candidates, only rejected candidates, or no candidates is not partial.
7. Warning order is the table order, with partial-row warnings secondarily ordered by row.
8. Warnings do not trigger retries, optimization, alternate orientation, clipping, or repair.

## 13. Error Conditions

| Error code | Condition |
|---|---|
| `PLC_REQUEST_INVALID` | Placement request identifier is missing, duplicated, or structurally invalid |
| `PLC_DEPENDENCY_MISSING` | A required dependency reference is absent or cannot resolve |
| `PLC_DEPENDENCY_NOT_ACCEPTED` | A dependency result is not final `Accepted` |
| `PLC_GEOMETRY_REFERENCE_INVALID` | Geometry, roof, selection, or partition references do not agree |
| `PLC_PARTITION_GEOMETRY_INVALID` | Selected partition geometry differs from Accepted dependency evidence |
| `PLC_AXIS_INVALID` | Local Axis reference is invalid, mismatched, mutated, or not Accepted |
| `PLC_MODULE_INVALID` | Module definition is invalid, mismatched, mutated, or not Accepted |
| `PLC_COORDINATE_SYSTEM_MISMATCH` | Coordinate-system identifiers disagree |
| `PLC_UNIT_INVALID` | Linear or power units do not match the Accepted contracts |
| `PLC_GRID_INVALID` | Grid envelope, dimensions, pitch, or candidate extent is non-finite or invalid |
| `PLC_CANDIDATE_ORDER_INVALID` | Candidate indices or row/column order are missing, duplicate, or non-deterministic |
| `PLC_CONTAINMENT_DECISION_INVALID` | A candidate has zero, multiple, or inconsistent decisions |
| `PLC_PANEL_IDENTIFIER_INVALID` | Panel identifier or placement order is missing, duplicate, non-contiguous, or unstable |
| `PLC_PANEL_GEOMETRY_INVALID` | Output panel geometry is not the corresponding accepted rectangle in global coordinates |
| `PLC_RESULT_INCONSISTENT` | Collection, count, capacity, warning, reference, or unit fields disagree |
| `PLC_PLACEMENT_FAILURE` | Valid inputs cannot complete the required finite deterministic workflow |
| `PLC_STATE_INVALID` | Claimed status contradicts validation or workflow state |
| `PLC_SOURCE_MUTATED` | Any Accepted dependency or source geometry changed |
| `PLC_RESULT_NONDETERMINISTIC` | Repeated identical input produces different candidates, decisions, panels, statistics, or warnings |

Errors are implementation-independent. A Rejected result contains at least one error and no valid partial placement result.

## 14. Acceptance Tests

| Test ID | Given | When | Required result |
|---|---|---|---|
| `AT-PLC-001` | Valid rectangular partition, zero rotation, and fitting module | Placement completes | Accepted ordered panels are fully contained |
| `AT-PLC-002` | Same valid request with a rotated Accepted Local Axis | Placement completes | Grid and global panel geometry follow the Axis deterministically |
| `AT-PLC-003` | One identical valid request repeated | Results are compared | Candidate sequence, decisions, identifiers, geometry, count, capacity, and warnings are identical |
| `AT-PLC-004` | Envelope cannot contain one module | Placement completes | Accepted zero-panel result has zero kWp and both zero-result warnings |
| `AT-PLC-005` | Exactly one candidate is contained | Placement completes | One `PNL-000001`, count one, and correct capacity are returned |
| `AT-PLC-006` | Valid envelope supports multiple rows and columns | Placement completes | Rows increase by local Y and columns by local X |
| `AT-PLC-007` | Candidate crosses the partition boundary | Containment is evaluated | Whole candidate is rejected and absent from panels/count/capacity |
| `AT-PLC-008` | Candidate touches the partition boundary without crossing | Containment is evaluated | Candidate is accepted |
| `AT-PLC-009` | Concave partition yields accepted and rejected candidates | Placement completes | Only fully contained candidates become panels |
| `AT-PLC-010` | Mixed accepted/rejected candidates in one row | Warnings are derived | Partial-row and unused-area warnings occur without rejection |
| `AT-PLC-011` | Rejected candidates exist but no row is mixed | Warnings are derived | Unused-area warning occurs; partial-row warning does not |
| `AT-PLC-012` | All generated candidates are accepted | Warnings are derived | No unused-area or partial-row warning occurs |
| `AT-PLC-013` | Some candidates are rejected before later accepted candidates | Panels are numbered | Accepted identifiers remain contiguous with no gap |
| `AT-PLC-014` | Accepted panel geometry is inspected | Corners are returned | Four global corners follow the required local-corner order |
| `AT-PLC-015` | Accepted count and positive Wp are known | Capacity is derived | kWp equals count times Wp divided by 1000 |
| `AT-PLC-016` | A required dependency reference is missing | Request is validated | Rejected with `PLC_DEPENDENCY_MISSING` |
| `AT-PLC-017` | A dependency is not Accepted | Request is validated | Rejected with `PLC_DEPENDENCY_NOT_ACCEPTED` |
| `AT-PLC-018` | Selection and partition references disagree | Request is validated | Rejected with `PLC_GEOMETRY_REFERENCE_INVALID` |
| `AT-PLC-019` | Axis belongs to another partition | Request is validated | Rejected with `PLC_AXIS_INVALID` |
| `AT-PLC-020` | Module result is invalid or changed | Request is validated | Rejected with `PLC_MODULE_INVALID` |
| `AT-PLC-021` | Coordinate-system identifiers disagree | Request is validated | Rejected with `PLC_COORDINATE_SYSTEM_MISMATCH` |
| `AT-PLC-022` | Units disagree with dependency contracts | Request is validated | Rejected with `PLC_UNIT_INVALID` |
| `AT-PLC-023` | Candidate order is duplicate or unstable | Result is validated | Rejected with `PLC_CANDIDATE_ORDER_INVALID` |
| `AT-PLC-024` | A rejected candidate appears in panel output | Result is validated | Rejected with `PLC_RESULT_INCONSISTENT` |
| `AT-PLC-025` | Panel IDs duplicate or skip placement order | Result is validated | Rejected with `PLC_PANEL_IDENTIFIER_INVALID` |
| `AT-PLC-026` | Panel count differs from geometry cardinality | Result is validated | Rejected with `PLC_RESULT_INCONSISTENT` |
| `AT-PLC-027` | Capacity differs from section 10 | Result is validated | Rejected with `PLC_RESULT_INCONSISTENT` |
| `AT-PLC-028` | Source partition, Axis, or module data changes | Result is validated | Rejected with `PLC_SOURCE_MUTATED` |
| `AT-PLC-029` | Valid zero-panel placement completes | Status is inspected | Status is Accepted, not Rejected or partial |
| `AT-PLC-030` | A final request changes any dependency or input | New placement is requested | New request identifier is required; prior final result remains unchanged |
| `AT-PLC-031` | A valid placement result is inspected | Scope is checked | No UI, rendering, DXF, import/export, optimization, AI, electrical, or structural output exists |

Acceptance evidence shall identify the request and dependency references, local envelope, ordered candidates, decisions, ordered panels, warnings, errors, status, count, capacity, determinism comparison, and immutability result. No test framework or implementation technique is prescribed.

## 15. Engineering Constraints

1. Only final Accepted dependency outputs are eligible inputs.
2. Exactly one selected partition, Local Axis, and active module apply to one request.
3. Placement follows the explicit Axis, effective module dimensions, gaps, margin, and pitches.
4. Full containment is mandatory; boundary contact is accepted.
5. Rejected candidates are never clipped, moved, rotated, or returned as panels.
6. Candidate and panel order are deterministic.
7. A valid zero-panel result is Accepted and warned.
8. Source inputs and final results are immutable.
9. No search, scoring, fallback, collision solving, or optimization is authorized.
10. No API, algorithm, library, language, architecture, persistence, UI, or rendering design is authorized.
11. No source code or approved Product or Engineering document is modified.
12. No DXF, data exchange, Product Sprint, or implementation work begins here.

## 16. Engineering Notes

1. **Primary mapping:** `PE-LAY-002` maps to `LAY-002`; supporting containment, ordered placement, and result behaviors remain traceable to already-approved capabilities and are not newly created.
2. **Sole parameter authority:** Dimensions, orientation, gaps, edge margin, pitch, and rated power come only from an Accepted PE-LAY-001 result.
3. **Geometry authority:** Polygon validity belongs to PE-GEO-001; selected-boundary identity belongs to PE-GEO-002; transformation behavior belongs to PE-AXS-001.
4. **Observable grid:** Envelope, ordering, and candidate outcomes are normative; iteration strategy and numeric representation are not.
5. **Containment boundary:** This specification neither adds tolerance nor chooses a geometry algorithm.
6. **Warning boundary:** No-fit is the approved baseline warning. The work-order-required empty, unused-area, and partial-row labels are strictly derived from result cardinality and existing candidate decisions; they do not create area analytics or optimization behavior.
7. **Unused area:** The warning means at least one rejected candidate, not a computed residual area or utilization percentage.
8. **Partial row:** The warning means mixed candidate decisions within an evaluated row, not an incomplete construction row or design defect.
9. **Installed capacity:** Capacity is nameplate arithmetic only, not electrical design or predicted energy.
10. **ENG-001 boundary:** After PM approval, this document may serve as the implementation contract for a separately governed ENG-001 Issue. It does not authorize implementation itself.

This specification becomes the approved PE-LAY-002 contract only after PM approval and merge under the [Development Constitution](../DEVELOPMENT_CONSTITUTION.md).
