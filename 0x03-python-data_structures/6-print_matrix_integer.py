#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        for j in i:
            if j == len(i) - 1:
                print(" ", end="")
            print("{:d}".format(j), end="")
        print()
