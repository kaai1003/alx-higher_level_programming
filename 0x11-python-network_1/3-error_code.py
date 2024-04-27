#!/usr/bin/python3
"""send request to URL and display body
handle error exception
Usage : script_name URL
"""
import sys
import urllib
import urllib.error
import urllib.request
import urllib.parse


if __name__ == "__main__":
    url = sys.argv[1]
    try:
        response = urllib.request.urlopen(url)
        print(response.read())
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
