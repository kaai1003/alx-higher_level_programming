#!/usr/bin/python3
"""send POST request to URL with email as parm
and display the body of the response
Usage : script_name URL
"""
import sys
import urllib
import urllib.request
import urllib.parse


if __name__ == "__main__":
    url = sys.argv[1]
    data = urllib.parse.urlencode({'email': sys.argv[2]}).encode('utf-8')
    with urllib.request.urlopen(url, data) as response:
        html = response.read()
        print(html)
