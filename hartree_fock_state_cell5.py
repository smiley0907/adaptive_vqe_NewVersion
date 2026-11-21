# Cell 5: Construct the Hartree-Fock initial state

# Create the Hartree-Fock initial state
hartree_fock_circuit = HartreeFock(
    num_spatial_orbitals=num_spatial_orbitals,
    num_particles=num_particles,
    qubit_mapper=mapper
)

# Display the circuit
print("Hartree-Fock Initial State Circuit:")
display(hartree_fock_circuit.draw("mpl"))

# Display circuit properties
print("\nNumber of qubits:", hartree_fock_circuit.num_qubits)
print("Circuit depth:", hartree_fock_circuit.depth())
print("Total gates:", hartree_fock_circuit.size())

# Obtain the initial statevector
initial_state = Statevector.from_instruction(hartree_fock_circuit)

print("\nInitial statevector:")
print(initial_state)
