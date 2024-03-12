#!/usr/bin/python3
def uppercase(str):
    tmpstr = ""
    for c in str:
        if ord(c) > 96 and ord(c) < 123:
            tmpstr += chr(ord(c)-32)
        else:
            tmpstr += c
    print("{}".format(tmpstr))
