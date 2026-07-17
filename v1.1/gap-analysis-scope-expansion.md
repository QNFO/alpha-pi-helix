# α-π-Helix: Gap Analysis & Scope Expansion

**Document ID:** QNFO.RSCH.APH.GAP.001
**Date:** 2026-07-17
**Status:** Complete — proposed WBS extensions for v3.0
**Based on:** WBS v2.0 (76 tasks, 10 phases), Paper v1.1 (50k chars)

---

## Executive Summary

The α-π-Helix project has established a coherent geometric narrative — π, α, and mass as orthogonal projections of the Helical Compton Vortex — with Phases 0-7 complete and Phase 9 partially active (4/15 done). However, eight critical knowledge gaps prevent the thesis from achieving full scientific credibility. This analysis identifies 38 concrete research questions and proposes 34 new WBS entries across 8 gap categories, organized for integration into WBS v3.0.

**Headline finding:** The current thesis is geometrically elegant but **scientifically incomplete**. It makes a compelling case that the three constants *can be viewed* as geometric projections, but does not demonstrate that this view *produces better predictions* than the standard model — the threshold for scientific acceptance.

---

## Gap 1: Experimental Roadmap

### Current State
- APH-9.5: Channeling experiment protocol (350 MeV e⁻, Si) — single experiment, pending
- Paper §11.4 lists falsification conditions but only 1 concrete experiment
- Hestenes' EDM channeling resonance is cited but no alternatives are proposed
- No timeline, no estimated costs, no equipment specification

### Why This Gap Is Critical
The paper's central claim — "the electron is a helical Compton vortex, not a point particle" — is a physical ontology claim. If the vortex is physically real (not just a mathematical re-description), it must produce **unique measurable signatures** distinguishable from standard QFT predictions. Without a comprehensive experimental roadmap, the thesis remains metaphysical — unfalsifiable in practice, not just in principle.

### Research Questions

| # | Question | Rationale |
|---|----------|-----------|
| E1 | Could polarized electron channeling through aligned crystals reveal a ZB resonance signature distinct from QED radiative corrections? | Hestenes' prediction is untested; needs protocol development and error budget analysis distinguishing geometric from perturbative effects. |
| E2 | Does the predicted oscillating EDM produce a detectable microwave/THz emission spectrum in electron storage rings, and how does it differ from synchrotron radiation? | If the electron has an internal oscillation at 1.55 × 10²¹ Hz, this should couple to external EM fields. |
| E3 | Can femtosecond laser-electron scattering (Compton backscattering) probe sub-Compton-wavelength structure with sufficient resolution to image the helical path? | Advances in attosecond physics may enable direct imaging of electron internal structure. |
| E4 | Do electron-positron annihilation spectra show deviations from point-particle QED predictions at energy scales approaching mc²/α ≈ 70 MeV? | The vortex has finite spatial extent; annihilation at close approach should show geometric corrections. |
| E5 | Can tabletop electron interferometry (e.g., Kapitza-Dirac effect with standing light waves) detect the ZB spatial smearing predicted by the helical model? | The ZB amplitude (~10⁻¹³ m) may be within reach of modern matter-wave interferometry. |

### Proposed WBS Tasks

| Task ID | Task | Deliverable | Phase |
|---------|------|-------------|-------|
| APH-10.1 | Systematic experimental roadmap: 5-experiment matrix with feasibility, cost, timeline, and distinguishing power | `experiments/roadmap-v1.md` | NEW Phase 10 |
| APH-10.2 | Detailed protocol for polarized electron channeling (EDM resonance) with error budget distinguishing geometric from QED radiative corrections | `experiments/channeling-protocol-v1.md` | NEW Phase 10 |
| APH-10.3 | Storage ring ZB emission spectrum modeling: compute expected THz signal and compare to synchrotron background | `experiments/storage-ring-zb-spectrum.md` | NEW Phase 10 |
| APH-10.4 | Attosecond/femtosecond laser-electron scattering feasibility study | `experiments/laser-scattering-feasibility.md` | NEW Phase 10 |
| APH-10.5 | Matter-wave interferometry probe of ZB spatial extent | `experiments/interferometry-zb-probe.md` | NEW Phase 10 |

---

## Gap 2: Cosmological Connection

### Current State
- **Zero cosmological content in the paper** — no mention of cosmology, dark energy, early universe, or cosmological constant
- APH-9.10: "Dark matter voton relic abundance" exists as a pending task but is narrow (votons only)
- No connection between the geometric picture and cosmological scale

### Why This Gap Is Critical
If the electron's mass IS an angular frequency (m = ω) and α IS a geometric aspect ratio, then these are not particle-specific properties but **scale-invariant geometric relations**. The same geometric logic should apply at cosmological scales:
- The cosmological constant Λ has dimensions of (length)⁻² — it defines a cosmological length scale, just as the Compton wavelength defines the electron scale
- Dark energy density ρ_Λ ≈ (10⁻³ eV)⁴ — could this be a geometric scale analogous to α?
- The Planck scale, Compton scale, and Hubble scale form a hierarchy that may be geometric in origin

Without addressing cosmology, the thesis is incomplete — it claims "geometric unification" but only unifies at one scale.

### Research Questions

| # | Question | Rationale |
|---|----------|-----------|
| C1 | Does the geometric hierarchy r_e : ƛ : a₀ = α² : α : 1 extend to cosmological scales, with the Hubble radius H₀⁻¹ = a₀ / α³ or similar? | There is an empirical near-coincidence: H₀⁻¹ ≈ a₀ / α³² ≈ 10²⁶ m. Is this meaningful? |
| C2 | Can dark energy be reinterpreted as the geometric aspect ratio (thickness/radius) of the cosmological horizon, analogous to α at the Compton scale? | ρ_Λ ∝ H₀² suggests dark energy is a horizon-scale geometric property. |
| C3 | Does the helical vortex picture have implications for early-universe phase transitions, particularly the electroweak transition where particle masses "freeze in"? | If mass = frequency, mass generation at phase transitions is a change in oscillation boundary conditions. |
| C4 | Can the baryon asymmetry be connected to the chirality of the helical vortex structure? | The helix is inherently chiral — matter/antimatter asymmetry may be geometric rather than dynamical. |
| C5 | Do cosmic microwave background anomalies (hemispherical power asymmetry, parity violation) show signatures of a preferred cosmic helicity? | A universe built from helical vortices would have net chirality at the largest scales. |

### Proposed WBS Tasks

| Task ID | Task | Deliverable | Phase |
|---------|------|-------------|-------|
| APH-10.6 | Geometric scale hierarchy: derive relationship between Planck, Compton, atomic, and Hubble scales in the vortex picture | `cosmology/scale-hierarchy.md` | NEW Phase 10 |
| APH-10.7 | Dark energy as horizon aspect ratio: geometric reinterpretation of Λ in terms of α-like ratio at cosmological scale | `cosmology/dark-energy-geometric.md` | NEW Phase 10 |
| APH-10.8 | Electroweak phase transition in the vortex picture: mass as frozen-in oscillation frequency | `cosmology/ew-transition-vortex.md` | NEW Phase 10 |
| APH-10.9 | Baryon asymmetry from helical chirality | `cosmology/baryon-asymmetry-chirality.md` | NEW Phase 10 |
| APH-10.10 | CMB anomalies and cosmic helicity: literature review + geometric interpretation | `cosmology/cmb-helicity-review.md` | NEW Phase 10 |

---

## Gap 3: Mathematical Rigor

### Current State
- Core identities are algebraically verified (α = r_e/ƛ, m = ω in Planck units)
- No Lagrangian, action, or variational principle
- No derivation of equations of motion for the vortex
- No proof of stability beyond heuristic arguments ("electromagnetic self-energy balanced against quantum oscillation")
- The paper describes *what* the geometry is, not *why* it is that way

### Why This Gap Is Critical
A geometric interpretation without a dynamical principle is a **kinematic description, not a physical theory**. Physics demands:
1. An **action** from which equations of motion follow
2. A **stability proof** showing the vortex is a minimum of that action
3. **Conserved quantities** derived from symmetries (Noether's theorem)
4. A **quantization procedure** that recovers the Dirac equation as an effective theory

The current work is analogous to Kepler's laws without Newton's — it describes the geometry correctly but lacks the dynamical foundation.

### Research Questions

| # | Question | Rationale |
|---|----------|-----------|
| M1 | What is the minimal action whose Euler-Lagrange equations yield a helical lightlike vortex solution with the Compton wavelength as its characteristic scale? | This is the core theoretical challenge. Candidate frameworks: Born-Infeld electrodynamics, Kalb-Ramond fields, or geometric actions in STA. |
| M2 | Can the vortex stability condition (EM self-energy = quantum oscillation energy) be derived from a variational principle, yielding α as the minimizing ratio? | If α emerges from energy minimization, its value becomes a prediction rather than an input. |
| M3 | What are the Noether conserved quantities of the helical vortex action, and do they correspond to charge (U(1)), spin (Poincaré), and lepton number? | Symmetries should map to observed quantum numbers. |
| M4 | Can one derive the Dirac equation as a linearized approximation of the vortex dynamics, analogous to sound waves emerging from fluid dynamics? | This would establish the vortex model as more fundamental than the Dirac equation. |
| M5 | What is the appropriate topological classification for helical vortices — are they characterized by Hopf invariants, linking numbers, or instanton numbers? | Topological stability is a stronger argument than energetic stability. |

### Proposed WBS Tasks

| Task ID | Task | Deliverable | Phase |
|---------|------|-------------|-------|
| APH-10.11 | Derive candidate geometric action for helical Compton vortex (Born-Infeld + STA approach) | `theory/action-principle.md` | NEW Phase 10 |
| APH-10.12 | Variational stability analysis: prove α ≈ 1/137 as energy-minimizing aspect ratio | `theory/stability-variational.md` | NEW Phase 10 |
| APH-10.13 | Noether analysis: map vortex symmetries to conserved quantum numbers | `theory/noether-conservation.md` | NEW Phase 10 |
| APH-10.14 | Derive Dirac equation as effective theory from vortex dynamics | `theory/dirac-as-effective.md` | NEW Phase 10 |
| APH-10.15 | Topological classification of helical vortices (Hopf, linking numbers) | `theory/topology-classification.md` | NEW Phase 10 |

---

## Gap 4: QFT Correspondence

### Current State
- APH-9.8: "QED coefficients from vortex hydrodynamics (C₂, C₃)" — pending
- APH-9.12: "Running of α geometric test" — pending
- Paper §11.2 briefly notes a_e ≈ α/(2π) as a geometric thickness correction
- No systematic comparison of vortex predictions vs. QFT predictions across multiple observables
- No discussion of the Lamb shift, vacuum polarization, or Delbrück scattering

### Why This Gap Is Critical
Quantum electrodynamics is the most precisely tested theory in physics. Any alternative model must **reproduce or exceed QED's predictive accuracy** for the key precision observables:
- Anomalous magnetic moment: a_e to 12 sig figs, a_μ to 9 sig figs
- Lamb shift: 2S-2P splitting to 10⁻⁶ precision
- Running coupling α(Q²): measured from low-energy to Z-pole
- Hyperfine splitting: positronium and muonium

The vortex model does not need to reproduce all 12 significant figures immediately, but it does need to (a) recover the leading terms geometrically and (b) identify where quantitative deviations are predicted. Without this, the model is unfalsifiable where QED is most precise — a fatal gap.

### Research Questions

| # | Question | Rationale |
|---|----------|-----------|
| Q1 | Can the full QED perturbative series for a_e be reinterpreted as a geometric series of vortex self-interaction corrections, with each order corresponding to a specific topological deformation? | The Schwinger term α/2π is already geometric; can C₂, C₃, C₄ all be expressed in terms of vortex geometry? |
| Q2 | What does the vortex model predict for the muon anomalous magnetic moment a_μ, and does it differ from the Standard Model prediction in the direction of the current ~4.2σ anomaly? | If the vortex model predicts a larger a_μ than SM, this would be a major success. |
| Q3 | How does the Lamb shift emerge from the finite spatial extent of the vortex — i.e., can the Uehling potential be derived from the vortex's charge distribution rather than vacuum polarization loops? | This is a concrete test: geometric vs. virtual-particle explanation. |
| Q4 | Does the running of α with energy scale correspond to a scale-dependent vortex aspect ratio, and does the predicted running match the measured α(Q²) from low-energy to the Z-pole? | APH-9.12 addresses this but needs expansion to full energy range. |
| Q5 | What do vortex geometry corrections predict for high-precision positronium spectroscopy (hyperfine splitting, decay rates) compared to NRQED predictions? | Positronium is a pure QED system — an ideal testbed. |

### Proposed WBS Tasks

| Task ID | Task | Deliverable | Phase |
|---------|------|-------------|-------|
| APH-10.16 | Systematic QED correspondence table: map all major QED precision observables to vortex geometric predictions | `qft/qed-correspondence-matrix.md` | NEW Phase 10 |
| APH-10.17 | Derive leading Schwinger term α/2π from geometric arguments; attempt C₂, C₃ from vortex self-interaction | `qft/schwinger-geometric.md` | NEW Phase 10 |
| APH-10.18 | Muon g-2 prediction from vortex model with comparison to Fermilab/BNL measurement and SM prediction | `qft/muon-g2-vortex.md` | NEW Phase 10 |
| APH-10.19 | Lamb shift from finite vortex extent (Uehling-like potential from charge distribution) | `qft/lamb-shift-vortex.md` | NEW Phase 10 |
| APH-10.20 | Positronium spectroscopy predictions from vortex model | `qft/positronium-vortex.md` | NEW Phase 10 |

---

## Gap 5: Alternative Theories Comparison

### Current State
- No comparison with any alternative theory framework
- Paper §7 compares electron models (Hestenes, Consa, Williamson, Rodrigues) — but these are all *within* the same geometric tradition
- No engagement with mainstream beyond-Standard-Model approaches

### Why This Gap Is Critical
The academic community will judge the α-π-Helix thesis against established alternative frameworks. Without a systematic comparison, the work appears:
1. **Isolated** — unaware of parallel efforts
2. **Naive** — failing to address known challenges that other frameworks have already tackled
3. **Overclaiming** — making assertions without demonstrating advantages

A credible comparison must show: (a) what the vortex model explains that these alternatives cannot, (b) where it makes different predictions, and (c) what it shares with each framework.

### Research Questions

| # | Question | Rationale |
|---|----------|-----------|
| T1 | How does the Helical Compton Vortex compare to string theory's fundamental strings — both propose extended objects, but does the vortex model avoid the landscape problem and the lack of unique predictions? | String theory is the dominant extended-object framework; direct comparison is essential. |
| T2 | Does LQG's spin-network picture have a dual description in terms of vortex tangles, and can the area quantization of LQG be mapped to vortex circulation quantization? | LQG shares topological/geometric motivations; cross-fertilization is possible. |
| T3 | Can Causal Dynamical Triangulations' emergent spacetime at the Planck scale be reinterpreted as a network of entangled vortices? | CDT produces de Sitter-like spacetime from first principles — does this relate to vortex cosmology? |
| T4 | Does the asymptotic safety scenario's prediction of a finite number of relevant couplings have a geometric interpretation in the vortex picture? | Asymptotic safety and geometric unification share the goal of reducing free parameters. |
| T5 | How does Lisi's E8 theory, which unifies all Standard Model particles in a single Lie group with geometric interpretation, compare to the vortex model's topological classification of particles? | Both are geometric unification programs; what are the relative strengths? |

### Proposed WBS Tasks

| Task ID | Task | Deliverable | Phase |
|---------|------|-------------|-------|
| APH-10.21 | Systematic comparison with String Theory: extended objects, landscape problem, predictions | `comparison/string-theory.md` | NEW Phase 10 |
| APH-10.22 | Comparison with Loop Quantum Gravity: spin networks ↔ vortex tangles, area quantization | `comparison/loop-quantum-gravity.md` | NEW Phase 10 |
| APH-10.23 | Comparison with Causal Dynamical Triangulations: emergent spacetime ↔ vortex network | `comparison/causal-dynamical-triangulations.md` | NEW Phase 10 |
| APH-10.24 | Comparison with Asymptotic Safety: relevant couplings ↔ geometric parameters | `comparison/asymptotic-safety.md` | NEW Phase 10 |
| APH-10.25 | Comparison with E8 Theory (Lisi): geometric unification programs compared | `comparison/e8-theory-lisi.md` | NEW Phase 10 |

---

## Gap 6: Historical Depth

### Current State
- Phase 1 covers: William Jones 1706, Attic numeral system, pre-1706 catalogue, Euler (pending)
- APH-1.7: Etruscan/Roman comparison — pending
- §2.3: Sommerfeld's introduction of α is covered but only in one paragraph
- Total historical scope: Western European + Attic Greek only

### Why This Gap Is Critical
The paper's central claim about π is that its "reification" from geometric proportion to transcendental number is a modern Western development. But this argument is weakened without showing:
1. **How other cultures treated π** — did Chinese, Indian, Babylonian, and Egyptian mathematicians also reify it, or did they maintain the proportion view?
2. **The full pre-history of α** — Sommerfeld didn't invent α in a vacuum; it emerged from the Bohr model, Rydberg constant, and Balmer series
3. **Whether the Attic Π → modern π transition is unique** or whether similar semantic drifts occurred in other symbolic systems

Without this global historical perspective, the "reification narrative" risks being Eurocentric and historically incomplete.

### Research Questions

| # | Question | Rationale |
|---|----------|-----------|
| H1 | How did Babylonian (base-60) and Egyptian (Rhind Papyrus) mathematics treat the circle ratio — as a proportion between measurable magnitudes or as a number with intrinsic value? | Tests the universality of the reification thesis. |
| H2 | Did Chinese mathematicians (Liu Hui, Zu Chongzhi) treat π as an independent number or as a geometric proportion to be approximated? | Zu's 355/113 is a remarkable approximation — was it treated as a *number* or a *construction*? |
| H3 | In Indian mathematics (Aryabhata, Madhava), was π treated as a transcendental constant, or did the infinite-series approach reveal a different ontological attitude? | Madhava's series for π predates European calculus — what was the philosophical framing? |
| H4 | How did Sommerfeld's introduction of α in 1916 relate to the Bohr model, the Rydberg constant, and earlier work on spectral line splitting by Michelson and others? | The coupling-constant interpretation is historically contingent, not logically necessary. |
| H5 | Are there other cases in the history of physics where a geometric proportion was reified into a "fundamental constant," and what can we learn from those episodes? | Precedent cases strengthen or weaken the thesis. Examples: Boltzmann's k, Planck's h. |

### Proposed WBS Tasks

| Task ID | Task | Deliverable | Phase |
|---------|------|-------------|-------|
| APH-1.8 | Babylonian and Egyptian circle ratio treatment | `history/babylonian-egyptian-pi.md` | Extend Phase 1 |
| APH-1.9 | Chinese mathematics: Liu Hui and Zu Chongzhi on π | `history/chinese-pi.md` | Extend Phase 1 |
| APH-1.10 | Indian mathematics: Aryabhata, Madhava, and the infinite-series approach to π | `history/indian-pi.md` | Extend Phase 1 |
| APH-1.11 | Sommerfeld's α: full pre-history from Balmer to Bohr to fine structure | `history/sommerfeld-alpha-prehistory.md` | Extend Phase 1 |
| APH-1.12 | Historical case studies: reification of geometric proportions into "fundamental constants" (k, h, G) | `history/reification-case-studies.md` | Extend Phase 1 |

---

## Gap 7: Philosophy of Science

### Current State
- Paper §9: "Reification of Constants — A Critique" — comprehensive treatment of reification (~2000 words)
- Covers: definition of reification, reification of π, α, and mass
- §9.5: Historical parallel to Greek proportion theory
- §9.6: Linear/circular assumptions in physics

### Why This Gap Is Critical
The reification critique is the philosophical backbone of the paper — without it, the geometric identities are "merely" mathematical curiosities. However, the current treatment:
1. **Does not engage with the philosophy of science literature** that has addressed similar issues
2. **Does not position itself** within established philosophical frameworks
3. **Lacks rigor** in defining what constitutes a "real" vs. "reified" entity — this is a deep philosophical problem

The paper makes a strong ontological claim (the electron IS a vortex, not a point particle) without justifying the criteria for ontological commitment. This leaves it vulnerable to instrumentalist critique: "You've found a useful geometric re-description — so what?"

### Research Questions

| # | Question | Rationale |
|---|----------|-----------|
| P1 | Does the Helical Compton Vortex model align with Structural Realism (Worrall, Ladyman), where what is "real" is the mathematical structure rather than the entities? | Structural realism provides a framework for claiming the vortex structure is real without claiming the vortex is a "thing." |
| P2 | Can Ontic Structural Realism (French, Ladyman) — which claims that structure is all there is — provide a philosophical foundation for the claim that π, α, and m are not independent entities but structural relations? | OSR eliminates the need to say what the vortex "is made of" — only that its relational structure is real. |
| P3 | How does the map/territory distinction (Korzybski, Bateson) apply to the relationship between the mathematical description (π, α, m as numbers) and the physical reality (the vortex)? | The paper precisely claims we've mistaken the map (constants) for the territory (geometry). |
| P4 | What are the criteria for "geometric reality" in physics, as established by historical debates (Newton vs. Leibniz on space, Einstein vs. Lorentz on spacetime)? | What does it take for a geometric entity to be accepted as physically real? |
| P5 | Does the vortex model commit the "reverse reification" fallacy — treating a useful mathematical construct (the vortex) as if it were physically real? | Self-critique: is the vortex itself a reification? |

### Proposed WBS Tasks

| Task ID | Task | Deliverable | Phase |
|---------|------|-------------|-------|
| APH-10.26 | Structural Realism and the vortex model: philosophical positioning | `philosophy/structural-realism.md` | NEW Phase 10 |
| APH-10.27 | Ontic Structural Realism as foundation for the unification thesis | `philosophy/ontic-structural-realism.md` | NEW Phase 10 |
| APH-10.28 | Map/territory distinction applied to fundamental constants | `philosophy/map-territory.md` | NEW Phase 10 |
| APH-10.29 | Criteria for geometric reality: historical precedents and application to the vortex | `philosophy/geometric-reality-criteria.md` | NEW Phase 10 |
| APH-10.30 | Self-critique: is the vortex itself a reification? | `philosophy/vortex-reification-self-critique.md` | NEW Phase 10 |

---

## Gap 8: Computational Validation

### Current State
- APH-9.2: STA π-free Dirac solver — pending
- APH-9.3: Koide formula from vortex topology — pending
- APH-9.4: α stability eigenvalue (Saffman vortex analog) — pending
- APH-9.8: QED coefficients from vortex hydrodynamics — pending
- APH-9.11: Planck self-consistency bound — pending
- APH-9.12: Running of α geometric test — pending
- **No numerical predictions unique to the model exist.** All geometric identities are re-expressions of known relationships.

### Why This Gap Is Critical
The paper's most significant weakness: **it makes no novel numerical prediction.** α ≈ 1/137 is known; m = ω is a unit conversion; π ≈ 3.14… is definitional. The geometric interpretation is elegant but unfruitful without:

1. **Unique signatures** — numbers that do not follow from existing theory
2. **Quantitative precision** — "α is an aspect ratio" must be followed by "and here is why that aspect ratio is 1/137.035999177…"
3. **Predictive power** — explaining not just known relationships but *unknown* ones

The absence of computational validation makes the thesis a **re-description, not a discovery**. To advance from "interesting perspective" to "scientific contribution," the model must produce at least one novel numerical prediction that can be tested against data.

### Research Questions

| # | Question | Rationale |
|---|----------|-----------|
| V1 | Can numerical simulation of a helical vortex in classical electrodynamics (with quantum constraints) produce a stable configuration whose aspect ratio converges to α ≈ 1/137? | This would be the first direct computational evidence for the vortex model. |
| V2 | Does the vortex model predict specific mass ratios for leptons (e:μ:τ) based on topological invariants (winding numbers), and do these match observed values? | Mass ratios are the most glaring unexplained pattern in particle physics. |
| V3 | What is the unique spectral signature of a vortex electron in a Penning trap — specifically, do the cyclotron and anomaly frequencies show geometric corrections? | Penning trap measurements achieve 10⁻¹¹ precision — deviations from QED could be detectable. |
| V4 | Can the Koide formula (Q = (m_e + m_μ + m_τ)/(√m_e + √m_μ + √m_τ)² = 2/3) be derived from vortex topology constraints? | The Koide formula is an unexplained empirical regularity — a topological derivation would be a major success. |
| V5 | What does the vortex model predict for the neutrino mass hierarchy and absolute mass scale, given that neutrinos may be "untwisted" (non-circulating) vortex states? | If neutrinos are vortex states with zero net circulation, their masses should follow from boundary conditions. |

### Proposed WBS Tasks

| Task ID | Task | Deliverable | Phase |
|---------|------|-------------|-------|
| APH-9.2-r | STA π-free Dirac solver with numerical benchmarks (revised) | `computation/sta-dirac-solver/` | Extend Phase 9 |
| APH-9.16 | Full numerical simulation of helical vortex stability: EM + quantum constraints → α convergence | `computation/vortex-stability-sim/` | Extend Phase 9 |
| APH-9.17 | Lepton mass ratios from vortex topological invariants | `computation/lepton-mass-ratios.md` | Extend Phase 9 |
| APH-9.18 | Penning trap geometric corrections: cyclotron and anomaly frequency predictions | `computation/penning-trap-corrections.md` | Extend Phase 9 |
| APH-9.19 | Neutrino mass hierarchy from vortex boundary conditions | `computation/neutrino-mass-vortex.md` | Extend Phase 9 |

---

## WBS v3.0 Integration Summary

### Proposed New Phases

| Phase | Title | New Tasks | Rationale |
|-------|-------|-----------|-----------|
| **Phase 10** | External Validation & Theory Building | 30 | All gaps require external-facing work: experiments, cosmology, comparison, philosophy. This phase consolidates them. |

### Phase 1 Extensions

| Task ID | Task | Gap |
|---------|------|-----|
| APH-1.8 | Babylonian and Egyptian circle ratio | Gap 6 |
| APH-1.9 | Chinese mathematics on π | Gap 6 |
| APH-1.10 | Indian mathematics on π | Gap 6 |
| APH-1.11 | Sommerfeld's α pre-history | Gap 6 |
| APH-1.12 | Historical reification case studies | Gap 6 |

### Phase 9 Extensions

| Task ID | Task | Gap |
|---------|------|-----|
| APH-9.16 | Vortex stability numerical simulation | Gap 8 |
| APH-9.17 | Lepton mass ratios from topology | Gap 8 |
| APH-9.18 | Penning trap geometric corrections | Gap 8 |
| APH-9.19 | Neutrino mass hierarchy from vortex BCs | Gap 8 |

### Phase 10: External Validation & Theory Building

| Task ID | Task | Gap |
|---------|------|-----|
| APH-10.1 | Systematic experimental roadmap | Gap 1 |
| APH-10.2 | Channeling experiment protocol | Gap 1 |
| APH-10.3 | Storage ring ZB emission spectrum | Gap 1 |
| APH-10.4 | Attosecond laser scattering feasibility | Gap 1 |
| APH-10.5 | Matter-wave interferometry ZB probe | Gap 1 |
| APH-10.6 | Geometric scale hierarchy (Planck→Hubble) | Gap 2 |
| APH-10.7 | Dark energy as horizon aspect ratio | Gap 2 |
| APH-10.8 | EW phase transition in vortex picture | Gap 2 |
| APH-10.9 | Baryon asymmetry from chirality | Gap 2 |
| APH-10.10 | CMB anomalies and cosmic helicity | Gap 2 |
| APH-10.11 | Geometric action for Compton vortex | Gap 3 |
| APH-10.12 | Variational stability → α prediction | Gap 3 |
| APH-10.13 | Noether conserved quantities | Gap 3 |
| APH-10.14 | Dirac equation as effective theory | Gap 3 |
| APH-10.15 | Topological classification | Gap 3 |
| APH-10.16 | QED correspondence matrix | Gap 4 |
| APH-10.17 | Schwinger term from geometry | Gap 4 |
| APH-10.18 | Muon g-2 prediction | Gap 4 |
| APH-10.19 | Lamb shift from finite vortex extent | Gap 4 |
| APH-10.20 | Positronium spectroscopy | Gap 4 |
| APH-10.21 | String theory comparison | Gap 5 |
| APH-10.22 | LQG comparison | Gap 5 |
| APH-10.23 | CDT comparison | Gap 5 |
| APH-10.24 | Asymptotic safety comparison | Gap 5 |
| APH-10.25 | E8 comparison | Gap 5 |
| APH-10.26 | Structural realism philosophical foundation | Gap 7 |
| APH-10.27 | Ontic structural realism framework | Gap 7 |
| APH-10.28 | Map/territory distinction | Gap 7 |
| APH-10.29 | Criteria for geometric reality | Gap 7 |
| APH-10.30 | Self-critique: vortex reification | Gap 7 |

---

## Summary Statistics

| Metric | Current (v2.0) | Proposed (v3.0) | Change |
|--------|---------------|-----------------|--------|
| Total Phases | 10 (0–9) | 11 (0–10) | +1 |
| Total Tasks | 76 | 110 | +34 |
| Phase 1 tasks | 7 | 12 | +5 |
| Phase 9 tasks | 15 | 19 | +4 |
| Phase 10 tasks | 0 | 30 | +30 |
| Tasks pending | ~20 | ~54 | +34 |

---

## Risk Assessment

| Risk | Severity | Mitigation |
|------|----------|------------|
| Scope creep: 34 new tasks may overwhelm | Medium | Prioritize by impact: experimental (Gap 1) and computational (Gap 8) first, then QFT correspondence (Gap 4), then others |
| Theoretical dead end: action principle may not yield α | High | Set falsification milestone: if no variational principle yields α by APH-10.12, reconsider geometric model |
| Resource constraints: computational simulation needs significant CPU | Medium | Start with simplified 2D+1 models; scale to full 3D+1 only after proof-of-concept |
| Community rejection: geometric model may be dismissed as "not even wrong" | Medium | Gap 7 (philosophy) and Gap 5 (comparison) are essential for positioning against this critique |

---

## Priority Ordering for v3.0 Execution

Based on scientific impact and logical dependency:

1. **Gap 8 (Computational)** — produces novel predictions → makes the thesis falsifiable
2. **Gap 4 (QFT Correspondence)** — establishes credibility with mainstream physics
3. **Gap 3 (Mathematical Rigor)** — provides dynamical foundation
4. **Gap 1 (Experimental)** — translates predictions into testable protocols
5. **Gap 2 (Cosmological)** — extends scope to largest scales
6. **Gap 5 (Alternative Theories)** — positions within academic landscape
7. **Gap 6 (Historical Depth)** — enriches narrative (low dependency)
8. **Gap 7 (Philosophy)** — deepens foundations (low dependency)

---

*Gap Analysis v1.0 — 2026-07-17 — QNFO.RSCH.APH.GAP.001*
