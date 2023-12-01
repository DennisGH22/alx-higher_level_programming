#!/usr/bin/python3
import urllib.request
import sys

url = sys.argv[1]

with urllib.request.urlopen(url) as response:
    x_request_id = response.headers.get('X-Request-Id')
    if x_request_id:
        print("{}".format(x_request_id))
