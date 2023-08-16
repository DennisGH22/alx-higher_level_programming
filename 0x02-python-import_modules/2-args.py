#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    elements_len = len(argv) - 1
    argument_str = "argument" if elements_len == 1 else "arguments"
    argument_end = "." if elements_len == 0 else ":"

    print("{} {}{}".format(elements_len, argument_str, argument_end))

    for i, v in enumerate(argv[1:], start=1):
        print("{}: {}".format(i, v))
