#!/usr/bin/python3
import urllib.request
import sys

if __name__ == "__main__":   
    args = sys.argv[1]
    url = urllib.request.Request(args)
    with urllib.request.urlopen(url) as response:
        body = response.info()
    print(body['X-Request-Id'])
