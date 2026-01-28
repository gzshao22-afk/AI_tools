## 1. The Bias-Variance Tradeoff

**Question:** Explain the Bias-Variance tradeoff.

**Answer:** The bias-variance tradeoff is the central struggle of building models that generalize well. It is a balancing act between two types of error:

- **Bias (Underfitting):** Error caused by overly simplistic assumptions (e.g., fitting a straight line to curved data). The model misses the "big picture."
    
- **Variance (Overfitting):** Error caused by over-sensitivity to small fluctuations in the training set. The model captures "noise" instead of the "signal."
    

**The Goal:** To find the "Sweet Spot" where **Total Error** is minimized.

$$\text{Total Error} = \text{Bias}^2 + \text{Variance} + \text{Irreducible Error}$$
___
## 2. Unbiased Regression & BLUE

**Question:** What is unbiased regression and what is an example of BLUE?

**Answer:** An **unbiased** regression is a model where the expected value of the parameter estimates equals the true population parameters. In statistics, the "gold standard" is the **BLUE** (**B**est **L**inear **U**nbiased **E**stimator).

- **Example:** Predicting **Hourly Wages** based on **Years of Education** using Ordinary Least Squares (OLS).
    
- If the relationship is linear and no key variables are omitted, OLS is BLUE because it hits the target "on average" and has the lowest variance among all unbiased linear models.
___
## 3. Ridge Regression (The "Leash")

**Question:** How does Ridge regression intentionally introduce bias?

**Answer:** Ridge introduces bias through **Shrinkage**. It adds a penalty to the cost function based on the **square** of the coefficients ($L2$ penalty).

$$\text{Cost} = \text{SSE} + \lambda \sum \beta^2$$

- **The Intentional Bias:** By forcing coefficients to be smaller, the model no longer perfectly fits the training data.
    
- **The Benefit:** It prevents the model from "over-reacting" to noise, drastically reducing variance and making the model more stable.

___
## 4. Lasso Regression (The "Scalpel")

**Question:** Explain Lasso regression.

**Answer:** Lasso (Least Absolute Shrinkage and Selection Operator) uses an **absolute value** penalty ($L1$ penalty) instead of a squared one.

$$\text{Cost} = \text{SSE} + \lambda \sum |\beta|$$

- **Feature Selection:** Unlike Ridge, Lasso can force coefficients to be **exactly zero**.
    
- **Use Case:** Use Lasso when you suspect only a few features out of many are actually important. It simplifies the model by "evicting" useless variables.
___
## 5. Partial Least Squares (PLS)

**Question:** Why do we need PLS, and how does it work?

**Answer:** While Ridge and Lasso work on original features, **PLS** is a **Supervised Dimensionality Reduction** technique.

- **The Problem:** When you have more features than rows ($p > n$) or highly correlated variables, Ridge and Lasso can struggle.
    
- **The Mechanism:** PLS creates new "Latent Components" (summaries of your data). Unlike PCA, which only looks at $X$ variance, PLS looks for directions in $X$ that specifically explain the variance in $Y$.
    
- **The Result:** It boils down thousands of messy, redundant variables into a few highly predictive "themes."

___
## 6. Comparison Summary Table

| **Method** | **Penalty** | **Feature Selection?** | **Bias** | **Variance** | **Best For...**                        |
| ---------- | ----------- | ---------------------- | -------- | ------------ | -------------------------------------- |
| **OLS**    | None        | No                     | Zero     | High         | Theoretical proof/interpretation.      |
| **Ridge**  | $L2$        | No                     | Moderate | Low          | Stable predictions with many features. |
| **Lasso**  | $L1$        | **Yes**                | Moderate | Low          | Sparse data (few important features).  |
| **PLS**    | Latent      | **Yes** (Combined)     | Moderate | Low          | Wide data ($p > n$) or Spectroscopy.   |
|            |             |                        |          |              |                                        |
