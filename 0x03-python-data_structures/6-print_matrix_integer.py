#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for num in matrix:
        for j in range(len(num)):
            if j != len(num) - 1:
                print("{:d}".format(num[j]), end=" ")
            else:
                print("{:d}".format(num[j]))
        print()
