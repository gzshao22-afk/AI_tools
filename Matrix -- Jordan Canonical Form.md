> Why can we compute $e^{At}$ , where A is matrix, t is a vector, block-by-block when A is block diagonal?

---

## Step 1: What “block diagonal” really means

Suppose

A= $\begin{bmatrix} B & 0 \\ 0 & C \end{bmatrix}$

Here B and C act on **different subspaces** — they don’t mix coordinates.

That “no mixing” (the zero blocks) is the whole reason.

## Step 2: Matrix exponential definition

$e^{At}=I+At+\frac{A^2t^2}{2!}+\frac{A^3t^3}{3!}+⋯$

So everything depends on powers of AAA.