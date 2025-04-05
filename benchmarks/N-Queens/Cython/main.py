from raw import n_queens

def print_board(board):
    """
    Prints the N-Queens board in a human-readable format.
    
    Args:
        board (list): The N-Queens board to print.
    """
    for row in board:
        print(" ".join("Q" if cell else "." for cell in row))
    print()


if __name__ == "__main__":
    N = 8
    solutions = n_queens(N)

    print(f"Total solutions for {N}-Queens: {len(solutions)}")
    for sol in solutions:
        print_board(sol)
