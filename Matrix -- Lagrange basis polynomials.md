Definition of the Lagrange basis polynomial:
$$L_j(x)=\prod_{m\neq j}\frac{x-x_m}{x_j-x_m}$$
The idea is that with $(x_0,y_0),(x_1,y_1),(x_2,y_2),\cdots,(x_n,y_n)$ known, y value at any new points can be interpolated as:
$$y=\begin{bmatrix}L_0(x) &  L_1(x) & L_2(x) & \cdots & L_n(x)\\ \end{bmatrix} *\begin{bmatrix}y_0 \\ y_1 \\ y_2 \\ \vdots \\ y_n\\ \end{bmatrix}$$
Similarly, if we know the derivatives at all these points, we can obtain the derivative at any new points:
$$y'=\begin{bmatrix}L_0'(x) &  L_1'(x) & L_2'(x) & \cdots & L_n'(x)\\ \end{bmatrix} *\begin{bmatrix}y_0 \\ y_1 \\ y_2 \\ \vdots \\ y_n\\ \end{bmatrix}$$




$$\begin{bmatrix}L_0(x_0) & L_1(x_0) & \cdots & L_n(x_0)\\
L_0(x_1) & L_1(x_1) & \cdots & L_n(x_1)\\
\vdots & \vdots & \ddots & \vdots\\
L_0(x_n) & L_1(x_n) & \cdots & L_n(x_n)\\
\end{bmatrix}$$