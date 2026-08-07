# Governance File Registry

## Purpose

Register governance files and their authoritative locations.

## Responsibility

Maintain the unique inventory of governance files.

## Information Domain

Governance

## Owner

PM

## Update Trigger

A governance file is added, moved, renamed, superseded, or retired.

## Registry Schema

| Field | Meaning |
|---|---|
| File ID | Unique governance-asset identifier |
| Repository Path | Authoritative path relative to repository root |
| Primary Domain | GIA domain owning the asset's primary responsibility |
| Responsibility | Unique purpose served by the asset |
| Status | Current governed lifecycle state |
| Authority | Work item or governance source establishing the asset |

## Registered Governance Assets

| File ID | Repository Path | Primary Domain | Responsibility | Status | Authority |
|---|---|---|---|---|---|
| GF-001 | `governance/GOVERNANCE_INFORMATION_ARCHITECTURE.md` | Governance | Authoritative information-domain map | Review Pending | WO-AISTUDIOCORE-002 |
| GF-002 | `governance/GOVERNANCE_RULES_REGISTRY.md` | Governance | Approved governance-rule index | Review Pending | WO-AISTUDIOCORE-003; Issue #32 |
| GF-003 | `governance/GOVERNANCE_FILE_REGISTRY.md` | Governance | Governance-asset location inventory | Review Pending | Issue #36 |
| GF-004 | `governance/ARCHITECTURE_DECISION_REGISTRY.md` | Decision | Architecture-decision record index | Review Pending | WO-AISTUDIOCORE-001 |
| GF-005 | `governance/HANDOVER_STANDARD.md` | Handover | Handover content and evidence contract | Review Pending | WO-AISTUDIOCORE-001 |
| GF-006 | `governance/HANDOVER_VERSION_POLICY.md` | Handover | Handover version-control policy | Review Pending | WO-AISTUDIOCORE-001 |
| GF-007 | `governance/HANDOVER_LIFECYCLE.md` | Handover | Handover state and transition control | Review Pending | WO-AISTUDIOCORE-001 |
| GF-008 | `governance/AISTUDIOCORE_HANDOVER.md` | Handover | Current AIStudioCore handover record | Review Pending | WO-AISTUDIOCORE-001 |
| GF-009 | `governance/WORKSPACE_REGISTRY.md` | Workspace | Governed workspace inventory | Review Pending | WO-AISTUDIOCORE-001 |
| GF-010 | `governance/EOS_V1_CAPABILITY_MATRIX.md` | Governance | EOS v1.0 capability source of truth | Review Pending | WO-AISTUDIOCORE-004 |
| GF-011 | `governance/EXECUTION_QUEUE_GOVERNANCE.md` | Work Orders | GitHub Issue execution-source control | Review Pending | Issue #32 |
| GF-012 | `governance/PM_GITHUB_ISSUE_BUILDER.md` | Work Orders | Planning-to-Issue publication contract | Review Pending | Issue #33 |
| GF-013 | `governance/issue_builder/pm_issue_builder.py` | Work Orders | Validated Issue Queue builder implementation | Review Pending | Issue #33 |
| GF-014 | `governance/issue_builder/tests/test_pm_issue_builder.py` | Evidence | Builder verification suite | Review Pending | Issue #33 |
| GF-015 | `governance/issue_builder/.gitignore` | Governance | Exclusion of generated Python cache artifacts | Active Support | Issue #33 |
| GF-016 | `governance/issue_builder/examples/demo_daily_planning_package.json` | Planning | Builder demonstration input | Demonstration | Issue #33 |
| GF-017 | `governance/issue_builder/examples/demo_queue_ready.json` | Evidence | Builder demonstration Queue Ready evidence | Demonstration | Issue #33 |
| GF-018 | `governance/issue_builder/packages/2026-08-06_daily_planning_package.json` | Planning | Approved daily Planning Package input | Active | 2026-08-06 Daily Planning Package |
| GF-019 | `governance/issue_builder/packages/2026-08-06_issue_queue_ready.json` | Evidence | Published daily Queue Ready evidence | Active | Issues #36-#44 |
| GF-020 | `governance/PLANNING_PACKAGE_GOVERNANCE.md` | Planning | Daily planning authority and publication contract | Review Pending | Issue #39 |
| GF-021 | `governance/WORK_ORDER_GOVERNANCE.md` | Work Orders | Work Order content, traceability, review, and closing contract | Review Pending | Issue #40 |
| GF-022 | `governance/EVIDENCE_GOVERNANCE.md` | Evidence | Evidence identity, provenance, validation, review, and retention contract | Review Pending | Issue #41 |
| GF-023 | `governance/ENGINEERING_KNOWLEDGE_GOVERNANCE.md` | Engineering Knowledge | Engineering knowledge identity, classification, provenance, review, and reuse contract | Review Pending | Issue #42 |
| GF-024 | `governance/BLUEPRINT_GOVERNANCE_REFERENCE.md` | Blueprint | Blueprint identity, integrity, authority classification, and governance relationship reference | Review Pending | Issue #43 |
| GF-025 | `governance/EOS_V1_FINAL_CAPABILITY_AUDIT.md` | Governance | Final evidence-based EOS v1.0 capability, dependency, coverage, and readiness audit | Review Pending | Issue #44 |
| GF-026 | `governance/PM_VERIFICATION_FRAMEWORK.md` | Governance | Evidence-based PM capability verification checks, records, results, and authority boundary | Review Pending | Issue #47 |

Repository paths are unique. Generated cache files excluded by GF-015 are not governance assets and must not be persisted.

## Related Documents

- [Governance Rules Registry](GOVERNANCE_RULES_REGISTRY.md)
- [Governance Information Architecture](GOVERNANCE_INFORMATION_ARCHITECTURE.md)
- [Workspace Registry](WORKSPACE_REGISTRY.md)

## Status

Formal registry foundation established — awaiting PM review.
