#!/usr/bin/python3
for i in range(ord('a'), ord('{')):
    enumerate(chr(i))
    if i % 2 == 0:
        i = chr(i - 32)
    else:
        i = chr(i)
    print(i, end="")
