#!/usr/bin/python3
"""N Queens solution finder module.
"""
import sys


solutions = []
"""The list of possible solutions to the N queens problem.
"""
n = 0
"""The size of the chessboard.
"""
board = None
"""The list representing the chessboard for queen placement.
"""


def get_input():
    """Retrieves and validates this program's argument.

    Returns:
        int: The size of the chessboard.
    """
    global n
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    return n


def is_position_safe(board, row, col):
    """Checks if a queen can be safely placed at the given position.

    Args:
        board (list): The board with queen placements.
        row (int): The row index.
        col (int): The column index.

    Returns:
        bool: True if the position is safe, otherwise False.
    """
    for i in range(row):
        # Check column and both diagonals
        if board[i] == col or abs(board[i] - col) == abs(i - row):
            return False
    return True


def solve_nqueens(row):
    """Recursively attempts to solve the N Queens problem.

    Args:
        row (int): The current row to attempt placing a queen.
    """
    global solutions, board, n
    if row == n:
        # If all queens are placed, add the solution
        solutions.append([[i, board[i]] for i in range(n)])
    else:
        for col in range(n):
            if is_position_safe(board, row, col):
                board[row] = col
                solve_nqueens(row + 1)
                # Backtrack
                board[row] = -1


def get_solutions():
    """Sets up the board and starts the solution search."""
    global board, n
    board = [-1] * n
    solve_nqueens(0)


# Main execution
n = get_input()
get_solutions()
for solution in solutions:
    print(solution)
