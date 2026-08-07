# Governance Information Architecture

## Purpose

Define the classification, ownership, relationships, and flow of AIStudioCore governance information.

## Responsibility

Maintain the unique authoritative map of governance information domains.

## Owner

PM

## Update Trigger

An information domain, domain boundary, ownership assignment, relationship, or governance-file classification changes.

## Information Domains

### Governance

- **Purpose:** Establish the authority, classification, and control framework for governed information.
- **Scope:** Governance rules, governance-file registration, domain classification, and authoritative governance references.
- **Owner:** PM
- **Inputs:** Approved governance authority, governed changes, and review outcomes.
- **Outputs:** Governance rules, file registrations, classifications, and control references.
- **Related Documents:** [Project Charter](../PROJECT_CHARTER.md); [Development Constitution](../DEVELOPMENT_CONSTITUTION.md); [Governance File Registry](GOVERNANCE_FILE_REGISTRY.md); [Governance Rules Registry](GOVERNANCE_RULES_REGISTRY.md).
- **Out of Scope:** Product requirements, architecture design, implementation, and workspace restructuring.

### Handover

- **Purpose:** Preserve governed continuity between work periods, owners, and execution contexts.
- **Scope:** Handover structure, versioning, lifecycle, and current handover records.
- **Owner:** PM
- **Inputs:** Governed status, decisions, evidence references, open work, and approved transitions.
- **Outputs:** Reviewable handover records with lifecycle and version status.
- **Related Documents:** [Handover Standard](HANDOVER_STANDARD.md); [Handover Version Policy](HANDOVER_VERSION_POLICY.md); [Handover Lifecycle](HANDOVER_LIFECYCLE.md); [AIStudioCore Handover](AISTUDIOCORE_HANDOVER.md).
- **Out of Scope:** Approval of source information and creation of product content.

### Planning

- **Purpose:** Organize approved intent into governed, reviewable future work.
- **Scope:** Planning packages, priorities, dependencies, sequencing, and readiness references.
- **Owner:** PM
- **Inputs:** Approved objectives, current handover, blueprint references, decisions, evidence, and constraints.
- **Outputs:** Approved planning packages and authorized work candidates.
- **Related Documents:** [Planning Package Governance](PLANNING_PACKAGE_GOVERNANCE.md); [AIStudioCore Handover](AISTUDIOCORE_HANDOVER.md); [Product Backlog](../PRODUCT/PRODUCT_BACKLOG.md); [Product Release Plan](../PRODUCT/PRODUCT_RELEASE_PLAN.md).
- **Out of Scope:** Work execution, product-baseline modification, and completion declarations.

### Blueprint

- **Purpose:** Identify the authoritative high-level product intent and capability structure used by governance.
- **Scope:** Approved blueprint references and their governance classification.
- **Owner:** PM
- **Inputs:** Approved product intent and governed baseline decisions.
- **Outputs:** Authoritative blueprint references for planning and work authorization.
- **Related Documents:** [Blueprint Governance Reference](BLUEPRINT_GOVERNANCE_REFERENCE.md); [Product Blueprint](../PRODUCT/PRODUCT_BLUEPRINT.md); [Governance File Registry](GOVERNANCE_FILE_REGISTRY.md); [Architecture Decision Registry](ARCHITECTURE_DECISION_REGISTRY.md).
- **Out of Scope:** Blueprint modification, implementation design, and unapproved capability expansion.

### Work Orders

- **Purpose:** Govern bounded work specifications and the GitHub Issue Execution Queue derived from approved planning.
- **Scope:** Work-order governance records plus GitHub Issue objective, Capability ID, repository target, scope boundaries, deliverables, evidence, acceptance, and review status.
- **Owner:** PM
- **Inputs:** Approved planning package, current handover, governance rules, decisions, and evidence requirements.
- **Outputs:** PM-authorized GitHub Issues as the sole Codex Execution Source, governed work-order records, and executor review packages.
- **Related Documents:** [Work Order Governance](WORK_ORDER_GOVERNANCE.md); [Execution Queue Governance](EXECUTION_QUEUE_GOVERNANCE.md); [PM GitHub Issue Builder](PM_GITHUB_ISSUE_BUILDER.md); [Governance Rules Registry](GOVERNANCE_RULES_REGISTRY.md); [AIStudioCore Handover](AISTUDIOCORE_HANDOVER.md).
- **Out of Scope:** Self-approval, scope expansion, and governed closing by the executor.

### Decision

- **Purpose:** Preserve traceable decisions and their authoritative records.
- **Scope:** Decision identity, owner, status, evidence reference, and supersession relationship.
- **Owner:** PM
- **Inputs:** Decision proposals, alternatives, evidence, and accountable review outcomes.
- **Outputs:** Classified decision records and an authoritative decision index.
- **Related Documents:** [Architecture Decision Registry](ARCHITECTURE_DECISION_REGISTRY.md); [Architecture Index](../PM/ARCHITECTURE_INDEX.md).
- **Out of Scope:** Creating architecture decisions or changing approved architecture in this information architecture.

### Evidence

- **Purpose:** Identify durable support for claims, reviews, decisions, and acceptance.
- **Scope:** Evidence references, provenance, classification, and linkage to governed records.
- **Owner:** PM
- **Inputs:** Repository records, execution results, review findings, and governed artifacts.
- **Outputs:** Traceable evidence references for decision, acceptance, and handover.
- **Related Documents:** [Evidence Governance](EVIDENCE_GOVERNANCE.md); [Gap Analysis](../PM/GAP_ANALYSIS.md); [GitHub Portfolio Asset Inventory](../PM/GITHUB_PORTFOLIO_ASSET_INVENTORY.md); [Governance Rules Registry](GOVERNANCE_RULES_REGISTRY.md).
- **Out of Scope:** Fabricating evidence, replacing accountable review, and modifying product behavior.

### Engineering Knowledge

- **Purpose:** Classify durable engineering knowledge for governed discovery and reuse.
- **Scope:** Engineering knowledge references, provenance, status, and relationships to decisions and evidence.
- **Owner:** Engineering
- **Inputs:** Reviewed specifications, implementation notes, validated findings, decisions, and evidence.
- **Outputs:** Indexed, traceable engineering knowledge references.
- **Related Documents:** [Engineering Knowledge Governance](ENGINEERING_KNOWLEDGE_GOVERNANCE.md); [Product Knowledge Index](../PM/PRODUCT_KNOWLEDGE_INDEX.md); [Branch Product Knowledge Map](../PM/BRANCH_PRODUCT_KNOWLEDGE_MAP.md); [Engineering](../ENGINEERING/).
- **Out of Scope:** Product implementation, unreviewed assumptions as truth, and architecture approval.

### Workspace

- **Purpose:** Identify governed workspaces without changing their structure.
- **Scope:** Workspace identity, authority, status, and reference location.
- **Owner:** PM
- **Inputs:** Approved workspace registrations and governed workspace status changes.
- **Outputs:** Authoritative workspace inventory references.
- **Related Documents:** [Workspace Registry](WORKSPACE_REGISTRY.md); [Governance File Registry](GOVERNANCE_FILE_REGISTRY.md).
- **Out of Scope:** Creating repositories, restructuring workspaces, and defining product functionality.

## Domain Relationships

| Source Domain | Relationship | Target Domain |
|---|---|---|
| Governance | constrains and classifies | All domains |
| Handover | carries current governed state into | Planning |
| Blueprint | provides approved intent to | Planning |
| Planning | supplies the daily Source of Truth to | Work Orders |
| Work Orders | admits execution only through a PM-authorized GitHub Issue and produces | Evidence |
| Evidence | supports | Decision |
| Decision | governs changes affecting | Blueprint, Planning, and Engineering Knowledge |
| Engineering Knowledge | informs, without approving | Planning and Decision |
| Workspace | locates authoritative records for | All domains |
| All domains | return governed state to | Handover |

## Ownership Matrix

| Information Domain | Accountable Owner | Primary Responsibility |
|---|---|---|
| Governance | PM | Governance authority and classification |
| Handover | PM | Governed continuity record |
| Planning | PM | Approved intent and sequencing |
| Blueprint | PM | Authoritative blueprint classification |
| Work Orders | PM | Bounded execution authorization |
| Decision | PM | Accountable decision record |
| Evidence | PM | Evidence acceptance and governance linkage |
| Engineering Knowledge | Engineering | Durable engineering knowledge stewardship |
| Workspace | PM | Governed workspace inventory |

Execution is authorized only through a PM-authorized GitHub Issue; authorization does not transfer accountable ownership.

## Information Flow

1. Governance classifies the authoritative rules, files, owners, and information boundaries.
2. Handover supplies current governed state; Blueprint supplies approved intent; Engineering Knowledge and Evidence supply traceable context.
3. Planning converts those governed inputs into an approved Planning Package, the daily Source of Truth.
4. PM admits executable Planning Package work to the GitHub Issue Execution Queue; the authorized Issue is Codex's sole Execution Source.
5. Codex executes the bounded Issue and returns evidence and engineering knowledge references.
6. PM reviews the evidence; Decisions record approved outcomes and govern any resulting authoritative change.
7. Handover records the resulting governed state for the next cycle.
8. Workspace references locate the authoritative records throughout the flow.

## Governance File Mapping

| Governance File | Primary Domain |
|---|---|
| `GOVERNANCE_INFORMATION_ARCHITECTURE.md` | Governance |
| `EOS_V1_CAPABILITY_MATRIX.md` | Governance |
| `EXECUTION_QUEUE_GOVERNANCE.md` | Work Orders |
| `PM_GITHUB_ISSUE_BUILDER.md` | Work Orders |
| `PLANNING_PACKAGE_GOVERNANCE.md` | Planning |
| `WORK_ORDER_GOVERNANCE.md` | Work Orders |
| `EVIDENCE_GOVERNANCE.md` | Evidence |
| `ENGINEERING_KNOWLEDGE_GOVERNANCE.md` | Engineering Knowledge |
| `BLUEPRINT_GOVERNANCE_REFERENCE.md` | Blueprint |
| `EOS_V1_FINAL_CAPABILITY_AUDIT.md` | Governance |
| `PM_VERIFICATION_FRAMEWORK.md` | Governance |
| `PM_CLOSING_BUILDER.md` | Handover |
| `closing_builder/pm_closing_builder.py` | Handover |
| `closing_builder/tests/test_pm_closing_builder.py` | Evidence |
| `closing_builder/.gitignore` | Governance |
| `GOVERNANCE_FILE_REGISTRY.md` | Governance |
| `GOVERNANCE_RULES_REGISTRY.md` | Governance |
| `ARCHITECTURE_DECISION_REGISTRY.md` | Decision |
| `HANDOVER_STANDARD.md` | Handover |
| `HANDOVER_VERSION_POLICY.md` | Handover |
| `HANDOVER_LIFECYCLE.md` | Handover |
| `AISTUDIOCORE_HANDOVER.md` | Handover |
| `WORKSPACE_REGISTRY.md` | Workspace |
| `issue_builder/pm_issue_builder.py` | Work Orders |
| `issue_builder/tests/test_pm_issue_builder.py` | Evidence |
| `issue_builder/.gitignore` | Governance |
| `issue_builder/examples/demo_daily_planning_package.json` | Planning |
| `issue_builder/examples/demo_queue_ready.json` | Evidence |
| `issue_builder/packages/2026-08-06_daily_planning_package.json` | Planning |
| `issue_builder/packages/2026-08-06_issue_queue_ready.json` | Evidence |

Each governance file has one primary domain. Cross-domain links do not transfer its primary responsibility.

## Governance Principles

This architecture adds no governance principles. It applies and references the approved principles in:

- [Project Charter - Governance Principles](../PROJECT_CHARTER.md#7-governance-principles)
- [Development Constitution - Governance Philosophy](../DEVELOPMENT_CONSTITUTION.md#2-governance-philosophy)

If a conflict is identified, the approved source document remains authoritative.

## Related Documents

- [Governance File Registry](GOVERNANCE_FILE_REGISTRY.md)
- [Governance Rules Registry](GOVERNANCE_RULES_REGISTRY.md)
- [Project Charter](../PROJECT_CHARTER.md)
- [Development Constitution](../DEVELOPMENT_CONSTITUTION.md)

## Status

Draft governance information architecture - awaiting PM review.
