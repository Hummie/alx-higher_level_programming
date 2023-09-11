#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    num_rows = len(matrix)
    num_cols = len(matrix[0])

    for row in range(num_rows):
        for col in range(num_cols):
            if col != 0:
                print(" ", end='')
            print("{:2d}".format(matrix[row][col]), end=' ')
        print()
