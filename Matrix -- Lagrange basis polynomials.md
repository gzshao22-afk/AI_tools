Definition of the Lagrange basis polynomial:
$$L_j(x)=\prod_{m\neq j}\frac{x-x_m}{x_j-x_m}$$
The idea is that with $(x_0,y_0),(x_1,y_1),(x_2,y_2),\cdots,(x_n,y_n)$ known, y value at any new points can be interpolated as:
$$y=\begin{bmatrix}L_0(x) &  L_1(x) & L_2(x) & \cdots & L_n(x)\\ \end{bmatrix} *\begin{bmatrix}y_0 \\ y_1 \\ y_2 \\ \vdots \\ y_n\\ \end{bmatrix}$$
Similarly, if we know the derivatives at all these points, we can obtain the derivative at any new points:
$$y'=\begin{bmatrix}L_0(x) &  L_1(x) & L_2(x) & \cdots & L_n(x)\\ \end{bmatrix} *\begin{bmatrix}y'_0 \\ y'_1 \\ y'_2 \\ \vdots \\ y'_n\\ \end{bmatrix}$$
To find y', we we construct a vector of the following shape:
$$\begin{bmatrix}L_0(x_0) & L_1(x_0) & \cdots & L_n(x_0)\\
L_0(x_1) & L_1(x_1) & \cdots & L_n(x_1)\\
\vdots & \vdots & \ddots & \vdots\\
L_0(x_n) & L_1(x_n) & \cdots & L_n(x_n)\\
\end{bmatrix}$$

The non-diagonal entries are all 0. However, by expanding each entry:
$$L_j(x)=\prod_{m\neq j}\frac{x-x_m}{x_j-x_m}$$
If we define the **node polynomial W(x)**, which contains all the roots $x_0, x_1, ..., x_n$:
$$W(x)=\prod_{m=0}^n(x-x_m)$$
We can rewrite $L_j(x)$ using $W(x)$ as:
$$L_j(x)=\prod \frac{W(x)}{(x-x_j)W_-(x_j)}$$
where $W_-(x_j)=\prod_{m\neq j}(x_j-x_m)$. This is a constant for a fixed j.

#### Deriving the off-diagonal
We differentiate $L_j(x)$ with respect to x using the quotient rule:
$$L'_j(x)=\frac{1}{W_-(x_j)}\left[\frac{W'(x)(x-x_j)-W(x)}{(x-x_j)^2}\right]$$
Now, we evaluate this at $x=x_i$:
+ Since $x_i$ is the root of $W(x)$, we know $W(x_i)=0$
+ Therefore, the formula simplifies to:
$$L'_j(x_i)=\frac{W'(x_i)}{W'(x_j)(x_i-x_j)}$$
If we define the weights $a_k=W'(x_k)=\prod_{m\neq k}(x_k-x_m)$, we get the standard off-diagonal formula:
$$D_{ij}=$$




