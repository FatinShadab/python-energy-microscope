import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../")))

from energy_module.decorator import measure_energy_to_csv
from time_modules.decorator import measure_time_to_csv
from input import __default__

import ctypes
from typing import List

# Load the shared library
lib = ctypes.CDLL("./libprime_sieve.so")

# Configure the C function
lib.sieve.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int)]
lib.sieve.restype = ctypes.POINTER(ctypes.c_int)
lib.free_array.argtypes = [ctypes.POINTER(ctypes.c_int)]

def get_primes(n: int) -> List[int]:
    count = ctypes.c_int()
    primes_ptr = lib.sieve(n, ctypes.byref(count))
    
    if not primes_ptr:
        raise MemoryError("Failed to allocate primes")

    # Copy the result to a Python list
    primes = [primes_ptr[i] for i in range(count.value)]

    # Free C memory
    lib.free_array(primes_ptr)

    return primes

@measure_energy_to_csv(n=__default__["sieve"]["test_n"], csv_filename="sieve_ctypes")
def run_energy_benchmark(n: int) -> None:
    get_primes(n)

@measure_time_to_csv(n=__default__["sieve"]["test_n"], csv_filename="sieve_ctypes")
def run_time_benchmark(n: int) -> None:
    get_primes(n)


if __name__ == "__main__":
    n = __default__["sieve"]["n"]
    
    run_energy_benchmark(n)
    run_time_benchmark(n)