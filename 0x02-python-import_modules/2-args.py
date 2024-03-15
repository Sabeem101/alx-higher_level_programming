#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    x = 0
    args_count = len(sys.argv) - 1
    if args_count == 1:
        print("{:d} argument:".format(1))
    elif args_count == 0:
        print("{:d} arguments.".format(1))
    else:
        print("{:d} arguments:".format(1))
    for a in sys.argv:
        if (x != 0):
            print("{:d}: {}".format(x, a))
        x += 1
