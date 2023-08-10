#!/usr/bin/python3
def uppercase(str):
    uppercase_str = ""
    for i in str:
        if ord('a') <= ord(i) <= ord('z'):
            i = chr(ord(i) - 32)
        uppercase_str += "{}".format(i)
    print(uppercase_str)
