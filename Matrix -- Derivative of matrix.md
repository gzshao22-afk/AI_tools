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


In the context of Ordinary Least Square regression problem:
To derive the **Ordinary Least Squares (OLS)** solution, we use the derivative of a quadratic form to find the best-fitting line for a dataset.

In simple terms, we want to find the vector of coefficients $\boldsymbol{\beta}$ that minimizes the distance between our predictions and the actual data.

---

## 1. Defining the Error (The Residuals)

Suppose we have a linear model $\mathbf{y} = \mathbf{X}\boldsymbol{\beta} + \boldsymbol{\epsilon}$. The "error" (residual) for our prediction is:

$$\mathbf{e} = \mathbf{y} - \mathbf{X}\boldsymbol{\beta}$$

To find the best fit, we minimize the **Sum of Squared Errors (SSE)**. In matrix notation, squaring a vector and summing it is the same as taking its inner product with itself:

$$S(\boldsymbol{\beta}) = \mathbf{e}^T \mathbf{e} = (\mathbf{y} - \mathbf{X}\boldsymbol{\beta})^T (\mathbf{y} - \mathbf{X}\boldsymbol{\beta})$$

---

## 2. Expanding into Quadratic Form

If we expand that expression using matrix algebra rules, we get:

$$S(\boldsymbol{\beta}) = \mathbf{y}^T\mathbf{y} - 2\boldsymbol{\beta}^T\mathbf{X}^T\mathbf{y} + \boldsymbol{\beta}^T(\mathbf{X}^T\mathbf{X})\boldsymbol{\beta}$$

Notice the parts of this equation:

- $\mathbf{y}^T\mathbf{y}$ is a constant (with respect to $\boldsymbol{\beta}$).
    
- $- 2\boldsymbol{\beta}^T\mathbf{X}^T\mathbf{y}$ is a **linear** term.
    
- $\boldsymbol{\beta}^T(\mathbf{X}^T\mathbf{X})\boldsymbol{\beta}$ is a **quadratic form** (where $\mathbf{A} = \mathbf{X}^T\mathbf{X}$).
    

---

## 3. Taking the Derivative

To find the minimum, we take the derivative with respect to $\boldsymbol{\beta}$ and set it to zero:

$$\frac{\partial S}{\partial \boldsymbol{\beta}} = 0 - 2\mathbf{X}^T\mathbf{y} + 2(\mathbf{X}^T\mathbf{X})\boldsymbol{\beta}$$

> **Wait, why $2(\mathbf{X}^T\mathbf{X})\boldsymbol{\beta}$?** > Because $\mathbf{X}^T\mathbf{X}$ is always a **symmetric matrix**. As we discussed, the derivative of the symmetric quadratic form $\mathbf{x}^T\mathbf{A}\mathbf{x}$ is $2\mathbf{Ax}$.

---

## 4. Solving for $\hat{\boldsymbol{\beta}}$

Now we just use basic algebra to isolate our goal:

$$2(\mathbf{X}^T\mathbf{X})\boldsymbol{\beta} = 2\mathbf{X}^T\mathbf{y}$$

$$(\mathbf{X}^T\mathbf{X})\boldsymbol{\beta} = \mathbf{X}^T\mathbf{y}$$

Finally, we multiply by the **inverse** of the matrix $(\mathbf{X}^T\mathbf{X})$ to solve for $\boldsymbol{\beta}$:

$$\hat{\boldsymbol{\beta}} = (\mathbf{X}^T\mathbf{X})^{-1} \mathbf{X}^T \mathbf{y}$$

This is the famous **Normal Equation**. It tells you exactly which weights to use to get the smallest possible error for your model.