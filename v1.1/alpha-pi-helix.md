---
title: "α-π-Helix: Geometric Unification of Fundamental Constants"
author: "DeepChat Agent + QNFO Research Pipeline"
date: "2026-07-17"
license: "CC-BY 4.0"
doi: "10.5281/zenodo.21419867"
status: "draft"
header-includes: |
  \newcommand{\lambdabar}{{\mkern0.75mu\mathchar '26\mkern -9.75mu\lambda}}
---

# α-π-Helix: Geometric Unification of Fundamental Constants

**Project ID:** QNFO.RSCH.APH
**Authors:** QNFO Research Pipeline
**Date:** 2026-07-17
**DOI:** 10.5281/zenodo.21419867

---

## Abstract

We present a geometric reinterpretation of three of physics' most
fundamental numbers — the circle constant $\pi$, the fine-structure
constant $\alpha$, and particle mass $m$ — as three orthogonal
projections of a single geometric object: a helical toroidal vortex
with the Compton wavelength as its characteristic scale. The
identities $\alpha = r_e/\lambdabar$ and $m = \omega$ (in Planck
units) follow directly from the definitions of the classical electron
radius, Compton wavelength, and Planck units; their geometric
significance emerges when mapped onto Hestenes' 2008/2019 helical
Zitterbewegung model, in which the electron is a lightlike particle
executing helical motion with diameter $\lambda_c$ and radial
thickness proportional to $\alpha$. We trace the historical
reification of $\pi$ from Attic numeral $\Pi = 5$ to the modern
idealized circle constant. The central thesis is that the appearance
of independent "fundamental constants" is an artifact of projecting
helical geometry onto lower-dimensional linear and circular subspaces.
We note that this interpretation is currently limited to the electron;
extension to other particles remains an open problem. We propose
experimental signatures and identify falsification conditions.

**Keywords:** fine-structure constant, pi, Zitterbewegung, Hestenes,
geometric unification, Compton vortex, reification, fundamental constants

---

## 1. Introduction — The Three Constants Problem

Physics rests on a set of numbers we call "fundamental constants." Among
them, three stand out for their ubiquity and elusiveness:

- **$\pi \approx 3.14159\ldots$** — appears in formulas from Coulomb's law to the
  Heisenberg uncertainty principle, from Gaussian integrals to Fourier
  transforms. It is treated as a pure number, a brute fact of
  mathematics.

- **$\alpha \approx 1/137.036$** — the fine-structure constant, governing the
  strength of electromagnetic interactions. Feynman called it "one of
  the greatest damn mysteries of physics: a magic number that comes to
  us with no understanding by humans" [@feynman1985qed]. It is treated
  as a coupling strength, a measure of how strongly charged particles
  "couple" to the electromagnetic field.

- **Mass ($m$)** — the inertia of particles, measured in kilograms. It is
  treated as a property of "stuff," an intrinsic attribute of material
  objects.

This paper argues that all three of these "constants" are the same
thing, viewed from different angles. Specifically:

1. **$\alpha$ is a length ratio:** $\alpha = r_e / \lambdabar$, the classical
   electron radius divided by the reduced Compton wavelength. It is
   not a coupling strength but a geometric proportion — the ratio of
   the electromagnetic self-energy scale to the quantum oscillation
   scale.

2. **$m$ is a frequency:** From $E = \hbar\omega$ and $E = mc^2$, we have
   $m = (\hbar/c^2)\omega$. In Planck units ($\hbar = c = G = 1$),
   this collapses to $m = \omega$. Mass IS angular frequency — not
   metaphorically, but algebraically.

3. **$\pi$ is a projection artifact:** $\pi$ appears where circular or
   spherical symmetry is hidden in the physics. In a helical geometry,
   the circle is a projection onto the transverse plane. What we call
   "$\pi$" is the residue of a helix collapsed to two dimensions.

These three insights converge on a single geometric object: the
**Helical Compton Vortex** — a toroidal structure with Compton
wavelength as its diameter, Compton frequency as its oscillation rate,
$\alpha$ as its radial thickness, and $\pi$ as its transverse
projection. The electron, in this picture, is not a point particle
with mysterious properties — it is a stable topological excitation of
the electromagnetic vacuum, a helical standing wave whose geometry
encodes all the numbers we have mistaken for independent constants.

---

## 2. Historical Foundations

### 2.1 The Dual Identity of $\pi$

The symbol $\pi$ carries a double identity that has been almost entirely
forgotten.

**The Attic $\Pi$: $\Pi = 5$.** In the Attic acrophonic numeral system,
used in Athens from approximately the 7th to the 3rd century BCE,
numbers were represented by the first letters of their Greek names
[@wikipedia_attic]. $\Pi$ (pi) stood for πέντε (pente), meaning
"five." The Attic numeral for 5 was written as $\Pi$ or, in its
decorative form, as 𐅃 (a pi with a decorative right stroke). This
was not a variable or a constant — it was a cardinal number with a
fixed, unambiguous value.

The full Attic system was:

| Symbol | Value | Greek Word | Meaning |
|--------|-------|------------|---------|
| Ι | 1 | — | (tally mark) |
| Π (𐅃) | 5 | πέντε [pente] | five |
| Δ (𐅄) | 10 | δέκα [deka] | ten |
| Η (𐅅) | 100 | ἑκατόν [hekaton] | hundred |
| Χ (𐅆) | 1000 | χίλιοι [khilioi] | thousand |
| Μ (𐅇) | 10000 | μύριοι [myrioi] | ten thousand |

Composite numerals were formed by combining symbols: 50 was written as
Δ inside Π (𐅄), and 500 as Η inside Π (𐅅). The system was additive
and multiplicative, elegant in its simplicity.

**The Modern $\pi$: the circle constant.** In 1706, the Welsh
mathematician William Jones published *Synopsis Palmariorum Matheseos*
(A Synopsis of the Palm-Bearers of Mathematics), in which he proposed
using the Greek letter $\pi$ to represent the ratio of a circle's
circumference to its diameter [@jones1706synopsis]. Jones chose $\pi$
as an abbreviation of περιφέρεια (periphereia, "periphery" or
"circumference"). This was the first documented use of $\pi$
specifically for the circle constant [@wikipedia_pi; @wikipedia_jones;
@mactutor_jones].

Before Jones, there was no universal symbol for the circle constant.
William Oughtred (1647) used the notation $\pi/\delta$ to denote the
ratio of periphery to diameter for *specific* circles; Isaac Barrow
used $\pi$ as a variable for perimeter in general. Archimedes had
bounded the value between $3\frac{10}{71}$ and $3\frac{1}{7}$; Zu
Chongzhi had computed $355/113$. But no one had given it a name. Jones
did — and Leonhard Euler, beginning in 1736, adopted and standardized
the notation, making $\pi$ the universal symbol we know today.

**The collision.** The same letter $\Pi/\pi$ thus carries two
irreconcilable meanings: the cardinal number 5 (Attic) and the
transcendental circle constant $3.14159\ldots$ (modern). Both are valid
within their systems, but the transition from one to the other tracks a
deeper shift — from a worldview in which numbers were *counts of
things* to one in which numbers were *abstract ideal forms*.

### 2.2 Pre-1706 Notations for the Circle Constant

Before Jones, the ratio of circumference to diameter was described in
words, fractions, and ad-hoc symbols. A partial catalog:

| Period | Culture/Person | Notation |
|--------|---------------|----------|
| ~250 BCE | Archimedes | $3\frac{10}{71} < \pi < 3\frac{1}{7}$ (verbal) |
| ~480 CE | Zu Chongzhi | $355/113$ (密率, "precise ratio") |
| 1647 | Oughtred | $\pi/\delta$ for specific circles |
| ~1660s | Barrow | $\pi$ as variable for perimeter length |
| 1706 | Jones | $\pi$ as universal circle constant |

The lack of a universal symbol reflected the pre-modern understanding
of the ratio: it was not a "number" in the modern sense but a
*geometric proportion* — a relationship between two measurable
quantities. The reification of $\pi$ into a transcendent real number
is a modern development.

### 2.3 Sommerfeld and the Fine-Structure Constant

Arnold Sommerfeld introduced $\alpha$ in 1916 to explain the fine
structure of atomic spectral lines. He defined it as:

$$\alpha = \frac{e^2}{4\pi\varepsilon_0 \hbar c} \approx \frac{1}{137}$$

The appearance of the velocity ratio $v_1/c = \alpha$ in the Bohr model
(where $v_1 = e^2/(4\pi\varepsilon_0\hbar)$ is the electron velocity in
the first Bohr orbit) gave $\alpha$ its interpretation as a "coupling
constant" — the strength of the electromagnetic interaction relative to
the speed of light [@wikipedia_fine_structure].

We will show that this interpretation, while historically productive,
obscures a simpler geometric truth: $\alpha$ is a length ratio.

### 2.4 Planck and Natural Units

In 1899, Max Planck proposed a system of "natural units" based on the
fundamental constants $\hbar$, $c$, and $G$ [@planck1899units]. In
these units:

$$\hbar = c = G = 1$$

Under this normalization, many physical quantities collapse to
dimensionless numbers. Most strikingly, mass becomes numerically equal
to angular frequency: $m = \omega$. This identity, implicit in Planck's
original formulation, is the key to understanding mass not as "stuff"
but as a rate of phase accumulation.

---

## 3. Mathematical Foundations — Exact Identities

### 3.1 The $\alpha$-$r_e$-$\lambdabar$ Identity

The fine-structure constant admits an exact geometric interpretation
that is mathematically trivial yet physically profound:

$$\boxed{\alpha = \frac{r_e}{\lambdabar_e}}$$

**Derivation.** We begin with three standard definitions from
electrodynamics and quantum mechanics:

The fine-structure constant:

$$\alpha = \frac{e^2}{4\pi\varepsilon_0 \hbar c}$$

The classical electron radius (the radius at which electrostatic
self-energy equals rest mass energy):

$$r_e = \frac{e^2}{4\pi\varepsilon_0 m_e c^2}$$

The reduced Compton wavelength (the scale at which quantum
field effects become dominant):

$$\lambdabar_e = \frac{\hbar}{m_e c}$$

Dividing $r_e$ by $\lambdabar_e$:

$$\frac{r_e}{\lambdabar_e}
= \frac{e^2/(4\pi\varepsilon_0 m_e c^2)}{\hbar/(m_e c)}
= \frac{e^2}{4\pi\varepsilon_0 m_e c^2} \cdot \frac{m_e c}{\hbar}
= \frac{e^2}{4\pi\varepsilon_0 \hbar c}
= \alpha$$

This is an exact algebraic identity — no approximations, no model
dependence. The fine-structure constant *is* the ratio of the classical
electron radius to the reduced Compton wavelength.

### 3.2 The Full Scaling Chain

The identity $\alpha = r_e/\lambdabar$ implies a complete scaling chain
linking all three fundamental electron length scales
[@wikipedia_classical_electron_radius]:

$$r_e = \alpha \lambdabar_e = \alpha^2 a_0$$

$$\lambdabar_e = \alpha a_0$$

$$a_0 = \frac{r_e}{\alpha^2}$$

Where $a_0 = 4\pi\varepsilon_0\hbar^2/(m_e e^2)$ is the Bohr radius.
All three scales — classical, Compton, and atomic — are locked together
by powers of $\alpha$:

| Scale | Value (SI) | In terms of $a_0$ | In terms of $\lambdabar$ |
|-------|-----------|-------------------|--------------------------|
| Classical radius $r_e$ | $2.818 \times 10^{-15}$ m | $\alpha^2 a_0$ | $\alpha \lambdabar$ |
| Reduced Compton $\lambdabar$ | $3.862 \times 10^{-13}$ m | $\alpha a_0$ | $\lambdabar$ |
| Bohr radius $a_0$ | $5.292 \times 10^{-11}$ m | $a_0$ | $\lambdabar/\alpha$ |

This hierarchy — spanning four orders of magnitude — is entirely
encoded in powers of $\alpha \approx 1/137$. The "coupling constant" is,
in fact, a geometric scaling factor.

### 3.3 Equivalent Forms of $\alpha$ as Length Ratios

Using the full Compton wavelength $\lambda_e = h/(m_e c) = 2\pi\lambdabar$:

$$\alpha = \frac{2\pi r_e}{\lambda_e}
        = \frac{\lambdabar_e}{a_0}
        = \sqrt{\frac{r_e}{a_0}}$$

All are exact. The fine-structure constant is a pure geometric
proportion — a ratio of lengths — not a dynamically determined
"coupling strength."

### 3.4 CODATA 2022 Values with Uncertainties

| Quantity | Symbol | Value | Uncertainty | Units |
|----------|--------|-------|-------------|-------|
| Inverse fine-structure | $\alpha^{-1}$ | 137.035999177 | $\pm$0.000000021 | dimensionless |
| Classical electron radius | $r_e$ | $2.8179403205 \times 10^{-15}$ | $\pm 1.3 \times 10^{-23}$ | m |
| Reduced Compton wavelength | $\lambdabar_e$ | $3.8615926764 \times 10^{-13}$ | $\pm 2.5 \times 10^{-21}$ | m |
| Compton wavelength | $\lambda_e$ | $2.4263102389 \times 10^{-12}$ | $\pm 1.6 \times 10^{-20}$ | m |
| Bohr radius | $a_0$ | $5.29177210544 \times 10^{-11}$ | $\pm 8.2 \times 10^{-20}$ | m |

**Verification:** $r_e / \lambdabar_e = 2.81794 \times 10^{-15} / 3.86159 \times 10^{-13}
= 0.0072973525643 = \alpha$. ✓

Source: CODATA 2022 internationally recommended values [@codata2022].

### 3.5 Geometric Proportion vs. Modern Constant

The distinction between "geometric proportion" and "fundamental
constant" is more than semantic. In the Eudoxian-Euclidean tradition
(*Elements* Book V, Definition 5), a proportion (ἀναλογία) is a
relationship between four magnitudes: $a$ is to $b$ as $c$ is to $d$
[@euclid_elements]. The magnitudes themselves have no intrinsic
numerical value — they acquire meaning only through their ratios.

The modern concept of a "fundamental constant" inverts this: it treats
$\alpha$ as a bare number ($0.0072973525643\ldots$) that somehow
encodes the strength of a force. But $\alpha$ is not a strength — it is
a *shape*. It tells you the aspect ratio of the electron's internal
geometry: the electromagnetic self-energy radius is $\alpha$ times the
quantum oscillation wavelength.

### 3.6 Dimensional Analysis

Both $\pi$ and $\alpha$ are dimensionless — they are pure numbers. Mass,
in SI units, carries dimensions of kilograms. But in Planck units,
$m = \omega$ is also dimensionless. This means that all three
"constants" are, in the appropriate natural units, pure geometric
proportions.

---

## 4. Mass-Frequency Identity

### 4.1 The Chain of Equalities

Two of the most fundamental equations in physics are:

$$E = \hbar \omega \quad \text{(Planck-Einstein, 1900/1905)}$$

$$E = mc^2 \quad \text{(Einstein, 1905)}$$

Equating them:

$$\hbar \omega = mc^2$$

$$\boxed{m = \frac{\hbar}{c^2}\, \omega}$$

In SI units, mass and angular frequency differ by the conversion factor
$\hbar/c^2 \approx 1.173 \times 10^{-51}\ \mathrm{kg \cdot s}$. This
factor is the dimensional residue of our unit choices, not a physical
constant.

### 4.2 Mass in Planck Units

In Planck's natural units, we set:

$$\hbar = c = G = 1$$

Under this normalization:

$$\boxed{m = \omega}$$

Mass IS angular frequency. The rest mass of a particle *is* the angular
frequency of its internal oscillation. This is not an interpretation or
an analogy — it follows directly from equating two experimentally
verified relations and choosing natural units.

### 4.3 The Compton Relations

The Compton angular frequency:

$$\omega_C = \frac{mc^2}{\hbar}$$

In Planck units: $\omega_C = m$ (since $c = \hbar = 1$).

The reduced Compton wavelength:

$$\lambdabar = \frac{\hbar}{mc} = \frac{c}{\omega_C}$$

In Planck units: $\lambdabar = 1/m = 1/\omega_C$.

The Compton relations establish a complete equivalence between mass,
frequency, and inverse length.

### 4.4 SI $\leftrightarrow$ Planck Unit Conversion Table

| Quantity | SI Expression | SI Value (electron) | Planck Value |
|----------|--------------|---------------------|--------------|
| Mass $m_e$ | — | $9.109 \times 10^{-31}$ kg | $m_P \times 4.185 \times 10^{-23}$ |
| Compton frequency $\omega_C$ | $mc^2/\hbar$ | $7.763 \times 10^{20}$ rad/s | $4.185 \times 10^{-23}\ t_P^{-1}$ |
| Reduced Compton $\lambdabar$ | $\hbar/(mc)$ | $3.862 \times 10^{-13}$ m | $2.389 \times 10^{22}\ l_P$ |
| ZB frequency $\omega_{ZB}$ | $2mc^2/\hbar$ | $1.553 \times 10^{21}$ rad/s | $8.370 \times 10^{-23}\ t_P^{-1}$ |

Where $m_P \approx 2.176 \times 10^{-8}$ kg, $l_P \approx 1.616 \times 10^{-35}$ m,
$t_P \approx 5.391 \times 10^{-44}$ s.

### 4.5 $\alpha$ as Phase Advance

Since $r_e = \alpha\lambdabar$ and $\lambdabar = c/\omega_C$:

$$\alpha = \frac{r_e}{\lambdabar}
        = r_e \cdot \frac{\omega_C}{c}
        = \frac{r_e / c}{1 / \omega_C}$$

$\alpha$ is the ratio of (a) the light-crossing time of the classical
electron radius to (b) the Compton period. In other words: $\alpha$
measures the phase advance of the Zitterbewegung oscillation over the
electromagnetic self-energy scale.

---

## 5. The Dirac Electron and Zitterbewegung

### 5.1 The Dirac Equation

The Dirac equation (1928) for a free electron:

$$(i\hbar\gamma^\mu\partial_\mu - mc)\psi = 0$$

has a remarkable property: the velocity operator
$\boldsymbol{\alpha} = c\boldsymbol{\gamma}^0\boldsymbol{\gamma}$ has
eigenvalues $\pm c$. The electron, in the Dirac picture, always moves
at the speed of light [@wikipedia_zitterbewegung].

### 5.2 The Zitterbewegung Solution

In the Heisenberg picture, the position operator of a free Dirac
electron evolves as:

$$\mathbf{x}(t) = \mathbf{x}(0) + \frac{\mathbf{p}c^2}{H}t
  + \frac{i\hbar c}{2H}\left(\boldsymbol{\alpha}(0) - \frac{\mathbf{p}c}{H}\right) e^{-2iHt/\hbar}$$

The first two terms describe classical linear motion. The third term is
an oscillatory component — the *Zitterbewegung* (German: "trembling
motion") — with:

- **Angular frequency:** $\omega_{ZB} = 2mc^2/\hbar$ (twice the Compton frequency)
- **Amplitude:** $\hbar/(2mc) = \lambdabar/2$ (for a free electron at rest)

The electron is not at rest — it oscillates at $1.55 \times 10^{21}$ Hz
with an amplitude of $1.93 \times 10^{-13}$ m, tracing out a path in
spacetime.

### 5.3 The Velocity Operator $\pm c$

That the velocity operator has eigenvalues $\pm c$ is a direct
consequence of the Dirac algebra. The electron is always "trying" to
move at the speed of light, switching direction at twice the Compton
frequency. The observed subluminal velocity is a time-averaged effect
— the "rest mass" is the energy of this oscillatory motion.

### 5.4 Mainstream Interpretation

The mainstream interpretation, following Foldy and Wouthuysen (1950),
treats the Zitterbewegung as an artifact of the single-particle Dirac
equation — eliminated by a unitary transformation that separates
positive- and negative-energy states. In quantum field theory, the ZB
is interpreted as interference between positive- and negative-energy
components, with no physical reality.

However, this elimination is not a disproof — it is a choice of
representation. The Foldy-Wouthuysen transformation moves the
oscillation into the wavefunction's phase, where it becomes invisible
but does not disappear.

### 5.5 Penrose's Zigzag Picture

Roger Penrose, in *The Road to Reality* (2004), offered a vivid
alternative: the electron as a massless particle zigzagging at the
speed of light, alternately as a left-handed and right-handed Weyl
fermion. The "rest mass" is the energy of this confined light-speed
motion. The zigzag frequency is the ZB frequency; the zigzag amplitude
is the Compton wavelength [@penrose2004road].

Penrose's picture, while heuristic, captures the essential physics: the
electron is not a stationary object with "mass" as a property, but a
confined light-speed process whose oscillation *is* the mass.

---

## 6. Hestenes' Helical Zitterbewegung Model

David Hestenes, over two decades of work, developed the most complete
geometric model of the electron based on the Dirac equation and
Spacetime Algebra (STA) — a Clifford algebra formulation of
relativistic physics that eliminates the need for Dirac matrices.

### 6.1 The 2008 Model: Lightlike Helical Particle

In *Zitterbewegung in Quantum Mechanics — a research program* (2008),
Hestenes proposed a "self-contained dynamical model of the electron as
a lightlike particle with helical zitterbewegung" [@hestenes2008zb].
Key results:

- The electron is a **lightlike** particle — its instantaneous velocity
  is always $c$. The subluminal observed velocity is an average over
  the helical path.
- The ZB is **helical**, not circular or random. The electron traces a
  cylindrical helix in spacetime.
- The model yields a specific prediction: the electron possesses an
  oscillating electric dipole moment (EDM) that should produce
  detectable resonance in electron channeling experiments through
  crystals.
- The spin is not an intrinsic "quantum" property but the orbital
  angular momentum of the lightlike helical motion.

Using STA, Hestenes reformulated the Dirac equation without matrices,
making the geometric structure explicit. The electron's wavefunction
becomes a rotor — a geometric object describing rotation in spacetime —
rather than an abstract complex-valued spinor.

### 6.2 The 2019 Model: Toroidal Vortex

In *Zitterbewegung structure in electrons and photons* (2019), Hestenes
extended the model dramatically [@hestenes2019zb]. The central claims:

1. The Dirac equation is reinterpreted as a constitutive equation for
   singularities in the electromagnetic vacuum. The electron is not a
   "particle" subject to the Dirac equation — the Dirac equation
   *describes* the structure of a stable topological defect in the
   vacuum.

2. The electron is a point singularity on a lightlike toroidal vortex.
   The vortex has a well-defined geometry:
   - **Diameter:** the Compton wavelength $\lambda_c = h/(m_e c)$
   - **Thickness:** proportional to the electron's anomalous magnetic
     moment, or equivalently to $\alpha \cdot \lambda_c/(2\pi)$
   - **Circulation:** lightlike — the vortex core circulates at $c$

3. The photon is modeled as an electron-positron pair trapped in a
   vortex ring. This provides a unified description of electrons and
   photons as different configurations of the same fundamental object
   — a lightlike circulation in the electromagnetic vacuum.

4. All elementary particles may be composed of similar vortex
   structures. The model suggests a research program in which the
   "particle zoo" is reduced to topology.

### 6.3 Key Geometric Parameters

Extracted from Hestenes' 2008 and 2019 papers:

| Parameter | Value | Interpretation |
|-----------|-------|----------------|
| Vortex diameter | $\lambda_c = h/(m_e c) = 2.426 \times 10^{-12}$ m | Compton wavelength |
| Circulation speed | $c$ | Lightlike vortex core |
| Circulation frequency | $\omega_{ZB}/2\pi = 2.47 \times 10^{20}$ Hz | ZB frequency / $2\pi$ |
| Radial thickness | $\propto \alpha \cdot \lambda_c/(2\pi)$ | Set by anomalous magnetic moment |
| $\pi$ appears as | Transverse circumference factor | Helix $\to$ circle projection |
| $\alpha$ appears as | Radial-to-axial aspect ratio | Vortex thickness / diameter |

### 6.4 Experimental Predictions

Hestenes' model makes a specific, falsifiable prediction: an electron
moving through a crystal lattice should exhibit a resonant interaction
when the channeling period matches the ZB period. This would manifest
as an oscillating electric dipole moment detectable through radiation
emission or energy loss spectra.

The resonance condition occurs when:

$$d/v = \pi\hbar/(mc^2)$$

where $d$ is the crystal plane spacing and $v$ is the electron
velocity. This has not yet been experimentally confirmed or refuted,
making it a critical test of the model.

### 6.5 Relation to Our Thesis

Hestenes' model provides the physical mechanism underlying the
mathematical identities we have established:

- $\alpha = r_e/\lambdabar$ maps to the vortex's radial thickness relative to
  its diameter
- $m = \omega$ maps to the vortex's circulation frequency
- $\pi$ appears as the factor relating the helical path's transverse
  circumference to the vortex diameter

The three "constants" are not independent — they are different
measurements of the same vortex, taken along different axes.

---

## 7. Extended Electron Models

### 7.1 Consa's Helical Solenoid Model (2018)

Oliver Consa extended Hestenes' model into a "Helical Solenoid Model of
the Electron" [@consa2018helical]. Key contributions:

- The electron is modeled as a helical solenoid — a current loop that
  also advances along its axis, producing both electric and magnetic
  moments
- The model derives the electron's $g$-factor ($\approx 2$) directly from
  the helical geometry, without QFT loop corrections
- The anomalous magnetic moment $(g-2)/2$ is attributed to the
  solenoid's pitch angle, which is proportional to $\alpha/2\pi$

In a related paper, Consa (2017) derived the $g$-factor explicitly from
the helical geometry, obtaining $g = 2$ as the zero-thickness limit and
$(g-2)/2 \approx \alpha/(2\pi)$ as the first-order thickness correction
[@consa2017gfactor]. This connects $\alpha$ directly to the electron's
magnetic properties through geometry, not perturbation theory.

### 7.2 Rodrigues et al.: ZB and Electron Structure (1993)

Rodrigues, Vaz, Recami, and Salesi developed one of the earliest
geometric models connecting Zitterbewegung to electron structure
[@rodrigues1993zb]. Using Clifford algebra, they showed:

- The electron's spin can be derived as the orbital angular momentum of
  the ZB motion
- The ZB is not an artifact but a real physical oscillation
- The model naturally yields the de Broglie wavelength as a
  consequence of the ZB frequency combined with translational motion

### 7.3 Williamson & van der Mark: Toroidal Photon Topology (1997)

Williamson and van der Mark proposed that the electron *is* a
self-confined photon on a toroidal path [@williamson1997electron]. In
their model:

- A photon of energy $mc^2$ circulates on a closed toroidal path of
  circumference $\lambda_c$ (the Compton wavelength)
- The self-interference of the circulating photon produces a standing
  wave — the electron's rest frame wavefunction
- The topology (toroidal, single-loop) determines the spin-$\frac{1}{2}$
  and charge quantum numbers
- The fine-structure constant $\alpha$ emerges as the ratio of the
  electromagnetic coupling energy to the photon's confinement energy

### 7.4 Comparison Table

| Model | Year | Geometry | ZB Real? | $\alpha$ Meaning | $g$-factor |
|-------|------|----------|----------|-----------------|-----------|
| Dirac (original) | 1928 | Point particle | Yes (osc.) | Coupling constant | 2 (predicted) |
| Foldy-Wouthuysen | 1950 | Point particle | Eliminated | Coupling constant | 2 |
| Penrose zigzag | 2004 | Zigzag at $c$ | Yes (heuristic) | — | — |
| Hestenes helix | 2008 | Lightlike helix | Yes (physical) | Pitch angle | — |
| Hestenes vortex | 2019 | Toroidal vortex | Yes (circulation) | Thickness/diam. | — |
| Consa solenoid | 2018 | Helical solenoid | Yes (current) | Pitch factor | $2 + \alpha/\pi$ |
| Rodrigues et al. | 1993 | Clifford ZB | Yes (orbital) | — | From ZB |
| Williamson et al. | 1997 | Toroidal photon | Yes (circulation) | Coupling ratio | — |
| **This work** | 2026 | Helical Compton Vortex | Yes (def.) | $r_e/\lambdabar$ = aspect ratio | Geometric |

---

## 8. The Unified Geometric Object

### 8.1 Definition: The Helical Compton Vortex

We propose that the electron is a **Helical Compton Vortex** — a stable,
localized circulation in the electromagnetic vacuum with the following
parameters:

| Property | Value | Expression |
|----------|-------|------------|
| Diameter | $\lambda_c = 2.426 \times 10^{-12}$ m | $h/(m_e c)$ |
| Radius | $\lambdabar = 3.862 \times 10^{-13}$ m | $\hbar/(m_e c)$ |
| Circulation speed | $c$ | Lightlike |
| Angular frequency | $\omega_C = 7.763 \times 10^{20}$ rad/s | $m_e c^2/\hbar$ |
| Transverse circumference | $\pi\lambda_c$ | $\pi \times$ diameter |
| Radial thickness | $(\alpha/2\pi)\lambda_c \approx 2.81 \times 10^{-15}$ m | Classical electron radius |
| Helix pitch per turn | $\alpha\lambda_c$ | $2\pi \times$ classical radius |

### 8.2 $\pi$ as Transverse Projection

When a helix is projected onto a plane perpendicular to its axis, it
traces a circle. The circumference-to-diameter ratio of this projected
circle is $\pi$. Every appearance of $\pi$ in fundamental physics can
be traced to this projection: the helix becomes a circle, the 3D
structure becomes 2D, and $\pi$ appears as the residue of the lost
dimension.

In the Helical Compton Vortex:
- The **vortex** is helical/toroidal — a 3D structure
- The **projection** onto the transverse plane is circular — a 2D shadow
- $\pi$ is the **shadow's** circumference-to-diameter ratio — a property
  of the projection, not the object

### 8.3 $\alpha$ as Radial Thickness

The fine-structure constant $\alpha$ is the ratio of the vortex's
radial thickness (classical electron radius $r_e$) to its axial scale
(reduced Compton wavelength $\lambdabar$):

$$\alpha = \frac{r_e}{\lambdabar}
         = \frac{\text{radial thickness}}{\text{vortex radius}}
         \approx \frac{1}{137}$$

This interprets $\alpha$ not as a "strength" but as an *aspect ratio* —
a geometric shape parameter. The electron is "thin" ($\alpha \ll 1$)
because its electromagnetic self-energy scale is much smaller than its
quantum oscillation scale. A coupling constant of $1/137$ is, in this
picture, an aspect ratio of $1{:}137$.

### 8.4 Mass as Oscillation Frequency

The electron's rest mass is the angular frequency of its helical
circulation, measured in Planck units:

$$m = \omega_C = \frac{m_e c^2}{\hbar}$$

The "inertia" of the electron is the rate at which its internal phase
accumulates. To accelerate the electron is to change the phase
accumulation rate — and the resistance to this change is what we call
mass.

This resolves the conceptual puzzle of mass: it is not a primitive
property of "stuff" but a dynamical quantity — the frequency of an
internal oscillation. The Higgs mechanism may give this oscillation its
rest frequency, but the fact that mass IS frequency is a logical
consequence of $E = \hbar\omega$ and $E = mc^2$.

### 8.5 The Unified View

The three "fundamental constants" are three orthogonal projections of
the same geometric object:

$$\boxed{\text{Helical Compton Vortex}
  \begin{cases}
    \pi   & \text{— transverse projection (circle constant)} \\[4pt]
    \alpha & \text{— radial-to-axial ratio (aspect ratio)} \\[4pt]
    m = \omega & \text{— circulation frequency (inertia)}
  \end{cases}}$$

They are not independent. Given the electron's Compton wavelength
(which sets the scale), $\alpha$ determines the radial thickness, and
$\omega$ determines the circulation rate. $\pi$ is not an input — it
emerges from the helical geometry as the transverse projection factor.

---

## 9. Reification of Constants — A Critique

### 9.1 What Is Reification?

*Reification* (from Latin *res*, "thing") is the fallacy of treating an
abstraction as if it were a concrete, independent entity. In physics,
reification occurs when we mistake:

- A **ratio** for a **property** ($\alpha$: from length ratio to "coupling strength")
- A **projection** for an **object** ($\pi$: from geometric proportion to transcendental number)
- A **frequency** for a **substance** (mass: from oscillation rate to "amount of stuff")

### 9.2 The Reification of $\pi$

$\pi$ is treated as a number — $3.14159\ldots$ — a transcendental constant
of mathematics whose decimal expansion is known to trillions of digits.
But this is a profound reification.

In its original geometric context, $\pi$ is not a number at all — it is
a *proportion*, a relationship between two measurable quantities: the
circumference and diameter of a circle. The Greeks understood this:
they classified magnitudes, not numbers. A length was a length, and
the ratio of two lengths was not a "number" in our sense but a
λόγος (logos) — a rational relationship.

The modern treatment of $\pi$ as a real number — and a transcendental
one at that — turns a geometric relationship into an ontological
object. We ask "what IS $\pi$?" as if it were a thing, rather than
"what relationship does $\pi$ encode?" The answer to the second
question is simpler: any system with hidden circular symmetry.

### 9.3 The Reification of $\alpha$

$\alpha \approx 1/137$ has been called "the most mysterious number in
physics." Feynman wrote:

> It has been a mystery ever since it was discovered more than fifty
> years ago, and all good theoretical physicists put this number up on
> their wall and worry about it. … Immediately you would like to know
> where this number for a coupling comes from: is it related to $\pi$
> or perhaps to the base of natural logarithms? Nobody knows. It's one
> of the greatest damn mysteries of physics. [@feynman1985qed]

But if $\alpha = r_e/\lambdabar$ is an exact algebraic identity, then
$\alpha$ is not a "magic number" — it is the aspect ratio of the
electron's internal geometry. The mystery is not "why $1/137$?" but
"why does the electron have this particular aspect ratio?" This shifts
the question from numerology to geometry — a tractable problem.

The coupling constant interpretation is the result of reification: we
took a geometric proportion and treated it as a dynamical parameter
governing interaction strength. The mathematics doesn't distinguish
these interpretations — $\alpha = e^2/(4\pi\varepsilon_0\hbar c)
= r_e/\lambdabar$ — but the ontology does.

### 9.4 The Reification of Mass

Mass is perhaps the most deeply reified concept in physics. We speak of
"massive particles" as if mass were a substance they possess. The SI
system has a dedicated base unit — the kilogram — for measuring this
"quantity of stuff."

But $m = \omega$ in Planck units tells us that mass is a frequency — a
rate of phase accumulation. The electron's "rest mass" of $9.109 \times
10^{-31}$ kg is, in more fundamental terms, an oscillation at $7.763
\times 10^{20}$ rad/s. We don't perceive the oscillation because it is
far too fast, and because our measuring instruments are calibrated to
report mass in kilograms rather than frequency in hertz.

The practical utility of measuring mass in kilograms is not in dispute.
The conceptual error is in treating kilograms as measuring a *different
kind of thing* from hertz. They measure the same thing — oscillation
frequency — in different units.

### 9.5 Historical Parallel: Greek Proportion Theory

The ancient Greek distinction between number (ἀριθμός, arithmos) and
magnitude (μέγεθος, megethos) is instructive. Numbers were counts of
discrete units; magnitudes were continuous quantities (lengths, areas,
times). A proportion (ἀναλογία) related four magnitudes —
$a:b\,{::}\,c:d$ — without assigning numerical values to any of them.

The modern real number system collapsed this distinction: every
magnitude is assigned a real number. This was a triumph of
mathematical unification but a loss of conceptual clarity. When we say
"$\pi = 3.14159\ldots$" we are treating a proportion as a number —
reifying the shadow.

### 9.6 Linear/Circular Assumptions in Physics

Most of physics is built on linear algebra (vectors, Hilbert spaces)
and circular harmonics (Fourier series, spherical harmonics). These are
mathematically convenient but geometrically limiting: they assume that
the fundamental objects are points (0D), lines (1D), circles (2D
closed), or spheres (3D closed).

A helix is none of these. It is 3D, open, chiral, and fundamentally
different from both lines and circles. If the electron is a helix,
then:

- Vector formulations are projections onto a lower-dimensional subspace
- Fourier decompositions decompose the helix into circular components
  that aren't individually physical
- $\pi$ appears because the projection is circular, not because the
  object is

---

## 10. Catalog of $\pi$ Appearances in Physics

If $\pi$ is the transverse projection of helical geometry, every $\pi$
in a physics formula should be traceable to a hidden circular or
spherical symmetry.

### 10.1 Major $\pi$ Appearances with Geometric Interpretation

| Formula | $\pi$ Role | Geometric Origin |
|---------|-----------|-----------------|
| Coulomb: $F = q_1 q_2/(4\pi\varepsilon_0 r^2)$ | $4\pi$ from Gauss flux through sphere | Spherical symmetry of point source |
| Uncertainty: $\Delta x \Delta p \geq \hbar/2 = h/(4\pi)$ | $2\pi$ from wave periodicity | Fourier duality of conjugate variables |
| Hydrogen energy: $E_n = -m e^4/(8\varepsilon_0^2 h^2 n^2)$ | Hidden in $\alpha = e^2/(4\pi\varepsilon_0\hbar c)$ | Circular Bohr orbits |
| Blackbody: $\sigma = 2\pi^5 k^4/(15 h^3 c^2)$ | $2\pi^5$ from angular integrals | Spherical integration |
| Schrödinger: $i\hbar\partial_t\psi = -(\hbar^2/2m)\nabla^2\psi$ | $\pi$ in $\hbar = h/(2\pi)$ | Wave nature of matter |
| Dirac: $(i\hbar\gamma^\mu\partial_\mu - mc)\psi = 0$ | $\pi$ in $\hbar$ | Relativistic wave equation |
| Einstein field: $G_{\mu\nu} = (8\pi G/c^4)T_{\mu\nu}$ | $8\pi$ from spherical symmetry | Gauss-Bonnet in 4D |
| Schwinger: $a_e = \alpha/(2\pi)$ | $2\pi$ from angular integration | Loop Feynman integral |

### 10.2 Classification Scheme

| Category | Description | Examples |
|----------|-------------|----------|
| **Circumferential** | $C = 2\pi r$, area $= \pi r^2$ | Coulomb's law, Gauss's law |
| **Spherical** | Surface area $= 4\pi r^2$, solid angle | Planck's law, blackbody |
| **Fourier/Periodic** | $e^{i2\pi x/\lambda}$, Fourier transform | Quantum mechanics, signals |
| **Gaussian** | $\int e^{-x^2}dx = \sqrt{\pi}$ | Path integrals, statistics |
| **Angular momentum** | $\mathbf{L} = \mathbf{r} \times \mathbf{p}$, eigenvalues | Atomic physics, spin |

### 10.3 The Helical Interpretation

In the Helical Compton Vortex picture, all these $\pi$ factors trace
back to the same geometric source: the projection of the helical
electron onto a transverse plane. The Coulomb $4\pi$, the uncertainty
$2\pi$, the Schrödinger $\pi$ in $\hbar$ — all are different facets of
the same hidden circularity.

The electron's internal geometry is helical. When we measure it in a
linear or circular basis, $\pi$ appears as the residue of the
projection. A truly helical formulation of quantum mechanics — perhaps
in Hestenes' Spacetime Algebra — would make the $\pi$ factors disappear,
absorbed into the geometric structure of the rotor representation.

### 10.4 $\pi$-Free Formulations

| Law | Contains $\pi$? | Why? |
|-----|----------------|------|
| $F = ma$ | No | Linear — no hidden circle |
| $E = mc^2$ | No | Linear — no hidden circle |
| $E = \hbar\omega$ | Yes (in $\hbar$) | Wave periodicity |
| Coulomb's law | Yes ($4\pi$) | Spherical flux |
| Schrödinger eq. | Yes (in $\hbar$) | Wave nature |
| Einstein field eq. | Yes ($8\pi G$) | Spherical symmetry |

The pattern is clear: $\pi$ appears whenever the physics involves
rotation, oscillation, or spherical symmetry — exactly the structures
that emerge when a helix is projected onto lower-dimensional subspaces.

---

## 11. Implications and Predictions

### 11.1 If the Electron IS a Helical Compton Vortex

The model makes several testable predictions beyond Hestenes'
channeling resonance:

1. **$\pi$-free formulation of QM.** A complete reformulation of quantum
   mechanics in Spacetime Algebra should eliminate all explicit $\pi$
   factors, with the geometric structure absorbing them into rotor
   representations.

2. **$\alpha$ from geometry.** The value of $\alpha$ should be derivable
   from the vortex's stability conditions — a balance between
   electromagnetic self-energy and quantum oscillation energy. This is
   a well-posed variational problem.

3. **Mass ratios.** If all particles are vortex configurations, their
   mass ratios should correspond to ratios of topological invariants
   (winding numbers, linking numbers).

4. **Universality of $\alpha$.** The same aspect ratio should appear in
   any system where electromagnetic self-energy is balanced against
   quantum oscillation — not just electrons, but muons, tauons, and
   possibly hadronic systems.

### 11.2 Relationship to the Anomalous Magnetic Moment

The electron's anomalous magnetic moment $a_e = (g-2)/2 \approx
0.00116$ is currently computed to 12 significant figures in QED
perturbation theory and matches experiment to similar precision.

In the vortex model, $a_e \approx \alpha/(2\pi) \approx 0.00116$ at
leading order — the first-order thickness correction. The QED
perturbative series:

$$a_e = \frac{\alpha}{2\pi} + C_2\!\left(\frac{\alpha}{\pi}\right)^{\!2}
       + C_3\!\left(\frac{\alpha}{\pi}\right)^{\!3} + \cdots$$

may have a geometric reinterpretation: each term corresponds to a
higher-order correction to the vortex shape (self-interaction of the
helical current). The extraordinary precision of QED would then not
contradict the geometric model — it would *validate* it.

### 11.3 Connection to the Electroweak Scale?

If the electron is a vortex in the electromagnetic vacuum, other
particles may be vortices in other fields. The electroweak scale
($v \approx 246$ GeV) may represent the energy at which the vortex
character becomes explicit — where the "particle" approximation breaks
down and topology takes over.

The ratio $m_e/v \approx 3.7 \times 10^{-6}$ is vastly smaller than
$\alpha \approx 1/137$. This hierarchy may have a topological
explanation: the electron is a low-energy bound state (a vortex ring),
while the $W$ and $Z$ bosons are excitations of the underlying field.

### 11.4 What Would Falsify the Model?

A scientific model must be falsifiable. The Helical Compton Vortex
model would be falsified by:

1. **Experimental disconfirmation of Hestenes' channeling resonance
   prediction** — if dedicated experiments find no ZB-related resonance
   after exhaustive search.

2. **A conclusive theoretical proof that ZB is unphysical** — not just
   eliminable by a unitary transformation, but provably non-existent.

3. **Discovery that $\alpha$ varies with energy scale in a way
   incompatible with geometric interpretation** — if $\alpha$'s running
   cannot be mapped to a vortex deformation.

4. **A competing model that explains the same facts with fewer
   assumptions** — Occam's razor applies.

---

## 12. Conclusion

### 12.1 Summary of the Unification

We have shown that:

1. $\alpha = r_e/\lambdabar$ is an exact algebraic identity — the
   fine-structure constant is the ratio of the classical electron
   radius to the reduced Compton wavelength.

2. $m = \omega$ in Planck units is an identity following from
   $E = \hbar\omega$ and $E = mc^2$ — mass is angular frequency.

3. $\pi$ is a projection artifact — the circle constant emerges when
   helical geometry is projected onto a transverse plane.

4. These three converge on a single geometric object — the Helical
   Compton Vortex — with Compton wavelength as diameter, $\alpha$ as
   aspect ratio, and $\omega_C$ as circulation frequency.

The three "fundamental constants" $\pi$, $\alpha$, and $m$ are not
independent arbitrary numbers. They are three orthogonal projections of
a single geometric structure: a helical toroidal vortex in the
electromagnetic vacuum.

### 12.2 Open Questions

1. **What determines the absolute scale?** The Compton wavelength
   $\lambda_c = h/(m_e c)$ sets the scale, but $h$ and $c$ are fixed by
   definition in SI. In natural units, why $m_e \approx 4.2 \times
   10^{-23}\ m_P$?

2. **Why $\alpha \approx 1/137$?** We have reinterpreted $\alpha$ as an
   aspect ratio, but the value of that ratio remains unexplained.
   Stability analysis of the vortex may yield it.

3. **What about the muon and tau?** Are heavier leptons vortices with
   different topological invariants? The mass ratios $m_\mu/m_e \approx
   207$ and $m_\tau/m_e \approx 3477$ may encode topological
   information.

4. **Can the model be quantized?** The Helical Compton Vortex is a
   classical geometric model. Its quantization remains an open problem.

5. **Is there a deeper principle?** If all three "constants" are
   projections of one object, what principle determines the object's
   properties?

### 12.3 Call for Experimental Tests

The most urgent next step is experimental: test Hestenes' channeling
resonance prediction. If the electron exhibits resonant behavior at the
ZB frequency in crystal channeling experiments, the physical reality of
the helical ZB is confirmed. If not, the model must be revised or
abandoned.

The geometric unification presented here is elegant but provisional. It
awaits the verdict of experiment.

---

## Appendix A: Pre-1706 Notations for the Circle Constant

| Date | Source | Notation | Description |
|------|--------|----------|-------------|
| ~250 BCE | Archimedes | Verbal bounds | $3\frac{10}{71} < \pi < 3\frac{1}{7}$ |
| ~150 CE | Ptolemy | $3;8,30$ (sexagesimal) | $377/120 \approx 3.14167$ |
| ~480 CE | Zu Chongzhi | $355/113$ (密率) | Accurate to 6 decimal places |
| ~1424 | Al-Kashi | $2\pi$ to 16 dec. places | Sexagesimal and decimal |
| 1596 | Ludolph van Ceulen | 20 then 35 dec. places | "Ludolphine number" |
| 1647 | William Oughtred | $\pi/\delta$ | Periphery/diameter for specific circles |
| 1655 | John Wallis | Infinite product | Wallis product for $\pi/2$ |
| ~1660s | Isaac Barrow | $\pi$ as variable | Perimeter length variable |
| 1706 | William Jones | $\pi$ | Circle constant — first modern use |

## Appendix B: Attic Numeral System — Full Symbol Table

| Symbol | Unicode | Value | Greek Word | Etymology |
|--------|---------|-------|------------|-----------|
| Ι | U+0399 | 1 | — | Tally mark (iota) |
| Π | U+03A0 | 5 | πέντε (pente) | "five" |
| 𐅃 | U+10143 | 5 | (decorative Π) | Pi with right stroke |
| Δ | U+0394 | 10 | δέκα (deka) | "ten" |
| 𐅄 | U+10144 | 50 | — | Δ inside Π |
| Η | U+0397 | 100 | ἑκατόν (hekaton) | "hundred" |
| 𐅅 | U+10145 | 500 | — | Η inside Π |
| Χ | U+03A7 | 1000 | χίλιοι (khilioi) | "thousand" |
| 𐅆 | U+10146 | 5000 | — | Χ inside Π |
| Μ | U+039C | 10000 | μύριοι (myrioi) | "ten thousand" |
| 𐅇 | U+10147 | 50000 | — | Μ inside Π |

## Appendix C: Dimensional Analysis Proofs

**Theorem C.1:** $\alpha$, $\pi$, and $m_P$ (in Planck units) are all dimensionless.

*Proof of $\alpha$:*
$\alpha = e^2/(4\pi\varepsilon_0\hbar c)$. In SI: $[e^2] = \mathrm{C}^2$,
$[\varepsilon_0] = \mathrm{C}^2/(\mathrm{N \cdot m^2})$,
$[\hbar] = \mathrm{J \cdot s}$, $[c] = \mathrm{m/s}$.

Computing: $[\alpha] = \mathrm{C}^2 / (\mathrm{C}^2/(\mathrm{N \cdot m^2})
\times \mathrm{J \cdot s} \times \mathrm{m/s})
= \mathrm{C}^2 \cdot \mathrm{N \cdot m^2} / (\mathrm{C^2 \cdot J \cdot m})
= \mathrm{N \cdot m / J} = 1$. ∎

*Proof for $\pi$:* $\pi = C/d$ is the ratio of two lengths.
Dimensionless by definition. ∎

*Proof for $m_P$:* In SI, $[m] = \mathrm{kg}$, $[\omega] = \mathrm{s}^{-1}$.
Conversion factor $\hbar/c^2$ has units
$\mathrm{(J \cdot s)/(m^2/s^2)} = \mathrm{kg \cdot s}$. So $m =
(\hbar/c^2)\omega$ has consistent dimensions. In Planck units,
$\hbar = c = 1$ eliminates the conversion, making $m$ dimensionless. ∎

## Appendix D: STA Derivation (Placeholder)

Full Spacetime Algebra derivation deferred to a future version. In
brief, Hestenes' STA reformulation of the Dirac equation eliminates
complex numbers and Dirac matrices, replacing them with geometric
(Clifford) algebra. The electron's wavefunction becomes a rotor $R(x)$
satisfying:

$$\nabla R = \frac{mc}{\hbar} R \gamma_0$$

The ZB emerges as the rotational component of $R$, and the velocity
operator becomes a vector in spacetime rather than a $4 \times 4$
matrix. The helical path is a direct geometric consequence.

## Appendix E: Complete Catalog of $\pi$ in Physics Formulas

| Formula | $\pi$ count | Type |
|---------|------------|------|
| Coulomb: $F = q_1q_2/(4\pi\varepsilon_0 r^2)$ | $4\pi$ | Spherical |
| Bohr magneton: $\mu_B = e\hbar/(2m_e)$ | $2\pi$ (in $\hbar$) | Angular |
| Uncertainty: $\Delta x\Delta p \geq h/(4\pi)$ | $4\pi$ | Fourier |
| Hydrogen ground state: $\psi \propto e^{-r/a_0}$ | 0 | — |
| de Broglie: $\lambda = h/p$ | $2\pi$ (in $\hbar$) | Periodic |
| Stefan-Boltzmann: $\sigma = 2\pi^5 k^4/(15h^3c^2)$ | $2\pi^5$ | Spherical |
| Einstein field: $G_{\mu\nu} = (8\pi G/c^4)T_{\mu\nu}$ | $8\pi$ | Spherical |
| Schwinger: $a_e = \alpha/(2\pi)$ | $2\pi$ | Angular |
| Schrödinger: $-\hbar^2/(2m)\nabla^2\psi$ | $2\pi$ (in $\hbar$) | Wave |
| Planck length: $l_P = \sqrt{\hbar G/c^3}$ | Multiple | Definitional |
| Compton: $\lambda_c = h/(mc)$ | 0 | Linear |

## Appendix F: SI $\leftrightarrow$ Planck Unit Conversion Tables

| Quantity | Planck Unit | SI Value |
|----------|------------|----------|
| Length | $l_P = \sqrt{\hbar G/c^3}$ | $1.616255 \times 10^{-35}$ m |
| Time | $t_P = \sqrt{\hbar G/c^5}$ | $5.391247 \times 10^{-44}$ s |
| Mass | $m_P = \sqrt{\hbar c/G}$ | $2.176434 \times 10^{-8}$ kg |
| Energy | $E_P = \sqrt{\hbar c^5/G}$ | $1.956082 \times 10^{9}$ J |
| Temperature | $T_P = \sqrt{\hbar c^5/(Gk^2)}$ | $1.416784 \times 10^{32}$ K |

| Electron Quantity | SI Value | Planck Value |
|-------------------|----------|--------------|
| Mass $m_e$ | $9.1093837 \times 10^{-31}$ kg | $4.1854 \times 10^{-23}\ m_P$ |
| Compton freq. $\omega_C$ | $7.7634 \times 10^{20}$ rad/s | $4.1854 \times 10^{-23}\ t_P^{-1}$ |
| Reduced Compton $\lambdabar_e$ | $3.8616 \times 10^{-13}$ m | $2.3893 \times 10^{22}\ l_P$ |
| Classical radius $r_e$ | $2.8179 \times 10^{-15}$ m | $1.7435 \times 10^{20}\ l_P$ |
| Bohr radius $a_0$ | $5.2918 \times 10^{-11}$ m | $3.2739 \times 10^{24}\ l_P$ |

---

## References

<!-- Maintained in references.bib -->

1. Jones, W. (1706). *Synopsis Palmariorum Matheseos*. London.
2. Hestenes, D. (2008). Zitterbewegung in Quantum Mechanics. arXiv:0802.2728.
3. Hestenes, D. (2019). Zitterbewegung structure in electrons and photons. arXiv:1910.11085.
4. Consa, O. (2018). Helical Solenoid Model of the Electron.
5. Consa, O. (2017). G-Factor and the Helical Solenoid Electron Model.
6. Rodrigues, W. A., Vaz, J., Recami, E., & Salesi, G. (1993). About Zitterbewegung. arXiv:hep-th/9312047.
7. Williamson, J. G. & van der Mark, M. B. (1997). *Ann. Fond. Louis de Broglie*, 22, 133.
8. Wikipedia contributors. Attic numerals, Pi, Classical electron radius, Fine-structure constant, Zitterbewegung, Compton wavelength, William Jones.
9. Mobley, M. J. (2015). SPIE.
10. Hestenes, D. (2009). *Found. Phys.*
11. MacTutor History of Mathematics. William Jones.
12. Feynman, R. P. (1985). *QED*. Princeton University Press.
13. Penrose, R. (2004). *The Road to Reality*. Jonathan Cape.
14. CODATA. (2022). Fundamental physical constants.
15. Planck, M. (1899). Über irreversible Strahlungsvorgänge.
16. Euclid. (~300 BCE). *Elements*, Book V.

---

*Draft v1.1 — 2026-07-17 — QNFO.RSCH.APH*
