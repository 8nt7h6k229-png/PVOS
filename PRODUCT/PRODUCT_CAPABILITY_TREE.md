# PVOS Product Capability Tree

Status: Proposed for PM approval under [PRODUCT-001A](https://github.com/8nt7h6k229-png/PVOS/issues/15)

## 1. Reading the tree

This tree assigns a stable ID to each evidenced, specified, planned, or explicitly deferred capability relevant to PVOS planning. Status meanings follow the [Product Blueprint](PRODUCT_BLUEPRINT.md). A row is classification evidence, not implementation authorization.

## 2. Capability summary

| ID | Capability | Domain | Current status | PVOS 1.x position |
|---|---|---|---|---|
| `GEO-001` | Explicit Polygon Geometry Input | Geometry | Existing / Specified | PVOS 1.0 |
| `GEO-002` | User-supplied Partition Selection | Geometry | Specified | PVOS 1.0 |
| `GEO-003` | Geometry Core Enhancement | Geometry | Planned | Gate-blocked 1.x candidate |
| `AXS-001` | Partition-specific Local Axis | Local Axis | Existing / Specified | PVOS 1.0 |
| `LAY-001` | PV Module Parameter Definition | Layout | Existing / Specified | PVOS 1.0 |
| `LAY-002` | Deterministic Layout Grid | Layout | Existing / Specified | PVOS 1.0 |
| `LAY-003` | Partition Boundary Containment | Layout | Existing / Specified | PVOS 1.0 |
| `LAY-004` | Ordered Panel Placement | Layout | Existing / Specified | PVOS 1.0 |
| `RES-001` | Panel Geometry Result | Result | Existing / Specified | PVOS 1.0 |
| `RES-002` | Panel Count | Result | Existing / Specified | PVOS 1.0 |
| `RES-003` | Installed Capacity | Result | Existing / Specified | PVOS 1.0 |
| `RES-004` | Placement Warning | Result | Existing / Specified | PVOS 1.0 |
| `VIS-001` | Layout Result Presentation | Visualization | Specified | PVOS 1.0 demonstration boundary |
| `PLT-001` | Standalone Core and CLI | Platform | Existing | PVOS 1.0 supporting execution asset |
| `PLT-002` | AutoCAD Product Host | Platform | Existing asset; integration unverified | Recognized, not a PVOS 1.0 integration claim |
| `DAT-001` | AutoCAD Geometry Conversion Boundary | Data Exchange | Existing asset | Recognized supporting boundary |
| `AIS-001` | AI Studio Project Knowledge Support | AI Studio | Existing internal support | Not an end-user release capability |
| `AIS-002` | Repository Intelligence | AI Studio | Existing internal support | Not an end-user release capability |
| `QUA-001` | Deterministic Result Reproduction | Quality | Existing / Specified | PVOS 1.0 |
| `QUA-002` | Geometry and Layout Validation Evidence | Quality | Existing | PVOS 1.0 supporting evidence |
| `QUA-003` | Governed Product Acceptance | Quality | Existing governance / Specified acceptance | PVOS 1.0 gate |
| `DAT-X01` | DXF Adapter Capability Proposal | Data Exchange | Deferred Proposal | Excluded from PVOS 1.x |

## 3. Geometry

### GEO-001 — Explicit Polygon Geometry Input

| Field | Definition |
|---|---|
| Purpose | Accept user-supplied 2D roof and partition polygon geometry as the planning context and placement boundary. |
| Dependencies | None. |
| Inputs | Polygon vertices in one global coordinate system and millimetre unit. |
| Outputs | Valid roof geometry context and selected partition boundary for downstream placement. |
| Related product | PVOS Deterministic Layout Product. |
| Current status | Existing polygon/partition domain evidence; behavior specified by PRODUCT-001. |
| Future status | Remains bounded to explicit straight-edged 2D polygons unless a baseline change is approved. |
| Evidence | [Product Baseline](../PM/PRODUCT_BASELINE.md), [MVP Specification §§4 and 6](PV_LAYOUT_MVP_SPEC.md). |

### GEO-002 — User-supplied Partition Selection

| Field | Definition |
|---|---|
| Purpose | Let the user choose exactly one supplied partition as the boundary for one layout operation. |
| Dependencies | `GEO-001`. |
| Inputs | User-supplied partition set and one selection. |
| Outputs | Selected partition identifier and boundary. |
| Related product | PVOS Deterministic Layout Product. |
| Current status | Specified by PRODUCT-001; no automatic partition generation claim. |
| Future status | Automatic recognition or generation remains Not Evidenced and excluded. |
| Evidence | [MVP Specification §§3–4](PV_LAYOUT_MVP_SPEC.md), [Product Scope](../PM/PRODUCT_SCOPE.md). |

### GEO-003 — Geometry Core Enhancement

| Field | Definition |
|---|---|
| Purpose | Classify the additional standalone geometry work already represented by PVOS Issue #1 and its branch. |
| Dependencies | `GEO-001`; separate Product Baseline Change before inclusion. |
| Inputs | Acceptance scope from a future governed disposition of Issue #1. |
| Outputs | Not defined as an included product outcome. |
| Related product | PVOS Deterministic Layout Product. |
| Current status | Planned / unmerged. |
| Future status | Candidate only; may be accepted, narrowed, deferred, or rejected by PM. |
| Evidence | [PVOS Issue #1](https://github.com/8nt7h6k229-png/PVOS/issues/1), [Product Baseline — Planned capability](../PM/PRODUCT_BASELINE.md). |

## 4. Local Axis

### AXS-001 — Partition-specific Local Axis

| Field | Definition |
|---|---|
| Purpose | Establish the origin and rotation that control panel alignment for the selected partition. |
| Dependencies | `GEO-002`. |
| Inputs | Global origin point and rotation angle in degrees. |
| Outputs | Local placement frame and reversible local/global interpretation. |
| Related product | PVOS Deterministic Layout Product. |
| Current status | Existing / Specified. |
| Future status | Alternative automatic orientation selection is excluded. |
| Evidence | [Product Baseline](../PM/PRODUCT_BASELINE.md), [MVP Specification §7](PV_LAYOUT_MVP_SPEC.md). |

## 5. Layout

### LAY-001 — PV Module Parameter Definition

| Field | Definition |
|---|---|
| Purpose | Define the module rectangle, spacing, edge margin, and rated power used by one layout operation. |
| Dependencies | `GEO-002`, `AXS-001`. |
| Inputs | Width, height, horizontal gap, vertical gap, edge margin, and module power. |
| Outputs | Valid module parameter set. |
| Related product | PVOS Deterministic Layout Product. |
| Current status | Existing / Specified. |
| Future status | Automatic orientation comparison remains excluded. |
| Evidence | [MVP Definition](../PM/MVP_DEFINITION.md), [MVP Specification §4.4](PV_LAYOUT_MVP_SPEC.md). |

### LAY-002 — Deterministic Layout Grid

| Field | Definition |
|---|---|
| Purpose | Generate repeatable rectangular panel candidates aligned to the Local Axis. |
| Dependencies | `GEO-002`, `AXS-001`, `LAY-001`. |
| Inputs | Selected partition in local coordinates and module parameters. |
| Outputs | Ordered panel candidates. |
| Related product | PVOS Deterministic Layout Product. |
| Current status | Existing / Specified. |
| Future status | Search, scoring, and optimization remain excluded. |
| Evidence | [Product Baseline](../PM/PRODUCT_BASELINE.md), [MVP Specification §8](PV_LAYOUT_MVP_SPEC.md). |

### LAY-003 — Partition Boundary Containment

| Field | Definition |
|---|---|
| Purpose | Accept only complete panel rectangles contained by the selected partition. |
| Dependencies | `LAY-002`. |
| Inputs | Ordered candidates and selected partition boundary. |
| Outputs | Accepted and rejected candidate decisions. |
| Related product | PVOS Deterministic Layout Product. |
| Current status | Existing / Specified. |
| Future status | Obstacle, shading, walkway, and rule-derived setback evaluation remain excluded. |
| Evidence | [Product Baseline](../PM/PRODUCT_BASELINE.md), [MVP Specification §9](PV_LAYOUT_MVP_SPEC.md). |

### LAY-004 — Ordered Panel Placement

| Field | Definition |
|---|---|
| Purpose | Return accepted panels in deterministic row-and-column order with stable identifiers. |
| Dependencies | `LAY-003`. |
| Inputs | Accepted panel candidates. |
| Outputs | Ordered placed-panel collection. |
| Related product | PVOS Deterministic Layout Product. |
| Current status | Existing / Specified. |
| Future status | Placement V2 and optimization remain Future / Recovery and excluded. |
| Evidence | [MVP Definition](../PM/MVP_DEFINITION.md), [MVP Specification §8](PV_LAYOUT_MVP_SPEC.md). |

## 6. Result and visualization

| ID | Capability | Purpose | Dependencies | Inputs | Outputs | Related product | Current status | Future status / evidence |
|---|---|---|---|---|---|---|---|---|
| `RES-001` | Panel Geometry Result | Provide four-corner panel geometry in global coordinates. | `LAY-004` | Ordered panels | Panel IDs and corner points | PVOS Layout | Existing / Specified | Remains 2D rectangular; [MVP Spec §5.1](PV_LAYOUT_MVP_SPEC.md) |
| `RES-002` | Panel Count | Report accepted panel quantity. | `LAY-004` | Ordered panels | Integer count | PVOS Layout | Existing / Specified | No change planned; [MVP Spec §5.2](PV_LAYOUT_MVP_SPEC.md) |
| `RES-003` | Installed Capacity | Calculate count × rated module power ÷ 1000. | `RES-002`, `LAY-001` | Count and power | kWp | PVOS Layout | Existing / Specified | Electrical analysis excluded; [MVP Spec §5.3](PV_LAYOUT_MVP_SPEC.md) |
| `RES-004` | Placement Warning | Identify the valid no-fit result. | `LAY-003` | Accepted-panel count | No-fit warning when count is zero | PVOS Layout | Existing / Specified | No broader diagnostic system implied; [MVP Spec §5.4](PV_LAYOUT_MVP_SPEC.md) |
| `VIS-001` | Layout Result Presentation | Let the user inspect geometry, count, capacity, and warnings. | `RES-001`–`RES-004` | Layout result | Reviewable user-visible result | PVOS Layout | Specified | No additional visualization family approved; [MVP Spec §§2 and 11](PV_LAYOUT_MVP_SPEC.md) |

## 7. Platform and data boundary

| ID | Capability | Purpose | Dependencies | Inputs | Outputs | Related product | Current status | Future status / evidence |
|---|---|---|---|---|---|---|---|---|
| `PLT-001` | Standalone Core and CLI | Provide existing runnable/testable execution assets for the bounded layout core. | Core layout capabilities | Layout request | Layout result | PVOS Layout | Existing | Product delivery acceptance remains governed; [Product Baseline](../PM/PRODUCT_BASELINE.md) |
| `PLT-002` | AutoCAD Product Host | Preserve the existing AutoCAD host as a portfolio asset. | None asserted for standalone PVOS | Host-specific user context | Existing host behavior | PvLayoutPlugin | Existing asset; integration unverified | Integration requires separate evidence; [Product Scope](../PM/PRODUCT_SCOPE.md) |
| `DAT-001` | AutoCAD Geometry Conversion Boundary | Convert supported detached AutoCAD geometry at the existing documented boundary. | Existing geometry asset | Supported detached geometry | Platform-neutral geometry | PvLayoutPlugin / PVOS support | Existing asset | No broader format claim; [Product Baseline](../PM/PRODUCT_BASELINE.md) |
| `DAT-X01` | DXF Adapter Capability Proposal | Preserve Issue #13 as a deferred proposal without defining product behavior. | GitHub evidence, Product Baseline Change, PM approval | Not approved | Not approved | None approved | Deferred Proposal | Excluded from PVOS 1.x; [Issue #13](https://github.com/8nt7h6k229-png/PVOS/issues/13), [Capability Matrix](../PM/PRODUCT_CAPABILITY_MATRIX.md) |

## 8. AI Studio and quality

| ID | Capability | Purpose | Dependencies | Inputs | Outputs | Related product | Current status | Future status / evidence |
|---|---|---|---|---|---|---|---|---|
| `AIS-001` | AI Studio Project Knowledge Support | Support evidence recovery and reviewable engineering preparation. | Approved repositories | Repository knowledge | Reviewable engineering support | AI Studio | Existing internal support | Not an end-user PVOS 1.0 capability; [Product Knowledge Index](../PM/PRODUCT_KNOWLEDGE_INDEX.md) |
| `AIS-002` | Repository Intelligence | Support symbol, reference, call-graph, and impact knowledge. | Repository sources | Repository evidence | Indexed knowledge | AI Studio | Existing internal support | Remains governed support; [Product Knowledge Index](../PM/PRODUCT_KNOWLEDGE_INDEX.md) |
| `QUA-001` | Deterministic Result Reproduction | Require identical valid inputs to produce identical ordered results. | `LAY-004`, `RES-001`–`RES-004` | Repeated identical requests | Comparable identical results | PVOS Layout | Existing / Specified | PVOS 1.0 acceptance; [MVP Spec §11.2](PV_LAYOUT_MVP_SPEC.md) |
| `QUA-002` | Geometry and Layout Validation Evidence | Preserve existing geometry/layout test evidence. | Existing baseline | Test cases and baseline | Review evidence | PVOS Layout | Existing | Additional platforms are not included; [Product Baseline](../PM/PRODUCT_BASELINE.md) |
| `QUA-003` | Governed Product Acceptance | Require evidence, PM review, merge, and closure for product state. | All release capabilities | Acceptance package | Approved or rejected product state | PVOS Portfolio | Existing governance / Specified | Remains implementation-independent; [Development Constitution](../DEVELOPMENT_CONSTITUTION.md) |

## 9. Deferred knowledge families

The approved evidence also indexes Roof Region history, Rule Engine, optimization, electrical, construction, runtime dashboard, Placement V2, platform validation, Cloud, Web, and Steel families. They remain Future / Recovery, Planned support, or Not Evidenced exactly as classified in the [Product Capability Matrix](../PM/PRODUCT_CAPABILITY_MATRIX.md) and [Branch Product Knowledge Map](../PM/BRANCH_PRODUCT_KNOWLEDGE_MAP.md).

They are not assigned capability IDs for executable PVOS work because no approved Product Baseline Change admits them. A future proposal must first pass evidence and baseline governance; this tree is not permission to implement them.
