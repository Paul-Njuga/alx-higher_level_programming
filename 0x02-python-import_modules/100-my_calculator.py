#!/usr/bin/python3


def calculator():
    from sys import argv
    from calculator_1 import add, sub, mul, div

    if (len(argv) - 1) != 3:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        exit(1)

    ops = ['+', '-', '*', '/']

    if argv[2] not in ops:
        print('Unknown operator. Available operators: +, -, * and /')
        exit(1)

    a = int(argv[1])
    b = int(argv[3])

    if argv[2] == ops[0]:
        res = add(a, b)
    elif argv[2] == ops[1]:
        res = sub(a, b)
    elif argv[2] == ops[2]:
        res = mul(a, b)
    elif argv[2] == ops[3]:
        res = div(a, b)
    print('{} {} {} = {}'.format(a, argv[2], b, res))


if __name__ == "__main__":
    calculator()
