#!/usr/bin/python3
"""add args to list Script"""


import sys
import os
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"
new_list = []
i = 1

if os.path.exists(filename):
    args_list = load_from_json_file(filename)
    new_list = args_list[:]
    while i < len(sys.argv):
        new_list.append(sys.argv[i])
        i += 1
else:
    while i < len(sys.argv):
        new_list.append(sys.argv[i])
        i += 1
save_to_json_file(new_list, filename)
