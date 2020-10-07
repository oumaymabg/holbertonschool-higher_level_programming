#!/usr/bin/python3
"""task-9:load,add,save"""
import sys


save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_json_file = __import__('8-load_from_json_file').load_from_json_file

save = "add_item.json"
JSON = []

if len(sys.argv) > 0:
    try:
        JSON = load_json_file(save)
    except Exception:
        pass
    save_to_json_file(js + sys.argv[1:], save)
