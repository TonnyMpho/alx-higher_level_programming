#!/usr/bin/python3
""" This module multiplies 2 matrices """

import numpy as np

def lazy_matrix_mul(m_a, m_b):
    """
    function that multiplies 2 matrices

    Args:
        m_a (list of lists): matrix one
        m_b (list of lists): matrix two

    Return:
        list of lists: the multiplied lists

    Raises:
        ValueError: if matrices are not compatable.
    """

    """ matrix multiplication using numpy """

    mul = np.matmul(m_a, m_b)

    return mul
