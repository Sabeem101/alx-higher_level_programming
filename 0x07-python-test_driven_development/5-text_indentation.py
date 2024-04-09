#!/usr/bin/python3
"""
Function that prints a text with
2 lines after each delimiter.
"""


def text_indentation(text):
    """
    Prints text with two new lines after each delimiter.
    Arguments:
        text(string): text to be printed.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    x = 0
    while x < len(text) and text[x] == ' ':
        x += 1

    while x < len(text):
        print(text[x], end="")
        if text[x] == "\n" or text[x] in ".?:":
            if text[x] in ".?:":
                print("\n")
            x += 1
            while x < len(text) and text[x] == ' ':
                x += 1
            continue
        x += 1
