#!/usr/bin/python3
"""x"""
import requests
from sys import argv

if __name__ == "__main__":
    response = requests.get(argv[1])
    if response.status_code == requests.codes.ok:
        print(response.text)
    else:
        print("Error code: {}".format(response.status_code))
