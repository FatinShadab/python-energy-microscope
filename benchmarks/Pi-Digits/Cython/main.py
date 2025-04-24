import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../")))

from energy_module.decorator import measure_energy_to_csv
from time_modules.decorator import measure_time_to_csv
from input import __default__

from raw import compute_pi_gauss_legendre

@measure_energy_to_csv(n=__default__["pi_digits"]["test_n"], csv_filename="pi_digits_cython")
def run_energy_benchmark(iterations: int) -> None:
    pi_approx : float = compute_pi_gauss_legendre(iterations)
    print(f"Computed Pi: {pi_approx}")

@measure_time_to_csv(n=__default__["pi_digits"]["test_n"], csv_filename="pi_digits_cython")
def run_time_benchmark(iterations: int) -> None:
    pi_approx : float = compute_pi_gauss_legendre(iterations)
    print(f"Computed Pi: {pi_approx}")


if __name__ == "__main__":
    ITERATIONS = __default__["pi_digits"]["iterations"]
    
    # Run benchmarks
    run_energy_benchmark(ITERATIONS)
    run_time_benchmark(ITERATIONS)
