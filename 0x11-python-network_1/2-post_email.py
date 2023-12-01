#!/usr/bin/python3
import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    args = sys.argv
    email = {'email': args[2]}
    data = urllib.parse.urlencode(email)
    data = data.encode()
    url = urllib.request.Request(args[1], data)
    with urllib.request.urlopen(url) as response:
        body = response.read().decode('utf-8')
    print(body)
