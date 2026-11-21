# Cell 13: Generate Conventional VQE vs Adaptive VQE comparison table

comparison_data = {
    "Metric": [
        "Average optimizer evaluations",
        "Average energy error (Hartree)",
        "Evaluation reduction (%)",
        "Energy error reduction (%)"
    ],
    "Conventional VQE": [
        avg_conventional_evaluations,
        avg_conventional_error,
        "-",
        "-"
    ],
    "Adaptive VQE": [
        avg_adaptive_evaluations,
        avg_adaptive_error,
        round(evaluation_reduction, 2),
        round(energy_error_reduction, 2)
    ]
}

comparison_df = pd.DataFrame(comparison_data)

print("Conventional VQE vs Adaptive VQE")
display(comparison_df)
