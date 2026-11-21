# Cell 4: Map the molecular Hamiltonian using Jordan-Wigner mapping

# Initialize the Jordan-Wigner mapper
mapper = JordanWignerMapper()

# Convert the molecular Hamiltonian into a qubit operator
qubit_hamiltonian = mapper.map(
    second_q_hamiltonian.second_q_op()
)

# Display the qubit Hamiltonian
print("Qubit Hamiltonian:")
print(qubit_hamiltonian)

# Display Hamiltonian properties
print("\nNumber of qubits:", qubit_hamiltonian.num_qubits)
print("Number of Pauli terms:", len(qubit_hamiltonian))

# Display individual Pauli terms and coefficients
print("\nHamiltonian terms:")

for pauli, coefficient in zip(
    qubit_hamiltonian.paulis,
    qubit_hamiltonian.coeffs
):
    print(f"{pauli}: {coefficient.real:.10f}")
