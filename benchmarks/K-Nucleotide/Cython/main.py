import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../")))

from energy_module.decorator import measure_energy_to_csv
from time_modules.decorator import measure_time_to_csv
from input import __default__

from collections import defaultdict
from typing import Dict

from raw import count_kmers

def read_sequence(file_path: str) -> str:
    """Reads the DNA sequence from a file, ignoring headers.
    
    Args:
        file_path (str): Path to the input file containing the DNA sequence.
    
    Returns:
        str: The processed DNA sequence as a single string.
    """
    sequence: list[str] = []
    with open(file_path, 'r') as file:
        for line in file:
            if not line.startswith('>'):
                sequence.append(line.strip().upper())  # Convert to uppercase for consistency
    return ''.join(sequence)

def print_kmer_frequencies(kmers: Dict[str, int]) -> None:
    """Prints k-mer frequencies sorted by frequency (descending), then alphabetically.
    
    Args:
        kmers (Dict[str, int]): Dictionary of k-mer counts.
    """
    sorted_kmers = sorted(kmers.items(), key=lambda item: (-item[1], item[0]))
    for kmer, freq in sorted_kmers:
        print(f"{kmer}: {freq}")

def main() -> None:
    """Main function to execute the K-Nucleotide frequency analysis."""    
    file_path: str = __default__["K_Nucleotide"]["nucleotide_sequence_file"]
    k: int = __default__["K_Nucleotide"]["k"]
    
    sequence: str = read_sequence(file_path)
    kmers: Dict[str, int] = count_kmers(sequence, k)
    print_kmer_frequencies(kmers)

@measure_energy_to_csv(n=__default__["K_Nucleotide"]["test_n"], csv_filename="K_Nucleotide_cython")
def run_energy_benchmark() -> None:
    main()

@measure_time_to_csv(n=__default__["K_Nucleotide"]["test_n"], csv_filename="K_Nucleotide_cython")
def run_time_benchmark() -> None:
    main()

if __name__ == "__main__":
    run_energy_benchmark()
    run_time_benchmark()
