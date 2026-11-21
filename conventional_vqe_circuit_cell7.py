# Cell 7: Construct the Conventional VQE parameterized circuit

from qiskit.circuit import ParameterVector

# Define the number of qubits
num_qubits = qubit_hamiltonian.num_qubits

# Define the number of variational parameters
num_parameters = 4

# Create a parameter vector
theta = ParameterVector("theta", num_parameters)

# Create the parameterized quantum circuit
conventional_circuit = QuantumCircuit(num_qubits)

# Prepare the Hartree-Fock reference state
conventional_circuit.compose(
    hartree_fock_circuit,
    inplace=True
)

# Apply parameterized rotation gates
for qubit in range(num_qubits):
    conventional_circuit.ry(theta[qubit], qubit)

# Apply entanglement gates
conventional_circuit.cx(0, 1)
conventional_circuit.cx(1, 2)
conventional_circuit.cx(2, 3)

# Apply additional parameterized rotations
for qubit in range(num_qubits):
    conventional_circuit.rz(theta[qubit], qubit)

# Display the circuit
print("Conventional VQE Circuit:")
display(conventional_circuit.draw("mpl"))

print("\nNumber of qubits:", conventional_circuit.num_qubits)
print("Number of parameters:", conventional_circuit.num_parameters)
print("Circuit depth:", conventional_circuit.depth())
print("Total gates:", conventional_circuit.size())
