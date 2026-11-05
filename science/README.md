# The scientific argument

[Home](../README.md) · [Results](results.md) · [Learning route](../learning/WATROUS_BRIDGE.md)

A stream of identical pure qubits contains two different resources: local purity and correlations that arise because all specimens share the same unknown state. A coherent register can retain those correlations without converting them into observations. A classical controller must instead infer a useful direction from outcomes before the next specimen arrives.

The [model](MODEL.md) defines the causal boundary and counts the final reset of every retained record. The [classical converse](classical_lower.md) combines an inherited Haar-posterior identity with a round-by-round entropy balance. It gives a sum of binary entropies of order squared logarithm, even for arbitrary adaptive instruments and unlimited classical memory.

The matching construction has two separate parts. The [adaptive learner](learner.md) uses a centered, unbiased Bloch-vector estimator and a small randomized tilt of each measurement. It has expected estimation error of order 1/t and expected probe regret of logarithmic order. The [work cycle](work_cycle.md) converts those outcomes into work, then pays for every record through an explicit, state-independent erasure schedule. No conversion of an infidelity bound into thermodynamic work is assumed without this step.

The [coherent construction](coherent.md) compresses the symmetric state after every arrival, leaving the just-processed specimen pure. The final memory reset costs ln(N+1) in units of k_B T, matching the global entropy lower bound. The symmetric-subspace entropy and its thermodynamic interpretation are inherited; the construction makes their compatibility with the same causal boundary explicit.

The [results page](results.md) collects exact finite bounds, quantifiers, an example, and limitations. [Related work](../references/PRIORITY.md) separates the new construction and causal comparison from the prior learning, prediction, and thermodynamic ingredients. [Verification](../verification/README.md) distinguishes analytical proofs from finite algebraic checks and Monte Carlo diagnostics.
