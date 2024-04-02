#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    leng = 0
    try:
        for el in my_list:
            if (leng >= x):
                break
            print("{}".format(el), end='')
            leng += 1
        print("".format())
        return leng
    except ValueError:
        print("ValueError error")
