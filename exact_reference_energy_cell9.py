# Cell 9: Calculate the exact reference energy for H2

from scipy.linalg import eigh

# Convert the qubit Hamiltonian into a matrix
hamiltonian_matrix = qubit_hamiltonian.to_matrix()

# Calculate all eigenvalues
eigenvalues = eigh(
    hamiltonian_matrix,
    eigvals_only=True
)

# Ground-state energy is the minimum eigenvalue
electronic_ground_state_energy = float(np.min(eigenvalues))

# Add the nuclear repulsion energy
nuclear_repulsion_energy = (
    electronic_structure_problem.nuclear_repulsion_energy
)

# Calculate total molecular reference energy
exact_reference_energy = (
    electronic_ground_state_energy
    + nuclear_repulsion_energy
)

print("H2 Exact Reference Energy")
print("-------------------------")
print("Electronic ground-state energy:",
      electronic_ground_state_energy, "Hartree")
print("Nuclear repulsion energy:",
      nuclear_repulsion_energy, "Hartree")
print("Total reference energy:",
      exact_reference_energy, "Hartree")
