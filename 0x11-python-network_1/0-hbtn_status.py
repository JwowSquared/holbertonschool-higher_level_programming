#!/usr/bin/python3
"""x"""
from urllib import request


if __name__ == "__main__":
    with request.urlopen("https://intranet.hbtn.io/status") as response:
        body = response.read()
        out = "Body response:"
        out += "\n\t- type: {}"
        out += "\n\t- content: {}"
        out += "\n\t- utf8 content: {}"
        print(out.format(type(body), body, body.decode("utf-8")))
