# Cell 10: Construct the Adaptive VQE operator pool

from qiskit.quantum_info import SparsePauliOp

# Define candidate Pauli operators
operator_pool = [
    SparsePauliOp.from_list([("XIII", 1.0)]),
    SparsePauliOp.from_list([("IXII", 1.0)]),
    SparsePauliOp.from_list([("IIXI", 1.0)]),
    SparsePauliOp.from_list([("IIIX", 1.0)]),
    SparsePauliOp.from_list([("XXII", 1.0)]),
    SparsePauliOp.from_list([("IIXX", 1.0)]),
    SparsePauliOp.from_list([("XIXI", 1.0)]),
    SparsePauliOp.from_list([("IXXI", 1.0)])
]

# Display the candidate operator pool
print("Adaptive VQE Candidate Operator Pool")
print("------------------------------------")

for index, operator in enumerate(operator_pool):
    print(f"Operator {index + 1}: {operator}")

print("\nTotal candidate operators:", len(operator_pool))
