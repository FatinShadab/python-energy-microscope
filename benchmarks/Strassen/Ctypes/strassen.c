#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int* safe_malloc(size_t size) {
    int* ptr = malloc(size);
    if (!ptr) {
        perror("Memory allocation failed");
        exit(EXIT_FAILURE);
    }
    return ptr;
}

void add(int* A, int* B, int* C, int size) {
    for (int i = 0; i < size * size; ++i)
        C[i] = A[i] + B[i];
}

void subtract(int* A, int* B, int* C, int size) {
    for (int i = 0; i < size * size; ++i)
        C[i] = A[i] - B[i];
}

void strassen(int* A, int* B, int* C, int size) {
    if (size == 1) {
        C[0] = A[0] * B[0];
        return;
    }

    int newSize = size / 2;
    int memSize = newSize * newSize * sizeof(int);

    int* A11 = safe_malloc(memSize); int* A12 = safe_malloc(memSize);
    int* A21 = safe_malloc(memSize); int* A22 = safe_malloc(memSize);
    int* B11 = safe_malloc(memSize); int* B12 = safe_malloc(memSize);
    int* B21 = safe_malloc(memSize); int* B22 = safe_malloc(memSize);
    int* M1  = safe_malloc(memSize); int* M2  = safe_malloc(memSize);
    int* M3  = safe_malloc(memSize); int* M4  = safe_malloc(memSize);
    int* M5  = safe_malloc(memSize); int* M6  = safe_malloc(memSize);
    int* M7  = safe_malloc(memSize); int* T1  = safe_malloc(memSize);
    int* T2  = safe_malloc(memSize);

    for (int i = 0; i < newSize; ++i) {
        for (int j = 0; j < newSize; ++j) {
            int idx = i * newSize + j;
            int iA = i * size + j;
            int iB = i * size + j + newSize;
            int iC = (i + newSize) * size + j;
            int iD = (i + newSize) * size + j + newSize;

            A11[idx] = A[iA];
            A12[idx] = A[iB];
            A21[idx] = A[iC];
            A22[idx] = A[iD];

            B11[idx] = B[iA];
            B12[idx] = B[iB];
            B21[idx] = B[iC];
            B22[idx] = B[iD];
        }
    }

    add(A11, A22, T1, newSize); add(B11, B22, T2, newSize); strassen(T1, T2, M1, newSize);
    add(A21, A22, T1, newSize); strassen(T1, B11, M2, newSize);
    subtract(B12, B22, T1, newSize); strassen(A11, T1, M3, newSize);
    subtract(B21, B11, T1, newSize); strassen(A22, T1, M4, newSize);
    add(A11, A12, T1, newSize); strassen(T1, B22, M5, newSize);
    subtract(A21, A11, T1, newSize); add(B11, B12, T2, newSize); strassen(T1, T2, M6, newSize);
    subtract(A12, A22, T1, newSize); add(B21, B22, T2, newSize); strassen(T1, T2, M7, newSize);

    for (int i = 0; i < newSize; ++i) {
        for (int j = 0; j < newSize; ++j) {
            int idx = i * newSize + j;
            int C11 = M1[idx] + M4[idx] - M5[idx] + M7[idx];
            int C12 = M3[idx] + M5[idx];
            int C21 = M2[idx] + M4[idx];
            int C22 = M1[idx] - M2[idx] + M3[idx] + M6[idx];

            C[i * size + j] = C11;
            C[i * size + j + newSize] = C12;
            C[(i + newSize) * size + j] = C21;
            C[(i + newSize) * size + j + newSize] = C22;
        }
    }

    free(A11); free(A12); free(A21); free(A22);
    free(B11); free(B12); free(B21); free(B22);
    free(M1);  free(M2);  free(M3);  free(M4);
    free(M5);  free(M6);  free(M7);
    free(T1);  free(T2);
}
