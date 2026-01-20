The time-dependent Schrödinger equation is a linear partial differential equation:

$$
i \hbar \frac{\partial \Psi(x,t)}{\partial t} = \hat{H} \Psi(x,t),
$$

which will be solved using the method of separation of variables.

First, we solve the time-independent (stationary) Schrödinger equation:

$${\hat {H}} |\Psi \rangle =E|\Psi \rangle, $$

which is equivalent to a Sturm–Liouville eigenvalue problem:

$$ {\frac {-\hbar ^{2}}{2m}}{\frac {d^{2}\psi }{dx^{2}}}+V\psi =E\psi. $$ 

The solution to this problem is a set of infinitely many eigenvalues of the Hamiltonian  $E_n$ and their corresponding eigenfunctions 
$\psi_n$ (stationary states), which form an orthonormal basis of the Hilbert space:

$$\Psi_1(x,t) = \psi_1(x) e^{\frac{-iE_1t}{\hbar}},\quad \Psi_2(x,t) = \psi_2(x) e^{\frac{-iE_2t}{\hbar}},\space ...$$

The complete solution is obtained as a linear combination, i.e., the spectral decomposition (an infinite sum) of the Hamiltonian’s eigenfunctions multiplied by coefficients $c_n$:

$${\displaystyle \Psi (x,t)=\sum _{n=1}^{\infty }c_{n}\psi _{n}e^{\frac {-iE_{n}t}{\hbar }}.}$$

The main solver in this repository is adapted from [this notebook](https://github.com/lukepolson/youtube_channel/blob/main/Python%20Metaphysics%20Series/vid17.ipynb), with modifications for animation and different potentials.

