#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for a, b in zip(list(a_dictionary.keys()), list(a_dictionary.values())):
        if b == value:
            del a_dictionary[a]
    return a_dictionary
