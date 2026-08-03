# PE-AXS-001 — Local Axis Engineering Specification

Work item: [PE-AXS-001 / PVOS Issue #21](https://github.com/8nt7h6k229-png/PVOS/issues/21)

Primary Capability: [`AXS-001` — Partition-specific Local Axis](../PRODUCT/PRODUCT_CAPABILITY_TREE.md)

Dependencies: [PE-GEO-001](PE-GEO-001_SPEC.md) and [PE-GEO-002](PE-GEO-002_SPEC.md)

Status: Proposed for PM approval

## 1. Purpose

This specification defines the observable engineering contract for assigning and using one two-dimensional Local Axis on one PE-GEO-002 Accepted selected partition.

It defines logical inputs, outputs, origin and rotation semantics, global/local transformation behavior, validation, errors, states, and behavior-level acceptance tests. It does not define an API, formula, matrix representation, algorithm, software architecture, user interface, storage model, geometry library, framework, or programming language.

Evidence:

- [PVOS 1.0 Product Baseline](../PM/PRODUCT_BASELINE.md) includes partition-specific Local Axis transformation.
- [PV Layout MVP Functional Specification §7](../PRODUCT/PV_LAYOUT_MVP_SPEC.md) defines an explicit origin, degree rotation, local X/Y alignment, global/local interpretation, and repeatability.
- [Product Capability Tree — AXS-001](../PRODUCT/PRODUCT_CAPABILITY_TREE.md) defines the capability purpose, dependency, inputs, and output boundary.
- [Product Backlog — PE-AXS-001](../PRODUCT/PRODUCT_BACKLOG.md) requires repeatable Local Axis acceptance examples after `GEO-002`.
- The approved existing geometry asset documents a default linear comparison tolerance of `1e-6 mm`: [PVOS.Geometry README](https://github.com/8nt7h6k229-png/PvLayoutPlugin/blob/main/src/r5d_src/PVOS.Geometry/README.md).

## 2. Scope

### Included

- one PE-GEO-002 Accepted selected partition;
- one user-supplied origin point;
- one user-supplied rotation in degrees;
- one partition-specific right-handed 2D Local Axis;
- local-to-global point transformation behavior;
- global-to-local point transformation behavior;
- ordered point-collection transformation behavior;
- deterministic and reversible results within the approved linear tolerance;
- immutable selected-partition source geometry;
- axis validation, states, stable error conditions, and acceptance tests.

### Excluded

- geometry creation, repair, or partition selection;
- automatic Local Axis generation, inference, recommendation, or optimization;
- magnetic north, true north, solar azimuth, roof slope, or three-dimensional orientation;
- PV module definition or orientation comparison;
- grid or panel-candidate generation;
- boundary containment or panel placement;
- statistics;
- visualization, rendering, or UI behavior;
- DXF or other data-format behavior;
- import or export behavior;
- electrical or structural design;
- source-code implementation; and
- architecture or implementation design.

## 3. Engineering Context

PE-AXS-001 begins only with one final `Accepted` result from PE-GEO-002.

```text
PE-GEO-002 Accepted selected partition
        +
User-supplied origin and rotation
        ↓
PE-AXS-001 validation
        ↓
Accepted partition-specific Local Axis
        +
Deterministic global/local transformation behavior
```

The Local Axis establishes the coordinate relationship used by future capabilities. This specification does not generate layout content in either coordinate system.

## 4. Input Contract

One Local Axis request contains the following logical information.

| Field | Cardinality | Requirement |
|---|---:|---|
| Axis request identifier | Exactly one | Non-empty identifier used to correlate input and result |
| Accepted selection reference | Exactly one | Resolves to one final PE-GEO-002 result with state `Accepted` |
| Selected partition identifier | Exactly one | Equals the partition identifier in the Accepted selection |
| Selected partition geometry | Exactly one | Equals the immutable geometry in the Accepted selection |
| Local Axis origin | Exactly one | User-supplied finite 2D point in the shared global coordinate system |
| Local Axis rotation | Exactly one | User-supplied finite numeric angle in degrees |
| Coordinate-system identifier | Exactly one | Equals the accepted geometry coordinate-system identifier |
| Linear unit | Exactly one | Millimetres |

The Local Axis belongs only to the referenced selected partition. The request shall not replace or edit accepted partition geometry.

The Local Axis identifier in an Accepted output is the accepted Axis request identifier. No separate identifier-generation behavior is defined.

## 5. Output Contract

One Axis request produces exactly one Axis result.

### 5.1 Common result fields

| Field | Requirement |
|---|---|
| Axis request identifier | Equals the submitted identifier when available |
| Accepted selection reference | Equals the validated PE-GEO-002 reference when available |
| Selected partition identifier | Equals the validated selected partition identifier when available |
| Axis state | Exactly one state defined in §12 |
| Validation result | Ordered collection of zero or more errors defined in §11 |

### 5.2 Accepted result

When state is `Accepted`, the result contains:

- Local Axis identifier equal to the Axis request identifier;
- accepted origin in global coordinates and millimetres;
- accepted supplied rotation in degrees;
- the defined local positive X and positive Y directions;
- the shared coordinate-system identifier;
- local-to-global transformation behavior;
- global-to-local transformation behavior; and
- an empty validation-error collection.

### 5.3 Rejected result

When state is `Rejected`, the result contains:

- no Accepted Local Axis;
- no transformation eligible for downstream Layout work; and
- one or more validation errors.

### 5.4 Prohibited outputs

The result contains no module data, grid, panel candidate, placement, boundary-containment result, statistic, rendering, or data-format result.

## 6. Local Axis Definition

One Local Axis is a two-dimensional orthonormal, right-handed coordinate frame associated with exactly one selected partition.

It has:

- one origin expressed in the shared global coordinate system;
- one local positive X direction established by the accepted rotation;
- one local positive Y direction perpendicular to local positive X and rotated 90 degrees counter-clockwise from it;
- unit scale, so one local millimetre equals one global millimetre; and
- a reversible relationship with the shared global coordinate system.

At zero-degree rotation:

- local positive X has the same direction as global positive X; and
- local positive Y has the same direction as global positive Y.

The axis is theoretical product behavior. This specification does not require direction vectors, matrices, trigonometric functions, or any other representation to be exposed or stored.

## 7. Origin Rules

1. Exactly one origin is explicitly supplied by the user.
2. The origin contains exactly two finite numeric coordinates.
3. The origin uses the Accepted geometry coordinate system.
4. Origin coordinates are interpreted in millimetres.
5. The origin belongs to the selected partition's Axis context through the accepted selection reference.
6. The origin maps to local point `(0, 0)`.
7. Local point `(0, 0)` maps to the accepted global origin.
8. The origin does not alter the selected partition geometry.

### Origin-containment boundary

The approved Product Baseline and PRODUCT-001 specification do not require the origin to be inside or on the selected partition. Existing Local Axis evidence accepts an explicit global origin without a containment rule.

Therefore origin containment is **not an acceptance criterion** for AXS-001:

- an origin inside the partition is not rejected because of location;
- an origin on the boundary is not rejected because of location; and
- an origin outside the partition is not rejected because of location.

This does not assign product meaning to an outside origin. Any future rule requiring an inside, boundary, selected-edge, centroid, or other derived origin requires PM disposition and a governed baseline change; it shall not be inferred by implementation.

## 8. Orientation and Rotation Rules

1. Exactly one rotation value is explicitly supplied by the user.
2. Rotation is a finite numeric value expressed in degrees.
3. The reference direction is global positive X.
4. Positive rotation is counter-clockwise when viewed in the shared two-dimensional coordinate plane.
5. Local positive X equals the direction established by the supplied rotation from global positive X.
6. Local positive Y is 90 degrees counter-clockwise from local positive X.
7. The basis is right-handed and orthonormal at unit scale.
8. Any finite degree value is accepted; no restricted input interval is established.
9. The accepted result preserves the supplied rotation value. Canonical numeric normalization is not required.
10. Rotations that differ by an integer multiple of 360 degrees are transformation-equivalent within the approved acceptance tolerance.
11. Equivalent angles may retain different supplied rotation values while producing equivalent coordinate results.
12. Identical valid requests produce identical Axis states and coordinate results.

No orientation is derived from roof geometry, partition edges, north, slope, sun position, module orientation, or a scoring rule.

## 9. Coordinate Transformation Rules

### 9.1 Global to local

Global-to-local behavior shall:

- interpret the input point in the shared global coordinate system and millimetres;
- express the point relative to the accepted origin and Local Axis directions;
- map the accepted origin to local `(0, 0)`;
- preserve distance and unit scale within the approved tolerance; and
- leave the input point and selected partition unchanged.

### 9.2 Local to global

Local-to-global behavior shall:

- interpret the input as local millimetre coordinates;
- express the corresponding point in the shared global coordinate system;
- map local `(0, 0)` to the accepted origin;
- preserve distance and unit scale within the approved tolerance; and
- leave the input point and selected partition unchanged.

### 9.3 Reversibility

For every finite point within the supported coordinate domain:

- global → local → global returns a point within `1e-6 mm` of the original global point; and
- local → global → local returns a point within `1e-6 mm` of the original local point.

Distance for this acceptance boundary is the ordinary 2D point-to-point distance. The tolerance defines required observable accuracy; it does not prescribe numeric type or technique.

### 9.4 Ordered collections

When an ordered point collection is transformed:

- output cardinality equals input cardinality;
- output point at each index corresponds to the input point at that same index;
- no point is inserted, removed, or reordered;
- repeated points remain repeated at their corresponding positions; and
- the input collection remains unchanged.

### 9.5 Determinism and equivalence

Identical Axis and point inputs produce identical outputs under the same declared coordinate contract. Transformation-equivalent angles produce outputs within `1e-6 mm` of each other for the same points.

## 10. Validation Rules

Validation applies to one complete Axis request.

| Validation group | Accepted condition |
|---|---|
| Axis request | One non-empty Axis request identifier is present |
| Selection reference | Resolves to one final PE-GEO-002 `Accepted` result |
| Partition reference | Identifier and geometry equal the Accepted selected partition |
| Coordinate system | Equals the Accepted geometry coordinate-system identifier |
| Unit | Millimetres |
| Origin | Exactly one finite 2D point is present |
| Rotation | Exactly one finite degree value is present |
| Axis basis | Defines one right-handed orthonormal 2D basis at unit scale |
| Transform behavior | Global/local behavior is deterministic and reversible within `1e-6 mm` |
| Axis state | Input and result form a valid state under §12 |
| Immutability | Selected partition geometry and submitted point collections are unchanged |

Origin position relative to the selected partition is not validated under the current baseline.

The final state is `Accepted` only when all applicable validation groups pass. Any validation error produces `Rejected`, and the result is ineligible for downstream Layout work.

Validation shall report all deterministically observable errors in stable order for identical input. No warning state and no partial Axis acceptance are defined.

## 11. Error Conditions

Each Axis error contains a stable error code, Axis request identifier when available, relevant selection or partition reference when available, and a human-readable explanation consistent with the code.

| Error code | Condition |
|---|---|
| `AXS_REQUEST_ID_REQUIRED` | Axis request identifier is absent or empty |
| `AXS_SELECTION_REFERENCE_INVALID` | Selection reference is absent, unresolved, or does not identify a final PE-GEO-002 Accepted result |
| `AXS_PARTITION_REFERENCE_MISMATCH` | Supplied partition identifier or geometry differs from the Accepted selection |
| `AXS_COORDINATE_SYSTEM_MISMATCH` | Axis coordinate-system identifier differs from the Accepted geometry coordinate system |
| `AXS_UNIT_INVALID` | Linear unit is absent or is not millimetres |
| `AXS_ORIGIN_REQUIRED` | Origin is absent or more than one origin is supplied |
| `AXS_ORIGIN_INVALID` | Origin is not two-dimensional or contains a non-finite coordinate |
| `AXS_ROTATION_REQUIRED` | Rotation is absent or more than one rotation is supplied |
| `AXS_ROTATION_INVALID` | Rotation is non-numeric or non-finite |
| `AXS_BASIS_DEGENERATE` | The resulting Axis cannot define two unit, perpendicular directions at unit scale |
| `AXS_HANDEDNESS_INVALID` | Resulting local Y direction is not the required counter-clockwise perpendicular to local X |
| `AXS_STATE_INVALID` | Supplied data and claimed or prior Axis state contradict §12 |
| `AXS_TRANSFORM_NOT_REVERSIBLE` | A required point round trip differs from its source by more than `1e-6 mm` |
| `AXS_TRANSFORM_NONDETERMINISTIC` | Identical valid Axis and point inputs do not reproduce the same coordinate result |
| `AXS_SOURCE_GEOMETRY_MUTATED` | Selected partition geometry changes during Axis assignment or transformation |
| `AXS_POINT_COLLECTION_MUTATED` | Ordered source points are inserted, removed, reordered, or changed by the transformation request |

Error presence always corresponds to `Rejected`; an `Accepted` result contains no errors.

## 12. Axis State

Axis state describes engineering status, not UI behavior.

| State | Meaning | Axis eligible downstream? | Validation errors |
|---|---|---:|---:|
| `Not Defined` | An Axis request context exists but origin or rotation has not been fully supplied. | No | None before validation; required-field errors if validation is requested |
| `Defined` | Exactly one origin and one rotation have been supplied and await validation. | No | None before validation |
| `Accepted` | Selection, origin, rotation, basis, transformation, and immutability rules pass. | Yes | Empty |
| `Rejected` | One or more Axis rules fail. | No | One or more |

### Valid progression

- `Not Defined` may become `Defined` when one origin and one rotation are supplied.
- `Not Defined` becomes `Rejected` if validation is requested with a missing required definition.
- `Defined` becomes `Accepted` when validation succeeds.
- `Defined` becomes `Rejected` when validation fails.
- `Accepted` and `Rejected` are final for that Axis request identifier.

A changed origin, rotation, selected partition, coordinate system, or unit requires a new Axis request identifier. A final Axis result shall not be silently rewritten.

The contract does not require intermediate-state persistence. If states are exposed or recorded, their observable meaning shall conform to this section.

## 13. Acceptance Tests

The following behavior-level tests define observable results without prescribing a test framework or implementation technique.

| ID | Given | When | Then |
|---|---|---|---|
| `AT-AXS-001` | One Accepted selected partition, finite origin, and rotation `0°` | Axis is validated | State is Accepted; local directions align with global X/Y; origin maps to local `(0,0)` |
| `AT-AXS-002` | One valid request with rotation `30°` | Axis is validated | State is Accepted; positive rotation and right-handed direction behavior match §§6 and 8 |
| `AT-AXS-003` | Equivalent requests with rotations `30°`, `390°`, and `-330°` | The same points are transformed | Results are equivalent within `1e-6 mm`; supplied rotation values may remain distinct |
| `AT-AXS-004` | The same valid Axis request and points are repeated | Results are compared | State and coordinate results are identical |
| `AT-AXS-005` | An Accepted Axis and local point `(0,0)` | Point is transformed to global | Result equals the accepted origin within `1e-6 mm` |
| `AT-AXS-006` | An Accepted Axis and its global origin | Point is transformed to local | Result equals `(0,0)` within `1e-6 mm` |
| `AT-AXS-007` | An Accepted Axis and finite global points | Each point completes global → local → global | Every result is within `1e-6 mm` of its source |
| `AT-AXS-008` | An Accepted Axis and finite local points | Each point completes local → global → local | Every result is within `1e-6 mm` of its source |
| `AT-AXS-009` | An ordered point collection containing distinct and repeated points | Collection is transformed | Cardinality and index correspondence are preserved; source is unchanged |
| `AT-AXS-010` | Origin is missing or multiple origins are supplied | Axis is validated | State is Rejected with `AXS_ORIGIN_REQUIRED` |
| `AT-AXS-011` | Origin has a non-finite coordinate or is not 2D | Axis is validated | State is Rejected with `AXS_ORIGIN_INVALID` |
| `AT-AXS-012` | Rotation is missing or multiple values are supplied | Axis is validated | State is Rejected with `AXS_ROTATION_REQUIRED` |
| `AT-AXS-013` | Rotation is non-finite | Axis is validated | State is Rejected with `AXS_ROTATION_INVALID` |
| `AT-AXS-014` | Selection reference does not resolve to PE-GEO-002 Accepted | Axis is validated | State is Rejected with `AXS_SELECTION_REFERENCE_INVALID` |
| `AT-AXS-015` | Partition identifier or geometry differs from the Accepted selection | Axis is validated | State is Rejected with `AXS_PARTITION_REFERENCE_MISMATCH` |
| `AT-AXS-016` | Coordinate-system identifier differs from Accepted geometry | Axis is validated | State is Rejected with `AXS_COORDINATE_SYSTEM_MISMATCH` |
| `AT-AXS-017` | Unit is not millimetres | Axis is validated | State is Rejected with `AXS_UNIT_INVALID` |
| `AT-AXS-018` | Claimed basis is degenerate or not right-handed | Axis is validated | State is Rejected with `AXS_BASIS_DEGENERATE` or `AXS_HANDEDNESS_INVALID` |
| `AT-AXS-019` | Request claims Accepted before validation or combines a final state with contradictory data | Axis is validated | State is Rejected with `AXS_STATE_INVALID` |
| `AT-AXS-020` | A point round trip exceeds `1e-6 mm` | Axis conformance is validated | State is Rejected with `AXS_TRANSFORM_NOT_REVERSIBLE` |
| `AT-AXS-021` | A valid Axis request uses an origin inside, on, or outside the partition | Axis is validated | Origin location alone does not cause rejection; all three follow the same non-containment rule |
| `AT-AXS-022` | A valid Axis is Accepted | Source partition geometry is compared before and after Axis use | Geometry and vertex order remain unchanged |
| `AT-AXS-023` | A prior request is final and origin or rotation changes | The changed definition is submitted | A new Axis request identifier is required; prior result remains unchanged |
| `AT-AXS-024` | A valid Axis is Accepted | Result is inspected | No module, grid, panel, containment, placement, statistic, rendering, or data-format output exists |

Acceptance evidence for a future implementation shall identify the Axis request, selection reference, origin, supplied rotation, tested points, expected state, actual state, error codes, tolerance comparison, and immutability result.

## 14. Engineering Constraints

1. The Axis consumes one PE-GEO-002 Accepted selected partition.
2. Origin and rotation are explicitly user supplied.
3. No axis, origin, or rotation is inferred, recommended, or optimized.
4. One Axis belongs to exactly one selected partition.
5. The shared coordinate system and millimetre unit are preserved.
6. The Local Axis is right-handed, orthonormal, two-dimensional, and unit scale.
7. Equivalent-angle and repeated-input behavior is deterministic.
8. Required point round trips satisfy the `1e-6 mm` acceptance boundary.
9. Selected partition geometry and input point collections remain immutable.
10. A Rejected Axis is not eligible for downstream Layout work.
11. Origin containment shall not be added without PM disposition and governed baseline change.
12. No API, formula, matrix, algorithm, library, language, architecture, UI, module, grid, placement, or Product Sprint work is authorized here.

## 15. Engineering Notes

1. **Coordinate contract:** AXS-001 connects Accepted selected geometry to future coordinate-aware behavior; it does not create that future behavior.
2. **Primary capability:** Every requirement in this document maps only to `AXS-001`.
3. **Dependency ownership:** PE-GEO-001 owns polygon acceptance; PE-GEO-002 owns partition selection; PE-AXS-001 owns the selected partition's coordinate frame.
4. **Tolerance authority:** `1e-6 mm` is the approved existing linear tolerance boundary. The specification uses the value without prescribing a library or numeric representation.
5. **Orientation preservation:** Supplied degree values need not be numerically normalized; transformation equivalence is the acceptance requirement.
6. **Origin uncertainty preserved:** No containment meaning is inferred. A future containment rule requires explicit PM governance.
7. **No algorithm prescription:** Transformation and reversibility are required outcomes. The means remain an implementation decision.
8. **No architecture prescription:** Logical requests, references, states, and results do not mandate services, endpoints, classes, files, databases, or queues.
9. **Phase boundary:** Approval completes the Local Axis Engineering Specification only. PE-LAY and Product Sprint implementation remain separate governed work.

This specification becomes the engineering contract for `AXS-001` only after PM approval and merge. Implementation remains subject to a separate governed Issue and the [Development Constitution](../DEVELOPMENT_CONSTITUTION.md).
