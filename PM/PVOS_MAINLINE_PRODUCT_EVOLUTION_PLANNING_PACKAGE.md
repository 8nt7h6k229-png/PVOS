# PVOS Mainline Product Evolution Planning Package

## Package Identity

| Field | Value |
|---|---|
| Package | `PVOS_MAINLINE_PRODUCT_EVOLUTION_PLANNING_PACKAGE` |
| Product | PVOS |
| Workflow | Workflow A — Product Mainline |
| Purpose | 規劃 C#／.NET Mainline、Core、Validation／Evidence、Result Package 及 Future Domain Readiness 的候選演進 |
| Planning Status | READY_FOR_PM_MAINLINE_PLANNING_REVIEW |
| Authority Boundary | Planning only; no Implementation Authorization or Product Scope change |
| Date | 2026-08-07 (Asia/Taipei) |

## Source Basis

- `PM/PVOS_PRODUCT_DIRECTION_DECISION_RECORD.md`
- `PM/PVOS_DUAL_WORKFLOW_EXECUTION_STRATEGY.md`
- `PM/PVOS_PRODUCT_DIRECTION_DECISION_PACKAGE.md`
- `PM/PVOS_1_0_PM_PRODUCT_ACCEPTANCE_RECORD.md`
- `PM/PVOS_1_1_PRODUCTION_READINESS_DECISION_RECORD.md`
- Current C# Core／Layout、Runtime、Golden Dataset、Regression、Evidence and Result Package assets

## Planning Boundary

本 Package 只建立 Mainline Evolution 候選方向、投資排序與 Gate 3 前置證據。它不會：

- 建立 GitHub Issue Queue、branch、commit or PR。
- 修改 source code、tests、runtime or Product behavior。
- 啟動 coding or implementation。
- 實作 Rooftop、Ground Mount、Fishery or other Domain capability。
- 將 Python 提升為 Product Engine or Product Behavior Authority。
- 修改 EOS、Governance、PVOS Scope or existing Acceptance status。
- Promotion Legacy assets or Canonical Project Model。

`Mainline ACTIVE` 代表既有工作流可接受未來經正式授權的工作，不代表本 Planning Package 已授權任何候選項目。

## Executive Planning Recommendation

建議 Mainline 投資次序：

1. **P0 — Product Integrity Preservation**：C# Product authority、Golden Regression、result lineage and failure isolation。
2. **P1 — Validation／Evidence and Result Package Evolution**：在不新增 Product behavior、API、UI or Cloud commitment 下，提高 repeatability、traceability and engineering usability。
3. **P2 — Cross-Domain Core Readiness Review**：只審查真正跨 Domain 的 Geometry／Partition／Validation contract gap。
4. **P3 — Future Domain Readiness Pattern**：建立可審查的 Domain Contract、Adapter and Evidence interface pattern；不實作任何 Domain。

任何候選只有在具備 Section 8 Gate Criteria 且 PM／Owner 明確授權後，才能進入 Gate 3。

## 1. Mainline Evolution Vision

### Long-Term Role

C#／.NET Mainline 是 PVOS 唯一正式產品行為來源，負責將經核准的 Product input 轉為 deterministic result，並透過 Validation、Evidence and Result Package 支援可重現 Product delivery。

Mainline 的長期角色不是吸收所有 Domain knowledge，而是提供穩定、可測試、跨 Domain 可重用的產品核心。Domain semantics、eligibility、professional responsibility and approval remain outside Core until separately selected and authorized.

### Product Behavior Authority

| Authority Area | Mainline Responsibility | Boundary |
|---|---|---|
| Product contracts | Own accepted C# input／result contracts | Contract changes require compatibility and Gate evidence |
| Geometry／Partition | Own reusable deterministic behavior | Does not infer Domain legality or semantics |
| Layout | Sole placement calculation authority | No Python or Domain duplicate Engine |
| Validation | Own Product input／result and accepted-rule validation | Does not replace professional approval |
| Evidence lineage | Produce traceable Product result identity and references | Evidence consumers do not recalculate |
| Release candidate | Form C# Mainline release evidence | PM／Owner retains Product Acceptance authority |

### Release Responsibility

A Mainline release candidate must preserve:

- Explicit accepted behavior and Scope。
- Deterministic repeatability。
- C# tests、Golden／Regression and affected-claim isolation。
- Result lineage from input through Product output。
- Compatibility and version identity where contracts change。
- No Domain-specific behavior hidden as Core improvement。
- No Python Product authority or second Engine。
- PM Product Acceptance boundary。

## 2. Core Capability Evolution

### Existing Core Assessment

| Core Capability | Existing Evidence State | Cross-Domain Common Value | Current Boundary |
|---|---|---|---|
| Geometry | Explicit points、polygons、GeometrySet、Local Axis and geometry validation | Stable representation of Domain-approved planar input | No Terrain、Roof、Aquaculture semantics or automatic repair |
| Partition | Explicit region identity and selection | Common separation of accepted feasible regions | Does not derive eligible regions from Domain Rules |
| Layout | Deterministic C# module placement with explicit parameters | Reusable placement behavior after Domain approval | No obstacle、shading、electrical、structural or domain optimization |
| Validation | Bounded input／result errors, tests and negative cases | Common contract and integrity verification | Not a general Domain Rule Engine |
| Evidence | Golden manifests、hash、repeatability and claim isolation | Cross-domain traceability and change evidence | Cannot create professional or customer acceptance |
| Result Package | Read-only result／evidence packaging and no-recalculation boundary | Stable downstream review surface | No API、UI、Cloud or persistence commitment |

### Cross-Domain Common Capability Test

A candidate belongs in Core only when all conditions hold:

1. It is required by at least two independently evidenced Domain or Product workflows, or is intrinsic to current Product integrity。
2. Its semantics can be expressed without Roof、Terrain、Aquaculture or other Domain assumptions。
3. It has one deterministic C# behavior and does not require a Domain-specific execution branch。
4. It can be covered by bounded contracts、tests、Golden／Regression and failure isolation。
5. Ownership belongs to Product Mainline rather than a professional Domain authority。
6. Promotion does not modify Product Scope without explicit approval。

Until these conditions are evidenced, the item remains a Domain、Adapter、Validation or Research candidate.

### Core Improvement Candidates

These are review candidates, not implementation commitments.

| Candidate | Product Value | Evidence Needed | Key Boundary |
|---|---|---|---|
| Contract invariants documentation | Make accepted Geometry／Partition／Layout assumptions explicit and reviewable | Current source／tests mapping and compatibility review | Documentation／contract review must not create new behavior |
| Validation error identity／claim isolation | Improve diagnosis and independent failure handling | Existing error catalog、negative tests、consumer need | Preserve existing accepted results and order |
| Deterministic result fingerprint | Strengthen result／revision identity | Field lineage、canonical ordering decision、collision／compatibility review | Fingerprint observes Product result; no new placement |
| Partition／input provenance reference | Allow Result evidence to identify approved input source | Consumer evidence need、ownership and data-boundary review | No persisted Canonical Project Model or Domain lifecycle |
| Shared tolerance／numeric policy review | Reduce ambiguity across Geometry and validation | Existing behavior inventory、test coverage、compatibility risk | No hidden geometry repair or Domain-specific tolerance |
| Performance／scale characterization | Establish current bounded operating envelope | Repeatable benchmark definition and accepted workload | Measurement only unless separate optimization authorization |

### Non-Core Boundaries

The following remain outside Core unless separately re-evaluated with cross-domain evidence and authority:

- Roof Rules、Obstacle semantics、Walkways and Setbacks。
- Terrain、GIS、Road、Drainage and construction zoning。
- Aquaculture、Water systems and coexistence requirements。
- Structural、Electrical、Shading and regulatory decisions。
- CAD／GIS host transactions、database ownership and full integration。
- UI、Cloud、API product commitments and persistence platform。
- Customer workflow、payer or commercial behavior。
- Legacy／Canonical models without approved Promotion Gate。

## 3. Validation / Evidence Evolution

### Dual-Line Model

```text
C# Mainline Product Result
          ↓
C# Tests / Golden Regression / Result Lineage
          ↓
Python Validation / Evidence Automation
          ↓
PM Review
```

Python validates and reports; C# Mainline owns Product behavior.

### Python Validation Track Candidates

| Candidate | Intended Value | Required Controls | Explicit Exclusion |
|---|---|---|---|
| Validator usability | Repeatable entry point、clear prerequisites and stable output | Versioned usage、stable check IDs、failure semantics | No Product calculation |
| Evidence report enhancement | Faster review and claim／failure identification | Raw finding retention、provenance、deterministic report identity | No Product Acceptance authority |
| Regression orchestration | Consistent execution of admitted evidence sets | Manifest-driven scope、isolated failures、no silent skip | No automatic scenario admission |
| Evidence integrity automation | Verify files、hashes、references and completeness | Immutable source identity and explicit BLOCKED／FAIL | No Evidence repair or result rewrite |
| Engineering diagnostics | Support troubleshooting and field evidence collection | Read-only observation、version／boundary notice | No Geometry repair、placement or Domain rule decision |
| Comparison tooling | Compare admitted outputs／reports across executions | Field-level lineage and accepted normalization | No reinterpretation of Product values |

### C# Mainline Validation Evolution

| Area | Candidate Direction | Evidence Gate |
|---|---|---|
| Golden Regression | Preserve admitted bounded claims and isolate affected scenarios | Admission record、static expected evidence、repeatability |
| Test Coverage | Target accepted contracts、negative inputs、boundary and failure behavior | Requirement／claim mapping; avoid count-only targets |
| Result Lineage | Trace every packaged field to input、C# Product result or validation finding | Field catalog and no-recalculation proof |
| Compatibility | Detect changed contracts or result identity before release | Version policy candidate、comparison evidence、migration impact |
| Failure Isolation | Return only affected claims／tests for correction | Stable check／error identity and dependency mapping |

### Evidence Evolution Principles

- More tests do not automatically mean broader Product Scope。
- New Golden scenarios require Evidence Admission and PM review。
- Python can automate evidence processing but cannot decide expected Product behavior。
- Report aggregation must preserve raw PASS／FAIL／BLOCKED and affected Claim identity。
- Mainline changes require C# evidence even if first discovered with Python。
- External Domain evidence and Mainline Regression evidence remain related but distinct authorities。

### Python Promotion Boundary

```text
Discovery / Experiment
        ↓
Evidence Proven
        ↓
PM Review
        ↓
Mainline Promotion Candidate
        ↓
Gate 3 Authorization
        ↓
C# Implementation + Regression + Acceptance
```

Python remains Validation／Engineering Support only and must not replace C# Mainline or become a second PVOS Engine.

## 4. Result Package Evolution

### Current Direction

The Result Package is a read-only engineering Evidence boundary. It packages existing Product results and evidence references without recalculating placement or creating an independent Product interpretation.

### Result Contract Review Candidates

| Review Area | Candidate Question | Required Evidence | Boundary |
|---|---|---|---|
| Result identity | What stable identity distinguishes request、execution、Product version and result? | Field lineage、repeatability and collision／compatibility analysis | Identity cannot change Product values |
| Contract fields | Which existing result fields are mandatory、optional or derived? | C# contract／source／test mapping | No undocumented new Product behavior |
| Status／finding references | How are errors、warnings and validation findings referenced? | Stable code identity and affected-claim map | Package does not decide acceptance |
| Version identity | How is Result Package format／semantics versioned? | Consumer inventory、compatibility and change policy | Planning does not create a public API commitment |
| Evidence reference | How are input、manifest、hash、test and approval records linked? | Provenance and integrity rules | Reference does not copy／promote unauthorized assets |
| Consumer boundary | Who may read the package and what may they do? | Consumer role／workflow evidence | Consumers cannot recalculate or reinterpret placement |

### Candidate Minimum Result Package Description

Planning may evaluate the need for:

- Package／schema identity。
- C# Product version and execution identity。
- Input／request and selected Partition reference。
- `LayoutResult` lineage。
- Validation findings and evidence manifest references。
- Integrity／fingerprint reference。
- Compatibility／consumer boundary statement。
- Explicit exclusions and unresolved risks。

This list is a review checklist, not an approved schema or serialization contract.

### Explicit Non-Commitments

The Result Package evolution shall not create:

- Public or private API commitment。
- UI or presentation product implementation。
- Cloud platform、network service or hosted evidence store。
- Canonical Project Model or Product database。
- CAD／GIS integration contract。
- Downstream recalculation or alternative Engine。

## 5. Future Domain Readiness

### Purpose

Prepare reusable review patterns so a future selected Domain can describe its data、rules、translation、responsibility and Evidence without modifying Core prematurely.

Preparation does not select or implement Rooftop、Ground Mount or Fishery PV.

### Domain Contract Pattern

A future Domain proposal should be able to define:

| Contract Area | Required Pattern |
|---|---|
| Domain identity | Domain、version、Owner and effective scope |
| Data semantics | Source、rights、units、coordinates、version and accepted status |
| Eligibility | How Domain-approved feasible regions are established |
| Rules | Rule ID、source、applicability、version and change authority |
| Translation | Domain input → Core Geometry／Partition／parameters mapping |
| Failure boundary | Missing／invalid Domain evidence stops before Core or yields explicit rejection |
| Professional responsibility | Domain、Structural、Electrical、Shading、regulatory and PM boundaries |
| Evidence admission | Case provenance、bounded claim、integrity and approval |
| Result review | Domain acceptance／rejection without changing C# result |

### Adapter Boundary Pattern

Future Adapter readiness may review:

- Source system identity and ownership。
- Unit、coordinate and precision conversion。
- Supported geometry／field subset。
- Transaction／database ownership outside Core。
- Conversion failure and unsupported input handling。
- Provenance and round-trip／comparison evidence where applicable。

Adapter readiness does not authorize AutoCAD Full Integration、GIS implementation or persistence.

### Evidence Interface Pattern

Future Domain evidence should reference, not silently merge:

- Source data identity。
- Domain Rule and Owner approval。
- Translation version and accepted Core input。
- C# Product result and validation findings。
- Python external verification result。
- Professional review and PM disposition。

The interface is a traceability pattern, not an API or Canonical schema.

### Domain-Specific No-Implementation Confirmation

| Domain | Planning Disposition |
|---|---|
| Rooftop PV | Gate 2 External Evidence Hold; no Domain implementation |
| Ground Mount PV | Deferred feasibility／evidence preparation only |
| Fishery PV | Deferred Domain ownership／evidence research only |

## 6. Technical Debt / Risk Assessment

| Risk Category | Risk | Impact | Candidate Control | Gate Effect |
|---|---|---|---|---|
| Architecture | Core absorbs Domain semantics for convenience | Coupling、hidden Scope and conflicting behavior | Cross-domain common capability test、Core／Domain contract review | Block Gate 3 if ownership unclear |
| Architecture | Result Package becomes API／database／second interpretation | Compatibility commitment and result divergence | Read-only lineage、consumer boundary、no-recalculation proof | Separate authorization required |
| Dual-Line | Python validator gradually calculates or repairs Product result | Second Engine and C#／Python inconsistency | Source／execution audit、stable role boundary、Promotion Gate | Immediate stop |
| Dual-Line | Python discovery is treated as Mainline implementation | Unreviewed behavior enters Product | Evidence → PM Review → C# candidate → Gate 3 | Block Promotion |
| Evidence | Golden coverage is mistaken for unlisted Domain coverage | False readiness／acceptance claims | Bounded Claim and Admission matrix | Return affected evidence |
| Evidence | Automation hides FAIL／BLOCKED or changes expected output | Invalid PM decision | Raw finding retention、stable IDs、failure isolation | Verification failure |
| Evidence | Result identity／version is ambiguous | Consumers compare incompatible results | Version／lineage review before contract change | Block release candidate |
| Scope Expansion | Rooftop／Ground／Fishery rules appear as generic Core improvement | Gate bypass and professional risk | Domain hold policy、changed-scope audit | Gate 3 locked |
| Scope Expansion | Adapter／Result review implies UI／Cloud／API commitment | Unplanned platform expansion | Explicit non-commitments and separate Gate | Defer |
| Legacy／Canonical | Historical asset used to accelerate work without Promotion review | Unaccepted behavior／ownership | Evidence-only classification and no-promotion check | Stop affected candidate |
| Technical Debt | Existing behavior assumptions lack explicit contract mapping | Regression risk during evolution | Source／test／claim inventory before change | Gate 3 evidence requirement |
| Technical Debt | Scenario／test growth increases maintenance without risk coverage | Cost without decision value | Risk-based coverage and affected-claim analysis | PM priority review |

## 7. Investment Priority

### Evaluation Scale

- **Value**：Product integrity、engineering efficiency or future readiness value。
- **Effort**：analysis、contract、implementation and maintenance cost。
- **Risk**：behavior、compatibility、authority and Scope risk。
- **Evidence Readiness**：current evidence available for a Gate decision。

| Priority | Candidate Investment | Value | Effort | Risk | Evidence Readiness | Recommended Disposition |
|---|---|---:|---:|---:|---:|---|
| P0 | C# Product authority／Regression／Result lineage preservation | High | Low–Medium | Low | High | Maintain as mandatory baseline |
| P0 | Failure isolation and stable validation identity review | High | Medium | Low–Medium | High | Prepare bounded Gate evidence |
| P1 | Python validator usability／Evidence report automation | Medium–High | Medium | Low–Medium | High | Candidate; Validation／Support only |
| P1 | Result Package identity／version／consumer boundary review | High | Medium | Medium | Medium–High | Review contract before implementation proposal |
| P1 | Test／Golden coverage mapped to accepted claims | High | Medium | Low | High | Improve evidence quality, not Scope |
| P2 | Core contract invariant／numeric policy review | Medium–High | Medium | Medium | Medium | Evidence inventory first |
| P2 | Performance／scale characterization | Medium | Medium | Low | Medium | Measurement candidate only |
| P3 | Domain Contract／Adapter／Evidence interface pattern | Medium | Medium | Medium | Medium | Preparation only; no Domain implementation |
| Deferred | Rooftop Domain behavior | Potential High | Unknown | High | Blocked external evidence | Gate 2 Hold |
| Deferred | Ground／Fishery Domain behavior | Unknown／Potential | High–Very High | High–Very High | Low | No implementation |
| Deferred | API／UI／Cloud／Full AutoCAD integration | Unproven | High | High | Low | Outside current planning scope |

### Recommended Priority

**P0 first: preserve and make explicit Product integrity — C# authority、Regression、failure isolation and Result lineage.**

P1 candidates may proceed to separate planning review only when their bounded value and no-new-behavior claim are evidenced. P2／P3 remain preparatory until their decision value is clear.

## 8. Implementation Gate Criteria

### Gate 3 Purpose

Gate 3 determines whether one bounded Mainline candidate has enough evidence and authority to enter implementation. This Package does not open Gate 3.

### Mandatory Gate 3 Evidence

| Criterion | Required Evidence | Failure Effect |
|---|---|---|
| Authority | Owner／PM-approved candidate and explicit Implementation Authorization | No coding／Issue Queue |
| Product Scope | Evidence that behavior is inside accepted Scope, or separate approved Scope change | Return／reject candidate |
| Problem／Value | Factual Product integrity、user or engineering need | No feature-by-assumption |
| Existing Asset Inspection | Current source、tests、contracts and related evidence inspected | Prevent duplicate／conflicting capability |
| Architecture Boundary | Core／Domain／Adapter／Validation responsibility and dependencies | Block hidden Domain behavior |
| C# Mainline Contract | Inputs、outputs、invariants、errors、version and compatibility | No Product behavior implementation |
| Python Boundary | No Product calculation、second Engine or authority transfer | Immediate stop |
| Acceptance Criteria | Bounded functional、negative、repeatability and lineage criteria | No PM-ready completion claim |
| Golden／Regression Plan | Affected claims、static evidence、failure isolation and admission needs | Block release candidate |
| Result／Consumer Boundary | No recalculation、API／UI／Cloud commitment or hidden persistence | Return contract |
| Risk／Rollback | Compatibility、failure、migration／rollback where applicable | Block implementation |
| Changed-Scope Audit | Explicit excluded Domain、Legacy、Canonical and platform areas | Stop Scope expansion |

### Additional Gate 3 Evidence by Candidate Type

#### Core Behavior Candidate

- Proof of cross-domain commonality or intrinsic Product integrity need。
- Compatibility analysis against accepted behavior and Golden evidence。
- No Domain Rule or professional decision embedded in Core。

#### Validation／Evidence Candidate

- Proof that expected Product behavior remains owned by C#。
- Stable check identity、raw findings and no Evidence repair。
- Evidence automation maintenance owner and failure semantics。

#### Result Package Candidate

- Field-level lineage and version policy candidate。
- Identified consumer need and prohibited consumer behavior。
- Explicit no-API、no-UI、no-Cloud and no-recalculation boundaries。

#### Future Domain Readiness Candidate

- Pattern／documentation only unless Gate 2 selected a Domain。
- No Domain-specific rule、case Promotion or implementation。
- Gate 2 and external evidence dependencies explicitly preserved。

### Gate 3 Entry Decision

Before Gate 3 may open, PM／Owner must select one bounded candidate and issue explicit authority. Permitted pre-implementation outcomes:

- `AUTHORIZED WITH BOUNDARY CONDITIONS`
- `RETURNED FOR ADDITIONAL EVIDENCE`
- `DEFERRED`
- `REJECTED`

Only `AUTHORIZED WITH BOUNDARY CONDITIONS` can permit implementation planning／execution, and only within its stated scope.

## Remaining Decisions

1. Which P0 integrity candidate should receive the first bounded Gate 3 evidence package?
2. Does Result Package version identity solve a confirmed consumer need, and who owns compatibility?
3. Which validation／evidence automation improvement provides measurable review or maintenance value?
4. Are current Core invariants sufficiently explicit, or is a source／test／claim inventory needed first?
5. What benchmark workload is representative for performance characterization without implying Domain support?
6. Who owns maintenance for future Domain Contract、Adapter and Evidence interface patterns?
7. Does any candidate require Product Scope or Architecture decision beyond Gate 1? If yes, Gate 3 remains blocked pending that authority.

## Next Gate

1. **PM Mainline Planning Review** — review priorities、boundaries and remaining decisions。
2. **Bounded Candidate Selection** — select at most one candidate for Gate evidence preparation。
3. **Gate 3 — Implementation Authorization** — only after all Section 8 evidence is complete and explicit Owner／PM authority is issued。

Rooftop Gate 2 External Evidence Hold remains independent and unchanged.

## Constraint Verification

| Constraint | Result |
|---|---|
| No GitHub Issue Queue | PASS |
| No source code modification | PASS |
| No coding started | PASS |
| No Domain capability implemented | PASS |
| No EOS modification | PASS |
| No Governance modification | PASS |
| No PVOS Scope modification | PASS |
| No Legacy Promotion | PASS |
| No Canonical Project Model Promotion | PASS |
| Gate 3 not opened | PASS |

## Package Status

**READY_FOR_PM_MAINLINE_PLANNING_REVIEW**
