#!/usr/bin/python3
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "test.json"
my_list = load_from_json_file(filename)
print(my_list)
print(type(my_list))
