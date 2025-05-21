import re
from typing import List, Tuple
from raw import regex_redux
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../")))

from energy_module.decorator import measure_energy_to_csv
from time_modules.decorator import measure_time_to_csv
from input import __default__

@measure_time_to_csv(n=__default__["regex_redux"]["test_n"], csv_filename="regex_redux_pypy")
def run_time_benchmark(file_path: str) -> None:
    """
    Measure and log the time it takes to run the Regex-Redux benchmark.
    """
    regex_redux(file_path)

@measure_energy_to_csv(n=__default__["regex_redux"]["test_n"], csv_filename="regex_redux_pypy")
def run_energy_benchmark(file_path: str) -> None:
    """
    Measure and log the energy consumption of the Regex-Redux benchmark.
    """
    regex_redux(file_path)


if __name__ == "__main__":
    file_path = __default__["regex_redux"]["file_path"]

    # You can change this to driver(file_path) if you want plain output
    run_energy_benchmark(file_path)
    run_time_benchmark(file_path)
