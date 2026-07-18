#!/usr/bin/env python3
"""APH-11.20: Literature Review — Knot Theory in Particle Physics (Synthesis)"""

print("="*60)
print("APH-11.20: Literature Review — Knot Theory in Particle Physics")
print("="*60)

print("""
CONSOLIDATED LITERATURE SYNTHESIS (Phase 13 + Phase 11 findings)

The α-π-Helix project now spans analysis of 8 published works
plus 2 internal research notes. This review summarizes all
external references and their relationship to the vortex model.


FOUNDATIONAL PRECURSORS (1997–2019)
====================================

[1] Williamson & van der Mark (1997)
    "Is the electron a photon with toroidal topology?"
    Ann. Fond. Louis de Broglie 22(2):133.
    → PRIORITY: 29 years. Electron = self-confined photon
      on a toroidal Compton-scale path. Exact geometric
      correspondence with α-π-Helix confirmed (Sec 13.14).
    → KEY PARAMETER: r₀ = alpha·ƛ, λ_C confinement.
    → RELATION: Direct precursor. All α-π-Helix core
      identities (alpha = r_e/ƛ, m = omega) trace here.

[2] Bilson-Thompson (2005)
    "A topological model of composite preons." hep-ph/0503213.
    → PRIORITY: 21 years. Helon braid model for ALL SM particles.
    → 3-strand B₃ topology → SU(3)×U(1).
    → RELATION: α-π-Helix extends BT with mass predictions.

[3] Bilson-Thompson, Markopoulou & Smolin (2007)
    "Quantum gravity and the Standard Model." CQG 24:3975.
    → PRIORITY: 19 years. Helon model in LQG context.

[4] Bilson-Thompson, Hackett & Kauffman (2009)
    "Particle identifications from braided ribbon networks."
    J. Math. Phys. 50:113505.
    → PRIORITY: 17 years. Formal B₃ classification.

[5] Chester, Arsiwalla & Kauffman (2025)
    "From the braided ribbon network to the Standard Model."
    Int. J. Theor. Phys. 64:221.
    → PRIORITY: 1 year. MATHEMATICAL PROOF of BT → SM gauge group.
    → B₃ → SU(3)×U(1) weight lattice. Compatible with α-π-Helix.

[6] Hestenes (2008, 2019)
    "Zitterbewegung in Quantum Mechanics." Found. Phys. 40:1-54.
    "The Zitterbewegung Interpretation of Quantum Mechanics."
    arXiv:1910.11085.
    → PRIORITY: 16–18 years. Compton-scale helical Zitterbewegung.
    → Toroidal vortex model with alpha scaling.
    → RELATION: α-π-Helix provides geometric parameterization.

[7] Faddeev & Niemi (1997)
    "Knots and particles." Nature 387:58.
    → PRIORITY: 29 years. Hopf-invariant knot solitons in Skyrme model.
    → E ~ Q_H^(3/4) vs α-π-Helix E ~ |w|^2 (different energy functional).
    → Crossover at Lk ≈ 66. Both agree: topological invariants → mass.

[8] Gersten (2013)
    "Topology of the Standard Model." arXiv:1306.3617.
    → PRIORITY: 13 years. Van Kampen diagram preon model.
    → Charge ±e/3 from 3-color topology. Same as B₃ abelianization.
    → Triple convergence: BT(2005) + Gersten(2013) + APH(2026).


INTERNAL RESEARCH NOTES (2026)
==============================

[R1] Universal Vortex Particle Model
    v1.2/research/universal-vortex-particle-model.md (13.5 KB)
    → Synthesis of Williamson + BT + α-π-Helix.
    → Complete particle-vortex dictionary (17 SM particles).
    → Information-theoretic "it from bit" framework.

[R2] Phase 13 Sprint Computation Portfolio
    v1.2/computation/ (16 scripts, ~50 KB)
    → Lepton writhe spectrum: sqrt(m) ∝ |w|
    → Koide fixed-point: NO fixed-point exists
    → kappa = 0.525 MeV/crossing^2
    → Gauge bosons from vortex topology
    → Higgs as topological soliton at Lk=428
    → Color confinement as unlinking barrier
    → Information ladder: S_e=0 → S_t=405 bits


PRIORITY TABLE
==============

Claim                         First Author     Year   Priority
-----                         ------------     ----   --------
Electron = confined photon    Williamson       1997   29 years
All SM particles = tops       Bilson-Thompson  2005   21 years
SU(3)×U(1) from B₃            Chester          2025   1 year
Knot soliton particles        Faddeev-Niemi    1997   29 years
Charge = ±e/3 from 3-colors   Gersten          2013   13 years
Compton vortex (ZB)           Hestenes         2008   18 years
Mass from writhe = kappa·|w|²  α-π-Helix       2026   GENUINELY NOVEL (but C7 partially falsified)


WHAT α-π-HELIX ADDS THAT IS TRULY NEW
======================================
1. QUANTITATIVE mass predictions: kappa = 0.525 MeV/crossing^2
   (BT and Gersten don't predict masses; Faddeev-Niemi uses different scaling)
2. The Compton-scale geometric BRIDGE between Williamson and BT
3. Experimental falsification framework (C1-C10, partially executed)
4. Information-theoretic formalization (S_e→S_t, Wheeler "it from bit")
5. Cross-framework comparison matrix (Williamson/BT/FN/Gersten)

WHAT α-π-HELIX DOES NOT ADD (and should not claim)
===================================================
1. The core lepton mass formula (n^2 x p) — FALSIFIED (C7, p=1 not prime)
2. The claim of exactly 3 generations from topology — BT found unbounded generations
3. A complete SM gauge group derivation — SU(2)_L requires B4, not yet derived
4. Independent discovery of charge quantization — BT had it in 2005
5. Novel particle classification — Gersten and BT already did this


GAPS IN THE LITERATURE (for future work)
=========================================
1. No publication has derived the full SM gauge group (U(1)×SU(2)×SU(3))
   from a single topological framework. B4 extension needed.
2. No topological model has predicted Higgs mass successfully.
   Best: top condensate m_H ≈ m_t/√2 (2.4% error, post-hoc).
3. No topological model has quantitative CKM/PMNS predictions.
   Braid overlap model gives qualitative hierarchy only.
4. No one has connected Compton-scale Zitterbewegung to B3 braid topology
   before α-π-Helix — this is the genuine novelty.
5. Experimental tests: channeling ZB, storage ring THz, muon g-2 writhe
   correction. None have been performed.
""")

print("="*60)
print("APH-11.20 COMPLETE — 8 published + 2 internal works reviewed")
print("="*60)
