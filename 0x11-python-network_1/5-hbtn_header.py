#!/usr/bin/python3
"""send http request using Request
display variable X-Request-Id
Usage: script_name URL"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    r = requests.get(url)
    print(r.headers.get('X-Request-Id'))
