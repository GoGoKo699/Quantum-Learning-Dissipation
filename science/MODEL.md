# Causal learning and work extraction: model to be verified

## Source
An unknown pure qubit state P is supplied as N independent identical copies. The state is fixed throughout a run; the performance criterion must explicitly specify either worst-case P or a Haar average. At round t the controller sees only the current specimen and retained memory, not future specimens.

## Controller classes
* Classical-memory controller: arbitrary adaptive quantum instrument on the arriving specimen, with only classical information retained across rounds. Ancillas used within a round must be returned or charged.
* Coherent-memory controller: a bounded quantum register may survive between rounds. All memory initialization, correlations, and final restoration must enter the accounting.

## Work ledger
Assume degenerate specimen Hamiltonians and a bath at temperature T. Define the work deficit relative to a known-state reference protocol, with signs and physical work-storage system stated explicitly. Count every record and reset, including the final memory. Quasistatic reversible operations are an ideal limit, not a finite-time implementation.

## Research targets (not established by this repository)
Determine whether classical-memory work deficit is Theta(k_B T (ln N)^2) and whether a logarithmic-qubit coherent register achieves k_B T ln(N+1) under exactly the same accounting. Prove lower and upper bounds with explicit constants, quantify the precise memory dimension and restoration requirements, and test worst-case versus average-case distinctions.

## Critical caveats
A learning regret bound is not automatically a thermodynamic work theorem. It must be converted through a physically consistent feedback and erasure ledger. A quantum memory's information content cannot be ignored at the final boundary. No claim of a completed proof or a PRX Quantum result is made here.
