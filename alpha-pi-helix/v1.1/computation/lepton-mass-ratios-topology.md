# APH-9.17: Lepton Mass Ratios from Vortex Topological Invariants

**α-π-Helix Project — Phase 9: Lepton Mass Hierarchy**
**Status: Exploratory analysis with honest assessment of successes and failures**
**Date: 2026-07-18**

---

## Abstract

The three charged leptons share the same fine-structure constant α = r_e/ƛ̄ in the α-π-Helix framework (where α is the vortex aspect ratio, the ratio of vortex core radius to ring radius), yet their masses span three orders of magnitude:

| Lepton | Mass (MeV) | Ratio to electron | Ratio to predecessor |
|--------|-----------|-------------------|---------------------|
| e      | 0.511     | 1                 | —                   |
| μ      | 105.66    | 206.8             | 206.8               |
| τ      | 1776.86   | 3477              | 16.8                |

We investigate whether this hierarchy can be derived from topological invariants of vortex rings. We systematically explore three candidate topological encodings — circulation quantum number n, knot type of the vortex centerline, and renormalization group running of vortex self-energy — and provide an honest accounting of what each approach predicts, where it succeeds, and where it fails.

**Executive summary:** No single topological invariant reproduces the observed mass ratios. The vortex model provides a conceptual framework — each generation corresponds to a distinct topological state — but quantitative predictions for the mass ratios remain beyond reach without additional dynamical input, particularly an RG mechanism that encodes how bare (degenerate) masses at the Planck scale flow to the observed low-energy hierarchy.

---

## 1. The α-π-Helix Vortex Framework

### 1.1 Recap: Electron as a Toroidal Vortex

In the α-π-Helix framework, the electron is modeled as a thin toroidal vortex ring. The fine-structure constant α emerges geometrically as the aspect ratio:

$$\alpha = \frac{r_e}{\bar{\lambda}_C}$$

where:
- $r_e$ = classical electron radius (the vortex core radius / minor radius)
- $\bar{\lambda}_C = \hbar/m_e c$ = reduced Compton wavelength (the vortex ring radius / major radius)

This follows Hestenes' geometric interpretation of Zitterbewegung as a lightlike helical trajectory, with the Compton wavelength as the vortex diameter. The key physical content is that the electromagnetic self-energy of a charged rotating vortex ring, when set equal to $m_e c^2$, yields precisely $\alpha = r_e/\bar{\lambda}_C$.

### 1.2 The Generation Problem

If all three charged leptons share the same α, why do their masses differ? In the vortex picture, a lepton is defined by two independent parameters, not one:

1. **The aspect ratio** α = r/ƛ — which is fixed by electromagnetism and identical for all three generations.
2. **The absolute scale** — the overall size of the vortex ring, which can differ across generations.

Since $\bar{\lambda}_C = \hbar/mc$, the Compton wavelength is inversely proportional to mass. So the three generations correspond to vortex rings of radii $\bar{\lambda}_{C}^{(n)}$ where $n = 1,2,3$, with $m_n = \hbar/(c \bar{\lambda}_{C}^{(n)})$.

The puzzle becomes: **What determines the discrete set of allowed vortex ring sizes?**

---

## 2. Approach 1: Circulation Quantum Numbers

### 2.1 Vortex Mass from Classical Hydrodynamics

In classical vortex dynamics, the energy (mass) of an isolated thin vortex ring with circulation Γ and ring radius R (where the core radius is r = αR) is:

$$m c^2 \propto \rho \Gamma^2 R \left[\ln\left(\frac{8R}{r}\right) - \beta\right]$$

where ρ is the effective mass density of the vortex medium and β is a core-shape-dependent constant (β ≈ 1/4 for a hollow core, β ≈ 2 for a uniform core). Using r = αR:

$$m c^2 \propto \rho \Gamma^2 R \left[\ln\left(\frac{8}{\alpha}\right) - \beta\right]$$

For α ≈ 1/137, the logarithmic factor is $\ln(8 \cdot 137) - \beta \approx 7.0 - \beta$, a slowly varying function of order unity.

### 2.2 Quantized Circulation

If the circulation is quantized, Γ = n·Γ₀ for integer n, and the ring radius is determined by the quantum constraint $R_n = \bar{\lambda}_{C}^{(n)} = \hbar/(m_n c)$, then:

$$m_n c^2 \propto \rho (n\Gamma_0)^2 \frac{\hbar}{m_n c} \left[\ln\left(\frac{8}{\alpha}\right) - \beta\right]$$

Solving for $m_n$:

$$m_n^2 \propto n^2 \cdot \frac{\rho \Gamma_0^2 \hbar}{c} \left[\ln\left(\frac{8}{\alpha}\right) - \beta\right]$$

$$\boxed{m_n \propto n}$$

This predicts:

| n | Predicted $m_n/m_e$ | Observed $m_n/m_e$ |
|---|---------------------|---------------------|
| 1 | 1                   | 1                   |
| 2 | 2                   | 206.8               |
| 3 | 3                   | 3477                |

**Verdict: FAIL.** Linear scaling in n completely misses the exponential-looking hierarchy. The ratio $m_\mu/m_e \approx 207$ requires $n \approx 207$ for the muon — far beyond n = 2.

### 2.3 Alternative: Fixed Radius, Variable Circulation

If instead the ring radius R is fixed (not determined by the Compton relation) and only circulation varies, then from $m \propto n^2$:

$$m_\mu/m_e = 4, \quad m_\tau/m_e = 9$$

Still off by factors of 52 and 386 respectively. No power-law in n can bridge a factor of 207 with n = 2.

**Verdict: FAIL.** Circulation quantum number alone cannot produce the observed mass ratios, regardless of whether the Compton constraint is applied or not.

---

## 3. Approach 2: Knot Type as Generation Label

### 3.1 Motivations

A more promising direction recognizes that vortex lines in three dimensions can form knots. The three generations might correspond to three distinct knot types of the vortex centerline:

- **e (n=1):** Unknot — the simplest possible closed curve
- **μ (n=2):** Trefoil knot (3₁ in knot tables) — crossing number c = 3
- **τ (n=3):** Cinquefoil knot (5₁) — crossing number c = 5

The idea is that higher-generation leptons are more "knotted" vortex rings, and the knotting energy contributes to the total mass.

### 3.2 Knot Energies

In classical knot theory, the **Möbius energy** and related conformal knot energies provide lower bounds on the bending energy of a knotted curve. For prime knots, the minimal ropelength (the ratio of knot length to thickness needed to tie the knot) grows with crossing number. The minimal ropelength for the unknot is 2π, for the trefoil is ≈16.4, and for the cinquefoil is ≈24.1.

If mass scales with the minimal ropelength $L_{\text{rope}}(c_n)$:

$$m_n/m_e = L_{\text{rope}}(c_n) / L_{\text{rope}}(0)$$

| Knot | c | $L_{\text{rope}}$ | Predicted ratio | Observed ratio |
|------|---|-------------------|-----------------|----------------|
| Unknot | 0 | 6.28 | 1 | 1 |
| Trefoil | 3 | 16.4 | 2.6 | 206.8 |
| Cinquefoil | 5 | 24.1 | 3.8 | 3477 |

**Verdict: FAIL.** Ropelength grows too slowly with crossing number. The muon would need a crossing number of several hundred to match $m_\mu/m_e \approx 207$ under linear ropelength scaling.

### 3.3 Exponential Knot Energy

If the vortex self-energy grows exponentially with knot complexity — perhaps because each additional crossing introduces topological constraints that multiply rather than add:

$$m_n \propto \exp(\kappa \cdot c_n)$$

Fitting κ from the electron-to-muon step:

$$\kappa = \frac{\ln(m_\mu/m_e)}{c_{\text{trefoil}} - c_{\text{unknot}}} = \frac{\ln(206.8)}{3} \approx 1.78$$

This predicts:

$$\frac{m_\tau}{m_e} = \exp(\kappa \cdot 5) = \exp(8.90) \approx 7260, \quad m_\tau \approx 3.7 \text{ GeV}$$

| Predicted | Observed | Error |
|-----------|----------|-------|
| 3.7 GeV   | 1.78 GeV | Factor 2.1 overprediction |

**Verdict: PARTIAL FAIL — qualitatively intriguing, quantitatively off by factor ~2.** The exponential ansatz captures the rapid growth but overpredicts the tau mass. The "coupling" κ derived from the e→μ step is too strong for the μ→τ step, suggesting either that the exponential scaling saturates or that the effective crossing-number difference between generations is smaller than the naive assignment c = {0, 3, 5}.

### 3.4 Power-Law Fits

We systematically test $m_n \propto c_n^k$:

| k | $m_\mu/m_e$ predicted | $m_\tau/m_e$ predicted | Residual |
|---|----------------------|----------------------|----------|
| 1 | 3 | 5 | Completely wrong |
| 2 | 9 | 25 | Completely wrong |
| 3 | 27 | 125 | Completely wrong |
| log(206.8)/log(3) ≈ 4.85 | 206.8 | ~2450 | 29% low for τ |

The power $k \approx 4.85$ fits the muon by construction but undershoots the tau by ~29%. No integer power works.

**Verdict: FAIL.** Power-law scaling in crossing number cannot fit both mass ratios simultaneously.

---

## 4. Approach 3: Helicity and Self-Linking

### 4.1 Hydrodynamic Helicity

For vortex configurations with linking between vortex lines, the helicity

$$H = \int \mathbf{v} \cdot (\nabla \times \mathbf{v})\,d^3x$$

is a conserved topological invariant. For linked vortex rings, $H \propto n_{\text{link}} \Gamma^2$. If each generation corresponds to a linked configuration with $n_{\text{link}} = n$, then:

$$m_n \propto H_n^{1/2} \propto n$$

This recovers the linear scaling of §2.2 — already ruled out.

### 4.2 Self-Linking Number

The Călugăreanu-White formula relates the self-linking number (Sl), writhe (Wr), and twist (Tw) of a ribbon:

$$\text{Sl} = \text{Wr} + \text{Tw}$$

For a closed vortex with internal twist (e.g., a framed knot), Sl is an integer topological invariant. If generations differ in Sl:

- For the unknot, Sl = 0 (framing 0)
- For a framed trefoil, Sl can take various values depending on framing

But the energy associated with self-linking scales linearly with Sl², and the observed ratios require large Sl differences incompatible with low-generation knot assignments.

**Verdict: FAIL.** Helicity and self-linking produce the same linear/quadratic scaling problems as the circulation quantum number approach.

---

## 5. Approach 4: Renormalization Group Running

### 5.1 The Degeneracy Hypothesis

The most promising framework recognizes that the mass ratios are **not** determined by a single topological invariant at low energies alone. Instead:

- **At the Planck scale** ($M_P \approx 1.22 \times 10^{19}$ GeV), all three generations are **degenerate**: $m_e = m_\mu = m_\tau = m_0$.
- The mass hierarchy **emerges through RG flow** as the energy scale is lowered from $M_P$ to the lepton mass scale.
- The topological invariants determine the **RG flow rate** for each generation, not the masses directly.

### 5.2 Vortex Self-Energy Running

In the vortex picture, the running of the mass is driven by the scale-dependence of the vortex aspect ratio $\alpha(Q^2)$ and the effective coupling $g(Q^2)$. The one-loop RG equation for the lepton mass has the form:

$$\frac{d\ln m_n}{d\ln Q} = -\gamma(g(Q^2))$$

where γ is the anomalous dimension, which may depend on the topological quantum numbers of the n-th generation.

If each generation has a distinct anomalous dimension $\gamma_n$, then integrating from $M_P$ down to the lepton mass scale $m_n$:

$$\frac{m_n}{m_0} = \exp\left(-\int_{\ln m_n}^{\ln M_P} \gamma_n(g(t))\,dt\right)$$

### 5.3 Topological Encoding of γ

The key hypothesis: the anomalous dimension γ depends on the topological invariants of the vortex configuration. For example:

$$\gamma_n = \gamma_0 \cdot f(c_n, H_n, \text{Sl}_n)$$

where $f$ is a function of the knot crossing number, helicity, and self-linking number.

If $f$ is approximately constant (dominant topological contribution) for each generation and the running is logarithmic, we get a multiplicative structure. The observed mass ratios $m_\mu/m_e \approx 207$ and $m_\tau/m_e \approx 3477$ require:

$$\gamma_2 - \gamma_1 \approx \frac{\ln(206.8)}{\ln(M_P/m_\mu)} \approx \frac{5.33}{39.2} \approx 0.136$$

$$\gamma_3 - \gamma_2 \approx \frac{\ln(16.8)}{\ln(M_P/m_\tau)} \approx \frac{2.82}{36.6} \approx 0.077$$

These are **small** differences in anomalous dimensions — of order 10% — suggesting that even subtle topological distinctions between generations can produce large mass hierarchies through the enormous lever arm $\ln(M_P/m_e) \approx 46$.

### 5.4 Plausibility Check

| Observable | Predicted (degenerate start) | Observed |
|-----------|------------------------------|----------|
| $m_\mu/m_e$ | $\exp[(\gamma_2-\gamma_1)\ln(M_P/m_\mu)]$ | 206.8 |
| $m_\tau/m_\mu$ | $\exp[(\gamma_3-\gamma_2)\ln(M_P/m_\tau)]$ | 16.8 |
| $\Delta\gamma_{21}$ | — | ≈0.136 |
| $\Delta\gamma_{32}$ | — | ≈0.077 |
| $\Delta\gamma_{21}/\Delta\gamma_{32}$ | — | ≈1.77 |

The ratio $\Delta\gamma_{21}/\Delta\gamma_{32} \approx 1.77$ should be compared to ratios of topological invariants. With knot crossing numbers {0, 3, 5}:

$$\frac{c_\mu - c_e}{c_\tau - c_\mu} = \frac{3}{2} = 1.50$$

The agreement is within ~15% — intriguing but not precise.

With ropelength {6.28, 16.4, 24.1}:

$$\frac{L_\mu - L_e}{L_\tau - L_\mu} = \frac{10.12}{7.70} \approx 1.31$$

Within ~25%.

**Verdict: QUALIFIED SUCCESS.** The RG framework provides a plausible explanation for why the mass hierarchy exists at all (degenerate UV, topology-dependent flow to IR), and the knot-crossing-number differences are in the right ballpark to explain the ratio of anomalous-dimension differences. But the RG equations for vortex configurations have not been derived from first principles, making this a sketch rather than a calculation.

---

## 6. Comparison with Koide Formula (APH-9.3)

In APH-9.3, an attempt was made to derive the observed lepton mass hierarchy from a vortex-topological mass matrix of the form:

$$H_{ij} = (A - B)n_i^2\delta_{ij} + B n_i n_j$$

with generations $n_i = (1,2,3)$ and interaction ratio $r = B/A \approx 0.934827$. This gave eigenvalues (0.08875, 0.36499, 13.54626) which do not reproduce the observed hierarchy (1:207:3477). The mismatch was left for APH-9.4 and subsequent subtasks.

The present analysis (§5) clarifies why this failed: **the mass matrix approach assumes the masses are determined by a single-scale calculation at the lepton mass scale.** In the RG picture, the masses are the result of 46 orders of magnitude of running from $M_P$ down to $m_e$. A tree-level mass matrix cannot capture this running — at best, it provides the UV boundary condition (degenerate masses) or the anomalous-dimension structure.

---

## 7. What Works and What Doesn't

### 7.1 Successes

| Claim | Status | Notes |
|-------|--------|-------|
| Three generations = three distinct vortex topologies | **Plausible** | Knot types {unknot, trefoil, cinquefoil} provide a natural 3-state system |
| α is universal across generations | **Supported** | All leptons share the same electromagnetic coupling; the vortex aspect ratio is fixed by QED |
| Mass hierarchy requires an additional quantum number beyond α | **Demonstrated** | The Compton wavelength scale (or equivalently the ring radius) must differ across generations |
| RG running as the mechanism for hierarchy generation | **Conceptually sound** | Degenerate UV → hierarchy from topology-dependent anomalous dimensions |
| Ratio of anomalous-dimension differences correlates with crossing-number ratio | **Suggestive** | $\Delta\gamma_{21}/\Delta\gamma_{32} \approx 1.77$ vs $c$ ratio 1.50 |

### 7.2 Failures

| Claim | Status | Notes |
|-------|--------|-------|
| $m_n \propto n$ from circulation quantum number | **Ruled out** | Factor 100+ off |
| $m_n \propto n^2$ from fixed-radius variable-circulation | **Ruled out** | Factor 50+ off |
| $m_n \propto c_n$ (linear in crossing number) | **Ruled out** | Factor 70+ off |
| $m_n \propto \exp(\kappa c_n)$ with constant κ | **Quantitatively off** | Overpredicts tau mass by factor ~2 |
| Single topological invariant determines mass directly | **Ruled out** | Ratios too large for simple scaling |
| Tree-level mass matrix from vortex interactions | **Ruled out** | Cannot capture 46-decade RG running |

### 7.3 Open Questions

1. **Deriving the anomalous dimension γ_n from vortex topology.** What is the explicit functional form $\gamma_n = f(c_n, H_n, \text{Sl}_n, \alpha)$? This requires a quantum field theory of vortex rings — a theory that does not yet exist.

2. **The mixing between generations.** CKM and PMNS mixing suggest that the mass eigenstates are not identical to the topological eigenstates. How does vortex topology encode flavor mixing?

3. **Neutrino masses.** If charged leptons correspond to knotted vortex rings, what topological configuration corresponds to neutrinos? The extreme mass suppression ($m_\nu/m_e \lesssim 10^{-7}$) would require either near-zero anomalous dimension differences or a fundamentally different topological class.

4. **The Koide formula.** The empirical Koide relation $(\sqrt{m_e} + \sqrt{m_\mu} + \sqrt{m_\tau})/(m_e + m_\mu + m_\tau) = 2/3$ holds to within experimental error. Can vortex topology explain this precise relation? It suggests an underlying symmetry structure not captured by any of the topological invariants explored here.

5. **Why three generations?** Knot theory provides infinitely many prime knots. Why does nature select exactly three? This may point to a deeper constraint — e.g., the number of compact dimensions in a string-theoretic embedding, or the dimensionality of the representation space of some gauge group.

---

## 8. Synthesis and Path Forward

The vortex model provides an elegant geometric picture of leptons but does not yet yield quantitative mass ratios. The central insight is that **topological invariants do not directly set the masses — they set the anomalous dimensions that govern the RG flow from a degenerate UV fixed point.** This shifts the problem from "what is the mass of each vortex state?" to "how does the vortex self-energy run with scale?"

The immediate next steps are:

| Priority | Task | Description |
|----------|------|-------------|
| **P0** | APH-9.18 | Compute vortex self-energy at one loop in an effective field theory of knotted vortex rings |
| **P1** | APH-9.19 | Classify all vortex configurations consistent with spin-1/2, charge −1, and renormalizability |
| **P2** | APH-9.20 | Derive the anomalous dimension γ_n from the knot-type dependence of the vortex propagator |
| **P3** | APH-9.21 | Test whether the Koide formula emerges naturally from the RG structure |

The task APH-9.17 has achieved its goal: it has systematically tested candidate topological invariants for direct mass prediction, ruled out naive scaling, and identified the RG-running framework as the most promising direction. The mass ratios remain unexplained in quantitative detail, but the conceptual landscape is now mapped.

---

## References (Internal)

1. APH-9.3: Koide formula from vortex topology — mass matrix approach with H_ij
2. Hestenes, D. (2019). Electron as a lightlike helical vortex. arXiv:1910.11085
3. APH-1.0: α as vortex aspect ratio — foundational parameterization of the α-π-Helix framework
4. Memory: α emerges as r_e/ƛ̄, the vortex core radius to ring radius ratio

## References (External — Conceptual)

5. Moffatt, H.K. (1969). The degree of knottedness of tangled vortex lines. *J. Fluid Mech.* 35, 117–129. [Helicity as a conserved topological invariant]
6. Ricca, R.L. & Moffatt, H.K. (1992). The helicity of a knotted vortex filament. In *Topological Aspects of the Dynamics of Fluids and Plasmas*. [Knot-type dependence of vortex energy]
7. Freedman, M.H., He, Z.-X., & Wang, Z. (1994). Möbius energy of knots and unknots. *Annals of Mathematics* 139(1), 1–50. [Conformal knot energies]
8. Particle Data Group (2024). Review of Particle Physics. *Prog. Theor. Exp. Phys.* 2024. [Lepton mass measurements]
9. Koide, Y. (1983). A fermion-boson composite model of quarks and leptons. *Phys. Lett. B* 120, 161–165. [Original Koide formula]

---

*Document prepared for the α-π-Helix project, Phase 9 subtask 17. All errors in reasoning are the author's responsibility. The openness about failures is by design — the purpose of APH-9.17 is not to claim a solution but to map the problem space honestly.*
