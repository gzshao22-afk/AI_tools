Laplace Transform applied to the convolution $f\ast g(t)$:
$$\mathcal{L}\{f\ast g\}
=\int_0^{\infty}e^{-st}\left(\int_0^t f(\tau)g(t-\tau)d\tau \right)dt$$

We can write this as a double integral over a region in the $(\tau, t)$ plane:
$$\int_0^\infty\int_0^t e^{-st}f(\tau)g(t-\tau)d\tau dt$$
The current limits are $0\leq \tau \leq t$ and $0 \leq t \leq \infty$. This describes a triangular region in the plane. If we flip the order of integration (integrating $t$ first), the limits become $\tau \leq t \leq \infty$ and $0\leq \tau \leq \infty$.

Our integral now looks like this:
$$\int_0^\infty f(\tau)\left(\int_{\tau}^{\infty}e^{-st}g(t-\tau)dt\right)d\tau$$

+ Let $u = t-\tau$
+ Then $dt=du$
+ When $t=\tau, u=0$
+ When $t\rightarrow \infty, u\rightarrow \infty$
+ Also, note that $t=u+\tau$, so $e^{-st}=e^{-s(u+\tau)}=e^{-su}e^{-s\tau}$

Plugging these terms into the inner integral:
$$\int_0^{\infty}f(\tau)\left(\int_0^{\infty}e^{-s\tau}e^{-su}g(u)du\right)d\tau$$
Separation of Variables, it becomes:
$$\left(\int_0^\infty e^{-s\tau}f(\tau)d\tau\right)\cdot \left(\int_0^\infty e^{-su}g(u)du\right)$$
By definition:
+ The first part is $\mathcal L\{f\}$
+ The second part is $\mathcal L\{g\}$
Thus, $\mathcal L\{f\ast g\}=F(s)\cdot G(s)$


#### D'Alembert's Work on Taylor's Theorem and Laplace Transform
Start with the Fundamental Theorem of Calculus:
$$f(x)=f(a)+\int_a^xf'(t)dt$$
To perform integration by parts, $\int udv=uv-\int vdu$. If we let $v=-(x-t)$
+ Let $u=f'(t) \Longrightarrow du=f''(d)dt$
+ Let $dv=dt \Longrightarrow v=-(x-t)$
Applying the formula:
$$\int_a^xf'(t)dt=\left[-f'(t)(x-t)\right]_a^x - \int_a^x-(x-t)f''(t)dt$$

This gives us:
$$f(x)=f(a)+f'(a)(x-a)+\int_a^x(x-t)f''(t)dt$$

The second Iteration.
To evaluate $\int_a^x(x-t)f''(t)dt$ :
+ Let $u=f''(t) \Longrightarrow du=f'''(t)dt$
+ Let $dv=(x-t)dt \Longrightarrow v=-\frac{(x-t)^2}{2}$
Applying integration by parts again:
$$\int_a^x(x-t)f''(t)dt=\left[-f''(t)\frac{(x-t)^2}{2}\right]_a^x + \int_a^x\frac{(x-t)^2}{2}f'''(t)dt$$
Again, this yields:
$$f(x)=f(a)+f'(a)(x-a)+\frac{f''(a)}{a}(x-a)^2+\int_a^x\frac{(x-t)^2}{2}f'''(t)dt$$
For the n-th step, the integral remainder $R_n(x)$ becomes:
$$R_n(x)=\int_a^x\frac{(x-t)^n}{n!}f^{n+1}(t)dt$$

This is the Laplace transform of two functions:
+ $g(t)=\frac{t^n}{n!}$
+ $h(t)=f^{n+1}(t)$
Applying Laplace Transform and using the Convolution Theorem:
$$\mathcal L\{R_n(x)\}=\mathcal L\{\frac{t^n}{n!}\} \,\cdot\,\mathcal L\{f^{(n+1)}(t)\}$$
![](./assets/Transform%20--%20Laplace%20Convolution/file-20260204163911776.png)
![](./assets/Transform%20--%20Laplace%20Convolution/file-20260204163943774.png)


