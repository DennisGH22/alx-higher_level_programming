#!/usr/bin/python3
def uppercase(str):
    if ord('a') <= ord(str) <= ord('z'):
        str = chr(ord(str) - 32)
        print("{}".format(str))
    else:
        print("{}".format(str))
