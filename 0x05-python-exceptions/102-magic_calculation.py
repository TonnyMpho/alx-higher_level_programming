#!/usr/bin/python3

def magic_calculation(a, b):

    results = 0

    for i in range(1, 3):
        try:
            if i > a:
                raise Exception("Too far")
            results += (a ** b) / i
        except Exception:
            results = a + b
            break

    return (results)
