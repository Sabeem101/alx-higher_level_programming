#!/usr/bin/python3
"""
Fetches "https://alx-intranet.hbtn.io/status".
"""
import urllib.request


if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    with urllib.request.urlopen(url) as response:
        dt = response.read()
        utf_dt = dt.decode('utf-8')
        ResType = type(dt)
        print(f"Body response:\n\t- type: {ResType}\n\t\
                - content: {dt}\n\t- utf8 content: {utf_dt}")
