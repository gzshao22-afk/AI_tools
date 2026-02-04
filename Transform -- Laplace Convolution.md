Laplace Transform applied to the convolution $f\ast g(t)$:
$$\mathcal{L}\{f\ast g\}
=\int_0^{\infty}e^{-st}\left(\int_0^t f(\tau)g(t-\tau)d\tau \right)dt$$

We can write this as a double integral over a region in the $(\tau, t)$ plane:
$$\int_0^\infty\int_0^t e^{-st}f(\tau)g(t-\tau)d\tau dt$$

