# Converting the learner into work, including its final reset

[Model](MODEL.md) · [Learner](learner.md) · [Results](results.md)

A small estimation error does not by itself prove a work guarantee. This page supplies the cycle and a reset prescription that does not require knowing the true state or its posterior.

## Measurement, feedback, and extraction

Use the learner's projective measurement along a_t, storing its sign in a clean classical bit. A premeasurement unitary followed by dephasing of the record realizes the instrument. In the degenerate setting dephasing can be implemented by a controlled phase with an initially maximally mixed reservoir coin, with no energy exchange. The spent coin is not reused.

Conditioned on the recorded sign, the specimen is a known pure eigenstate. Rotate it to a fixed reference state and perform ideal isothermal expansion to I/2, extracting k_B T ln 2. The feedback rotation is controlled by the stored bit, rather than an external uncharged measurement record. The original specimen is then discarded before the next one arrives.

Keep the sign history and the independent four-valued random choices. Arithmetic and control selection can be performed reversibly from these inputs, and their working registers can be uncomputed before final erasure. Initially mixed random-choice registers provide no purity for work extraction. After erasing all sign bits, refresh any residual correlations of these random registers by swapping with fresh maximally mixed bath registers. Their original marginal and independence are thereby restored at zero work. This construction uses unrestricted classical memory, as permitted by the model; it does not claim an optimal classical storage size.

## A reset schedule independent of the unknown state

For round t set

```math
p_t=\min\left\{\frac12,\frac{38}{t}\right\}.
```

Design the reset of its sign bit for reference distribution (1-p_t,p_t). For an actual minus probability q, the ideal expected work supplied to this reset is

```math
\beta W_{\rm erase}(q,p_t)
=-(1-q)\ln(1-p_t)-q\ln p_t.
```

An explicit realization first quenches the two energy levels from zero to -k_B T ln(1-p_t) and -k_B T ln p_t. Thermalizing then produces the reference Gibbs distribution, whose partition function is one. Quasistatically changing to a pure reference ground state has zero further free-energy difference with this energy-offset convention; finally returning the empty excited level to zero costs no work. The total is the displayed cross entropy. Exact purity and reversible saturation are ideal limits, not finite-reservoir claims.

The reset can be applied separately to each bit after uncomputing the arithmetic. Correlations between bits do not change the expected work of a local reset, which is determined by that bit's marginal. Resetting each to a pure state removes all its correlations. We are not claiming this deliberately simple erasure schedule is the optimal correlated erasure protocol.

For t at most 76, p_t=1/2 and the cost is exactly ln 2 for every q. For larger t the learner guarantees E q_t <= p_t. Since the cross entropy above is linear and increasing in q when p_t <= 1/2,

```math
\beta\,\mathbb E_{\boldsymbol n}W_{{\rm erase},t}\le h(p_t).
```

The estimate is unconditional and valid for every fixed pure input state. It does not assume a bound on every measurement history. After paying all these resets, the net work obeys

```math
\beta\,\mathbb E_{\boldsymbol n}W_{\rm net}
\ge N\ln2-U_N.
```

Record erasure is charged once. Adding another full record-entropy cost to this expression would double count it. Conversely, citing the extracted N ln 2 before restoration would give a false advantage.

## Asymptotic order

For large t, h(38/t) = (38/t)[ln t - ln 38 + 1] + O(t^(-2)). Summing gives U_N = 19(ln N)^2 + O(ln N). Together with the classical converse, this establishes the optimal squared-logarithmic order under the specified mean-work account.

## Finite precision and ideal limits

For a fixed finite horizon N the learner has a finite tree of at most 8^N seed/outcome histories. Its exact control directions can be precomputed and then approximated uniformly. This is an existence argument, not a computationally efficient compilation claim.

Suppose each implemented projective direction changes every conditional binary outcome probability by at most eta. A sequential coupling bounds the total-variation distance of the full transcript laws by N eta. The final erasure cost is the transcript function sum_t -ln p_t(b_t), between zero and N ell_N, where ell_N = max(ln 2, ln(N/38)). Hence its mean changes by at most N^2 ell_N eta. The post-measurement specimens remain known pure eigenstates of the actual implemented projectors, so their feedback and expansion can be tailored to those actual directions. Choosing eta arbitrarily small realizes the ideal statistical bound with arbitrarily small additive overhead for each fixed N.

The thermal stages require separate quasistatic and finite-gap approximations. The project takes their ideal limits and does not assert a uniform finite-time or finite-energy-gap overhead as N grows. A fixed source mixedness or a fixed persistent implementation error is not covered by this finite-horizon approximation statement.
