# Refractive Index, Fresnel Equations, and Kramers–Kronig Analysis

---

## 1. The Complex Refractive Index

When light propagates through a material, its behavior is governed by the material's **complex refractive index**, defined as:

$$\tilde{n} = n + i\kappa$$

where both $n$ and $\kappa$ are real, frequency-dependent quantities.

### 1.1 The Real Part: $n$ (Refractive Index)

The real part $n$ is the conventional refractive index. It describes **how much the phase velocity of light is slowed** relative to vacuum:

$$v_\text{phase} = \frac{c}{n}$$

- $n > 1$ means light travels more slowly through the medium than in vacuum.
- $n$ governs **refraction** (bending of light at interfaces, described by Snell's law) and the **wavelength** of light inside the medium.
- A larger $n$ corresponds to a more optically dense medium.

### 1.2 The Imaginary Part: $\kappa$ (Extinction Coefficient)

The imaginary part $\kappa$ is the **extinction coefficient**. It describes how strongly the medium **absorbs** (or amplifies) the electromagnetic wave as it propagates.

For a plane wave traveling in the $z$-direction, the electric field goes as:

$$E \propto e^{i(\tilde{n}\omega/c)z} = e^{i(n\omega/c)z} \cdot e^{-(\kappa\omega/c)z}$$

The second exponential is a **real decay envelope**: the wave's amplitude diminishes as $e^{-\kappa\omega z/c}$.

- $\kappa > 0$: the medium absorbs light (lossy).
- $\kappa = 0$: the medium is transparent at that frequency.
- $\kappa < 0$: optical gain (e.g., in a laser medium).

The **absorption coefficient** $\alpha$ (measurable via Beer–Lambert law) relates to $\kappa$ as:

$$\alpha = \frac{2\kappa\omega}{c} = \frac{4\pi\kappa}{\lambda_0}$$

### 1.3 Connection to the Dielectric Function

The complex refractive index is directly related to the complex dielectric function $\tilde{\varepsilon} = \varepsilon_1 + i\varepsilon_2$ via:

$$\tilde{\varepsilon} = \tilde{n}^2 \implies \varepsilon_1 = n^2 - \kappa^2, \quad \varepsilon_2 = 2n\kappa$$

Both representations carry equivalent physical information.

---

## 2. Reflectivity, Phase Shift, and the Fresnel Equations

### 2.1 Fresnel Equations at Normal Incidence

When light hits a flat interface between vacuum (or air, $\tilde{n}_1 = 1$) and a material ($\tilde{n}_2 = \tilde{n} = n + i\kappa$) at **normal incidence**, the Fresnel reflection coefficient is:

$$\tilde{r} = \frac{1 - \tilde{n}}{1 + \tilde{n}}$$

This is a **complex number**. Writing it in polar form:

$$\tilde{r} = \sqrt{R}, e^{i\theta}$$

we extract two independently measurable quantities:

|Quantity|Symbol|Physical meaning|
|---|---|---|
|Reflectivity|$R =|\tilde{r}|
|Phase shift|$\theta$|Phase change of the reflected electric field|

### 2.2 Inverting the Fresnel Equations

Given $R$ and $\theta$, the complex refractive index can be recovered analytically. From the Fresnel formula:

$$\tilde{r} = \sqrt{R},e^{i\theta} = \frac{1 - (n+i\kappa)}{1 + (n+i\kappa)}$$

Solving for $n$ and $\kappa$:

$$n = \frac{1 - R}{1 + R - 2\sqrt{R}\cos\theta}$$

$$\kappa = \frac{2\sqrt{R}\sin\theta}{1 + R - 2\sqrt{R}\cos\theta}$$

### 2.3 The Measurement Problem

In a typical **reflectance spectroscopy** experiment, the measured quantity is the **intensity reflectivity** $R(\omega)$ — a real, non-negative number for each frequency. The **phase shift** $\theta(\omega)$ is **not directly accessible** from a simple intensity measurement.

This creates a fundamental challenge: we have one measured function ($R$) but need two functions ($n$ and $\kappa$, or equivalently $\theta$) to fully characterize the material. This is where **Kramers–Kronig analysis** becomes essential.

---

## 3. Kramers–Kronig Analysis

### 3.1 Physical Motivation: Causality

The Kramers–Kronig relations follow from a single deep physical principle: **causality**. A material cannot respond to a perturbation before the perturbation arrives. Mathematically, the response function (here, the complex reflectivity amplitude $\tilde{r}(\omega)$ or the dielectric function $\tilde{\varepsilon}(\omega)$) must be an **analytic function** in the upper half of the complex frequency plane.

This analyticity, combined with physical boundary conditions (the response vanishes at infinite frequency), is sufficient to derive integral relationships between the real and imaginary parts of any causal response function.

### 3.2 The Kramers–Kronig Relations

For the complex dielectric function $\tilde{\varepsilon}(\omega) = \varepsilon_1(\omega) + i\varepsilon_2(\omega)$, the Kramers–Kronig relations are:

$$\varepsilon_1(\omega) = 1 + \frac{2}{\pi},\mathcal{P}!\int_0^\infty \frac{\omega',\varepsilon_2(\omega')}{\omega'^2 - \omega^2},d\omega'$$

$$\varepsilon_2(\omega) = -\frac{2\omega}{\pi},\mathcal{P}!\int_0^\infty \frac{\varepsilon_1(\omega') - 1}{\omega'^2 - \omega^2},d\omega'$$

where $\mathcal{P}$ denotes the **Cauchy principal value** of the integral (necessary to handle the singularity at $\omega' = \omega$).

**Key implication:** If you know $\varepsilon_2(\omega)$ (related to absorption, hence to $\kappa$) over all frequencies, you can compute $\varepsilon_1(\omega)$ (related to $n$), and vice versa. The real and imaginary parts of a causal response function are **not independent**.

### 3.3 Application to Reflectance: Obtaining the Phase

In practice, one measures $R(\omega)$ and wants $\theta(\omega)$. Taking the logarithm of the complex reflectivity:

$$\ln \tilde{r}(\omega) = \ln\sqrt{R(\omega)} + i\theta(\omega)$$

The function $\ln\tilde{r}(\omega)$ is itself a causal response function (under appropriate conditions), so its real part $\frac{1}{2}\ln R$ and imaginary part $\theta$ are related by Kramers–Kronig:

$$\theta(\omega) = -\frac{2\omega}{\pi},\mathcal{P}!\int_0^\infty \frac{\ln\sqrt{R(\omega')}}{\omega'^2 - \omega^2},d\omega'$$

This is the central result of **Kramers–Kronig reflectance analysis**: given measured $R(\omega)$ over a wide spectral range, one can compute the phase $\theta(\omega)$ — and then immediately obtain both $n(\omega)$ and $\kappa(\omega)$ from the inverted Fresnel equations in Section 2.2.

### 3.4 The Role of Cauchy's Integral Theorem

The mathematical foundation of the Kramers–Kronig relations is **Cauchy's Integral Theorem** from complex analysis.

#### Statement of Cauchy's Integral Theorem

For a function $f(z)$ that is **analytic** (holomorphic) everywhere inside and on a closed contour $C$:

$$\oint_C f(z),dz = 0$$

#### Derivation of Kramers–Kronig from Cauchy

Consider the function $\chi(\omega) = \chi_1(\omega) + i\chi_2(\omega)$, a causal response function (e.g., susceptibility or $\ln\tilde{r}$). Because causality requires that $\chi(\omega)$ is analytic in the **upper half complex $\omega$-plane**, we can apply Cauchy's theorem to the contour integral:

$$\oint_C \frac{\chi(\omega')}{\omega' - \omega},d\omega' = 0$$

choosing a contour that:

1. Runs along the **real axis** (from $-\infty$ to $+\infty$, with a small semicircle indenting around the pole at $\omega' = \omega$).
2. Closes with a **large semicircle** in the upper half-plane (where $\chi \to 0$ at large $|\omega'|$, so this arc contributes nothing).

Evaluating the small indentation around the pole using the **residue theorem** (it contributes $i\pi\chi(\omega)$), one obtains:

$$\mathcal{P}!\int_{-\infty}^{+\infty} \frac{\chi(\omega')}{\omega' - \omega},d\omega' = i\pi\chi(\omega)$$

Separating real and imaginary parts of this equation yields the Kramers–Kronig relations. The **Cauchy principal value** $\mathcal{P}$ arises naturally to handle the integrable singularity at $\omega' = \omega$.

#### Summary of the Mathematical Logic

```
Causality
    ↓
χ(ω) is analytic in upper half complex plane
    ↓
Cauchy's Integral Theorem applies on closed contour
    ↓
Residue Theorem handles the pole at ω' = ω
    ↓
Kramers–Kronig relations (real ↔ imaginary parts linked)
    ↓
Phase θ(ω) obtained from measured R(ω)
    ↓
n(ω) and κ(ω) from inverted Fresnel equations
```

---

## 4. Practical Workflow Summary

|Step|What is done|Key equation/tool|
|---|---|---|
|1. Measure|Record reflectivity spectrum $R(\omega)$|Experiment|
|2. KK Integration|Compute phase $\theta(\omega)$ from $R(\omega)$|Kramers–Kronig + Cauchy's theorem|
|3. Invert Fresnel|Solve for $n(\omega)$ and $\kappa(\omega)$|Fresnel equations (inverted)|
|4. Derive $\tilde{\varepsilon}$|Compute dielectric function|$\varepsilon_1 = n^2 - \kappa^2$, $\varepsilon_2 = 2n\kappa$|

### Caveats and Practical Considerations

- **Integration range:** The Kramers–Kronig integral formally requires data from $\omega = 0$ to $\infty$. In practice, measured spectra are finite, so extrapolations must be made at both low and high frequency ends, introducing some uncertainty.
- **Anchoring:** The value of $n$ at a known frequency (e.g., from an ellipsometry measurement or from the optical constant at a transparent region) can be used to check consistency.
- **Ellipsometry as an alternative:** Spectroscopic ellipsometry directly measures both amplitude and phase of the reflected field (via the ellipsometric angles $\Psi$ and $\Delta$), bypassing the need for Kramers–Kronig analysis entirely — at the cost of more complex instrumentation.

---

## References and Further Reading

- Kramers, H.A. (1927); Kronig, R. de L. (1926) — original derivations.
- Wooten, F. _Optical Properties of Solids_ (Academic Press, 1972) — classic textbook treatment.
- Dressel, M. & Grüner, G. _Electrodynamics of Solids_ (Cambridge, 2002) — detailed derivations and applications.
- Toll, J.S. _Causality and the Dispersion Relation_ (Phys. Rev., 1956) — formal mathematical foundation.