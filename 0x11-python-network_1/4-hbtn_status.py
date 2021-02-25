#!/usr/bin/python3
"""x"""
import requests


if __name__ == "__main__":
    response = requests.get("https://intranet.hbtn.io/status")
    out = "Body response:"
    out += "\n\t- type: {}"
    out += "\n\t- content: {}"
    print(out.format(type(response.text), response.text))
