#!/usr/bin/python3

""" function that divides all elements of a matrix. """

def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix

    Args:
        matrix (list): list of lists
        div (int): number to divide with

    Returns:
        matrix:matrix with divided values

    Raises:
        TypeError: matrix must be a matrix (list of lists) of integers/floats
        TypeError: div must be a number
        ZeroDivisionError: division by zero
    """
    if not isinstance(matrix, list) or not all(isinstance(lst, list) for lst in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    for lst in matrix:
        for num in lst:
            if not isinstance(num, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not all(len(lst) == len(matrix[0]) for lst in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    div_matrix = []
    for lst in matrix:
        div_matrix.append([round((num / div), 2) for num in lst])

    return div_matrix
