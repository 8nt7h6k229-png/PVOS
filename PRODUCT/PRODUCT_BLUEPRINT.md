# PVOS Product Blueprint

Work item: [PRODUCT-001A / PVOS Issue #15](https://github.com/8nt7h6k229-png/PVOS/issues/15)

Status: Proposed for PM approval

## 1. Purpose

This Blueprint is the master product-planning index for PVOS. It connects approved product intent to stable capability identifiers, candidate engineering work, and evidence-gated release allocation.

It defines **what product structure is governed**, not how software is designed or implemented. It does not change the Product Baseline, authorize a backlog item, promote a deferred proposal, or certify a release.

Evidence authority:

1. [PVOS Project Charter](../PROJECT_CHARTER.md)
2. [PVOS Development Constitution](../DEVELOPMENT_CONSTITUTION.md)
3. [PVOS 1.0 Product Baseline](../PM/PRODUCT_BASELINE.md), [Product Scope](../PM/PRODUCT_SCOPE.md), and [Product Capability Matrix](../PM/PRODUCT_CAPABILITY_MATRIX.md)
4. [PV Layout MVP Functional Specification](PV_LAYOUT_MVP_SPEC.md)
5. [Branch Product Knowledge Map](../PM/BRANCH_PRODUCT_KNOWLEDGE_MAP.md) and [Product Knowledge Index](../PM/PRODUCT_KNOWLEDGE_INDEX.md)

## 2. Planning principles

- **Product First:** work begins from an approved user outcome or product-governance need.
- **Evidence First:** capability status is determined by approved evidence, not aspiration.
- **Capability-driven planning:** every future engineering Issue names exactly one primary capability ID.
- **Implementation-independent:** this Blueprint defines outcomes, dependencies, and evidence gates without prescribing design.
- **Respect Product Baseline:** planning cannot silently change Included, Planned, Future, Deferred, or Not Evidenced states.
- **Respect Governance Baseline:** Issues, review, phase gates, approval, merge, and closure remain mandatory.

## 3. Status model

| Status | Meaning | Planning effect |
|---|---|---|
| **Existing** | Approved default-branch evidence establishes the capability or support asset. | May be included only within its evidenced boundary. |
| **Specified** | An approved product specification defines required behavior; delivery acceptance is still governed separately. | Eligible for engineering decomposition, not automatically complete. |
| **Planned** | An open governed Issue or PR establishes intent. | Excluded from the current baseline until separately accepted. |
| **Future / Recovery** | Branch or document evidence exists outside the approved product baseline. | May be studied; not a release commitment. |
| **Deferred Proposal** | A proposal is intentionally isolated pending evidence and baseline change. | Cannot enter a release or implementation backlog. |
| **Not Evidenced** | No affirmative evidence supports the capability claim. | Excluded; no engineering work may imply it exists. |

Release placement does not override capability status. A Planned or Future capability requires a Product Baseline Change and PM approval before becoming Included.

## 4. Product portfolio

| Product or product asset | Position | Current authority | Product claim |
|---|---|---|---|
| **PVOS Deterministic Layout Product** | Primary product | PM-003 baseline and PRODUCT-001 specification | Explicit geometry → deterministic placement → reviewable result |
| **PvLayoutPlugin AutoCAD Host** | Existing product-host asset | PvLayoutPlugin `main`, indexed by PM-001 and PM-003 | Existing host; integration with standalone PVOS is not claimed |
| **PVOS Geometry / AutoCAD Adapter** | Existing supporting asset | Merged PvLayoutPlugin evidence indexed by PM-003 | Platform-neutral geometry and supported conversion boundary; no broader data-exchange claim |
| **AI Studio / Repository Intelligence** | Internal engineering-support product | Merged evidence indexed by PM-001 and PM-003 | Knowledge and repository analysis support; not an end-user PVOS 1.0 capability |

No Cloud, Web, Steel, electrical, structural, construction, optimization, automatic roof-recognition, or collaborative product is established by the approved baseline.

## 5. Product hierarchy

```text
PVOS Portfolio
├── PVOS Deterministic Layout Product
│   ├── Geometry Input
│   ├── Partition Selection
│   ├── Local Axis
│   ├── Module Definition
│   ├── Deterministic Layout
│   ├── Boundary Containment
│   ├── Panel Placement Result
│   ├── Result Presentation
│   └── Product Quality
├── Existing Supporting Product Assets
│   ├── Standalone Core and CLI
│   ├── AutoCAD Product Host
│   └── AutoCAD Geometry Conversion Boundary
├── Internal Engineering Support
│   ├── AI Studio
│   └── Repository Intelligence
└── Governed Candidate Space
    ├── Planned Geometry Core Enhancement
    ├── Future / Recovery Knowledge
    ├── Deferred DXF Adapter Proposal
    └── Not-Evidenced Capabilities
```

The hierarchy is a product classification, not a component diagram or ownership design.

## 6. Capability domains

| Domain | Capability IDs | Product role |
|---|---|---|
| Geometry | `GEO-001`–`GEO-003` | Accept explicit 2D geometry and classify the planned Geometry Core extension |
| Local Axis | `AXS-001` | Define partition-specific panel alignment |
| Layout | `LAY-001`–`LAY-004` | Define module parameters, grid generation, containment, and ordered placement |
| Result | `RES-001`–`RES-004` | Provide geometry, count, capacity, and warnings |
| Visualization | `VIS-001` | Let the user inspect the approved layout result; no additional visualization family is implied |
| Platform | `PLT-001`–`PLT-002` | Identify existing execution and host assets without asserting integration |
| Data Exchange | `DAT-001`; proposal `DAT-X01` | Classify the existing AutoCAD conversion boundary and isolate the deferred DXF proposal |
| AI Studio | `AIS-001`–`AIS-002` | Preserve internal engineering-support capabilities |
| Quality | `QUA-001`–`QUA-003` | Preserve determinism, validation evidence, and governed acceptance |

Full definitions are authoritative in [Product Capability Tree](PRODUCT_CAPABILITY_TREE.md).

## 7. Engineering decomposition policy

The [Product Backlog](PRODUCT_BACKLOG.md) decomposes approved or evidenced capability outcomes into candidate work packages. Each work package:

- has one primary capability ID;
- states evidence, outcome, dependencies, and gate status;
- avoids implementation and architecture decisions;
- requires its own governed Issue before work begins; and
- cannot change the capability's baseline status by appearing in the backlog.

Cross-capability work is split into separate Issues. An umbrella tracking Issue may reference several capability Issues but cannot replace their one-to-one primary mapping.

## 8. Implementation sequence policy

Sequence follows product dependency, not technology preference:

1. **Geometry contract:** explicit roof and partition geometry.
2. **Placement frame:** selected partition, Local Axis, and module parameters.
3. **Deterministic placement:** grid generation and boundary containment.
4. **Result:** ordered panel geometry, count, installed capacity, and warnings.
5. **Demonstration and acceptance:** result presentation, determinism evidence, and PM acceptance.
6. **Post-baseline candidates:** only after the preceding release gate and any required Product Baseline Change.

This sequence does not start a Product Sprint and does not imply that an already-existing capability must be rebuilt.

## 9. Release policy

The [Product Release Plan](PRODUCT_RELEASE_PLAN.md) is evidence-gated:

- PVOS 1.0 contains the approved deterministic layout MVP only.
- A post-1.0 capability may enter PVOS 1.x only when the approved baseline already evidences it as Existing or Planned and a separate gate admits it.
- No additional visualization capability is approved beyond reviewing the PRODUCT-001 result.
- Deferred and Not-Evidenced capabilities remain outside PVOS 1.x.
- PVOS 2.x is a deferred horizon, not an approved release commitment.

## 10. Traceability rule

Every future Product Engineering Issue shall include:

| Required field | Rule |
|---|---|
| Primary capability | Exactly one ID from the Capability Tree |
| Product evidence | Approved document, Issue, PR, commit, or existing product asset |
| Current status | The status recorded in the Capability Tree |
| Intended outcome | Product behavior or evidence, not implementation design |
| Dependencies | Capability IDs that must be accepted first |
| Release target | Approved allocation or `Unallocated` |
| Gate | Entry and exit evidence required for PM review |

If no capability ID fits, the work stops. PM first determines whether the proposal is already evidenced, requires a Product Baseline Change, remains deferred, or is rejected.

## 11. Blueprint answers

| PM question | Authoritative answer |
|---|---|
| What products exist? | §4 Product portfolio |
| What capabilities exist? | [Product Capability Tree](PRODUCT_CAPABILITY_TREE.md) |
| What is implemented? | Capabilities marked Existing, within their evidence boundary |
| What is planned? | Capabilities marked Specified or Planned, without automatic baseline inclusion |
| What is deferred? | Future / Recovery, Deferred Proposal, and Not Evidenced entries |
| What engineering work comes next? | Gate-eligible sequence in [Product Backlog](PRODUCT_BACKLOG.md) |
| What release may contain it? | [Product Release Plan](PRODUCT_RELEASE_PLAN.md) |

---

This Blueprint becomes authoritative only after PM approval and merge. It is subordinate to the Project Charter, Development Constitution, and approved Product Baseline.
