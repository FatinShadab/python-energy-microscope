# cython: boundscheck=False, wraparound=False, nonecheck=False, cdivision=True
from libc.math cimport sqrt
from libc.stdlib cimport malloc, free
from collections import Counter
from cython.view cimport array as cvarray
from cython.operator cimport dereference as deref


cdef class KNN:
    cdef int k
    cdef str mode
    cdef list data

    def __init__(self, int k=3, str mode="classification"):
        if k <= 0:
            raise ValueError("k must be a positive integer")
        if mode not in ("classification", "regression"):
            raise ValueError("mode must be either 'classification' or 'regression'")

        self.k = k
        self.mode = mode
        self.data = []

    def fit(self, list X, list y):
        if len(X) != len(y):
            raise ValueError("Feature and label lists must have the same length")
        self.data = list(zip(X, y))

    cdef double _euclidean_distance(self, list point1, list point2):
        cdef Py_ssize_t i, n = len(point1)
        cdef double s = 0.0
        for i in range(n):
            s += (point1[i] - point2[i]) ** 2
        return sqrt(s)

    cpdef list predict(self, list X):
        cdef list predictions = []
        for x in X:
            predictions.append(self._predict_single(x))
        return predictions

    cdef float _predict_single(self, list x):
        cdef list distances = []
        cdef double d
        for features, label in self.data:
            d = self._euclidean_distance(x, features)
            distances.append((d, label))
        distances.sort(key=lambda d: d[0])
        cdef list k_nearest_neighbors = distances[:self.k]
        
        if self.mode == "classification":
            labels = [label for _, label in k_nearest_neighbors]
            return Counter(labels).most_common(1)[0][0]
        else:  # regression
            return sum(label for _, label in k_nearest_neighbors) / self.k
