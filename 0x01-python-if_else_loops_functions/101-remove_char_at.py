#!/usr/bin/python3
def remove_char_at(str, n):
    if n >= 0:
        tmpstr = str[:n] + str[n + 1:]
        return (tmpstr)
    else:
        return (str)
