#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or (roman_string is None):
        return 0
    rnum = {"I": 1, "V": 5, "X": 10, "L": 50,
            "C": 100, "D": 500, "M": 1000}
    rstr = roman_string
    con = [rnum[x[0]] if rnum[x[0]] >= rnum[x[1]] else (-1*rnum[x[0]]) for x in zip(rstr, rstr[1:] + rstr[-1])]
    return sum(con)
