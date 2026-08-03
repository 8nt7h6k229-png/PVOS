# PE-LAY-001 - PV Module Parameters Engineering Specification

Work item: [PE-LAY-001 / PVOS Issue #23](https://github.com/8nt7h6k229-png/PVOS/issues/23)

Primary Capability: [`LAY-001` - PV Module Parameter Definition](../PRODUCT/PRODUCT_CAPABILITY_TREE.md)

Dependencies: [PE-GEO-001](PE-GEO-001_SPEC.md), [PE-GEO-002](PE-GEO-002_SPEC.md), and [PE-AXS-001](PE-AXS-001_SPEC.md)

Status: Proposed for PM approval

## 1. Purpose

This specification defines the sole approved engineering contract for PV module parameters consumed by future deterministic Placement Engineering.

It defines module identity, physical dimensions, explicit orientation, row and column gaps, edge margin, derived installation pitches, rated power, validation, states, errors, and behavior-level acceptance tests. It does not define a grid, candidate, panel placement, boundary check, algorithm, API, software architecture, UI, storage model, framework, or programming language.

Evidence:

- [PV Layout MVP Functional Specification, sections 4.4 and 8](../PRODUCT/PV_LAYOUT_MVP_SPEC.md) defines positive dimensions, non-negative gaps and edge margin, rated power, local X/Y alignment, and pitch relationships.
- [Product Capability Tree, LAY-001](../PRODUCT/PRODUCT_CAPABILITY_TREE.md) defines the module rectangle, spacing, edge margin, and rated power used by one layout operation.
- [Product Backlog, PE-LAY-001](../PRODUCT/PRODUCT_BACKLOG.md) requires valid dimensions, gaps, margin, rated power, and invalid-input evidence after `GEO-002` and `AXS-001`.
- [PVOS 1.0 Product Baseline](../PM/PRODUCT_BASELINE.md) includes explicit module spacing parameters in the deterministic layout boundary.

## 2. Scope

### Included

- one user-supplied module-definition set;
- exactly one active module definition;
- module and parameter-request identifiers;
- physical module width and length;
- explicit module orientation relative to the Accepted Local Axis;
- effective X and Y dimensions;
- column gap, row gap, and edge margin;
- column and row installation pitches;
- rated module power in watts-peak;
- deterministic parameter validation;
- module states and stable error conditions; and
- behavior-level acceptance tests.

### Excluded

- module catalog discovery or recommendation;
- automatic orientation selection or comparison;
- Local Axis creation or modification;
- grid, row, column, or panel-candidate generation;
- panel placement;
- collision or boundary checking;
- panel count or installed-capacity statistics;
- electrical design, stringing, inverter selection, energy yield, loss, or efficiency analysis;
- rendering, visualization, or UI behavior;
- DXF or other data-format behavior;
- import or export behavior;
- optimization;
- roof detection; and
- source-code, algorithm, or architecture design.

## 3. Engineering Context

PE-LAY-001 follows Accepted geometry selection and Local Axis definition but does not consume them to place panels.

```text
User-supplied module definition set
        +
Exactly one active module identifier
        |
PE-LAY-001 validation
        |
One Accepted effective module parameter definition
```

Future Placement Engineering may consume only an `Accepted` module definition from this contract. It shall not reinterpret dimensions, gaps, orientation, margin, pitch, or rated power independently.

## 4. Input Contract

One module-parameter request contains the following logical information.

### 4.1 Request fields

| Field | Cardinality | Requirement |
|---|---:|---|
| Parameter request identifier | Exactly one | Non-empty identifier used to correlate input and result |
| Module-definition set | One collection | Contains one or more user-supplied module definitions |
| Active module identifier | Exactly one | Names one and only one definition in the supplied set |
| Linear unit | Exactly one | Millimetres for dimensions, gaps, margin, and pitches |
| Power unit | Exactly one | Watts-peak (`Wp`) |

### 4.2 Module-definition fields

Each supplied module definition contains:

| Field | Cardinality | Requirement |
|---|---:|---|
| Module identifier | Exactly one | Non-empty and unique within the request |
| Physical width | Exactly one | Finite value greater than zero, in millimetres |
| Physical length | Exactly one | Finite value greater than zero, in millimetres |
| Rated power | Exactly one | Finite value greater than zero, in Wp |
| Orientation | Exactly one | `Width Along Local X` or `Length Along Local X` |
| Column gap | Exactly one | Finite value greater than or equal to zero, in millimetres |
| Row gap | Exactly one | Finite value greater than or equal to zero, in millimetres |
| Edge margin | Exactly one | Finite value greater than or equal to zero, in millimetres |

All definitions in the supplied set shall satisfy the contract. A request containing an invalid inactive definition is Rejected; the contract does not preserve invalid definitions as an accepted catalog.

The user explicitly supplies the definitions, active identifier, and orientation. No value is inferred from geometry, naming, ordering, prior jobs, manufacturer data, or optimization.

## 5. Output Contract

One module-parameter request produces exactly one module-parameter result.

### 5.1 Common result fields

| Field | Requirement |
|---|---|
| Parameter request identifier | Equals the submitted identifier when available |
| Module state | Exactly one state defined in section 12 |
| Validation result | Ordered collection of zero or more errors defined in section 11 |

### 5.2 Accepted result

When state is `Accepted`, the result contains exactly one active module definition with:

- module identifier;
- physical width and physical length;
- effective width along local X;
- effective length along local Y;
- effective orientation;
- column gap and row gap;
- edge margin;
- column pitch and row pitch;
- rated power and Wp unit;
- millimetre unit for linear values; and
- an empty validation-error collection.

### 5.3 Rejected result

When state is `Rejected`, the result contains:

- no Accepted active module definition;
- no parameters eligible for downstream Placement Engineering; and
- one or more validation errors.

### 5.4 Prohibited outputs

The result contains no grid, row instances, column instances, panel candidate, placed panel, boundary decision, collision result, statistic, rendering, or data-format result.

## 6. Module Definition

A PV module definition is one immutable parameter record identified by a non-empty module identifier.

It describes:

- one physical rectangle through width and length;
- one explicit orientation relative to the Accepted Local Axis;
- one effective rectangular footprint in local X/Y terms;
- one column gap, row gap, and edge margin;
- one derived column pitch and row pitch; and
- one positive rated power.

The contract does not require physical length to be greater than physical width. The labels identify user-supplied manufacturer dimensions; orientation determines how those dimensions map to local X and local Y.

Exactly one definition is active per parameter request. The module-definition set may contain additional valid definitions for explicit user choice, but only the active definition is returned as the Accepted parameter source for the future Layout Job.

Accepted definitions and results are immutable. Changing any identifier, dimension, orientation, gap, margin, power, or active choice requires a new parameter request identifier.

## 7. Physical Dimensions

1. Physical width and physical length are finite numeric values.
2. Both values are strictly greater than zero.
3. Both values are expressed in millimetres.
4. Neither dimension includes a gap or edge margin.
5. Neither dimension is modified by validation.
6. Physical dimensions remain attached to the module identifier regardless of orientation.
7. Effective dimensions are derived only from physical dimensions and the explicit orientation.

### Effective dimensions

| Orientation | Effective width along local X | Effective length along local Y |
|---|---:|---:|
| `Width Along Local X` | Physical width | Physical length |
| `Length Along Local X` | Physical length | Physical width |

Effective dimensions describe the rectangular module footprint for future parameter consumption. They do not create a candidate or position.

## 8. Orientation Rules

1. Exactly one orientation value is explicitly supplied for each module definition.
2. Accepted orientation values are exactly `Width Along Local X` and `Length Along Local X`.
3. Orientation refers to the Accepted Local Axis defined by PE-AXS-001.
4. `Width Along Local X` maps physical width to local X and physical length to local Y.
5. `Length Along Local X` maps physical length to local X and physical width to local Y.
6. Orientation changes effective dimensions but does not alter physical dimensions.
7. Orientation does not rotate or mutate selected partition geometry or the Local Axis.
8. No automatic portrait/landscape comparison, fallback, recommendation, or optimization occurs.
9. Identical valid orientation inputs produce identical effective dimensions.

The terms portrait and landscape are not normative orientation values because their meaning can depend on naming conventions. The two accepted values state the required axis relationship directly.

## 9. Gap Definition

### Column gap

Column gap is the non-negative clear spacing parameter associated with the local X direction between adjacent future module columns.

### Row gap

Row gap is the non-negative clear spacing parameter associated with the local Y direction between adjacent future module rows.

### Edge margin

Edge margin is the non-negative parameter applied by the approved product contract to the future local grid envelope. It is not a geometry offset, setback rule, obstacle clearance, or boundary-validation result.

### Installation pitch

- `column pitch = effective width along local X + column gap`
- `row pitch = effective length along local Y + row gap`

Pitch values are finite, positive, and expressed in millimetres for every valid module definition.

Pitch is a parameter relationship only. This specification does not use pitch to generate a grid, row, column, candidate, or placement.

## 10. Validation Rules

Validation applies to one complete module-parameter request.

| Validation group | Accepted condition |
|---|---|
| Request | One non-empty parameter request identifier is present |
| Definition set | One or more definitions are supplied |
| Module identifiers | Every identifier is non-empty and unique within the request |
| Active definition | Exactly one active identifier names exactly one supplied definition |
| Units | Linear unit is millimetres and power unit is Wp |
| Dimensions | Every width and length is finite and greater than zero |
| Rated power | Every power value is finite and greater than zero |
| Orientation | Every value is one of the two values defined in section 8 |
| Gaps and margin | Every gap and margin is finite and non-negative |
| Effective dimensions | Match the physical dimensions and explicit orientation |
| Pitches | Match section 9 and are finite and positive |
| Module state | Input and result form a valid state under section 12 |
| Immutability | Submitted definitions are unchanged by validation |

The final state is `Accepted` only when every validation group passes. Any error produces `Rejected`; no module parameter is eligible for downstream Placement Engineering.

Validation shall report all deterministically observable errors in stable order for identical input. No warning state and no partial acceptance are defined.

## 11. Error Conditions

Each error contains a stable code, parameter request identifier when available, module identifier when available, affected field, and a human-readable explanation consistent with the code.

| Error code | Condition |
|---|---|
| `MOD_REQUEST_ID_REQUIRED` | Parameter request identifier is absent or empty |
| `MOD_DEFINITION_SET_EMPTY` | No module definition is supplied |
| `MOD_ID_REQUIRED` | A module identifier is absent or empty |
| `MOD_ID_DUPLICATE` | More than one supplied definition uses the same module identifier |
| `MOD_ACTIVE_REQUIRED` | No active module identifier is supplied |
| `MOD_MULTIPLE_ACTIVE` | More than one active module identifier is supplied |
| `MOD_ACTIVE_UNKNOWN` | Active identifier does not name exactly one supplied definition |
| `MOD_LINEAR_UNIT_INVALID` | Linear unit is absent or is not millimetres |
| `MOD_POWER_UNIT_INVALID` | Power unit is absent or is not Wp |
| `MOD_WIDTH_INVALID` | Physical width is missing, non-numeric, non-finite, or not greater than zero |
| `MOD_LENGTH_INVALID` | Physical length is missing, non-numeric, non-finite, or not greater than zero |
| `MOD_RATED_POWER_INVALID` | Rated power is missing, non-numeric, non-finite, or not greater than zero |
| `MOD_ORIENTATION_INVALID` | Orientation is missing, multiple, or not one of the two accepted values |
| `MOD_COLUMN_GAP_INVALID` | Column gap is missing, non-numeric, non-finite, or negative |
| `MOD_ROW_GAP_INVALID` | Row gap is missing, non-numeric, non-finite, or negative |
| `MOD_EDGE_MARGIN_INVALID` | Edge margin is missing, non-numeric, non-finite, or negative |
| `MOD_EFFECTIVE_DIMENSION_INVALID` | Effective dimensions do not match physical dimensions and orientation |
| `MOD_PITCH_INVALID` | A pitch does not match section 9 or is non-finite/non-positive |
| `MOD_STATE_INVALID` | Supplied data and claimed or prior Module state contradict section 12 |
| `MOD_SOURCE_MUTATED` | A supplied module definition changes during validation or result production |
| `MOD_RESULT_NONDETERMINISTIC` | Identical valid requests do not reproduce the same Accepted parameters and state |

Error presence always corresponds to `Rejected`; an `Accepted` result contains no errors.

## 12. Module States

Module state describes engineering status, not UI behavior.

| State | Meaning | Definition eligible downstream? | Validation errors |
|---|---|---:|---:|
| `Undefined` | A parameter request exists but the active module definition is incomplete or absent. | No | None before validation; required-field errors if validation is requested |
| `Defined` | The definition set and exactly one active choice are supplied and await validation. | No | None before validation |
| `Accepted` | All request, identity, parameter, derived-value, state, and immutability rules pass. | Yes | Empty |
| `Rejected` | One or more rules fail. | No | One or more |

### Valid progression

- `Undefined` may become `Defined` when the required definition set and active choice are supplied.
- `Undefined` becomes `Rejected` if validation is requested while required data is missing.
- `Defined` becomes `Accepted` when validation succeeds.
- `Defined` becomes `Rejected` when validation fails.
- `Accepted` and `Rejected` are terminal for that parameter request identifier.

Any changed definition, parameter, unit, orientation, or active choice requires a new parameter request identifier. A final result shall not be silently rewritten.

The contract does not require intermediate-state persistence. If states are exposed or recorded, their observable meaning shall conform to this section.

## 13. Acceptance Tests

The following behavior-level tests define observable results without prescribing a test framework or implementation technique.

| ID | Given | When | Then |
|---|---|---|---|
| `AT-MOD-001` | One valid definition with positive dimensions/power, allowed orientation, non-negative gaps/margin, and matching active ID | Request is validated | State is Accepted; effective values, pitches, power, and ID are returned; errors are empty |
| `AT-MOD-002` | Orientation `Width Along Local X` | Request is validated | Effective X width equals physical width; effective Y length equals physical length |
| `AT-MOD-003` | Orientation `Length Along Local X` | Request is validated | Effective X width equals physical length; effective Y length equals physical width |
| `AT-MOD-004` | Equivalent valid request is repeated | Results are compared | State and every Accepted parameter are identical |
| `AT-MOD-005` | Physical width is zero, negative, non-finite, or absent | Request is validated | State is Rejected with `MOD_WIDTH_INVALID` |
| `AT-MOD-006` | Physical length is zero, negative, non-finite, or absent | Request is validated | State is Rejected with `MOD_LENGTH_INVALID` |
| `AT-MOD-007` | Rated power is positive and finite | Request is validated | Power validation passes and value is retained in Wp |
| `AT-MOD-008` | Rated power is zero, negative, non-finite, or absent | Request is validated | State is Rejected with `MOD_RATED_POWER_INVALID` |
| `AT-MOD-009` | Orientation is absent, multiple, or unsupported | Request is validated | State is Rejected with `MOD_ORIENTATION_INVALID` |
| `AT-MOD-010` | Two definitions share an identifier | Request is validated | State is Rejected with `MOD_ID_DUPLICATE` |
| `AT-MOD-011` | Column gap is zero or positive and finite | Request is validated | Column-gap validation passes; column pitch follows section 9 |
| `AT-MOD-012` | Row gap is zero or positive and finite | Request is validated | Row-gap validation passes; row pitch follows section 9 |
| `AT-MOD-013` | A gap is negative, non-finite, or absent | Request is validated | State is Rejected with the applicable gap error |
| `AT-MOD-014` | Edge margin is zero or positive and finite | Request is validated | Edge-margin validation passes and value is retained |
| `AT-MOD-015` | Edge margin is negative, non-finite, or absent | Request is validated | State is Rejected with `MOD_EDGE_MARGIN_INVALID` |
| `AT-MOD-016` | No active identifier is supplied | Request is validated | State is Rejected with `MOD_ACTIVE_REQUIRED` |
| `AT-MOD-017` | Multiple active identifiers are supplied | Request is validated | State is Rejected with `MOD_MULTIPLE_ACTIVE` |
| `AT-MOD-018` | Active identifier names no supplied definition | Request is validated | State is Rejected with `MOD_ACTIVE_UNKNOWN` |
| `AT-MOD-019` | More than one valid definition is supplied and exactly one is active | Request is validated | Only the explicitly active definition is returned as Accepted |
| `AT-MOD-020` | An inactive definition is invalid | Request is validated | Complete request is Rejected with the applicable module error |
| `AT-MOD-021` | Linear unit is not millimetres or power unit is not Wp | Request is validated | State is Rejected with the applicable unit error |
| `AT-MOD-022` | Request claims Accepted before validation or combines a final state with contradictory data | Request is validated | State is Rejected with `MOD_STATE_INVALID` |
| `AT-MOD-023` | A valid definition is Accepted | Source and result are compared | Source fields are unchanged; physical values remain distinct from effective values |
| `AT-MOD-024` | A final request changes any parameter or active choice | Changed data is submitted | A new parameter request identifier is required; prior final result remains unchanged |
| `AT-MOD-025` | A valid definition is Accepted | Result is inspected | No grid, candidate, placement, boundary, statistic, rendering, or data-format output exists |

Acceptance evidence for a future implementation shall identify the parameter request, definition set, active ID, input values, expected state, actual state, error codes, effective dimensions, pitches, rated power, and immutability result.

## 14. Engineering Constraints

1. Module definitions, active choice, and orientation are user supplied.
2. Exactly one active definition is accepted per parameter request.
3. All identifiers are non-empty and unique within the request.
4. Dimensions and rated power are finite and positive.
5. Gaps and edge margin are finite and non-negative.
6. Linear values use millimetres; rated power uses Wp.
7. Effective dimensions follow only the explicit orientation mapping.
8. Pitches follow only the relationships in section 9.
9. No automatic orientation selection, recommendation, fallback, or optimization occurs.
10. Accepted parameters and source definitions are immutable.
11. A Rejected definition is ineligible for downstream Placement Engineering.
12. No grid, candidate, placement, collision, boundary, statistic, UI, data-format, electrical, or Product Sprint work is authorized here.

## 15. Engineering Notes

1. **Sole parameter authority:** Future Placement Engineering shall reference this specification rather than redefining module parameters.
2. **Primary capability:** Every requirement in this document maps only to `LAY-001`.
3. **Dependency boundary:** PE-GEO-001 and PE-GEO-002 own accepted geometry and selection; PE-AXS-001 owns the Local Axis; PE-LAY-001 owns module parameters only.
4. **Edge-margin evidence:** Edge margin is required because PRODUCT-001 and the Capability Tree include it in the approved deterministic MVP parameter boundary.
5. **Orientation evidence:** Orientation is explicit and user controlled. The two normative values avoid inferred portrait/landscape semantics.
6. **Pitch versus grid:** Pitch is an accepted parameter relationship. Using it to enumerate positions belongs to later capability `LAY-002`.
7. **Rated power boundary:** Rated power is retained for later approved capacity calculation; no electrical behavior is defined here.
8. **No algorithm prescription:** Validation and derived parameter outcomes are required; the means remain an implementation decision.
9. **No architecture prescription:** Logical sets, identifiers, states, fields, and results do not mandate services, endpoints, classes, files, databases, or UI controls.
10. **Phase boundary:** Approval completes the Module Parameters Engineering Specification only. Grid and Placement work remain separate governed Issues.

This specification becomes the engineering contract for `LAY-001` only after PM approval and merge. Implementation remains subject to a separate governed Issue and the [Development Constitution](../DEVELOPMENT_CONSTITUTION.md).
