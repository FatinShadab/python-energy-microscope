import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../")))

from energy_module.decorator import measure_energy_to_csv
from time_modules.decorator import measure_time_to_csv
from input import __default__

import ctypes
import numpy as np
import random
from typing import List

# Load the compiled shared library
lib = ctypes.CDLL('./libknn.so')  # Ensure this path is correct for your system

# Define function signature
lib.knn_predict.argtypes = [
    ctypes.POINTER(ctypes.c_double),  # train_X
    ctypes.POINTER(ctypes.c_double),  # train_y
    ctypes.c_int, ctypes.c_int,       # num_samples, num_features
    ctypes.POINTER(ctypes.c_double),  # input
    ctypes.c_int,                     # k
    ctypes.POINTER(ctypes.c_double)   # output prediction
]

def knn_predict(train_X: List[List[float]], train_y: List[float], input_vector: List[float], k: int) -> float:
    num_samples = len(train_X)
    num_features = len(train_X[0])

    flat_X = np.array(train_X, dtype=np.float64).flatten()
    arr_y = np.array(train_y, dtype=np.float64)
    input_arr = np.array(input_vector, dtype=np.float64)

    result = ctypes.c_double()
    lib.knn_predict(
        flat_X.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
        arr_y.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
        num_samples,
        num_features,
        input_arr.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
        k,
        ctypes.byref(result)
    )

    return result.value

def driver(num_samples: int, num_features: int, k: int):
    X_train = [[random.uniform(0, 100) for _ in range(num_features)] for _ in range(num_samples)]
    y_train = [random.uniform(0, 100) for _ in range(num_samples)]
    input_vector = [random.uniform(0, 100) for _ in range(num_features)]

    prediction = knn_predict(X_train, y_train, input_vector, k)
    print("Regression Prediction (ctypes):", prediction)

@measure_energy_to_csv(n=__default__["knn"]["test_n"], csv_filename="knn_ctypes")
def run_energy_benchmark(num_samples: int, num_features: int, k: int) -> None:
    driver(num_samples, num_features, k)

@measure_time_to_csv(n=__default__["knn"]["test_n"], csv_filename="knn_ctypes")
def run_time_benchmark(num_samples: int, num_features: int, k: int) -> None:
    driver(num_samples, num_features, k)

if __name__ == "__main__":
    num_samples = __default__["knn"]["num_samples"]
    num_features = __default__["knn"]["num_features"]
    k = __default__["knn"]["k"]

    run_energy_benchmark(num_samples, num_features, k)
    run_time_benchmark(num_samples, num_features, k)
