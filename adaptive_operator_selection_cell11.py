# Cell 11: Define the adaptive operator-selection procedure

def select_adaptive_operator(
    parameters,
    circuit,
    operator_pool,
    hamiltonian
):
    """
    Select the candidate operator that produces the
    lowest molecular energy when applied to the current state.
    """

    current_energy = calculate_energy(
        parameters,
        circuit,
        hamiltonian
    )

    best_operator = None
    best_energy = current_energy
    best_index = None

    for index, operator in enumerate(operator_pool):

        # Evaluate candidate operators using their expectation
        # value with the current quantum state.
        state = Statevector.from_instruction(
            circuit.assign_parameters(parameters)
        )

        score = abs(
            np.real(state.expectation_value(operator))
        )

        if score > 0:
            if best_operator is None:
                best_operator = operator
                best_index = index
                best_score = score
            elif score > best_score:
                best_operator = operator
                best_index = index
                best_score = score

    return best_index, best_operator, current_energy


print("Adaptive operator-selection procedure defined.")
