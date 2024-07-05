#!/usr/bin/python3
"""
Takes in a URL, sends a request to the URL
and displays the body of the response.
"""
import urllib.request
import urllib.parse
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(req) as response:
            print(response.read().decode("ascii"))
    except urllib.error.HTTPError as err:
        print("Error code: {}".format(err.code))
