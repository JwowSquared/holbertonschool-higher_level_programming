#!/usr/bin/python3
"""x"""


if __name__ == "__main__":
    jsave = __import__('7-save_to_json_file').save_to_json_file
    jload = __import__('8-load_from_json_file').load_from_json_file
    import sys

    try:
        my_obj = jload("add_item.json")
    except:
        my_obj = []

    for i in range(1, len(sys.argv)):
        my_obj.append(sys.argv[i])

    jsave(my_obj, "add_item.json")
