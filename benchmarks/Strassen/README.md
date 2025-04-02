# Strassen Algorithm

The Strassen algorithm is an efficient algorithm for matrix multiplication. It was introduced by Volker Strassen in 1969 and is one of the most famous examples of divide-and-conquer algorithms. Strassen's algorithm reduces the number of multiplications required for matrix multiplication compared to the conventional method.

In traditional matrix multiplication, multiplying two matrices of size `n × n` involves `O(n^3)` operations. Strassen's algorithm reduces the time complexity to `O(n^(log2(7))) ≈ O(n^2.81)`, making it faster for large matrices.

## Algorithm

Strassen's matrix multiplication algorithm works by dividing the matrices into smaller submatrices, performing recursive multiplications on them, and combining the results with additions and subtractions.

### Matrix Partitioning
For two matrices `A` and `B`, where each matrix is split into four blocks as:

```
A = | A11  A12 |
    | A21  A22 |

B = | B11  B12 |
    | B21  B22 |
```

The product matrix `C = A × B` is computed as:

```
C = | C11  C12 |
    | C21  C22 |
```

Where:
```
C11 = M1 + M4 - M5 + M7
C12 = M3 + M5
C21 = M2 + M4
C22 = M1 - M2 + M3 + M6
```

The seven intermediate matrices `M1` through `M7` are computed as follows:

```
M1 = (A11 + A22) × (B11 + B22)
M2 = (A21 + A22) × B11
M3 = A11 × (B12 - B22)
M4 = A22 × (B21 - B11)
M5 = (A11 + A12) × B22
M6 = (A21 - A11) × (B11 + B12)
M7 = (A12 - A22) × (B21 + B22)
```

## Pseudocode

```
Function Strassen(A, B):
    if size of A and B is 1x1:
        return A * B

    split A into A11, A12, A21, A22
    split B into B11, B12, B21, B22

    M1 = Strassen(A11 + A22, B11 + B22)
    M2 = Strassen(A21 + A22, B11)
    M3 = Strassen(A11, B12 - B22)
    M4 = Strassen(A22, B21 - B11)
    M5 = Strassen(A11 + A12, B22)
    M6 = Strassen(A21 - A11, B11 + B12)
    M7 = Strassen(A12 - A22, B21 + B22)

    C11 = M1 + M4 - M5 + M7
    C12 = M3 + M5
    C21 = M2 + M4
    C22 = M1 - M2 + M3 + M6

    return the combined matrix C = [C11, C12, C21, C22]
```

## Implementation Approach

1. **Input Matrices:**
   - Accept two square matrices `A` and `B` for multiplication.
   - If the matrices are not square or the sizes are not powers of 2, you can pad them with zeros.

2. **Base Case:**
   - When the matrix size is `1 × 1`, the multiplication is straightforward and can be done directly.

3. **Recursive Step:**
   - Split each matrix into four submatrices (as shown in the pseudocode).
   - Calculate the seven intermediate products `M1` to `M7` recursively.
   - Combine the results to form the resulting matrix.

4. **Matrix Addition and Subtraction:**
   - Use matrix addition and subtraction to combine the results from the intermediate matrices.

5. **Return the Result:**
   - Once all recursive steps are completed, return the final product matrix.

## Time Complexity

The time complexity of Strassen’s algorithm is:

```
O(n^(log2(7))) ≈ O(n^2.81)
```

This is a significant improvement over the standard `O(n^3)` complexity for matrix multiplication.

## Space Complexity

- The space complexity is `O(n^2)`, since we need to store intermediate matrices, which are of size `n × n`.

## References Used for Implementation and Information

- Strassen, V. (1969). *Gaussian elimination is not optimal.* Numerische Mathematik, 13(4), 354-356.
- "Matrix multiplication using Strassen's algorithm." [Wikipedia](https://en.wikipedia.org/wiki/Strassen_algorithm)
- Cormen, T.H., Leiserson, C.E., Rivest, R.L., Stein, C. (2009). *Introduction to Algorithms (3rd ed.).*