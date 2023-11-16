#!/usr/bin/python3
"""
rotate 2d matrix
"""


def rotate_2d_matrix(matrix):
    """rotate 2d maatrix 90 degrees in place"""
    left, right = 0, len(matrix) - 1

    while (left < right):
        for i in range(right - left):
            top, bottom = left, right
            temp = matrix[top][left + i]
            matrix[top][left + i] = matrix[bottom - i][left]
            matrix[bottom - i][left] = matrix[bottom][right - i]
            matrix[bottom][right - i] = matrix[top + i][right]
            matrix[top + i][right] = temp
        left += 1
        right -= 1
