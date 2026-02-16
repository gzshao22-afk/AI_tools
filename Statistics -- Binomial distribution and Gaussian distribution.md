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
$$-k\cdot ln\left(\frac{np+x}{np}\right)=-k\cdot ln\left(1+\frac{x}{np}\right)$$
	as $ln\epsilon \approx\epsilon -\frac{\epsilon^2}{2}$,
	it becomes:
	$$-(np+x)\left( \frac{x}{np} - \frac{x^2}{2n^2p^2}\right)=-x+\frac{x^2}{2np}-\frac{x^2}{np}+\frac{x^3}{2n^2p^2}$$
	The last term can be ignored as $n \rightarrow \infty$, it becomes:
	$$-x-\frac{x^2}{2np}$$
3. The third term,
$$-(n-k)\cdot ln\left(\frac{n-k}{nq}\right)=-(nq-x)\cdot ln\left(1-\frac{x}{nq}\right)$$
	This simplifies to:
	$$-(nq-x)\left(-\frac{x}{nq}-\frac{x^2}{2n^2q^2}\right)=x+\frac{x^2}{2nq}-\frac{x^2}{nq}-\frac{x^3}{2n^2q^2} \approx x-\frac{x^2}{2nq}$$
Putting all 3 terms together:
$$ln\left(\sqrt{\frac{1}{2\pi npq}}\right) -\frac{x^2}{2n}\left(\frac1p+\frac1q\right)=ln\left(\sqrt{\frac{1}{2\pi npq}}\right)-\frac{x^2}{2n}\frac{1}{pq}$$

Putting back the exponential:
$$\sqrt{\frac{1}{2\pi npq}}e^{-\frac{x^2}{2npq}}$$
$npq$ is the variance, the above term becomes
$$\sqrt{\frac{1}{2\pi \sigma^2}}e^{-\frac{x^2}{2\sigma^2}}$$

