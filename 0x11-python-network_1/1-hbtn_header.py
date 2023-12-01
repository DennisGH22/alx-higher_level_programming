#!/usr/bin/python3
import urllib.request
import sys

with urllib.request.urlopen(sys.argv[1]) as response:
    x_request_id = response.headers.get('X-Request-Id')
    print("{}".format(x_request_id))
