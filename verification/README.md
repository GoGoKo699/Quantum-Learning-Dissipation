# Reproducing the finite checks

[Home](../README.md) · [Theorems](../science/results.md) · [Check map](PLAN.md)

The analytical proofs establish the universal bounds. The code checks their algebra and finite constructions and provides a seeded simulation of the learner. It does not optimize over all controllers or establish a priority claim.

## Commands

With Python 3.10 or later:

```bash
python -m pip install -r verification/requirements.txt
python verification/check_science.py
python verification/check_science.py --simulate --output /tmp/qld-results.json
```

The first command after installation performs deterministic seeded finite tests. The second also simulates 3000 trajectories to 4096 specimens. It includes exact coordinate poles and otherwise draws fixed pure-state directions from Haar measure. It retains every trajectory; there is no postselection.

## What is checked

The conditional-moment test sums the four tangent choices and both binary outcomes exactly in floating-point arithmetic for 640 direction/time cases. It compares the resulting mean and variance against the formulas in [the learner proof](../science/learner.md). It tests the induction inequality for rounds 65 through 19999 and the entropy-sum identity at several horizons.

The coherent checks build the orthonormal input vectors for rounds 1 through 18, compare their explicit binomial amplitudes with the input tensor product, and independently integrate the compressed density matrix over a sphere quadrature for horizons 1 through 14. They do not materialize an optimal primitive-gate compiler.

The recorded run has maximum mean-identity error below 2e-14, relative variance error below 9e-15, isometry error below 5e-16, compression-vector error below 4e-16, and Haar-average error below 4e-15. The exact tolerances are in the script; small floating-point differences across platforms are expected.

At horizon 4096, the seeded simulation gives mean reset cross-entropy approximately 308.83 nats and expected-regret diagnostic approximately 52.07. The standard error reported by the script describes its Monte Carlo mean; it is not a theorem about every input or a confidence statement for the optimal work deficit. The rigorous explicit upper bound at that horizon is approximately 600.63 nats, and the lower bound is approximately 42.05 nats. All are dimensionless deficits; multiply by k_B T for energy.

## Evidence boundaries

A passing script checks the implemented formulas and stated finite ranges. The arbitrary-controller converse, all-horizon induction, ideal erasure limit, and information-theoretic compression claims are established in the written proofs. These checks are not independent expert review, hardware validation, a finite-power estimate, or a certificate of hosted GitHub mathematical rendering. A source change that affects a formula requires rerunning its affected tests.
