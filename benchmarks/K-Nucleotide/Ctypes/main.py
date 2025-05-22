import sys
import os
import time
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../")))

from energy_module.decorator import measure_energy_to_csv
from time_modules.decorator import measure_time_to_csv
from input import __default__

from typing import Dict

import ctypes
from ctypes import c_char_p, c_int, POINTER, Structure

# Adjust for your platform
lib = ctypes.CDLL('./libkmer.so')  # or libkmer.dylib / kmer.dll

class KmerCount(Structure):
    _fields_ = [("kmer", c_char_p), ("count", c_int)]

class KmerMap(Structure):
    _fields_ = [("data", POINTER(KmerCount)), ("size", c_int), ("capacity", c_int)]

lib.count_kmers.restype = POINTER(KmerMap)
lib.count_kmers.argtypes = [c_char_p, c_int]

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


def count_kmers(sequence: str, k: int):
    seq_bytes = sequence.encode('utf-8')
    result = lib.count_kmers(seq_bytes, k)
    kmer_map = result.contents

    counts = {}
    for i in range(kmer_map.size):
        kmer = kmer_map.data[i].kmer.decode('utf-8')
        count = kmer_map.data[i].count
        counts[kmer] = count

    return counts

def main() -> None:
    """Main function to execute the K-Nucleotide frequency analysis."""    
    file_path: str = __default__["K_Nucleotide"]["nucleotide_sequence_file"]
    k: int = __default__["K_Nucleotide"]["k"]
    
    sequence: str = read_sequence(file_path)
    kmers: Dict[str, int] = count_kmers(sequence, k)
    print_kmer_frequencies(kmers)

@measure_energy_to_csv(n=__default__["K_Nucleotide"]["test_n"], csv_filename="K_Nucleotide_ctypes")
def run_energy_benchmark() -> None:
    main()
    time.sleep(0.01)

@measure_time_to_csv(n=__default__["K_Nucleotide"]["test_n"], csv_filename="K_Nucleotide_ctypes")
def run_time_benchmark() -> None:
    main()
    time.sleep(0.01)


if __name__ == "__main__":
    run_energy_benchmark()
    run_time_benchmark()
