#!/usr/bin/python3
cend = ", "
for x in range(0, 100):
    dig2 = x % 10
    dig1 = x / 10
    if x < 10 and dig1 < dig2:
        print("{}{}".format(0, x), end=cend)
    elif dig1 < dig2:
        if x == 89:
            cend = "\n"
        print(x, end=cend)
