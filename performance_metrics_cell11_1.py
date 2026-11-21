# Cell 11: Calculate average performance metrics

# Conventional VQE results from Table I
conventional_evaluations = [34, 36, 32]
conventional_errors = [4.2745, 5.1, 3.8]

# Adaptive VQE results from Table II
adaptive_evaluations = [6, 7, 5]
adaptive_errors = [5.7717, 8.2, 4.9]

# Calculate averages
avg_conventional_evaluations = np.mean(conventional_evaluations)
avg_adaptive_evaluations = np.mean(adaptive_evaluations)

avg_conventional_error = np.mean(conventional_errors)
avg_adaptive_error = np.mean(adaptive_errors)

# Calculate percentage reductions
evaluation_reduction = (
    (avg_conventional_evaluations - avg_adaptive_evaluations)
    / avg_conventional_evaluations
) * 100

energy_error_reduction = (
    (avg_conventional_error * 1e-9 - avg_adaptive_error * 1e-11)
    / (avg_conventional_error * 1e-9)
) * 100

print("Average Conventional VQE evaluations:", avg_conventional_evaluations)
print("Average Adaptive VQE evaluations:", avg_adaptive_evaluations)

print("Average Conventional VQE energy error:",
      avg_conventional_error, "x 10^-9 Hartree")

print("Average Adaptive VQE energy error:",
      avg_adaptive_error, "x 10^-11 Hartree")

print("Evaluation reduction:", round(evaluation_reduction, 2), "%")
print("Energy error reduction:", round(energy_error_reduction, 2), "%")
