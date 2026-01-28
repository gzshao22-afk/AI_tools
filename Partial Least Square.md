
### Summary of the PLS Workflow

| **Step**        | **Operation**    | **Purpose**                                           |
| --------------- | ---------------- | ----------------------------------------------------- |
| **Pre-process** | Center & Scale   | Put all variables on an equal playing field.          |
| **Supervise**   | $X^T Y$          | Find the direction that actually predicts the target. |
| **Compress**    | $t = Xw$         | Turn many variables into one "Latent Component."      |
| **Deflate**     | $X - tp^T$       | Remove the "explained" info to find the next signal.  |
| **Validate**    | Cross-Validation | Stop before you start modeling noise (Variance).      |


### Phase 1: Data Treatment
### 1. Mean Centering

Subtract the average from every column. This ensures the model focuses on **change** (deviations) rather than absolute magnitude.

$$X_{centered} = X - \bar{X}$$

$$Y_{centered} = Y - \bar{Y}$$
### 2. Auto-scaling (Standardization)

Divide by the standard deviation. This ensures a feature measured in "grams" doesn't overpower a feature measured in "tons."

$$X_{scaled} = \frac{X_{centered}}{\sigma_X}$$

___
### Phase 2: The Iterative Loop (Kernel)
### 3. Compute Weights ($w$) via Supervision

This is the $X^T Y$ step. It finds the direction in $X$ that has the highest covariance with $Y$.

$$w = X^T Y$$

_We then normalize $w$ so its length equals 1._

### 4. Generate Scores ($t$)

We project our data onto that weight vector to get a single "summary" column.

$$t = Xw$$


### 5. Calculate Loadings ($p$ and $c$)

We see how much our new score $t$ actually explains the original data.

- **X-loading ($p$):** $p = (X^T t) / (t^T t)$
    
- **Y-loading ($c$):** $c = (Y^T t) / (t^T t)$

____
### Phase 3: Deflation (The Cleanup)

### 6. Deflate the Matrices

We calculate the "Residuals" (the leftovers).

$$X_{new} = X - tp^T$$

$$Y_{new} = Y - tc^T$$

**Repeat:** You now take $X_{new}$ and $Y_{new}$ back to **Step 3** to find the next component.

___
### Phase 4: 

Once you have extracted $k$ components (determined by cross-validation):

### 7. Construct the Final Regression

The final model looks like a standard regression, but it's built on the stable "Scores" rather than the shaky original features.

$$\hat{Y} = T C^T$$

### 8. Convert back to Original Units

Because we scaled and centered at the start, the model does a final "un-scaling" so you can input raw data and get a real prediction (e.g., actual "Yield" in kg).


