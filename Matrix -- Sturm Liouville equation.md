
### Variation of Parameters Formula
The variation of parameters formula provides a systematic way to find a

**particular solution** ($y_p$) for non-homogeneous linear differential equations. It is more general than other methods because it works for any forcing function 𝑔(𝑥), provided you can perform the required integration. 

**The Standard Formula (Second Order)** 

For a second-order differential equation in **standard form**:  
$$y^{′′}+p(x)y^{′}+q(x)y=g(x)$$
If $y_1$ and $y_2$ are linearly independent solutions to the homogeneous equation, the particular solution is given by:  
$$y_p(x)=u_1(x)y_1(x)+u_2(x)y_2(x)$$

Where the "parameters" $u_1$ and $u_2$ are calculated as:
$$u_1(x)=\int \frac{-y_2g(x)}{W(y_1,y_2)}dx$$
$$u_2(x)=\int \frac{-y_1g(x)}{W(y_1,y_2)}dx$$


The term $𝑊(𝑦_1,𝑦_2)$ is the Wronskian, defined as the determinant:  
$$W=y_1 y_{2}^{'}-y_2 y_{1}^{'}$$

**General Formula for n-th Order**
For higher-order equations, the formula generalizes using a system of linear equations. A particular solution for an n-th order equation is: 
$$y_p(x)=\sum_{i=1}^{n}u_i(x)y_i(x)$$

The derivatives of these functions, $u_i^{'}$, are found by solving the following matrix equation:

$$\begin{bmatrix}
y_1 & y_2 & \cdots & y_n\\ 
y_1^{'} & y_2^{'} & \cdots & y_n^{'}\\ \vdots & \vdots & \ddots & \vdots \\ y_1^{n-1} & y_2^{n-1} & \cdots & y_n^{n-1}
\end{bmatrix}
\begin{bmatrix} 
u_1^{'} \\ u_1^{2} \\ \vdots\\u_1^{n-1} \end{bmatrix}
= 
\begin{bmatrix}
0 \\ 0 \\ \vdots \\ g(x)
\end{bmatrix}
$$

![](./assets/Matrix%20--%20Sturm%20Liouville%20equation/file-20260201152315864.png)

![](./assets/Matrix%20--%20Sturm%20Liouville%20equation/file-20260201152328928.png)

![](./assets/Matrix%20--%20Sturm%20Liouville%20equation/file-20260201152345556.png)

![](./assets/Matrix%20--%20Sturm%20Liouville%20equation/file-20260201152402959.png)

![400](./assets/Matrix%20--%20Sturm%20Liouville%20equation/file-20260201152520952.png)


### Cauchy-Euler Equation

General form:
$$a_nx^n\frac{d^ny}{dx^n} + a_{n-1}x^{n-1}\frac{d^{n-1}y}{dx^{n-1 }} + \cdots + a_1x\frac{dy}{dx}+a_0y = f(x)$$
Example problem:
$$x^2y{''}-xy-3y=2x^2$$
1. Assuming $y =x^r$, Find the homogeneous solution to $$x^2y{''}-xy-3y=0$$
2. Find the Particular Solution ($y_p$)
   For the non-homogeneous term $f(x)=2x^2$, we can use the method of Variation of Parameters. 
![400](./assets/Matrix%20--%20Sturm%20Liouville%20equation/file-20260202093328866.png)

![400](./assets/Matrix%20--%20Sturm%20Liouville%20equation/file-20260202093350095.png)
![400](./assets/Matrix%20--%20Sturm%20Liouville%20equation/file-20260202093432558.png)

![400](./assets/Matrix%20--%20Sturm%20Liouville%20equation/file-20260202093452355.png)


#### Another example problem
![400](./assets/Matrix%20--%20Sturm%20Liouville%20equation/file-20260202141430686.png)
![400](./assets/Matrix%20--%20Sturm%20Liouville%20equation/file-20260202141613904.png)
![400](./assets/Matrix%20--%20Sturm%20Liouville%20equation/file-20260202141645844.png)
![400](./assets/Matrix%20--%20Sturm%20Liouville%20equation/file-20260202141706080.png)

![400](./assets/Matrix%20--%20Sturm%20Liouville%20equation/file-20260202141723916.png)


### Bessel's Equation

The Bessel equation of order $\alpha$
$$x^2\frac{d^2y}{dx^2}+x\frac{dy}{dx}+(x^2-\alpha^2)y=0$$
where $\alpha$ is a constant, often an integer or half-integer, representing the order of the equation.

![400](./assets/Matrix%20--%20Sturm%20Liouville%20equation/file-20260202152709197.png)

![400](./assets/Matrix%20--%20Sturm%20Liouville%20equation/file-20260202152759236.png)

![400](./assets/Matrix%20--%20Sturm%20Liouville%20equation/file-20260202152821912.png)

![400](./assets/Matrix%20--%20Sturm%20Liouville%20equation/file-20260202152844881.png)

![400](./assets/Matrix%20--%20Sturm%20Liouville%20equation/file-20260202152912634.png)

![400](./assets/Matrix%20--%20Sturm%20Liouville%20equation/file-20260202152942562.png)


### Legendre's Equation
The standard form:
$$(1-x^2)\frac{d^2y}{dx^2}-2x\frac{dy}{dx}+l(l+1)y=0$$
The solutions: Legendre Polynomials. Here are the first few:
+ $P_0(x)=1$
+ $P_1(x)=x$
+ $P_2(x)=\frac12(3x^2-1)$
+ $P_3(x)=\frac12(5x^3-3x)$

Instead of solving the ODE from scratch every time, you can generate any Legendre Polynomial using **Rodrigues' Formula**:
$$P_l(x)=\frac{1}{2^ll!}\frac{d^l}{dx^l}(x^2-1)^l$$



&Ouml;
AT&amp;T
'AT&T'






 




### Schrodinger's equation




### Green's function

