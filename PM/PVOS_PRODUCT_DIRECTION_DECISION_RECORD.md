# PVOS Product Direction Decision Record

## 1. Decision Identity

| Field | Decision Record |
|---|---|
| Decision Name | PVOS Product Direction — Gate 1 |
| Date | 2026-08-07 (Asia/Taipei) |
| Product | PVOS |
| Decision Gate | Gate 1 — Product Direction Approval |
| Status | APPROVED WITH BOUNDARY CONDITIONS |
| Record Type | Durable Owner／PM Product Direction Decision |
| Decision Basis | `PM/PVOS_PRODUCT_DIRECTION_DECISION_PACKAGE.md` |

## 2. Owner Decision

Owner approves the following direction:

| Decision Item | Owner Decision |
|---|---|
| PVOS Product Direction | APPROVED |
| Dual-Line Development Strategy | APPROVED |
| Core + Domain Modules Direction | APPROVED |
| Implementation Authorization | NOT GRANTED BY THIS DECISION |
| Product Scope Expansion | NOT GRANTED BY THIS DECISION |

Owner approval establishes the product direction and the decision framework only. It does not approve a Domain implementation, Product Scope change, GitHub Issue Queue or development commitment.

## 3. PM Decision

| Field | PM Decision |
|---|---|
| Recommendation | APPROVED WITH BOUNDARY CONDITIONS |
| Approval Basis | Existing Product Acceptance, Production Readiness, Feature Expansion evidence, Domain Market Strategy Review and current Core evidence |
| Scope Effect | No Product Scope modification |
| Implementation Effect | No implementation authorization |
| Next Required Review | Gate 2 — Domain Selection Review |

PM recommends approval because the proposed direction preserves the accepted deterministic C# Mainline, formalizes the Core／Domain responsibility boundary and retains Evidence-first Product Acceptance controls. Approval remains bounded by Sections 6 and 7 of this record.

## 4. Approved Direction

### Product Positioning

PVOS is positioned as:

> **PV Engineering Layout and Evidence Operating System**

PVOS provides deterministic engineering layout behavior, validation and traceable evidence over explicitly governed inputs. It supports engineering decision workflows without replacing qualified Domain, structural, electrical, regulatory or Product Acceptance authority.

### Approved Core Direction

The approved PVOS Core direction contains:

| Core Capability | Approved Responsibility Direction |
|---|---|
| Geometry | Stable, explicit and verifiable geometry foundation |
| Partition | Explicit governed configuration regions and selection |
| Layout | Deterministic placement from approved inputs and parameters |
| Validation | Product input, output, integrity and accepted-rule verification |
| Evidence | Traceable input, result, version, validation and claim evidence |
| Result Package | Read-only packaging of Product results and Evidence references |

### Approved Architecture Direction

```text
Domain Data / Domain Rules / Domain Ownership
                    ↓
              Domain Modules
                    ↓
                PVOS Core
Geometry → Partition → Layout → Validation
                    ↓
        Evidence → Result Package
```

The approved architecture direction is **Core + Domain Modules**.

- PVOS Core owns reusable deterministic Product behavior.
- Domain Modules own Domain semantics, rules, eligibility, translation and responsibility boundaries.
- A Domain Module may use the Core but may not duplicate or replace the Core Layout Engine.
- Approval of this direction does not approve any individual Domain Module implementation.

## 5. Dual-Line Development Strategy

### Line 1 — PVOS Mainline Product

| Field | Approved Direction |
|---|---|
| Technology | C#／.NET |
| Authority | Product Behavior Authority |
| Responsibility | Production Features, Domain Modules, Release Capability and Product Acceptance implementation basis |
| Engine Status | Sole PVOS Product Engine |

C#／.NET Mainline is the only authority that may implement accepted PVOS Product behavior and form a Product Release candidate.

### Line 2 — PVOS Validation／Engineering Support Track

| Field | Approved Direction |
|---|---|
| Technology | Python |
| Authority | Validation only |
| Responsibility | Rapid validation, Evidence generation, Regression support, Engineering experiments and Field support tools |
| Product Authority | NONE |

Python may observe, validate, compare and report C# Mainline results and admitted Evidence. Python may not calculate or repair Placement, define Product behavior, replace C# Mainline or become a second PVOS Engine.

### Promotion Boundary

```text
Validation Track Candidate
          ↓
     Evidence Proven
          ↓
       PM Review
          ↓
Mainline Promotion Candidate
          ↓
Implementation Authorization
```

`Mainline Promotion Candidate` means eligible for separate Mainline planning review only. It does not mean promoted, scheduled, implemented or accepted.

Any Product behavior originating from a Validation／Engineering experiment must receive explicit Implementation Authorization, be implemented in C# Mainline and later pass Product Acceptance. Python code itself does not acquire Product Behavior Authority through this process.

## 6. Boundary Conditions

This decision explicitly does **not** authorize:

- Python becoming a second PVOS Engine.
- Python replacing C#／.NET Mainline or owning Product Behavior Authority.
- Legacy asset Promotion.
- Canonical Project Model Promotion.
- PVOS 2.x expansion.
- Unapproved Rooftop, Ground Mount, Fishery or other Domain implementation.
- Electrical, Shading, Structural or other specialist capability implementation.
- Product Scope expansion without the applicable Decision Gate and explicit authority.
- Research evidence, prototypes or planning documents being treated as implementation commitments.
- A GitHub Issue Queue, code change, release or Product Acceptance arising automatically from Gate 1.

### Boundary Confirmation

| Boundary | Confirmation |
|---|---|
| C# Mainline remains sole Product Behavior Authority | CONFIRMED |
| Python remains Validation／Engineering Support Track only | CONFIRMED |
| No second Engine | CONFIRMED |
| No Legacy or Canonical Promotion | CONFIRMED |
| No PVOS 2.x expansion | CONFIRMED |
| No unapproved Domain implementation | CONFIRMED |
| No Scope expansion without Gate | CONFIRMED |
| No implementation started by this record | CONFIRMED |

## 7. Deferred Items

The following items remain deferred and are not approved for implementation:

| Deferred Item | Current Disposition |
|---|---|
| Ground Mount Domain | DEFERRED — candidate feasibility／market evidence only |
| Fishery PV Domain | DEFERRED — Domain evidence and ownership research only |
| Electrical | DEFERRED — separate specialist direction and authority required |
| Shading | DEFERRED — separate specialist direction and authority required |
| AutoCAD Full Integration | DEFERRED — no implementation commitment |
| Cloud／UI | DEFERRED — outside the approved immediate product direction |

Rooftop PV is a Gate 2 selection candidate, not an approved Domain implementation. Ground Mount and Fishery PV remain deferred regardless of their market potential until separately reviewed.

## 8. Next Gate

### Gate 2 — Domain Selection Review

Gate 2 determines whether one Domain is sufficiently evidenced to enter bounded implementation planning review. Gate 2 does not itself authorize implementation unless the subsequent Gate 3 requirements and explicit authority are satisfied.

### Required Evidence

| Evidence Area | Minimum Requirement |
|---|---|
| Market Evidence | Identified user, payer, workflow pain, frequency, impact, alternative tools and adoption evidence |
| Domain Owner | Named accountable owner for Domain data, rules, applicability and professional responsibility |
| Workflow Validation | Current-state and proposed workflow validated with representative users and bounded cases |
| Value Assessment | Factual value hypothesis covering rework, consistency, Evidence, time or risk; commercial assumptions remain explicit |
| Technical Fit | Core reuse, Domain gap, data contract, dependencies, complexity and no-second-Engine proof |

### Gate 2 Required Decision

Gate 2 must return one of:

- `DOMAIN SELECTED WITH BOUNDARY CONDITIONS`
- `RETURNED FOR ADDITIONAL EVIDENCE`
- `DEFERRED`
- `REJECTED`

No Domain may progress to an Implementation Queue solely because it is ranked first in the Market Strategy Review.

## Decision Evidence Chain

- `PM/PVOS_PRODUCT_DIRECTION_DECISION_PACKAGE.md`
- `PM/PVOS_DOMAIN_MARKET_STRATEGY_REVIEW_PACKAGE.md`
- `PM/PVOS_1_0_PM_PRODUCT_ACCEPTANCE_RECORD.md`
- `PM/PVOS_1_1_PRODUCTION_READINESS_DECISION_RECORD.md`
- `PM/PVOS_1_2_POST_ACCEPTANCE_PLANNING_PACKAGE.md`
- `PM/PVOS_1_2_MILESTONE_ACCEPTANCE_REVIEW.md` when present in the governed evidence chain
- Current C# Core, Layout, Golden Dataset, Regression, Runtime and Python Validation Evidence

## Constraint Verification

| Constraint | Result |
|---|---|
| No code modification | PASS |
| No GitHub Issue Queue | PASS |
| No EOS modification | PASS |
| No Governance modification | PASS |
| No Product Scope modification | PASS |
| No implementation started | PASS |

## Final Decision Status

**GATE 1 — PRODUCT DIRECTION APPROVED WITH BOUNDARY CONDITIONS**

**NEXT GATE — GATE 2: DOMAIN SELECTION REVIEW**
