import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../")))

from energy_module.decorator import measure_energy_to_csv
from time_modules.decorator import measure_time_to_csv
from input import __default__

import math

def compute_pi_gauss_legendre(iterations: int = 10) -> float:
    """
    Computes an approximation of Pi using the Gauss-Legendre algorithm.

    This algorithm iteratively refines the value of Pi with quadratic convergence,
    meaning the number of correct digits roughly doubles in each iteration.

    Parameters:
    iterations (int): The number of iterations to perform. More iterations yield higher precision.

    Returns:
    float: The computed value of Pi.
    """
    # Initialize variables
    a: float = 1.0
    b: float = 1.0 / math.sqrt(2)
    t: float = 0.25
    p: float = 1.0

    for _ in range(iterations):
        a_next: float = (a + b) / 2
        b = math.sqrt(a * b)
        t -= p * (a - a_next) ** 2
        a = a_next
        p *= 2  # Double p in each iteration

    # Compute final Pi approximation
    return ((a + b) ** 2) / (4 * t)

@measure_energy_to_csv(n=__default__["pi_digits"]["test_n"], csv_filename="pi_digits_pypy")
def run_energy_benchmark(iterations: int) -> None:
    pi_approx : float = compute_pi_gauss_legendre(iterations)
    print(f"Computed Pi: {pi_approx}")

@measure_time_to_csv(n=__default__["pi_digits"]["test_n"], csv_filename="pi_digits_pypy")
def run_time_benchmark(iterations: int) -> None:
    pi_approx : float = compute_pi_gauss_legendre(iterations)
    print(f"Computed Pi: {pi_approx}")


if __name__ == "__main__":
    ITERATIONS = __default__["pi_digits"]["iterations"]
    
    # Run benchmarks
    run_energy_benchmark(ITERATIONS)
    run_time_benchmark(ITERATIONS)
