# Engineering Operating System v1.0 Capability Matrix

## Purpose

Provide the single authoritative capability catalog and coverage record for Engineering Operating System v1.0.

## Information Domain

Governance

## Authority and Boundary

- **Owner Directive:** Engineering Operating System v1.0 must be built to 100%.
- **Daily source of truth:** The approved Planning Package is the Source of Truth for the day's work.
- **Sole execution source:** Codex execution may start only from an authorized GitHub Issue in the Execution Queue.
- **Boundary:** This matrix catalogs EOS governance and engineering-operating capabilities. It does not define PVOS product capabilities, modify the Product Blueprint, change the Operating Cycle, or change workspace architecture.
- **Completion authority:** Capability status records progress only. This matrix does not declare EOS v1.0 complete.
- **Work-order rule:** Every subsequent EOS v1.0 work order must reference at least one Capability ID from this matrix. A work order is a governance and coverage record; it is not Codex's execution source.

## Execution Source

```text
Planning Package (daily Source of Truth)
    ↓
GitHub Issue (Execution Queue; sole Codex Execution Source)
    ↓
Codex
    ↓
Evidence
    ↓
PM Review
```

No Planning Package item or PM Work Order directly triggers Codex execution. PM authorizes executable work through the corresponding GitHub Issue.

## Status Model

| Status | Meaning |
|---|---|
| Not Started | No authorized implementation evidence is recorded. |
| In Progress | Authorized foundation or implementation exists, but the capability is not yet complete. |
| Completed | The capability deliverable exists and meets its work-order acceptance criteria, pending or having passed governed review as recorded. |
| Verified | PM has accepted the capability evidence and recorded verification. |

Only one current status applies to each capability. `Verified` is the final capability state; it does not by itself declare EOS v1.0 complete.

## Capability Catalog

| Capability ID | Capability Name | Information Domain | Owner | Current Status |
|---|---|---|---|---|
| EOS-001 | Governance Information Architecture | Governance | PM | Verified |
| EOS-002 | Governance File Registration | Governance | PM | Verified |
| EOS-003 | Governance Rule Registration | Governance | PM | Verified |
| EOS-004 | Architecture Decision Registration | Decision | PM | Verified |
| EOS-005 | Handover Content Standard | Handover | PM | Verified |
| EOS-006 | Handover Version Control | Handover | PM | Verified |
| EOS-007 | Handover Lifecycle Control | Handover | PM | Verified |
| EOS-008 | Current AIStudioCore Handover | Handover | PM | Verified |
| EOS-009 | Workspace Registration | Workspace | PM | Verified |
| EOS-010 | Planning Package Governance | Planning | PM | Verified |
| EOS-011 | Work Order Governance | Work Orders | PM | Verified |
| EOS-012 | Evidence Governance | Evidence | PM | Verified |
| EOS-013 | Engineering Knowledge Governance | Engineering Knowledge | Engineering | Verified |
| EOS-014 | Blueprint Governance Reference | Blueprint | PM | Verified |
| EOS-015 | EOS Capability Governance | Governance | PM | Verified |
| EOS-016 | Execution Queue Governance | Work Orders | PM | Verified |

## Capability Definitions

### EOS-001 — Governance Information Architecture

| Field | Definition |
|---|---|
| Capability ID | EOS-001 |
| Capability Name | Governance Information Architecture |
| Purpose | Provide the authoritative classification and relationship model for EOS governance information. |
| Description | Defines information domains, ownership, relationships, information flow, and governance-file mapping. |
| Owner | PM |
| Inputs | Approved governance sources; domain requirements; existing governance files. |
| Outputs | Authoritative Governance Information Architecture. |
| Dependencies | None. |
| Related Governance Documents | `GOVERNANCE_INFORMATION_ARCHITECTURE.md`; `PROJECT_CHARTER.md`; `DEVELOPMENT_CONSTITUTION.md` |
| Verification Method | Confirm all approved domains, owners, relationships, flows, and file mappings are present and non-duplicative. |
| Current Status | Verified |

### EOS-002 — Governance File Registration

| Field | Definition |
|---|---|
| Capability ID | EOS-002 |
| Capability Name | Governance File Registration |
| Purpose | Maintain the unique inventory of governance files and authoritative locations. |
| Description | Registers governance-file identity, location, ownership, lifecycle status, and domain classification. |
| Owner | PM |
| Inputs | Governance files; approved file lifecycle changes; domain classifications. |
| Outputs | Current Governance File Registry. |
| Dependencies | EOS-001 |
| Related Governance Documents | `GOVERNANCE_FILE_REGISTRY.md`; `GOVERNANCE_INFORMATION_ARCHITECTURE.md` |
| Verification Method | Compare the registry against repository governance files and confirm unique, complete mappings. |
| Current Status | Verified |

### EOS-003 — Governance Rule Registration

| Field | Definition |
|---|---|
| Capability ID | EOS-003 |
| Capability Name | Governance Rule Registration |
| Purpose | Maintain the unique formal registry of approved governance rules. |
| Description | Records rule identity, approval, source, effective date, affected documents, decisions, and revision history. |
| Owner | PM |
| Inputs | Owner-approved rules; authoritative sources; rule revisions. |
| Outputs | Traceable Governance Rules Registry and rule index. |
| Dependencies | EOS-001 |
| Related Governance Documents | `GOVERNANCE_RULES_REGISTRY.md`; `GOVERNANCE_INFORMATION_ARCHITECTURE.md` |
| Verification Method | Validate unique Rule IDs, required fields, source traceability, approval, and index-to-record correspondence. |
| Current Status | Verified |

### EOS-004 — Architecture Decision Registration

| Field | Definition |
|---|---|
| Capability ID | EOS-004 |
| Capability Name | Architecture Decision Registration |
| Purpose | Maintain a unique, traceable index of architecture decision records. |
| Description | Registers decision identity, status, owner, evidence, authoritative record, and supersession relationships without making architecture decisions. |
| Owner | PM |
| Inputs | Approved architecture decision records; decision status changes; related evidence. |
| Outputs | Current Architecture Decision Registry. |
| Dependencies | EOS-001; EOS-012 |
| Related Governance Documents | `ARCHITECTURE_DECISION_REGISTRY.md`; `PM/ARCHITECTURE_INDEX.md` |
| Verification Method | Confirm unique decision references, valid status, evidence linkage, and authoritative record location. |
| Current Status | Verified |

### EOS-005 — Handover Content Standard

| Field | Definition |
|---|---|
| Capability ID | EOS-005 |
| Capability Name | Handover Content Standard |
| Purpose | Define the required structure and evidence fields of governed handovers. |
| Description | Establishes the minimum reviewable content contract for handover records. |
| Owner | PM |
| Inputs | Approved continuity requirements; evidence requirements; review requirements. |
| Outputs | Authoritative Handover Standard. |
| Dependencies | EOS-001; EOS-012 |
| Related Governance Documents | `HANDOVER_STANDARD.md`; `GOVERNANCE_INFORMATION_ARCHITECTURE.md` |
| Verification Method | Validate the standard against approved required fields and evidence references. |
| Current Status | Verified |

### EOS-006 — Handover Version Control

| Field | Definition |
|---|---|
| Capability ID | EOS-006 |
| Capability Name | Handover Version Control |
| Purpose | Control identification, succession, and retention of handover versions. |
| Description | Defines how handover versions are distinguished and how the authoritative current version is identified. |
| Owner | PM |
| Inputs | Approved versioning and retention requirements; handover lifecycle events. |
| Outputs | Authoritative Handover Version Policy. |
| Dependencies | EOS-005; EOS-007 |
| Related Governance Documents | `HANDOVER_VERSION_POLICY.md`; `HANDOVER_STANDARD.md`; `HANDOVER_LIFECYCLE.md` |
| Verification Method | Confirm version identifiers, succession, authority, and retention conditions are unambiguous. |
| Current Status | Verified |

### EOS-007 — Handover Lifecycle Control

| Field | Definition |
|---|---|
| Capability ID | EOS-007 |
| Capability Name | Handover Lifecycle Control |
| Purpose | Control governed states, transitions, review gates, and closing conditions for handovers. |
| Description | Defines the permitted lifecycle of a handover record without changing the Operating Cycle. |
| Owner | PM |
| Inputs | Approved handover states; PM review outcomes; closing directives. |
| Outputs | Authoritative Handover Lifecycle. |
| Dependencies | EOS-005; EOS-006 |
| Related Governance Documents | `HANDOVER_LIFECYCLE.md`; `HANDOVER_STANDARD.md`; `HANDOVER_VERSION_POLICY.md` |
| Verification Method | Validate every state and transition against approved entry, exit, review, and closing conditions. |
| Current Status | Verified |

### EOS-008 — Current AIStudioCore Handover

| Field | Definition |
|---|---|
| Capability ID | EOS-008 |
| Capability Name | Current AIStudioCore Handover |
| Purpose | Preserve the unique current governed continuity record for AIStudioCore. |
| Description | Records current governed status and references according to the handover standard, version policy, and lifecycle. |
| Owner | PM |
| Inputs | Governed work status; decisions; evidence references; PM lifecycle directives. |
| Outputs | Current AIStudioCore Handover record. |
| Dependencies | EOS-005; EOS-006; EOS-007; EOS-010; EOS-011; EOS-012 |
| Related Governance Documents | `AISTUDIOCORE_HANDOVER.md`; `HANDOVER_STANDARD.md`; `HANDOVER_VERSION_POLICY.md`; `HANDOVER_LIFECYCLE.md` |
| Verification Method | Confirm one current record exists and complies with the approved handover controls. |
| Current Status | Verified |

### EOS-009 — Workspace Registration

| Field | Definition |
|---|---|
| Capability ID | EOS-009 |
| Capability Name | Workspace Registration |
| Purpose | Maintain the authoritative identity and reference location of governed workspaces. |
| Description | Registers existing workspaces and their governance status without creating or restructuring them. |
| Owner | PM |
| Inputs | Approved workspace registrations; workspace status changes. |
| Outputs | Current Workspace Registry. |
| Dependencies | EOS-001; EOS-002 |
| Related Governance Documents | `WORKSPACE_REGISTRY.md`; `GOVERNANCE_FILE_REGISTRY.md` |
| Verification Method | Compare registered workspaces with approved existing locations and confirm unique identities. |
| Current Status | Verified |

### EOS-010 — Planning Package Governance

| Field | Definition |
|---|---|
| Capability ID | EOS-010 |
| Capability Name | Planning Package Governance |
| Purpose | Govern approved intent, priorities, dependencies, and readiness for executable work. |
| Description | Provides the controlled daily Source of Truth from which PM authorizes GitHub Issues in the Execution Queue. |
| Owner | PM |
| Inputs | Current handover; approved objectives; blueprint references; decisions; evidence; constraints. |
| Outputs | Approved Daily Planning Package and candidates for PM-authorized GitHub Issues. |
| Dependencies | EOS-001; EOS-008; EOS-012; EOS-014 |
| Related Governance Documents | `PLANNING_PACKAGE_GOVERNANCE.md`; `GOVERNANCE_INFORMATION_ARCHITECTURE.md`; `GOVERNANCE_RULES_REGISTRY.md`; `AISTUDIOCORE_HANDOVER.md` |
| Verification Method | Validate required planning inputs, owner approval, priorities, dependencies, and readiness references. |
| Current Status | Verified |

### EOS-011 — Work Order Governance

| Field | Definition |
|---|---|
| Capability ID | EOS-011 |
| Capability Name | Work Order Governance |
| Purpose | Govern bounded work specifications and capability coverage derived from approved planning. |
| Description | Controls work-order identity, capability mapping, objective, scope, evidence, acceptance, repository target, and review state without making the work order an execution source. |
| Owner | PM |
| Inputs | Approved planning package; Capability IDs; current handover; rules; evidence requirements. |
| Outputs | Governed work-order records and review packages mapped to this matrix and their Execution Queue Issues. |
| Dependencies | EOS-003; EOS-010; EOS-012; EOS-015; EOS-016 |
| Related Governance Documents | `WORK_ORDER_GOVERNANCE.md`; `EXECUTION_QUEUE_GOVERNANCE.md`; `GOVERNANCE_INFORMATION_ARCHITECTURE.md`; `GOVERNANCE_RULES_REGISTRY.md`; `EOS_V1_CAPABILITY_MATRIX.md` |
| Verification Method | Confirm every work order is bounded, mapped to at least one Capability ID, and does not substitute for an authorized GitHub Issue as the execution source. |
| Current Status | Verified |

### EOS-012 — Evidence Governance

| Field | Definition |
|---|---|
| Capability ID | EOS-012 |
| Capability Name | Evidence Governance |
| Purpose | Preserve durable, traceable support for governed claims, decisions, reviews, and acceptance. |
| Description | Controls evidence identity, provenance, classification, linkage, and review status. |
| Owner | PM |
| Inputs | Repository records; execution results; review findings; governed artifacts. |
| Outputs | Traceable evidence references and governed evidence status. |
| Dependencies | EOS-001; EOS-003; EOS-016 |
| Related Governance Documents | `EVIDENCE_GOVERNANCE.md`; `GOVERNANCE_INFORMATION_ARCHITECTURE.md`; `GOVERNANCE_RULES_REGISTRY.md`; `PM/GAP_ANALYSIS.md`; `PM/GITHUB_PORTFOLIO_ASSET_INVENTORY.md` |
| Verification Method | Trace each governed claim to durable evidence and confirm provenance and review status. |
| Current Status | Verified |

### EOS-013 — Engineering Knowledge Governance

| Field | Definition |
|---|---|
| Capability ID | EOS-013 |
| Capability Name | Engineering Knowledge Governance |
| Purpose | Govern discovery, classification, provenance, and reuse of durable engineering knowledge. |
| Description | Controls engineering-knowledge references and status without modifying product implementation or approving architecture. |
| Owner | Engineering |
| Inputs | Reviewed specifications; implementation notes; validated findings; decisions; evidence. |
| Outputs | Indexed and traceable engineering-knowledge references. |
| Dependencies | EOS-001; EOS-004; EOS-012 |
| Related Governance Documents | `ENGINEERING_KNOWLEDGE_GOVERNANCE.md`; `EVIDENCE_GOVERNANCE.md`; `GOVERNANCE_INFORMATION_ARCHITECTURE.md`; `GOVERNANCE_RULES_REGISTRY.md`; `PM/PRODUCT_KNOWLEDGE_INDEX.md`; `PM/BRANCH_PRODUCT_KNOWLEDGE_MAP.md` |
| Verification Method | Audit knowledge references for provenance, classification, review status, and duplication. |
| Current Status | Verified |

### EOS-014 — Blueprint Governance Reference

| Field | Definition |
|---|---|
| Capability ID | EOS-014 |
| Capability Name | Blueprint Governance Reference |
| Purpose | Provide authoritative Blueprint references to governance without changing Blueprint content. |
| Description | Identifies approved Blueprint location, authority, and relationship to planning and decisions. |
| Owner | PM |
| Inputs | Approved Blueprint; governed baseline decisions; file registration. |
| Outputs | Traceable authoritative Blueprint reference for planning. |
| Dependencies | EOS-001; EOS-002; EOS-004 |
| Related Governance Documents | `BLUEPRINT_GOVERNANCE_REFERENCE.md`; `GOVERNANCE_INFORMATION_ARCHITECTURE.md`; `GOVERNANCE_FILE_REGISTRY.md`; `PRODUCT/PRODUCT_BLUEPRINT.md` |
| Verification Method | Confirm the reference resolves to the approved Blueprint and no Blueprint content was modified. |
| Current Status | Verified |

### EOS-015 — EOS Capability Governance

| Field | Definition |
|---|---|
| Capability ID | EOS-015 |
| Capability Name | EOS Capability Governance |
| Purpose | Maintain the unique EOS v1.0 capability catalog, dependency map, completion status, and work-order coverage. |
| Description | Provides the authoritative capability list against which subsequent EOS work orders and verification are mapped. |
| Owner | PM |
| Inputs | Owner capability directive; Governance Information Architecture; work-order coverage; verification outcomes. |
| Outputs | Current EOS v1.0 Capability Matrix. |
| Dependencies | EOS-001; EOS-003 |
| Related Governance Documents | `PM_VERIFICATION_FRAMEWORK.md`; `EOS_V1_FINAL_CAPABILITY_AUDIT.md`; `EXECUTION_QUEUE_GOVERNANCE.md`; `PM_GITHUB_ISSUE_BUILDER.md`; `EOS_V1_CAPABILITY_MATRIX.md`; `GOVERNANCE_INFORMATION_ARCHITECTURE.md`; `GOVERNANCE_RULES_REGISTRY.md` |
| Verification Method | Validate unique IDs, complete definitions, acyclic or explicitly controlled dependencies, status validity, and complete work-order coverage. |
| Current Status | Verified |

### EOS-016 — Execution Queue Governance

| Field | Definition |
|---|---|
| Capability ID | EOS-016 |
| Capability Name | Execution Queue Governance |
| Purpose | Govern GitHub Issues as the sole execution source for Codex. |
| Description | Controls admission of approved Planning Package work into the GitHub Issue Execution Queue and preserves the flow from Codex execution to evidence and PM review. |
| Owner | PM |
| Inputs | Approved Planning Package; Capability IDs; bounded scope; repository target; evidence and acceptance requirements. |
| Outputs | PM-authorized GitHub Issue; traceable Codex execution state; links to resulting evidence and PM review. |
| Dependencies | EOS-003; EOS-010; EOS-015 |
| Related Governance Documents | `EXECUTION_QUEUE_GOVERNANCE.md`; `EOS_V1_CAPABILITY_MATRIX.md`; `GOVERNANCE_INFORMATION_ARCHITECTURE.md`; `GOVERNANCE_RULES_REGISTRY.md` |
| Verification Method | Confirm every Codex execution traces to one PM-authorized GitHub Issue and that the Issue links its Planning Package authority, Capability ID, evidence, and PM review state. |
| Current Status | Verified |

## Capability Dependency Map

| Capability | Direct Dependencies |
|---|---|
| EOS-001 | None |
| EOS-002 | EOS-001 |
| EOS-003 | EOS-001 |
| EOS-004 | EOS-001, EOS-012 |
| EOS-005 | EOS-001, EOS-012 |
| EOS-006 | EOS-005, EOS-007 |
| EOS-007 | EOS-005, EOS-006 |
| EOS-008 | EOS-005, EOS-006, EOS-007, EOS-010, EOS-011, EOS-012 |
| EOS-009 | EOS-001, EOS-002 |
| EOS-010 | EOS-001, EOS-008, EOS-012, EOS-014 |
| EOS-011 | EOS-003, EOS-010, EOS-012, EOS-015, EOS-016 |
| EOS-012 | EOS-001, EOS-003, EOS-016 |
| EOS-013 | EOS-001, EOS-004, EOS-012 |
| EOS-014 | EOS-001, EOS-002, EOS-004 |
| EOS-015 | EOS-001, EOS-003 |
| EOS-016 | EOS-003, EOS-010, EOS-015 |

Mutual dependencies among EOS-006/EOS-007 and EOS-008/EOS-010 represent coordinated governance-control sets. They require joint consistency verification and do not authorize scope expansion.

## Capability Completion Matrix

| Capability ID | Not Started | In Progress | Completed | Verified |
|---|:---:|:---:|:---:|:---:|
| EOS-001 |  |  |  | X |
| EOS-002 |  |  |  | X |
| EOS-003 |  |  |  | X |
| EOS-004 |  |  |  | X |
| EOS-005 |  |  |  | X |
| EOS-006 |  |  |  | X |
| EOS-007 |  |  |  | X |
| EOS-008 |  |  |  | X |
| EOS-009 |  |  |  | X |
| EOS-010 |  |  |  | X |
| EOS-011 |  |  |  | X |
| EOS-012 |  |  |  | X |
| EOS-013 |  |  |  | X |
| EOS-014 |  |  |  | X |
| EOS-015 |  |  |  | X |
| EOS-016 |  |  |  | X |

## Coverage Mapping

| Work Order | Capability Coverage | Evidence | Work Order State |
|---|---|---|---|
| WO-AISTUDIOCORE-001 | EOS-002, EOS-004, EOS-005, EOS-006, EOS-007, EOS-008, EOS-009 | Eight governance skeletons under `governance/` | Completed — Pending Daily Closing |
| WO-AISTUDIOCORE-002 | EOS-001 | `GOVERNANCE_INFORMATION_ARCHITECTURE.md` and domain alignment updates | Completed — Pending Daily Closing |
| WO-AISTUDIOCORE-003 | EOS-003 | Formal index and nine approved rule registrations in `GOVERNANCE_RULES_REGISTRY.md` | Completed — Pending Daily Closing |
| WO-AISTUDIOCORE-004 | EOS-015, EOS-016 | `EOS_V1_CAPABILITY_MATRIX.md`, approved R1 execution-source revision, and Owner certification record | Verified — Certification Persisted |
| GitHub Issue #32 | EOS-016 | `EXECUTION_QUEUE_GOVERNANCE.md` and aligned governance documents | READY_FOR_PM_REVIEW |
| GitHub Issue #33 | EOS-016 | `PM_GITHUB_ISSUE_BUILDER.md`, implementation, tests, and Queue demonstration | READY_FOR_PM_REVIEW |
| GitHub Issue #36 | EOS-002, EOS-015 | Governance asset registry, GIA mapping, and GitHub repository persistence | READY_FOR_PM_REVIEW |
| GitHub Issue #37 | EOS-004 | Qualified historical ADR index with explicit provenance and unresolved gaps | READY_FOR_PM_REVIEW |
| GitHub Issue #38 | EOS-005, EOS-006, EOS-007, EOS-008 | Completed handover contract, version policy, lifecycle, and current working record | READY_FOR_PM_REVIEW |
| GitHub Issue #39 | EOS-010 | Formal Planning Package authority, contract, validation gate, and daily success criteria | READY_FOR_PM_REVIEW |
| GitHub Issue #40 | EOS-011 | Formal Work Order contract, Capability and GitHub Issue traceability, and closing boundaries | READY_FOR_PM_REVIEW |
| GitHub Issue #41 | EOS-012 | Formal evidence schema, provenance, validation, review status, and retention controls | READY_FOR_PM_REVIEW |
| GitHub Issue #42 | EOS-013 | Engineering knowledge classification, precedence, existing-asset map, gaps, and reuse controls | READY_FOR_PM_REVIEW |
| GitHub Issue #43 | EOS-014 | Blueprint identity, immutable integrity evidence, authority classification, and explicit approval gap | READY_FOR_PM_REVIEW |
| GitHub Issue #44 | EOS-015 | Sixteen-capability audit, dependency and governance-flow verification, risks, and PM Review recommendation | READY_FOR_PM_REVIEW |
| GitHub Issue #46 | EOS-009 | Verified governed workspace identity, repository relationship, owner, status, and local evidence reference | READY_FOR_PM_REVIEW |
| GitHub Issue #47 | EOS-015 | PM verification inputs, checks, results, authority boundary, records, and sixteen-capability coverage | READY_FOR_PM_REVIEW |
| GitHub Issue #48 | EOS-008, EOS-015 | Deterministic evidence-gated PM Closing Package Builder, contract, and automated tests | READY_FOR_PM_REVIEW |
| GitHub Issue #49 | EOS-003, EOS-015 | GVR-010 registration and evidence-to-improvement review, carry-over, and closure controls | READY_FOR_PM_REVIEW |
| GitHub Issue #50 | EOS-010, EOS-015 | Current R2 registry, EOS-017 input, published Queue evidence, integrity, and closing-baseline traceability | READY_FOR_PM_REVIEW |
| GitHub Issue #51 | EOS-001–EOS-016 | Final certification audit, 16/16 PM Verification Records, approved dependency disposition, and Owner certification decision | CERTIFIED — OWNER APPROVED |

Coverage indicates which work order established or advances a capability. It does not replace capability verification or daily closing.

## Related Governance Documents

- [Governance Information Architecture](GOVERNANCE_INFORMATION_ARCHITECTURE.md)
- [Governance Rules Registry](GOVERNANCE_RULES_REGISTRY.md)
- [Governance File Registry](GOVERNANCE_FILE_REGISTRY.md)
- [AIStudioCore Handover](AISTUDIOCORE_HANDOVER.md)
- [Execution Queue Governance](EXECUTION_QUEUE_GOVERNANCE.md)
- [Blueprint Governance Reference](BLUEPRINT_GOVERNANCE_REFERENCE.md)
- [EOS v1.0 Final Capability Audit](EOS_V1_FINAL_CAPABILITY_AUDIT.md)

## Status

EOS-001 through EOS-016 are Verified under `EOS_V1_CERTIFICATION_RECORD_2026-08-07.md`. Engineering Operating System v1.0 is Owner-approved and Certified; Daily Governed Closing remains a separate lifecycle action.
