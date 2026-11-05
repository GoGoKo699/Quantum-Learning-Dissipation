# Related work and attribution

[Home](../README.md) · [Scientific results](../science/results.md) · [Bibliography](references.bib)

The comparison concerns sequential processing of identical unknown pure qubits, expected net work, and a controller that is returned after all records are charged. The contribution is the matching squared-logarithmic classical work deficit, its comparison with the logarithmic coherent benchmark, and an explicit qubit learner with logarithmic expected probe regret. It is not the first connection between learning and work, the first quantum-memory advantage, or a new Haar-posterior identity.

## Adaptive work extraction

Josep Lumbreras, Ruo Cheng Huang, Yanglin Hu, Mile Gu, and Marco Tomamichel, **Quantum state-agnostic work extraction (almost) without dissipation**, [arXiv:2505.09456v1](https://arxiv.org/abs/2505.09456v1), 14 May 2025. The [full text](https://arxiv.org/html/2505.09456v1) defines sequential unknown-qubit extraction with a semiclassical weight, uses adaptive exploration and exploitation, and proves a polylogarithmic dissipation upper bound. Equation (15) gives a high-probability bound of order beta-inverse times ln-squared N times ln(N/delta). Appendix D explicitly discusses measurement and memory-erasure costs; it would be incorrect to describe that work as ignoring all record erasure.

The revised preprint **Learning to extract work optimally from unknown quantum states with exponentially reduced dissipation**, [Research Square, version 1](https://doi.org/10.21203/rs.3.rs-9431975/v1), posted 11 May 2026, retains this scaling in equation (3). Its battery model and high-probability statement must not be silently identified with an unrestricted ideal-average-work theorem.

The present [converse](../science/classical_lower.md) instead covers arbitrary classical causal controllers under the stated entropy/work account. The [upper construction](../science/work_cycle.md) supplies its own measurement-feedback-reset cycle and attains the matching expected order. The learning-to-work connection and the usefulness of near-aligned probes are inherited; the exact centered estimator and the resulting matched causal cost are the added steps. No improvement of the prior paper's high-probability guarantee is claimed.

## Low-disturbance pure-state learning

Josep Lumbreras, Mikhail Terekhov, and Marco Tomamichel, **Learning pure quantum states almost without regret**, *npj Quantum Information* (26 June 2026), [DOI](https://doi.org/10.1038/s41534-026-01305-z). In the inspected accepted manuscript, Theorem 11, equations (111)–(112), gives expected regret bounded by a logarithmic term plus a squared-logarithmic term and expected online infidelity bounded by a constant times ln(t)/t. The published abstract explicitly identifies the remaining logarithmic gap. Their higher-dimensional result is broader than the qubit setting here.

The [learner](../science/learner.md) uses four tangent directions, a centered unbiased inverse-design update, and a closed conditional-variance identity. It gives expected estimation infidelity at most 21/t and cumulative expected probe regret at most 76 + 38 ln N, uniformly over fixed pure qubit states. This closes the expected-regret order gap for that qubit task against the inspected theorem. It does not supply the earlier work's general-dimensional or simultaneous high-probability conclusions. The logarithmic regret lower bound and the use of adaptive nearly aligned measurements are not new here.

Related foundations include Lumbreras and Tomamichel, **Linear bandits with polylogarithmic minimax regret**, [COLT 2024, PMLR 247, 3644–3682](https://proceedings.mlr.press/v247/lumbreras24a.html), and their later **Learning Pure Quantum States in Any Dimension (Almost) Without Regret**, [arXiv:2605.09019v1](https://arxiv.org/abs/2605.09019v1). These establish relevant vanishing-variance and adaptive-probe methods. The comparison is about the actual expected-risk bounds, not proof length or a change of terminology.

## Haar posterior and the classical converse

Masahito Hayashi, Ayanava Dasgupta, and Naqueeb Ahmad Warsi, **Haar-Bayesian Pure-State Prediction under Relative-Entropy Loss: Arbitrary-Effect Reduction and Global Optimality**, [arXiv:2609.10072v1](https://arxiv.org/abs/2609.10072v1), 9 September 2026. This work supplies the arbitrary-effect posterior formula and its outcome-wise entropy lower bound. Both are inherited ingredients. The [classical proof](../science/classical_lower.md) reproduces the qubit derivation and then applies it at every causal cut, using a controller-entropy telescope to obtain the total work deficit.

The primary abstract and the earlier attributed derivation in Quantum-Learning-Under-Drift support this comparison. The mathematical statement used here is proved in full in the repository; the current source review does not claim a new line-by-line audit of the entire posterior paper.

## Coherent erasure and symmetric compression

Haimeng Zhao, Yuzhen Zhang, and John Preskill, **Learning to erase quantum states: thermodynamic implications of quantum learning theory**, *npj Quantum Information* (27 May 2026), [DOI](https://doi.org/10.1038/s41534-026-01273-4). Equation (6) of the inspected accepted manuscript gives the Haar erasure cost through the symmetric-subspace dimension. For qubits that cost is k_B T ln(N+1). Their reversible-learning framework is a direct thermodynamic antecedent.

The entropy benchmark and symmetric-state compression are credited rather than presented as discoveries. The [coherent account](../science/coherent.md) writes an explicit streaming isometry and final reset to show that the benchmark is attainable under the same specimen-release chronology as the classical theorem. The new comparison is between those matched causal models. It is not a claim that coherent processing first makes universal work extraction possible.

## Thermodynamic and educational foundations

David Reeb and Michael M. Wolf, **An improved Landauer principle with finite-size corrections**, *New Journal of Physics* **16**, 103011 (2014), [DOI](https://doi.org/10.1088/1367-2630/16/10/103011), [arXiv:1306.4352](https://arxiv.org/abs/1306.4352). The Gibbs entropy identity underlying the round-by-round bound is inherited. Ideal reversible erasure and pure-state expansion are limiting constructions; finite baths have additional restrictions.

John Watrous, **The Theory of Quantum Information**, Cambridge University Press (2018), [DOI](https://doi.org/10.1017/9781316848142), [author's source page](https://cs.uwaterloo.ca/~watrous/TQI/). This is the single educational anchor. Channels and instruments, entropy and data processing, and symmetric-subspace/Haar tools support the proofs. The thermodynamic model and centered adaptive update are additional project material, not claims attributed to the textbook. The book is linked, not redistributed.

## Internal antecedents and the surviving contribution

[Quantum-Learning-Under-Drift](https://github.com/GoGoKo699/Quantum-Learning-Under-Drift/tree/5abbebb11139e955488a62a8ba1c5b9d392f4f98), especially `science/haar_posterior.md`, already uses classical histories as effects and the same inherited posterior for prediction. Its task is per-arrival classification under a changing hidden source, with no complete thermal work cycle. The present project adds neither that posterior nor a general classical-versus-quantum distinction; it adds a different causal work law and the explicit expected-risk learner needed to attain it.

[Quantum-Precision-Heat-Tradeoff](https://github.com/GoGoKo699/Quantum-Precision-Heat-Tradeoff/tree/e5abf69e000e75d90aef97428f414d4cdf265809), especially `science/model.md`, studies a single-use conditional-output heat problem with returned workspace. Its source, output task, and heat objective differ from the repeated unknown-state work account here. The shared Gibbs entropy identity does not imply the present learning construction. [Measurement-Free-Memory-Cost](https://github.com/GoGoKo699/Measurement-Free-Memory-Cost) concerns noisy storage and processing rather than this ideal boundary-work task.

## Coverage and limits

This is a targeted primary-source and model-level comparison, checked in November 2026, not an exhaustive priority certificate. Relevant accepted-manuscript statements, the work-extraction full text, and the explicitly identified internal derivations were inspected. General-dimensional learning, finite-power engines, arbitrary source drift, and microscopic entropy-bearing batteries are not silently included in the claimed improvement. Correctness of the self-contained proofs and external novelty are separate judgments.
