# 1. The Solute as a Random Walk

  
Imagine a single molecule moving through \(N\) plates. 

At each plate, it has a choice:

- \(p\): the probability it is in the **mobile phase** (moving forward) 

- \(q = 1 - p\): the probability it is in the **stationary phase** (staying still)

The molecule’s journey is a series of \(N\) independent “trials.” 

This follows a **binomial distribution**.

---

# 2. Statistical Properties

For a binomial distribution, the mean and variance are:

- **Mean** ($\mu$): $np$
- **Variance** ($\sigma^2$): $np(1-p)$

---
# 3. Relating to Chromatography

In chromatography, we don’t observe the individual microscopic trials. 

Instead, we observe **Retention time** ($t_R$) and **Peak width** ($\sigma$)

  

These correspond to the statistical properties of the random walk:
+ The Mean ($\mu$): The retention time $t_R$ is proportional to the average numbers of steps taken to exit. So, $t_R \propto np$
+ The Variance ($\sigma^2$): The peak spread $\sigma^2$ is proportional to the variance of those steps, so $\sigma^2 \propto np(1-p)$
---
# 4. The Derivation of \(N\)

  To isolate the number of plates, consider the ratio of the squared mean to the variance:
$$

\frac{\mu^2}{\sigma^2}

= \frac{(np)^2}{npq}

= n \cdot \frac{p}{q}$$

In HPLC, \(n\) is very large, p and q are both distant from 0 and 1 for molecules with significant interactions with the stationary an mobile phases, and the binomial distribution **converges to a Gaussian**. 

In this Gaussian limit, the plate number is defined as:
$$
N = \left( \frac{t_R}{\sigma} \right)^2
$$
This expression captures how sharply and efficiently a peak elutes: narrower peaks and longer retention correspond to a larger plate count.