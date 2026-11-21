# Cell 15: Plot molecular energy error comparison

import matplotlib.pyplot as plt

methods = ["Conventional VQE", "Adaptive VQE"]

# Convert both average errors to the same unit: 10^-11 Hartree
energy_errors = [
    avg_conventional_error * 1e11,
    avg_adaptive_error * 1e11
]

plt.figure(figsize=(8, 5))

bars = plt.bar(
    methods,
    energy_errors,
    width=0.5
)

plt.title("Molecular Energy Error Comparison for H2")
plt.xlabel("VQE Method")
plt.ylabel("Average Energy Error (10^-11 Hartree)")

for bar in bars:
    height = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        height,
        f"{height:.4f}",
        ha="center",
        va="bottom"
    )

plt.tight_layout()
plt.show()
