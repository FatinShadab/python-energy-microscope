from raw import fannkuch_redux
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../")))

from energy_module.decorator import measure_energy_to_csv
from time_modules.decorator import measure_time_to_csv
from input import __default__


def driver(n: int) -> None:
    max_flips, count_max_flips = fannkuch_redux(n)
    print(f"Max flips: {max_flips}")
    print(f"Count of max flips: {count_max_flips}")

@measure_energy_to_csv(n=__default__["fannkuch_redux"]["test_n"], csv_filename="fannkuch_redux_cython")
def run_energy_benchmark(n: int) -> None:
    driver(n)

@measure_time_to_csv(n=__default__["fannkuch_redux"]["test_n"], csv_filename="fannkuch_redux_cython")
def run_time_benchmark(n: int) -> None:
    driver(n)

    
if __name__ == "__main__":
    n = __default__["fannkuch_redux"]["n"]
    run_energy_benchmark(n)
    run_time_benchmark(n)
