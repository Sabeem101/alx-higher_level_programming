#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    leng1 = 0
    leng2 = 0
    for el in my_list:
        try:
            if (leng1 >= x):
                break
            print("{:d}".format(el), end="")
            leng1 += 1
        except (ValueError, TypeError):
            leng2 += 1
    if (leng1+leng2 < x):
        raise IndexError("list index out of range")
    print("".format())
    return leng1
