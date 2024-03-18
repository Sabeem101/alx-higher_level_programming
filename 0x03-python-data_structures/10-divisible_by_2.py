#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    nlist = []
    el = len(my_list)
    for iter in range(0, el):
        if (my_list[iter] % 2) == 0:
            nlist.append(True)
        else:
            nlist.append(False)
    return nlist
