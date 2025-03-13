# Spectral Norm Algorithm

The **Spectral Norm** of a matrix measures the largest singular value, which is crucial in numerical analysis, signal processing, and machine learning. It helps assess matrix stability and is computed using the **Power Method**, an iterative algorithm for finding dominant eigenvalues.


## Algorithm Explanation

The **Spectral Norm** of a matrix \( A \) is defined as:

\[
\| A \| = \max \{ \sigma_1, \sigma_2, ..., \sigma_n \}
\]

where \( \sigma_i \) are the singular values of \( A \). It is equivalent to the **largest eigenvalue of \( A^T A \) under square root**.

We approximate it using the **Power Iteration Method**:

1. **Initialize a random vector** \( u \).
2. **Multiply \( u \) by the matrix \( A \)** to get \( v = A \cdot u \).
3. **Multiply \( v \) by the transpose of \( A \) ( \( A^T \) )** to get a new vector \( u' = A^T \cdot v \).
4. **Normalize \( u' \)** to maintain numerical stability.
5. **Repeat steps 2-4** for several iterations.
6. Compute the spectral norm as:

   \[
   \| A \| \approx \sqrt{ (A \cdot u) \cdot u }
   \]

## **Time Complexity**
The power iteration method primarily involves matrix-vector multiplication at each iteration. Let \( n \) be the size of the matrix:

- **Matrix-vector multiplication** takes \( O(n^2) \) time.
- The iteration runs for a fixed number of iterations \( k \) (typically small, e.g., 10-20 iterations).

Thus, the **overall time complexity** is:

\[
O(k \cdot n^2)
\]

where \( k \) is the number of iterations, and \( n \) is the number of rows/columns in the square matrix.

## **Space Complexity**
The space complexity is determined by the storage requirements for the matrix and vectors:

- **Matrix** requires \( O(n^2) \) space.
- **Vectors** \( u \) and \( v \) each require \( O(n) \) space.

Thus, the **overall space complexity** is:

\[
O(n^2)
\]

where \( n \) is the size of the matrix.


## Implementation Approach

- **Matrix-Vector Multiplication**: Efficiently multiplies a matrix with a vector.
- **Power Iteration Method**: Uses repeated multiplications to converge to the dominant eigenvalue.
- **Normalization**: Ensures numerical stability.
- **Efficient Computation**: Uses Python lists and list comprehensions.

## Applications
- Machine Learning: Regularization and stability analysis.
- Graph Theory: Eigenvalue analysis of adjacency matrices.
- Physics & Engineering: Wave propagation, quantum mechanics.

## References
- Golub, G. H., & Van Loan, C. F. (2013). Matrix Computations.
- Trefethen, L. N., & Bau, D. (1997). Numerical Linear Algebra.