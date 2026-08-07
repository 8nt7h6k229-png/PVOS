# Platform / Product Separation — Architecture Decision Knowledge

## Purpose

Preserve the approved 2026-08-06 Platform / Product Separation architecture decision as reusable Engineering Knowledge.

## Architecture Decision

### Platform

`AIStudioCore` is the Engineering Platform.

Its responsibilities contain:

- Engineering Operating System;
- Governance;
- Planning Package;
- PM GitHub Issue Builder;
- Execution Queue;
- Repository Intelligence;
- Handover; and
- Engineering Knowledge.

### Products

AIStudioCore hosts one or more independent Products.

PVOS is the first Product hosted by AIStudioCore. PVOS owns its:

- Product Blueprint;
- Product Roadmap;
- Product Backlog;
- Product Acceptance; and
- Product Release.

### Separation Rule

Platform and Products are independent architectural layers.

Products consume Platform capabilities. The Platform shall never become a Product.

## Rationale

- Engineering execution, governance, planning, evidence, knowledge, and handover are reusable Platform responsibilities rather than PVOS product behavior.
- Product intent, product sequencing, product acceptance, and product release remain owned by each independent Product.
- Keeping these responsibilities separate prevents Platform capability from being presented as PVOS product functionality.
- The separation allows the same Engineering Platform capabilities to support more than one independent Product without transferring Product ownership to the Platform.

## Evidence

| Evidence | Supported Observation |
|---|---|
| `governance/EOS_V1_CAPABILITY_MATRIX.md` | AIStudioCore Engineering Operating System capabilities are classified separately from PVOS product capabilities. |
| `governance/GOVERNANCE_INFORMATION_ARCHITECTURE.md` | Governance, Planning, Work Orders, Evidence, Engineering Knowledge, Handover, and Workspace are Platform information domains. |
| `governance/PM_GITHUB_ISSUE_BUILDER.md` | Daily Planning Packages are converted into governed GitHub Issue execution queues. |
| `governance/EXECUTION_QUEUE_GOVERNANCE.md` | Execution Queue control is an Engineering Platform responsibility. |
| `governance/AISTUDIOCORE_HANDOVER.md` | AIStudioCore maintains governed engineering continuity. |
| `PRODUCT/PRODUCT_BLUEPRINT.md` | PVOS product intent and portfolio position are maintained as Product information. |
| `PRODUCT/PRODUCT_BACKLOG.md` | PVOS candidate Product Engineering work is maintained within the Product layer. |
| `PRODUCT/PRODUCT_RELEASE_PLAN.md` | PVOS capability allocation, acceptance gates, and releases are Product responsibilities. |
| `PM/PRODUCT_BASELINE.md` | PVOS current product boundary is evidenced independently of Platform capability. |
| `ENGINEERING/PVOS_PRODUCT_DISCOVERY_KNOWLEDGE_2026-08-06.md` | PVOS is recorded as an existing Deterministic Layout MVP awaiting Product Acceptance. |

The evidence identifies the currently separate responsibility sets. This knowledge record preserves the approved architectural rule and does not modify any cited source.

## Impact

1. AIStudioCore work shall be classified as Engineering Platform work unless an independent Product work item explicitly owns the product outcome.
2. PVOS planning and acceptance shall remain within PVOS Product assets and shall consume, rather than absorb, AIStudioCore Platform capabilities.
3. Engineering Operating System completion does not establish PVOS product completion.
4. PVOS product progress does not redefine AIStudioCore as a PVOS-specific Product.
5. Shared Platform capabilities may support multiple Products without merging their Blueprints, Backlogs, Acceptance records, or Releases.

## Future Product Strategy

The architecture shall support additional independent Products, including but not limited to:

- CRM;
- MES; and
- Steel Platform.

Each future Product shall maintain its own product intent, roadmap, backlog, acceptance, and release boundary while consuming applicable AIStudioCore Platform capabilities. Listing a future Product here records architectural extensibility only; it does not approve, scope, prioritize, or initiate that Product.

## Related Documents

- `governance/EOS_V1_CAPABILITY_MATRIX.md`
- `governance/GOVERNANCE_INFORMATION_ARCHITECTURE.md`
- `governance/PM_GITHUB_ISSUE_BUILDER.md`
- `governance/EXECUTION_QUEUE_GOVERNANCE.md`
- `governance/AISTUDIOCORE_HANDOVER.md`
- `PRODUCT/PRODUCT_BLUEPRINT.md`
- `PRODUCT/PRODUCT_CAPABILITY_TREE.md`
- `PRODUCT/PRODUCT_BACKLOG.md`
- `PRODUCT/PRODUCT_RELEASE_PLAN.md`
- `PM/PRODUCT_BASELINE.md`
- `ENGINEERING/PVOS_PRODUCT_DISCOVERY_KNOWLEDGE_2026-08-06.md`

## Status

Architecture Decision Engineering Knowledge prepared for PM review.
