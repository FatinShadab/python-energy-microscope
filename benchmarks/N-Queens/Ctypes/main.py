import os
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

# Example
if __name__ == "__main__":
    n = 8
    solutions = solve_n_queens(n)
    print(f"Total solutions: {len(solutions)}")
    for sol in solutions:
        for row in sol:
            print(" ".join("Q" if x else "." for x in row))
        print()
