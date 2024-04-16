#!/usr/bin/python3
"""
Defines a pascal triangle that create a list of lists.
"""


def pascal_triangle(n):
    """
    Represents pascal's triangle of size n.
    """
    if n <= 0:
        return []
    T = [[1]]
    while len(T) != n:
        trg = T[-1]
        tmp = [1]
        for x in range(len(trg) - 1):
            tmp.append(trg[x] + trg[x + 1])
        tmp.append(1)
        T.append(tmp)
    return T
