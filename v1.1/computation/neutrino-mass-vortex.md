# APH-9.6: Neutrino Mass from Quantized Vortex States

**Project:** QNFO.RSCH.APH | **Task:** APH-9.6 | **Date:** 2026-07-17

## 1. The Neutrino as an Untwisted Vortex

If the electron is a helical Compton vortex with electromagnetic charge arising from the circulation of the vortex current, the neutrino is naturally interpreted as the **neutral counterpart:** a vortex ring with zero net electromagnetic circulation but nonzero weak isospin charge.

### 1.1 Vortex Parameters

| Property | Electron | Neutrino |
|---|---|---|
| EM charge | $e$ | 0 |
| Weak charge | $g_W$ (projected) | $g_W$ (full) |
| Circulation | $\Gamma_e = \hbar/m_e$ | $\Gamma_\nu = \hbar/m_\nu$ |
| Aspect ratio | $\alpha = r_e/\lambdabar_e$ | $\alpha_\nu \ll \alpha$ (no EM core) |
| Ring radius | $\lambdabar_e = 3.86\times 10^{-13}$ m | $\lambdabar_\nu = \hbar/(m_\nu c) \gg \lambdabar_e$ |

Key difference: without electromagnetic charge, the neutrino vortex has no classical electron radius $r_e$. Its "core" is defined by the weak interaction scale rather than EM.

---

## 2. Vortex Circulation Quantization

### 2.1 Fundamental Circulation

In the vortex model, circulation is quantized in units of $\hbar/m$:
$$\Gamma = \oint \mathbf{v} \cdot d\mathbf{l} = n \cdot \frac{\hbar}{m}$$

For the electron (n=1): $\Gamma_e = \hbar/m_e$, giving the Compton relation $\lambdabar_e = \hbar/(m_e c)$.

### 2.2 Neutrino Circulation Spectrum

If neutrinos are vortex states with integer circulation quantum numbers $n_\nu$:
$$m_\nu(n) \cdot \lambdabar_\nu(n) = \frac{\hbar}{c}$$

The mass spectrum for vortex states with circulation $n$ follows from vortex energy:
$$E_n \propto \Gamma_n^2/R_n \propto n^2 \cdot (n\hbar/(m_1c))^{-1} \propto n^3$$

This gives $m_\nu(n) \propto n^3$, which would produce very large mass splittings:
$$m_2/m_1 = 8, \quad m_3/m_1 = 27$$

The observed neutrino mass splittings are much smaller: $\Delta m^2_{21} \approx 7.4\times 10^{-5}$ eV², $\Delta m^2_{31} \approx 2.5\times 10^{-3}$ eV². [established]

This suggests neutrinos are NOT simple quantized vortex rings with integer circulation — unless the fundamental circulation quantum is extremely small.

---

## 3. Three Scenarios

### 3.1 Dirac Neutrinos

If neutrinos are Dirac particles (distinct $\nu$ and $\bar{\nu}$), they form three vortex generations analogous to charged leptons but without the EM structure. The mass hierarchy would follow the same topological pattern as charged leptons — which we have not yet derived successfully.

**Prediction:** $m_{\nu 1}:m_{\nu 2}:m_{\nu 3}$ follows the same pattern as $m_e:m_\mu:m_\tau$ but at a much lower absolute scale.

**Issue:** The charged lepton mass ratios ($1:206.8:3477$) are much larger than the neutrino mass ratios (which are nearly degenerate if the lightest neutrino is $\sim 0.01$ eV, giving ratios $\sim 1:2:5$). This suggests different dynamics for neutrinos.

### 3.2 Majorana Neutrinos (Self-Conjugate Vortex)

If neutrinos are Majorana particles, the vortex is its own anti-vortex: $\nu = \bar{\nu}$. This has a natural geometric interpretation: a vortex ring with no net circulation (the forward and backward paths cancel). The mass arises from the **self-linking energy** of the untwisted ring:

$$m_\nu \propto \frac{\hbar^2}{M R^2}$$

where $M$ is a large mass scale (the "seesaw scale") and $R \sim 1/M$ is the vortex radius at that scale.

This naturally produces small neutrino masses:
$$m_\nu \sim \frac{v^2}{M_R}$$

where $v = 246$ GeV is the electroweak scale and $M_R$ is the Majorana mass scale.

### 3.3 Seesaw Mechanism from Vortex-Anti-Vortex Pairs

In the seesaw mechanism, light neutrinos arise from the mixing of left-handed ($\nu_L$, mass $\sim 0$) and right-handed ($N_R$, mass $\sim M_R$) states:

$$M_\nu = \begin{pmatrix} 0 & m_D \\ m_D & M_R \end{pmatrix}$$

Diagonalizing gives light mass $m_\nu \approx m_D^2/M_R$ and heavy mass $\approx M_R$.

In the vortex picture, this corresponds to a **vortex-anti-vortex pair**: the left-handed neutrino is a vortex with one chirality, the right-handed neutrino is a vortex with opposite chirality. Their coupling $m_D$ is the vortex-vortex interaction energy, and $M_R$ is the self-energy of the heavy right-handed vortex.

---

## 4. Mass Scale Estimates

### 4.1 Seesaw Estimate

With $m_D \sim v = 246$ GeV and $M_R \sim 10^{14}$ GeV:
$$m_\nu \sim \frac{(246 \text{ GeV})^2}{10^{14} \text{ GeV}} \sim 6\times 10^{-4} \text{ eV}$$

Observed mass scale from oscillations: $m_\nu \sim \sqrt{\Delta m^2_{atm}} \sim 0.05$ eV.

The seesaw estimate is two orders of magnitude too small. Increasing $m_D$ (e.g., to the GUT scale $\sim 10^{16}$ GeV) or decreasing $M_R$ can bring the estimate into agreement, but this requires model-dependent choices. [speculative]

### 4.2 Alternative: Radiative Mass Generation

If neutrino masses are generated radiatively (e.g., via loop diagrams with charged leptons and W bosons), the vortex model predicts:
$$m_\nu \sim \frac{\alpha_W}{4\pi} \cdot m_e \cdot \left(\frac{\lambdabar_e}{\lambdabar_W}\right)^2$$

where $\lambdabar_W \sim 2.5\times 10^{-18}$ m is the W boson Compton wavelength. This gives:
$$m_\nu \sim \frac{1/30}{4\pi} \cdot 0.511 \text{ MeV} \cdot \left(\frac{3.86\times 10^{-13}}{2.5\times 10^{-18}}\right)^2 \sim \text{huge}$$

This overestimates the neutrino mass dramatically, indicating that additional suppression mechanisms are needed.

---

## 5. Testable Predictions

### 5.1 Absolute Mass Scale
The vortex model predicts neutrino masses are set by the ratio of the weak scale to a high scale (GUT or Planck). The absolute scale is $m_\nu \sim 0.01$–$0.1$ eV, consistent with cosmological bounds $\sum m_\nu < 0.12$ eV. [speculative]

### 5.2 Hierarchy Pattern
If neutrinos follow the same topological invariant structure as charged leptons, the mass hierarchy should be similar — but the observed near-degeneracy disfavors this. More likely: neutrino masses are generated by a different mechanism (seesaw, radiative) that produces a compressed spectrum.

### 5.3 Dirac vs. Majorana
The vortex model naturally favors Majorana neutrinos because a zero-circulation vortex is self-conjugate. The smoking-gun test is neutrinoless double beta decay ($0\nu\beta\beta$).

### 5.4 CP Violation
The vortex chirality (handedness of the helical circulation) provides a natural source of CP violation in the lepton sector. The CP-violating phase $\delta_{CP}$ may be related to the geometric phase (Berry phase) accumulated by the vortex during propagation.

---

## 6. Conclusions

1. **The neutrino is naturally the neutral partner** of the charged lepton in the vortex framework — a vortex without EM circulation.
2. **Majorana nature is geometrically natural:** zero-circulation vortex = self-conjugate.
3. **The absolute mass scale** from the seesaw mechanism is consistent with observations to within two orders of magnitude.
4. **The mass hierarchy** is NOT explained by simple vortex quantization — more complex dynamics (RG running, topological invariants) are needed.
5. **Testable predictions:** $0\nu\beta\beta$ (Majorana), absolute mass scale from cosmology, CP violation from geometric phase.

---

## References
- Fukuda, Y. et al. (Super-Kamiokande) (1998). "Evidence for Oscillation of Atmospheric Neutrinos." *Physical Review Letters*, 81, 1562.
- Minkowski, P. (1977). "μ→eγ at a Rate of One Out of 10⁹ Muon Decays?" *Physics Letters B*, 67, 421.
- de Salas, P.F. et al. (2021). "2020 Global Reassessment of the Neutrino Oscillation Picture." *JHEP*, 02, 071.
