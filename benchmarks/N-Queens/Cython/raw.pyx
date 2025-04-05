# filename: n_queens.pyx

# cython: boundscheck=False
# cython: wraparound=False
# cython: initializedcheck=False
# cython: language_level=3

from libc.stdlib cimport malloc, free
from libc.string cimport memset
cimport cython

@cython.boundscheck(False)
@cython.wraparound(False)
cdef int is_safe(int[:, :] board, int row, int col, int n):
    cdef int i, j

    for i in range(row):
        if board[i, col]:
            return 0

    for i, j in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
        if board[i, j]:
            return 0

    for i, j in zip(range(row - 1, -1, -1), range(col + 1, n)):
        if board[i, j]:
            return 0

    return 1

@cython.boundscheck(False)
@cython.wraparound(False)
cdef void solve_n_queens(int[:, :] board, int row, int n, list solutions):
    cdef int col, i, j
    if row == n:
        solution = []
        for i in range(n):
            solution.append([board[i, j] for j in range(n)])
        solutions.append(solution)
        return

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row, col] = 1
            solve_n_queens(board, row + 1, n, solutions)
            board[row, col] = 0

@cython.boundscheck(False)
@cython.wraparound(False)
def n_queens(int n):
    """
    Entry point for solving the N-Queens problem in optimized Cython.
    """
    cdef int[:, :] board = cython.view.array(shape=(n, n), itemsize=cython.sizeof(int), format="i")
    cdef int i, j

    # Initialize board with 0s
    for i in range(n):
        for j in range(n):
            board[i, j] = 0

    solutions = []
    solve_n_queens(board, 0, n, solutions)
    return solutions
