# Cell 2: Import libraries and configure the H2 molecular system

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from scipy.optimize import minimize

from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector

from qiskit_aer import AerSimulator

from qiskit_nature.second_q.drivers import PySCFDriver
from qiskit_nature.second_q.mappers import JordanWignerMapper
from qiskit_nature.second_q.transformers import ActiveSpaceTransformer
from qiskit_nature.second_q.circuit.library import HartreeFock

from qiskit_algorithms import VQE
from qiskit_algorithms.optimizers import SLSQP

from IPython.display import display

# Molecular configuration: Hydrogen (H2)

BOND_DISTANCE = 0.735  # Angstrom
BASIS_SET = "sto3g"
CHARGE = 0
SPIN = 0

print("Molecular system: H2")
print("Bond distance:", BOND_DISTANCE, "Angstrom")
print("Basis set:", BASIS_SET)
print("Charge:", CHARGE)
print("Spin:", SPIN)
