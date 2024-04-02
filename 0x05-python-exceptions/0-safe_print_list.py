#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    leng = 0
    for el in range(x):
        try:
            print("{}".format(el), end='')
            leng += 1
        except:
            break
    print()
    return (leng)
