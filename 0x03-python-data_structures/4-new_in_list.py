#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    nlist = my_list.copy()
    el = len(my_list)
    if idx < 0 or idx >= el or el == 0:
        return (nlist)
    else:
        nlist[idx] = element
        return (nlist)
