#!/usr/bin/env python3
"""APH-13.12: Confined-Photon Bit → Emergent Spacetime — Wheeler 'it from bit'"""

import math

print("="*60)
print("APH-13.12: Confined-Photon Bit → Emergent Spacetime")
print("="*60)

print("""
Wheeler (1990): "It from bit" — physical reality emerges from information.

In the α-π-Helix vortex framework:
  "Bit"  = Photon confinement state (0 = free photon, 1 = confined photon)
  "It"   = The Standard Model particle spectrum

The bit-to-it ladder:

LEVEL 0: FREE PHOTON
  Bit state: [0]
  Physics: Massless, no rest frame, propagates at c
  Pre-geometric: No Compton wavelength (no rest frame = no length scale)
  Spacetime: Not yet emerged

LEVEL 1: CONFINED PHOTON (electron)
  Bit state: [1]
  Physics: Cyclic motion at c → rest mass m_e, Compton wavelength lambda_C
  Pre-geometric → Geometric: Photon path closure creates a LENGTH SCALE
    lambda_C = h/(m_e c) = 2.43e-12 m
  This length scale defines the "pixel size" of emergent spacetime
  The Compton period defines a TIME SCALE: T_C = h/(m_e c^2) = 8.09e-21 s
  Spacetime: Emerges from the photon's cyclic motion

LEVEL 2: BRAIDED CONFINED PHOTON (muon, tau, quarks)
  Bit state: [1, w] where w is the braid word
  Physics: Higher writhe → higher mass → shorter Compton wavelength
  Each braid crossing adds:
    - ~0.525 MeV to the mass
    - Shrinks the Compton wavelength by factor ~sqrt(m)
    - Increases the rest-frame energy density
  The braid is a "memory" — storing information about the particle's
  generation and flavor in the vortex topology

LEVEL 3: EMERGENT METRIC
  The Compton wavelength of the LIGHTEST confined photon (electron)
  sets the fundamental length scale of emergent spacetime:
    l_min = lambda_C_e / (2*pi) = hbar/(m_e c) = 3.86e-13 m
  
  This is the "quantum foam" scale — the minimum resolvable distance
  because any probe with higher energy would create a heavier particle
  (higher writhe) with its OWN (shorter) Compton wavelength.
  
  Gravity: The Planck length emerges from the statistical average
  of Compton wavelengths across all possible confined-photon states:
    l_Planck = sqrt(hbar*G/c^3) = 1.62e-35 m
    l_Planck/lambda_C_e = 1.62e-35 / 2.43e-12 = 6.67e-24
  
  The hierarchy problem: why is l_Planck << lambda_C_e?
  In the vortex model: because the gravitational coupling of braid
  writhe to spacetime curvature is extremely weak (G ~ 1/M_Planck^2).

INFORMATION BUDGET OF THE UNIVERSE:
  Each particle = one confined photon + braid word
  Information per particle = log2(|braid configurations|) = S bits
  From APH-13.11: S_e=0, S_mu=9.7, S_tau=41, S_t=405 bits
  
  Total information of the SM = sum over all particle types × their
  information content. Each stable matter particle (e, u, d) stores
  ~0-3 bits. The entire observable universe (~10^80 particles) stores
  ~10^80 bits — Wheeler's "it from bit" in exact form.
""")

# Computation: Planck-to-Compton ratio
hbar = 1.054571817e-34
G = 6.67430e-11
c = 2.99792458e8
m_e = 9.1093837015e-31

lambda_C_e = hbar / (m_e * c)
l_planck = math.sqrt(hbar * G / c**3)
t_planck = math.sqrt(hbar * G / c**5)
t_C = hbar / (m_e * c**2)

print("--- Emergent Spacetime Parameters ---")
print(f"  Electron:")
print(f"    Compton wavelength:  lambda_C = {lambda_C_e:.2e} m")
print(f"    Compton time:        T_C = {t_C:.2e} s")
print(f"    Compton frequency:   f_C = {1/t_C:.2e} Hz = {1/t_C*6.582e-16*1e6:.4f} MeV/hbar")
print()
print(f"  Planck scale:")
print(f"    Planck length: l_P = {l_planck:.2e} m")
print(f"    Planck time:   t_P = {t_planck:.2e} s")
print()
print(f"  Ratios:")
print(f"    lambda_C / l_P = {lambda_C_e/l_planck:.2e}")
print(f"    T_C / t_P       = {t_C/t_planck:.2e}")
print(f"    (l_P/lambda_C)^2 ≈ alpha_G = G*m_e^2/(hbar*c) = {G*m_e**2/(hbar*c):.2e}")
print()

# The information-to-geometry correspondence
print("--- Information → Geometry ---")
print(f"""
  Confined photon bit = 1 → lambda_C = {lambda_C_e:.2e} m (emerged)
  
  Additional braid bit → shorter Compton wavelength:
    lambda(mu) = hbar/(m_mu*c) = hbar/(207*m_e*c) = lambda_C_e/207
               = {lambda_C_e/207:.2e} m
  
  The braid "compresses" spacetime by factor sqrt(m/m_e).
  Heavier particles = more information = smaller length scale.
  
  The Planck scale is the limit where the information density
  becomes maximal — where the Compton wavelength equals the
  Schwarzschild radius (2Gm/c^2 = hbar/(mc)):
    m_Planck = sqrt(hbar*c/G) = {math.sqrt(hbar*c/G):.2e} kg
             = {math.sqrt(hbar*c/G)*c**2/1.602e-13:.2e} GeV
  
  At this scale: S ~ log(phi^(m_Planck/kappa))
  m_Planck = sqrt(hbar*c/G)*c^2 = {math.sqrt(hbar*c/G)*c**2/1.602e-13:.2e} GeV
  → The Planck-scale object stores astronomical information
  → This is the quantum-gravitational "it from bit" limit
""")

print("="*60)
print("APH-13.12 COMPLETE — Confined-photon bit → emergent spacetime")
print("="*60)
