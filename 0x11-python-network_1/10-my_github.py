#!/usr/bin/python3
"""
Takes your GitHub credentials and uses GitHub API
to display your id.
"""
from requests.auth import HTTPBasicAuth
import requests
import sys


if __name__ == "__main__":
    auth = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    req = requests.get("https://api.github.com/user", auth=auth)
    print(req.json().get("id"))
