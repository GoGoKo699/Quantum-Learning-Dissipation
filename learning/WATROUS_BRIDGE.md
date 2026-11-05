# Educational anchor: Watrous (2018)

John Watrous, *The Theory of Quantum Information* (Cambridge University Press, 2018), is the single educational anchor for this project.

## Source-to-problem bridge
- Quantum states, channels, instruments and trace norms: define each adaptive one-specimen operation and its classical outcome.
- Purifications, Stinespring representations and complementary channels: account for information leaving the controller and for residual correlations.
- Entropy, relative entropy and data processing: support information bounds, but do not themselves imply a heat/work statement.
- Symmetric subspaces and Haar integration: analyze learning from identical unknown pure qubits.
- Quantum memory versus classical records: formalize which systems persist between arrivals.

## Scope distinction
The textbook supplies information-theoretic tools. Thermodynamic work, bath return, and the conversion from estimation regret to dissipated work require separate explicit assumptions and proofs.

## Worked starting example
For a uniformly random pure qubit P, the mean state is I/2. Without a prior specimen, no fixed basis distinguishes P from its antipode on average. With a single measured training copy, the conditional state estimate is informative, but its measurement outcome is a physical record requiring accounting. Compare this with retaining the copy coherently: no classical estimate is necessary, but the retained register is itself a resource.

## Reading path
Study the channel/instrument framework first, then entropy and data processing, then Haar moments and symmetric subspaces. Return to the operational work ledger after each stage. Do not read the entire textbook as a prerequisite.
