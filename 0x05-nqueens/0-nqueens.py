#!/usr/bin/python3
"""0. N queens"""
import sys


def is_safe(board, row, col):
    """
    Check if a queen can be placed at the specified position
    Args:
        board: List representing the current state of the board.
        row: Row index of the position to check.
        col: Column index of the position to check.
    Returns:
        True if a queen can be placed at the specified position
    """
    for i in range(row):
        if (
            board[i] == co or
                board[i] - i == col - row or
                board[i] + i == col + row
        ):
            return False
    return True


def solve_nqueens(board, row, n):
    """
    Solve the N Queens problem recursively using backtracking.
    Args:
        board: List representing the current state of the board.
        row: Current row being considered for queen placement.
        n: Size of the board.
    """
    if row == n:
        # All queens have been placed, print the solution
        print(board)
        return

    for col in range(n):
        if is_safe(board, row, col):
            board[row] = col
            solve_nqueens(board, row + 1, n)


def nqueens(n):
    """
    Solve the N Queens problem and print all possible solutions.
    Args:
        n: Size of the chessboard and number of queens.
    """
    # Check if the input is a valid integer
    try:
        n = int(n)
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    # Check if N is at least 4
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [-1] * n
    solve_nqueens(board, 0, n)


if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    nqueens(sys.argv[1])
