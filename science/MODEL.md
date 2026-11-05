# Source, causal controllers, and the work account

[Science](README.md) · [Results](results.md) · [Classical converse](classical_lower.md)

## Source and performance criterion

A source emits one qubit at each round, always in the same unknown pure state

```math
P_{\boldsymbol n}=\frac{I+\boldsymbol n\cdot\boldsymbol\sigma}{2},
\qquad \boldsymbol n\in\mathbb S^2.
```

Conditioned on the fixed direction, the input is its tensor power. The controller receives neither the direction nor a state-preparation oracle. It must finish accessing specimen t before specimen t+1 arrives. Discarded specimens and spent reservoir components cannot be accessed again.

Every specimen has zero Hamiltonian at its arrival and departure. The reservoir temperature is positive. Natural logarithms and entropy in nats are used throughout. Set beta equal to the inverse of k_B T. For a protocol pi, define the dimensionless expected work deficit

```math
\mathcal D_N(\pi,\boldsymbol n)
=N\ln2-\beta\,\mathbb E_{\boldsymbol n}W_{\rm net}(\pi).
```

The expectation includes measurement results and internal randomness. Net work includes restoration of every controller register. The reference N k_B T ln 2 is the ideal mean work obtainable from N known pure qubits. The deficit is a difference from that reference; it is not, by definition, the total heat emitted or the total entropy production of a run.

We study both the Haar-average optimum and the minimax optimum:

```math
D_{\rm C}^{\rm av}(N)=\inf_\pi\int\mathcal D_N(\pi,\boldsymbol n)\,d\boldsymbol n,
\qquad
D_{\rm C}^{\rm max}(N)=\inf_\pi\sup_{\boldsymbol n}\mathcal D_N(\pi,\boldsymbol n).
```

The prior is used in the converse, not supplied to the upper construction as knowledge of the true state. The classical construction has a bound for every fixed pure state.

## What can persist?

At the boundary between rounds, a classical controller has only a register diagonal in a fixed, known classical basis. Its dimension, computation, adaptive instruments within a round, and classical history length are unrestricted. Every register that retains input-dependent information, including work-readout records, is part of this controller. Ancillas can be used inside a round, but they must be returned or included in the charged output memory. There is no surviving quantum side channel in a reservoir, actuator, preparation device, or battery.

A coherent controller is subject to the same chronological access and thermodynamic account, but can retain a quantum register. The construction uses at most ceil(log_2(N+1)) persistent qubits. This is a sufficient size, not a converse on the smallest coherent memory attaining the optimum. Temporary implementation resources are not asserted to have optimal gate costs.

The controller begins independently of the source and ends in its initial state, with no accessible input-dependent record remaining. A pure register is a borrowed resource whose final reset is charged. Initially mixed random seeds are also returned; a swap with a fresh maximally mixed reservoir register can remove their final correlations at zero work in the degenerate model. Unlimited classical memory means an arbitrarily large finite register for each implementation, followed by ideal limits; no differential entropy of an infinitely precise classical record is used.

## Thermodynamic convention

We use ideal average work under externally driven Hamiltonians, with fresh Gibbs reservoir components, reversible computation, and arbitrary controlled operations. All working-register Hamiltonians return to zero at the round boundaries. Positive W means work delivered by the device. Pure-state expansion and erasure at the entropy limit are quasistatic infima/suprema, approached with increasing reservoir, gap, precision, or time resources. Exact saturation by a finite full-rank reservoir is not claimed.

This convention does not identify an arbitrary microscopic battery's raw mean energy increase with useful work. A battery may not be an uncharged entropy sink or a retained quantum memory. A microscopic implementation with entropy-bearing work storage requires its own free-energy and correlation account. No finite-power, finite-gap, deterministic-work, or hardware-efficiency claim follows from the results here.

For an accessible working register A and an initially independent Gibbs bath B, the usual entropy balance gives

```math
\beta\,\mathbb E W_{\rm out}
=S(A')-S(A)-I(A':B')-D(\rho'_B\Vert\gamma_B)
\le S(A')-S(A).
```

This is the standard Gibbs identity and subadditivity, not a new thermodynamic principle. It applies to each round's entire accessible register, not to a specimen while silently ignoring the controller. The model does not allow reuse of a spent bath carrying information about the source. See [the work cycle](work_cycle.md) for an explicit upper construction with all outcome records erased, and [the related-work account](../references/PRIORITY.md) for attribution.
