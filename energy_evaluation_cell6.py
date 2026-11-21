# Cell 6: Define the quantum energy evaluation function

def calculate_energy(parameters, circuit_template, hamiltonian):
    """
    Calculate the molecular energy for a given set of
    variational parameters.
    """

    # Bind parameters to the quantum circuit
    bound_circuit = circuit_template.assign_parameters(
        parameters
    )

    # Simulate the quantum circuit
    state = Statevector.from_instruction(bound_circuit)

    # Calculate the expectation value of the Hamiltonian
    energy = state.expectation_value(hamiltonian)

    return float(np.real(energy))


print("Energy evaluation function defined successfully.")
