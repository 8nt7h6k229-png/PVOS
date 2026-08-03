# PVOS Development Constitution

Status: Proposed for PM approval

Authority: PVOS Engineering Governance

Evidence baseline: PM-001, PM-002, PM-003, and PM-004

This Constitution defines how PVOS engineering work is governed and executed. It records the practices demonstrated while establishing the approved governance baseline; it does not create product scope, architecture, implementation policy, a roadmap, or sprint planning.

The [PVOS Project Charter](PROJECT_CHARTER.md) remains the highest-level governance reference. This Constitution is subordinate to the Charter and applies its values to engineering process.

## 1. Purpose

The purpose of this Constitution is to ensure that PVOS engineering work:

- begins from an explicit product or governance need;
- uses approved evidence rather than assumption;
- preserves knowledge before authorizing creation or replacement;
- moves through a visible Issue, branch, commit, Pull Request, review, merge, and closure record;
- respects phase gates and approved product boundaries;
- keeps AI assistance reviewable and subordinate to accountable human decisions; and
- reaches a verifiable completion state rather than stopping at implementation.

These duties implement the Charter's requirements for traceable decisions, explicit scope changes, visible exceptions, and no silent completion. Evidence: [Project Charter §§6–8](PROJECT_CHARTER.md), [Product Baseline — Product Complete definition](PM/PRODUCT_BASELINE.md), and [Gap Analysis](PM/GAP_ANALYSIS.md).

## 2. Governance Philosophy

PVOS engineering is governed by the following principles and no additional constitutional principles are established here.

| Principle | Constitutional meaning | Approved evidence |
|---|---|---|
| **Product First** | Work is justified by the approved product purpose, scope, baseline, or an explicit governance need. Repository activity alone does not define product value. | [Project Charter §§3–5](PROJECT_CHARTER.md); [Product Scope](PM/PRODUCT_SCOPE.md) |
| **Evidence Before Assumption** | Claims, decisions, completion, and exceptions cite durable evidence. Missing evidence is recorded as uncertainty or a gap, not replaced by inference. | [Project Charter §§6–7](PROJECT_CHARTER.md); [Portfolio inventory rules](PM/GITHUB_PORTFOLIO_ASSET_INVENTORY.md) |
| **GitHub is the Single Source of Truth** | The governed record is the repository history and its Issues, branches, commits, Pull Requests, reviews, merged documents, and closure state. Conversations and tool-local state are not authoritative by themselves. | [Project Charter §§2 and 7](PROJECT_CHARTER.md); [Product Baseline — Evidence precedence](PM/PRODUCT_BASELINE.md) |
| **Inventory Before Creation** | Existing repositories, branches, Issues, Pull Requests, documents, and product knowledge are identified before new work is authorized. | [GitHub Portfolio Asset Inventory](PM/GITHUB_PORTFOLIO_ASSET_INVENTORY.md); [Gap Analysis](PM/GAP_ANALYSIS.md) |
| **Recover Before Rebuild** | Existing knowledge is classified and evaluated before equivalent knowledge is recreated. Recovery preserves provenance and does not silently promote historical work into the baseline. | [Branch Product Knowledge Map](PM/BRANCH_PRODUCT_KNOWLEDGE_MAP.md); [Branch Recovery Index](PM/BRANCH_RECOVERY_INDEX.md); [Project Charter §10](PROJECT_CHARTER.md) |
| **Finish Before Optimize** | Authorized work first satisfies its approved acceptance and closure conditions. Optimization or expansion does not substitute for completing the governed work item. | [Project Charter §§6–7 and 9](PROJECT_CHARTER.md); [Product Baseline — Product Complete definition](PM/PRODUCT_BASELINE.md) |
| **Close the Loop** | Work is not complete at implementation or merge alone; review, merge, Issue closure, baseline synchronization, and required completion evidence are part of the lifecycle. | [Gap Analysis GAP-007 and GAP-008](PM/GAP_ANALYSIS.md); [Product Baseline](PM/PRODUCT_BASELINE.md) |
| **Governance Before Implementation** | Scope, authority, evidence expectations, acceptance criteria, and applicable gates are established before implementation changes the project. | [Project Charter §7](PROJECT_CHARTER.md); [Product Scope — Change boundary](PM/PRODUCT_SCOPE.md) |
| **Phase Gate Enforcement** | A dependent phase begins only after its documented entry and exit conditions are satisfied and the preceding baseline is approved. | [Project Charter §§7 and 10](PROJECT_CHARTER.md); approved sequence [PM-001 PR #3](https://github.com/8nt7h6k229-png/PVOS/pull/3), [PM-002 PR #5](https://github.com/8nt7h6k229-png/PVOS/pull/5), [PM-003 PR #7](https://github.com/8nt7h6k229-png/PVOS/pull/7), and [PM-004 PR #9](https://github.com/8nt7h6k229-png/PVOS/pull/9) |
| **Knowledge is a Product Asset** | Product knowledge is inventoried, classified, indexed, preserved, and reviewed with the same traceability expected of other project assets. | [Product Knowledge Index](PM/PRODUCT_KNOWLEDGE_INDEX.md); [Project Charter §§5–6](PROJECT_CHARTER.md) |
| **AI Assists Engineering** | AI may recover, analyze, compare, and prepare work, but it cannot approve scope, establish product truth, accept engineering work, or declare completion. | [Project Charter §8](PROJECT_CHARTER.md); [Product Capability Matrix](PM/PRODUCT_CAPABILITY_MATRIX.md) |
| **PM Owns Governance** | PM owns approval of product scope, baselines, phase-gate outcomes, governance exceptions, and completion declarations. Engineering and AI prepare evidence for that accountable review. | [Project Charter §§5, 7, and 9](PROJECT_CHARTER.md); [MVP Definition — Acceptance](PM/MVP_DEFINITION.md) |

## 3. Development Principles

Every engineering work item shall apply the constitutional principles as follows:

1. State the product or governance purpose before selecting an implementation response.
2. Identify the approved baseline and evidence relevant to the work.
3. Inspect existing assets and recovery candidates before authorizing equivalent creation.
4. Distinguish existing, planned, future, branch-only, experimental, deprecated, and not-evidenced states where they affect the work.
5. Keep the change bounded by the approved Issue and acceptance criteria.
6. Complete the authorized outcome and its evidence before proposing optimization or expansion.
7. Preserve uncertainties, conflicts, and exceptions as visible findings for PM disposition.

Branch presence, an open Issue, a draft, an implementation, or an AI recommendation is evidence of a state; none alone is proof of approved product capability. Evidence: [Branch Product Knowledge Map — Evidence and status rules](PM/BRANCH_PRODUCT_KNOWLEDGE_MAP.md), [Product Capability Matrix](PM/PRODUCT_CAPABILITY_MATRIX.md), and [Project Charter §7](PROJECT_CHARTER.md).

## 4. Project Governance Workflow

Engineering work follows this governed lifecycle:

**Issue → Branch → Implementation → Commit → Push → Draft Pull Request → PM Review → Merge → Close Issue**

### Issue

Work begins with an Issue that identifies the objective, scope, constraints, acceptance criteria, evidence expectations, and applicable phase gate. The Issue establishes authorized intent; it does not prove implementation or completion.

### Branch

The branch is created from the approved base after entry conditions are confirmed. Its name and commits remain traceable to the Issue. Branch-only content remains branch-only until approved and merged.

### Implementation

Implementation is limited to the Issue scope. Evidence recovery, analysis, documentation, validation, or source changes are performed only when authorized by that scope. Discoveries outside scope are recorded for PM disposition rather than silently absorbed.

### Commit and push

Commits provide immutable evidence of the work performed. The remote branch makes the review package visible in GitHub without changing the approved baseline.

### Draft Pull Request

The Draft Pull Request identifies the Issue, exact change set, evidence, validation, limitations, and remaining review responsibility. Draft status means the work is presented for review preparation, not approved.

### PM Review, merge, and closure

PM review determines whether the acceptance criteria and phase gate are satisfied. Only the reviewed Head may be merged. After merge, the Issue is closed as completed only when the required evidence is present and the approved base contains the merged work.

This lifecycle was used to establish PM-001 through PM-004. Evidence: [PM-001 Issue #2](https://github.com/8nt7h6k229-png/PVOS/issues/2) and [PR #3](https://github.com/8nt7h6k229-png/PVOS/pull/3); [PM-002 Issue #4](https://github.com/8nt7h6k229-png/PVOS/issues/4) and [PR #5](https://github.com/8nt7h6k229-png/PVOS/pull/5); [PM-003 Issue #6](https://github.com/8nt7h6k229-png/PVOS/issues/6) and [PR #7](https://github.com/8nt7h6k229-png/PVOS/pull/7); [PM-004 Issue #8](https://github.com/8nt7h6k229-png/PVOS/issues/8) and [PR #9](https://github.com/8nt7h6k229-png/PVOS/pull/9).

## 5. Phase Gate Policy

A phase gate protects the project from building dependent work on an unapproved premise.

For each gate:

- entry conditions identify the approved evidence required before work begins;
- exit conditions identify the reviews, merges, closures, and baseline state required before the phase is complete;
- gate evidence is recorded in GitHub;
- PM determines whether the gate is open or closed; and
- dependent work remains blocked while required evidence is absent, changed, or unresolved.

A reviewed commit identity is part of the approval evidence when specified. If that identity changes before merge, the approval no longer applies and review is repeated. A gate is not closed by elapsed time, implementation progress, or assertion.

The PM-004 gate demonstrated this policy: PM-001, PM-002, and PM-003 were reviewed, merged, closed, and synchronized to `main` before the Project Charter proceeded; the Charter was then merged only after its reviewed Head remained unchanged. Evidence: merged [PRs #3, #5, #7, and #9](https://github.com/8nt7h6k229-png/PVOS/pulls?q=is%3Apr+is%3Amerged) and closed [Issues #2, #4, #6, and #8](https://github.com/8nt7h6k229-png/PVOS/issues?q=is%3Aissue+is%3Aclosed).

## 6. GitHub Governance

GitHub is the durable Single Source of Truth for governed engineering state.

The following evidence roles apply:

- **Issue:** authorized intent, boundaries, acceptance criteria, and lifecycle state.
- **Branch:** isolated work and recoverable context; not an approved baseline by itself.
- **Commit:** immutable content evidence.
- **Pull Request:** proposed integration, review discussion, validation, and approval record.
- **Review:** accountable assessment of the exact proposed change.
- **Merge:** admission into the approved branch, subject to the applicable gate.
- **Closed Issue:** recorded lifecycle completion after the work and closure evidence agree.
- **Default branch and merged governance documents:** current approved baseline.

Issue or PR text proves intent and workflow state, while commits and documents prove content. Open and draft work is never represented as merged baseline. Direct-to-base exceptions, unresolved comments, changed review Heads, failed validation, or unclear scope remain visible and block completion unless PM records a bounded disposition.

Evidence: [Portfolio inventory rules](PM/GITHUB_PORTFOLIO_ASSET_INVENTORY.md), [Product Knowledge Index — Authority rules](PM/PRODUCT_KNOWLEDGE_INDEX.md), [Gap Analysis GAP-003, GAP-005, GAP-007, and GAP-016](PM/GAP_ANALYSIS.md), and [Project Charter §7](PROJECT_CHARTER.md).

## 7. Product Governance

Engineering work shall preserve the approved product purpose, baseline, scope, MVP, exclusions, and capability classifications.

- Existing capability requires approved baseline evidence.
- Planned capability remains excluded until its governed work is accepted.
- Future or branch-only knowledge remains a candidate, not a commitment.
- Not-evidenced capability is not inferred or claimed.
- A capability changes state only through an explicit governed baseline change.

Implementation discovery, recovery, technical feasibility, or AI output cannot silently expand the product. When work would affect scope or capability state, PM approval and the associated baseline update precede any product claim.

Evidence: [Product Baseline](PM/PRODUCT_BASELINE.md), [Product Scope — Change boundary](PM/PRODUCT_SCOPE.md), [Product Capability Matrix](PM/PRODUCT_CAPABILITY_MATRIX.md), and [Project Charter §§4–5](PROJECT_CHARTER.md).

## 8. Knowledge Governance

Product and engineering knowledge is governed as a product asset.

Before creating or replacing knowledge, the project shall:

1. inventory relevant repositories, branches, Issues, Pull Requests, documents, and commits;
2. classify each finding by subject, location, evidence, and lifecycle state;
3. distinguish approved baseline knowledge from branch-only, deprecated, experimental, planned, future, or missing knowledge;
4. preserve provenance when recovering or promoting knowledge; and
5. record gaps without filling them through unsupported inference.

Recovery does not authorize automatic merging, deletion, redesign, or product promotion. Obsolete for independent recovery does not itself authorize branch deletion. Conflicting or duplicate knowledge remains visible until PM disposition.

Evidence: [GitHub Portfolio Asset Inventory](PM/GITHUB_PORTFOLIO_ASSET_INVENTORY.md), [Product Knowledge Index](PM/PRODUCT_KNOWLEDGE_INDEX.md), [Branch Product Knowledge Map](PM/BRANCH_PRODUCT_KNOWLEDGE_MAP.md), [Branch Recovery Index](PM/BRANCH_RECOVERY_INDEX.md), and [Gap Analysis](PM/GAP_ANALYSIS.md).

## 9. AI Governance

AI assists engineering by helping recover evidence, classify knowledge, analyze repositories, identify gaps, compare approved records, and prepare reviewable work.

AI shall:

- operate within the authorized Issue and approved baseline;
- cite evidence for material findings and clearly identify uncertainty;
- keep generated work reviewable and attributable;
- avoid presenting inference as repository fact; and
- stop at human decision boundaries for scope, product truth, acceptance, exceptions, and completion.

AI shall not approve its own work, alter the product baseline by assertion, replace PM governance, or treat its model, memory, conversation, or tool state as the Single Source of Truth. AI models and providers remain replaceable; governance and evidence remain durable.

Evidence: [Project Charter §8](PROJECT_CHARTER.md), [Product Capability Matrix — AI Studio / Repository Intelligence](PM/PRODUCT_CAPABILITY_MATRIX.md), [Product Knowledge Index — AI knowledge](PM/PRODUCT_KNOWLEDGE_INDEX.md), and [MVP Definition — exclusions](PM/MVP_DEFINITION.md).

## 10. Change Control

Every governed change begins with an Issue and identifies:

- the approved baseline being changed or preserved;
- the purpose, scope, exclusions, and acceptance criteria;
- the evidence and validation required;
- dependencies and phase-gate conditions;
- the exact proposed change set; and
- the accountable PM review required for approval.

Changes remain bounded through branch isolation and Pull Request review. Amendments after approval require renewed review when they alter the reviewed evidence. No rebase, amendment, force-push, direct merge, or content substitution may be used to preserve the appearance of an approval after the reviewed change has changed.

Exceptions are not implied. PM may record a bounded exception with its reason, affected scope, evidence, and disposition; the exception remains visible and does not silently become normal practice.

Evidence: [Project Charter §7](PROJECT_CHARTER.md), [Gap Analysis GAP-016](PM/GAP_ANALYSIS.md), and the reviewed-Head integrity and closing record in [PM-004 PR #9](https://github.com/8nt7h6k229-png/PVOS/pull/9).

## 11. Completion Definition

A work item is complete only when all applicable conditions are satisfied:

1. The Issue objective and acceptance criteria are met within scope.
2. Required evidence and validation are recorded and reviewable.
3. The Pull Request contains only the approved change set.
4. Blocking findings and review threads are resolved or receive an explicit PM disposition.
5. PM approves the exact reviewed Head under the applicable phase gate.
6. The approved change is merged into the intended base.
7. The intended base contains the reviewed work and is synchronized where required.
8. The Issue is closed as completed.
9. Required branch or closing actions are recorded.
10. The resulting product, knowledge, and governance states agree with the approved baseline.

Implementation complete, documentation complete, merged, and product complete are distinct claims. Each requires its applicable evidence; none is inferred from another. This rule closes the lifecycle gaps recorded during PM-001 and applies the no-silent-completion rule of the Charter.

Evidence: [Product Baseline — Product Complete definition](PM/PRODUCT_BASELINE.md), [Gap Analysis GAP-007 and GAP-008](PM/GAP_ANALYSIS.md), [Project Charter §§7 and 9](PROJECT_CHARTER.md), and [PM-004 closing record](https://github.com/8nt7h6k229-png/PVOS/pull/9).

## 12. Continuous Improvement

Continuous improvement applies to the governed process without silently changing this Constitution.

The project shall use completed work, gap analysis, incidents, review findings, and closure evidence to identify where governance was unclear, incomplete, or unenforced. Improvement begins by inventorying the evidence and recovering existing practice. A proposed constitutional change then follows the same Issue, branch, Pull Request, PM review, merge, and closure workflow as other governed work.

No lesson, tool preference, AI recommendation, or isolated exception becomes constitutional practice automatically. A change must show that it is consistent with the Project Charter, supported by approved evidence, and accepted by PM. Until approval, the current Constitution remains authoritative.

Evidence: [Gap Analysis](PM/GAP_ANALYSIS.md), [Project Charter §§7 and 10](PROJECT_CHARTER.md), and the approved PM-001 through PM-004 workflow records.

---

This Constitution takes effect only after PM approval and merge. It governs engineering process while leaving product purpose to the Project Charter and product boundaries to the approved Product Baseline, MVP Definition, Product Scope, and Product Capability Matrix.
