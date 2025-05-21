from raw import fasta_alignment
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../")))

from energy_module.decorator import measure_energy_to_csv
from time_modules.decorator import measure_time_to_csv
from input import __default__

def driver(k, query, target):
    """
        Driver function to perform the alignment and print results.
    """
    
    score, alignment, aligned_q, aligned_t = fasta_alignment(query, target, k)

    print("Score:", score)
    print("Alignment starts at:", alignment)
    print("Query:", aligned_q)
    print("Target:", aligned_t)
    

# Benchmarking functions for energy
@measure_energy_to_csv(n=__default__["fasta"]["test_n"], csv_filename="fasta_cython")
def run_energy_benchmark(k: int, query_sequence: str, target_sequence: str) -> None:
    driver(k, query_sequence, target_sequence)

# Benchmarking function for time
@measure_time_to_csv(n=__default__["fasta"]["test_n"], csv_filename="fasta_cython")
def run_time_benchmark(k: int, query_sequence: str, target_sequence: str) -> None:
    driver(k, query_sequence, target_sequence)


if __name__ == "__main__":
    k = __default__["fasta"]["k"]
    query_sequence = __default__["fasta"]["query_sequence"]
    target_sequence = __default__["fasta"]["target_sequence"]
    
    # Run the energy benchmark
    run_energy_benchmark(k, query_sequence, target_sequence)
    # Run the time benchmark
    run_time_benchmark(k, query_sequence, target_sequence)
