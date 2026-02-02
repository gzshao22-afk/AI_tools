
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

### Green's function


<div style="background-color: #e3e3e3; padding: 10px; border: 1px solid #ccc; ">
This is text inside a colored box.
</div>


