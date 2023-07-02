#!/usr/bin/python3
""" This module multiplies 2 matrices """

def matrix_mul(m_a, m_b):
    """
    function that multiplies 2 matrices

    Args:
        m_a (list of lists): matrix one
        m_b (list of lists): matrix two

    Return:
        list of lists: the multiplied lists

    Raises:
        TypeError: If m_a or m_b is not a list or a list of lists.
        ValueError: If m_a or m_b is empty or not a rectangle.
        TypeError: If an element of m_a or m_b is not an integer or float.
        ValueError: If m_a and m_b cannot be multiplied.
    """

    if type(m_a) != list or isinstance(m_b, list):
        raise TypeError("m_a must be a list or m_b must be a list")

    if not all(isinstance(a, list) for a in m_a) or not all(isinstance(b, list) for b in m_a):
        raise TypeError("m_a must be a list of lists or m_b must be a list of lists")

    if m_a == [] or m_b == [] or m_a == [[]] or m_b == [[]]:
        raise ValueError("m_a can't be empty or m_b can't be empty")

    if not all(isinstance(num, (int, float)) for row in m_a for num in row) or \
            not all(isinstance(num, (int, float)) for row in m_b for num in row):
        raise TypeError("m_a should contain only integers or floats or m_b should contain only integers or floats")

    if not all(len(row) == len(m_a[0]) for row in m_a) or not all(len(row) == len(m_b[0]) for row in m_b):
        raise ValueError("each row of m_a must be of the same size or each row of m_b must be of the same size")


    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    """ matrix multiplication """
    mul = []
    for i in range(len(m_a)):
        results = []
        for j in range(len(m_b[0])):
            element = 0
            for k in range(len(m_b)):
                element += m_a[i][k] * m_b[k][j]
            results.append(element)
        mul.append(results)

    return mul
