#!/usr/bin/python3
"""display github api id"""
import requests
import sys


url = "https://api.github.com/user"
try:
    r = requests.get(url, auth=(sys.argv[1], sys.argv[2]))
    r.raise_for_status()
    r_dict = r.json()
    print(r_dict['id'])
except Exception as e:
    print("None")
