import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../")))

from energy_module.decorator import measure_energy_to_csv
from time_modules.decorator import measure_time_to_csv
from input import __default__

import ctypes
from typing import List

# Load the compiled shared library
lib = ctypes.CDLL('./libspectral.so')  # Or 'spectral.dll' on Windows

# Define argument and return types
lib.spectral_norm.argtypes = [ctypes.POINTER(ctypes.c_double), ctypes.c_int, ctypes.c_int]
lib.spectral_norm.restype = ctypes.c_double

def flatten(matrix: List[List[int]]) -> List[float]:
    return [float(val) for row in matrix for val in row]

def spectral_norm(matrix: List[List[int]], iterations: int = 10) -> float:
    n = len(matrix)
    flat_matrix = flatten(matrix)
    c_matrix = (ctypes.c_double * (n * n))(*flat_matrix)
    return lib.spectral_norm(c_matrix, n, iterations)

@measure_energy_to_csv(n=__default__["spectral-norm"]["test_n"], csv_filename="spectral_norm_ctypes")
def run_energy_benchmark(matrix: List[List[int]], iterations=10) -> None:
    spectral_norm(matrix, iterations)

@measure_time_to_csv(n=__default__["spectral-norm"]["test_n"], csv_filename="spectral_norm_ctypes")
def run_time_benchmark(matrix: List[List[int]], iterations=10) -> None:
    spectral_norm(matrix, iterations)


if __name__ == "__main__":
    # Example matrix
    A = __default__["spectral-norm"]["matrix"]
    itr = __default__["spectral-norm"]["iterations"]

    # Run the benchmarks
    run_energy_benchmark(A, itr)
    run_time_benchmark(A, itr)
