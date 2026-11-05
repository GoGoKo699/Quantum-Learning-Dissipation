# Related work and attribution

[Home](../README.md) · [Scientific results](../science/results.md) · [Bibliography](references.bib)

The comparison concerns sequential processing of identical unknown pure qubits, expected net work, and a controller that is returned after all records are charged. The contribution is the matching squared-logarithmic classical work deficit, its comparison with the logarithmic coherent benchmark, and an explicit qubit learner with logarithmic expected probe regret. It is not the first connection between learning and work, the first quantum-memory advantage, a new causal free-energy framework, or a new Haar-posterior identity.

## Adaptive work extraction

Josep Lumbreras, Ruo Cheng Huang, Yanglin Hu, Mile Gu, and Marco Tomamichel, **Quantum state-agnostic work extraction (almost) without dissipation**, [arXiv:2505.09456v1](https://arxiv.org/abs/2505.09456v1), 14 May 2025. The [full text](https://arxiv.org/html/2505.09456v1) defines sequential unknown-qubit extraction with a semiclassical weight, uses adaptive exploration and exploitation, and proves a polylogarithmic dissipation upper bound. Equation (15) gives a high-probability bound of order beta-inverse times ln-squared N times ln(N/delta). Appendix D explicitly discusses measurement and memory-erasure costs; it would be incorrect to describe that work as ignoring all record erasure.

The revised preprint **Learning to extract work optimally from unknown quantum states with exponentially reduced dissipation**, [Research Square, version 1](https://doi.org/10.21203/rs.3.rs-9431975/v1), posted 11 May 2026, retains this scaling in equation (3). Its battery model and high-probability statement must not be silently identified with an unrestricted ideal-average-work theorem.

The present [converse](../science/classical_lower.md) covers arbitrary classical causal controllers under the stated entropy/work account. The [upper construction](../science/work_cycle.md) supplies its own measurement-feedback-reset cycle and attains the matching expected order. The learning-to-work connection and nearly aligned probes are inherited; the centered estimator and matched causal cost are the added steps. No improvement of the prior high-probability guarantee is claimed.

## Low-disturbance pure-state learning

Josep Lumbreras, Mikhail Terekhov, and Marco Tomamichel, **Learning pure quantum states almost without regret**, *npj Quantum Information* (26 June 2026), [DOI](https://doi.org/10.1038/s41534-026-01305-z). In the inspected accepted manuscript, Theorem 11, equations (111)–(112), gives an expected-regret bound containing logarithmic and squared-logarithmic terms and expected online infidelity bounded by a constant times ln(T)/t, where T is the chosen total measurement horizon. Their higher-dimensional scope is broader than the qubit theorem here.

The [learner](../science/learner.md) uses four tangent directions, a centered unbiased inverse-design update, and a closed conditional-variance identity. It gives expected estimation infidelity at most 21/t and cumulative expected probe regret at most 76 + 38 ln N, uniformly over fixed pure qubit states. This closes the expected-regret order gap for the qubit task against the inspected theorem, without establishing a corresponding high-probability or higher-dimensional result. The logarithmic regret lower bound is inherited.

Related foundations include Lumbreras and Tomamichel, **Linear bandits with polylogarithmic minimax regret**, [COLT 2024, PMLR 247, 3644–3682](https://proceedings.mlr.press/v247/lumbreras24a.html), and **Learning Pure Quantum States in Any Dimension (Almost) Without Regret**, [arXiv:2605.09019v1](https://arxiv.org/abs/2605.09019v1). Vanishing observation variance and adaptive exploration are established mechanisms. The comparison concerns the actual expected-risk bounds, not proof length or a change of terminology.

## Haar posterior and the classical converse

Masahito Hayashi, Ayanava Dasgupta, and Naqueeb Ahmad Warsi, **Haar-Bayesian Pure-State Prediction under Relative-Entropy Loss: Arbitrary-Effect Reduction and Global Optimality**, [arXiv:2609.10072v1](https://arxiv.org/abs/2609.10072v1), 9 September 2026. The arbitrary-effect posterior formula and its outcome-wise entropy bound are inherited ingredients. The [classical proof](../science/classical_lower.md) reproduces the qubit derivation and applies it at each causal cut, with a controller-entropy telescope.

The primary abstract and the attributed derivation in Quantum-Learning-Under-Drift support this comparison. The exact mathematical statement used here is proved in full locally; the source review does not claim a new line-by-line audit of the entire posterior paper.

## Coherent erasure and symmetric compression

Haimeng Zhao, Yuzhen Zhang, and John Preskill, **Learning to erase quantum states: thermodynamic implications of quantum learning theory**, *npj Quantum Information* (27 May 2026), [DOI](https://doi.org/10.1038/s41534-026-01273-4). Equation (6) of the inspected accepted manuscript gives the Haar erasure cost through the symmetric-subspace dimension. For qubits this is k_B T ln(N+1). Reversible learning is a direct thermodynamic antecedent.

The entropy benchmark and symmetric-state compression are credited rather than presented as discoveries. The [coherent account](../science/coherent.md) supplies an explicit streaming isometry and final reset, attaining the benchmark under the same specimen-release chronology as the classical theorem. The added comparison is between those matched causal models, not the first possibility of universal coherent work extraction.

## Other causal thermodynamic frameworks

Ruo Cheng Huang, Isha Singh Le Xue, Yuxuan Qu, Paul M. Riechers, Varun Narasimhachar, and Mile Gu, **Time-ordered free energy in correlated quantum systems: An agentic approach**, [arXiv:2608.12942](https://arxiv.org/abs/2608.12942), is a direct framework antecedent. Theorem 2 and Supplement I express causal dissipation through accumulated conditional outcome entropies and a final predictive entropy, relative to global entropy. Thus neither causal entropy accounting nor the classical-versus-coherent distinction is new here.

The reviewed model uses known hidden-Markov source descriptions and tailored-state extraction actions. Supplement J treats reversible internal-memory updates using retained battery records. That account is not automatically the present requirement to return or charge every accessible source-dependent record, including work records. It should not be described as simply ignoring memory costs.

The consequential remainder is the fixed-unknown-pure-qubit evaluation: the arbitrary-instrument converse, the explicit uniform expected-risk learner, and the resulting matched squared-logarithmic loss. The earlier functional does not itself provide this estimator or evaluate that asymptotic optimum. The source comparison inspected the main model and theorem statements and Supplements I–J; it is not a full independent proof audit.

Huang's thesis, **A Demon that remembers: An agential approach towards quantum thermodynamics of temporal correlations**, [arXiv:2604.04462](https://arxiv.org/abs/2604.04462), is another framework antecedent, discussing unknown-source learning and polylogarithmic dissipation. Its abstract and available introductory material were read; the entire learning chapter was not independently audited. The specific work-extraction and learning theorems above remain the quantitative comparators.

## Thermodynamic and educational foundations

David Reeb and Michael M. Wolf, **An improved Landauer principle with finite-size corrections**, *New Journal of Physics* **16**, 103011 (2014), [DOI](https://doi.org/10.1088/1367-2630/16/10/103011), [arXiv:1306.4352](https://arxiv.org/abs/1306.4352). The Gibbs entropy identity is inherited. Reversible erasure and pure-state expansion are limiting constructions; finite baths impose additional restrictions.

John Watrous, **The Theory of Quantum Information**, Cambridge University Press (2018), [DOI](https://doi.org/10.1017/9781316848142), [author's source page](https://cs.uwaterloo.ca/~watrous/TQI/). This is the single educational anchor. The channel, instrument, entropy, and symmetric-subspace foundations support the proofs. The thermodynamic model and adaptive estimator are project material, not textbook claims. The book is linked, not redistributed.

## Internal antecedents and the surviving contribution

[Quantum-Learning-Under-Drift](https://github.com/GoGoKo699/Quantum-Learning-Under-Drift/tree/5abbebb11139e955488a62a8ba1c5b9d392f4f98), especially `science/haar_posterior.md`, already uses classical histories as effects and the inherited posterior for prediction. Its task is per-arrival classification under a changing hidden source, without a complete thermal work cycle. The present project does not add that posterior; it adds the causal work law and expected-risk learner needed to attain it.

[Quantum-Precision-Heat-Tradeoff](https://github.com/GoGoKo699/Quantum-Precision-Heat-Tradeoff/tree/e5abf69e000e75d90aef97428f414d4cdf265809), especially `science/model.md`, treats single-use conditional-output heat with returned workspace. Its source, output task, and heat objective differ from repeated unknown-state work extraction. The common Gibbs identity does not imply the new learning construction. [Measurement-Free-Memory-Cost](https://github.com/GoGoKo699/Measurement-Free-Memory-Cost) concerns noisy storage and processing, not this ideal boundary-work task.

## Coverage and limits

This is a scoped primary-source and model-level comparison from November 2026, not an exhaustive priority certificate. The accepted learning manuscript's qubit theorem, work-extraction text, relevant causal-framework sections, and identified internal derivations were inspected to the extents stated above. No finite-power engine, arbitrary drift model, noisy persistent memory, general-dimensional matching result, or microscopic entropy-bearing battery implementation is silently included. Self-contained proof correctness, external novelty, and journal significance remain separate judgments.
