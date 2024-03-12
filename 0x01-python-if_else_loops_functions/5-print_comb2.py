#!/usr/bin/python3
cend = ", "
for x in range(0, 100):
    if x < 10:
        print("{}{}".format(0, x), end=cend)
    else:
        if x == 99:
            cend = "\n"
        print(x, end=cend)
