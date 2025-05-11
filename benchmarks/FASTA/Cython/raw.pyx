# raw.pyx
import numpy as np
cimport numpy as np

from typing import Tuple, List

DTYPE = np.int32
ctypedef np.int32_t DTYPE_t

# Function to generate k-tuples
def generate_k_tuples(str sequence, int k) -> list:
    return [sequence[i:i+k] for i in range(len(sequence) - k + 1)]

# Function to calculate alignment using dynamic programming
def extend_alignment(str query, str target, int start_q, int start_t, int k,
                     int match=1, int mismatch=-1, int gap=-2) -> Tuple[int, str, str]:
    cdef int n = len(query)
    cdef int m = len(target)

    # Allocate DP matrix using NumPy for performance
    cdef np.ndarray[DTYPE_t, ndim=2] dp = np.zeros((n + 1, m + 1), dtype=DTYPE)

    cdef int i, j, score, max_score = 0
    cdef int max_i = 0, max_j = 0

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if query[i - 1] == target[j - 1]:
                score = match
            else:
                score = mismatch

            dp[i, j] = max(
                0,
                dp[i - 1, j - 1] + score,
                dp[i - 1, j] + gap,
                dp[i, j - 1] + gap
            )

            if dp[i, j] > max_score:
                max_score = dp[i, j]
                max_i, max_j = i, j

    # Traceback
    aligned_query = []
    aligned_target = []
    i, j = max_i, max_j

    while i > 0 and j > 0 and dp[i, j] > 0:
        if dp[i, j] == dp[i - 1, j - 1] + (match if query[i - 1] == target[j - 1] else mismatch):
            aligned_query.append(query[i - 1])
            aligned_target.append(target[j - 1])
            i -= 1
            j -= 1
        elif dp[i, j] == dp[i - 1, j] + gap:
            aligned_query.append(query[i - 1])
            aligned_target.append('-')
            i -= 1
        else:
            aligned_query.append('-')
            aligned_target.append(target[j - 1])
            j -= 1

    aligned_query.reverse()
    aligned_target.reverse()

    return max_score, ''.join(aligned_query), ''.join(aligned_target)

# FASTA alignment algorithm
def fasta_alignment(str query, str target, int k,
                    int match=1, int mismatch=-1, int gap=-2) -> Tuple[int, Tuple[int, int], str, str]:

    query_k_tuples = generate_k_tuples(query, k)
    target_k_tuples = generate_k_tuples(target, k)

    cdef dict hash_table = {}
    cdef int i, target_start

    for i, seq in enumerate(target_k_tuples):
        if seq not in hash_table:
            hash_table[seq] = []
        hash_table[seq].append(i)

    cdef int best_score = 0
    cdef Tuple[int, int] best_alignment = (0, 0)
    cdef str best_aligned_query = ""
    cdef str best_aligned_target = ""
    cdef int score
    cdef str aligned_query, aligned_target

    for i, query_tuple in enumerate(query_k_tuples):
        if query_tuple in hash_table:
            for target_start in hash_table[query_tuple]:
                score, aligned_query, aligned_target = extend_alignment(
                    query, target, i, target_start, k, match, mismatch, gap
                )
                if score > best_score:
                    best_score = score
                    best_alignment = (i, target_start)
                    best_aligned_query = aligned_query
                    best_aligned_target = aligned_target

    return best_score, best_alignment, best_aligned_query, best_aligned_target
