#!/usr/bin/python3
import urllib.request
import sys

"""
Sends a request to the URL and displays the value of the X-Request-Id
"""

url = sys.argv[1]

with urllib.request.urlopen(url) as response:
    x_request_id = response.headers.get('X-Request-Id')
    if x_request_id:
        print(x_request_id)
