$$M_x(t)=E[e^{tX}]$$
The reason we use $e^{tX}$ is because of its Taylor Series expansion:
$$e^{tX}=1+tX+\frac{(tX)^2}{2!}+\frac{(tX)^3}{3!}+\cdots$$
When take the expectation of the whole string:
$$M_X(t)=1+tE[X]+\frac{t^2}{2!}E[X^2]+\frac{t^3}{3!}E[X^3]+\cdots$$
Example: The Bernoulli Distribution (A coin flip)
Imagine a coin flip where:
+ $X=1$ Heads with probability p
+ $X=0$ Tails with probability q (which is 1-p)
1. Find the MGF
	By definition of expectation ($Value \times Probability$):
	 $$M_X(t)=(e^{t\cdot 1}\cdot p)+(e^{t\cdot 0}\cdot q)$$
$$M_X(t)=pe^t+q$$
	 To find the mean:
	 + Step A (Derivative): the derivative of $M_X(t)=pe^t+q$ is $pe^t$
	 + Step B (set $t=0$): $pe^0=p\cdot 1=p$


#### How it MGF used to prove the Central Limit Theorem
>[!The Central Limit Theorem] 
>The sum of almost any random variables will eventually look like a Normal distribution, even if the individual variables are weird or skewed.

1. Standardize the Variables:
	 First transform random variables $X_i$ into standard units $Z_i$, so they all have a mean of 0 and variance of 1
	 $$Z_i=\frac{X_i-\mu}{\sigma}$$
2. Multiplying of MGF
	The MGF of a sum of independent variables is the product of their individual MGFs. If we have n identical variables, we get:
	$$M_{Sum}(t)=[M_Z(t)]^n$$
	Because we are looking at the average:
	$$M_{Average}(t)=\left[M_Z\left(\frac{t}{\sqrt{n}}\right)\right]^n$$
	Taylor expansion of MGF:
	$$M_Z(s)=1+(Mean)s+\frac{Variance}{2}s^2+\cdots$$
	With Mean=0 and Variance=1, it simplifies to:
	$$M_Z\left(\frac{t}{\sqrt{n}}\right) \approx 1+ 0+\frac12\left(\frac{t}{\sqrt{n}}\right)^2 = 1+\frac{t^2}{2n}$$
3. As $n \rightarrow \infty$,  $\left(1+\frac{t^2}{2n}\right)^n$ becomes $e^{t^2/2}$