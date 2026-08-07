# PVOS Dual Workflow Execution Strategy

## 1. Decision Identity

| Field | Decision Record |
|---|---|
| Decision Name | PVOS Dual Workflow Execution Strategy |
| Date | 2026-08-07 (Asia/Taipei) |
| Product | PVOS |
| Authority | Owner Approved Direction／PM Command |
| Status | ACTIVE WITH BOUNDARY CONDITIONS |
| Decision Scope | Product execution workflow separation; no Product Scope or implementation authorization change |

## Source Basis

- `PM/PVOS_PRODUCT_DIRECTION_DECISION_RECORD.md`
- `PM/PVOS_GATE2_DOMAIN_SELECTION_REVIEW_PACKAGE.md`
- `PM/ROOFTOP_GATE2_BLOCKED_EVIDENCE_RECOVERY_PLAN.md`
- `PM/PVOS_PRODUCT_DIRECTION_DECISION_PACKAGE.md` — Dual-Line Development Strategy

## Decision Purpose

正式記錄 PVOS 同時維持兩條互相協調、但權限與輸入來源不同的工作流：

1. **Product Mainline Workflow**：在既有核准 Product Scope 與正式執行授權下持續 Product Core、Validation、Evidence 及 Regression 工作。
2. **External Evidence Workflow**：蒐集 Domain Selection 所需、無法由 Repository 或產品程式自行產生的外部證據。

外部證據不足會暫停 Domain Selection，但不會凍結所有 Mainline 工程活動。相對地，Mainline 活躍也不能繞過 Domain Gate，提前實作 Rooftop 或其他未核准 Domain capability。

## 2. Dual Workflow Strategy Overview

```text
Workflow A — Product Mainline
C# Product Behavior + Validation / Regression / Evidence
                    │
                    │ approved Product boundary only
                    │
                    ├──────────────┐
                    │              │
                    │       Shared Evidence Standards
                    │              │
                    └──────────────┤
                                   │
Workflow B — External Evidence Track
Domain Owner + Customer Workflow + Cases + Value + Responsibility
                                   │
                                   ↓
                           PM Gate 2 Decision
```

### Workflow Relationship

| Area | Workflow A — Product Mainline | Workflow B — External Evidence Track |
|---|---|---|
| Primary Purpose | 維持及改善已核准 Product capabilities | 補足 Domain Selection 的外部與責任證據 |
| Product Authority | C#／.NET Mainline | NONE |
| Typical Evidence | Tests、Golden、Regression、Result lineage、release evidence | Owner acceptance、interviews、case provenance、baseline、professional responsibility |
| Python Role | Validation／Engineering Support | Evidence checking、formatting and traceability support only |
| Gate Dependency | 既有 Scope 內工作不依賴 Domain Selection | 必須通過 PM Gate 2 才能形成 Domain Selection |
| Domain Implementation | 禁止，除非另通過 Gate 2 and Gate 3 | 不實作 Product behavior |

### Coordination Rule

- Workflow A 可以提供 Core capability facts、Validation method and Evidence format 給 Workflow B。
- Workflow B 可以提交 Domain requirement、risk and evidence-backed candidate 給 PM Review。
- Workflow B 的發現不會自動變成 Workflow A 的 Product behavior。
- 任何 Promotion 必須依 Section 5 的 Python／Evidence Promotion Boundary 及正式 Gate 流程。

## 3. Workflow A — Product Mainline

### Purpose

持續產品開發，不等待 Domain Selection；但只限既有 PVOS Product Scope、已批准 Planning／Execution authority 及 Product Acceptance process 內的工作。

`Mainline ACTIVE` 表示這條工作流可接受未來經正式授權的工作，不表示本文件本身建立 Issue、排程、Commit 或 Implementation Authorization。

### Authority

| Field | Authority |
|---|---|
| Technology | C#／.NET |
| Product Behavior Authority | PVOS Mainline only |
| Release Capability | Mainline under approved release process |
| Product Acceptance | PM／Owner decision based on Mainline Evidence |
| Python Authority | Validation／Engineering Support only |

### Allowed Product Areas

在不改變既有 Scope、且另有正式工作授權時，Workflow A 可處理：

- Core Geometry。
- Partition。
- Deterministic Layout。
- Core／Product Validation。
- Evidence lineage and integrity。
- Result Package。
- Golden／Regression Foundation。
- Evidence automation and failure isolation。
- Python validation tooling that does not calculate Product behavior。

「Allowed」代表符合本策略的候選工作類別，不是本文件對任何具體功能的 Implementation Authorization。

### Mainline Execution Controls

每項 Mainline 工作仍須具備：

- 正式 Source and Execution Authority。
- Scope、Out of Scope and affected Product capability。
- Architecture／Product boundary review where applicable。
- Tests、Golden／Regression and Evidence requirements。
- No second Engine proof。
- PM Review and Product Acceptance boundary。

### Python Role

Python 可在 Workflow A 中：

- 驗證 C# CLI／Mainline outputs。
- 檢查 Golden manifest、hash、repeatability and Evidence completeness。
- 產生不改寫 Product result 的 Evidence report。
- 支援 Regression automation、diagnostics and engineering productivity。

Python 不得產生、修復或替代 C# Product result。

### Forbidden

- 未批准的 Domain Rule。
- Rooftop-specific implementation。
- Ground Mount or Fishery-specific implementation。
- Hidden Scope Expansion。
- 以通用 Core 名義放入單一 Domain behavior。
- Python placement、second Engine or Product Behavior Authority。
- Legacy／Canonical Promotion without separate authority。
- 因 Mainline Active 而跳過 Planning、Execution、Review or Acceptance controls。

## 4. Workflow B — External Evidence Track

### Purpose

補足 Domain Selection 所需、不能由產品程式或 Repository 推測的外部證據。External Evidence Track 不是產品開發線，也不擁有 Product behavior。

### Current Example

**Rooftop Gate 2 Evidence Recovery**

目前 Rooftop Gate 2 因六項外部／責任證據不足而處於 Hold：

- `RT-GAP-001` Domain Owner。
- `RT-GAP-002` Customer Workflow。
- `RT-GAP-003` Representative Cases。
- `RT-GAP-004` Current-State Value Baseline。
- `RT-GAP-005` User／Payer／Value Evidence。
- `RT-GAP-007` Professional Responsibility Boundary。

`RT-GAP-006` Domain Contract、`RT-GAP-008` Technical Fit and `RT-GAP-009` Scope Boundary review evidence remain preserved.

### Required External Evidence

| Evidence Area | Required Proof | Cannot Be Replaced By |
|---|---|---|
| Domain Owner | Named authority、Rule／Data ownership、maintenance and exclusions | Owner command alone、Codex inference or role placeholder |
| Customer Workflow | Representative actor、tool、handoff、revision、pain and Evidence confirmation | Market report or internal candidate workflow |
| Representative Cases | Legal rights、de-identification、provenance、version、bounded claim and admission | Core Golden scenarios or direct Legacy Promotion |
| Value Baseline | Factual time、revision、error or verification measurement | Qualitative benefit statement or estimated ROI |
| Professional Responsibility | Named Domain／Structural／Electrical／Shading／regulatory responsibility acceptance | Draft matrix without accountable acceptance |

### External Evidence Activities

- Owner appointment and responsibility acceptance。
- Customer／EPC／designer／professional interviews。
- Lawful, de-identified case collection and Evidence Admission。
- Current-state measurement and commercial role validation。
- Responsibility matrix acceptance and contradiction resolution。
- Evidence status tracking and PM handover preparation。

### Status Model

| Status | Meaning | Authority |
|---|---|---|
| `BLOCKED` | 必要 owner、source、rights、case or measurement unavailable | Executor reports; PM determines disposition |
| `READY_FOR_PM_REVIEW` | Evidence package complete and traceable; no PASS claim | Executor |
| `APPROVED` | PM／Owner accepts Evidence for the applicable Gate criterion | PM／Owner only |

`APPROVED` evidence does not by itself authorize implementation. Domain Selection and Gate 3 remain separate decisions.

### External Evidence Controls

- Preserve raw source、role、date、collection method、limitations and contradictions。
- Do not promote historical or Legacy assets merely because current evidence is blocked。
- Do not use Product tests as customer value measurements。
- Do not create a synthetic Domain Owner or professional acceptance record。
- Re-review preserved Contract／Technical／Scope evidence only when new external evidence changes their assumptions。

## 5. Python Promotion Boundary

### Approved Flow

```text
Python Discovery / Engineering Experiment
                  ↓
              Evidence
                  ↓
              PM Review
                  ↓
      Mainline Promotion Candidate
                  ↓
   Explicit Implementation Authorization
                  ↓
        C# Mainline Implementation
                  ↓
       Product Validation / Acceptance
```

### Promotion Meaning

`Mainline Promotion Candidate` only means the evidence is eligible for separate Product planning and Architecture review. It does not mean the Python artifact, algorithm or behavior has been promoted, approved, scheduled or accepted.

### Python MUST NOT

- Become a second PVOS Engine。
- Own Product Behavior Authority。
- Replace C#／.NET Mainline。
- Calculate or repair Placement、Geometry、capacity、warnings or Product results。
- Define a Domain Rule by implementation precedent。
- Automatically create a Mainline feature from an experiment。

### Promotion Requirements

- Evidence-backed problem and value。
- PM Review。
- Formal C# Mainline contract and Owner。
- Scope／Out of Scope and compatibility evidence。
- Gate 3 Implementation Authorization when required。
- C# implementation、Regression Evidence and Product Acceptance。

## 6. Gate 2 Hold Policy

### Hold Trigger

When any mandatory external Domain evidence is incomplete, unavailable, contradictory or lacks an accountable owner:

| Gate Item | Required State |
|---|---|
| Domain Selection | **HOLD** |
| Domain Result | **NOT REJECTED** unless PM explicitly rejects |
| Domain Acceptance | **NOT ACCEPTED** |
| Implementation Gate | **LOCKED** |

### Meaning of HOLD

`HOLD` means the candidate remains eligible for evidence recovery. It is neither approval nor rejection. Evidence already accepted or review-ready remains preserved; only incomplete／affected items are returned.

### Hold Controls

- No Domain-specific Issue Queue or implementation。
- No automatic switch to the next Domain candidate。
- No claim that market potential or Core fit compensates for missing Evidence Owner、customer workflow、cases、value or professional responsibility。
- No Gate 3 preparation unless PM／Owner explicitly authorizes it after Gate 2 approval。
- Mainline work inside existing approved Product boundaries remains governed by Workflow A and is not placed on global hold。

## 7. Non-Blocking Development Principle

### External Evidence MUST NOT Block

Subject to normal Planning、Execution and Review authorization, incomplete External Domain Evidence must not block:

- Core development inside existing approved Product Scope。
- Validation tooling that preserves C# authority。
- Regression improvement and failure isolation。
- Evidence automation and Result lineage。
- Engineering productivity support that does not calculate Product behavior。
- Maintenance and defect correction within accepted behavior, when separately authorized。

### Mandatory Wait Boundary

Domain-specific implementation must wait for the applicable Gate approval.

The following cannot proceed merely because Mainline is active:

- Rooftop Roof Rule、Obstacle、Walkway or Setback behavior。
- Ground Terrain／GIS／Road／Drainage behavior。
- Fishery Aquaculture／Water／Coexistence behavior。
- Domain-specific Structural、Electrical or Shading decisions。
- Domain case Promotion into Product authority。

### Non-Blocking Decision Test

Before treating work as independent of Gate 2, confirm all of the following:

1. The behavior already belongs to accepted PVOS Product Scope。
2. The work does not encode a Domain-specific assumption。
3. It does not depend on blocked external Evidence for correctness or acceptance。
4. C# Mainline remains Product authority。
5. Python remains Validation／Support only。
6. Normal Planning、Execution and Acceptance authority exists separately from this strategy。

If any answer is no or unknown, the work remains held pending PM Scope／Gate review.

## 8. Operating Status

| Operating Area | Current Status | Meaning |
|---|---|---|
| Gate 1 — Product Direction | **APPROVED WITH BOUNDARY CONDITIONS** | Core + Domain Modules and Dual-Line direction approved |
| Gate 2 — Rooftop | **EXTERNAL EVIDENCE HOLD** | Candidate preserved; six mandatory external gaps blocked |
| Workflow A — Product Mainline | **ACTIVE** | May receive separately authorized in-scope Product work; no authorization created here |
| Workflow B — External Evidence Track | **ACTIVE／BLOCKED ITEMS PRESENT** | Recovery may continue when owners and sources become available |
| Gate 3 — Implementation Authorization | **LOCKED** | No Rooftop-specific implementation or Gate 3 opening |
| Rooftop Domain | **NOT SELECTED／NOT ACCEPTED** | Gate 2 evidence incomplete |

## Current Decision Flow

```text
Gate 1 Product Direction
        APPROVED
            │
            ├──────── Workflow A: Mainline ACTIVE
            │          Existing Scope + Separate Authority
            │
            └──────── Workflow B: Rooftop Evidence HOLD
                            ↓
                    Recover External Evidence
                            ↓
                      PM Gate 2 Review
                            ↓
                  Gate 3 remains LOCKED
```

## Decision Controls

| Control | Confirmation |
|---|---|
| Mainline may continue without waiting for Domain Selection | CONFIRMED — existing Scope and separate authorization only |
| External Evidence cannot create Product behavior | CONFIRMED |
| Domain implementation waits for Gate approval | CONFIRMED |
| C#／.NET remains sole Product Behavior Authority | CONFIRMED |
| Python remains Validation／Engineering Support | CONFIRMED |
| Gate 2 Rooftop is Hold, not Rejected or Accepted | CONFIRMED |
| Gate 3 remains locked | CONFIRMED |

## Constraints Verification

| Constraint | Result |
|---|---|
| No code modification | PASS |
| No Issue Queue | PASS |
| Gate 3 not opened | PASS |
| No EOS modification | PASS |
| No Governance modification | PASS |
| No PVOS Scope modification | PASS |

## Strategy Status

**ACTIVE WITH BOUNDARY CONDITIONS**

**GATE 2 ROOFTOP — EXTERNAL EVIDENCE HOLD**

**GATE 3 — LOCKED**
