# PVOS Product Direction Decision Package

## Package Identity

| 欄位 | 內容 |
|---|---|
| Deliverable | `PVOS_PRODUCT_DIRECTION_DECISION_PACKAGE` |
| Purpose | 提供 PVOS 未來產品定位、核心架構方向與投資優先順序的 PM 決策基礎 |
| Decision State | PROPOSED — PENDING PM PRODUCT DIRECTION REVIEW |
| Basis Date | 2026-08-07 |
| Authority Boundary | 決策建議；不授權 Product Scope 變更、實作、Issue Queue 或投資承諾 |

## Source Basis and Evidence Status

| Source | Repository Evidence | 本文件使用方式 |
|---|---|---|
| PVOS 1.0 Product Accepted | `PM/PVOS_1_0_PM_PRODUCT_ACCEPTANCE_RECORD.md` | 已接受的 Deterministic Layout MVP 基準 |
| PVOS 1.1 Production Ready | `PM/PVOS_1_1_PRODUCTION_READINESS_DECISION_RECORD.md` | `APPROVED WITH BOUNDARY CONDITIONS` 的 Durable Decision |
| PVOS 1.2 Feature Expansion Accepted | 本次 PM 指令列為 Source Basis；Repository 有 PR #88 合併證據、Post-Acceptance Package 與後續證據，但本次檢查未找到獨立命名的 Durable PVOS 1.2 Acceptance Record | 視為 Owner／PM 提供的決策前提；不由本文件補造或改寫 Acceptance Record |
| Domain Market Strategy Review | `PM/PVOS_DOMAIN_MARKET_STRATEGY_REVIEW_PACKAGE.md` | 三領域相對適配、缺口與建議進入順序 |
| Current Core Capability Evidence | C# Core／Layout、Golden Dataset、Regression、Runtime、Result Package 與 Python Validation Evidence | 定義已證實能力與不得越界的限制 |

## Executive Decision Proposal

建議將 PVOS 定位為：

> **以確定性配置、可重現驗證及工程證據為核心的太陽光電配置引擎與工程決策證據產品。**

PVOS 應維持一個跨領域穩定的 Core，由 Domain Module 提供領域語意、規則及責任邊界。近期優先方向不是擴充成全能型太陽光電設計平台，而是先證明既有 Core 在單一市場領域中能可靠降低配置重作、結果不一致及工程證據斷裂。

候選首要驗證領域為 **Rooftop PV**；Ground Mount 為第二候選；Fishery PV 維持研究與證據蒐集。這是技術與市場驗證順序建議，不是最終商業選擇，也不授權任何 Domain Module 實作。

## 1. PVOS Vision Statement

### 長期產品定位

PVOS 長期應成為不同太陽光電工程領域可共同使用的 **Deterministic PV Layout and Evidence Core**：接收經領域責任人確認的工程輸入與可行區域，產生可重現的配置結果、驗證結果及可追溯 Evidence，供工程師、審查者與下游工具使用。

產品不以取代工程師為目的，而是把下列事項變成可治理、可比較及可重現的產品能力：

- 明確的幾何與配置輸入。
- 確定性的排列結果。
- 可隔離的驗證失敗。
- 輸入、規則、結果與版本的 Evidence Chain。
- 不重新計算產品結果的 Result Package 與 Presentation Boundary。

### 核心價值

1. **Determinism**：相同受控輸入與版本產生相同結果。
2. **Engineering Integrity**：Domain 規則、Core 計算與專業簽認責任不混淆。
3. **Traceability**：每個結果可追溯至輸入、規則、版本與驗證證據。
4. **Change Control**：工程修改可以比較，不必依賴人工記憶或不可重現的操作。
5. **Domain Extensibility with Boundaries**：以獨立 Domain Module 延伸，不將所有產業規則塞入 Core。

### 不追求的方向

在未經獨立 Direction、Scope 與 Implementation Gate 核准前，PVOS 不追求：

- 自動取代工程師或做無責任歸屬的 AI Design Decision。
- 通用 CAD、GIS、BIM 或專案管理平台。
- 完整結構、電氣、遮蔭、發電模擬、施工或養殖設計套件。
- Cloud、UI 或 API 平台本身。
- 第二套 PVOS Engine；Python 不取代 C# Mainline，也不計算 Placement。
- 透過 Legacy／Canonical Model Promotion 隱性擴張產品範圍。
- 同時進入 Rooftop、Ground Mount 與 Fishery 三個 Domain 的平行產品化。

## 2. Core Architecture Direction

### Architecture Principle

```text
Domain Evidence / Approved Engineering Input
                    ↓
           Domain Module Boundary
     semantics · rules · eligibility · ownership
                    ↓
                PVOS Core
 Geometry → Partition → Layout → Validation
                    ↓
        Evidence → Result Package
                    ↓
 Domain / Professional / Product Acceptance
```

此圖是方向性責任分界，不是新架構核准或實作規格。

### PVOS Core Responsibility

| Core Capability | 應承擔的長期責任 | 現有證據邊界 | 不承擔 |
|---|---|---|---|
| Geometry | 提供穩定、可驗證的幾何資料與運算基礎 | `Point2D`、`Polygon2D`、GeometrySet、Local Axis 與受控幾何驗證 | 地形語意、屋頂語意、魚塭語意、測量正確性 |
| Partition | 表示已被領域流程核准的配置分區與選擇 | 明確 Partition 與 unknown selection rejection | 自行決定土地、屋頂或魚塭的合法可用區 |
| Layout | 依明確軸向、模組參數、間距與 Margin 產生確定性 Placement | C# `LayoutEngine`、穩定順序、Stable IDs | 發電最佳化、結構設計、電氣設計、遮蔭決策 |
| Validation | 驗證 Core 輸入、輸出、完整性及已核准的產品規則 | C# tests、Golden Regression、Python 外部 Evidence validation | 將外部專業判斷轉成未核准 Product Rule |
| Evidence | 保存輸入、結果、版本、驗證與受影響 Claim | Golden manifests、SHA-256、repeatability evidence | 取代主管機關、專業技師或 Domain Owner 的核准 |
| Result Package | 封裝既有產品結果與 Evidence 參照，供受控消費 | Read-only、lineage、presentation no-recalculation boundary | 新增計算、重新解讀 Placement、隱性建立 API 承諾 |

### Domain Module Responsibility

每個 Domain Module 必須在資料進入 Core 前，承擔該市場的語意與規則責任：

| 責任 | Domain Module 必須定義 |
|---|---|
| Domain Data | 屋頂、土地、地形、魚塭、水域、障礙、道路等資料語意、來源與版本 |
| Eligibility | 哪些區域可成為 Core 的 accepted feasible region，以及核准者 |
| Domain Rules | 退縮、走道、地形、養殖、遮蔭或其他領域限制的適用條件 |
| Ownership | 規則 Owner、資料 Owner、專業簽認者與變更批准者 |
| Translation | Domain Data 如何轉為 Core Geometry、Partition、Parameters 與 Constraints |
| Domain Validation | Core Result 如何回到領域情境檢查，不改寫 Core Result |
| Evidence Admission | 真實案例、規則版本與結果如何進入受控證據基準 |

### Mandatory Boundary Rules

- Core 只處理已核准的明確輸入，不推測土地、屋頂或養殖合法性。
- Domain Module 不應複製 Layout Engine；跨 Domain 共用計算留在 Core。
- Domain Validation 可判定 Result 是否適用，但不可在 Presentation 或 Evidence 階段重算 Placement。
- Electrical、Shading、Structural、Terrain 及 Aquaculture 是獨立專業責任候選，不因資料可表示為 Polygon 就自動成為 Core 能力。
- 任一 Domain Module 進入產品基準前，必須通過本文件 Gate 1 至 Gate 3。

## 3. Domain Strategy

### Comparative Assessment

| 評估面向 | Rooftop PV | Ground Mount PV | Fishery PV |
|---|---|---|---|
| Market Fit | 高：台灣既有市場基礎明確，排版修改與文件一致性有可驗證痛點 | 高潛力：大型場址、分區與版本管理價值明顯 | 專業利基：有差異化機會，但受養殖事實、政策及個案條件高度約束 |
| Core Fit | **高**：最接近現有二維 Boundary、Partition、Layout、Evidence | **中**：平面分區可用，但地形與多系統協調是重大缺口 | **低至中**：幾何與 Evidence 可用，但不足以形成漁電設計能力 |
| Domain Gap | Roof Boundary、Obstacle、女兒牆、走道、退縮、結構、電氣、遮蔭 | Terrain、GIS／CAD、道路、排水、緩衝、施工分區、電氣、遮蔭 | Aquaculture、魚塭水系、養殖操作、遮蔭／環境、法規、跨專業責任 |
| Development Complexity | 中 | 高 | 極高 |
| Evidence Readiness | 中：Core 證據充足；缺真實 admitted rooftop workflow evidence | 低至中：缺 terrain／GIS／大型場址 contract evidence | 低：缺 Domain Owner、個案規則與責任證據 |
| 主要錯誤風險 | 把排列誤稱結構／電氣／遮蔭合規 | 把平面配置誤稱完整場址工程 | 把固定遮蔽率或幾何配置誤稱農電共生合規 |
| 建議狀態 | 第一候選；進入 Domain Selection Review | 第二候選；先做 Feasibility／Data Contract Research | Research Only；不進 Implementation Selection |

### Rooftop PV Direction

建議以 bounded workflow 驗證：由具責任的工程資料提供屋頂 Boundary、排除區及參數，PVOS 產生可重現 Layout、變更比較與 Result Evidence。

進入 Domain Selection 前仍須取得：

- 合法且去識別的代表案例。
- Roof／Obstacle／Walkway／Setback 的候選資料契約與 Owner。
- 目前改圖工時、返工、文件錯配的基準數據。
- 工程師對 Result Package 與 Evidence 的實際使用驗證。

### Ground Mount Direction

Ground Mount 應被視為 Core 的第二個可擴展候選，而不是 Rooftop 的放大版。其前置研究應集中在 Terrain、座標系、測量／GIS 來源、道路、排水、施工分區及跨工具版本責任。

在這些契約未成立前，不應授權大型場址自動配置或宣稱完整地面型工程能力。

### Fishery PV Direction

Fishery PV 應維持獨立 Evidence Collection Track。進入產品方向候選至少需要：具資格的 Aquaculture Domain Owner、實際養殖工作流、個案核准規則、遮蔭／水域／維護條件與多角色責任矩陣。

在上述條件未滿足前，PVOS 只可被描述為可能提供 Geometry、Layout 與 Evidence 底座，不可被定位為漁電共生設計產品。

## 4. Market Entry Strategy

### Technical Validation Order

1. **Core Evidence Baseline Preservation**：先維持 C# Mainline、Golden、Regression、Result Package 及 Python Support boundary。
2. **Rooftop Domain Contract Validation**：先驗證資料、規則、責任與 Evidence，不直接進入功能開發。
3. **Rooftop Bounded Product Validation**：只有 Gate 2 通過後，才可提出小範圍 Implementation Authorization。
4. **Ground Mount Feasibility**：以 GIS／Terrain／版本契約研究為主，避免複製 Engine。
5. **Fishery Domain Evidence Collection**：取得 Domain Owner 與真實案例後再重評。

### Commercial Opportunity Assessment

| 商業問題 | 目前證據 | Decision Impact |
|---|---|---|
| 市場是否存在 | 三個領域皆有實際工程活動；Domain Review 對台灣官方資料已有證據 | 可支持 Discovery，不足以支持營收預測 |
| 痛點是否重要 | 排版修改、跨文件一致性與 Evidence 斷裂具工程合理性 | 需用訪談、工時與返工數據量化 |
| 誰是付費者 | 未有 Repository 證據 | Gate 2 前必須確認業主、EPC、設計顧問或其他角色 |
| 願付價格／ROI | 未有證據 | 不得形成投資回收承諾 |
| 導入成本 | CAD／GIS／流程整合與 Domain Rule 成本尚未量化 | Ground／Fishery 風險尤其高 |
| 競品轉換理由 | 專用 PV 軟體、CAD、GIS 與自製工具共同存在 | 必須證明 PVOS 的 Evidence／Determinism 差異可被客戶感知 |

### Company Strategic Fit

已證實的公司／產品優勢是 C# 確定性 Layout、清楚資料契約、Golden Regression、Evidence-first 與 no-recalculation Result boundary。未證實的能力包括領域銷售通路、屋頂結構／電氣服務、地面型土木／GIS 交付及養殖專業。

因此推薦順序是「證據最接近、領域缺口最小」的技術驗證次序，而不是最終商業市場選擇。最終 Domain Selection 必須加入客戶、價格、導入成本與公司人才證據。

## 5. 12 Months Roadmap Candidates

本節為四個季度的候選決策序列，不代表日期承諾、人力承諾或 Implementation Authorization。

| 候選期間 | Core Evolution | Domain Validation | Tool Evolution | Integration Research | Exit Evidence |
|---|---|---|---|---|---|
| Months 1–3 | 保持 Core baseline；盤點 Geometry／Partition／Validation contract 缺口 | Rooftop 使用者與資料流程 Discovery；建立候選 Rule／Owner matrix | Python validator 使用流程、報告與維護責任評估 | CAD input／output 與版本責任研究 | Direction evidence、客戶痛點基準、Domain Selection Package |
| Months 4–6 | 僅在 Gate 3 核准後評估 bounded contract evolution | Rooftop admitted cases 與 bounded validation candidate | Result Package versioning／consumer boundary review | CAD exchange feasibility；不建立未批准 Adapter | 可重現案例、Evidence chain、使用者價值驗證 |
| Months 7–9 | 依已接受 Rooftop evidence 決定是否需要共用 Core 改進 | Rooftop acceptance preparation；Ground Terrain／GIS feasibility | Golden coverage 與失敗隔離改善候選 | GIS、座標、Terrain data contract research | Rooftop acceptance evidence 或明確停止決定；Ground feasibility disposition |
| Months 10–12 | 維持單一 C# Engine 與跨域責任分界 | 決定 Ground 是否進下一 Gate；Fishery 只做 Domain evidence readiness review | Evidence automation 的維護與採用成效檢查 | 不形成 Electrical／Shading／Cloud／UI 承諾 | 下一年度投資決策、保留／停止／擴展建議 |

### Candidate Workstreams

#### Core Evolution

- 保護現有 deterministic behavior 與 backward evidence traceability。
- 評估 Geometry／Partition contract 是否足以接收 Domain-approved feasible regions。
- 維持 Validation failure isolation、Golden admission 與 Result lineage。
- 任何新通用 Constraint 能力都必須證明跨 Domain 共性，不能由單一領域規則直接提升為 Core。

#### Domain Validation

- Rooftop：Boundary、Obstacle、Walkway、Setback、Owner、Evidence Admission。
- Ground：Terrain、GIS、道路、排水、施工分區與座標／版本責任。
- Fishery：養殖營運、法規版本、遮蔭、水域與責任 Evidence；Research Only。

#### Tool Evolution

- Python 保持 Validation／Support Track，只觀察 C# 結果與 Evidence。
- Result Package 可研究版本、相容性、consumer boundary；不自動形成 API。
- 工程使用流程、報告可讀性與 repeatability 可以驗證，但不得新增 Product calculation。

#### Integration Research

- CAD／DXF／DWG 與 GIS 資料的來源、座標、單位、圖層、版本及授權。
- 不在研究階段承諾 AutoCAD Full Integration、Cloud、UI、Electrical 或 Shading implementation。
- Integration 必須維持 Adapter／Domain／Core 分界，不把外部交易或資料庫責任帶入 Core。

## Dual-Line Development Strategy

### Strategic Model

PVOS 應採取兩條協調發展線，但兩者的產品權限並不對等：

```text
Line 1 — C# / .NET Mainline
Product Behavior Authority · Production Features · Domain Modules
Release Capability · Product Acceptance Basis
                         ↑
                  Promotion Gate only
                         ↑
Line 2 — Python Validation / Engineering Support Track
Rapid Validation · Evidence · Regression Support
Engineering Experiments · Field Support Tools
```

| 發展線 | 技術 | 正式責任 | 明確禁止 |
|---|---|---|---|
| Line 1 — PVOS Mainline Product | C#／.NET | Product Behavior Authority、Production Features、Domain Modules、Release Capability、Product Acceptance 執行基礎 | 不得未經 Gate 吸收研究原型、未核准 Domain Rule 或 Legacy 行為 |
| Line 2 — Validation／Engineering Support Track | Python | Rapid Validation、Evidence generation、Regression support、Engineering experiments、Field support tools | 不得取代 C# Mainline、不得成為第二 PVOS Engine、不得擁有 Product Behavior Authority、不得計算或修復 Placement |

兩條線的協調原則是：Mainline 產生產品行為與結果；Validation Track 觀察、檢查、比較並包裝既有產品 Evidence。Python 產生的發現可以成為 Mainline 變更候選的證據，但永遠不能因為原型可執行就自動取得產品權限。

### 1. Mainline Roadmap

#### Core Evolution

- 維持 C#／.NET 為 Geometry、Partition、Layout、Validation、Evidence lineage 與 Result Package 的唯一 Product Behavior Authority。
- Core 的任何演進必須保存 deterministic behavior、Stable IDs、Golden Regression 與 failure isolation。
- 只有能證明跨 Domain 共性且通過 Architecture／PM Review 的能力，才可列為 Core evolution candidate。
- Python experiment、Legacy asset 或單一 Domain convenience 不得直接提升為 Core behavior。

#### Domain Expansion

- Domain Module 的 production implementation 只能位於 Mainline 授權範圍，並遵守 Core／Domain responsibility boundary。
- 建議驗證順序仍為 Rooftop、Ground Mount、Fishery；這是 Gate sequence，不是三域 implementation commitment。
- 每次只選一個 Domain 通過 Gate 2；其他領域保持 Research／Deferred。
- Domain Rule、資料 translation、Owner 與專業簽認在 Gate 3 前必須完整。

#### Production Capability Development

- Production Feature 必須有 C# Mainline contract、測試、Golden／Regression Evidence、Result lineage 與 release boundary。
- Release Candidate 只能由 Mainline 建立，並由 PM 依 Gate 4 判定 Product Acceptance。
- CLI、Runtime、Domain Module 或未來 Adapter 均不得繞過 Mainline Product Behavior Authority。

### 2. Validation Track Roadmap

#### Python Validation Tools

- 持續檢查 C# CLI、靜態 Golden assets、manifest、hash、結果欄位與 repeatability。
- 改善可重複執行、失敗定位、受影響 Claim 隔離及工程師使用流程。
- 工具輸出只能描述觀察到的 C# 結果與 Evidence；不得生成應由 Product Engine 計算的面板、容量、錯誤或警告。

#### Evidence Automation

- 候選方向包括 deterministic fingerprint、報告產生、Evidence index、provenance 與保留政策。
- 自動化必須保留每個檢查的 identity、原始結果與 FAIL／BLOCKED，不得用彙總報告掩蓋失敗。
- Evidence automation 不得變成 Product database、canonical schema 或 release authority。

#### Regression Automation

- 對已 admitted Golden scenarios 執行 integrity、repeatability 與 evidence comparison。
- 擴充 scenario 必須先通過 Evidence Admission，不得由 Python 工具自行授權新 Product Behavior。
- Python regression failure 應指出受影響 Claim，最終 Product correction 與 acceptance 仍由 C# Mainline 流程承擔。

#### Engineering Productivity and Field Support

- 可評估批次驗證、現場 Evidence 收集、輸入完整性檢查、差異報告與診斷輔助。
- Field Support Tool 必須標示非產品計算、資料來源、適用版本及輸出限制。
- Engineering experiment 的目的是降低不確定性；未經 Promotion Gate 不得交付為正式 Product Feature。

### 3. Promotion Boundary

```text
Validation Track Candidate
          ↓
Evidence Proven
          ↓
PM Review
          ↓
Mainline Promotion Candidate
          ↓
Gate 3 — Explicit Implementation Authorization
          ↓
C# Mainline Implementation + Regression Evidence
          ↓
Gate 4 — Product Acceptance
```

`Mainline Promotion Candidate` 只代表有資格進入 Mainline 規劃審議，不代表已 Promotion、已排程或已取得 Product Behavior Authority。

Promotion 的最低條件：

1. 問題與價值有可追溯 Evidence，不只是一個可執行 Python prototype。
2. 候選行為有正式 C# Mainline contract、Owner、Scope、Out of Scope 與相容性分析。
3. 沒有複製 Layout／Geometry／Product calculation，且不形成第二 Engine。
4. PM 明確審查；若涉及 Scope 或 Architecture 變更，另取得所需 Authority。
5. 通過 Gate 3 後才可在 C# Mainline 實作；通過 Gate 4 後才取得 Product Acceptance。

### Dual-Line 12-Month Coordination Candidates

| 候選期間 | Mainline | Validation／Support Track | Coordination Gate |
|---|---|---|---|
| Months 1–3 | 保存 Core baseline；釐清 Rooftop contract gap | 強化 repeatability、Evidence report 與工程使用流程 | Gate 1 Direction Approval；準備 Gate 2 evidence |
| Months 4–6 | 只在 Gate 3 後執行 bounded C# candidate | 對 admitted cases 做外部驗證與差異報告 | Promotion Candidate Review；無自動 Promotion |
| Months 7–9 | 維持 single-engine regression；準備 bounded release evidence | 擴充 regression automation 與 field evidence support | Mainline／Python 結果一致性審查 |
| Months 10–12 | 依 Gate 4 結果決定 release／retain／stop | 評估工具採用、維護成本及下一批 evidence gaps | Product Acceptance 與下一年度投資決策 |

## 6. Investment Priority

### Evaluation Scale

- Value：對客戶痛點與產品差異化的候選價值。
- Effort：取得資料、領域規則、工程實作與維護的相對投入。
- Risk：技術、責任、法規及 Scope 風險。
- Evidence Readiness：目前可支持下一個決策的證據程度。

| Priority Candidate | Value | Effort | Risk | Evidence Readiness | 建議 Disposition |
|---|---:|---:|---:|---:|---|
| Core Evidence／Regression preservation | 高 | 低至中 | 低 | 高 | **P0 保持**；所有方向的共同基礎 |
| C# Mainline Product Authority／release integrity | 高 | 中 | 低至中 | 高 | **P0 保持**；唯一產品行為與 Release 路徑 |
| Python Validation／Evidence Automation | 中至高 | 中 | 低至中 | 高 | **P1 候選**；Support Track only，受 Promotion Boundary 約束 |
| Rooftop Domain Discovery／Contract Validation | 高 | 中 | 中 | 中 | **P1 候選**；進 Gate 2 審議 |
| Result Package／Validation Tool engineering usability | 中至高 | 中 | 低至中 | 高 | **P1 候選**；不得形成 API 或第二 Engine |
| Customer／Workflow／ROI Evidence Collection | 高 | 中 | 低 | 低 | **P1 必要**；補足商業決策缺口 |
| Ground Terrain／GIS Feasibility | 高潛力 | 高 | 高 | 低至中 | **P2 Research**；Rooftop validation 後再決定 |
| Fishery Domain Evidence／Owner readiness | 未確定 | 高 | 極高 | 低 | **P3 Research Only** |
| Electrical／Shading／Structural implementation | 未經核准 | 極高 | 極高 | 低 | **Defer**；需獨立方向與責任決策 |
| UI／Cloud／Full AutoCAD integration | 未經證實 | 高 | 高 | 低 | **Defer**；目前不是方向核心 |

### Recommended Investment Logic

先投資 Evidence readiness 與單一 Domain validation，再投資功能。任何高價值但低 Evidence readiness 的項目，只能取得研究預算候選，不應直接取得 Implementation Authorization。

## 7. Risk Assessment

| Risk Category | 風險 | 可能影響 | 控制方式 | Gate Owner |
|---|---|---|---|---|
| Technical | Domain Module 複製 Layout 邏輯，形成第二 Engine | 結果分歧、維護與驗證成本增加 | 單一 C# Core；Domain 只做語意、eligibility 與 translation | Architecture／PM |
| Technical | Result Package、Python 或 Presentation 重算／修復產品結果 | 破壞 Evidence lineage | No-recalculation audit、field lineage、repeatability tests | PM Verification |
| Technical | Python 快速原型逐步取得未授權 Product Behavior Authority | 形成第二 Engine、C#／Python 結果分歧 | 明確 Line ownership、source audit、Promotion Gate、C# Mainline-only implementation | Architecture／PM |
| Technical | Validation automation 的摘要掩蓋個別 FAIL 或改寫 Evidence | 錯誤判定 readiness／acceptance | Stable check identity、raw result retention、failure isolation | PM Verification |
| Technical | CAD／GIS 單位、座標、圖層或版本失真 | 錯誤配置與不可追溯輸入 | 明確 data contract、source identity、conversion evidence | Domain／Integration Owner |
| Domain Knowledge | 屋頂規則、地形或養殖條件被過度簡化 | 不合規、不安全或無法營運 | 合格 Domain Owner、規則來源與適用條件 | Domain Owner |
| Domain Knowledge | Core Geometry 被誤認為結構／電氣／遮蔭結論 | 專業責任越界 | 輸出聲明、獨立 validation 與簽認 | PM／Professional Owner |
| Market Validation | 痛點存在但付費者、ROI 或採用流程不成立 | 投資無法商業化 | 訪談、工時／返工基準、paid pilot criteria | Product／Commercial Owner |
| Market Validation | 競品已涵蓋客戶所需工作流 | 差異化不足 | 比較 Evidence、determinism、導入成本與 switching reason | Product Owner |
| Scope Expansion | 同時開三個 Domain 或加入 UI／Cloud／Electrical | 稀釋 Core、延後可驗證結果 | One Domain at a Time；Gate 3 明確 changed-scope approval | Owner／PM |
| Scope Expansion | Research 文件被當成 Implementation commitment | 未授權工作進入 Queue | Package status、Gate、Issue source 與 acceptance 分離 | PM |
| Evidence | PVOS 1.2 Acceptance 缺少本次檢查可辨識的獨立 Durable Record | Source traceability 弱於 1.0／1.1 | PM 確認既有決策來源；本文件不補造紀錄 | PM |

## 8. Decision Gates

### Gate 1 — Product Direction Approval

**Decision Question**：是否批准 PVOS 以 Deterministic Layout and Evidence Core 為長期定位，並採 Core／Domain Module 分層方向？

**Required Evidence**：

- PVOS 1.0／1.1／1.2 現況與邊界可追溯。
- Vision、非目標、Core／Domain 責任及主要風險獲 Owner／PM 確認。
- Dual-Line 模型獲確認：C#／.NET 是唯一 Product Mainline；Python 是 Validation／Engineering Support Track。
- Python 不得取代 Mainline、成為第二 Engine 或擁有 Product Behavior Authority。
- 明確聲明本 Gate 不改變 Product Scope、不授權 Implementation。

**Allowed Outcomes**：`APPROVED`、`APPROVED WITH CONDITIONS`、`RETURNED FOR EVIDENCE`、`REJECTED`。

### Gate 2 — Domain Selection

**Decision Question**：在 Rooftop、Ground Mount 或 Fishery 中，哪一個 Domain 值得進入 bounded product validation？

**Required Evidence**：

- 具代表性的客戶／工程工作流與痛點證據。
- 付費者、導入者、價值指標與競品轉換理由。
- Domain Data、Rule、Owner、Professional Responsibility 與 Evidence matrix。
- Value／Effort／Risk／Evidence Readiness 比較。
- 單一 Domain 選擇；其他 Domain 保持 Research／Deferred。
- 定義該 Domain 的 Mainline responsibility 與 Validation Track evidence responsibility，禁止兩線重複 Product calculation。

**目前建議**：Rooftop 為第一候選，但在上述市場與責任證據補齊前不得視為最終商業決定。

### Gate 3 — Implementation Authorization

**Decision Question**：是否授權一個明確、bounded、可驗收的 Implementation Package？

**Required Evidence**：

- Gate 1 與 Gate 2 已核准。
- Scope、Out of Scope、Architecture Contract、Dependencies 與 Owner 完整。
- Acceptance Criteria、Golden Evidence、Regression、rollback／failure isolation 明確。
- 已證明不建立第二 Engine、不隱性 Promotion Legacy／Canonical assets。
- Validation Track 候選已完成 Evidence Proven 與 PM Review；Python prototype 本身不作為 Product implementation。
- 所有 Product Behavior、Production Feature 與 Domain Module 均指定在 C# Mainline 實作與驗收。
- 經明確 Authority 建立 Planning Package 與 Execution Queue；研究文件本身不能觸發實作。

**禁止**：由本文件直接產生 Issue、Code、Commit 或 Implementation Commitment。

### Gate 4 — Product Acceptance

**Decision Question**：被授權的 bounded capability 是否以證據證明符合 Product Acceptance？

**Required Evidence**：

- Accepted requirements 與實際結果逐項 mapping。
- C# Mainline tests、Golden／Regression、repeatability 與 Result lineage 全部可重現。
- Product Behavior 可追溯至 C# Mainline；Python 只提供獨立 Validation／Evidence，不是 acceptance authority。
- 若候選源自 Validation Track，需證明已依 Promotion Boundary 重新形成 Mainline contract、implementation 與 regression evidence。
- Domain Owner／使用者驗證及未解風險完整。
- Product Scope 與既有 PVOS 1.0／1.1／1.2 Acceptance 不被隱性改寫。
- PM 做 Product Acceptance；執行者不得自行宣告 Accepted。

## PM Decision Matrix

| Decision Item | Proposed Decision | Confidence | 仍缺 Evidence |
|---|---|---|---|
| Long-term positioning | Deterministic PV Layout and Engineering Evidence Product | 高（技術方向） | 客戶對此價值主張的商業驗證 |
| Core architecture | Geometry、Partition、Layout、Validation、Evidence、Result Package | 高 | 未來 contract evolution 仍須逐項 Gate |
| Domain architecture | Domain Module 承擔語意、規則、eligibility、ownership 與 translation | 高（責任方向） | 各 Domain 的正式 Owner 與 contract |
| First validation domain | Rooftop PV | 中 | 客戶、ROI、案例、Roof Rule ownership |
| Second domain | Ground Mount PV | 中低 | Terrain／GIS feasibility、導入成本 |
| Fishery direction | Research／Evidence Collection only | 高 | Aquaculture owner、真實 workflow 與法規責任證據 |
| 12-month plan | Gate-driven candidate roadmap | 中 | 人力、預算、商務時程與 Gate decisions |

## Recommended PM Disposition

建議 PM 對本 Package 採以下裁決方式：

1. **Gate 1：審議並決定是否批准 Product Direction。**
2. 若 Gate 1 通過，只授權準備 Gate 2 所需的 Rooftop Domain 與 Market Evidence。
3. 在 Gate 2 前，不建立 Domain Implementation Queue。
4. Ground Mount 保持第二候選研究；Fishery 保持 Evidence Collection Only。
5. 任何 Core、Domain、Tool 或 Integration 變更均需獨立 Gate 3 授權。

## Constraint Verification

| Constraint | Result |
|---|---|
| No code modification | PASS — 本 Package 僅新增 PM 決策文件 |
| No GitHub Issue Queue | PASS |
| No implementation commitment | PASS — 所有 Roadmap 項目均為候選且受 Gate 控制 |
| No EOS modification | PASS |
| No Governance modification | PASS |
| No Product Scope modification | PASS — 方向建議不改寫既有 Scope／Acceptance |

## Related Documents

- `PM/PVOS_1_0_PM_PRODUCT_ACCEPTANCE_RECORD.md`
- `PM/PVOS_1_1_PRODUCTION_READINESS_DECISION_RECORD.md`
- `PM/PVOS_1_2_POST_ACCEPTANCE_PLANNING_PACKAGE.md`
- `PM/PVOS_DOMAIN_MARKET_STRATEGY_REVIEW_PACKAGE.md`
- `PM/PRODUCT_BASELINE.md`
- `PRODUCT/PVOS_RUNTIME_RESULT_PACKAGE_EVOLUTION.md`
- `VALIDATION/GOLDEN_DATASET_NEXT_PHASE_EVIDENCE.md`
- `VALIDATION/REGRESSION_VALIDATION_PACKAGE.md`
- `VALIDATION/PYTHON_VALIDATION_TOOL_EVOLUTION_EVIDENCE.md`

## Package Status

READY_FOR_PM_PRODUCT_DIRECTION_REVIEW
