#!/usr/bin/python3
"""x"""


def load_from_json_file(filename):
    """x"""
    import json
    with open(filename, "r") as f:
        out = json.load(f)
    return out
