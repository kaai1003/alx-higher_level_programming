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
        with urllib.request.urlopen(url) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
