## 1. The Bias-Variance Tradeoff

**Question:** Explain the Bias-Variance tradeoff.

**Answer:** The bias-variance tradeoff is the central struggle of building models that generalize well. It is a balancing act between two types of error:

- **Bias (Underfitting):** Error caused by overly simplistic assumptions (e.g., fitting a straight line to curved data). The model misses the "big picture."
    
- **Variance (Overfitting):** Error caused by over-sensitivity to small fluctuations in the training set. The model captures "noise" instead of the "signal."
    

**The Goal:** To find the "Sweet Spot" where **Total Error** is minimized.

$$\text{Total Error} = \text{Bias}^2 + \text{Variance} + \text{Irreducible Error}$$
___

