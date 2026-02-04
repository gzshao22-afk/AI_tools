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
