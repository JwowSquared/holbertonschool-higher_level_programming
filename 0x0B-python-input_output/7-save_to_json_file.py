#!/usr/bin/python3
"""x"""


def save_to_json_file(myobj, filename):
    """x"""
    import json
    with open(filename, "w") as f:
        json.dump(myobj, f)
