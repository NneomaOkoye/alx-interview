#!/usr/bin/python3
"""Impementation of pascal triangle """


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing the Pascal’s triangle of n
    """
    triangle = []

    # Check for valid input
    if n <= 0:
        return triangle

    # Create the base of the triangle
    triangle.append([1])

    # Generate the rest of the triangle
    for row in range(1, n):
        # Create an empty row
        curr_row = []
        # Append 1 to the beginning of the row
        curr_row.append(1)
        # Generate the values inside the row
        for j in range(1, row):
            curr_row.append(triangle[row-1][j-1] + triangle[row-1][j])
        # Append 1 to the end of the row
        curr_row.append(1)
        # Append the row to the triangle
        triangle.append(curr_row)

    return triangle
