#!/usr/bin/python3
"""
python script
"""


def pascal_triangle(n):
    """
    returns a list of lists of integers
    representing the Pascal’s triangle of n
    """
    if n <= 0:
        return []

    triangle = []

    for i in range(n):
        if i == 0:
            triangle.append([1])
        else:
            row = [1]
            last_row = triangle[-1]
            for j in range(1, i):
                row.append(last_row[j - 1] + last_row[j])
            row.append(1)
            triangle.append(row)
    return triangle
