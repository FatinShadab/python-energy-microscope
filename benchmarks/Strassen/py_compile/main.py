import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../")))

from energy_module.decorator import measure_energy_to_csv
from time_modules.decorator import measure_time_to_csv
from input import __default__

from typing import List

def add_matrices(A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
    """Adds two matrices A and B."""
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def subtract_matrices(A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
    """Subtracts matrix B from A."""
    return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def split_matrix(A: List[List[int]]) -> List[List[List[int]]]:
    """Splits a matrix into four submatrices."""
    mid = len(A) // 2
    A11 = [row[:mid] for row in A[:mid]]
    A12 = [row[mid:] for row in A[:mid]]
    A21 = [row[:mid] for row in A[mid:]]
    A22 = [row[mid:] for row in A[mid:]]
    return [A11, A12, A21, A22]

def merge_matrices(C11: List[List[int]], C12: List[List[int]], C21: List[List[int]], C22: List[List[int]]) -> List[List[int]]:
    """Merges four submatrices into a single matrix."""
    n = len(C11)
    return [C11[i] + C12[i] for i in range(n)] + [C21[i] + C22[i] for i in range(n)]

def strassen_multiplication(A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
    """Performs matrix multiplication using Strassen's algorithm."""
    n = len(A)
    if n == 1:
        return [[A[0][0] * B[0][0]]]
    
    # Splitting matrices into quadrants
    A11, A12, A21, A22 = split_matrix(A)
    B11, B12, B21, B22 = split_matrix(B)
    
    # Computing the seven Strassen submatrices
    M1 = strassen_multiplication(add_matrices(A11, A22), add_matrices(B11, B22))
    M2 = strassen_multiplication(add_matrices(A21, A22), B11)
    M3 = strassen_multiplication(A11, subtract_matrices(B12, B22))
    M4 = strassen_multiplication(A22, subtract_matrices(B21, B11))
    M5 = strassen_multiplication(add_matrices(A11, A12), B22)
    M6 = strassen_multiplication(subtract_matrices(A21, A11), add_matrices(B11, B12))
    M7 = strassen_multiplication(subtract_matrices(A12, A22), add_matrices(B21, B22))
    
    # Computing the final quadrants of result matrix C
    C11 = add_matrices(subtract_matrices(add_matrices(M1, M4), M5), M7)
    C12 = add_matrices(M3, M5)
    C21 = add_matrices(M2, M4)
    C22 = add_matrices(subtract_matrices(add_matrices(M1, M3), M2), M6)
    
    return merge_matrices(C11, C12, C21, C22)

def main(A, B) -> None:
    """
    Main function to perform Strassen's matrix multiplication.
    
    Args:
        A (List[List[int]]): First matrix.
        B (List[List[int]]): Second matrix.
    """
    result = strassen_multiplication(A, B)
    for row in result:
        print(row)
        
@measure_energy_to_csv(n=__default__["strassen"]["test_n"], csv_filename="strassen_pycompile")
def run_energy_benchmark(A: List[List[int]], B: List[List[int]]) -> None:
    """
    Run the energy benchmark for Strassen's matrix multiplication.
    
    Args:
        A (List[List[int]]): First matrix.
        B (List[List[int]]): Second matrix.
    """
    main(A, B)
    
@measure_time_to_csv(n=__default__["strassen"]["test_n"], csv_filename="strassen_pycompile")
def run_time_benchmark(A: List[List[int]], B: List[List[int]]) -> None:
    """
    Run the time benchmark for Strassen's matrix multiplication.
    
    Args:
        A (List[List[int]]): First matrix.
        B (List[List[int]]): Second matrix.
    """
    main(A, B)


if __name__ == "__main__":
    A = __default__["strassen"]["A"]
    B = __default__["strassen"]["B"]
    
    # Run the benchmarks
    run_energy_benchmark(A, B)
    run_time_benchmark(A, B)
