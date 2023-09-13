#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrix_sqr = list(map(lambda row: list(map(lambda x: x ** 2, row)), matrix))
    return matrix_sqr

