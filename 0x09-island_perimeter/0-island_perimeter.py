#!/usr/bin/python3
"""island perimeter interview question:

   - grid is a list of list of integers:
       - 0 represents water
       - 1 represents land
       - Each cell is square, with a side length of 1
        -Cells are connected horizontally/vertically (not diagonally).
       - grid is rectangular, with its width and height not exceeding 100
   - The grid is completely surrounded by water
   - There is only one island (or nothing).
   - The island doesn’t have “lakes” (water inside that isn’t
     connected to the water surrounding the island).
"""


def island_perimeter(grid):
    """returns perimeter of the island described in grid"""
    perimeter = 0
    for i in range(1, len(grid) - 1):
        for j in range(1, len(grid[i]) - 1):
            if grid[i][j] != 1:
                continue
            count = 0
            if grid[i - 1][j] == 0:
                count += 1
            if grid[i + 1][j] == 0:
                count += 1
            if grid[i][j - 1] == 0:
                count += 1
            if grid[i][j + 1] == 0:
                count += 1
            perimeter += count
    return perimeter
