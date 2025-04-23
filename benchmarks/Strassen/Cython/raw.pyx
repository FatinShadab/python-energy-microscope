# cython: boundscheck=False
# cython: wraparound=False
# cython: cdivision=True

from cython cimport boundscheck, wraparound
cimport cython
from typing import List

@cython.boundscheck(False)
@cython.wraparound(False)
cpdef list add_matrices(list A, list B):
    cdef int n = len(A)
    cdef int m = len(A[0])
    cdef list C = [[0] * m for _ in range(n)]
    cdef int i, j
    for i in range(n):
        for j in range(m):
            C[i][j] = A[i][j] + B[i][j]
    return C

@cython.boundscheck(False)
@cython.wraparound(False)
cpdef list subtract_matrices(list A, list B):
    cdef int n = len(A)
    cdef int m = len(A[0])
    cdef list C = [[0] * m for _ in range(n)]
    cdef int i, j
    for i in range(n):
        for j in range(m):
            C[i][j] = A[i][j] - B[i][j]
    return C

cpdef tuple split_matrix(list A):
    cdef int n = len(A) // 2
    A11 = [row[:n] for row in A[:n]]
    A12 = [row[n:] for row in A[:n]]
    A21 = [row[:n] for row in A[n:]]
    A22 = [row[n:] for row in A[n:]]
    return A11, A12, A21, A22

cpdef list merge_matrices(list C11, list C12, list C21, list C22):
    cdef int n = len(C11)
    cdef list C = []
    for i in range(n):
        C.append(C11[i] + C12[i])
    for i in range(n):
        C.append(C21[i] + C22[i])
    return C

cpdef list strassen_multiplication(list A, list B):
    cdef int n = len(A)
    if n == 1:
        return [[A[0][0] * B[0][0]]]

    A11, A12, A21, A22 = split_matrix(A)
    B11, B12, B21, B22 = split_matrix(B)

    M1 = strassen_multiplication(add_matrices(A11, A22), add_matrices(B11, B22))
    M2 = strassen_multiplication(add_matrices(A21, A22), B11)
    M3 = strassen_multiplication(A11, subtract_matrices(B12, B22))
    M4 = strassen_multiplication(A22, subtract_matrices(B21, B11))
    M5 = strassen_multiplication(add_matrices(A11, A12), B22)
    M6 = strassen_multiplication(subtract_matrices(A21, A11), add_matrices(B11, B12))
    M7 = strassen_multiplication(subtract_matrices(A12, A22), add_matrices(B21, B22))

    C11 = add_matrices(subtract_matrices(add_matrices(M1, M4), M5), M7)
    C12 = add_matrices(M3, M5)
    C21 = add_matrices(M2, M4)
    C22 = add_matrices(subtract_matrices(add_matrices(M1, M3), M2), M6)

    return merge_matrices(C11, C12, C21, C22)
