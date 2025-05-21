import re
from typing import List, Tuple
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../")))

from energy_module.decorator import measure_energy_to_csv
from time_modules.decorator import measure_time_to_csv
from input import __default__


def read_fasta_file(file_path: str) -> str:
    """
    Reads a FASTA file and returns the DNA sequence as a single string.
    Removes descriptions and line breaks.
    """
    with open(file_path, 'r') as file:
        content = file.read()

    # Remove description lines and newlines
    return re.sub(r">.*\n|\n", "", content)

def count_patterns(sequence: str, patterns: List[str]) -> List[Tuple[str, int]]:
    """
    Counts occurrences of each pattern in the DNA sequence.
    """
    results = []
    for pattern in patterns:
        count = len(re.findall(pattern, sequence))
        results.append((pattern, count))
    return results

def apply_substitutions(sequence: str, substitutions: List[Tuple[str, str]]) -> str:
    """
    Applies a series of substitution patterns to the DNA sequence.
    """
    for pattern, replacement in substitutions:
        sequence = re.sub(pattern, replacement, sequence)
    return sequence

def regex_redux(file_path: str) -> None:
    """
    Main function to execute the Regex-Redux benchmark.
    """
    # Step 1: Read and clean the input sequence
    sequence = read_fasta_file(file_path).lower()
    initial_length = len(sequence)

    # Step 2: Count the original patterns
    patterns = [
        'agggtaaa|tttaccct',
        '[cgt]gggtaaa|tttaccc[acg]',
        'a[act]ggtaaa|tttacc[agt]t',
        'ag[act]gtaaa|tttac[agt]ct',
        'agg[act]taaa|ttta[agt]cct',
        'aggg[acg]aaa|ttt[cgt]ccct',
        'agggt[cgt]aa|tt[acg]accct',
        'agggta[cgt]a|t[acg]taccct',
        'agggtaa[cgt]|[acg]ttaccct'
    ]

    # Counting occurrences
    pattern_counts = count_patterns(sequence, patterns)

    # Step 3: Apply the substitutions
    substitutions = [
        (r'tHa[Nt]', '<4>'),
        (r'aND|caN|Ha[DS]|WaS', '<3>'),
        (r'a[NSt]|BY', '<2>'),
        (r'<[^>]*>', '|'),
        (r'\|[^|][^|]*\|', '-')
    ]

    modified_sequence = apply_substitutions(sequence, substitutions)

    # Step 4: Output results
    print("Pattern Counts:")
    for pattern, count in pattern_counts:
        print(f"{pattern}: {count}")

    print("\nInitial Length:", initial_length)
    print("Cleaned Length:", len(sequence))
    print("Substituted Length:", len(modified_sequence))

@measure_time_to_csv(n=__default__["regex_redux"]["test_n"], csv_filename="regex_redux_cpython")
def run_time_benchmark(file_path: str) -> None:
    """
    Measure and log the time it takes to run the Regex-Redux benchmark.
    """
    regex_redux(file_path)


@measure_energy_to_csv(n=__default__["regex_redux"]["test_n"], csv_filename="regex_redux_cpython")
def run_energy_benchmark(file_path: str) -> None:
    """
    Measure and log the energy consumption of the Regex-Redux benchmark.
    """
    regex_redux(file_path)


if __name__ == "__main__":
    file_path = __default__["regex_redux"]["file_path"]

    # You can change this to driver(file_path) if you want plain output
    run_energy_benchmark(file_path)
    run_time_benchmark(file_path)
