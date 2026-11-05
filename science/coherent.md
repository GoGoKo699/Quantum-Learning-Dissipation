# Streaming coherent compression and the exact entropy benchmark

[Model](MODEL.md) · [Results](results.md) · [Sources](../references/PRIORITY.md)

## The global lower bound is inherited

For Haar-distributed pure qubits,

```math
\int P^{\otimes N}\,dP=\frac{\Pi_N}{N+1},
\qquad S\!\left(\frac{\Pi_N}{N+1}\right)=\ln(N+1).
```

Even an unrestricted collective controller that returns its ancillas cannot extract more than k_B T times [N ln 2 - ln(N+1)] from this ensemble. Apply the Gibbs entropy bound to all specimens and returned registers together; the outgoing N-qubit entropy is at most N ln 2. This gives the Haar-average deficit lower bound ln(N+1), and therefore the same minimax lower bound.

The symmetric-subspace formula and its use as a Haar erasure/work benchmark are established results. In particular, Zhao, Zhang, and Preskill give the general-dimensional Haar erasure cost. The issue here is not rediscovering that entropy, but attaining it while releasing each specimen before the next arrives.

## A causal compressor

Reserve a register M of dimension at least N+1, initially |0>. For a pure qubit |psi> = alpha|0> + beta|1>, define

```math
|C_t(\psi)\rangle
=\sum_{k=0}^t\sqrt{\binom tk}\,\alpha^{t-k}\beta^k|k\rangle_M.
```

Suppose that after t-1 arrivals M holds C_(t-1). In M tensor S_t, the following t+1 states are orthonormal:

```math
|v_{t,k}\rangle
=\sqrt{\frac{t-k}{t}}|k\rangle_M|0\rangle_{S_t}
+\sqrt{\frac{k}{t}}|k-1\rangle_M|1\rangle_{S_t},
\qquad 0\le k\le t,
```

where a term with zero coefficient is omitted. Their orthonormality follows from their disjoint computational supports and unit norms. The actual input has the expansion

```math
|C_{t-1}(\psi)\rangle|\psi\rangle
=\sum_{k=0}^t\sqrt{\binom tk}\,\alpha^{t-k}\beta^k|v_{t,k}\rangle.
```

Choose a known unitary U_t sending every v_(t,k) to |k>_M|0>_S. An isometry between these equal-dimensional orthonormal sets extends to a unitary on the whole fixed register. It is independent of alpha and beta. It produces

```math
U_t\bigl(|C_{t-1}(\psi)\rangle|\psi\rangle\bigr)
=|C_t(\psi)\rangle|0\rangle.
```

The just-processed specimen is now pure and independent of M. Expand it isothermally to I/2, extracting k_B T ln 2, and discard it. Only M persists. This induction gives a genuinely sequential protocol, rather than a collective operation postponed until all samples have arrived.

## Pay for the memory at the end

The Haar average of C_N is the maximally mixed state on its N+1-dimensional active subspace. This follows either from the compression isometry and the Haar moment identity or from direct integration of the binomial amplitudes. Thus the optimal ensemble reset costs k_B T ln(N+1).

To make the construction uniform over each fixed unknown input, first depolarize M within its known active subspace at zero Hamiltonian, using a fresh thermal randomizer that is then discarded. The resulting state is exactly I/(N+1) on that subspace for every input. For the Haar average this operation changes nothing; for a particular pure state it discards unused information at zero energy exchange. Reset this known mixed state quasistatically to the original |0>. The same reset cost therefore applies to every input, and M is returned pure and decoupled.

The net deficit is ln(N+1), matching both the Bayes and minimax lower bounds. A qubit realization needs ceil(log_2(N+1)) persistent qubits, with unused basis states kept empty. No quantum register other than M carries input information through a causal cut. Fresh bath resources and the final erasure are not omitted.

The compressor is a standard symmetric-state/Schur-compression mechanism made explicit for this chronological task. Its information-theoretic memory bound does not include a claimed optimal gate synthesis, geometric locality, protected storage, or finite-power implementation.
