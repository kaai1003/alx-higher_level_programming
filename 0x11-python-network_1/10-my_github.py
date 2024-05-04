#!/usr/bin/python3
"""display github api id"""
import requests
import sys


url = "https://api.github.com/user"
r = requests.get(url, auth=(sys.argv[1], sys.argv[2]))
r_dict = r.json()
print(r_dict)
print(r_dict['id'])
