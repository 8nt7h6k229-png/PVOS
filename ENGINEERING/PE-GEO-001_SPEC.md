# PE-GEO-001 — Explicit Roof & Partition Geometry Specification

Work item: [PE-GEO-001 / PVOS Issue #17](https://github.com/8nt7h6k229-png/PVOS/issues/17)

Primary Capability: [`GEO-001` — Explicit Polygon Geometry Input](../PRODUCT/PRODUCT_CAPABILITY_TREE.md)

Status: Proposed for PM approval

## 1. Purpose

This specification defines the engineering contract for receiving, validating, accepting, and rejecting explicit user-supplied roof and partition polygon geometry.

It translates the approved `GEO-001` product capability into implementation-independent behavior. It defines required data, observable results, validation rules, error conditions, and acceptance tests. It does not select an API, algorithm, software architecture, storage model, user interface, framework, or programming language.

Evidence:

- [PV Layout MVP Functional Specification](../PRODUCT/PV_LAYOUT_MVP_SPEC.md) requires user-supplied 2D roof and partition polygons in one coordinate system.
- [Product Capability Tree — GEO-001](../PRODUCT/PRODUCT_CAPABILITY_TREE.md) defines the purpose, inputs, outputs, and current boundary.
- [Product Backlog — PE-GEO-001](../PRODUCT/PRODUCT_BACKLOG.md) requires valid explicit roof and partition input acceptance evidence.

## 2. Scope

### Included

- one user-supplied roof polygon;
- one user-supplied collection of partition polygons;
- geometry and partition identifiers;
- two-dimensional coordinate and unit declarations;
- polygon, partition, and collection validation;
- all-or-nothing geometry acceptance;
- structured validation results and error conditions; and
- behavior-level acceptance tests.

### Excluded

- layout and panel placement;
- Local Axis assignment or transformation;
- PV module definition;
- statistics or installed-capacity calculation;
- visualization or rendering;
- DXF or other data-format behavior;
- import or export behavior;
- optimization;
- roof detection or automatic region recognition;
- automatic partition generation;
- polygon repair, simplification, splitting, merging, clipping, or offsetting;
- coordinate-system conversion; and
- software architecture or implementation design.

The contract accepts geometry as supplied or rejects the complete request. It does not modify geometry to make it acceptable.

## 3. Engineering Context

The PRODUCT-001 workflow begins with explicit geometry before partition selection, Local Axis, module parameters, or placement. `PE-GEO-001` owns only the boundary between user-supplied geometry and an accepted geometry set.

```text
User-supplied geometry
        ↓
PE-GEO-001 validation and acceptance
        ↓
Accepted roof + accepted partition collection + identifiers
```

Downstream capabilities may consume an Accepted result. They shall not consume a Rejected result as if it were valid geometry.

This specification refines `GEO-001`; it does not include `GEO-002` partition selection. Acceptance of a partition collection does not select a partition for layout.

## 4. Input Contract

One geometry-input request contains the following logical information.

### 4.1 Request metadata

| Field | Cardinality | Requirement |
|---|---:|---|
| Request identifier | Exactly one | Non-empty identifier used to correlate the validation result with the submitted request |
| Coordinate-system identifier | Exactly one | Non-empty identifier or agreed project-coordinate designation shared by every coordinate in the request |
| Linear unit | Exactly one | Millimetres |

The contract does not transform coordinates or units. The user supplies all coordinates in the declared system and unit.

### 4.2 Roof polygon

| Field | Cardinality | Requirement |
|---|---:|---|
| Roof identifier | Exactly one | Non-empty and unique within the request |
| Dimension | Exactly one | Two-dimensional |
| Coordinate-system reference | Exactly one | Equals the request coordinate-system identifier |
| Boundary | Exactly one | Closed polygon defined by an ordered cyclic vertex sequence |
| Vertices | At least three distinct | Finite X and Y values in the request coordinate system and millimetres |

### 4.3 Partition collection

The request contains one or more partitions.

Each partition contains:

| Field | Cardinality | Requirement |
|---|---:|---|
| Partition identifier | Exactly one | Non-empty and unique among partitions and distinct from the roof identifier |
| Dimension | Exactly one | Two-dimensional |
| Coordinate-system reference | Exactly one | Equals the request coordinate-system identifier |
| Boundary | Exactly one | Closed polygon defined by an ordered cyclic vertex sequence |
| Vertices | At least three distinct | Finite X and Y values in the shared coordinate system and millimetres |

The user supplies the complete partition collection. The contract does not discover, derive, generate, or select a partition.

## 5. Output Contract

One geometry-input request produces exactly one validation result.

### 5.1 Common result fields

| Field | Requirement |
|---|---|
| Request identifier | Equals the submitted request identifier |
| Validation status | Exactly one of `Accepted` or `Rejected` |
| Validation errors | Ordered collection of zero or more errors defined in §10 |

### 5.2 Accepted result

When status is `Accepted`, the result contains:

- the accepted roof identifier and polygon;
- every accepted partition identifier and polygon in the submitted collection order;
- the declared coordinate-system identifier;
- the millimetre unit declaration; and
- an empty validation-error collection.

Accepted coordinates and identifiers shall represent the submitted values. Acceptance shall not repair, simplify, reorder, split, merge, offset, or otherwise alter polygon meaning.

### 5.3 Rejected result

When status is `Rejected`, the result contains:

- no accepted roof polygon;
- no accepted partition polygons;
- one or more validation errors; and
- the submitted request identifier when it was available.

The contract does not partially accept a request. One invalid roof, partition, identifier, coordinate declaration, or collection rule rejects the complete request.

### 5.4 Prohibited outputs

The result contains no layout, Local Axis, panel placement, rendering, module information, or statistics.

## 6. Geometry Definition

### Point

A point is one ordered pair `(X, Y)` of finite numeric coordinates in the request's declared coordinate system and millimetre unit.

### Vertex sequence

A vertex sequence is the submitted order of polygon vertices. Consecutive vertices define consecutive boundary segments.

### Closed polygon

A closed polygon is a cyclic boundary in which the final logical boundary segment connects the last vertex to the first vertex. The input representation shall unambiguously express that cyclic closure. No open polyline is accepted as a polygon.

### Simple polygon

A simple polygon has one boundary, at least three distinct vertices, non-zero enclosed area, and no intersection or overlap between non-adjacent boundary segments. Adjacent segments meet only at their shared vertex. The polygon has no holes, curves, arcs, bulges, or three-dimensional coordinates.

### Roof polygon

The roof polygon is the single user-supplied simple polygon that defines the containing geometry context for the partition collection.

### Partition polygon

A partition polygon is a user-supplied simple polygon that is fully contained within, or on the boundary of, the roof polygon.

## 7. Polygon Rules

The roof and every partition shall satisfy all of the following rules:

1. The geometry is two-dimensional.
2. The boundary is closed.
3. The boundary contains at least three distinct vertices.
4. Every coordinate is finite.
5. Consecutive logical vertices are distinct; no boundary segment has zero length.
6. The polygon has non-zero enclosed area.
7. The polygon is simple and does not self-intersect or self-overlap.
8. Non-adjacent boundary segments do not touch at a vertex or along a segment.
9. The polygon uses the request's declared coordinate system and millimetre unit.
10. The polygon contains straight boundary segments only.

Vertex winding direction is not an acceptance criterion. Clockwise and counter-clockwise simple polygons are both valid and retain their submitted meaning.

## 8. Partition Rules

1. The request contains at least one partition.
2. Every partition is explicitly user supplied.
3. Every partition has one non-empty identifier.
4. Partition identifiers are unique within the collection.
5. The roof identifier and every partition identifier are mutually distinct.
6. Every partition polygon independently satisfies §7.
7. Every point in a partition boundary and interior lies inside or on the roof polygon.
8. A partition may touch the roof boundary.
9. A partition that crosses the roof boundary or has any portion outside the roof is invalid.
10. The collection order is preserved in the Accepted result.

Overlap, adjacency, or gaps between two otherwise valid partitions are not evaluated by `GEO-001`. This specification neither approves nor prohibits those inter-partition relationships; any product rule for them requires a separately governed capability contract.

## 9. Validation Rules

Validation is applied to one complete request and produces one deterministic status.

| Validation group | Accepted condition |
|---|---|
| Request | Request identifier, coordinate-system identifier, and millimetre unit are present |
| Roof | Exactly one identified polygon satisfies all polygon rules |
| Partition collection | At least one partition is present |
| Partitions | Every partition satisfies all polygon and partition rules |
| Identifiers | All geometry identifiers are non-empty and unique within the request |
| Coordinates | All points are 2D, finite, and interpreted in one declared coordinate system and unit |
| Containment | Every partition is fully inside or on the roof boundary |

Validation shall report all deterministically observable errors for the submitted request rather than treating the first error as acceptance of the remaining geometry. Error ordering shall be stable for identical input. The implementation may choose how validation is performed, provided the observable result conforms to this contract.

No warning state is defined. A request either satisfies every rule and is Accepted, or has at least one error and is Rejected.

## 10. Error Conditions

Each validation error contains:

- an error code;
- the affected geometry identifier when available;
- the affected submitted field or rule; and
- a human-readable explanation that does not contradict the code.

| Error code | Condition |
|---|---|
| `GEO_REQUEST_ID_REQUIRED` | Request identifier is absent or empty |
| `GEO_COORDINATE_SYSTEM_REQUIRED` | Coordinate-system identifier is absent or empty |
| `GEO_COORDINATE_SYSTEM_MISMATCH` | A roof or partition coordinate-system reference differs from the request coordinate-system identifier |
| `GEO_UNIT_INVALID` | Declared linear unit is absent or is not millimetres |
| `GEO_ROOF_REQUIRED` | Exactly one roof polygon was not supplied |
| `GEO_PARTITION_COLLECTION_EMPTY` | No partition was supplied |
| `GEO_IDENTIFIER_REQUIRED` | Roof or partition identifier is absent or empty |
| `GEO_IDENTIFIER_DUPLICATE` | A geometry identifier is repeated within the request |
| `GEO_DIMENSION_INVALID` | Geometry is not two-dimensional |
| `GEO_COORDINATE_INVALID` | A coordinate is not finite or cannot be interpreted in the declared coordinate system |
| `GEO_POLYGON_OPEN` | Submitted geometry does not define a closed cyclic boundary |
| `GEO_VERTEX_COUNT_INVALID` | Polygon has fewer than three distinct vertices |
| `GEO_ZERO_LENGTH_EDGE` | Two consecutive logical vertices define a zero-length boundary segment |
| `GEO_AREA_INVALID` | Polygon encloses no non-zero area |
| `GEO_POLYGON_NOT_SIMPLE` | Polygon self-intersects, self-touches at non-adjacent edges, or self-overlaps |
| `GEO_BOUNDARY_TYPE_UNSUPPORTED` | Boundary contains a curve, arc, bulge, hole, or unsupported non-linear/3D element |
| `GEO_PARTITION_OUTSIDE_ROOF` | Any part of a partition lies outside or crosses the roof polygon |

Multiple errors may be returned for one request. Error presence always corresponds to `Rejected`; an `Accepted` result contains no errors.

## 11. Acceptance Tests

The following are behavior-level tests. They define observable acceptance and rejection without prescribing test framework or implementation technique.

| ID | Given | When | Then |
|---|---|---|---|
| `AT-GEO-001` | One simple rectangular roof and one simple rectangular partition fully inside it, with valid identifiers and shared coordinates | Geometry is validated | Status is Accepted; submitted roof and partition are returned; errors are empty |
| `AT-GEO-002` | One simple concave roof and one simple partition fully inside it | Geometry is validated | Status is Accepted; concavity alone is not rejected |
| `AT-GEO-003` | One valid roof and multiple valid identified partitions inside it | Geometry is validated | Status is Accepted; all partitions are returned in submitted order |
| `AT-GEO-004` | The same valid request is submitted repeatedly | Each request is validated | Status, accepted identifiers, geometry meaning, collection order, and errors are identical |
| `AT-GEO-005` | A roof boundary is not closed | Geometry is validated | Status is Rejected with `GEO_POLYGON_OPEN`; no geometry is accepted |
| `AT-GEO-006` | A polygon has fewer than three distinct vertices | Geometry is validated | Status is Rejected with `GEO_VERTEX_COUNT_INVALID` |
| `AT-GEO-007` | A polygon contains consecutive duplicate logical vertices | Geometry is validated | Status is Rejected with `GEO_ZERO_LENGTH_EDGE` |
| `AT-GEO-008` | A polygon's vertices are collinear and enclose no area | Geometry is validated | Status is Rejected with `GEO_AREA_INVALID` |
| `AT-GEO-009` | A roof or partition boundary crosses itself | Geometry is validated | Status is Rejected with `GEO_POLYGON_NOT_SIMPLE` |
| `AT-GEO-010` | A partition is completely outside the roof | Geometry is validated | Status is Rejected with `GEO_PARTITION_OUTSIDE_ROOF` |
| `AT-GEO-011` | A partition crosses the roof boundary | Geometry is validated | Status is Rejected with `GEO_PARTITION_OUTSIDE_ROOF` |
| `AT-GEO-012` | A valid partition touches but does not cross the roof boundary | Geometry is validated | Containment passes; the request is Accepted if all other rules pass |
| `AT-GEO-013` | Two partitions have the same identifier, or a partition repeats the roof identifier | Geometry is validated | Status is Rejected with `GEO_IDENTIFIER_DUPLICATE` |
| `AT-GEO-014` | The partition collection is empty | Geometry is validated | Status is Rejected with `GEO_PARTITION_COLLECTION_EMPTY` |
| `AT-GEO-015` | A coordinate is non-finite | Geometry is validated | Status is Rejected with `GEO_COORDINATE_INVALID` |
| `AT-GEO-016` | A polygon's coordinate-system reference differs from the request declaration, or the request unit is not millimetres | Geometry is validated | Status is Rejected with `GEO_COORDINATE_SYSTEM_MISMATCH` or `GEO_UNIT_INVALID`, as applicable |
| `AT-GEO-017` | One partition is invalid while the roof and other partitions are valid | Geometry is validated | The complete request is Rejected; no roof or partition is partially accepted |
| `AT-GEO-018` | A valid request is accepted | The result is inspected | It contains no layout, placement, Local Axis, rendering, module, or statistics output |

Acceptance evidence for a future implementation shall identify the tested request, expected rule, actual status, returned error codes, and reviewed result.

## 12. Engineering Notes

1. **Contract boundary:** This document governs geometry input acceptance only. `GEO-002` governs later partition selection.
2. **No repair:** Invalid geometry is rejected. Automatic closing, deduplication, reordering, simplification, clipping, or other repair is outside scope.
3. **No detection:** Roof and partition polygons are user supplied. No inference or generation occurs.
4. **No algorithm prescription:** Terms such as simple, contained, and self-intersecting describe required outcomes. This specification does not prescribe how they are determined.
5. **No architecture prescription:** Logical fields and results do not mandate classes, endpoints, files, databases, services, libraries, or UI controls.
6. **No partial acceptance:** Downstream work receives one fully Accepted geometry set or no accepted geometry.
7. **Stable evidence:** Identical input produces the same status, geometry identifiers, collection order, and ordered error result.
8. **Baseline control:** Any request to add automatic detection, partition generation, geometry repair, new geometry types, coordinate conversion, or downstream layout behavior requires separate capability and baseline governance.

This specification becomes the engineering contract for `GEO-001` only after PM approval and merge. Implementation work remains subject to a separate governed Issue and the [Development Constitution](../DEVELOPMENT_CONSTITUTION.md).
