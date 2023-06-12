#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return

    for num in matrix:
        for i in range(len(num)):
            print(
                    "{:d}".format(num[i]),
                    end="" if i == len(num) - 1 else " ")

        print()
