#!/usr/bin/python3
if __name__ == "__main__":

    from calculator_1 import add, sub, mul, div
    from sys import argv, exit

    if len(argv) < 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    num1 = int(argv[1])
    num2 = int(argv[3])
    op = argv[2]

    if op != "+" and op != "-" and op != "*" and op != "/":
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    if op == '+':
        print("{} {} {} = {}".format(num1, op, num2, add(num1, num2)))
    elif op == '-':
        print("{} {} {} = {}".format(num1, op, num2, sub(num1, num2)))
    elif op == '*':
        print("{} {} {} = {}".format(num1, op, num2, mul(num1, num2)))
    elif op == '/':
        print("{} {} {} = {}".format(num1, op, num2, div(num1, num2)))
