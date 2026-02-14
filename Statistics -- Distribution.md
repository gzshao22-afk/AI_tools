#Gaussian_distribution #Poisson_distribution #Exponential_distribution #Lognormal_distribution #Exponential_modified_Gaussian_distribution #Lorentzian_distribution

Summary of the Connections

|Perspective|Question|Distribution|
|---|---|---|
|**Counting**|"How many spikes occurred in 1 second?"|**Poisson**|
|**Timing**|"How long did I wait for the _next_ spike?"|**Exponential**|
|**Combined**|"Total time = Physical signal + Waiting for the spike"|**ExGaussian**|

Poisson distribution:
$$P(X=k)=\frac{\lambda^k*e^{-\lambda}}{k!}$$
>[!Note]
>+ $k$: the number of occurrences (0, 1, 2, ...)
>+  $\lambda$: the average number of events in the interval (rate)
>+ $e$: Euler's number (~2.718)
>+ $k!$: The factorial of $k$

If we know the rate of occurrences, the probability of 0 occurrence happening in the upcoming time period of $t$ is:
$$P(X=0)=\frac{\lambda_t^0e^{-\lambda_t}}{0!}=e^{-\lambda_t}$$
where $\lambda_t$ is the adjusted occurrence rate in for the new time frame.

Poisson distribution:
$$P(X=k)=\frac{\lambda^k*e^{-\lambda}}{k!}$$
>[!Note]
Given a Poisson distribution for occurrences, the wait time between event is an exponential distribution.

Poisson distribution is derived from binomial distribution
$$P(X=k)=\begin{pmatrix}n \\ k\end{pmatrix}p^k(1-p)^{n-k}$$
When Poisson was investigating legal probabilities such as wrongful convictions, he found as $n \rightarrow \infty, p \rightarrow 0$, calculation becomes extremely difficult. He observed that their product remains a constant, $\lambda=np$. Plugging this into the binomial equation
$$\begin{align}P(X=k) 
& = {n \choose k}p^k(1-p)^{n-k} \\
& = \frac{n!}{k!(n-k)!}\cdot \frac{\lambda^k}{n^k}\cdot \left(1-\frac{\lambda}{n}\right)^n \cdot \left( 1-\frac{\lambda}{n}\right)^{-k}
\end{align}$$

**Step 1:**
$$\frac{n!}{k!(n-k)!}\cdot \frac{\lambda^k}{n^k}$$
becomes
$$\frac{n!}{n^k(n-k)!}\cdot \frac{\lambda^k}{k!}=\frac{n\cdot(n-1)\cdot(n-2)\cdots(n-k+1)}{n^k}\cdot \frac{\lambda^k}{n^k}
$$
when n is very large, 
$$\frac{n\cdot(n-1)\cdot(n-2)\cdots(n-k+1)}{n^k}$$
becomes 1, it simplifies to:
$$\frac{\lambda^k}{n^k}$$


**Step 2:**
$$\left(1-\frac{\lambda}{n}\right)^n$$
By definition, $\lim_{n \to \infty}(1+\frac{x}{n})^n=e^x$. Therefore:
$$\left(1-\frac{\lambda}{n}\right)^n \rightarrow e^{-\lambda}$$


**Step 3:**
$$\left( 1-\frac{\lambda}{n}\right)^{-k}$$
as n approaches infinity, the values becomes 0, thus Poisson distribution expression:
$$P(X=k)=\frac{\lambda^k*e^{-\lambda}}{k!}$$



### Negative Binomial Distribution
When mean of Poisson distribution is smaller than its variance, e.g., bursts of events. Example: A tour bus arrives! Suddenly 50 people walk in at once, then nobody for two hours. The average is still 10 per hour.

>[!Definition] The definition of the Negative Binomial is: "The probability of having exactly $k$ failures before the $r$-th success."
1. The very last trial must be a success;
2. In all previous trials, you must have exactly $r-1$ successes and $k$ failures.
$$P(X=k)={k+r-1 \choose k} \times p^r \times (1-p)^k$$
Unlike the standard binomial of $(p+q)^n$, negative binomial is $p^r(1-q)^{-r}$, where p is success rate and q is failure rate, r is the number of successes.
$$p^r(1-q)^{-r}=(1-q)^r(1-q)^{-r}=1$$

