#!/usr/bin/python3
"""
Takes in a URL and an email, ends a POST request to the passed
URL with the email as parameter, and displays the body of the response.
"""
import urllib.request
import urllib.parse
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    val = {"email": sys.argv[2]}
    dt = urllib.parse.urlencode(val).encode("ascii")
    req = urllib.request.Request(url, dt)
    with urllib.request.urlopen(req) as response:
        print(response.read().decode("utf-8"))
