# PVOS Product Release Plan

Status: Proposed evidence-gated plan under [PRODUCT-001A](https://github.com/8nt7h6k229-png/PVOS/issues/15)

## 1. Release planning rule

This plan allocates approved capabilities to product gates. It is not a date roadmap, sprint plan, implementation authorization, or Product Baseline Change.

A release label does not promote capability status. Only reviewed evidence, an approved baseline decision where required, merge, and closure can admit a capability.

## 2. PVOS 1.0 — Deterministic Layout MVP

### Product outcome

A user supplies roof geometry and partitions, selects one partition, assigns its Local Axis, supplies PV module parameters, generates a deterministic contained layout, and reviews panel geometry, panel count, installed capacity, and placement warnings.

### Included capability allocation

| Domain | Capability IDs | Release boundary |
|---|---|---|
| Geometry | `GEO-001`, `GEO-002` | Explicit user-supplied 2D polygons and one selected partition |
| Local Axis | `AXS-001` | Explicit origin and rotation |
| Layout | `LAY-001`–`LAY-004` | Fixed module parameters, deterministic grid, containment, ordered placement |
| Result | `RES-001`–`RES-004` | Global panel geometry, count, kWp, and no-fit warning |
| Visualization | `VIS-001` | Review of the approved layout result only |
| Platform | `PLT-001` | Existing standalone execution asset supporting demonstration |
| Quality | `QUA-001`–`QUA-003` | Determinism, evidence, and governed acceptance |

### Recognized but not integrated release claims

- `PLT-002` AutoCAD Product Host remains an existing separate asset.
- `DAT-001` AutoCAD Geometry Conversion Boundary remains an existing supporting asset.
- AI Studio capabilities `AIS-001` and `AIS-002` remain internal engineering support.

### Exit gate

PVOS 1.0 is accepted only when:

1. every included capability has an approved Issue-to-evidence mapping;
2. the PRODUCT-001 user workflow is demonstrable;
3. deterministic, geometry, boundary, result, and warning acceptance evidence is recorded;
4. the supporting-lane ownership/integration disposition required by PM-003 is resolved or formally accepted as separate;
5. no Planned, Future, Deferred, or Not-Evidenced capability is represented as included; and
6. PM approves and closes the governed release package.

Current state: product specification approved; underlying baseline assets exist; product-complete release acceptance is not yet recorded.

## 3. PVOS 1.1 — Geometry candidate gate

PVOS 1.1 has no approved included scope.

`GEO-003` Geometry Core Enhancement is the only named post-1.0 candidate supported as **Planned** by the approved PM-003 baseline. It is represented by open [PVOS Issue #1](https://github.com/8nt7h6k229-png/PVOS/issues/1) and an unmerged branch.

It may be allocated to PVOS 1.1 only after:

1. branch and Issue evidence are inventoried against current `main`;
2. PM defines the bounded product outcome and exclusions;
3. acceptance evidence is defined without architecture prescription;
4. a Product Baseline Change is approved; and
5. the governed release allocation is updated.

Until then, PVOS 1.1 is **Reserved / Gate-blocked**, not committed.

## 4. PVOS 1.2 — Unallocated

PVOS 1.2 has no approved capability allocation.

PRODUCT-001 already includes review of panel geometry, panel count, installed capacity, and warnings through `VIS-001`. The approved baseline does not support a separate visualization enhancement capability. No such capability is created by this plan.

PVOS 1.2 remains **Unallocated** until approved evidence and a Product Baseline Change establish a bounded capability.

## 5. PVOS 2.x — Deferred horizon

PVOS 2.x is a classification horizon, not an approved release or commitment.

The following evidence families remain deferred under their current PM-002/PM-003 classifications:

- advanced Roof Region relationships;
- Rule Engine and constraint optimization;
- electrical and string design;
- structural and construction planning;
- runtime dashboard and Placement V2;
- broader validation/platform proposals;
- Cloud, Web, Steel, and collaborative product families; and
- `DAT-X01` DXF Adapter Capability Proposal.

No item above has PVOS 2.x scope, sequence, or acceptance approval. Each requires affirmative evidence, bounded product definition, Product Baseline Change, and PM approval before release allocation.

Roof Detection and automatic region recognition remain Not Evidenced, not deferred release promises.

## 6. Release exclusion matrix

| Capability class | PVOS 1.0 | PVOS 1.1 | PVOS 1.2 | PVOS 2.x horizon |
|---|---|---|---|---|
| Approved deterministic MVP | Included at approved boundary | Preserved | Preserved | Preserved unless later governed change |
| `GEO-003` Planned Geometry Core | Excluded | Gate-blocked candidate | Unallocated | Unallocated |
| Additional visualization | Not defined beyond `VIS-001` | Excluded | Unallocated | Unallocated |
| DXF import or DXF export | Excluded | Excluded | Excluded | Deferred proposal only; no release allocation |
| AI product decisions | Excluded | Excluded | Excluded | Future proposal only |
| Optimization, electrical, structural, construction | Excluded | Excluded | Excluded | Deferred evidence families only |
| Cloud and multi-user products | Excluded | Excluded | Excluded | Future proposal only |

## 7. Change control

Changing a release allocation requires:

1. one primary capability ID;
2. approved GitHub evidence;
3. a governed Issue with product outcome and exclusions;
4. Product Baseline Change approval when status or scope changes;
5. an updated Capability Tree and Backlog mapping; and
6. PM review, merge, and closure.

Evidence: [Product Baseline](../PM/PRODUCT_BASELINE.md), [Product Capability Matrix](../PM/PRODUCT_CAPABILITY_MATRIX.md), [Project Charter](../PROJECT_CHARTER.md), [Development Constitution](../DEVELOPMENT_CONSTITUTION.md), and [PRODUCT-001 Specification](PV_LAYOUT_MVP_SPEC.md).
