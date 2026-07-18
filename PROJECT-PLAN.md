# PROJECT-PLAN.md — α-π-Helix: Geometric Unification of Fundamental Constants

**Project ID:** QNFO.RSCH.APH
**Status:** Phase 13 COMPLETE — Zenodo v1.4 published
**Date:** 2026-07-18

---

## §1. Charter

### 1.1 Mission

Investigate whether the three fundamental constants — π, α (fine-structure constant), and particle mass m — are independent numbers or different projections of a single underlying geometric structure: a helical toroidal vortex with the Compton wavelength as its characteristic scale.

### 1.2 Core Claim (Locked)

**Original claim (v1.1):** π, α, and m are not independent "fundamental constants" but different projections of a single underlying geometric structure — a helical/toroidal vortex with the Compton wavelength as its characteristic scale.

**Reformulation (v1.4, post-Phase 13):** All Standard Model particles are different topological vortex/helicon configurations of the same fundamental pattern — a photon confined to a toroidal/helical path, as first proposed by Williamson & van der Mark (1997). Quantum numbers (charge, color, spin, generation) are topological invariants of the vortex configuration. Mass = κ × |w|² where |w| is the B₃ braid word length.

**Falsifiability:** The claim is falsifiable — C7 (electron self-ratio mass formula) was partially falsified at desk level. The Koide fixed-point hypothesis was definitively falsified (no fixed-point exists; Q(μ) runs away from 2/3).

---

## §2. Work Breakdown Structure (WBS)

### Phase Summary

| Phase | Description | Status | Tasks |
|:------|:------------|:-------|:------|
| 0 | Infrastructure & Registration | ✅ | 5/5 |
| 1 | Historical Foundations | ✅ | 8/8 |
| 2 | Mathematical Foundations | ✅ | Various |
| 3 | Physical Foundations (ZB, Dirac) | ✅ | Various |
| 4 | Synthesis Writing | ✅ | Various |
| 5 | Publication Pipeline | ✅ | PDF + Zenodo |
| 6 | Archive & Sync | ✅ | GitHub + R2 |
| 7 | Red-Team & Peer Review | ✅ | Multiple rounds |
| 8 | Closeout | ✅ | Audit documented |
| 9 | Applications & Roadmap | ✅ | 12/12 |
| 10 | Cosmology, Theory, Quantum Gravity | ⚡ | Partial |
| 11 | Particle Zoo Resolution | ✅ 25/25 | 100% |
| 12 | Bilson-Thompson Priority Comparison | ✅ | Published |
| 13 | Universal Vortex Particle Model | ✅ 16/16 | Zenodo v1.4 |

### Current WBS Version: v3.2

- **Total Tasks:** 151
- **Tasks Complete:** ~96 (64%)
- **Zenodo DOI:** 10.5281/zenodo.21424990 (v1.4)

**Full WBS:** `alpha-pi-helix/v1.1/WBS-v3.0.md` (v3.2)

---

## §3. Milestones with Gate Criteria

| Milestone | Date | Gate Criteria | Status |
|:----------|:-----|:--------------|:-------|
| M0: Infrastructure | 2026-07-17 | Git repo, D1, R2, Zenodo community | ✅ |
| M1: Paper v1.1 | 2026-07-17 | PDF built, Zenodo v1.1 published | ✅ |
| M2: Phase 9 computations | 2026-07-17 | Koide, Saffman, Planck, lepton masses | ✅ |
| M3: WBS v3.0 | 2026-07-17 | 110 tasks, Phase 10 added | ✅ |
| M4: Phase 11 falsification | 2026-07-18 | 10/10 criteria, C7 partially falsified | ✅ |
| M5: Phase 12 BT priority | 2026-07-18 | 4/5 claims have 2005 antecedents | ✅ |
| M6: WBS v3.1 | 2026-07-18 | 135 tasks, Phase 11-12 added | ✅ |
| M7: Phase 13 universal model | 2026-07-18 | 16/16 tasks, all SM particles classified | ✅ |
| M8: Zenodo v1.4 | 2026-07-18 | DOI published, R2 + GitHub synced | ✅ |
| M9: Phase 11 consolidation | 2026-07-18 | 25/25 tasks complete | ✅ |

---

## §4. Deliverable Registry

| ID | Deliverable | Path | Archival Target |
|:---|:------------|:-----|:----------------|
| D001 | Paper PDF (v1.4) | paper/alpha-pi-helix.pdf | Zenodo, GitHub, R2 |
| D002 | Paper source (v1.4) | paper/alpha-pi-helix.md | Zenodo, GitHub, R2 |
| D003 | WBS v3.2 | alpha-pi-helix/v1.1/WBS-v3.0.md | GitHub |
| D004 | Universal Vortex Model | alpha-pi-helix/v1.2/research/universal-vortex-particle-model.md | GitHub, R2 |
| D005 | Williamson analysis | alpha-pi-helix/v1.2/literature/APH-13.14-williamson-analysis.md | GitHub, R2 |
| D006 | Computation portfolio (18 scripts) | alpha-pi-helix/v1.2/computation/ | GitHub, R2 (bundle) |
| D007 | Provenance bundle | paper/PROVENANCE-BUNDLE.zip | Zenodo, R2 |
| D008 | Session notes | research-notes/session-2026-07-17.md, session-2026-07-18.md | GitHub |
| D009 | Red-team report | review/red-team-v1.4.md | GitHub |
| D010 | BT comparison | alpha-pi-helix/v1.1/comparison/bilson-thompson-helon-vs-aphase11.md | GitHub |

---

## §5. Risk Register

| ID | Risk | Probability | Impact | Mitigation | Status |
|:---|:-----|:------------|:-------|:-----------|:-------|
| R1 | Core claim (C7) falsified | HIGH | HIGH | Withdraw C7, reframe as vortex extension of BT | RESOLVED |
| R2 | Bilson-Thompson priority overlap | HIGH | MEDIUM | Cite BT, reframe as extension | MITIGATED |
| R3 | Koide fixed-point nonexistent | CONFIRMED | LOW | Document as definitive negative result | RESOLVED |
| R4 | Zenodo title corruption | MEDIUM | LOW | Fixed: use byte-array UTF-8 for PUT | RESOLVED |
| R5 | R2 sync failure | LOW | MEDIUM | Use primary-r2:qnfo-projects bucket | MITIGATED |
| R6 | Submodule tracking issues | MEDIUM | LOW | Commit inside submodule first | MONITORED |
| R7 | SU(2)_L not derivable from B3 alone | CONFIRMED | MEDIUM | Document as known gap; B4 extension future work | ACCEPTED |
| R8 | CKM numerical fit RMS 0.219 | HIGH | LOW | Braid overlap model qualitative only | DOCUMENTED |

---

## §6. Success Criteria

| Criterion | Target | Actual | Status |
|:----------|:-------|:-------|:-------|
| Paper published on Zenodo | v1.0+ | v1.4 | ✅ |
| All SM particles classified | v1.4 | 17/17 particles | ✅ |
| Falsifiable predictions | ≥5 | 10 (C1-C10) | ✅ |
| Cross-framework comparison | ≥3 | BT, Gersten, FN, Williamson | ✅ |
| GitHub sync | Every phase | 25+ commits | ✅ |
| R2 archive | Every version | v1.1–v1.4 | ✅ |
| Session documentation | Every session | 2 session notes | ✅ |
| Red-team review | ≥2 rounds | 2 rounds (Phase 7 + Phase 13) | ✅ |

---

## §7. Version History

| Version | Date | Change |
|:--------|:-----|:-------|
| v1.0 | 2026-07-17 | Initial project plan |
| v1.1 | 2026-07-18 | Updated with Phase 11-12, WBS v3.1 |
| v1.2 | 2026-07-18 | Updated with Phase 13, WBS v3.2, Zenodo v1.4 |

---

**Author:** QNFO Research Pipeline
**Date:** 2026-07-18
**Status:** Current — Phase 13 complete, Phase 11 at 25/25
