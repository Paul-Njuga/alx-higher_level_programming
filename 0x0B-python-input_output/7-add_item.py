#!/usr/bin/python3
"""Load, add, save: """
import sys
import os.path as path

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

if path.isfile(filename):
    my_list = load_from_json_file(filename)
else:
    my_list = []

for i in range(1, len(sys.argv)):
    item = str(sys.argv[i])
    my_list.append(item)

save_to_json_file(my_list, filename)
