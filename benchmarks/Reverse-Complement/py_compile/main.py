import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../")))

from energy_module.decorator import measure_energy_to_csv
from time_modules.decorator import measure_time_to_csv
from input import __default__

from typing import List

def reverse_complement(dna_sequence: str) -> str:
    """
    Computes the reverse complement of a given DNA sequence.

    DNA bases are replaced with their complementary bases:
    - 'A' → 'T'
    - 'T' → 'A'
    - 'C' → 'G'
    - 'G' → 'C'

    The sequence is first reversed and then each base is replaced with its complement.

    Args:
        dna_sequence (str): The input DNA sequence (uppercase, consisting of A, T, C, G).

    Returns:
        str: The reverse complement of the input DNA sequence.
    
    Example:
        >>> reverse_complement("ATGC")
        'GCAT'
    """

    # Complement mapping dictionary
    complement_map: dict[str, str] = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}

    # Generate reverse complement using list comprehension (efficient in CPython)
    return "".join(complement_map[base] for base in reversed(dna_sequence))

@measure_energy_to_csv(n=__default__["reverse_complement"]["test_n"], csv_filename="reverse_complement_pycompile")
def run_energy_benchmark(dna_sequence: str) -> None:
    reverse_complement(dna_sequence)

@measure_time_to_csv(n=__default__["reverse_complement"]["test_n"], csv_filename="reverse_complement_pycompile")
def run_time_benchmark(dna_sequence: str) -> None:
    reverse_complement(dna_sequence)


if __name__ == "__main__":
    # Example DNA sequence
    dna = __default__["reverse_complement"]["dna_sequence"]
    
    # Run benchmarks
    run_energy_benchmark(dna)
    run_time_benchmark(dna)

