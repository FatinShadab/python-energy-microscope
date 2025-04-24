// knn.c
#include <math.h>
#include <stdlib.h>

double euclidean_distance(double* a, double* b, int size) {
    double sum = 0.0;
    for (int i = 0; i < size; i++) {
        double diff = a[i] - b[i];
        sum += diff * diff;
    }
    return sqrt(sum);
}

void knn_predict(double* train_X, double* train_y, int num_samples, int num_features,
                 double* input, int k, double* out_prediction) {
    double* distances = (double*) malloc(sizeof(double) * num_samples);
    int* indices = (int*) malloc(sizeof(int) * num_samples);

    for (int i = 0; i < num_samples; i++) {
        distances[i] = euclidean_distance(input, &train_X[i * num_features], num_features);
        indices[i] = i;
    }

    // Simple selection sort for k smallest distances
    for (int i = 0; i < k; i++) {
        for (int j = i + 1; j < num_samples; j++) {
            if (distances[j] < distances[i]) {
                double tmp_d = distances[i]; distances[i] = distances[j]; distances[j] = tmp_d;
                int tmp_i = indices[i]; indices[i] = indices[j]; indices[j] = tmp_i;
            }
        }
    }

    double sum = 0.0;
    for (int i = 0; i < k; i++) {
        sum += train_y[indices[i]];
    }

    *out_prediction = sum / k;

    free(distances);
    free(indices);
}
