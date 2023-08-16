#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys

    elements_len = len(sys.argv) - 1

    if elements_len != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    operator = sys.argv[2]
    a = sys.argv[1]
    b = sys.argv[3]

    if operator == '+':
        print("{} {} {} = {}".format(a, operator, b, add(int(a), int(b))))
    elif operator == '-':
        print("{} {} {} = {}".format(a, operator, b, sub(int(a), int(b))))
    elif operator == '*':
        print("{} {} {} = {}".format(a, operator, b, mul(int(a), int(b))))
    elif operator == '/':
        print("{} {} {} = {}".format(a, operator, b, div(int(a), int(b))))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
