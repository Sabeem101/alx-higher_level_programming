#!/usr/bin/python3
"""
Fetches "https://alx-intranet.hbtn.io/status".
"""
import urllib.request


if __name__ == "__main__":
    url = urllib.request.Request("https://alx-intranet.hbtn.io/status")
    with urllib.request.urlopen(url) as response:
        dt = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(dt)))
        print("\t- content: {}".format(dt))
        print("\t- utf8 content: {}".format(dt.decode("utf-8")))
