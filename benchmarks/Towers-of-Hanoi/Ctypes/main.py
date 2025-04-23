import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../")))

import ctypes
from ctypes import c_int, c_char_p
from input import __default__
import argparse
from energy_module.decorator import measure_energy_to_csv
from time_modules.decorator import measure_time_to_csv

# Load the shared library
lib = ctypes.CDLL("./libhanoi.so")

# Declare the argument types for the C function
lib.towers_of_hanoi.argtypes = [c_int, c_char_p, c_char_p, c_char_p]
lib.towers_of_hanoi.restype = None

# Call the C function from Python
def driver(n):
    source = b"A"      # b"A" = byte string
    auxiliary = b"B"
    target = b"C"

    lib.towers_of_hanoi(n, source, auxiliary, target)
    
@measure_energy_to_csv(n=__default__["hanoi"]["test_n"], csv_filename="hanoi_ctypes")
def run_energy_benchmark(n):
    """
    Run the energy benchmark for the Towers of Hanoi problem.
    """
    driver(n)

@measure_time_to_csv(n=__default__["hanoi"]["test_n"], csv_filename="hanoi_ctypes")
def run_time_benchmark(n):
    """
    Run the time benchmark for the Towers of Hanoi problem.
    """
    driver(n)


if __name__ == "__main__":
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Solve the Towers of Hanoi problem.")
    parser.add_argument(
        "-n", "--num_disks", type=int, default=__default__["hanoi"]["n"], 
        help=f"Number of disks (default: {__default__['hanoi']['n']})"
    )
    args = parser.parse_args()

    # Get the number of disks from the arguments or use the default value
    n = args.num_disks
    
    # Run the benchmarks
    run_energy_benchmark(n)
    run_time_benchmark(n)
