#!/usr/bin/python3
"""send http request using Request
display body content if Statut code < 400
Usage: script_name URL"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    r = requests.get(url)
    if r.status_code >= 400:
        print("Error code: {}".format(r.status_code))
    else:
        print(r.text)
