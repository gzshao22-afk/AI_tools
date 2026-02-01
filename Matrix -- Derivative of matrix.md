In linear algebra, a **quadratic form** is a scalar-valued function that maps a vector to a real number through a square matrix. It’s "quadratic" because if you expand the expression, every term is of the second degree (e.g., $x_1^2$, $x_1x_2$, etc.).

The standard notation for a quadratic form is:

$$f(\mathbf{x}) = \mathbf{x}^T \mathbf{A} \mathbf{x}$$

Where:

- $\mathbf{x}$ is a column vector of size $n \times 1$.
    
- $\mathbf{A}$ is a square matrix of size $n \times n$.
    
- $\mathbf{x}^T$ is the transpose of $\mathbf{x}$ (a $1 \times n$ row vector).
-

## Visualizing the Expansion

If you have a $2 \times 2$ matrix, the multiplication looks like this:

$$f(\mathbf{x}) = \begin{bmatrix} x_1 & x_2 \end{bmatrix} \begin{bmatrix} a_{11} & a_{12} \\ a_{21} & a_{22} \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \end{bmatrix} = a_{11}x_1^2 + (a_{12} + a_{21})x_1x_2 + a_{22}x_2^2$$

> **Note:** In most applications (like physics or statistics), we assume $\mathbf{A}$ is **symmetric** ($a_{12} = a_{21}$), which simplifies the middle term to $2a_{12}x_1x_2$.


## Finding the Derivative

When we talk about the derivative of a quadratic form, we are usually finding the **gradient** with respect to the vector $\mathbf{x}$.

The goal is to find $\nabla_{\mathbf{x}} (\mathbf{x}^T \mathbf{A} \mathbf{x})$.

### 1. Using the Product Rule

Think of $\mathbf{x}^T \mathbf{A} \mathbf{x}$ as the product of two terms: $\mathbf{u} = \mathbf{x}^T$ and $\mathbf{v} = \mathbf{Ax}$. Using the matrix version of the product rule:

1. Differentiate with respect to the "first" $\mathbf{x}$: $(\frac{\partial \mathbf{x}^T}{\partial \mathbf{x}}) \mathbf{Ax} = \mathbf{I} \mathbf{Ax} = \mathbf{Ax}$.
    
2. Differentiate with respect to the "second" $\mathbf{x}$: $\mathbf{x}^T \mathbf{A} (\frac{\partial \mathbf{x}}{\partial \mathbf{x}}) = \mathbf{x}^T \mathbf{A}$.
    

To keep the dimensions consistent for a gradient (which should be a column vector), we transpose the second part: $(\mathbf{x}^T \mathbf{A})^T = \mathbf{A}^T \mathbf{x}$.

### 2. The General Result

The derivative of the quadratic form is:

$$\frac{\partial}{\partial \mathbf{x}} (\mathbf{x}^T \mathbf{A} \mathbf{x}) = (\mathbf{A} + \mathbf{A}^T) \mathbf{x}$$

### 3. The Symmetric Case (Most Common)

If the matrix $\mathbf{A}$ is symmetric (meaning $\mathbf{A} = \mathbf{A}^T$), the formula simplifies beautifully, much like the power rule in basic calculus ($d/dx [ax^2] = 2ax$):

$$\frac{\partial}{\partial \mathbf{x}} (\mathbf{x}^T \mathbf{A} \mathbf{x}) = 2\mathbf{Ax}$$

