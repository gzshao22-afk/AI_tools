# ELISA Curve Fitting Summary (4PL / LL.4)

## 1. Why ELISA Uses Nonlinear Curve Fitting
- ELISA signal vs. concentration is **sigmoidal (S-shaped)**  
- Contains:
  - Lower plateau (background)
  - Upper plateau (saturation)
  - Steep transition region  
- Linear models fail → **logistic models required**

---

## 2. 4-Parameter Logistic (4PL) Model

### Standard Form

$y = D + \frac{A - D}{1 + (x/C)^B}$


### Parameters
- **A**: lower asymptote  
- **D**: upper asymptote  
- **C**: EC50 (midpoint)  
- **B**: slope (Hill slope)

---

## 3. Why 4PL is Preferred
- Matches biological binding behavior  
- Handles **wide dynamic range**  
- Provides **interpretable parameters**  
- Enables accurate **interpolation of unknowns**

---

## 4. LL.4 Form Used in R (`drc`)

$y = c + \frac{d - c}{1 + \exp\big(b(\log x - \log e)\big)}$


### Key Identity

$\exp\big(b(\log x - \log e)\big) = (x/e)^b$


➡️ Same as standard 4PL, just rewritten

---

## 5. Why Use $(1 + \exp(b(\log x - \log e))$

### (1) Numerical Stability
- Avoids overflow/underflow from $$((x/e)^b)  $$
- Keeps computation in **log space**

### (2) Works in Log-Concentration Space
- ELISA curves are **symmetric in log(x)**  
- Improves model behavior and fitting

### (3) Direct Interpretation of EC50
- When \(x = e\):
  - exponent = 0 → denominator = 2  
  - response = midpoint  
- ✅ **e = EC50 directly**

### (4) Symmetry Around Midpoint
- Equal fold-changes (e.g., ×10 and ÷10) behave symmetrically  
- Matches biological systems

### (5) Optimization-Friendly
- Smooth exponential → stable gradients  
- Better convergence in nonlinear regression

---

## 6. Key Quality Metrics

### R² (Goodness of Fit)
- Measures how well model fits data  
- Close to 1 = better  
- ⚠️ Not sufficient alone

---

### CV (Coefficient of Variation)
\[
CV = \frac{\text{SD}}{\text{Mean}} \times 100\%
\]
- Measures **precision**  
- Typical threshold: <10–20%

---

### LLoQ (Lower Limit of Quantification)
- Lowest concentration with:
  - acceptable **precision (CV)**  
  - acceptable **accuracy (bias)**  
- Defines assay sensitivity

---

## 7. R Example (4PL Fit)

```r
install.packages("drc")
library(drc)

# Data
conc <- c(0.1, 0.5, 1, 5, 10, 50, 100)
absorbance <- c(0.05, 0.12, 0.2, 0.55, 0.8, 1.2, 1.35)
data <- data.frame(conc, absorbance)

# Fit 4PL
model <- drm(absorbance ~ conc, data = data, fct = LL.4())

# Summary
summary(model)

# Plot
plot(model, log = "x")

# Predict unknown
ED(model, respLev = 0.6, type = "absolute")

# Parameters
coef(model)