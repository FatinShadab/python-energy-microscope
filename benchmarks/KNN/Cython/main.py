import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../")))

from energy_module.decorator import measure_energy_to_csv
from time_modules.decorator import measure_time_to_csv
from input import __default__

import random
from raw import KNN

def driver(num_samples: int, num_features: int, k: int) -> None:
    # Generate a large dataset
    num_samples = num_samples
    num_features = num_features
    k = k

    X_train = [[random.uniform(0, 100) for _ in range(num_features)] for _ in range(num_samples)]
    y_train_classification = [random.randint(0, 1) for _ in range(num_samples)]
    y_train_regression = [random.uniform(0, 100) for _ in range(num_samples)]

    # Classification Example
    knn_classifier = KNN(k=k, mode="classification")
    knn_classifier.fit(X_train, y_train_classification)
    prediction_classification = knn_classifier.predict([[random.uniform(0, 100) for _ in range(num_features)]])
    print("Classification Prediction:", prediction_classification)

    # Regression Example
    knn_regressor = KNN(k=k, mode="regression")
    knn_regressor.fit(X_train, y_train_regression)
    prediction_regression = knn_regressor.predict([[random.uniform(0, 100) for _ in range(num_features)]])
    print("Regression Prediction:", prediction_regression)

@measure_energy_to_csv(n=__default__["knn"]["test_n"], csv_filename="binary_trees_cython")
def run_energy_benchmark(num_samples: int, num_features: int, k: int) -> None:
    driver(num_samples, num_features, k)

@measure_time_to_csv(n=__default__["knn"]["test_n"], csv_filename="binary_trees_cython")
def run_time_benchmark(num_samples: int, num_features: int, k: int) -> None:
    driver(num_samples, num_features, k)


if __name__ == "__main__":
    num_samples = __default__["knn"]["num_samples"]
    num_features = __default__["knn"]["num_features"]
    k = __default__["knn"]["k"]

    run_energy_benchmark(num_samples, num_features, k)
    run_time_benchmark(num_samples, num_features, k)
