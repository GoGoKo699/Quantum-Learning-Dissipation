# From Watrous to causal learning and work

[Home](../README.md) · [30 milestones](MILESTONES.md) · [Scientific overview](../science/README.md)

The single educational anchor is John Watrous, **The Theory of Quantum Information**, Cambridge University Press (2018). Use the [author's source page](https://cs.uwaterloo.ca/~watrous/TQI/) and [published edition](https://doi.org/10.1017/9781316848142). The author-hosted draft is linked for personal study rather than copied into this repository. Chapters are more useful here than reading the book from beginning to end.

## Source-to-project map

| Watrous material | What to extract | Where it is used |
|---|---|---|
| Chapter 2, basic notions; measurements and instruments | A measurement effect gives a probability, while an instrument also specifies the remaining state | [Classical histories](../science/classical_lower.md), [feedback cycle](../science/work_cycle.md) |
| Chapter 2, channels and their representations | A complete operation includes ancillas, records, and discarded systems | [Operational model](../science/MODEL.md) |
| Chapter 5, quantum entropy and source coding | Entropy of a classical-quantum state, subadditivity, and relative entropy | [Controller entropy telescope](../science/classical_lower.md#3-the-controller-entropy-must-telescope) |
| Chapter 7, permutation invariance and unitarily invariant measures; especially symmetric subspaces and Haar averages | The average of identical pure-state copies is a normalized symmetric projector | [Posterior](../science/classical_lower.md#2-the-inherited-posterior-identity), [coherent compression](../science/coherent.md) |

Chapter 7's permutation-operator and Haar-measure sections are the main representation-theory bridge. The project needs the symmetric representation of qubits, not the entire general representation-theory machinery. The entropy convention here is natural logarithms; a book formula in bits must be multiplied by ln 2 before it enters an energy expression.

The textbook does not establish this project's thermodynamic model or adaptive estimator. The Gibbs entropy balance is a separate thermodynamic input, attributed to Reeb and Wolf in [related work](../references/PRIORITY.md). The exact Haar-posterior identity and its entropy bound are attributed to Hayashi, Dasgupta, and Warsi. Conditional expectations and the elementary stochastic-approximation calculation are developed in the project itself.

## Translate the notation

A pure qubit state is P, not its Bloch vector n. The vector is a real unit vector satisfying P = (I+n dot sigma)/2. A density operator can be mixed, whereas the normalized direction w used for a probe represents a pure projector. The unconstrained estimate v in the algorithm is not required to lie in the Bloch ball and is never submitted as a density operator.

A POVM effect E_h is positive and determines the probability of a history. Its normalized one-particle marginal tau_h is a density operator constructed in a proof, not an extra physical memory supplied to the device. Pi_m is a projector with trace m+1 for m qubits; Pi_m/(m+1), not Pi_m alone, is the Haar-averaged density operator.

Entropy S and classical entropy H are dimensionless nats. Work W has energy units. The quantity beta W is dimensionless, and the deficit D is defined by N ln 2 minus beta times net work. An estimation error, an entropy, and an energy are different objects even when one bounds another.

## Worked example 1: one classical observation

Draw a pure qubit uniformly from the Bloch sphere and measure its first specimen in the computational basis. Conditional on observing zero, take the effect E = |0><0|. The inherited posterior formula at m=1 gives

```math
\rho_0=\frac{I+|0\rangle\langle0|}{3}
=\begin{pmatrix}2/3&0\\0&1/3\end{pmatrix}.
```

The next specimen is not known to be |0>. It has this predictive state after averaging the unknown source conditional on the observed record. Its entropy is h(1/3), not zero. Observing one gives the reversed diagonal and the same entropy.

Before any sample, the predictive state is I/2 with entropy ln 2. Thus the two-round classical lower bound is ln 2 + h(1/3), approximately 1.32966 nats. The coherent global benchmark is ln 3, approximately 1.09861 nats. This compares a lower bound with an attainable coherent value; it does not assert that the two-round classical lower bound is attained by the particular upper construction.

The distinction matters thermodynamically: feedback can extract work from the known post-measurement state, but the recorded outcome must still be reset. Treating the record as a mathematical label with no physical cost would erase the mechanism of the theorem.

## Worked example 2: why an aligned probe still explores

Suppose the current estimate w happens to equal the true direction n. The learner nevertheless uses a small tangent tilt. With a = c w + s u and c-squared plus s-squared equal to one, the minus probability is (1-c)/2. This is nonzero: an exactly aligned measurement would reveal no tangent direction.

The centered update subtracts the predicted mean c from the outcome b. Averaging the four tangent choices and the binary outcome gives E g = n. Its variance at exact alignment is

```math
\mathbb E\|\boldsymbol g-\boldsymbol n\|^2=4+\frac{s^2}{c^2}.
```

There is no inverse-squared-tilt divergence in this aligned case. Away from alignment, the additional variance is 4 c-squared times the squared direction error divided by s-squared. The proof chooses the decreasing tilt so that this error-dependent contribution can be absorbed into the 1/t risk induction. This is the reason to study the exact conditional moments before trying a numerical optimizer.

## Worked example 3: returning a compressed memory

For two identical qubits, the symmetric sector has basis |00>, (|01>+|10>)/sqrt(2), |11>. A coherent compressor stores its three amplitudes in a three-dimensional register while releasing a pure specimen at each step. The Haar average of this memory is I/3, so its final ideal erasure costs k_B T ln 3. The memory is not free merely because its state is pure conditional on the unknown source; the controller does not know that conditional pure state.

The [streaming construction](../science/coherent.md) generalizes this observation to a sector of dimension N+1 and explicitly returns the register. The known-state benchmark and the unknown-state benchmark differ because the available classical description differs, not because entropy stops obeying the second law.

## A connected reading route

Use milestones M01–M12 to assemble states, instruments, entropy, Haar averaging, and the work convention. M13–M18 then prove the lower bound. M19–M26 build the learner and its fully charged classical implementation. M27–M30 establish the coherent comparison, reproduce the checks, and separate the contribution from inherited ingredients.

The milestones are shared understanding targets. They contain no personal assessment, answer key, or progress record. Readers already comfortable with channels and entropy can begin directly at [the classical converse](../science/classical_lower.md) and [the learner proof](../science/learner.md).
