# Branch Recovery Index

This index covers every `develop`, `feature/*`, and `recovery/*` branch visible on GitHub on 2026-08-03. `agent/*` delivery branches are excluded from product-knowledge scope.

## Recovery decisions

| Repository / branch | Head | Main relationship | Knowledge | Classification | PM recovery disposition |
|---|---|---|---|---|---|
| PVOS `develop` | [`f6120ee`](https://github.com/8nt7h6k229-png/PVOS/commit/f6120eefb6eae89c220c7303a4d4d40fe7a0538a) | 0 ahead; same head as `main` | No unique knowledge | Deprecated for independent recovery | No recovery required; retain/delete only by separate governance decision |
| PVOS `feature/geometry-core` | [`1323988`](https://github.com/8nt7h6k229-png/PVOS/commit/13239884c85609faccb59dcd9d1be1a32c23fe71) | 3 commits ahead | Point2D, Vector2D, BoundingBox, Line2D | Branch-only / Experimental; [issue #1](https://github.com/8nt7h6k229-png/PVOS/issues/1) open | Recover knowledge; do not copy code under PM-002 |
| PvLayoutPlugin `develop` | [`aaa9c58`](https://github.com/8nt7h6k229-png/PvLayoutPlugin/commit/aaa9c582e1be6b0e285c4fecd09d32903518e01e) | 0 ahead; fully ancestor of `main` | No unique branch knowledge | Deprecated for independent recovery | No recovery required |
| `docs/pvos-testing-platform` | [`2173d27`](https://github.com/8nt7h6k229-png/PvLayoutPlugin/commit/2173d27eadf16d7573e02eef4ba6ce8b579735cd) | 2 ahead; 13 changed documents | Architecture specification plus testing strategy, matrix, CI and runtime validation | Branch-only / Experimental; [PR #7](https://github.com/8nt7h6k229-png/PvLayoutPlugin/pull/7) open | Recover as one knowledge set; includes predecessor architecture branch by ancestry |
| `feature/ai-studio-foundation` | [`15f8286`](https://github.com/8nt7h6k229-png/PvLayoutPlugin/commit/15f8286c88e6d3022208fd86ef2105e50613cc66) | 0 ahead; fully merged by [PR #9](https://github.com/8nt7h6k229-png/PvLayoutPlugin/pull/9) | AI Studio foundation | Main / Deprecated branch | No branch recovery required |
| `feature/construction-intelligence` | [`0106f22`](https://github.com/8nt7h6k229-png/PvLayoutPlugin/commit/0106f220e0ffe65e3dcd46fee5a5c4078dc57151) | 86 ahead; same head as `feature/roof-setback-local-axis`; ancestor of V5.3 analyzer | Product lineage through construction V5.1c | Deprecated as separate recovery source | Recover from V5.3 analyzer, which contains it by Git ancestry |
| `feature/plugin-v07-geometry-integration` | [`fd99ad9`](https://github.com/8nt7h6k229-png/PvLayoutPlugin/commit/fd99ad9dd975dd7fd66f01765fa5a026f7bd6e5d) | 1 ahead; ancestor of testing branch | Software Architecture Specification v1.0 | Deprecated as separate recovery source; [PR #6](https://github.com/8nt7h6k229-png/PvLayoutPlugin/pull/6) remains open | Recover through `docs/pvos-testing-platform`; preserve PR #6 evidence |
| `feature/pvos-geometry-phase2` | [`af682cc`](https://github.com/8nt7h6k229-png/PvLayoutPlugin/commit/af682cce3db5c99b6f67e169cbf5f0692e592c77) | 1 ahead; ancestor of platform bootstrap | Computational geometry phase 2 | Deprecated as separate recovery source / Experimental [PR #8](https://github.com/8nt7h6k229-png/PvLayoutPlugin/pull/8) | Recover through platform bootstrap; preserve PR #8 evidence |
| `feature/pvos-platform-bootstrap` | [`e8ef6ea`](https://github.com/8nt7h6k229-png/PvLayoutPlugin/commit/e8ef6ea1899336a00ffeb2ede2d3b28ff8a2f59a) | 57 ahead; 67 changed documents | Geometry/solver platform, datasets, validation, ADRs, governance, release | Branch-only; tagged historical candidate | High-priority recovery source |
| `feature/roof-setback-local-axis` | [`0106f22`](https://github.com/8nt7h6k229-png/PvLayoutPlugin/commit/0106f220e0ffe65e3dcd46fee5a5c4078dc57151) | 86 ahead; same head as construction branch; ancestor of V5.3 analyzer | Roof, local-axis and complete product history through V5.1c | Deprecated as separate recovery source; [PR #1](https://github.com/8nt7h6k229-png/PvLayoutPlugin/pull/1) remains open | Recover from V5.3 analyzer; retain PR #1 as workflow evidence |
| `feature/unit-normalize` | [`aaa9c58`](https://github.com/8nt7h6k229-png/PvLayoutPlugin/commit/aaa9c582e1be6b0e285c4fecd09d32903518e01e) | 0 ahead; same head as `develop`, fully in `main` | Issue describes DWG normalization, but branch contains no unique implementation/knowledge commit | Experimental; [issue #10](https://github.com/8nt7h6k229-png/PvLayoutPlugin/issues/10) open | No branch knowledge to recover; retain Issue evidence |
| `feature/v5.1d-ladder-planning` | [`0d72746`](https://github.com/8nt7h6k229-png/PvLayoutPlugin/commit/0d727467908e66db3ee5aaabccee29d935121f31) | 89 ahead; ancestor of V5.3 analyzer | Ladder planning and ADR-0019 | Deprecated as separate recovery source | Recover from V5.3 analyzer |
| `feature/v5.1e-cable-tray-planning` | [`6b130f3`](https://github.com/8nt7h6k229-png/PvLayoutPlugin/commit/6b130f317468592baeab2aed098d217cfec1c478) | 92 ahead; ancestor of V5.3 analyzer | Cable tray and runtime pipeline inspector | Deprecated as separate recovery source | Recover from V5.3 analyzer |
| `feature/v5.2-runtime-dashboard` | [`d1a209b`](https://github.com/8nt7h6k229-png/PvLayoutPlugin/commit/d1a209bcb9013135ed39538a46739733e4c19b8b) | 94 ahead; ancestor of V5.3 analyzer | Runtime dashboard | Deprecated as separate recovery source | Recover from V5.3 analyzer |
| `feature/v5.3-placement-v2-foundation` | [`2298448`](https://github.com/8nt7h6k229-png/PvLayoutPlugin/commit/229844818d76295ef8c95659bfa0d8e7ae815518) | 95 ahead; direct ancestor of analyzer branch | Placement Engine V2 foundation | Deprecated as separate recovery source | Recover from analyzer branch |
| `feature/v5.3-placement-v2-analyzer` | [`9dc296b`](https://github.com/8nt7h6k229-png/PvLayoutPlugin/commit/9dc296bd20e94a21acbabb805c4b0342d474866d) | 96 ahead; 150 changed documents | Superset of historical V0.4–V5.3 product, architecture and engineering knowledge; V1 adapter and V2 analyzer | Branch-only; latest historical product branch | Highest-priority recovery source |
| `recovery/ri-002-reference-preservation` | [`2b03c23`](https://github.com/8nt7h6k229-png/PvLayoutPlugin/commit/2b03c23dd9a8f47dfc08683a7a87774665c6806c) | Original six RI commits differ by SHA, but its product tree matches `main` except later governance/AI docs on `main` | Preserved original Method/Reference/Call Graph/Impact sequence | Deprecated for independent recovery; [issue #15](https://github.com/8nt7h6k229-png/PvLayoutPlugin/issues/15) closed and [PRs #17–#21](https://github.com/8nt7h6k229-png/PvLayoutPlugin/pulls?q=is%3Apr+is%3Amerged+RI-) merged | No product recovery required; retain branch as recovery provenance until PM retention decision |

## Recommended recovery sets

These recommendations select existing evidence collections; they do not propose architecture or code movement.

1. **Historical product set:** `feature/v5.3-placement-v2-analyzer`. It is proven by Git ancestry to contain `feature/construction-intelligence`, `feature/roof-setback-local-axis`, ladder, cable-tray, dashboard and placement-foundation histories.
2. **PVOS platform set:** `feature/pvos-platform-bootstrap`. It contains `feature/pvos-geometry-phase2` by ancestry and adds 57 branch-only commits covering solver, validation, datasets, ADRs and release governance.
3. **Architecture/testing set:** `docs/pvos-testing-platform`. It contains `feature/plugin-v07-geometry-integration` by ancestry and adds testing knowledge.
4. **Standalone PVOS geometry set:** `PVOS/feature/geometry-core`. It is three commits ahead of PVOS `main` and is tied to open issue #1.
5. **Recovery provenance set:** retain `recovery/ri-002-reference-preservation` as evidence; do not duplicate its already merged product knowledge.

## Obsolete branch answer

For independent knowledge recovery, the following are obsolete because Git proves they have no unique commits or are fully contained by a selected successor:

- `PVOS/develop`
- `PvLayoutPlugin/develop`
- `feature/ai-studio-foundation`
- `feature/construction-intelligence`
- `feature/plugin-v07-geometry-integration`
- `feature/pvos-geometry-phase2`
- `feature/roof-setback-local-axis`
- `feature/v5.1d-ladder-planning`
- `feature/v5.1e-cable-tray-planning`
- `feature/v5.2-runtime-dashboard`
- `feature/v5.3-placement-v2-foundation`
- `recovery/ri-002-reference-preservation` for product recovery only

`feature/unit-normalize` is classified Experimental rather than Deprecated because Issue #10 remains open, but the branch currently has no unique commit. No branch deletion is authorized by PM-002.
