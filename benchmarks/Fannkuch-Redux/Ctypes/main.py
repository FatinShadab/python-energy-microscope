import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../")))

from energy_module.decorator import measure_energy_to_csv
from time_modules.decorator import measure_time_to_csv
from input import __default__

import ctypes

# Load shared library
lib = ctypes.CDLL('./fannkuch.so')  # or 'fannkuch.dll' on Windows

# Prepare argument types
lib.fannkuch_redux.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int)]

# Prepare return values
max_flips = ctypes.c_int()
count_max_flips = ctypes.c_int()

def driver(n: int) -> None:
    """
    Driver function to call the C function and print results.
    
    :param n: The size of the permutation.
    """
    # Call the C function
    lib.fannkuch_redux(n, ctypes.byref(max_flips), ctypes.byref(count_max_flips))
    
    print(f"Max flips: {max_flips.value}")
    print(f"Count of max flips: {count_max_flips.value}")
    
    
@measure_energy_to_csv(n=__default__["fannkuch_redux"]["test_n"], csv_filename="fannkuch_redux_ctypes")
def run_energy_benchmark(n: int) -> None:
    driver(n)

@measure_time_to_csv(n=__default__["fannkuch_redux"]["test_n"], csv_filename="fannkuch_redux_ctypes")
def run_time_benchmark(n: int) -> None:
    driver(n)
    

if __name__ == "__main__":
    n = __default__["fannkuch_redux"]["n"]
    run_energy_benchmark(n)
    run_time_benchmark(n)
