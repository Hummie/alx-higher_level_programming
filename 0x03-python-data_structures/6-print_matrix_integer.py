#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    num_rows = len(matrix)
    num_colu = len(matrix[0])

    for row in range(num_rows):
        for colu in range(num_colu):
            print("{:2d}".format(matrix[row][colu]), end=' ')
        print()
