#!/usr/bin/python3
""" Technical interview preparation """


def pascal_triangle(n):
    """
    function def pascal_triangle(n): that returns a
    list of lists of integers representing the Pascal’s
    triangle of n Returns an empty list if n <= 0
    """
    if n <= 0:
        return []

    tri = []
    for i in range(n):
        r = []
        for k in range(i + 1):
            if k == 0 or k == i:
                r.append(1)
            else:
                p_r = tri[i - 1]
                r.append((p_r[k - 1] + p_r[k]))
        tri.append(r)
    return tri
