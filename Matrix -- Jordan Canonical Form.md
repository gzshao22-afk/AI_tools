> Why can we compute $e^{At}$ , where A is matrix, t is a vector, block-by-block when A is block diagonal?

---

## Step 1: What “block diagonal” really means

Suppose

$A =\begin{bmatrix} B & 0 \\ 0 & C \end{bmatrix}$

Here B and C act on **different subspaces** — they don’t mix coordinates.

That “no mixing” (the zero blocks) is the whole reason.

## Step 2: Matrix exponential definition

$e^{At}=I+At+\frac{A^2t^2}{2!}+\frac{A^3t^3}{3!}+⋯$

So everything depends on powers of A.

## Step 3: What happens when you square A?

$A^2 = \begin{bmatrix} B^2 & 0 \\ 0 & C^2 \end{bmatrix}$

Same pattern!

And in general:

$A^n = \begin{bmatrix} B^n & 0 \\ 0 & C^n \end{bmatrix}$

The zero blocks stay zero forever because there’s **no cross-interaction**.

## Step 4: Plug into the exponential series

$e^{At} = \sum\limits_{n=0}^{\infty} \frac{A^n t^n}{n!} = \sum\limits_{n=0}^{\infty} \frac{1}{n!} \begin{bmatrix} B^n t^n & 0 \\ 0 & C^n t^n \end{bmatrix}$

Add term by term:

$e^{At}= \begin{bmatrix} \sum\limits_{n=0}^\infty \frac{B^n t^n}{n!} & 0 \\ 0 & \sum\limits_{n=0}^\infty \frac{C^n t^n}{n!} \end{bmatrix}$

But those sums are just exponentials!

$\boxed{ e^{At} = \begin{bmatrix} e^{Bt} & 0 \\ 0 & e^{Ct} \end{bmatrix} }$​

## Howthis applies to Jordan form

Jordan form is:

$J= \begin{bmatrix} J_1 & 0 & 0\\ 0 & J_2 & 0\\ 0 & 0 & J_3 \end{bmatrix}$

Each $J_i$​ is a Jordan block → so

eJt=[eJ1t000eJ2t000eJ3t]e^{Jt}= \begin{bmatrix} e^{J_1t} & 0 & 0\\ 0 & e^{J_2t} & 0\\ 0 & 0 & e^{J_3t} \end{bmatrix}eJt=​eJ1​t00​0eJ2​t0​00eJ3​t​​

That’s why we can compute block by block.