# cython: boundscheck=False
# cython: wraparound=False
from libc.math cimport sqrt
from typing import List
cimport cython

@cython.boundscheck(False)
@cython.wraparound(False)
cpdef List[float] multiply_matrix_vector(List[List[object]] matrix, List[object] vector):
    cdef int rows = len(matrix)
    cdef int cols = len(vector)
    cdef List[float] result = [0.0] * rows
    cdef int i, j
    cdef double s

    for i in range(rows):
        s = 0.0
        for j in range(cols):
            s += float(matrix[i][j]) * float(vector[j])
        result[i] = s

    return result

@cython.boundscheck(False)
@cython.wraparound(False)
cpdef double spectral_norm(List[List[object]] matrix, int iterations=10):
    cdef int n = len(matrix)
    cdef List[float] u = [1.0] * n
    cdef List[float] v
    cdef List[float] temp
    cdef double norm
    cdef int i, j

    for _ in range(iterations):
        v = multiply_matrix_vector(matrix, u)

        # Transpose manually
        transposed = [[matrix[j][i] for j in range(n)] for i in range(n)]

        u = multiply_matrix_vector(transposed, v)

        # Normalize
        norm = sqrt(sum(x * x for x in u))
        u = [x / norm for x in u]

    # Final spectral norm computation
    temp = multiply_matrix_vector(matrix, u)
    return sqrt(sum(temp[i] * u[i] for i in range(n)))
