# An unbiased adaptive learner with logarithmic expected probe regret

[Results](results.md) · [Work conversion](work_cycle.md) · [Checks](../verification/README.md)

The protocol below receives exactly one copy per round. It knows that the state is pure, but does not know its Bloch vector n. It uses neither a warm start nor a state-preparation oracle. All expectations in this page are for one fixed n and include the protocol's random choices.

## 1. Protocol

Initialize v_0 = 0. At round t, normalize v_(t-1) to a unit vector w_t; when it is zero, choose the north pole. Choose any deterministically specified orthonormal pair e_1,e_2 perpendicular to w_t. A nonsingular rule is to cross w_t with the Cartesian axis having its smallest absolute component, normalize, and take the second cross product.

Set

```math
s_t^2=\min\left\{\frac12,\frac{32}{t}\right\},
\qquad c_t=\sqrt{1-s_t^2}.
```

Choose u_t uniformly from e_1,-e_1,e_2,-e_2, and measure the specimen along the unit Bloch direction

```math
\boldsymbol a_t=c_t\boldsymbol w_t+s_t\boldsymbol u_t.
```

Record b_t in {-1,+1}, whose conditional mean is n dot a_t. Form

```math
\boldsymbol g_t=\boldsymbol w_t+
(b_t-c_t)\left(\frac{\boldsymbol w_t}{c_t}
+\frac{2\boldsymbol u_t}{s_t}\right),
\qquad
\boldsymbol v_t=\left(1-\frac1t\right)\boldsymbol v_{t-1}
+\frac1t\boldsymbol g_t.
```

The unconstrained v_t is not itself a quantum state; only its normalized direction is used for the next physical measurement. The four-valued random choice is independent of the source. Its physical record is accounted for in the work construction.

## 2. Exact conditional moments

Condition on the entire past and abbreviate w,s,c. The random tangent vector has mean zero and second moment (I-ww^T)/2. Therefore the design matrix is

```math
A=\mathbb E[\boldsymbol a\boldsymbol a^{\mathsf T}]
=c^2\boldsymbol w\boldsymbol w^{\mathsf T}
+\frac{s^2}{2}(I-\boldsymbol w\boldsymbol w^{\mathsf T}),
\qquad
A^{-1}\boldsymbol a=\frac{\boldsymbol w}{c}+\frac{2\boldsymbol u}{s}.
```

Using E[b|a] = n dot a and E[a] = c w gives

```math
\mathbb E[\boldsymbol g\mid\text{past}]=\boldsymbol n.
```

This identity averages the chosen probe and its outcome; it does not pretend that one projective measurement estimates all Bloch components by itself.

Let e = ||n-w||^2. Because n and w are unit vectors and b^2=1,

```math
\mathbb E(b-c)^2=s^2+c^2 e,
\qquad
\left\|\frac{\boldsymbol w}{c}+\frac{2\boldsymbol u}{s}\right\|^2
=\frac1{c^2}+\frac4{s^2}.
```

Subtracting the squared conditional mean from the second moment yields the exact variance

```math
\mathbb E\!\left[\|\boldsymbol g-\boldsymbol n\|^2\mid\text{past}\right]
=4+\frac{s^2}{c^2}+\frac{4c^2}{s^2}e.
```

The centering b-c is important: the variance becomes small when the current direction is accurate, even though the inverse design matrix grows.

## 3. Uniform mean-square bound

For any vector v, its normalization w satisfies ||w-n|| <= 2||v-n||; at v=0 the same squared bound follows from ||w-n||^2 <= 4. Let R_t = E||v_t-n||^2. Conditional unbiasedness eliminates the cross term in the update, so

```math
R_t=\left(1-\frac1t\right)^2R_{t-1}
+\frac1{t^2}\mathbb E\!\left[\|\boldsymbol g_t-\boldsymbol n\|^2\right].
```

For t at most 64, s^2=c^2=1/2 and the variance is 5+4e <= 21. Since the coefficient of R_0 vanishes at t=1, induction gives R_t <= 21/t throughout these rounds.

For t at least 65, the variance identity and E e <= 4R_(t-1) give

```math
R_t\le\left[\left(1-\frac1t\right)^2+\frac1{2t}\right]R_{t-1}
+\frac5{t^2}.
```

Substituting 21/(t-1), the difference between 21/t and the right-hand side is

```math
\frac1{t^2}\left(16-\frac{21t}{2(t-1)}\right)>0.
```

This is positive in the stated range. Thus R_t <= 21/t for every t, for every fixed pure input state. The normalized estimate has expected infidelity E e/4 <= R_t. No exceptional directions, favorable-history event, or postselection are used.

## 4. The probes themselves are inexpensive

Let q_t denote the minus-outcome probability for the chosen probe. Averaging the tangent choice gives

```math
\mathbb E q_t
=\frac{1-c_t}{2}+\frac{c_t}{4}\mathbb E\|\boldsymbol n-\boldsymbol w_t\|^2.
```

For t at least 65 this is at most 16/t + 21/(t-1), hence at most 38/t. Use the trivial bound one in the first 76 rounds. The cumulative expected probe infidelity is therefore at most 76 + 38 ln N. Combined with the inherited posterior-based logarithmic lower bound, this determines its optimal order for qubits.

The proof is an expected-risk proof. It is not a high-probability confidence-sequence theorem. Purity enters the variance identity; a fixed mixed-state noise floor cannot be silently substituted into it. These limits are essential when comparing with prior polylogarithmic learning guarantees.
