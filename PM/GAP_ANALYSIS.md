# Gap Analysis

PM-001 records evidence gaps and governance gaps only. It does not prescribe new architecture or implementation.

| ID | Gap | Evidence | Impact | Required follow-up class |
|---|---|---|---|---|
| GAP-001 | Most historical product and architecture documents are absent from PvLayoutPlugin `main` and exist only on long-lived branches. | [main docs](https://github.com/8nt7h6k229-png/PvLayoutPlugin/tree/main/docs), [V5.3 branch docs](https://github.com/8nt7h6k229-png/PvLayoutPlugin/tree/feature/v5.3-placement-v2-analyzer/docs) | Default branch is not a complete knowledge base. | PM disposition/recovery issue |
| GAP-002 | PVOS platform bootstrap is tagged and branch-only, not merged to `main`. | [platform tag](https://github.com/8nt7h6k229-png/PvLayoutPlugin/tree/v0.1.0-platform-bootstrap), [branch](https://github.com/8nt7h6k229-png/PvLayoutPlugin/tree/feature/pvos-platform-bootstrap) | Mature validation, dataset, ADR and governance assets are isolated. | PM review |
| GAP-003 | Open PRs #1, #6, #7 and #8 have no recorded disposition; this was already identified by governance issue #16. | [issue #16](https://github.com/8nt7h6k229-png/PvLayoutPlugin/issues/16) | Baseline status remains ambiguous. | Existing governance action |
| GAP-004 | PR #7 targets feature branch `feature/plugin-v07-geometry-integration`, not `main`. | [PR #7](https://github.com/8nt7h6k229-png/PvLayoutPlugin/pull/7) | Testing knowledge depends on unresolved PR #6. | PM dependency review |
| GAP-005 | All queried branches report unprotected. | [repository branches](https://github.com/8nt7h6k229-png/PvLayoutPlugin/branches), [issue #16](https://github.com/8nt7h6k229-png/PvLayoutPlugin/issues/16) | Documented workflow is not demonstrably enforced by repository policy. | Governance verification |
| GAP-006 | PVOS had no PR history before PM-001, while `feature/geometry-core` is ahead of `main`. | [PVOS pulls](https://github.com/8nt7h6k229-png/PVOS/pulls?q=is%3Apr), [geometry branch](https://github.com/8nt7h6k229-png/PVOS/tree/feature/geometry-core) | Geometry work is not reviewed/merged through the documented workflow. | PM disposition |
| GAP-007 | AIENV-002 issue #23 remains open although PR #25 is merged. | [issue #23](https://github.com/8nt7h6k229-png/PvLayoutPlugin/issues/23), [PR #25](https://github.com/8nt7h6k229-png/PvLayoutPlugin/pull/25) | Issue/implementation lifecycle is inconsistent. | Issue closure review |
| GAP-008 | Open Method Intelligence issue #11 overlaps closed issue #12 and merged PR #17. | [issue #11](https://github.com/8nt7h6k229-png/PvLayoutPlugin/issues/11), [issue #12](https://github.com/8nt7h6k229-png/PvLayoutPlugin/issues/12), [PR #17](https://github.com/8nt7h6k229-png/PvLayoutPlugin/pull/17) | Duplicate intent remains in open backlog. | Issue disposition |
| GAP-009 | Original RI commits remain on `recovery/ri-002-reference-preservation` after recovery copies were merged through PRs #17–#21. | [recovery branch](https://github.com/8nt7h6k229-png/PvLayoutPlugin/tree/recovery/ri-002-reference-preservation), [issue #15](https://github.com/8nt7h6k229-png/PvLayoutPlugin/issues/15) | Evidence is preserved but branch purpose/retention is undocumented. | Recovery retention decision |
| GAP-010 | Two ADR numbering namespaces (`docs/architecture/adr` and `docs/adr`) overlap. | [historical ADRs](https://github.com/8nt7h6k229-png/PvLayoutPlugin/tree/feature/v5.3-placement-v2-analyzer/docs/architecture/adr), [platform ADRs](https://github.com/8nt7h6k229-png/PvLayoutPlugin/tree/feature/pvos-platform-bootstrap/docs/adr) | ADR identifiers are ambiguous outside branch context. | Knowledge-governance classification |
| GAP-011 | Two Architecture Bible variants coexist without default-branch authority. | [architecture tree](https://github.com/8nt7h6k229-png/PvLayoutPlugin/tree/feature/v5.3-placement-v2-analyzer/docs/architecture) | Readers cannot infer an approved canonical version. | PM review, no automatic merge |
| GAP-012 | PVOS and PvLayoutPlugin both contain PVOS geometry/layout assets, but no default-branch portfolio document defines repository ownership. | [PVOS](https://github.com/8nt7h6k229-png/PVOS), [PvLayoutPlugin geometry](https://github.com/8nt7h6k229-png/PvLayoutPlugin/tree/main/src/r5d_src/PVOS.Geometry) | Cross-repository source-of-truth boundary is unclear. | Product ownership decision |
| GAP-013 | No explicit DXF Import asset was recovered from repositories, issues, PR titles or document paths. | [code search](https://github.com/8nt7h6k229-png/PvLayoutPlugin/search?q=DXF&type=code), [issue #10](https://github.com/8nt7h6k229-png/PvLayoutPlugin/issues/10) | Required knowledge category has no verified asset. | Evidence search / backlog classification |
| GAP-014 | No explicit DXF Export asset was recovered from repositories, issues, PR titles or document paths. | [code search](https://github.com/8nt7h6k229-png/PvLayoutPlugin/search?q=DXF&type=code) | Required knowledge category has no verified asset. | Evidence search / backlog classification |
| GAP-015 | The 261-document branch union has no single default-branch index. | [portfolio inventory](GITHUB_PORTFOLIO_ASSET_INVENTORY.md), [branches](https://github.com/8nt7h6k229-png/PvLayoutPlugin/branches) | Discovery currently requires branch archaeology. | PM-001 provides the first cross-repository index |
| GAP-016 | Governance incident records emergency direct-to-main commits. | [incident report](https://github.com/8nt7h6k229-png/PvLayoutPlugin/blob/main/PM/INCIDENT_2026-07-31_GOVERNANCE_GAP.md), [issue #16](https://github.com/8nt7h6k229-png/PvLayoutPlugin/issues/16) | Historical workflow contains an explicit exception. | Preserve exception evidence |

## Definition-of-done coverage

| Required inventory | Result |
|---|---|
| Repository | Complete for the two named repositories |
| Branch | Complete for all GitHub branches visible on 2026-08-03 |
| Issues | Complete for all issues visible on 2026-08-03 |
| Pull requests | Complete for all PRs visible on 2026-08-03 |
| Documents | Classified across the full branch union; authoritative tree links retained |
| Architecture | Indexed by family, branch and ADR collection |
| Product knowledge | Classified by requested and recovered domains |
| AI knowledge | AI Studio, Repository Intelligence and AI specifications indexed |
| Governance | Governance documents, templates, issue and incident indexed |
| Recovery program | Issue #15, recovery branch and merged recovery PRs indexed |
| Gap analysis | Completed above |

Completion means inventory coverage, not resolution of the recorded gaps.
