#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    infin = len(sys.argv)
    res = 0
    for x in range(1, infin):
        res += int(sys.argv[x])
    print(res)
