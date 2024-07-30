#!/usr/bin/python3
"""
Finds a peak in a list of unsorted integers.
"""


def find_peak(list_of_integers):
    """
    Attributes:
        list_of_integers(int): list of integers to find the peak.
    """
    if list_of_integers:
        leng = len(list_of_integers) - 1
        lst = 0
        while lst < leng:
            mid = (lst + leng) // 2
            if list_of_integers[mid] > list_of_integers[mid + 1]:
                leng = mid
            else:
                lst = mid + 1
        return list_of_integers[lst]
