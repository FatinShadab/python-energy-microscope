import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../")))

from energy_module.decorator import measure_energy_to_csv
from time_modules.decorator import measure_time_to_csv
from input import __default__

import ctypes
from ctypes import POINTER, c_int, byref

if os.name == "nt":
    lib = ctypes.CDLL("n_queens.dll")
else:
    lib = ctypes.CDLL("./libnqueens.so")

# Setup return and argument types
lib.solve_n_queens.argtypes = [c_int, POINTER(POINTER(POINTER(POINTER(c_int))))]
lib.solve_n_queens.restype = c_int

lib.free_solutions.argtypes = [POINTER(POINTER(POINTER(c_int))), c_int, c_int]

def solve_n_queens(n):
    out_solutions = POINTER(POINTER(POINTER(c_int)))()
    count = lib.solve_n_queens(n, byref(out_solutions))

    result = []
    for i in range(count):
        solution = []
        for j in range(n):
            row = [out_solutions[i][j][k] for k in range(n)]
            solution.append(row)
        result.append(solution)

    # Free C memory
    lib.free_solutions(out_solutions, count, n)

    return result

def main(n):
    solutions = solve_n_queens(n)
    print(f"Total solutions: {len(solutions)}")
    for sol in solutions:
        for row in sol:
            print(" ".join("Q" if x else "." for x in row))
        print()
        
@measure_energy_to_csv(n=__default__["n-queens"]["test_n"], csv_filename="n_queens_ctypes")
def run_energy_benchmark(n: int) -> None:
    main(n)

@measure_time_to_csv(n=__default__["n-queens"]["test_n"], csv_filename="n_queens_ctypes")
def run_time_benchmark(n: int) -> None:
    main(n)


if __name__ == "__main__":
    N = __default__["n-queens"]["n"]
   
    # Run the energy benchmark
    run_energy_benchmark(N)
    # Run the time benchmark
    run_time_benchmark(N)
