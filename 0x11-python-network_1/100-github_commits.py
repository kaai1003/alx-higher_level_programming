#!/usr/bin/python3
"""list 10 commits from REPO
Usage: script OWNER REPO
"""

import requests
import sys


url = "https://api.github.com/repos/{}/{}/commits".format(sys.argv[1],
                                                          sys.argv[2])
try:
    r = requests.get(url)
    r_dict = r.json()
    i = 0
    for item in r_dict:
        if i < 10:
            print("{}: {}".format(item['sha'],
                                  item['commit']['author']['name']))
        else:
            break
        i += 1
except Exception as e:
    print(e)
