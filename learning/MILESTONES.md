# Thirty milestones for causal learning and work

[Home](../README.md) · [Watrous bridge](WATROUS_BRIDGE.md) · [Science](../science/README.md)

The map has 12 foundation milestones and 18 project milestones. Each is a learner-independent understanding target, not a claim of personal mastery. Watrous (2018) is the single educational anchor; the thermodynamic and research dependencies remain explicitly attributed.

## Foundations

### M01 — Pure qubits and Bloch vectors
**Question:** Which real vectors describe the source? **Target:** Derive P = (I+n dot sigma)/2 and show that purity is equivalent to unit Bloch-vector norm. **Dependencies:** None. **Connection:** Purity later controls the estimator variance, not merely notation. **Sources:** Watrous, Chapter 2; [model](../science/MODEL.md).

### M02 — One specimen, one binary outcome
**Question:** What does a projective probe reveal? **Target:** Derive Pr(b|a) = (1+b n dot a)/2 and distinguish the probe direction from the unknown source direction. **Dependencies:** M01. **Connection:** Every statistical update must use this actual single-copy feedback. **Sources:** Watrous, Chapter 2 measurements; [learner](../science/learner.md#1-protocol).

### M03 — Effects are not instruments
**Question:** What remains after a measurement? **Target:** Separate a POVM effect, outcome probability, and conditional post-measurement state. **Dependencies:** M01–M02. **Connection:** The lower bound needs only effects, while work extraction needs the physical instrument. **Sources:** Watrous, Chapter 2 instruments; [work cycle](../science/work_cycle.md#measurement-feedback-and-extraction).

### M04 — A classical quantum boundary
**Question:** What makes a retained register classical? **Target:** Write a block-diagonal classical-quantum state and identify which coherence would violate the boundary restriction. **Dependencies:** M03. **Connection:** Unlimited classical bits do not reproduce a retained unknown qubit. **Sources:** Watrous, Chapter 2; [persistent resources](../science/MODEL.md#what-can-persist).

### M05 — Include the entire operation
**Question:** Can discarded apparatus contain a hidden resource? **Target:** Represent a channel using a unitary, ancilla, and partial trace; explain why a subsequently reused ancilla is persistent memory. **Dependencies:** M03–M04. **Connection:** The work converse fails if an information-bearing side channel is omitted. **Sources:** Watrous, Chapter 2 channel representations; [model](../science/MODEL.md).

### M06 — Conditional entropy and subadditivity
**Question:** How is the incoming entropy evaluated? **Target:** Derive S(MS) = H(M) + sum_h p_h S(rho_h) for classical M and bound a qubit output entropy by ln 2. **Dependencies:** M04. **Connection:** These two identities provide the input and output sides of every round. **Sources:** Watrous, Chapter 5; [entropy telescope](../science/classical_lower.md#3-the-controller-entropy-must-telescope).

### M07 — From Gibbs entropy to work
**Question:** Under what convention does entropy bound extracted work? **Target:** Derive beta Q = Delta S_B + D(rho'_B || gamma_B), combine it with unitary entropy conservation, and state the required boundary Hamiltonians. **Dependencies:** M05–M06. **Connection:** An information inequality becomes a work bound only after the resource account is fixed. **Sources:** Watrous, Chapter 5 for entropy tools; Reeb–Wolf in [related work](../references/PRIORITY.md#thermodynamic-and-educational-foundations); [model](../science/MODEL.md#thermodynamic-convention).

### M08 — Haar averaging is not a physical oracle
**Question:** Why introduce a prior in a worst-case problem? **Target:** Compute the one-qubit Haar mean I/2 and explain how an average supplies a minimax lower bound. **Dependencies:** M01. **Connection:** The algorithm is still ignorant of the actual direction. **Sources:** Watrous, Chapter 7 Haar measures; [source criterion](../science/MODEL.md#source-and-performance-criterion).

### M09 — The symmetric sector
**Question:** How large is the space occupied by identical copies? **Target:** Construct the Dicke basis, count m+1 dimensions, and obtain integral P^(tensor m) dP = Pi_m/(m+1). **Dependencies:** M01, M08. **Connection:** The same sector controls posterior prediction and coherent compression. **Sources:** Watrous, Chapter 7 symmetric subspaces; [coherent benchmark](../science/coherent.md#the-global-lower-bound-is-inherited).

### M10 — Quantum posterior prediction
**Question:** What state describes the next specimen after a classical outcome? **Target:** Write its normalized Bayesian integral and work through the one-observation diagonal (2/3,1/3) example. **Dependencies:** M03, M08–M09. **Connection:** A likely estimate is not a perfectly known specimen. **Sources:** [Worked example](WATROUS_BRIDGE.md#worked-example-1-one-classical-observation); [posterior proof](../science/classical_lower.md#2-the-inherited-posterior-identity).

### M11 — Conditional moments and adaptive updates
**Question:** Which cross term disappears in a stochastic recurrence? **Target:** Condition on the complete history and show how conditional unbiasedness eliminates the estimation-error cross term. **Dependencies:** M02. **Connection:** Adaptivity does not permit replacing conditional quantities by unjustified independent ones. **Sources:** [Moment calculation](../science/learner.md#2-exact-conditional-moments) and [risk recurrence](../science/learner.md#3-uniform-mean-square-bound); this probability calculation is supplied by the project.

### M12 — Feedback and final erasure
**Question:** Why does measuring and extracting not give free work? **Target:** Follow a specimen through measurement, controlled rotation, expansion, and the later reset of its sign bit. **Dependencies:** M03, M07. **Connection:** The cycle counts a record once, neither omitting nor double-counting it. **Sources:** [Work cycle](../science/work_cycle.md); [prior extraction work](../references/PRIORITY.md#adaptive-work-extraction).

## The classical lower bound

### M13 — Freeze the causal model
**Question:** What can cross a round boundary? **Target:** Identify every retained controller, seed, work record, and forbidden reused bath, and distinguish persistent from temporary quantum resources. **Dependencies:** M04–M07, M12. **Connection:** A separation is meaningful only with matched accounts. **Sources:** [Model](../science/MODEL.md).

### M14 — Bayes, minimax, and expectation
**Question:** Which quantity is optimized? **Target:** Distinguish infimum-average from infimum-supremum and expected work from a high-probability work guarantee. **Dependencies:** M08, M13. **Connection:** The lower and upper bounds meet in the same statistical criterion. **Sources:** [Definitions](../science/MODEL.md#source-and-performance-criterion), [results](../science/results.md).

### M15 — Collapse a classical history to one effect
**Question:** Does adaptive processing escape a tomography bound? **Target:** Construct the effect E_h of a complete history on the first m copies, including coarsening and independent ancillary randomness. **Dependencies:** M03–M05, M09, M13. **Connection:** A collective-measurement relaxation strengthens the opponent without weakening the conclusion. **Sources:** [History reduction](../science/classical_lower.md#1-a-history-is-an-effect-on-the-consumed-copies).

### M16 — Derive the inherited posterior identity
**Question:** Why can no record make the predictive state pure? **Target:** Use the symmetric-projector permutation identity to obtain rho_h = (I+m tau_h)/(m+2), then its outcome-wise entropy lower bound. **Dependencies:** M06, M09–M10, M15. **Connection:** The nonzero smallest eigenvalue is the uncertainty paid at every cut. **Sources:** [Proof and attribution](../science/classical_lower.md#2-the-inherited-posterior-identity); Hayashi–Dasgupta–Warsi in [related work](../references/PRIORITY.md#haar-posterior-and-the-classical-converse).

### M17 — Telescope the controller entropy
**Question:** Where does unlimited classical memory disappear from the lower bound? **Target:** Sum the per-round work inequalities and include the final restoration term, cancelling H(M_t)-H(M_(t-1)). **Dependencies:** M06–M07, M13, M16. **Connection:** Classical storage is unlimited, but entropy capacity is not consumed for free. **Sources:** [Full telescope](../science/classical_lower.md#3-the-controller-entropy-must-telescope).

### M18 — Understand the squared logarithm
**Question:** Why is the deficit larger than a logarithm? **Target:** Prove the telescoping identity for B_N and compare sum ln(t)/t with its integral. **Dependencies:** M16–M17. **Connection:** Entropy of a small residual error contains an extra logarithm beyond infidelity. **Sources:** [Lower-sum analysis](../science/classical_lower.md#4-size-of-the-lower-bound), [results](../science/results.md).

## A learner that attains the order

### M19 — Build a nonsingular tangent frame
**Question:** How can the policy explore every direction without a pole singularity? **Target:** Construct e_1,e_2 using the least-aligned Cartesian axis and verify the mean and covariance of the four tangent choices. **Dependencies:** M01–M02. **Connection:** The construction is uniform over the sphere, not only a neighborhood of a known state. **Sources:** [Protocol](../science/learner.md#1-protocol), `frame` in [the code](../verification/check_science.py).

### M20 — Center the inverse-design estimator
**Question:** Why subtract c from the observed sign? **Target:** Compute the design matrix A and prove E[g|past] = n for g = w+(b-c)A-inverse a. **Dependencies:** M11, M19. **Connection:** The adaptive observation can be globally unbiased without a warm start. **Sources:** [Exact moments](../science/learner.md#2-exact-conditional-moments).

### M21 — Retain the error-dependent variance
**Question:** Does a vanishing tilt make the estimator unusably noisy? **Target:** Derive the exact variance 4+s-squared/c-squared+4c-squared e/s-squared and identify the cancellation at e=0. **Dependencies:** M20. **Connection:** The variance decreases with alignment, allowing inexpensive exploration. **Sources:** [Variance identity](../science/learner.md#2-exact-conditional-moments), [worked example](WATROUS_BRIDGE.md#worked-example-2-why-an-aligned-probe-still-explores).

### M22 — Normalize without losing uniformity
**Question:** What happens when the estimate is zero or points the wrong way? **Target:** Prove the factor-two norm inequality and include the zero-vector convention. **Dependencies:** M19–M21. **Connection:** Bad histories remain in the expectation instead of being discarded. **Sources:** [Normalization bound](../science/learner.md#3-uniform-mean-square-bound).

### M23 — Close the 1/t induction
**Question:** Which tilt schedule absorbs the error-dependent noise? **Target:** Prove the early-round bound with capped tilt, then the t-at-least-65 recurrence and the explicit constant 21. **Dependencies:** M11, M21–M22. **Connection:** This is an all-state expected-risk theorem, not an observed simulation slope. **Sources:** [Induction](../science/learner.md#3-uniform-mean-square-bound), [finite checks](../verification/README.md).

### M24 — Bound the probes, not just the estimates
**Question:** Does an accurate estimate imply low disturbance of the consumed samples? **Target:** Compute the actual probe's minus probability after averaging the tilt and derive the 38/t bound and logarithmic regret. **Dependencies:** M16, M18, M23. **Connection:** Exploration has its own cost and must appear in the work bound. **Sources:** [Probe calculation](../science/learner.md#4-the-probes-themselves-are-inexpensive), [regret converse](../science/classical_lower.md#5-the-separate-probe-regret-consequence).

### M25 — Erase using a known reference distribution
**Question:** Must the engine know the true outcome probability? **Target:** Derive the cross-entropy reset cost for reference p_t and use its linearity in the actual q_t to turn an unconditional expectation bound into a work guarantee. **Dependencies:** M07, M12, M24. **Connection:** No hidden posterior oracle or high-probability event is required. **Sources:** [Reset schedule](../science/work_cycle.md#a-reset-schedule-independent-of-the-unknown-state).

### M26 — Return seeds and arithmetic registers
**Question:** Which apparently auxiliary information is still charged? **Target:** Uncompute arithmetic from the retained history, reset all sign bits, and explain the zero-work fresh-mixed-register swap that removes random-seed correlations. **Dependencies:** M05, M12–M13, M25. **Connection:** The completed device returns its entire controller, not only a selected output bit. **Sources:** [Feedback and return](../science/work_cycle.md#measurement-feedback-and-extraction), [resource model](../science/MODEL.md#what-can-persist).

## Coherent comparison and synthesis

### M27 — Compress before the next arrival
**Question:** Is symmetric compression compatible with the causal deadline? **Target:** Verify the orthonormal v_(t,k) vectors, their binomial-amplitude expansion, and the state-independent unitary mapping to compressed memory plus a pure specimen. **Dependencies:** M05, M09, M13. **Connection:** The construction releases every specimen immediately rather than storing all N qubits. **Sources:** [Causal compressor](../science/coherent.md#a-causal-compressor).

### M28 — Pay the coherent entropy once
**Question:** Why is the final cost ln(N+1), even for a fixed unknown state? **Target:** Derive the Haar-uniform memory, use an input-independent active-subspace depolarization for uniformity, and charge its final pure reset. **Dependencies:** M07–M09, M14, M27. **Connection:** The global entropy benchmark is attainable with the same chronology and return rules. **Sources:** [Coherent optimum](../science/coherent.md), Zhao–Zhang–Preskill in [related work](../references/PRIORITY.md#coherent-erasure-and-symmetric-compression).

### M29 — Separate proof, approximation, and computation
**Question:** What do finite tests actually establish? **Target:** Reproduce the moment and compression checks, derive the finite-transcript coupling error, and distinguish a seeded Monte Carlo average from a universal theorem or efficient compiler. **Dependencies:** M23–M28. **Connection:** Finite precision is admitted through a stated ideal limit, not assumed costless at all scales. **Sources:** [Verification](../verification/README.md), [finite-horizon approximation](../science/work_cycle.md#finite-precision-and-ideal-limits).

### M30 — State the consequence without enlarging it
**Question:** What remains new after crediting all foundations? **Target:** Explain the matched causal work law, its explicit expected-risk construction, the inherited posterior and coherent benchmark, and the unresolved leading-constant, noise, time, and gate costs. **Dependencies:** M14–M29. **Connection:** Scientific significance and rigorous scope must be assessed together. **Sources:** [Results](../science/results.md), [related work](../references/PRIORITY.md), [scientific overview](../science/README.md).
