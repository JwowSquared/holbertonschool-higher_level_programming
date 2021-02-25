#!/usr/bin/python3
"""x"""
import requests
from sys import argv

if __name__ == "__main__":
    c = ""
    if len(argv) > 1:
        c = argv[1]
    response = requests.post("http://0.0.0.0:5000/search_user", data={"q": c})
    if response.headers.get("content-type") == "application/json":
        response = response.json()
        if response == {}:
            print("No result")
        else:
            print("[{}] {}".format(response.get("id"), response.get("name")))
    else:
        print("Not a valid JSON")
