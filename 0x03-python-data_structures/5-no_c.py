#!/usr/bin/python3
def no_c(my_string):
    nstr = ""
    for st in my_string:
        if st != 'c' and st != 'C':
            nstr += st
    return nstr
