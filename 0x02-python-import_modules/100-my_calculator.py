#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div

    functions = {"+": add, "-": sub, "*": mul, "/": div}

    argv = sys.argv[1:]
    argc = len(argv)
    if argc != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    operator = argv[1]

    if operator in functions:
        a = int(argv[0])
        b = int(argv[2])
        cal = functions[operator](a, b)
        print("{} ".format(a) + operator + " {} = {}".format(b, cal))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
