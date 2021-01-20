#!/usr/bin/python3
""" Response header value #1 """
from sys import argv
import requests


if __name__ == '__main__':
    html = requests.get(argv[1]).headers.get('X-Request-Id')
    print(html)
