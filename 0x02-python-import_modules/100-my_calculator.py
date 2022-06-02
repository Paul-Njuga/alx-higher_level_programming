#!/usr/bin/python3


def calculator():
    import sys
    from calculator_1 import add, sub, mul, div

    if len(sys.argv) != 4:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        exit(1)

    ope = sys.argv[2]
    if ope != '+' and ope != '-' and ope != '*' and ope != '/':
        print('Unknown operator. Available operators: +, -, * and /')
        exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[3])
    if ope == '+':
        res = add(a, b)
    if ope == '-':
        res = sub(a, b)
    if ope == '*':
        res = mul(a, b)
    if ope == '/':
        res = div(a, b)
    print('{} {} {} = {}'.format(a, ope, b, res))


if __name__ == "__main__":
    calculator()
