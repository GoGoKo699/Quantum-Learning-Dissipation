# Quantum Learning Dissipation

**How much work is lost when a device processes an unknown quantum source one specimen at a time and retains only classical information?**

A source emits identical copies of a fixed unknown pure qubit. Each specimen must leave the device before the next arrives. All records and controller registers are restored at the end. In the ideal average-work model, the optimal deficit relative to knowing the state in advance has squared-logarithmic order for a classical controller. A logarithmic-size coherent register reduces it to an exact logarithmic entropy cost.

## Main result

Let N be the number of specimens, T the bath temperature, and h the binary entropy in natural logarithms. The [classical bounds](science/results.md), for both Haar-average and worst-case expected net work, are

```math
k_{\mathrm B}T\sum_{t=1}^N h\!\left(\frac1{t+1}\right)
\le \Delta W_{\mathrm C}^{\rm opt}(N)
\le k_{\mathrm B}T\sum_{t=1}^N h\!\left(\min\left\{\frac12,\frac{38}{t}\right\}\right).
```

Consequently,

```math
\Delta W_{\mathrm C}^{\rm opt}(N)
=\Theta\!\left(k_{\mathrm B}T(\ln N)^2\right).
```

The [coherent construction](science/coherent.md) uses at most ceil(log_2(N+1)) persistent qubits and attains the corresponding optimum

```math
\Delta W_{\mathrm Q}^{\rm opt}(N)=k_{\mathrm B}T\ln(N+1).
```

The classical constants are not sharp. These are expected-work optima in an ideal quasistatic limit, not deterministic work, finite-power performance, or a claim that every physical battery's energy gain is useful work. The deficit is measured against the known-state benchmark; it is not defined as total bath heat.

## What makes the bounds meet?

The [lower bound](science/classical_lower.md) applies an inherited Haar-posterior entropy bound at every causal cut and cancels the controller's entropy changes against its final reset. It allows arbitrary adaptive instruments and unlimited classical storage.

The [upper construction](science/learner.md) uses a centered unbiased estimator and four small tangent tilts of the current direction. Its expected estimation error is at most 21/t for every fixed pure qubit, and its cumulative expected probe regret has logarithmic order. An [explicit work cycle](science/work_cycle.md) then extracts work and pays for every measurement record through a state-independent reset schedule.

The posterior identity, the global Haar entropy benchmark, and the connection between learning and work extraction have prior sources. The added result is the matched causal work law and the explicit expected-risk construction that attains its classical order. [Related work](references/PRIORITY.md) states the comparison with the closest learning and extraction theorems.

## Read and reproduce

| Question | Account |
|---|---|
| What is supplied, retained, and charged? | [Operational model](science/MODEL.md) |
| What exactly is proved? | [Results and limitations](science/results.md) |
| Why does classical memory incur the larger deficit? | [Entropy converse](science/classical_lower.md) |
| How does the adaptive learner work? | [Algorithm and proof](science/learner.md) |
| Where is the final record-erasure cost included? | [Physical work cycle](science/work_cycle.md) |
| How is the coherent benchmark attained sequentially? | [Streaming compression](science/coherent.md) |
| What is inherited and what is added? | [Related work](references/PRIORITY.md) |
| How can the finite checks be repeated? | [Verification](verification/README.md) |

Start with the [connected scientific overview](science/README.md), or use the [LLM reading guide](llms.txt) to locate a particular statement. The learning route uses **John Watrous, The Theory of Quantum Information (2018)**: the [source bridge](learning/WATROUS_BRIDGE.md) and [30 milestones](learning/MILESTONES.md) connect the prerequisites to the complete argument.

```bash
python -m pip install -r verification/requirements.txt
python verification/check_science.py
python verification/check_science.py --simulate --output /tmp/qld-results.json
```

The suite checks exact conditional-moment formulas by finite enumeration, the induction constants, entropy identities, and the coherent isometries and Haar averages. The optional seeded simulation is a diagnostic, not a proof. No independent experimental or expert validation is claimed.

## Scope

The source is pure and fixed, and controls and bath operations are idealized. Fixed mixedness, source drift, noisy persistent memory, efficient finite-precision compilation, finite-time power, optimal leading constants, and the smallest sufficient coherent memory are not determined here. The comparison uses the same chronology and reset account for both controller classes; it does not grant either a free quantum side channel.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).
