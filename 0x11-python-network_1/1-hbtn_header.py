#!/usr/bin/python3
"""sends a request to the URL
displays the value of the X-Request-Id
Usage : script_name URL
"""
import sys
import urllib
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        html = response.info()
        print(html["X-Request-Id"])
