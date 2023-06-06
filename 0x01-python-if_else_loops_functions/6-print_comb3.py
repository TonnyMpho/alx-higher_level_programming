#!/usr/bin/python3

for num in range(10):
    for i in range(num + 1, 10):
        print("{}{}".format(num, i), end=", ")
        if num == 8 and i == 9:
            print("{}{}".format(num, i))
