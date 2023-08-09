#!/usr/bin/python3
for i in range(0, 100):
    if len(str(i)) < 2:
        i = '0' + str(i)
    if i == 99:
        print("{}".format(i))
        continue
    print("{}".format(i), end=", ")
