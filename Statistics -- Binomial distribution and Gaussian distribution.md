 $$Binomial(n,p) \approx \mathcal N(np,np(1-p))$$
 Probability mass function (PMF) of a Binomial random variable $X ~ Binomial(n,p)$ is:
 $$P(X=k)={n \choose k}p^k(1-p)^{n-k}=\frac{n!}{k!(n-k)!}p^kq^{n-k}$$
 where $q=1-p$

Applying Stirling's Approximation: when n is large:
$$n! \approx \sqrt{2\pi n}\left(\frac{n}{e}\right)^n$$
Substituting this for in the PMF:
$$\begin{align}
P(X=k) & \approx \sqrt{\frac{n}{2\pi k(n-k)}} \frac{n^n}{k^k(n-k)^{n-k}}p^kq^{n-k}\\
& = \sqrt{\frac{n}{2\pi k(n-k)}}\left(\frac{np}{k}\right)^k\left(\frac{nq}{n-k}\right)^{n-k}
\end{align}$$
Let the mean be $\mu=np$, the deviation from the mean as $x=k-np$. Therefore:
+ $k=np+x$
+ $n-k=nq-x$

Logarithmic Transformation: take the natural log of this expression:
1. The first term, as n becomes large, $k=np$
$$ln\left(\sqrt{\frac{n}{2\pi k(n-k)}}\right)=ln\left(\sqrt{\frac{n}{2\pi npq}}\right)$$
2. The second term, 
$$ln()$$