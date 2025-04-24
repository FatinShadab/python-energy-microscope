import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../")))

from energy_module.decorator import measure_energy_to_csv
from time_modules.decorator import measure_time_to_csv
from input import __default__

import ctypes
import platform

# Load shared library based on OS
if platform.system() == "Windows":
    lib = ctypes.CDLL("./pi.dll")
else:
    lib = ctypes.CDLL("./libpi.so")

# Define return type and argument type for the function
lib.compute_pi_gauss_legendre.argtypes = [ctypes.c_int]
lib.compute_pi_gauss_legendre.restype = ctypes.c_double

def driver(iterations):
    """
    Driver function to call the C function for computing Pi using Gauss-Legendre algorithm.
    
    :param iterations: Number of iterations for the algorithm
    :return: Computed value of Pi
    """
    pi_approx : float = lib.compute_pi_gauss_legendre(iterations)
    print(f"Computed Pi: {pi_approx}")
    
    return pi_approx

@measure_energy_to_csv(n=__default__["pi_digits"]["test_n"], csv_filename="pi_digits_ctypes")
def run_energy_benchmark(iterations: int) -> None:
    driver(iterations)

@measure_time_to_csv(n=__default__["pi_digits"]["test_n"], csv_filename="pi_digits_ctypes")
def run_time_benchmark(iterations: int) -> None:
    driver(iterations)
    
    
if __name__ == "__main__":
    ITERATIONS = __default__["pi_digits"]["iterations"]
    
    # Run benchmarks
    run_energy_benchmark(ITERATIONS)
    run_time_benchmark(ITERATIONS)
