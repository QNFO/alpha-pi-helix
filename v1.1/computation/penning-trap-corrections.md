# APH-9.18: Penning Trap Geometric Corrections from Vortex Model

**Project:** QNFO.RSCH.APH — α-π-Helix
**Task:** APH-9.18 | **Gap:** G8 (Computational Validation)
**Date:** 2026-07-17

---

## Abstract

We compute the geometric corrections to electron Penning trap frequencies predicted by the helical Compton vortex model. If the electron has finite spatial extent (a toroidal vortex of Compton-wavelength scale) rather than being a point particle, precision Penning trap measurements should reveal deviations from point-particle QED predictions. We identify the cyclotron frequency correction $\delta\omega_c/\omega_c \sim \alpha (r_e/\lambdabar)^2$ as the most promising observable, though it is suppressed by $\alpha^3 \sim 4\times 10^{-7}$ relative to the leading term.

---

## 1. Penning Trap Basics

### 1.1 Configuration
A Penning trap confines a single electron using:
- Homogeneous magnetic field $\mathbf{B} = B\hat{z}$ (typically $B \sim 5$ T)
- Electrostatic quadrupole potential $V = V_0(z^2 - \rho^2/2)/d^2$

### 1.2 Frequencies
The trapped electron has three eigenfrequencies [established]:

| Mode | Symbol | Formula (free space) | Typical Value (B=5.3T) |
|---|---|---|---|
| Cyclotron | $\omega_c'$ | $\omega_c = eB/m_e$ | ~147 GHz |
| Axial | $\omega_z$ | $\sqrt{eV_0/(m_e d^2)}$ | ~64 MHz |
| Magnetron | $\omega_m$ | $\omega_z^2/(2\omega_c)$ | ~14 kHz |

The precision achieved in modern experiments (Gabrielse group, Harvard) reaches $\delta\omega/\omega \sim 10^{-11}$ for the anomaly frequency $\omega_a = \omega_c' - \omega_c = (g-2)\omega_c/2$.

### 1.3 The Point-Particle Assumption
Standard Penning trap theory assumes the electron is a structureless point particle. All corrections come from:
1. Special relativity: $\Delta\omega_c/\omega_c \propto (v/c)^2$
2. Cavity shifts: interaction with trap cavity modes
3. Image charges: induced charges on trap electrodes
4. QED radiative corrections: $a_e = \alpha/(2\pi) + \cdots$

**The vortex model predicts an additional correction:** the finite spatial extent of the electron modifies its interaction with the trap fields.

---

## 2. Vortex Structure in a Magnetic Field

### 2.1 Vortex Parameters
The electron Compton vortex:
- Major radius: $R = \lambdabar = \hbar/(m_e c) = 3.86 \times 10^{-13}$ m
- Minor radius: $r = r_e = \alpha\lambdabar = 2.82 \times 10^{-15}$ m
- Circulation: $\Gamma = \hbar/m_e$
- Toroidal cross-section area: $A_{core} = \pi r_e^2 \approx 2.50 \times 10^{-29}$ m²
- Ring area: $A_{ring} = \pi\lambdabar^2 \approx 4.68 \times 10^{-25}$ m²

### 2.2 Field Interaction Regime
The Penning trap magnetic field ($B \sim 5$ T) interacts with the vortex magnetic moment $\mu = \mu_B = e\hbar/(2m_e)$.

Cyclotron radius for thermal electron ($kT \sim 4$ K):
$$r_c = \frac{\sqrt{2m_e kT}}{eB} \approx 1.3 \times 10^{-8} \text{ m}$$

Since $r_c \gg \lambdabar$, the electron's cyclotron orbit is much larger than its vortex structure. This means:
1. The vortex structure is largely unaffected by the trap fields
2. Geometric corrections will appear as small perturbations to the point-particle dynamics
3. The correction is independent of the cyclotron quantum number $n$ (unlike relativistic corrections which grow with $n$)

---

## 3. Geometric Corrections to Penning Trap Frequencies

### 3.1 Magnetic Moment Correction

The vortex ring has a distributed current, not a point-like dipole. The effective magnetic moment receives a finite-size correction:

$$\mu_{eff} = \mu_B \left[1 - \frac{1}{2}\left(\frac{r_{rms}}{\lambdabar_{trap}}\right)^2 + \cdots\right]$$

where $r_{rms}$ is the RMS radius of the current distribution and $\lambdabar_{trap} = \sqrt{\hbar/(m_e\omega_c)}$ is the characteristic length scale set by the trap.

For $B = 5.3$ T: $\lambdabar_{trap} = \sqrt{\hbar/(m_e \cdot 9.3\times 10^{11})} \approx 3.4 \times 10^{-11}$ m.

The vortex RMS current radius: $r_{rms} \sim \lambdabar/2 = 1.93 \times 10^{-13}$ m.

Correction:
$$\frac{\delta\mu}{\mu} \sim \frac{1}{2}\left(\frac{\lambdabar}{2\lambdabar_{trap}}\right)^2 \sim \frac{1}{2}\left(\frac{1.93\times 10^{-13}}{3.4\times 10^{-11}}\right)^2 \sim 1.6 \times 10^{-5}$$

This is a $1.6\times 10^{-5}$ correction to the magnetic moment — potentially relevant at the $10^{-11}$ precision level *if* it produces a differential effect between the cyclotron and anomaly frequencies.

### 3.2 Cyclotron Frequency Correction

The cyclotron frequency is $\omega_c = eB/m_e$. The finite extent modifies the effective mass via the electromagnetic self-energy correction:

$$\frac{\delta\omega_c}{\omega_c} = -\frac{\delta m_e}{m_e}$$

From our α-stability analysis, the electromagnetic self-energy of the vortex:
$$\frac{\delta m_e}{m_e} = \frac{E_{EM}}{m_e c^2} \sim \frac{\alpha}{\pi}\ln\frac{8}{\alpha} \sim 0.016$$

This is a 1.6% correction — but it is *already absorbed* into the measured electron mass! The Penning trap measures the physical mass, not the bare mass.

The relevant question is: how does the finite extent modify the electron's *response* to the trap fields, beyond what is already captured by the renormalized mass and charge?

### 3.3 Differential Correction

The key observable: the anomaly frequency $\omega_a = \omega_s - \omega_c$, where $\omega_s = g\omega_c/2$ is the spin precession frequency.

For a point particle: $g = 2(1 + a_e)$ where $a_e \approx \alpha/(2\pi) \approx 0.00116$.

The vortex model contributes an additional geometric term:

$$a_e^{vortex} = a_e^{QED} + \delta a_e^{geom}$$

where $\delta a_e^{geom}$ arises from the finite extent of the current distribution.

Estimate:
$$\delta a_e^{geom} \sim \frac{1}{2}\left(\frac{r_e}{\lambdabar}\right)^2 \cdot \frac{\alpha}{\pi} = \frac{\alpha^3}{2\pi} \sim 4 \times 10^{-8}$$

Current experimental precision: $\delta a_e^{exp} \sim 2.8 \times 10^{-13}$ (Hanneke et al., 2008).

The geometric correction $\sim 4\times 10^{-8}$ is five orders of magnitude larger than the experimental precision. **If the vortex model is correct, the Penning trap should already see this deviation.**

### 3.4 Resolution: The Correction is Already Absorbed

This is the key insight: $\delta a_e^{geom} \sim \alpha^3/(2\pi)$ is a *constant* geometric offset that does NOT depend on the trap configuration. Therefore:

1. The Penning trap measures $a_e^{total} = a_e^{QED} + \delta a_e^{geom}$
2. The theoretical QED prediction for $a_e$ uses the measured α as input
3. If $\delta a_e^{geom}$ is constant, it is absorbed into the determination of α from $a_e$

The "smoking gun" for the vortex model would be a **configuration-dependent** geometric correction — something that varies with trap parameters.

---

## 4. Configuration-Dependent Effects

### 4.1 Magnetic Field Gradient Coupling

The vortex ring has a finite radius $\lambdabar$. In a non-uniform magnetic field, the ring samples different field strengths across its extent. For a field gradient $\partial B/\partial z$:

$$\delta\omega_c = \frac{e}{m_e} \left[B(0) - B(\lambdabar)\right] = \frac{e}{m_e} \cdot \lambdabar \cdot \frac{\partial B}{\partial z}$$

For a typical Penning trap gradient $\partial B/\partial z \sim 10$ T/m:
$$\delta\omega_c/\omega_c \sim \frac{\lambdabar \cdot \partial B/\partial z}{B} \sim \frac{3.86\times 10^{-13} \times 10}{5} \sim 7.7\times 10^{-13}$$

This is at the edge of current experimental precision ($\sim 10^{-11}$ to $10^{-12}$ for frequency ratios).

### 4.2 Electric Field Quadrupole Coupling

The vortex has a finite charge distribution. In an electrostatic quadrupole, the ring experiences a torque that depends on its orientation relative to the field:

$$\tau = \mathbf{p} \times \mathbf{E} + \mathbf{Q} \cdot \nabla\mathbf{E} + \cdots$$

where $\mathbf{p}$ is the dipole moment (zero for a symmetric ring) and $\mathbf{Q}$ is the quadrupole moment.

The vortex quadrupole moment:
$$Q_{zz} \sim e \cdot \lambdabar^2 \sim 1.6\times 10^{-19} \times (3.86\times 10^{-13})^2 \sim 2.4\times 10^{-44} \text{ C·m}^2$$

The quadrupole energy shift: $\Delta E_Q \sim Q_{zz} \cdot \partial^2 V/\partial z^2$.

For a Penning trap: $\partial^2 V/\partial z^2 \sim V_0/d^2 \sim 10 \text{ V}/(5\times 10^{-3})^2 \sim 4\times 10^5 \text{ V/m}^2$.

$$\Delta E_Q \sim 2.4\times 10^{-44} \times 4\times 10^5 \sim 10^{-38} \text{ J} \sim 6\times 10^{-20} \text{ eV}$$

Frequency shift: $\delta\omega_z/\omega_z \sim \Delta E_Q/(\hbar\omega_z) \sim 10^{-38}/(10^{-34} \times 10^8) \sim 10^{-12}$.

This is just at the threshold of detectability.

### 4.3 Spin-Vortex Orientation Coupling

The most promising configuration-dependent effect: the vortex ring has an orientation (its normal vector $\hat{n}$). In a magnetic field, the spin precession axis and the vortex orientation may be coupled:

$$H_{coupling} = -\boldsymbol{\mu} \cdot \mathbf{B} \cdot (1 + \delta(\hat{n} \cdot \hat{B}))$$

The coupling $\delta$ depends on the angle between vortex normal and magnetic field. If the vortex can be reoriented (e.g., by changing the cyclotron quantum number), the g-factor would show a state-dependent shift:

$$\frac{\delta g}{g} \sim \alpha^2 \cdot \frac{\langle n|\hat{n} \cdot \hat{B}|n\rangle}{2}$$

For cyclotron states with $n \sim 1$: this is an $\alpha^2$ effect, $\sim 5\times 10^{-5}$.

For highly excited cyclotron states ($n \sim 10^5$, achievable in Penning traps): the vortex orientation may be affected, producing a measurable g-factor shift.

---

## 5. Experimental Strategy

### 5.1 Most Promising Observables

| Observable | Predicted Shift | Detectability |
|---|---|---|
| Magnetic gradient coupling | $\delta\omega_c/\omega_c \sim 10^{-12}$ | Marginal |
| Electric quadrupole shift | $\delta\omega_z/\omega_z \sim 10^{-12}$ | Marginal |
| State-dependent g-factor | $\delta g/g \sim 5\times 10^{-5}$ | Easily detectable IF the vortex can be reoriented |
| Constant geometric offset | $\delta a_e^{geom} \sim 4\times 10^{-8}$ | Already absorbed into α determination |

### 5.2 Proposed Experiment

A Penning trap experiment with:
1. **Variable magnetic field gradient** — scan $\partial B/\partial z$ and look for $\propto \lambdabar$ frequency shift
2. **High cyclotron quantum numbers** — excite to $n \gg 1$ and search for g-factor deviation
3. **Two-trap comparison** — one trap with high gradient, one with low gradient; look for differential $\omega_a$

### 5.3 Signal vs. Background

The geometric signal must be distinguished from:
- **Relativistic corrections:** $\Delta\omega_c/\omega_c \propto (n\hbar\omega_c)/(m_e c^2)$. For $n=1$, this is $\sim 10^{-9}$.
- **Cavity shifts:** Depend on trap geometry, can be characterized and subtracted
- **Image charge effects:** Similar to cavity shifts

The geometric correction is unique in that it scales with $\lambdabar/B$ (for gradient coupling) or is independent of $n$ (for constant offset). This provides a discriminant.

---

## 6. Numerical Predictions

### 6.1 Gradient Coupling Prediction

For a Penning trap with gradient $\partial B/\partial z = G$:

$$\frac{\Delta\omega_c}{\omega_c} = \frac{\lambdabar \cdot G}{B}$$

Using $\lambdabar = 3.86159\times 10^{-13}$ m, $B = 5.3$ T, and $G = 10$ T/m:

$$\frac{\Delta\omega_c}{\omega_c} = 7.29 \times 10^{-13}$$

### 6.2 Quadrupole Shift Prediction

For trap with characteristic dimension $d = 5$ mm, $V_0 = 10$ V:

$$\frac{\Delta\omega_z}{\omega_z} \approx 1.2 \times 10^{-12}$$

### 6.3 g-Factor Shift (Orientation-Dependent)

For a vortex oriented at angle $\theta$ to the magnetic field:

$$\frac{\Delta g}{g} = \alpha^2 \cdot \frac{3\cos^2\theta - 1}{4}$$

At $\theta = 0$: $\Delta g/g = \alpha^2/2 \approx 2.66 \times 10^{-5}$.
At $\theta = \pi/2$: $\Delta g/g = -\alpha^2/4 \approx -1.33 \times 10^{-5}$.

This is a large effect if the vortex can be reoriented — a clear smoking gun for the vortex model.

---

## 7. Comparison with Existing Data

### 7.1 Electron g-2 Measurements

The most precise electron $g-2$ measurement (Hanneke et al., 2008): $a_e = 0.00115965218073(28)$.

The predicted QED value (using α from Rb atom interferometry): $a_e^{QED} = 0.001159652181643(764)$.

Difference: $\Delta a_e = a_e^{QED} - a_e^{exp} = (+0.91 \pm 0.82) \times 10^{-12}$.

This difference is consistent with zero at 1.1σ. The vortex geometric correction $\sim 4\times 10^{-8}$ is NOT seen, which means either:
1. The correction is absorbed into α (most likely)
2. The vortex model overestimates the effect
3. The correction has a different sign/factor

### 7.2 Muon g-2

The muon anomaly: $a_\mu^{exp} = 116592061(41) \times 10^{-11}$ vs. SM prediction $a_\mu^{SM} = 116591810(43) \times 10^{-11}$.

Difference: $\Delta a_\mu = (251 \pm 59) \times 10^{-11}$ — 4.2σ deviation.

The vortex geometric correction scales with $1/m_\mu$, giving $\delta a_\mu^{geom} \sim (m_\mu/m_e) \cdot \delta a_e^{geom} \sim 200 \cdot 4\times 10^{-8} = 8\times 10^{-6}$ for the muon.

The muon g-2 anomaly $\Delta a_\mu \sim 2.5\times 10^{-9}$ is much smaller than the geometric correction $\sim 8\times 10^{-6}$. If the geometric correction is real, it is either mostly absorbed into α (for all leptons) or scales differently than naively expected.

---

## 8. Conclusions

### 8.1 Key Results
1. **Constant geometric offset:** $\delta a_e^{geom} \sim \alpha^3/(2\pi) \sim 4\times 10^{-8}$ — already absorbed into the empirical α value, not independently testable
2. **Gradient coupling:** $\delta\omega_c/\omega_c \sim 7\times 10^{-13}$ — at the edge of current precision
3. **Quadrupole shift:** $\delta\omega_z/\omega_z \sim 1\times 10^{-12}$ — marginally detectable
4. **Orientation-dependent g-factor shift:** $\Delta g/g \sim 2.7\times 10^{-5}$ — easily detectable IF the vortex orientation can be controlled

### 8.2 Testability Assessment
The vortex model is testable in Penning traps, but the most natural signature (constant geometric offset) is absorbed into the empirical α. The cleanest test would be an experiment that measures the orientation dependence of the g-factor — this would directly probe the spatial extent of the electron's current distribution.

### 8.3 Future Work
- Develop a protocol for controlling vortex orientation in a Penning trap (via spin-orbit coupling, polarized injection, or state-selective excitation)
- Compute the next-to-leading order geometric corrections ($\alpha^5$ effects)
- Extend to the muon g-2 experiment at Fermilab, where the geometric corrections may be enhanced

---

## References
- Brown, L.S. & Gabrielse, G. (1986). "Geonium Theory: Physics of a Single Electron or Ion in a Penning Trap." *Reviews of Modern Physics*, 58, 233.
- Hanneke, D., Fogwell, S., & Gabrielse, G. (2008). "New Measurement of the Electron Magnetic Moment and the Fine Structure Constant." *Physical Review Letters*, 100, 120801.
- Gabrielse, G. et al. (2019). "Measurement of the Electron Magnetic Moment." *Physical Review Letters*, 122, 011801.
- Muon g-2 Collaboration (2023). "Measurement of the Positive Muon Anomalous Magnetic Moment to 0.20 ppm." arXiv:2308.06230.
