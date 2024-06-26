#!/usr/bin/python3
"""POST http request using Requests
pass letter as params
Usage: script_name URL"""
import requests
import sys


if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    if len(sys.argv) < 2:
        q = {'q': ""}
    else:
        q = {'q': sys.argv[1]}
    try:
        r = requests.post(url, data=q)
        r.raise_for_status()
        r_dict = r.json()
        if not r_dict:
            print("No result")
        else:
            print("[{}] {}".format(r_dict['id'], r_dict['name']))
    except ValueError as e:
        print("Not a valid JSON")
