#!/usr/bin/python3
tmpstr = ""
for x in reversed(range(97, 123)):
    if (x % 2) == 0:
        tmpstr += chr(x)
    else:
        tmpstr += chr(x-32)
print("{}".format(tmpstr), end="")
