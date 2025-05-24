import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../")))

from energy_module.decorator import measure_energy_to_csv
from time_modules.decorator import measure_time_to_csv
from raw import spectral_norm
from input import __default__

from typing import List

@measure_energy_to_csv(n=__default__["spectral-norm"]["test_n"], csv_filename="spectral_norm_cpython")
def run_energy_benchmark(matrix: List[List[int]], iterations=10) -> None:
    spectral_norm(matrix, iterations)

@measure_time_to_csv(n=__default__["spectral-norm"]["test_n"], csv_filename="spectral_norm_cpython")
def run_time_benchmark(matrix: List[List[int]], iterations=10) -> None:
    spectral_norm(matrix, iterations)
    

if __name__ == "__main__":
    A = __default__["spectral-norm"]["matrix"]
    itr = __default__["spectral-norm"]["iterations"]
    
    # Run the benchmarks
    run_energy_benchmark(A, itr)
    run_time_benchmark(A, itr)
