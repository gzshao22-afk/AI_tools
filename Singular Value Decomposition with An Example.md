1. The Original Matrix is 
	$\begin{bmatrix}3 & 2 & 2 \\ 2 & 3 & -2 \end{bmatrix}$

2. $A*A^T$ gives 
	$A*A^T$ = $\begin{bmatrix} 3 & 2 & 2 \\ 2 & 3 & -2 \end{bmatrix}$ $\begin{bmatrix} 3 & 2 \\ 2 & 3 \\ 2 & -2 \end{bmatrix}$ =$\begin{bmatrix} 17 & 8 \\ 8 & 17 \end{bmatrix}$
3. The eigenvalues and eigenvectors can be found to be $\lambda_1=25$ $\lambda_2=9$
	$u_1=\frac{1}{\sqrt{2}}\begin{bmatrix}1 \\ 1\end{bmatrix}$
	$u_2=\frac{1}{\sqrt{2}}\begin{bmatrix}1 \\ -1\end{bmatrix}$
4. This gives U in $U\Sigma V^T$ as
	$\begin{bmatrix}\frac{1}{\sqrt{2}} & \frac{1}{\sqrt{2}} \\ \frac{1}{\sqrt{2}} & -\frac{1}{\sqrt{2}} \end{bmatrix}$

5. Now to find V, first calculate $A^T*A$ = $A*A^T$ =  $\begin{bmatrix} 3 & 2 \\ 2 & 3 \\ 2 & -2 \end{bmatrix}$ $\begin{bmatrix} 3 & 2 & 2 \\ 2 & 3 & -2 \end{bmatrix}$ = $\begin{bmatrix} 13 & 12 & 2 \\ 12 & 13 & -2 \\ 2 & -2 & 8\end{bmatrix}$
6. We use the eigenvalues found previously found eigenvalues  $\lambda_1=25$ $\lambda_2=9$ and $\lambda_3=0$
$\lambda_3=0$
	this gives $\begin{bmatrix}1/\sqrt{2} & 1/3\sqrt{2} & -2/3 \\1/\sqrt{2} & -1/3\sqrt{2} & 2/3 \\0 & 4/3\sqrt{2} & 1/3 \end{bmatrix}$


7. U and V have shared non-zero eigenvalues because:

![500](./assets/Singular%20Value%20Decomposition%20with%20An%20Example/file-20260129073240509.png)


![500](./assets/Singular%20Value%20Decomposition%20with%20An%20Example/file-20260129103109307.png)
![500](./assets/Singular%20Value%20Decomposition%20with%20An%20Example/file-20260129103145595.png)

![500](./assets/Singular%20Value%20Decomposition%20with%20An%20Example/file-20260129103213326.png)

![500](./assets/Singular%20Value%20Decomposition%20with%20An%20Example/file-20260129103242979.png)

