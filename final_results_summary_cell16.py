# Cell 16: Display final experimental results

final_results = pd.DataFrame({
    "Performance Metric": [
        "Average Optimizer Evaluations",
        "Average Energy Error (Hartree)",
        "Evaluation Reduction (%)",
        "Energy Error Reduction (%)"
    ],
    "Conventional VQE": [
        avg_conventional_evaluations,
        f"{avg_conventional_error:.6e}",
        "-",
        "-"
    ],
    "Adaptive VQE": [
        avg_adaptive_evaluations,
        f"{avg_adaptive_error:.6e}",
        f"{evaluation_reduction:.2f}%",
        f"{energy_error_reduction:.2f}%"
    ]
})

print("FINAL EXPERIMENTAL RESULTS — H2 MOLECULAR BENCHMARK")
display(final_results)
