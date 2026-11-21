# Cell 14: Plot optimizer evaluation comparison

import matplotlib.pyplot as plt

# Optimizer evaluation data
methods = ["Conventional VQE", "Adaptive VQE"]

evaluations = [
    avg_conventional_evaluations,
    avg_adaptive_evaluations
]

# Generate bar chart
plt.figure(figsize=(8, 5))

bars = plt.bar(
    methods,
    evaluations,
    width=0.5
)

plt.title("Optimizer Evaluation Comparison for H2")
plt.xlabel("VQE Method")
plt.ylabel("Average Optimizer Evaluations")

# Display values above bars
for bar in bars:
    height = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        height,
        f"{height:.0f}",
        ha="center",
        va="bottom"
    )

plt.tight_layout()
plt.show()
