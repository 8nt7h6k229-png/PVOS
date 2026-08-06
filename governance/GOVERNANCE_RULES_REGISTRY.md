# Governance Rules Registry

## Purpose

Register approved governance rules and their authoritative sources.

## Responsibility

Maintain the unique index of governance rules.

## Information Domain

Governance

## Owner

PM

## Update Trigger

A governance rule is proposed, approved, changed, superseded, or retired.

## Registry Schema

Every registered rule contains:

- Rule ID
- Rule Name
- Status
- Purpose
- Description
- Source
- Approved By
- Effective Date
- Affected Documents
- Related Decisions
- Revision History

## Governance Rules Index

| Rule ID | Rule Name | Status | Effective Date |
|---|---|---|---|
| GVR-001 | Daily Closing Policy | APPROVED | 2026-08-06 |
| GVR-002 | PM Execution Directive | APPROVED | 2026-08-06 |
| GVR-003 | Planning Package Commitment Policy | APPROVED | 2026-08-06 |
| GVR-004 | PM Context Source Policy | APPROVED | 2026-08-06 |
| GVR-005 | Existing Assets First | APPROVED | 2026-08-06 |
| GVR-006 | Engineering Knowledge First | APPROVED | 2026-08-06 |
| GVR-007 | Evidence First | APPROVED | 2026-08-06 |
| GVR-008 | No Scope Expansion | APPROVED | 2026-08-06 |
| GVR-009 | One Closed Loop at a Time | APPROVED | 2026-08-06 |

## Registered Rules

### GVR-001 — Daily Closing Policy

| Field | Registration |
|---|---|
| Rule ID | GVR-001 |
| Rule Name | Daily Closing Policy |
| Status | APPROVED |
| Purpose | Keep work-order review distinct from governed daily closing. |
| Description | Individual work orders remain pending daily closing until PM explicitly closes the Daily Planning Package. Executors must not close individual work orders or the daily package. |
| Source | 2026-08-06 Daily Planning Package; CODEX EXECUTION BASIS — 2026-08-06; WO-AISTUDIOCORE-003 |
| Approved By | Owner |
| Effective Date | 2026-08-06 |
| Affected Documents | `AISTUDIOCORE_HANDOVER.md`; `HANDOVER_LIFECYCLE.md`; `GOVERNANCE_RULES_REGISTRY.md` |
| Related Decisions | None registered. |
| Revision History | 2026-08-06 — Initial approved registration. |

### GVR-002 — PM Execution Directive

| Field | Registration |
|---|---|
| Rule ID | GVR-002 |
| Rule Name | PM Execution Directive |
| Status | APPROVED |
| Purpose | Preserve PM authority over governed execution instructions. |
| Description | Executors act only from a PM-authorized GitHub Issue in the Execution Queue, within its bounded governance context, and return the required review state without self-approval or closing. |
| Source | CODEX EXECUTION BASIS — 2026-08-06; Owner Approved Governance Pilot Run SOP; WO-AISTUDIOCORE-003; GitHub Issue #32 |
| Approved By | Owner |
| Effective Date | 2026-08-06 |
| Affected Documents | `GOVERNANCE_RULES_REGISTRY.md`; `AISTUDIOCORE_HANDOVER.md`; `EXECUTION_QUEUE_GOVERNANCE.md` |
| Related Decisions | None registered. |
| Revision History | 2026-08-06 — Initial approved registration; aligned to GitHub Issue as sole Execution Source by Issue #32. |

### GVR-003 — Planning Package Commitment Policy

| Field | Registration |
|---|---|
| Rule ID | GVR-003 |
| Rule Name | Planning Package Commitment Policy |
| Status | APPROVED |
| Purpose | Establish the approved Daily Planning Package as the governing commitment for the day's work. |
| Description | The approved Planning Package remains the daily Source of Truth; executable items enter Codex only through PM-authorized GitHub Issues in the Execution Queue. |
| Source | 2026-08-06 Daily Planning Package; CODEX EXECUTION BASIS — 2026-08-06; WO-AISTUDIOCORE-003; GitHub Issue #32 |
| Approved By | Owner |
| Effective Date | 2026-08-06 |
| Affected Documents | `GOVERNANCE_INFORMATION_ARCHITECTURE.md`; `AISTUDIOCORE_HANDOVER.md`; `GOVERNANCE_RULES_REGISTRY.md`; `EXECUTION_QUEUE_GOVERNANCE.md` |
| Related Decisions | None registered. |
| Revision History | 2026-08-06 — Initial approved registration; execution admission aligned to Issue #32. |

### GVR-004 — PM Context Source Policy

| Field | Registration |
|---|---|
| Rule ID | GVR-004 |
| Rule Name | PM Context Source Policy |
| Status | APPROVED |
| Purpose | Keep execution context traceable to PM-designated governance sources. |
| Description | Executors use the approved Planning Package as daily Source of Truth and the current PM-authorized GitHub Issue as sole Execution Source; referenced governed assets provide context, while unstated context is not authoritative. |
| Source | CODEX EXECUTION BASIS — 2026-08-06; Owner Approved Governance Pilot Run SOP; WO-AISTUDIOCORE-003; GitHub Issue #32 |
| Approved By | Owner |
| Effective Date | 2026-08-06 |
| Affected Documents | `AISTUDIOCORE_HANDOVER.md`; `GOVERNANCE_FILE_REGISTRY.md`; `GOVERNANCE_RULES_REGISTRY.md`; `EXECUTION_QUEUE_GOVERNANCE.md` |
| Related Decisions | None registered. |
| Revision History | 2026-08-06 — Initial approved registration; context and execution-source boundary aligned to Issue #32. |

### GVR-005 — Existing Assets First

| Field | Registration |
|---|---|
| Rule ID | GVR-005 |
| Rule Name | Existing Assets First |
| Status | APPROVED |
| Purpose | Prevent duplicate governed assets and preserve existing authoritative work. |
| Description | Inspect existing repository assets before creation; extend an existing same-purpose asset when present and create only when absent. |
| Source | WO-AISTUDIOCORE-001; WO-AISTUDIOCORE-002; WO-AISTUDIOCORE-003; Owner Approved Governance Pilot Run SOP |
| Approved By | Owner |
| Effective Date | 2026-08-06 |
| Affected Documents | `GOVERNANCE_FILE_REGISTRY.md`; `GOVERNANCE_RULES_REGISTRY.md`; `GOVERNANCE_INFORMATION_ARCHITECTURE.md` |
| Related Decisions | None registered. |
| Revision History | 2026-08-06 — Initial approved registration. |

### GVR-006 — Engineering Knowledge First

| Field | Registration |
|---|---|
| Rule ID | GVR-006 |
| Rule Name | Engineering Knowledge First |
| Status | APPROVED |
| Purpose | Preserve and reuse governed engineering knowledge before producing equivalent knowledge. |
| Description | Inspect relevant existing engineering knowledge and its provenance before creating or changing an equivalent engineering-knowledge asset. |
| Source | Owner Approved Governance Pilot Run SOP; WO-AISTUDIOCORE-003 |
| Approved By | Owner |
| Effective Date | 2026-08-06 |
| Affected Documents | `GOVERNANCE_INFORMATION_ARCHITECTURE.md`; `GOVERNANCE_RULES_REGISTRY.md` |
| Related Decisions | None registered. |
| Revision History | 2026-08-06 — Initial approved registration. |

### GVR-007 — Evidence First

| Field | Registration |
|---|---|
| Rule ID | GVR-007 |
| Rule Name | Evidence First |
| Status | APPROVED |
| Purpose | Keep governed claims, decisions, and review outcomes evidence-based. |
| Description | Use approved, durable evidence before assumption; record missing evidence as uncertainty or a gap rather than replacing it with inference. |
| Source | `PROJECT_CHARTER.md` §7; `DEVELOPMENT_CONSTITUTION.md` §2; Owner Approved Governance Pilot Run SOP; WO-AISTUDIOCORE-003 |
| Approved By | Owner |
| Effective Date | 2026-08-06 |
| Affected Documents | `GOVERNANCE_INFORMATION_ARCHITECTURE.md`; `GOVERNANCE_RULES_REGISTRY.md`; `AISTUDIOCORE_HANDOVER.md` |
| Related Decisions | None registered. |
| Revision History | 2026-08-06 — Initial approved registration. |

### GVR-008 — No Scope Expansion

| Field | Registration |
|---|---|
| Rule ID | GVR-008 |
| Rule Name | No Scope Expansion |
| Status | APPROVED |
| Purpose | Keep execution within its approved authorization boundary. |
| Description | Executors must not add objectives, deliverables, rules, architecture, product content, or repository changes outside the issued work order. |
| Source | WO-AISTUDIOCORE-001; WO-AISTUDIOCORE-002; CODEX EXECUTION BASIS — 2026-08-06; WO-AISTUDIOCORE-003 |
| Approved By | Owner |
| Effective Date | 2026-08-06 |
| Affected Documents | `GOVERNANCE_RULES_REGISTRY.md`; `AISTUDIOCORE_HANDOVER.md` |
| Related Decisions | None registered. |
| Revision History | 2026-08-06 — Initial approved registration. |

### GVR-009 — One Closed Loop at a Time

| Field | Registration |
|---|---|
| Rule ID | GVR-009 |
| Rule Name | One Closed Loop at a Time |
| Status | APPROVED |
| Purpose | Keep execution within one PM-authorized governance loop at a time. |
| Description | Executors advance the currently authorized governance loop and do not initiate a separate loop without PM authorization. Multiple work orders may remain governed by the same Daily Planning Package. |
| Source | Owner Approved Governance Pilot Run SOP; 2026-08-06 Daily Planning Package; WO-AISTUDIOCORE-003 |
| Approved By | Owner |
| Effective Date | 2026-08-06 |
| Affected Documents | `HANDOVER_LIFECYCLE.md`; `AISTUDIOCORE_HANDOVER.md`; `GOVERNANCE_RULES_REGISTRY.md` |
| Related Decisions | None registered. |
| Revision History | 2026-08-06 — Initial approved registration. |

## Related Documents

- [Governance File Registry](GOVERNANCE_FILE_REGISTRY.md)
- [Governance Information Architecture](GOVERNANCE_INFORMATION_ARCHITECTURE.md)
- [Architecture Decision Registry](ARCHITECTURE_DECISION_REGISTRY.md)

## Status

Formal registry foundation — awaiting PM review and daily closing.
