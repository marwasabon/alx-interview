#!/usr/bin/python3
"""Python Script for Rotates a 2D matrix"""


def rotate_2d_matrix(matrix):
    """Function Rotates 2D matrix 90 degrees clockwise
    Matrix is edited in-place
    args:
    matrix
    """
    n = len(matrix)
    layers = (n + 1) // 2  # Calculate the number of layers

    for layer in range(layers):
        first = layer
        last = n - layer - 1
        for i in range(first, last):
            offset = i - first
            # Save the top value
            top = matrix[first][i]
            # Move left to top
            matrix[first][i] = matrix[last - offset][first]
            # Move bottom to left
            matrix[last - offset][first] = matrix[last][last - offset]
            # Move right to bottom
            matrix[last][last - offset] = matrix[i][last]
            # Move top to right
            matrix[i][last] = top
