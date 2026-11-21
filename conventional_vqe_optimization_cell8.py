# Cell 8: Optimize the Conventional VQE circuit using SLSQP

# Initialize optimizer evaluation counter
conventional_evaluations = 0

# Define the objective function
def conventional_objective(parameters):
    global conventional_evaluations

    conventional_evaluations += 1

    energy = calculate_energy(
        parameters,
        conventional_circuit,
        qubit_hamiltonian
    )

    return energy


# Initial parameter values
initial_parameters = np.zeros(num_parameters)

# Run classical optimization
conventional_result = minimize(
    conventional_objective,
    initial_parameters,
    method="SLSQP",
    options={
        "maxiter": 200,
        "ftol": 1e-12,
        "disp": True
    }
)

# Store optimized results
conventional_energy = conventional_result.fun
conventional_parameters = conventional_result.x

# Calculate energy error
conventional_energy_error = abs(
    conventional_energy - exact_reference_energy
)

print("\nConventional VQE Results")
print("------------------------")
print("Optimized energy:", conventional_energy, "Hartree")
print("Exact reference energy:", exact_reference_energy, "Hartree")
print("Energy error:", conventional_energy_error, "Hartree")
print("Optimizer function evaluations:", conventional_evaluations)
print("Optimization successful:", conventional_result.success)
print("Optimizer message:", conventional_result.message)
