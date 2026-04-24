

---

## 1. Intuition: What Green’s Theorem Says

**Green’s Theorem** connects a **line integral around a closed curve** to a **double integral over the region inside**.

$$
\oint_C (P\,dx + Q\,dy) = \iint_D \left(\frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y}\right)\, dA
$$

### Intuitive Picture
- Think of a vector field flowing in a region \(D\)
- The left side = **circulation along the boundary \(C\)**
- The right side = **sum of tiny rotations (curl) inside the region**

👉 Key idea:
> The total “rotation” inside a region equals the circulation along its boundary.

---

## 2. Intuitive Breakdown

- Each tiny area contributes a **local rotation**
- Internal edges cancel out when summing
- Only the **outer boundary remains**

This is why:
- Local behavior (derivatives) → global behavior (integral)

---

## 3. Rigorous Statement

Let:
- \(C\): positively oriented, piecewise smooth, closed curve  
- \(D\): region enclosed by \(C\)  
- \(P(x,y), Q(x,y)\): functions with continuous partial derivatives  

Then:

$$
\oint_C (P\,dx + Q\,dy)
=
\iint_D \left(\frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y}\right)\, dA
$$

---

## 4. Sketch of Proof (Idea)

1. Break region \(D\) into many small rectangles  
2. Apply the theorem to each rectangle  
3. Adjacent edges cancel (opposite directions)  
4. Only boundary terms remain  

This is analogous to:
- Discrete → continuous limit  
- Cancellation of internal contributions  

---

## 5. Applications of Green’s Theorem

---

### 5.1 Area Calculation

Choose:
$$
P = 0, \quad Q = x
$$

Then:

$$
\text{Area} = \iint_D 1\, dA = \oint_C x\,dy
$$

Alternative form:

$$
\text{Area} = \frac{1}{2} \oint_C (x\,dy - y\,dx)
$$

---

### Example: Area of a Circle

Let:
$$
x = R\cos t,\quad y = R\sin t
$$

Then:

$$
\text{Area} = \frac{1}{2} \oint_C (x\,dy - y\,dx) = \pi R^2
$$

---

### 5.2 Circulation of a Vector Field

Let:
$$
\mathbf{F} = (P, Q)
$$

Then:

$$
\text{Circulation} = \oint_C \mathbf{F} \cdot d\mathbf{r}
$$

Green’s theorem gives:

$$
= \iint_D \left(\frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y}\right)\, dA
$$

---

### Example

Let:
$$
\mathbf{F} = (-y, x)
$$

Then:

$$
\frac{\partial Q}{\partial x} = 1,\quad \frac{\partial P}{\partial y} = -1
$$

So:

$$
\text{curl} = 2
$$

Thus:

$$
\oint_C \mathbf{F} \cdot d\mathbf{r} = 2 \cdot \text{Area}(D)
$$

---

## 6. Transition to Complex Analysis

Let:
$$
z = x + iy, \quad f(z) = u(x,y) + i v(x,y)
$$

We want to evaluate:

$$
\oint_C f(z)\,dz
$$

---

### Expand \(dz\)

$$
dz = dx + i\,dy
$$

So:

$$
f(z)\,dz = (u + iv)(dx + i\,dy)
$$

Multiply:

$$
= (u\,dx - v\,dy) + i(v\,dx + u\,dy)
$$

---

## 7. Apply Green’s Theorem

Split into real and imaginary parts:

### Real part:
$$
\oint_C (u\,dx - v\,dy)
$$

### Imaginary part:
$$
\oint_C (v\,dx + u\,dy)
$$

Apply Green’s theorem to each.

---

## 8. Use Cauchy-Riemann Equations

If \(f(z)\) is analytic:

$$
\frac{\partial u}{\partial x} = \frac{\partial v}{\partial y}, \quad
\frac{\partial u}{\partial y} = -\frac{\partial v}{\partial x}
$$

---

### Compute the curl terms

#### Real part:
$$
\frac{\partial (-v)}{\partial x} - \frac{\partial u}{\partial y}
= -\frac{\partial v}{\partial x} - \frac{\partial u}{\partial y} = 0
$$

#### Imaginary part:
$$
\frac{\partial u}{\partial x} - \frac{\partial v}{\partial y} = 0
$$

---

## 9. Conclusion: Cauchy’s Integral Theorem

Since both parts vanish:

$$
\oint_C f(z)\,dz = 0
$$

---

## 10. Final Insight

- Green’s theorem: **real-variable circulation = area integral of curl**  
- Cauchy’s theorem: **analytic functions have zero “complex curl”**  

👉 Therefore:
> No net accumulation → integral around closed loop is zero

---

## 11. Big Picture

| Concept | Meaning |
|--------|--------|
| Green’s Theorem | Boundary ↔ interior relationship |
| Curl | Local rotation |
| Analytic function | Zero rotation (in complex sense) |
| Cauchy’s Theorem | No circulation → integral = 0 |

---

## 12. Key Takeaway

> Cauchy’s Integral Theorem is essentially **Green’s Theorem applied to complex functions satisfying the Cauchy–Riemann equations**.

---