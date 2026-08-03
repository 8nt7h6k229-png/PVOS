# PVOS Project Charter

Status: Proposed for PM approval

Authority: PVOS Project Governance

Evidence baseline: PM-001, PM-002, and PM-003

This Charter is the highest-level governance reference for PVOS. It states why the project exists, what product it is accountable for, and how enduring decisions are made. Detailed product boundaries remain in the approved governance baseline; this Charter does not replace or expand them.

## 1. Vision

PVOS exists to make photovoltaic planning results dependable, understandable, and governable.

The project envisions a product whose planning outcomes can be reviewed with confidence because its scope is explicit, its evidence is traceable, and its results are produced within approved boundaries. PVOS should remain coherent as implementations, delivery environments, and supporting tools change.

This vision follows the approved definition of PVOS 1.0 as a bounded, deterministic 2D photovoltaic placement baseline, not as the sum of every capability found in repository history. Evidence: [Product Baseline](PM/PRODUCT_BASELINE.md) and [Product Capability Matrix](PM/PRODUCT_CAPABILITY_MATRIX.md).

## 2. Mission

The mission of PVOS is to turn explicit photovoltaic planning geometry and parameters into reviewable placement results while preserving a trustworthy chain from product intent to approved evidence.

PVOS pursues this mission by:

- maintaining a clear product baseline and explicit exclusions;
- preserving product knowledge without confusing historical, planned, or experimental work with released capability;
- requiring material decisions and changes to pass through the governed delivery workflow; and
- keeping product truth in approved, durable records rather than in conversations, assumptions, or tool-specific state.

Evidence: [GitHub Portfolio Asset Inventory](PM/GITHUB_PORTFOLIO_ASSET_INVENTORY.md), [Branch Product Knowledge Map](PM/BRANCH_PRODUCT_KNOWLEDGE_MAP.md), and [Product Scope](PM/PRODUCT_SCOPE.md).

## 3. Product Position

PVOS is an evidence-driven photovoltaic planning product foundation. Its defining value is not the number of accumulated features, but the reliability and clarity of the capability it officially supports.

PVOS 1.0 is positioned around a bounded workflow: explicit planning geometry and orientation, explicit module parameters, deterministic placement within the supplied boundary, and a reviewable result summary. Existing product-host and adapter assets are recognized, but unverified integration is not presented as complete. Evidence: [MVP Definition](PM/MVP_DEFINITION.md) and [Product Baseline](PM/PRODUCT_BASELINE.md).

Historical branches, open work items, and proposed capabilities remain portfolio evidence. They do not become official product claims until approved through governance. Evidence: [Branch Recovery Index](PM/BRANCH_RECOVERY_INDEX.md) and [Product Capability Matrix](PM/PRODUCT_CAPABILITY_MATRIX.md).

## 4. Product Baseline

The official PVOS 1.0 product baseline is the approved baseline defined by PM-003. At Charter approval, it consists of the existing deterministic 2D placement foundation and its bounded inputs, transformations, containment behavior, outputs, tests, and recognized supporting assets.

The baseline distinguishes four states:

- **Existing** — approved evidence supports the capability on the official baseline.
- **Planned** — an open, governed work item exists, but the capability is not included.
- **Future** — repository evidence or proposals exist, but they are not a PVOS 1.0 commitment.
- **Not evidenced** — no affirmative basis exists for a product claim.

Only an approved baseline change may alter these states. Discovery, branch presence, implementation history, or AI output alone cannot expand the product baseline. Evidence: [Product Baseline](PM/PRODUCT_BASELINE.md), [Product Scope](PM/PRODUCT_SCOPE.md), and [Product Capability Matrix](PM/PRODUCT_CAPABILITY_MATRIX.md).

## 5. Project Scope

The project governs the definition, evidence, controlled evolution, and accountable delivery of PVOS.

Within the PVOS 1.0 boundary, the project is responsible for:

- the approved product purpose and MVP outcome;
- the integrity of the official product baseline;
- the classification and preservation of product knowledge;
- the distinction between included, planned, future, experimental, deprecated, and unsupported claims; and
- the evidence and review needed to declare a product state complete.

The project does not treat every historical branch or adjacent idea as active scope. Items excluded or not evidenced by the approved baseline remain outside PVOS 1.0 unless a later governed decision changes the baseline. Evidence: [Product Scope](PM/PRODUCT_SCOPE.md), [Gap Analysis](PM/GAP_ANALYSIS.md), and [Branch Recovery Index](PM/BRANCH_RECOVERY_INDEX.md).

## 6. Core Values

### Evidence before assertion

Product claims and decisions must be traceable to approved records. Uncertainty is stated; it is not filled with inference. Evidence: [Portfolio Asset Inventory](PM/GITHUB_PORTFOLIO_ASSET_INVENTORY.md).

### Determinism and reviewability

The product should produce outcomes that can be examined and compared within their approved boundary. Reviewability is a product quality, not merely a delivery activity. Evidence: [MVP Definition](PM/MVP_DEFINITION.md).

### Clarity of scope

Included, planned, future, and unsupported capabilities are kept distinct. Scope is not expanded through implication. Evidence: [Product Capability Matrix](PM/PRODUCT_CAPABILITY_MATRIX.md).

### Knowledge stewardship

Repository history is preserved and classified so that useful knowledge can be recovered without rewriting history or mistaking older work for current authority. Evidence: [Product Evolution Timeline](PM/PRODUCT_EVOLUTION_TIMELINE.md) and [Branch Recovery Index](PM/BRANCH_RECOVERY_INDEX.md).

### Accountability

Completion requires verifiable evidence, review, approval, and closure. A claim of progress cannot substitute for the governed state of the project. Evidence: [Product Baseline](PM/PRODUCT_BASELINE.md).

### Durable purpose

The project is guided by user and engineering outcomes rather than by a particular implementation, delivery environment, or AI model.

## 7. Governance Principles

1. **Approved evidence is authoritative.** The official baseline is established through reviewed and merged records.
2. **Scope changes are explicit.** A capability enters the product only through a governed baseline change.
3. **History is evidence, not automatic authority.** Branch-only, deprecated, experimental, and recovery assets remain classified until reviewed.
4. **Decisions are traceable.** Material product decisions identify their evidence, owner, review, and resulting state.
5. **No silent promotion.** Planned, future, or not-evidenced capabilities cannot be represented as existing.
6. **No silent completion.** Product completion requires the approved evidence and closure conditions defined by the baseline.
7. **Governance is implementation-independent.** Tools may support the workflow, but no tool determines product truth by itself.
8. **Exceptions remain visible.** Any approved exception must be bounded and recorded; it does not silently become normal practice.

These principles consolidate the approved inventory, recovery, gap, and baseline rules without changing them. Evidence: [Gap Analysis](PM/GAP_ANALYSIS.md), [Branch Product Knowledge Map](PM/BRANCH_PRODUCT_KNOWLEDGE_MAP.md), and [Product Baseline](PM/PRODUCT_BASELINE.md).

## 8. AI Position

AI is a supporting capability for knowledge recovery, analysis, documentation, and planning assistance. It may help people find evidence, compare alternatives, identify gaps, and prepare reviewable work.

AI is not the authority for product truth, engineering acceptance, scope approval, or release completion. Its outputs must remain traceable, reviewable, and subject to the same governance as human-produced work. Deterministic product evidence and accountable approval remain authoritative.

AI models, providers, and interfaces are replaceable. The project's purpose, evidence standards, and decision rights must outlive them. AI-assisted product functionality is not part of the PVOS 1.0 MVP unless separately admitted through an approved baseline change.

Evidence: AI Studio and Repository Intelligence are classified as existing internal engineering support in [Product Capability Matrix](PM/PRODUCT_CAPABILITY_MATRIX.md); AI-generated product decisions are excluded from the approved [MVP Definition](PM/MVP_DEFINITION.md); the AI asset inventory is recorded in [Product Knowledge Index](PM/PRODUCT_KNOWLEDGE_INDEX.md).

## 9. Product Success Criteria

PVOS is successful when:

- users and reviewers can understand what the product does and does not claim to do;
- supported planning outcomes are deterministic and reviewable within the approved boundary;
- every official capability is connected to approved evidence and accountable ownership;
- product knowledge remains discoverable across repositories and history;
- planned and future work cannot silently alter current product claims;
- gaps, limitations, and integration uncertainty remain visible until resolved;
- product-complete declarations satisfy the approved governance and validation conditions; and
- the project can evolve without losing its product purpose or historical accountability.

Success is measured against the approved baseline and its completion criteria, not against feature count or the volume of historical implementation. Evidence: [Product Baseline](PM/PRODUCT_BASELINE.md), [Product Scope](PM/PRODUCT_SCOPE.md), and [Gap Analysis](PM/GAP_ANALYSIS.md).

## 10. Long-term Strategy

PVOS will evolve by protecting a stable product purpose while allowing governed changes to the product baseline.

Long-term direction is governed by the following commitments:

- **Strengthen the approved core before expanding claims.** Product integrity takes precedence over breadth.
- **Recover before recreating.** Existing portfolio knowledge is examined and classified before new work is authorized.
- **Promote through evidence.** Historical, planned, and future capabilities advance only after review establishes their product value, boundary, and acceptance evidence.
- **Maintain one official baseline.** Repositories and branches may serve different roles, but the approved product definition remains singular and explicit.
- **Preserve portfolio optionality without promising it.** Recoverable assets remain available for future decisions without becoming automatic commitments.
- **Keep governance durable.** Decision principles survive changes in implementation, organization, tools, and AI models.

This strategy defines how direction is governed; it is not a roadmap and sets no sprint sequence. Evidence: [Branch Recovery Index](PM/BRANCH_RECOVERY_INDEX.md), [Product Evolution Timeline](PM/PRODUCT_EVOLUTION_TIMELINE.md), and [Product Baseline](PM/PRODUCT_BASELINE.md).

---

The Charter is changed only through the governed project workflow. Subordinate plans, baselines, and engineering decisions must remain consistent with it. Where detailed product evidence changes, the applicable baseline documents are updated and approved without silently rewriting the enduring purpose stated here.
