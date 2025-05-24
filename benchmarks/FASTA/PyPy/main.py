from typing import List, Tuple
import sys
import time
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../")))

from energy_module.decorator import measure_energy_to_csv
from time_modules.decorator import measure_time_to_csv
from input import __default__


# Function to generate k-tuples from a sequence
def generate_k_tuples(sequence: str, k: int) -> List[str]:
    """
    Generates all possible k-tuples (substrings of length k) from a sequence.

    Args:
    - sequence (str): The sequence from which k-tuples are generated.
    - k (int): The length of each k-tuple.

    Returns:
    - List[str]: A list of k-tuples (substrings of length k).
    """
    return [sequence[i:i+k] for i in range(len(sequence) - k + 1)]

# Function to calculate the alignment score using dynamic programming
def extend_alignment(query: str, target: str, start_q: int, start_t: int, k: int, match: int = 1, mismatch: int = -1, gap: int = -2) -> Tuple[int, str, str]:
    """
    Extends the k-tuple match using dynamic programming to find the best local alignment score.

    Args:
    - query (str): The query sequence.
    - target (str): The target sequence.
    - start_q (int): The starting position of the k-tuple in the query sequence.
    - start_t (int): The starting position of the k-tuple in the target sequence.
    - k (int): The length of the k-tuple.
    - match (int, optional): The score for a match. Defaults to 1.
    - mismatch (int, optional): The score for a mismatch. Defaults to -1.
    - gap (int, optional): The score for a gap. Defaults to -2.

    Returns:
    - Tuple[int, str, str]: The alignment score, aligned query sequence, and aligned target sequence.
    """
    # Initialize DP matrix for local alignment (Smith-Waterman approach)
    n, m = len(query), len(target)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    max_score = 0
    max_i, max_j = 0, 0
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if query[i-1] == target[j-1]:
                score = match
            else:
                score = mismatch
            dp[i][j] = max(0, dp[i-1][j-1] + score, dp[i-1][j] + gap, dp[i][j-1] + gap)

            if dp[i][j] > max_score:
                max_score = dp[i][j]
                max_i, max_j = i, j

    # Traceback to retrieve the best alignment (optional, if you need aligned sequences)
    aligned_query, aligned_target = [], []
    i, j = max_i, max_j
    while i > 0 and j > 0 and dp[i][j] > 0:
        if dp[i][j] == dp[i-1][j-1] + (match if query[i-1] == target[j-1] else mismatch):
            aligned_query.append(query[i-1])
            aligned_target.append(target[j-1])
            i -= 1
            j -= 1
        elif dp[i][j] == dp[i-1][j] + gap:
            aligned_query.append(query[i-1])
            aligned_target.append('-')
            i -= 1
        else:
            aligned_query.append('-')
            aligned_target.append(target[j-1])
            j -= 1

    aligned_query.reverse()
    aligned_target.reverse()

    return max_score, ''.join(aligned_query), ''.join(aligned_target)

# Function for FASTA sequence alignment
def fasta_alignment(query: str, target: str, k: int, match: int = 1, mismatch: int = -1, gap: int = -2) -> Tuple[int, Tuple[int, int], str, str]:
    """
    Performs the FASTA algorithm for local sequence alignment using k-tuple search followed by dynamic programming extension.

    Args:
    - query (str): The query sequence.
    - target (str): The target sequence.
    - k (int): The length of the k-tuple.
    - match (int, optional): The score for a match. Defaults to 1.
    - mismatch (int, optional): The score for a mismatch. Defaults to -1.
    - gap (int, optional): The score for a gap. Defaults to -2.

    Returns:
    - Tuple[int, Tuple[int, int], str, str]: The best alignment score, the starting positions of the best alignment in the query and target sequences, the aligned query sequence, and the aligned target sequence.
    """
    # Step 1: Generate k-tuples from query and target sequences
    query_k_tuples = generate_k_tuples(query, k)
    target_k_tuples = generate_k_tuples(target, k)

    # Step 2: Create a hash table for target k-tuples
    hash_table = {}
    for i, seq in enumerate(target_k_tuples):
        if seq not in hash_table:
            hash_table[seq] = []
        hash_table[seq].append(i)

    # Step 3: Perform k-tuple matching and extend alignments
    best_score = 0
    best_alignment = None
    best_aligned_query = ''
    best_aligned_target = ''
    
    for i, query_tuple in enumerate(query_k_tuples):
        if query_tuple in hash_table:
            for target_start in hash_table[query_tuple]:
                score, aligned_query, aligned_target = extend_alignment(query, target, i, target_start, k, match, mismatch, gap)
                if score > best_score:
                    best_score = score
                    best_alignment = (i, target_start)
                    best_aligned_query = aligned_query
                    best_aligned_target = aligned_target

    return best_score, best_alignment, best_aligned_query, best_aligned_target

# driver function to run the FASTA alignment
def driver(k: int, query_sequence: str, target_sequence: str) -> None:
    """
    Main driver function to run the FASTA alignment.
    """

    # Perform FASTA sequence alignment
    score, alignment, aligned_query, aligned_target = fasta_alignment(query_sequence, target_sequence, k)

    # Output the results
    print(f"Best alignment score: {score}")
    print(f"Best alignment starting at query position {alignment[0]} and target position {alignment[1]}")
    print("\nAligned Sequences:")
    print(f"Query:   {aligned_query}")
    print(f"Target:  {aligned_target}")
    
# Benchmarking functions for energy
@measure_energy_to_csv(n=__default__["fasta"]["test_n"], csv_filename="fasta_pypy")
def run_energy_benchmark(k: int, query_sequence: str, target_sequence: str) -> None:
    driver(k, query_sequence, target_sequence)
    time.sleep(0.01) # Simulate some processing time

# Benchmarking function for time
@measure_time_to_csv(n=__default__["fasta"]["test_n"], csv_filename="fasta_pypy")
def run_time_benchmark(k: int, query_sequence: str, target_sequence: str) -> None:
    driver(k, query_sequence, target_sequence)
    time.sleep(0.01) # Simulate some processing time


# Example usage
if __name__ == "__main__":
    k = __default__["fasta"]["k"]
    query_sequence = __default__["fasta"]["query_sequence"]
    target_sequence = __default__["fasta"]["target_sequence"]

    # Run the energy benchmark
    run_energy_benchmark(k, query_sequence, target_sequence)

    # Run the time benchmark
    run_time_benchmark(k, query_sequence, target_sequence)
