#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        lsd = -number % 10
        lsd = lsd
    else:
        lsd = number % 10
    print(lsd, end="")
    return (lsd)
