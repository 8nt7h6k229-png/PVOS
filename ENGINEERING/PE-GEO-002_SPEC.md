# PE-GEO-002 — Supplied Partition Selection Specification

Work item: [PE-GEO-002 / PVOS Issue #19](https://github.com/8nt7h6k229-png/PVOS/issues/19)

Primary Capability: [`GEO-002` — User-supplied Partition Selection](../PRODUCT/PRODUCT_CAPABILITY_TREE.md)

Dependency: [PE-GEO-001 — Explicit Roof & Partition Geometry Specification](PE-GEO-001_SPEC.md)

Status: Proposed for PM approval

## 1. Purpose

This specification defines the engineering contract for selecting exactly one user-supplied partition from one geometry set already accepted under PE-GEO-001.

It defines logical inputs, observable selection states, validation behavior, outputs, error conditions, and acceptance tests. It does not define an API, algorithm, architecture, user interface, storage model, framework, or programming language.

Evidence:

- [PV Layout MVP Functional Specification](../PRODUCT/PV_LAYOUT_MVP_SPEC.md) requires the user to select exactly one supplied partition for one layout operation.
- [Product Capability Tree — GEO-002](../PRODUCT/PRODUCT_CAPABILITY_TREE.md) defines selection purpose, dependency, inputs, outputs, and exclusion of automatic partition generation.
- [Product Backlog — PE-GEO-002](../PRODUCT/PRODUCT_BACKLOG.md) requires demonstrated selection of one supplied partition after `GEO-001`.
- [PE-GEO-001](PE-GEO-001_SPEC.md) defines the accepted roof geometry and accepted partition collection consumed by this contract.

## 2. Scope

### Included

- one PE-GEO-001 Accepted geometry set;
- one accepted roof reference;
- one accepted partition collection;
- one user-supplied selected partition identifier;
- one selection request identifier;
- exactly-one selection validation;
- geometry-set and partition-membership validation;
- immutable selected-partition result;
- selection states and stable error conditions; and
- behavior-level acceptance tests.

### Excluded

- geometry creation, repair, or revalidation of polygon shape;
- automatic partition selection, ranking, recommendation, or generation;
- Local Axis;
- PV module definition;
- layout, placement, or grid generation;
- geometric boundary validation for panels;
- rendering, visualization, or UI behavior;
- statistics;
- DXF or other data-format behavior;
- import or export behavior;
- optimization;
- roof detection; and
- software architecture or implementation design.

This contract identifies one accepted partition. It does not perform any downstream operation with that partition.

## 3. Engineering Context

PE-GEO-002 begins only after PE-GEO-001 has produced an `Accepted` geometry result.

```text
PE-GEO-001 Accepted geometry set
        +
User-supplied partition identifier
        ↓
PE-GEO-002 selection validation
        ↓
Accepted selected partition or Rejected selection
```

One selection request represents the partition choice for one future Layout Job. The Layout Job itself, its Local Axis, module data, and placement result are outside this specification.

PE-GEO-002 trusts accepted polygon meaning from PE-GEO-001 but verifies that the supplied geometry reference and partition collection still satisfy the selection preconditions defined here. It does not repeat polygon-shape or roof-containment validation.

## 4. Input Contract

One partition-selection request contains the following logical information.

### 4.1 Selection request

| Field | Cardinality | Requirement |
|---|---:|---|
| Selection request identifier | Exactly one | Non-empty identifier used to correlate input and result |
| Geometry-set reference | Exactly one | Identifies one PE-GEO-001 result whose validation status is `Accepted` |
| Roof identifier | Exactly one | Equals the accepted roof identifier in the referenced geometry set |
| Accepted partition collection | Exactly one collection | Contains the accepted partitions associated with the referenced roof |
| Selected partition identifier | Exactly one | User-supplied identifier naming one member of the accepted partition collection |

The selected partition identifier is a scalar logical choice. If an incoming representation supplies zero or more than one candidate identifier, it does not satisfy the input contract and is rejected under §8.

### 4.2 Accepted geometry-set preconditions

The referenced PE-GEO-001 result shall:

- have status `Accepted`;
- contain one accepted roof identifier and polygon;
- contain one or more accepted partitions;
- contain unique, non-empty geometry identifiers;
- associate every accepted partition with that roof geometry set; and
- contain no PE-GEO-001 validation errors.

Geometry values are read-only inputs to selection. The selection request shall not carry replacement or edited geometry.

### 4.3 User-supplied choice

The choice originates from the user or from an upstream caller acting on the user's explicit choice. The product shall not infer a choice from partition order, area, identifier value, geometry, previous selection, or any other attribute.

## 5. Output Contract

One selection request produces exactly one selection result.

### 5.1 Common result fields

| Field | Requirement |
|---|---|
| Selection request identifier | Equals the submitted identifier when available |
| Geometry-set reference | Equals the validated input reference when available |
| Selection state | Exactly one state defined in §9 |
| Validation result | Ordered collection of zero or more selection errors |

### 5.2 Accepted result

When the final state is `Accepted`, the result contains:

- the selection request identifier;
- the accepted geometry-set reference;
- the accepted roof identifier;
- the selected partition identifier;
- the exact selected partition geometry from the accepted collection; and
- an empty validation-error collection.

The selected partition geometry and identifier retain the accepted PE-GEO-001 meaning. The selection result shall not reorder vertices, change coordinates, replace identifiers, repair geometry, or create a new partition.

### 5.3 Rejected result

When the final state is `Rejected`, the result contains:

- the selection request identifier when available;
- no accepted selected partition;
- no geometry eligible for downstream use; and
- one or more selection errors.

### 5.4 Prohibited outputs

The selection result contains no layout, Local Axis, module placement, grid, panel boundary validation, rendering, or statistics.

## 6. Partition Selection Rules

1. One selection request corresponds to one future Layout Job partition choice.
2. Exactly one selected partition identifier is accepted per request.
3. The selected identifier is explicitly supplied; no automatic selection occurs.
4. Only a partition contained in the referenced PE-GEO-001 Accepted partition collection is selectable.
5. The selected partition shall belong to the accepted roof geometry identified by the request.
6. Identifier equality determines which accepted partition is selected; collection position does not.
7. Reordering an otherwise identical accepted partition collection shall not change the selected partition.
8. The selected partition geometry is returned without mutation.
9. Selection does not remove, modify, reorder, or otherwise change the accepted source collection.
10. Identical valid selection inputs produce the same selected identifier, geometry, final state, and validation result.
11. A different selected partition requires a distinct selection request; an Accepted result is not silently rewritten.
12. No fallback partition is selected when the requested identifier is invalid.

## 7. Validation Rules

Validation applies to the complete selection request.

| Validation group | Accepted condition |
|---|---|
| Selection request | One non-empty selection request identifier is present |
| Geometry reference | The reference resolves to the intended PE-GEO-001 `Accepted` result |
| Roof reference | The supplied roof identifier equals the accepted roof identifier |
| Partition collection | One or more accepted partitions are present |
| Identifier integrity | Accepted partition identifiers are non-empty and unique |
| Selection cardinality | Exactly one selected partition identifier is supplied |
| Selection membership | The selected identifier names exactly one member of the accepted partition collection |
| Selection state | The state and supplied data form one valid state defined in §9 |

The final state is `Accepted` only when every validation group passes. Any error produces `Rejected` and no accepted selected partition.

Validation shall report all deterministically observable selection errors. Error ordering shall be stable for identical input. No warning state and no partial selection are defined.

## 8. Error Conditions

Each selection error contains:

- a stable error code;
- the selection request identifier when available;
- the geometry-set, roof, or partition identifier relevant to the failure when available; and
- a human-readable explanation consistent with the code.

| Error code | Condition |
|---|---|
| `SEL_REQUEST_ID_REQUIRED` | Selection request identifier is absent or empty |
| `SEL_SELECTION_REQUIRED` | No selected partition identifier is supplied |
| `SEL_MULTIPLE_SELECTIONS` | More than one selected partition identifier is supplied |
| `SEL_PARTITION_UNKNOWN` | The selected identifier does not name a member of the accepted partition collection |
| `SEL_GEOMETRY_REFERENCE_INVALID` | Geometry-set reference is absent, unresolved, refers to a non-Accepted PE-GEO-001 result, or does not match the supplied accepted geometry |
| `SEL_ROOF_REFERENCE_INVALID` | Supplied roof identifier does not equal the accepted roof identifier in the referenced geometry set |
| `SEL_PARTITION_COLLECTION_EMPTY` | Referenced accepted partition collection contains no partition |
| `SEL_PARTITION_ID_REQUIRED` | An accepted partition has an absent or empty identifier |
| `SEL_PARTITION_ID_DUPLICATE` | Accepted partition identifiers are not unique |
| `SEL_PARTITION_MEMBERSHIP_INVALID` | A partition presented as selectable is not associated with the referenced accepted roof geometry set |
| `SEL_STATE_INVALID` | Supplied data and claimed or prior selection state form a state not permitted by §9 |

The duplicate, empty-collection, identifier, and membership errors defend the PE-GEO-001 dependency boundary. Their presence indicates that the referenced geometry cannot be treated as a valid Accepted geometry set for selection.

## 9. Selection State

Selection state describes observable engineering status, not UI behavior.

| State | Meaning | Selected partition available? | Validation errors |
|---|---|---:|---:|
| `Not Selected` | A selection request context exists, but no candidate partition identifier has been supplied. | No | None before validation; missing-selection error if validation is requested |
| `Selected` | Exactly one candidate partition identifier has been supplied and awaits validation against the Accepted geometry set. | Candidate only; not eligible downstream | None before validation |
| `Accepted` | The candidate and every selection precondition pass validation. | Yes | Empty |
| `Rejected` | One or more selection rules fail validation. | No | One or more |

### Valid state progression

- `Not Selected` may become `Selected` when exactly one user-supplied candidate identifier is associated with the request.
- `Not Selected` becomes `Rejected` if validation is requested without a candidate identifier.
- `Selected` becomes `Accepted` when validation succeeds.
- `Selected` becomes `Rejected` when validation fails.
- `Accepted` and `Rejected` are final for that selection request identifier.

A new choice is represented by a new selection request. This preserves the evidence of the earlier final result and prevents silent mutation.

The contract does not require an implementation to persist intermediate states. If states are exposed or recorded, their observable meaning shall conform to this section.

## 10. Acceptance Tests

The following behavior-level tests define observable results without prescribing test framework or implementation technique.

| ID | Given | When | Then |
|---|---|---|---|
| `AT-SEL-001` | One PE-GEO-001 Accepted geometry set and one selected identifier naming a member partition | Selection is validated | State is Accepted; exact identifier and immutable partition geometry are returned; errors are empty |
| `AT-SEL-002` | The same valid geometry set and selected identifier are submitted repeatedly | Each request is validated | Selected identifier, geometry meaning, final state, and errors are identical |
| `AT-SEL-003` | The accepted collection is reordered but contains the same uniquely identified partitions and the same selected identifier | Selection is validated | The same partition is Accepted; its geometry is unchanged |
| `AT-SEL-004` | No selected partition identifier is supplied | Selection is validated | State is Rejected with `SEL_SELECTION_REQUIRED`; no partition is returned |
| `AT-SEL-005` | More than one candidate identifier is supplied | Selection is validated | State is Rejected with `SEL_MULTIPLE_SELECTIONS` |
| `AT-SEL-006` | One selected identifier is not present in the accepted collection | Selection is validated | State is Rejected with `SEL_PARTITION_UNKNOWN`; no fallback is selected |
| `AT-SEL-007` | Geometry-set reference is absent or unresolved | Selection is validated | State is Rejected with `SEL_GEOMETRY_REFERENCE_INVALID` |
| `AT-SEL-008` | Referenced PE-GEO-001 result has status Rejected | Selection is validated | State is Rejected with `SEL_GEOMETRY_REFERENCE_INVALID` |
| `AT-SEL-009` | Supplied roof identifier differs from the accepted roof identifier | Selection is validated | State is Rejected with `SEL_ROOF_REFERENCE_INVALID` |
| `AT-SEL-010` | Referenced accepted partition collection is empty | Selection is validated | State is Rejected with `SEL_PARTITION_COLLECTION_EMPTY` |
| `AT-SEL-011` | Two accepted partitions have the same identifier | Selection is validated | State is Rejected with `SEL_PARTITION_ID_DUPLICATE` |
| `AT-SEL-012` | An accepted partition identifier is empty | Selection is validated | State is Rejected with `SEL_PARTITION_ID_REQUIRED` |
| `AT-SEL-013` | The candidate partition is associated with a different geometry set or roof | Selection is validated | State is Rejected with `SEL_PARTITION_MEMBERSHIP_INVALID` or the applicable reference error |
| `AT-SEL-014` | A request claims Accepted before validation, or combines a final state with contradictory data | Selection is validated | State is Rejected with `SEL_STATE_INVALID` |
| `AT-SEL-015` | A valid selection is Accepted | Source and result geometry are compared | Selected geometry is identical in meaning; source collection and vertices are unchanged |
| `AT-SEL-016` | A valid selection is Accepted | Result is inspected | No layout, Local Axis, placement, grid, rendering, module, or statistics output exists |
| `AT-SEL-017` | A prior request is Accepted and the user chooses another partition | The new choice is submitted | It uses a distinct selection request and does not mutate the prior Accepted result |
| `AT-SEL-018` | Selection request identifier is absent or empty | Selection is validated | State is Rejected with `SEL_REQUEST_ID_REQUIRED` |

Acceptance evidence for a future implementation shall identify the selection request, accepted geometry-set reference, candidate identifier, expected state, actual state, returned errors, and selected partition when Accepted.

## 11. Engineering Constraints

1. The implementation shall consume only geometry accepted under PE-GEO-001.
2. The implementation shall accept exactly one explicit partition choice per selection request.
3. The implementation shall not infer or recommend a partition.
4. Identifier-based selection shall not depend on collection order.
5. Accepted geometry and the source partition collection remain immutable.
6. Rejected selection produces no downstream-eligible partition.
7. No fallback, repair, or partial selection is permitted.
8. The implementation shall preserve deterministic results for identical input.
9. No UI, layout, Local Axis, placement, visualization, statistics, or data-format behavior is included.
10. Implementation design remains subject to a separate governed Issue; this specification does not authorize source-code work.

## 12. Engineering Notes

1. **Dependency boundary:** PE-GEO-001 owns polygon validity and roof containment. PE-GEO-002 owns selection reference, cardinality, membership, state, and result.
2. **Primary capability:** All behavior in this document maps only to `GEO-002`.
3. **Selection versus geometry:** Selection references accepted geometry; it does not copy with changed meaning or create new geometry.
4. **Selection versus layout:** An Accepted partition is eligible for later capabilities, but no layout behavior is defined here.
5. **Engineering state:** State names describe contract status and do not prescribe screens, controls, messages, or interaction flow.
6. **No algorithm prescription:** Deterministic lookup and membership are required outcomes; the means are an implementation decision.
7. **No architecture prescription:** Logical request, result, and reference fields do not mandate services, classes, endpoints, files, databases, or queues.
8. **Traceability:** The selection request identifier and geometry-set reference preserve the relationship between the user choice and the accepted geometry evidence.
9. **Phase completion:** Approval of this specification completes the Geometry Input specification phase only; it does not start Local Axis or Layout work.

This specification becomes the engineering contract for `GEO-002` only after PM approval and merge. Implementation remains subject to a separate governed Issue and the [Development Constitution](../DEVELOPMENT_CONSTITUTION.md).
