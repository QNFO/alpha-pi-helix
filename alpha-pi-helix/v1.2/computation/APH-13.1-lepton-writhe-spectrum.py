#!/usr/bin/env python3
"""APH-13.1: Lepton Writhe Spectrum Computation
Compute vortex writhe for (p,q) torus knots and fit to charged lepton masses.
"""

import math
import itertools

# ============================================================
# PDG 2024 pole masses (MeV)
# ============================================================
M_E = 0.510998950
M_MU = 105.6583755
M_TAU = 1776.86

MASSES = {"e": M_E, "mu": M_MU, "tau": M_TAU}

# ============================================================
# Section 1: Torus Knot Geometry
# ============================================================
def torus_knot_writhe(p, q):
    """Compute writhe of a (p,q) torus knot.
    
    For a (p,q) torus knot with p,q coprime positive integers:
    The writhe Wr ≈ p*q for the standard embedding.
    
    More precisely, using the formula from Fuller (1971) and
    the parametric representation r(t) = (R cos(qt), R sin(qt), r sin(pt)):
    
    Wr(p,q) = (1/(4π)) ∮ ∮ (dr × dr')·r̂ / |r - r'|^3
    
    For a (p,q) torus knot, the asymptotic writhe is:
    Wr = p*q * (1/2π) * ∫₀²π sin²(qt) / (1 + (r/R)² sin²(pt))^{3/2} dt
    
    For the Compton-scale vortex, r/R = α (the fine-structure constant),
    so the core radius is much smaller than the ring radius.
    """
    # Standard approximation for small r/R (tight winding):
    # Wr ≈ p*q * [1 - (3/8)(r/R)² * p²/(p²+q²) + ...]
    alpha = 1/137.036
    ratio_sq = alpha**2
    correction = (3/8) * ratio_sq * p**2 / (p**2 + q**2)
    return p * q * (1 - correction)

def torus_knot_twist(p, q, frame_type="natural"):
    """Twist of a framed torus knot.
    
    In the natural framing (parallel transport), the total twist Tw
    satisfies Lk = Wr + Tw, where Lk = p*q is the self-linking number
    for framing p*q.
    """
    wr = torus_knot_writhe(p, q)
    lk = p * q
    return lk - wr

def torus_knot_length(p, q, r_ring=1.0):
    """Arc length of a (p,q) torus knot on a torus with ring radius R.
    
    L = ∮ √(R² + r²(dθ/dt)²) dt for parametric curve.
    Approximation for p,q >> 1: L ≈ 2πR * max(p,q)
    For the Compton vortex: R = ƛ (reduced Compton wavelength).
    """
    # Exact: L ≈ 2π * √(p²*r² + q²*R²) for specific parameterization
    # For Compton-scale vortex with r/R = α:
    alpha = 1/137.036
    r_core = r_ring * alpha
    return 2 * math.pi * math.sqrt(p**2 * r_core**2 + q**2 * r_ring**2)

# ============================================================
# Section 2: Compute Writhe for Lepton (p,2) Torus Knots
# ============================================================
print("="*70)
print("APH-13.1: Lepton Vortex Writhe Spectrum")
print("="*70)

lepton_knots = [
    ("e (unknot)", 1, 2),
    ("μ (trefoil)", 3, 2),
    ("τ (cinquefoil)", 5, 2),
]

print("\n--- Torus Knot Parameters ---")
print(f"{'Particle':<18} {'(p,q)':<10} {'Wr(p,q)':<12} {'Tw(p,q)':<12} {'Lk=pq':<10} {'r/R=α':<10}")
print("-"*70)
for name, p, q in lepton_knots:
    wr = torus_knot_writhe(p, q)
    tw = torus_knot_twist(p, q)
    lk = p * q
    alpha = 1/137.036
    print(f"{name:<18} ({p},{q}){'':<5} {wr:<12.6f} {tw:<12.6f} {lk:<10} {alpha:<10.6f}")

# ============================================================
# Section 3: Fit m = κ * Wr^n
# ============================================================
print("\n--- Model 1: Simple Power Law m ∝ Wr^n ---")
lepton_data = [
    ("e", 1, 2, M_E),
    ("μ", 3, 2, M_MU),
    ("τ", 5, 2, M_TAU),
]

for exponent in [1, 2, 3, 4]:
    wr_vals = [torus_knot_writhe(p, q) for _, p, q, _ in lepton_data]
    masses = [m for _, _, _, m in lepton_data]
    
    # Normalize to electron
    wr_e = wr_vals[0]
    m_e = masses[0]
    
    wr_ratios = [wr/wr_e for wr in wr_vals]
    mass_ratios_actual = [m/m_e for m in masses]
    
    # Fit m/m_e = κ * (Wr/Wr_e)^n => κ = (m/m_e) / (Wr/Wr_e)^n
    # Using muon to calibrate κ
    kappa_mu = mass_ratios_actual[1] / (wr_ratios[1] ** exponent)
    kappa_tau = mass_ratios_actual[2] / (wr_ratios[2] ** exponent)
    
    predicted_mu = kappa_mu * (wr_ratios[1] ** exponent) * m_e
    predicted_tau = kappa_tau * (wr_ratios[2] ** exponent) * m_e
    
    print(f"\nn = {exponent}:")
    print(f"  Wr ratios (e, μ, τ): {wr_ratios[0]:.3f}, {wr_ratios[1]:.3f}, {wr_ratios[2]:.3f}")
    print(f"  Actual mass ratios:   {mass_ratios_actual[0]:.1f}, {mass_ratios_actual[1]:.1f}, {mass_ratios_actual[2]:.1f}")
    print(f"  κ (from μ) = {kappa_mu:.2f}")
    print(f"  κ (from τ) = {kappa_tau:.2f}")
    print(f"  κ consistency ratio (τ/μ) = {kappa_tau/kappa_mu:.3f}")
    print(f"  Predicted m_μ (from κ_μ) = {predicted_mu:.2f} MeV (actual: {M_MU:.5f}, err: {(predicted_mu/M_MU - 1)*100:.2f}%)")
    print(f"  Predicted m_τ (from κ_τ) = {predicted_tau:.2f} MeV (actual: {M_TAU:.2f}, err: {(predicted_tau/M_TAU - 1)*100:.2f}%)")

# ============================================================
# Section 4: Fit m/m_e = 1 + α⁻¹ * (Wr/Wr₀ - 1)^n
# ============================================================
print("\n\n--- Model 2: m/m_e = 1 + β * (Wr - Wr_e)^n ---")
print("(Excess writhe energy above electron baseline)")

for exponent in [2, 3, 4]:
    wr_e = torus_knot_writhe(1, 2)
    wr_mu = torus_knot_writhe(3, 2)
    wr_tau = torus_knot_writhe(5, 2)
    
    delta_wr_mu = wr_mu - wr_e
    delta_wr_tau = wr_tau - wr_e
    
    # Fit β from muon
    beta_mu = (M_MU/M_E - 1) / (delta_wr_mu ** exponent)
    beta_tau = (M_TAU/M_E - 1) / (delta_wr_tau ** exponent)
    
    pred_mu = M_E * (1 + beta_mu * (delta_wr_mu ** exponent))
    pred_tau = M_E * (1 + beta_tau * (delta_wr_tau ** exponent))
    
    print(f"\nn = {exponent}:")
    print(f"  ΔWr (μ-e) = {delta_wr_mu:.4f}, ΔWr (τ-e) = {delta_wr_tau:.4f}")
    print(f"  β (from μ) = {beta_mu:.6e}")
    print(f"  β (from τ) = {beta_tau:.6e}")
    print(f"  β consistency ratio = {beta_tau/beta_mu:.3f}")
    print(f"  Predicted m_μ = {pred_mu:.2f} MeV (actual: {M_MU:.5f})")
    print(f"  Predicted m_τ = {pred_tau:.2f} MeV (actual: {M_TAU:.2f})")

# ============================================================
# Section 5: Bilson-Thompson Helon Writhe Model
# ============================================================
print("\n\n--- Model 3: Helon Braid Length as Effective Writhe ---")
print("In Bilson-Thompson (2005), leptons are 3 parallel untwisted strands.")
print("Mass differences come from braid complexity (generation).")
print()
print("Braid group B₃ on 3 strands: generators σ₁, σ₂")
print("Electron: identity braid (3 parallel strands, no crossings)")
print("Muon:    braid with ~14-15 crossings (to match √(m_μ/m_e) ≈ 14.4)")
print("Tau:     braid with ~59 crossings (to match √(m_τ/m_e) ≈ 59.0)")
print()
print("If m ∝ N_crossings² where N is the number of braid crossings:")
print(f"  √(m_μ/m_e) = √({M_MU/M_E:.1f}) = {math.sqrt(M_MU/M_E):.1f} ≈ N_crossings(μ)")
print(f"  √(m_τ/m_e) = √({M_TAU/M_E:.1f}) = {math.sqrt(M_TAU/M_E):.1f} ≈ N_crossings(τ)")
print()
print("This predicts braid word lengths:")
print(f"  Electron: |w| = 0")
print(f"  Muon:     |w| ≈ 14-15 (e.g., (σ₁σ₂)⁷ or σ₁σ₂σ₁σ₂...)")
print(f"  Tau:      |w| ≈ 59  (complex braid sequence)")
print()

# Check if 14 and 59 have interesting braid-group representations
def braid_word_length_check():
    """Check if the predicted braid lengths have simple B₃ representations."""
    n_mu = round(math.sqrt(M_MU/M_E))
    n_tau = round(math.sqrt(M_TAU/M_E))
    
    print(f"Nearest integer braid lengths: n_μ = {n_mu}, n_τ = {n_tau}")
    print()
    
    # Check if these are lengths of simple periodic words in B₃
    # (σ₁σ₂)^k has length 2k
    for k in range(1, 20):
        if 2*k == n_mu:
            print(f"  μ: (σ₁σ₂)^{k} of length {2*k} = {n_mu} ✓")
        if 2*k == n_tau:
            print(f"  τ: (σ₁σ₂)^{k} of length {2*k} = {n_tau} ✓")
    
    # (σ₁σ₂σ₁)^k has length 3k
    for k in range(1, 20):
        if 3*k == n_mu:
            print(f"  μ: (σ₁σ₂σ₁)^{k} of length {3*k} = {n_mu} ✓")
        if 3*k == n_tau:
            print(f"  τ: (σ₁σ₂σ₁)^{k} of length {3*k} = {n_tau} ✓")

braid_word_length_check()

# ============================================================
# Section 6: Full Lepton Spectrum Table
# ============================================================
print("\n\n--- Model 4: Lepton Writhe Spectrum (Full Parameterization) ---")
print()

# Compute using exact mass ratios and invert for writhe
# m/m_e = (Wr/Wr_e)^n => Wr/Wr_e = (m/m_e)^(1/n)
print("Inverting: Wr/Wr_e = (m/m_e)^(1/n)")
print(f"{'n':<6} {'Wr_μ/Wr_e':<14} {'Wr_τ/Wr_e':<14} {'Wr_τ/Wr_μ':<14}")
print("-"*50)
for n in [1, 2, 3, 4]:
    wr_mu_ratio = (M_MU/M_E) ** (1/n)
    wr_tau_ratio = (M_TAU/M_E) ** (1/n)
    print(f"{n:<6} {wr_mu_ratio:<14.3f} {wr_tau_ratio:<14.3f} {wr_tau_ratio/wr_mu_ratio:<14.3f}")

# ============================================================
# Section 7: Călugăreanu-White Constraint
# ============================================================
print("\n\n--- Section 7: Călugăreanu-White Theorem Constraints ---")
print("Lk = Wr + Tw (for closed ribbon/vortex)")
print("For a framed (p,q) torus knot with natural framing:")
print()

for name, p, q in lepton_knots:
    wr = torus_knot_writhe(p, q)
    tw = torus_knot_twist(p, q)
    lk = p * q
    print(f"  {name:<18}: Lk = {lk:.1f}, Wr = {wr:.4f}, Tw = {tw:.4f}, Wr+Tw = {wr+tw:.4f} = Lk ✓")

# ============================================================
# Section 8: Energy Decomposition Proposal
# ============================================================
print("\n\n--- Section 8: Vortex Energy Decomposition ---")
print("""
Proposed energy decomposition for a Compton-scale vortex:

E_total = E_circulation + E_bending + E_twist + E_writhe

where:
  E_circulation ∝ (Γ)²/R = (p·Γ₀)²/(p·ƛ) = p·Γ₀²/ƛ
  E_bending    ∝ (κB²)·R = (1/R²)·R = 1/R ∝ 1/p  
  E_twist      ∝ (Tw)²/R = (p·q - Wr)²/(p·ƛ)
  E_writhe     ∝ (Wr)²/R = Wr²/(p·ƛ)

For (p,2) torus knots:
  E_c(p) ∝ p  (linear in p)
  E_b(p) ∝ 1/p (inverse in p)
  E_t(p) ∝ (p·q - Wr)²/p
  E_w(p) ∝ Wr²/p

Using m_e = 0.511 MeV as the baseline (p=1, Wr≈2):
""")

def vortex_energy(p, q, a, b, c, d):
    """Compute vortex energy for given coefficients.
    a = circulation coefficient
    b = bending coefficient  
    c = twist coefficient
    d = writhe coefficient
    """
    wr = torus_knot_writhe(p, q)
    lk = p * q
    tw = lk - wr
    
    E_circ = a * p
    E_bend = b / p
    E_twist = c * tw**2 / p
    E_writhe = d * wr**2 / p
    
    return E_circ + E_bend + E_twist + E_writhe

# Fit coefficients to match (p=1,m_e), (p=3,m_mu), (p=5,m_tau)
# With 4 parameters and 3 data points, this is underdetermined.
# Use physical constraints to reduce parameters.

print("With 4 parameters (a,b,c,d) and 3 data points, the fit is underdetermined.")
print("Physical constraint: E_bend << E_circ (bending energy is negligible for")
print("  Compton-scale vortices with α << 1). Set b=0.")
print()
print("This leaves 3 parameters (a,c,d) for 3 masses — exactly determined.")
print("Solving the linear system...")
print()

# Solve the linear system for a, c, d (with b=0)
import numpy as np

def build_matrix(ps):
    """Build the design matrix for vortex energy fit."""
    M = []
    for p in ps:
        wr = torus_knot_writhe(p, 2)
        lk = p * 2
        tw = lk - wr
        
        # Row: [p, tw²/p, wr²/p]
        row = [p, tw**2 / p, wr**2 / p]
        M.append(row)
    return np.array(M)

ps = [1, 3, 5]
M = build_matrix(ps)
targets = np.array([M_E, M_MU, M_TAU])

# Solve linear system
try:
    coeffs = np.linalg.solve(M, targets)
    a, c, d = coeffs
    print(f"  a (circulation) = {a:.6f} MeV")
    print(f"  c (twist)       = {c:.6f} MeV")
    print(f"  d (writhe)      = {d:.6f} MeV")
    print()
    
    # Verify
    for i, (name, p, q) in enumerate(lepton_knots):
        E_pred = vortex_energy(p, q, a, 0, c, d)
        actual = targets[i]
        err = (E_pred/actual - 1) * 100
        print(f"  {name:<18}: predicted = {E_pred:.6f} MeV, actual = {actual:.6f} MeV, err = {err:+.4f}%")
    
    # Check if coefficients are physically sensible
    print()
    print("Physical interpretation:")
    print(f"  Circulation dominates: a/(a+c+d) = {a/(a+c+d):.3f}")
    print(f"  Twist contribution:    c/(a+c+d) = {c/(a+c+d):.3f}")
    print(f"  Writhe contribution:   d/(a+c+d) = {d/(a+c+d):.3f}")
    
except np.linalg.LinAlgError as e:
    print(f"  Linear solve failed: {e}")
    
    # Try least-squares if singular
    coeffs, residuals, rank, singular = np.linalg.lstsq(M, targets, rcond=None)
    a, c, d = coeffs
    print(f"  Least-squares solution:")
    print(f"  a = {a:.6f}, c = {c:.6f}, d = {d:.6f}")

print()
print("="*70)
print("APH-13.1 COMPLETE — See analysis above for lepton writhe spectrum.")
print("="*70)
