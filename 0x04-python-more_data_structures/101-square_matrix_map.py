#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map(lambda mat_row: list(map(lambda i: i**2, mat_row)), matrix))
