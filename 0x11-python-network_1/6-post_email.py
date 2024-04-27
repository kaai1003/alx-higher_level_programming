#!/usr/bin/python3
"""send http + email POST using Request
display body content
Usage: script_name URL email"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    data = {'email': sys.argv[2]}
    r = requests.post(url, data=data)
    print(r.text)
