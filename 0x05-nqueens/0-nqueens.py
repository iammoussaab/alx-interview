#!/usr/bin/python3
"""N Queens"""
import sys


def print_board(board, n):
    """Print allocated positions of the queens"""
    result = []
    for i in range(n):
        result.append([i, board[i]])
    print(result)


def is_position_safe(board, row, col):
    """Check if it's safe to place a queen at board[row] = col"""
    for i in range(row):
        # Check column and diagonal conflicts
        if board[i] == col or abs(board[i] - col) == abs(i - row):
            return False
    return True


def safe_positions(board, row, n):
    """Find all safe positions for queens and print solutions"""
    if row == n:
        print_board(board, n)
    else:
        for col in range(n):
            if is_position_safe(board, row, col):
                board[row] = col
                safe_positions(board, row + 1, n)
                board[row] = -1  # Reset position (backtrack)


def create_board(size):
    """Generates the board"""
    return [-1] * size


if len(sys.argv) != 2:
    print("Usage: nqueens N")
    exit(1)

try:
    n = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    exit(1)

if n < 4:
    print("N must be at least 4")
    exit(1)

board = create_board(n)
safe_positions(board, 0, n)
