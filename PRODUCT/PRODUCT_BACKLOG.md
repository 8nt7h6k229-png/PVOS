# PVOS Product Backlog

Status: Proposed planning decomposition under [PRODUCT-001A](https://github.com/8nt7h6k229-png/PVOS/issues/15)

## 1. Backlog policy

This backlog identifies candidate Product Engineering work needed to demonstrate and accept already-approved PVOS outcomes. It does not start a Product Sprint, authorize implementation, or change a capability's status.

Every executable work item shall be created as a separate governed Issue and shall map to exactly one primary capability ID from the [Product Capability Tree](PRODUCT_CAPABILITY_TREE.md). Dependencies may reference other capabilities, but scope belongs to the primary capability only.

Backlog states:

- **Gate-ready:** approved product behavior exists and the item may be proposed as an Issue after PM authorizes the Product Engineering phase.
- **Blocked:** a named evidence or baseline gate is unmet.
- **Deferred:** no implementation Issue may be opened under the current baseline.
- **Complete evidence:** the relevant existing asset is indexed; no rebuild is implied.

## 2. MVP engineering sequence

| Sequence | Backlog ID | Primary capability | Product outcome | Dependencies | State | Required completion evidence |
|---:|---|---|---|---|---|---|
| 1 | `PE-GEO-001` | `GEO-001` | Demonstrate valid explicit roof and partition polygon input at the PRODUCT-001 boundary. | None | Gate-ready | Issue acceptance, repeatable input examples, review record |
| 2 | `PE-GEO-002` | `GEO-002` | Demonstrate user selection of exactly one supplied partition without automatic generation. | `GEO-001` | Gate-ready | Selected-partition result and exclusion evidence |
| 3 | `PE-AXS-001` | `AXS-001` | Demonstrate user-assigned origin and rotation controlling partition placement alignment. | `GEO-002` | Gate-ready | Repeatable Local Axis acceptance examples |
| 4 | `PE-LAY-001` | `LAY-001` | Demonstrate valid module dimensions, gaps, margin, and rated power as layout inputs. | `GEO-002`, `AXS-001` | Gate-ready | Input acceptance evidence and invalid-input findings |
| 5 | `PE-LAY-002` | `LAY-002` | Demonstrate deterministic local-axis-aligned candidate generation and ordering. | `LAY-001` | Gate-ready | Repeatability evidence for identical inputs |
| 6 | `PE-LAY-003` | `LAY-003` | Demonstrate that only complete panel rectangles contained by the selected partition are accepted. | `LAY-002` | Gate-ready | Boundary acceptance examples, including rejected candidates |
| 7 | `PE-LAY-004` | `LAY-004` | Demonstrate ordered placed panels with stable identifiers. | `LAY-003` | Gate-ready | Ordered placement result evidence |
| 8 | `PE-RES-001` | `RES-001` | Demonstrate four-corner panel geometry returned in global coordinates. | `LAY-004` | Gate-ready | Geometry result acceptance evidence |
| 9 | `PE-RES-002` | `RES-002` | Demonstrate panel count equals returned panel geometry count. | `RES-001` | Gate-ready | Count reconciliation evidence |
| 10 | `PE-RES-003` | `RES-003` | Demonstrate installed-capacity calculation at the approved formula boundary. | `RES-002`, `LAY-001` | Gate-ready | Formula examples and review evidence |
| 11 | `PE-RES-004` | `RES-004` | Demonstrate zero-panel no-fit warning behavior. | `LAY-003` | Gate-ready | No-fit and fit-case warning evidence |
| 12 | `PE-VIS-001` | `VIS-001` | Present panel geometry, count, capacity, and warnings as one reviewable layout result. | `RES-001`–`RES-004` | Gate-ready | Demonstrable user workflow reviewed against PRODUCT-001 |
| 13 | `PE-QUA-001` | `QUA-001` | Prove identical valid inputs reproduce identical ordered results. | `VIS-001` | Gate-ready | Recorded deterministic comparison |
| 14 | `PE-QUA-003` | `QUA-003` | Assemble the PVOS 1.0 product acceptance package and obtain PM disposition. | All PVOS 1.0 backlog items | Blocked until preceding acceptance evidence | Reviewed Head, validation, merge, Issue closure, baseline state |

Sequence expresses product dependency. It does not prescribe whether an engineer reuses existing assets, fills an evidence gap, or performs an authorized change; the future Issue determines that bounded scope after inventory.

## 3. Existing supporting-asset disposition

| Backlog ID | Primary capability | Product outcome | State | Gate |
|---|---|---|---|---|
| `PE-PLT-001` | `PLT-001` | Confirm the existing standalone core and CLI evidence used by the PVOS 1.0 demonstration. | Complete evidence; acceptance linkage pending | Must not become a rebuild assumption |
| `PE-PLT-002` | `PLT-002` | Obtain PM disposition on whether the AutoCAD host remains a separate recognized lane or enters a future integration proposal. | Blocked | Cross-repository ownership/integration decision |
| `PE-DAT-001` | `DAT-001` | Preserve and review the existing AutoCAD geometry-conversion boundary as a supporting asset. | Complete evidence | No expanded data-exchange claim |
| `PE-AIS-001` | `AIS-001` | Preserve AI Studio as governed internal engineering support. | Complete evidence | Not mapped to an end-user release |
| `PE-AIS-002` | `AIS-002` | Preserve Repository Intelligence as governed internal engineering support. | Complete evidence | Not mapped to an end-user release |
| `PE-QUA-002` | `QUA-002` | Link existing geometry and layout validation evidence to the product acceptance package. | Gate-ready | Evidence review only unless a separate Issue authorizes change |

## 4. Post-1.0 candidate

| Backlog ID | Primary capability | Product outcome | State | Required gate |
|---|---|---|---|---|
| `PE-GEO-003` | `GEO-003` | Review and disposition the already-planned Geometry Core enhancement represented by Issue #1. | Blocked | Inventory branch evidence; define accepted product boundary; Product Baseline Change; PM approval |

This candidate is not admitted to PVOS 1.1 merely by appearing here.

## 5. Deferred register

| Reference | Classification | Backlog rule |
|---|---|---|
| `DAT-X01` / [PRODUCT-00X Issue #13](https://github.com/8nt7h6k229-png/PVOS/issues/13) | Deferred Proposal | No implementation backlog item until affirmative GitHub evidence, Product Baseline Change, and PM approval |
| Roof Detection and automatic region recognition | Not Evidenced | No implementation backlog item |
| Rule Engine, optimization, electrical, structural, construction, runtime dashboard, Cloud, Web, and collaborative products | Future / Recovery or Not Evidenced | No implementation backlog item without separate evidence and baseline governance |

## 6. Issue mapping rule

Each future Issue title or body shall contain `Primary Capability: <ID>`. One Issue may have only one primary capability. If a proposed outcome spans two primary capabilities, PM splits it before engineering begins.

An Issue may not use `DAT-X01` or any deferred knowledge family as an implementation mapping until its required baseline gate is closed.

Evidence: [Development Constitution §§4–7 and 10–11](../DEVELOPMENT_CONSTITUTION.md), [Product Blueprint](PRODUCT_BLUEPRINT.md), and [MVP Specification](PV_LAYOUT_MVP_SPEC.md).
