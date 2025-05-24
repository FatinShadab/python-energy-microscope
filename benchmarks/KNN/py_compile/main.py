import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../../")))

from energy_module.decorator import measure_energy_to_csv
from time_modules.decorator import measure_time_to_csv
from input import __default__

from typing import List, Tuple, Dict
import math
import random
from collections import Counter


class KNN:
    def __init__(self, k: int = 3, mode: str = "classification") -> None:
        """
        Initializes the K-Nearest Neighbors (KNN) model.

        :param k: Number of nearest neighbors to consider.
        :param mode: Either "classification" or "regression" mode.
        """
        if k <= 0:
            raise ValueError("k must be a positive integer")
        if mode not in ("classification", "regression"):
            raise ValueError("mode must be either 'classification' or 'regression'")
        
        self.k = k
        self.mode = mode
        self.data: List[Tuple[List[float], float]] = []

    def fit(self, X: List[List[float]], y: List[float]) -> None:
        """
        Stores the training data.

        :param X: List of feature vectors.
        :param y: Corresponding labels or values.
        """
        if len(X) != len(y):
            raise ValueError("Feature and label lists must have the same length")
        
        self.data = list(zip(X, y))

    def _euclidean_distance(self, point1: List[float], point2: List[float]) -> float:
        """
        Computes the Euclidean distance between two points.
        
        :param point1: First data point.
        :param point2: Second data point.
        :return: Euclidean distance.
        """
        return math.sqrt(sum((p1 - p2) ** 2 for p1, p2 in zip(point1, point2)))

    def predict(self, X: List[List[float]]) -> List[float]:
        """
        Predicts the class or value for given input data.

        :param X: List of feature vectors.
        :return: Predicted labels or values.
        """
        return [self._predict_single(x) for x in X]

    def _predict_single(self, x: List[float]) -> float:
        """
        Predicts the class or value for a single input data point.

        :param x: Feature vector.
        :return: Predicted label or value.
        """
        distances: List[Tuple[float, float]] = [(self._euclidean_distance(x, features), label) for features, label in self.data]
        distances.sort(key=lambda d: d[0])
        k_nearest_neighbors = distances[:self.k]
        
        if self.mode == "classification":
            labels = [label for _, label in k_nearest_neighbors]
            return Counter(labels).most_common(1)[0][0]
        else:  # regression
            return sum(label for _, label in k_nearest_neighbors) / self.k

def driver(num_samples: int, num_features: int, k: int):
    # Generate a large dataset for CPU and memory profiling
    num_samples = num_samples
    num_features = num_features

    X_train = [[random.uniform(0, 100) for _ in range(num_features)] for _ in range(num_samples)]
    y_train_classification = [random.randint(0, 1) for _ in range(num_samples)]
    y_train_regression = [random.uniform(0, 100) for _ in range(num_samples)]

    # Classification Example
    knn_classifier = KNN(k=5, mode="classification")
    knn_classifier.fit(X_train, y_train_classification)
    prediction_classification = knn_classifier.predict([[random.uniform(0, 100) for _ in range(num_features)]])
    print("Classification Prediction:", prediction_classification)

    # Regression Example
    knn_regressor = KNN(k=5, mode="regression")
    knn_regressor.fit(X_train, y_train_regression)
    prediction_regression = knn_regressor.predict([[random.uniform(0, 100) for _ in range(num_features)]])
    print("Regression Prediction:", prediction_regression)
    # Note: The above example generates random data for demonstration purposes.
    
@measure_energy_to_csv(n=__default__["knn"]["test_n"], csv_filename="knn_pycompile")
def run_energy_benchmark(num_samples: int, num_features: int, k: int) -> None:
    driver(num_samples, num_features, k)

@measure_time_to_csv(n=__default__["knn"]["test_n"], csv_filename="knn_pycompile")
def run_time_benchmark(num_samples: int, num_features: int, k: int) -> None:
    driver(num_samples, num_features, k)
    

if __name__ == "__main__":
    num_samples = __default__["knn"]["num_samples"]
    num_features = __default__["knn"]["num_features"]
    k = __default__["knn"]["k"]

    run_energy_benchmark(num_samples, num_features, k)
    run_time_benchmark(num_samples, num_features, k)
