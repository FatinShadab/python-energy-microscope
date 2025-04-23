#include <math.h>
#include <stdlib.h>

// Multiply matrix with vector: result = matrix * vector
void matvec_mul(double* result, double* matrix, double* vector, int n) {
    for (int i = 0; i < n; i++) {
        result[i] = 0.0;
        for (int j = 0; j < n; j++) {
            result[i] += matrix[i * n + j] * vector[j];
        }
    }
}

// Compute dot product of two vectors
double dot(double* a, double* b, int n) {
    double s = 0.0;
    for (int i = 0; i < n; i++) {
        s += a[i] * b[i];
    }
    return s;
}

// Normalize a vector (in-place)
void normalize(double* vec, int n) {
    double norm = sqrt(dot(vec, vec, n));
    for (int i = 0; i < n; i++) {
        vec[i] /= norm;
    }
}

// Spectral norm using the power method
__attribute__((visibility("default"))) // Required to export for ctypes on Linux/macOS
double spectral_norm(double* matrix, int n, int iterations) {
    double* u = malloc(sizeof(double) * n);
    double* v = malloc(sizeof(double) * n);
    double* tmp = malloc(sizeof(double) * n);

    for (int i = 0; i < n; i++) {
        u[i] = 1.0;
    }

    for (int it = 0; it < iterations; it++) {
        matvec_mul(v, matrix, u, n);

        // Multiply with transpose(A) * v manually
        for (int i = 0; i < n; i++) {
            tmp[i] = 0.0;
            for (int j = 0; j < n; j++) {
                tmp[i] += matrix[j * n + i] * v[j]; // Transposed index
            }
        }

        for (int i = 0; i < n; i++) {
            u[i] = tmp[i];
        }

        normalize(u, n);
    }

    matvec_mul(tmp, matrix, u, n);
    double result = 0.0;
    for (int i = 0; i < n; i++) {
        result += tmp[i] * u[i];
    }

    free(u);
    free(v);
    free(tmp);

    return sqrt(result);
}
