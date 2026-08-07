# PVOS Bounded Mainline Candidate Selection Package

## Package Identity

| Field | Value |
|---|---|
| Package | `PVOS_BOUNDED_MAINLINE_CANDIDATE_SELECTION_PACKAGE` |
| Product | PVOS |
| Workflow | Workflow A — Product Mainline |
| Purpose | 從 P0／P1 候選中選出第一個 bounded Mainline candidate，供 Gate 3 前置證據準備 |
| Status | READY_FOR_PM_CANDIDATE_SELECTION_REVIEW |
| Recommended Candidate | Candidate A — C# Product Integrity Enhancement |
| Gate Effect | Candidate recommendation only; Gate 3 remains LOCKED |
| Date | 2026-08-07 (Asia/Taipei) |

## Source Basis

- `PM/PVOS_MAINLINE_PRODUCT_EVOLUTION_PLANNING_PACKAGE.md`
- `PM/PVOS_PRODUCT_DIRECTION_DECISION_RECORD.md`
- `PM/PVOS_DUAL_WORKFLOW_EXECUTION_STRATEGY.md`
- Current C# Core、Layout、Runtime、Golden Dataset、Regression、Validation and Result Package evidence

## Selection Boundary

This Package evaluates and recommends one bounded candidate. It does not:

- Create a GitHub Issue Queue、branch、commit or PR。
- Modify code or start implementation。
- Open Gate 3 or grant Implementation Authorization。
- Change PVOS Scope、EOS、Governance or existing Product Acceptance。
- Implement Rooftop、Ground Mount、Fishery or any Domain capability。
- Promote Legacy assets or Canonical Project Model。

## Executive Recommendation

Select **Candidate A — C# Product Integrity Enhancement** as the first bounded Mainline candidate, narrowed to:

> **Inventory and prove existing C# Core invariants, stable failure identity, Result lineage and Golden Regression claim mapping without adding or changing Product behavior.**

Candidate A is preferred because it directly protects the sole Product Behavior Authority, uses existing high-readiness evidence, reduces risk for every later Mainline candidate and can be bounded as an integrity／contract-evidence task. Candidate B is valuable but is already a support track and should follow a clearer C# authority baseline. Candidate C has long-term value but requires consumer and compatibility decisions not yet evidenced.

Selection of Candidate A means only that it is recommended for Gate 3 evidence preparation. It is not implementation authorization.

## Candidate Pool

| Candidate | Short Name | Proposed Bounded Outcome |
|---|---|---|
| A | C# Product Integrity Enhancement | Existing invariant、failure、lineage and Golden claim baseline made explicit and verifiable |
| B | Python Validation／Evidence Automation | More usable and repeatable external validation／evidence workflow without Product authority |
| C | Result Package Evolution | Reviewed result／version identity、evidence references and consumer boundary |

## Evaluation Method

Each candidate is evaluated against:

1. Product Value。
2. Mainline Fit。
3. Evidence Readiness。
4. Implementation Risk。
5. Gate 3 Readiness。

Qualitative ratings:

- **High**：strong direct evidence／fit or material impact。
- **Medium**：valuable but evidence／decision gaps remain。
- **Low**：weak fit or insufficient evidence for first candidate。

## Candidate A — C# Product Integrity Enhancement

### Bounded Candidate Definition

Candidate A includes only:

- Core invariant inventory。
- Stable failure identity review。
- Result lineage mapping。
- Golden Regression strengthening through requirement／claim mapping and gap evidence。

Candidate A does not authorize new Geometry、Partition、Layout、Constraint or Domain behavior. Any discovered behavior change becomes a separate candidate and must not be implemented under this scope.

### 1. Product Value

#### Problem Solved

Existing behavior is supported by source、tests、Golden scenarios and Runtime evidence, but its invariants and field-level claim chain are distributed across assets. This makes future changes vulnerable to accidental contract drift, ambiguous failure impact and weak result traceability.

#### Engineering Impact

- Gives engineers one explicit map from accepted Product behavior to C# source、tests、Golden claims and Result fields。
- Improves failure isolation and prevents unrelated capabilities from being revalidated unnecessarily。
- Establishes a safer baseline for Result Package、Validation automation and future bounded Core work。
- Helps distinguish a genuine behavior change from documentation、test or evidence maintenance。

#### Long-Term PVOS Value

High. Every Mainline release、candidate Promotion and future Domain integration depends on stable Core authority and traceable accepted behavior.

**Product Value Rating: HIGH**

### 2. Mainline Fit

| Fit Area | Assessment |
|---|---|
| C# Responsibility | Directly concerns current C# Core／Layout contracts and release evidence |
| Product Behavior Authority | Reinforces rather than transfers Mainline authority |
| Core Compatibility | Reviews existing Geometry、Partition、Layout、Validation and Result behavior without Domain semantics |
| Python Boundary | Python may verify Evidence only; expected behavior remains C#／PM controlled |

**Mainline Fit Rating: HIGH**

### 3. Evidence Readiness

#### Existing Evidence

- C# Domain and Layout source。
- Layout and Production Readiness tests。
- PVOS-GOLDEN-001 through 008 and manifest evidence。
- Runtime Input、Workflow、Presentation and Result Package boundaries。
- Product Acceptance and Production Readiness records。
- Python validation and repeatability evidence as independent support。

#### Missing Evidence

- One authoritative Core invariant catalog mapped to accepted Scope。
- Stable failure／warning identity catalog and affected-claim mapping。
- Field-level lineage from input／C# result to Result Package／Evidence。
- Explicit mapping from every accepted invariant to tests and Golden scenarios。
- Disposition for uncovered accepted claims versus out-of-scope behavior。

#### Validation Method

- Read-only source／contract／test inventory first。
- Requirement → invariant → source → test → Golden／Evidence mapping。
- Negative and boundary evidence review。
- Repeatability and Result lineage verification。
- Changed-scope and no-new-behavior audit。

**Evidence Readiness Rating: HIGH**

### 4. Implementation Risk

| Risk | Level | Control |
|---|---|---|
| Architecture risk | Low–Medium | Inventory existing authority; no architecture change |
| Scope risk | Low if bounded | Any newly proposed behavior is excluded and returned separately |
| Maintenance risk | Medium | Assign owner、version and update trigger for catalogs／mappings |
| Behavioral regression | Low for evidence-only work; higher if code change is introduced | Gate scope prohibits behavior change unless separately authorized |
| Evidence overclaim | Medium | Every claim must identify accepted Scope and exclusions |

**Implementation Risk Rating: LOW–MEDIUM**

### 5. Gate 3 Readiness

| Requirement | Current State |
|---|---|
| Scope clarity | HIGH — bounded integrity／evidence task can be stated precisely |
| Contract clarity | MEDIUM–HIGH — current contracts exist but need consolidated invariant catalog |
| Acceptance criteria | DRAFTABLE from current accepted behavior and evidence |
| Regression plan | HIGH — existing tests and eight Golden scenarios provide baseline |
| Owner／maintenance | GAP — artifact owner and update triggers require PM decision |
| Change policy | GAP — disposition required if inventory reveals inconsistent accepted evidence |

**Gate 3 Readiness: CONDITIONAL — BEST OF CANDIDATE POOL**

## Candidate B — Python Validation / Evidence Automation

### Bounded Candidate Definition

- Validator usability。
- Evidence report automation。
- Regression support and engineering productivity。
- No Product calculation、expected-result authority or second Engine。

### 1. Product Value

#### Problem Solved

Reduce manual validation setup、evidence comparison and report preparation while preserving visible failures and stable evidence identity.

#### Engineering Impact

- Faster repeatable evidence runs。
- More consistent report／manifest checks。
- Better failure diagnosis and affected-claim isolation。

#### Long-Term PVOS Value

Medium–High. It improves engineering throughput, but Product authority and accepted behavior still depend on C# Mainline.

**Product Value Rating: MEDIUM–HIGH**

### 2. Mainline Fit

| Fit Area | Assessment |
|---|---|
| C# Responsibility | Indirect; observes C# Product results |
| Product Behavior Authority | Must remain entirely with C# Mainline |
| Core Compatibility | Strong as external validation, weak as first Mainline product candidate |
| Dual-Line Boundary | Explicit and already evidenced |

**Mainline Fit Rating: MEDIUM**

### 3. Evidence Readiness

#### Existing Evidence

- Python validator source、tests、usage and repeatability evidence。
- Stable validation check concepts and manifest／hash verification。
- Durable no-second-Engine and validation-only decisions。

#### Missing Evidence

- Prioritized usability problem with measurable engineering baseline。
- Named maintenance owner and report retention policy。
- Consumer／reviewer requirements for report evolution。
- Clear boundary between useful automation and unnecessary framework growth。

#### Validation Method

- Source audit proving no Product calculation。
- Repeatability and equivalent-report identity checks。
- Negative tests、raw finding retention and failure isolation。
- Measured engineering workflow improvement。

**Evidence Readiness Rating: HIGH TECHNICALLY／MEDIUM FOR VALUE**

### 4. Implementation Risk

| Risk | Level | Control |
|---|---|---|
| Architecture risk | Low | Keep tool external to Product Core |
| Scope risk | Medium | Prohibit Product behavior、scenario admission and acceptance authority |
| Maintenance risk | Medium–High | Define owner、Python runtime、report schema and support boundary |
| Second Engine risk | High impact, currently controlled | Mandatory source／execution audit and promotion boundary |

**Implementation Risk Rating: MEDIUM**

### 5. Gate 3 Readiness

| Requirement | Current State |
|---|---|
| Scope clarity | HIGH |
| Contract clarity | MEDIUM — validator/report contract needs bounded target |
| Acceptance criteria | MEDIUM–HIGH technically; value metric missing |
| Regression plan | HIGH |
| Maintenance／consumer evidence | GAP |

**Gate 3 Readiness: CONDITIONAL — DEFER AFTER CANDIDATE A**

## Candidate C — Result Package Evolution

### Bounded Candidate Definition

- Result identity。
- Version identity。
- Evidence references。
- Consumer boundary。
- No API、UI、Cloud、persistence or recalculation commitment。

### 1. Product Value

#### Problem Solved

Clarify how Product result、version and Evidence can be reliably identified and consumed without downstream reinterpretation.

#### Engineering Impact

- Stronger result comparison and compatibility review。
- Clearer Evidence handover and consumer responsibilities。
- Better foundation for future Domain or integration review。

#### Long-Term PVOS Value

High, especially as consumers and Domains increase. Current consumer demand and compatibility ownership remain insufficiently evidenced.

**Product Value Rating: HIGH POTENTIAL／MEDIUM CURRENT EVIDENCE**

### 2. Mainline Fit

| Fit Area | Assessment |
|---|---|
| C# Responsibility | Result identity and lineage originate from C# Product result |
| Product Behavior Authority | Strong fit if package stays read-only |
| Core Compatibility | Compatible, but format／version decisions can create long-term commitments |
| Consumer Boundary | Must prevent recalculation、API implication and alternative interpretation |

**Mainline Fit Rating: HIGH**

### 3. Evidence Readiness

#### Existing Evidence

- Runtime Result Package and Presentation no-recalculation boundaries。
- Existing C# `LayoutResult` fields and Result Evidence。
- Golden／Regression and Python Evidence validation。

#### Missing Evidence

- Identified consumers and their required fields／workflows。
- Owner for format／semantic version compatibility。
- Field-level lineage catalog。
- Version change、compatibility、deprecation and migration policy。
- Decision whether a persistent serialized format is needed at all。

#### Validation Method

- Consumer need review。
- Field lineage and no-recalculation audit。
- Version／compatibility scenario review。
- Golden result comparison and negative consumer-boundary checks。

**Evidence Readiness Rating: MEDIUM**

### 4. Implementation Risk

| Risk | Level | Control |
|---|---|---|
| Architecture risk | Medium–High | Keep package read-only and separate from Core calculation |
| Scope risk | High | Explicitly exclude API、UI、Cloud、database and Canonical Model |
| Maintenance risk | High | Version／compatibility owner and lifecycle policy required |
| Consumer lock-in | Medium–High | Prove consumer need before format commitment |

**Implementation Risk Rating: MEDIUM–HIGH**

### 5. Gate 3 Readiness

| Requirement | Current State |
|---|---|
| Scope clarity | MEDIUM — review boundary clear; concrete result contract not selected |
| Contract clarity | MEDIUM–LOW — identity／version policy unresolved |
| Acceptance criteria | MEDIUM — lineage and no-recalculation criteria available |
| Regression plan | MEDIUM–HIGH — existing results help; compatibility cases missing |
| Consumer／owner evidence | GAP |

**Gate 3 Readiness: NOT FIRST — DEFER PENDING CONSUMER／COMPATIBILITY EVIDENCE**

## Comparative Evaluation Matrix

| Criterion | Candidate A | Candidate B | Candidate C |
|---|---|---|---|
| Product Value | High | Medium–High | High potential／Medium evidenced |
| Mainline Fit | High | Medium | High |
| Evidence Readiness | High | High technical／Medium value | Medium |
| Architecture Risk | Low–Medium | Low–Medium | Medium–High |
| Scope Risk | Low when bounded | Medium | High |
| Maintenance Risk | Medium | Medium–High | High |
| Scope Clarity | High | High | Medium |
| Contract Clarity | Medium–High | Medium | Medium–Low |
| Acceptance Criteria Readiness | High | Medium–High | Medium |
| Regression Plan Readiness | High | High | Medium–High |
| Recommended Order | **1** | **2** | **3** |

## Selected Candidate

### Recommendation

**Candidate A — C# Product Integrity Enhancement**

### Selected Bounded Scope

1. Inventory accepted C# Core invariants for Geometry、Partition、Layout、Validation and `LayoutResult`。
2. Map errors／warnings／failures to stable identity and affected Product claims。
3. Trace Result fields to accepted input、C# source behavior、tests and Evidence references。
4. Map accepted claims to C# tests and PVOS-GOLDEN-001–008。
5. Identify gaps、contradictions and out-of-scope behavior without correcting or implementing them under this candidate。
6. Define update triggers and maintenance ownership for the resulting integrity artifacts。

### Explicit Out of Scope

- Any Product behavior change。
- New Geometry、Partition、Layout or Constraint capability。
- Rooftop、Ground Mount、Fishery or other Domain behavior。
- Python Product calculation or second Engine。
- Result Package schema／API implementation。
- UI、Cloud、AutoCAD Full Integration、Electrical or Shading。
- Legacy／Canonical Promotion。

## Why Candidate A Is Selected

- It directly reinforces C#／.NET Product Behavior Authority approved at Gate 1。
- It has the highest combined Product value、evidence readiness and bounded-scope clarity。
- It can first expose inconsistencies without prematurely authorizing correction or new behavior。
- It supplies the authority baseline required by both Python Evidence automation and Result Package evolution。
- It reduces architecture and acceptance risk for future candidates while remaining independent of Rooftop Gate 2 Hold。

## Deferred Candidates

### Candidate B — Deferred to Second Position

Reason:

- Technical evidence is strong, but the first Mainline candidate should clarify C# invariants and accepted claims before automating more evidence around them。
- A measurable validator usability／maintenance problem and responsible owner remain needed。
- Existing Python tooling already supports validation; deferral does not block current Evidence runs。

Re-entry evidence:

- Candidate A integrity baseline accepted。
- Named tool／report maintenance owner。
- Measured engineering productivity or review problem。
- Bounded report／automation contract and no-second-Engine validation plan。

### Candidate C — Deferred to Third Position

Reason:

- Consumer need、version owner and compatibility policy are unresolved。
- Premature format evolution can create API、persistence or compatibility commitments。
- Candidate A Result lineage mapping should precede any Result Package contract evolution。

Re-entry evidence:

- Candidate A field-level lineage accepted。
- Identified consumer and bounded need。
- Version／compatibility owner and policy proposal。
- Explicit no-API、no-UI、no-Cloud、no-recalculation contract。

## Required Gate 3 Evidence for Candidate A

Gate 3 remains locked until all evidence below is ready and PM／Owner explicitly opens the Gate.

| Gate Evidence ID | Required Evidence | Passing Condition |
|---|---|---|
| `ML-A-G3-001` | Candidate Scope Record | Included／excluded artifacts and no-behavior-change boundary approved |
| `ML-A-G3-002` | Existing Asset Inspection | Source、tests、Golden、Runtime、Result and decision evidence inventoried |
| `ML-A-G3-003` | Accepted Claim Baseline | Product Acceptance／Scope claims identified without adding claims |
| `ML-A-G3-004` | Core Invariant Draft | Each invariant has source、owner、version and applicability |
| `ML-A-G3-005` | Failure Identity Draft | Errors／warnings／rejections mapped to affected claims and stable identity |
| `ML-A-G3-006` | Result Lineage Draft | Every in-scope result field traces to input、C# behavior and evidence |
| `ML-A-G3-007` | Regression Coverage Map | Claims mapped to tests／Golden scenarios; gaps explicit |
| `ML-A-G3-008` | Acceptance Criteria | Completeness、traceability、contradiction、no-new-behavior and maintenance criteria |
| `ML-A-G3-009` | Maintenance／Update Policy | Named owner and triggers for source、contract、test or acceptance changes |
| `ML-A-G3-010` | Risk／Contradiction Disposition | No silent correction; each inconsistency returned for separate PM decision |
| `ML-A-G3-011` | Dual-Line／Scope Audit | C# authority preserved; Python validation only; no Domain／Legacy／Canonical expansion |
| `ML-A-G3-012` | Explicit Implementation Authorization | Owner／PM selects exact execution scope and authorizes Gate 3 |

## Candidate A Acceptance Criteria Draft

These criteria are proposed for Gate 3 review and are not yet approved:

1. Every accepted in-scope Core behavior maps to a uniquely identified invariant or documented boundary。
2. Every invariant maps to current C# source and at least one verification method, or is explicitly marked GAP。
3. Every in-scope error／warning／rejection has stable identity and affected-claim mapping。
4. Every in-scope `LayoutResult`／Result Package value has field-level lineage or an explicit unresolved gap。
5. PVOS-GOLDEN-001–008 are mapped only to their bounded claims; no Domain coverage is inferred。
6. Contradictions are visible and receive PM disposition; none are silently corrected。
7. No source code、Product behavior、Scope、Domain capability or accepted evidence is changed by inventory work unless separately authorized。
8. Artifact owner、version and update trigger are defined。
9. Python is used only for Evidence／consistency checking and does not establish expected Product behavior。

## Regression Plan Draft

| Layer | Review Method | Expected Output |
|---|---|---|
| C# unit／regression tests | Map test name to invariant、claim and failure identity | Coverage map with uncovered／duplicate claims |
| Golden Dataset | Map scenario and static expected evidence to bounded claim | Golden claim matrix; no Domain inference |
| Runtime／CLI | Trace constructed input through C# execution to result fields | Runtime lineage map |
| Python validator | Verify existing Evidence identity、hash and repeatability | Independent support report; no Product authority |
| Acceptance records | Map accepted Scope and exclusions to evidence | Acceptance-to-evidence matrix |

No new test or code execution scope is authorized by this draft. Gate 3 must define whether implementation includes documentation only, test additions or other bounded changes.

## Stop Conditions

Stop Candidate A Gate preparation or future execution if:

- Work requires changing Product behavior rather than documenting／verifying it。
- An invariant depends on unapproved Rooftop、Ground Mount、Fishery or other Domain Rules。
- Python is required to define expected Product behavior or calculate results。
- Result lineage requires a new API、UI、Cloud、database or Canonical Model commitment。
- Legacy assets must be promoted to fill a gap。
- Existing Acceptance records conflict and PM disposition is unavailable。
- Scope cannot remain bounded to Product integrity。
- No owner accepts maintenance of integrity artifacts。
- Gate 3 is not explicitly authorized。

## Gate 3 Readiness Assessment

| Area | Status | Remaining Action |
|---|---|---|
| Candidate selection recommendation | READY_FOR_PM_REVIEW | PM select／return／defer |
| Scope boundary | DRAFT READY | PM approve bounded scope |
| Existing evidence availability | HIGH | Formal inspection package required |
| Contract／invariant baseline | PARTIAL | Consolidated draft required |
| Acceptance criteria | DRAFT READY | PM approve／amend |
| Regression plan | DRAFT READY | PM approve exact execution level |
| Owner／maintenance | GAP | Assign accountable owner |
| Explicit Gate 3 authority | LOCKED | Separate Owner／PM authorization required |

**Overall Gate 3 Readiness: CONDITIONAL — NOT OPEN**

## Remaining Decisions

1. Does PM select Candidate A as the first bounded Mainline candidate?
2. Is Candidate A initially documentation／evidence-only, or may a later Gate 3 authorization include bounded test changes?
3. Who owns the Core invariant、failure identity、Result lineage and Regression mapping artifacts?
4. Which Acceptance record is authoritative if inventory finds inconsistent claims?
5. Does Result lineage stop at `LayoutResult`, or include the current read-only Result Package fields in the first scope?
6. What is the approved disposition process for uncovered claims or contradictions?
7. When Candidate A is accepted, should Candidate B or C be reviewed next?

## Next Step

PM Candidate Selection Review. If Candidate A is selected, prepare only the `ML-A-G3-001` through `ML-A-G3-011` evidence package. Gate 3 remains locked until `ML-A-G3-012` explicit Owner／PM authorization.

## Constraint Verification

| Constraint | Result |
|---|---|
| No GitHub Issue Queue | PASS |
| No source code modification | PASS |
| No implementation started | PASS |
| Gate 3 not opened | PASS |
| No EOS modification | PASS |
| No Governance modification | PASS |
| No PVOS Scope modification | PASS |
| No Domain capability implemented | PASS |

## Package Status

**READY_FOR_PM_CANDIDATE_SELECTION_REVIEW**
