import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../../")))

from energy_module.decorator import measure_energy_to_csv
from time_modules.decorator import measure_time_to_csv
from input import __default__

import math
from typing import List

def multiply_matrix_vector(matrix: List[List[int]], vector):
    """
    Multiplies a matrix with a vector.

    This function performs a matrix-vector multiplication, which is
    essential for the power iteration method to compute the spectral norm.

    Args:
    matrix (list of list of floats): The matrix to be multiplied.
    vector (list of floats): The vector to be multiplied with the matrix.

    Returns:
    list of floats: The resulting vector after the matrix-vector multiplication.
    """
    return [sum(row[i] * vector[i] for i in range(len(vector))) for row in matrix]

def spectral_norm(matrix: List[List[int]], iterations=10):
    """
    Computes the spectral norm (largest singular value) of a matrix using the power method.

    The power method is an iterative algorithm that computes the dominant eigenvalue of a matrix.
    The spectral norm is the largest singular value of the matrix, which is the square root of 
    the largest eigenvalue of the matrix A^T * A.

    Steps:
    1. Initialize a random vector.
    2. Perform matrix-vector multiplication and its transpose to converge on the dominant eigenvalue.
    3. Normalize the resulting vector for numerical stability.
    4. Repeat the process for a fixed number of iterations.
    5. Compute the spectral norm as the square root of the resulting value.

    Args:
    matrix (list of list of floats): The matrix whose spectral norm is to be calculated.
    iterations (int): The number of iterations to run the power method (default is 10).

    Returns:
    float: The spectral norm (largest singular value) of the matrix.
    """
    n = len(matrix)
    u = [1.0] * n  # Initial vector with all elements as 1.0

    for _ in range(iterations):
        # Step 2: Perform matrix-vector multiplication
        v = multiply_matrix_vector(matrix, u)
        
        # Step 3: Perform transpose of matrix and multiply with the result
        u = multiply_matrix_vector(list(zip(*matrix)), v)  # Transpose matrix multiplication
        
        # Step 4: Normalize the resulting vector
        norm = math.sqrt(sum(x**2 for x in u))
        u = [x / norm for x in u]

    # Step 5: Calculate the spectral norm (largest singular value)
    return math.sqrt(sum(multiply_matrix_vector(matrix, u)[i] * u[i] for i in range(n)))

@measure_energy_to_csv(n=__default__["spectral-norm"]["test_n"], csv_filename="spectral_norm_pycompile")
def run_energy_benchmark(matrix: List[List[int]], iterations=10) -> None:
    spectral_norm(matrix, iterations)

@measure_time_to_csv(n=__default__["spectral-norm"]["test_n"], csv_filename="spectral_norm_pycompile")
def run_time_benchmark(matrix: List[List[int]], iterations=10) -> None:
    spectral_norm(matrix, iterations)


if __name__ == "__main__":
    # Example matrix
    A = __default__["spectral-norm"]["matrix"]
    itr = __default__["spectral-norm"]["iterations"]

    # Run the benchmarks
    run_energy_benchmark(A, itr)
    run_time_benchmark(A, itr)
