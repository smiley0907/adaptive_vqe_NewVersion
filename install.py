# Cell 1: Install and verify required packages

%pip install -q qiskit qiskit-aer qiskit-nature qiskit-algorithms pyscf scipy numpy pandas matplotlib

# Verify package versions

import qiskit
import qiskit_aer
import qiskit_nature
import qiskit_algorithms
import numpy
import scipy
import pandas
import matplotlib

print("Qiskit:", qiskit.__version__)
print("Qiskit Aer:", qiskit_aer.__version__)
print("Qiskit Nature:", qiskit_nature.__version__)
print("Qiskit Algorithms:", qiskit_algorithms.__version__)
print("NumPy:", numpy.__version__)
print("SciPy:", scipy.__version__)
print("Pandas:", pandas.__version__)
print("Matplotlib:", matplotlib.__version__)
