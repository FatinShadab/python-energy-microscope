import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../")))

from energy_module.decorator import measure_energy_to_csv
from time_modules.decorator import measure_time_to_csv
from input import __default__

from raw import reverse_complement

@measure_energy_to_csv(n=__default__["reverse_complement"]["test_n"], csv_filename="reverse_complement_cython")
def run_energy_benchmark(dna_sequence: str) -> None:
    reverse_complement(dna_sequence.encode("utf-8"))
    
@measure_time_to_csv(n=__default__["reverse_complement"]["test_n"], csv_filename="reverse_complement_cython")
def run_time_benchmark(dna_sequence: str) -> None:
    reverse_complement(dna_sequence.encode("utf-8"))


if __name__ == "__main__":
    # Example DNA sequence
    dna = __default__["reverse_complement"]["dna_sequence"]
    
    # Run benchmarks
    run_energy_benchmark(dna)
    run_time_benchmark(dna)
