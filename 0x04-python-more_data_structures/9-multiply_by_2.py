#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    n_dictionary = a_dictionary.copy()
    for key, value in list(n_dictionary.items()):
        n_dictionary[key] = value * 2
    return n_dictionary
