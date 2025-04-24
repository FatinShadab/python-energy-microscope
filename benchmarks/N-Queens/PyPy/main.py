import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../")))

from energy_module.decorator import measure_energy_to_csv
from time_modules.decorator import measure_time_to_csv
from input import __default__

"""
Solving Approach in the Code ->
--------------------------------

# is_safe(board, row, col, n):
    - Ensures that placing a queen at board[row][col] does not violate constraints.
    - Checks for conflicts in the column, left diagonal, and right diagonal.

# solve_n_queens(board, row, n, solutions):
    - Recursively places queens in each row.
    - Calls is_safe before placing a queen.
    - Uses backtracking to undo incorrect placements.

# n_queens(n):
    - Initializes an empty board and starts the recursive backtracking process.
    - Stores and returns all possible solutions.

# print_solution(board):
    - Converts the numerical board representation into a visual format where Q 
    represents a queen and . represents an empty space.
"""

def print_solution(board):
    """
    Prints the N-Queens board configuration.
    """
    for row in board:
        print(" ".join("Q" if cell else "." for cell in row))
    print("\n")

def is_safe(board, row, col, n):
    """
    Checks if placing a queen at board[row][col] is safe.
    
    Args:
        board (list): The current N-Queens board.
        row (int): The row index to check.
        col (int): The column index to check.
        n (int): The size of the board.
    
    Returns:
        bool: True if it's safe, False otherwise.
    """
    # Check this column on upper side
    for i in range(row):
        if board[i][col]:
            return False
    
    # Check upper diagonal (left)
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j]:
            return False
    
    # Check upper diagonal (right)
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j]:
            return False
    
    return True

def solve_n_queens(board, row, n, solutions):
    """
    Solves the N-Queens problem using backtracking.
    
    Args:
        board (list): The current N-Queens board.
        row (int): The current row being considered.
        n (int): The size of the board.
        solutions (list): List to store valid solutions.
    """
    if row == n:
        solutions.append([row[:] for row in board])
        return
    
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1  # Place queen
            solve_n_queens(board, row + 1, n, solutions)
            board[row][col] = 0  # Backtrack

def n_queens(n):
    """
    Finds all possible solutions for the N-Queens problem.
    
    Args:
        n (int): The size of the board.
    
    Returns:
        list: A list of solutions where each solution is a board configuration.
    """
    board = [[0] * n for _ in range(n)]
    solutions = []
    solve_n_queens(board, 0, n, solutions)
    return solutions

def main(n):
    """
    Main function to execute the N-Queens solver.
    
    Args:
        n (int): The size of the board.
    """
    solutions = n_queens(n)
    print(f"Total solutions for {n}-Queens: {len(solutions)}")
    for sol in solutions:
        print_solution(sol)
        
@measure_energy_to_csv(n=__default__["n-queens"]["test_n"], csv_filename="n_queens_pypy")
def run_energy_benchmark(n: int) -> None:
    main(n)

@measure_time_to_csv(n=__default__["n-queens"]["test_n"], csv_filename="n_queens_pypy")
def run_time_benchmark(n: int) -> None:
    main(n)

# Example usage
if __name__ == "__main__":
    N = __default__["n-queens"]["n"]
    
    # Run the energy benchmark
    run_energy_benchmark(N)
    # Run the time benchmark
    run_time_benchmark(N)
