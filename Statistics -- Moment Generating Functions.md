$$M_x(t)=E[e^{tX}]$$
The reason we use $e^{tX}$ is because of its Taylor Series expansion:
$$e^{tX}=1+tX+\frac{(tX)^2}{2!}+\frac{(tX)^3}{3!}+\cdots$$
When take the expectation of the whole string:
$$M_X(t)=1+tE[X]+\frac{t^2}{2!}E[X^2]+\frac{t^3}{3!}E[X^3]+\cdots$$
Example: The Bernouli Distribution (A coin flip)
Imagine a coin flip where:
+ $X=1$ ()