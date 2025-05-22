// n_queens.c
// gcc -shared -o libnqueens.so -fPIC n_queens.c

#include <stdlib.h>
#include <string.h>

int** allocate_board(int n) {
    int** board = (int**)malloc(n * sizeof(int*));
    for (int i = 0; i < n; i++) {
        board[i] = (int*)calloc(n, sizeof(int));
    }
    return board;
}

void free_board(int** board, int n) {
    for (int i = 0; i < n; i++) {
        free(board[i]);
    }
    free(board);
}

int is_safe(int** board, int row, int col, int n) {
    for (int i = 0; i < row; i++)
        if (board[i][col]) return 0;

    for (int i = row-1, j = col-1; i>=0 && j>=0; i--, j--)
        if (board[i][j]) return 0;

    for (int i = row-1, j = col+1; i>=0 && j<n; i--, j++)
        if (board[i][j]) return 0;

    return 1;
}

void copy_solution(int*** solutions, int** board, int* solution_count, int n) {
    int** sol = allocate_board(n);
    for (int i = 0; i < n; i++)
        memcpy(sol[i], board[i], n * sizeof(int));
    solutions[*solution_count] = sol;
    (*solution_count)++;
}

void solve(int** board, int row, int n, int*** solutions, int* solution_count) {
    if (row == n) {
        copy_solution(solutions, board, solution_count, n);
        return;
    }
    for (int col = 0; col < n; col++) {
        if (is_safe(board, row, col, n)) {
            board[row][col] = 1;
            solve(board, row + 1, n, solutions, solution_count);
            board[row][col] = 0;
        }
    }
}

int solve_n_queens(int n, int**** out_solutions) {
    int** board = allocate_board(n);
    // For n = 12, there are 14200 solutions
    int*** solutions = (int***)malloc(15000 * sizeof(int**));
    int count = 0;
    solve(board, 0, n, solutions, &count);
    free_board(board, n);
    *out_solutions = solutions;
    return count;
}

void free_solutions(int*** solutions, int count, int n) {
    for (int i = 0; i < count; i++) {
        for (int j = 0; j < n; j++) {
            free(solutions[i][j]);
        }
        free(solutions[i]);
    }
    free(solutions);
}
