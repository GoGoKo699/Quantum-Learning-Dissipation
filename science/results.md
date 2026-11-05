# Work deficits and learning bounds

[Science](README.md) · [Model](MODEL.md) · [Verification](../verification/README.md)

Write h(p) = -p ln p - (1-p) ln(1-p), with the continuous endpoint convention. Define

```math
B_N=\sum_{t=1}^N h\!\left(\frac1{t+1}\right),
\qquad
U_N=\sum_{t=1}^N h\!\left(\min\left\{\frac12,\frac{38}{t}\right\}\right).
```

## Classical controller

Under the [model](MODEL.md), for every positive integer N,

```math
B_N\le D_{\rm C}^{\rm av}(N)
\le D_{\rm C}^{\rm max}(N)\le U_N.
```

The lower bound allows arbitrary adaptive instruments and unrestricted classical storage. The upper bound is achieved as an ideal mean-work limit by one explicit sequential projective-measurement protocol, uniformly over the unknown pure state. All its classical records and random seeds are restored or charged.

The lower sum has the exact identity

```math
B_N=\ln(N+1)+\sum_{t=1}^N\frac{\ln t}{t+1}
=\frac12(\ln N)^2+\ln N+O(1).
```

The upper sum satisfies

```math
U_N=19(\ln N)^2+O(\ln N).
```

Consequently both classical optima have order (ln N)^2. These are matching orders, not matching leading constants. The proofs are [the entropy converse](classical_lower.md), [the learner](learner.md), and [the charged work cycle](work_cycle.md).

## Coherent controller

With the same access chronology and return conditions, a persistent register of ceil(log_2(N+1)) qubits suffices for

```math
D_{\rm Q}^{\rm av}(N)=D_{\rm Q}^{\rm max}(N)=\ln(N+1).
```

These equalities describe ideal thermodynamic optima. The lower bound holds even with unrestricted coherent memory; the construction supplies the stated sufficient memory size. The [proof](coherent.md) uses streaming symmetric-subspace compression and charges its final erasure. The Haar entropy benchmark is an established ingredient, not a new discovery.

## Learning statement used by the construction

For every fixed unit Bloch vector n, the learner produces an unconstrained estimate v_t and a pure-state direction w_(t+1) with

```math
\mathbb E_{\boldsymbol n}\|\boldsymbol v_t-\boldsymbol n\|^2\le\frac{21}{t},
\qquad
\mathbb E_{\boldsymbol n}\frac{1-\boldsymbol n\cdot\boldsymbol w_{t+1}}2\le\frac{21}{t}.
```

Its actual probe direction a_t obeys expected infidelity at most 38/t for t at least 77. Thus its cumulative expected probe regret is at most 76 + 38 ln N. The Haar-posterior argument also gives a lower bound H_(N+1)-1 for every causal probe-selection strategy, so the optimal expected qubit probe regret has logarithmic order. The usual expected post-measurement infidelity is at most twice this probe regret. No matching lower bound for every alternative definition of disturbance is asserted.

These are expected-risk bounds, uniform over fixed states. They do not supply a simultaneous high-probability confidence band or a higher-dimensional pure-state result.

## Finite example and interpretation

For N = 4096, the explicit classical lower and upper bounds are approximately 42.05257 and 600.62700 nats, while the coherent optimum is 8.31801 nats. Multiplication by k_B T converts these deficits to energy. The upper constant is conservative; it is not a measured optimal classical cost. A seeded 3000-trajectory numerical check of the explicit learner gives a mean cross-entropy reset cost near 308.83 nats at this horizon; it is a diagnostic of this construction, not a proof or an optimization over all controllers.

The mechanism is not simply that estimating a state consumes energy. A classical record can improve later operations, but the uncertainty remaining at each causal boundary still limits the work obtainable in that round. Coherent storage preserves the common unknown state in one growing symmetric register, paying its entropy only once at the end.

## Scope

The exact source is a fixed pure qubit. The proof does not establish robustness to fixed mixedness, source drift, or noise in the persistent memory. It does not optimize the leading classical constant, the smallest sufficient coherent memory, computational complexity, finite-time power, or a microscopic work-storage implementation. [Finite-horizon control approximation](work_cycle.md#finite-precision-and-ideal-limits) is an existence statement with no efficient lookup-table claim. The literature comparison is a scoped primary-source comparison, not an exhaustive priority certificate or independent expert verification.
