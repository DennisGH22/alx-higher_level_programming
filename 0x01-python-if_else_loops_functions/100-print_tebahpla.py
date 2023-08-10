#!/usr/bin/python3
for i in range(ord('z'), ord('`'), -1):
    enumerate(chr(i))
    if i % 2 == 0:
        i = chr(i)
    else:
        i = chr(i - 32)
    print("{}".format(i), end="")
