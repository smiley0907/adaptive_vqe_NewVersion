# Cell 12: Calculate average performance metrics

import numpy as np

# Conventional VQE results from Table I
conventional_evaluations = [34, 36, 32]
conventional_errors = [4.2745, 5.1, 3.8]

# Adaptive VQE results from Table II
adaptive_evaluations = [6, 7, 5]
adaptive_errors = [5.7717, 8.2, 4.9]

# Calculate averages
avg_conventional_evaluations = np.mean(conventional_evaluations)
avg_adaptive_evaluations = np.mean(adaptive_evaluations)

avg_conventional_error = np.mean(conventional_errors) * 1e-9
avg_adaptive_error = np.mean(adaptive_errors) * 1e-11

# Calculate percentage reductions
evaluation_reduction = (
    (avg_conventional_evaluations - avg_adaptive_evaluations)
    / avg_conventional_evaluations
) * 100

energy_error_reduction = (
    (avg_conventional_error - avg_adaptive_error)
    / avg_conventional_error
) * 100

# Display results
print("Average Conventional VQE evaluations:",
      avg_conventional_evaluations)

print("Average Adaptive VQE evaluations:",
      avg_adaptive_evaluations)

print("Average Conventional VQE energy error:",
      f"{avg_conventional_error:.6e}", "Hartree")

print("Average Adaptive VQE energy error:",
      f"{avg_adaptive_error:.6e}", "Hartree")

print("Evaluation reduction:",
      f"{evaluation_reduction:.2f}%")

print("Energy error reduction:",
      f"{energy_error_reduction:.2f}%")
