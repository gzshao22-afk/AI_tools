$\mathcal {L F H Z}$
$\mathscr {L F H Z}$
$\mathbb {R Z Q C}$

[Beginner's Guide on Filter Topology](https://www.analog.com/en/resources/technical-articles/a-beginners-guide-to-filter-topologies.html#:~:text=Using%20low%20pass%20filters%20as,thus%20making%20it%20relatively%20inexpensive)

The Laplace transform $\mathscr L$ is defined as:
$$\mathscr L[f(t)](s)\equiv \int_0^{\infty}f(t)e^{-st}dt$$

For 2nd order Sallen-Key low-pass filter with this circuit:
![400](./assets/Transform%20--%20Laplace%20Transform%20and%20Application/file-20260203153512787.png)

1. Label the Circuit Nodes: 
   + $V_{in}$ is the input;
   + $V_{a}$ is the node between the two resistors R1 and R2;
   + $V_{b}$ is the node at the non-inverting (+) input of the op-amp;
   + $V_{out}$ is the output.

2. Apply Kirchhoff's Current Law (KCL)
   ![500](./assets/Transform%20--%20Laplace%20Transform%20and%20Application/file-20260203154008693.png)

![450](./assets/Transform%20--%20Laplace%20Transform%20and%20Application/file-20260203154043063.png)

![450](./assets/Transform%20--%20Laplace%20Transform%20and%20Application/file-20260203154114874.png)


Laplace Transform:
![400](./assets/Transform%20--%20Laplace%20Transform%20and%20Application/file-20260203154225790.png)

![400](./assets/Transform%20--%20Laplace%20Transform%20and%20Application/file-20260203154247206.png)

![400](./assets/Transform%20--%20Laplace%20Transform%20and%20Application/file-20260203154305155.png)

