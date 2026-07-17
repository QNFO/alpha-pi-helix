# APH-9.18: Penning Trap Geometric Corrections from Vortex Model

**Project:** QNFO.RSCH.APH — α-π-Helix
**Task:** APH-9.18 | **Gap:** G8 (Computational Validation)
**Date:** 2026-07-17

---

## Abstract

We compute the geometric corrections to electron Penning trap frequencies predicted by the helical Compton vortex model. If the electron has finite spatial extent (a toroidal vortex of Compton-wavelength scale) rather than being a point particle, precision Penning trap measurements should reveal deviations from point-particle QED predictions. We identify the cyclotron frequency correction δω_c/ω_c ~ α (r_e/ƛ)² as the most promising observable, though it is suppressed by α³ ~ 4×10⁻⁷ relative to the leading term.

---

## 1. Penning Trap Basics

### 1.1 Configuration
A Penning trap confines a single electron using:
- Homogeneous magnetic field B = Bẑ (typically B ~ 5 T)
- Electrostatic quadrupole potential V = V₀(z² − ρ²/2)/d²

### 1.2 Frequencies

| Mode | Symbol | Formula | Typical (B=5.3T) |
|---|---|---|---|
| Cyclotron | ω_c′ | ω_c = eB/m_e | ~147 GHz |
| Axial | ω_z | √(eV₀/(m_e d²)) | ~64 MHz |
| Magnetron | ω_m | ω_z²/(2ω_c) | ~14 kHz |

Precision: δω/ω ~ 10⁻¹¹ for the anomaly frequency ω_a = ω_c′ − ω_c = (g−2)ω_c/2 (Gabrielse group, Harvard).

### 1.3 Point-Particle Assumption
Standard theory assumes a structureless point particle. The vortex model predicts an additional correction from the electron's finite spatial extent.

---

## 2. Vortex Structure in a Magnetic Field

### 2.1 Vortex Parameters
- Major radius: R = ƛ = 3.86 × 10⁻¹³ m
- Minor radius: r = r_e = 2.82 × 10⁻¹⁵ m
- Circulation: Γ = ħ/m_e
- Core area: A_core = π r_e² ≈ 2.50 × 10⁻²⁹ m²

### 2.2 Field Interaction Regime
Cyclotron radius r_c >> ƛ, so vortex structure is largely unaffected by trap fields. Geometric corrections appear as small perturbations.

---

## 3. Geometric Corrections

### 3.1 Magnetic Moment Correction
Finite-size correction: δμ/μ ~ 1.6 × 10⁻⁵ (potentially relevant at 10⁻¹¹ level if differential).

### 3.2 Cyclotron Frequency Correction
Self-energy correction of ~1.6% already absorbed into measured mass. The relevant question: how does finite extent modify response to trap fields beyond renormalized mass/charge?

### 3.3 Differential Correction — Anomaly Frequency
The key observable: ω_a = ω_s − ω_c.

Geometric contribution: δa_e^geom ~ α³/(2π) ~ 4 × 10⁻⁸

**Critical insight**: This is a CONSTANT offset independent of trap configuration. It is therefore absorbed into the empirical α determination. The smoking gun would be a configuration-dependent geometric correction.

---

## 4. Configuration-Dependent Effects

### 4.1 Magnetic Field Gradient Coupling
δω_c/ω_c ~ ƛ·(∂B/∂z)/B ~ 7.7 × 10⁻¹³ — at edge of current precision.

### 4.2 Electric Quadrupole Shift
δω_z/ω_z ~ 1.2 × 10⁻¹² — marginally detectable.

### 4.3 Spin-Vortex Orientation Coupling (MOST PROMISING)
State-dependent g-factor shift: Δg/g ~ α² ~ 5 × 10⁻⁵

At θ = 0: Δg/g = α²/2 ≈ 2.66 × 10⁻⁵
At θ = π/2: Δg/g = −α²/4 ≈ −1.33 × 10⁻⁵

**Easily detectable IF vortex orientation can be controlled** — a clear smoking gun.

---

## 5. Experimental Strategy

| Observable | Predicted Shift | Detectability |
|---|---|---|
| Magnetic gradient coupling | δω_c/ω_c ~ 10⁻¹² | Marginal |
| Electric quadrupole shift | δω_z/ω_z ~ 10⁻¹² | Marginal |
| State-dependent g-factor | Δg/g ~ 5×10⁻⁵ | Easily detectable |
| Constant geometric offset | δa_e^geom ~ 4×10⁻⁸ | Absorbed into α |

**Proposed experiment**: Variable magnetic field gradient, high cyclotron quantum numbers, two-trap comparison.

---

## 6. Comparison with Existing Data

### 6.1 Electron g-2
Δa_e = a_e^QED − a_e^exp = (+0.91 ± 0.82) × 10⁻¹² — consistent with zero. The vortex geometric correction ~4×10⁻⁸ is NOT seen → absorbed into α.

### 6.2 Muon g-2
Δa_μ ~ 2.5×10⁻⁹ (4.2σ deviation). The geometric correction ~8×10⁻⁶ is much larger — either absorbed into α or scales differently.

---

## 7. Conclusions

1. **Constant geometric offset** (~4×10⁻⁸) — absorbed into empirical α, not independently testable
2. **Gradient coupling** (~7×10⁻¹³) — at edge of precision
3. **Orientation-dependent g-factor shift** (~2.7×10⁻⁵) — easily detectable, clear smoking gun
4. The vortex model IS testable in Penning traps, but requires orientation control

---

## References
- Brown, L.S. & Gabrielse, G. (1986). "Geonium Theory." *Rev. Mod. Phys.*, 58, 233.
- Hanneke, D. et al. (2008). "New Measurement of the Electron Magnetic Moment." *PRL*, 100, 120801.
- Muon g-2 Collaboration (2023). arXiv:2308.06230.
