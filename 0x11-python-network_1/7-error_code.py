#!/usr/bin/python3
""" Error code #1  """
from sys import argv
import requests


if __name__ == '__main__':
    html = requests.get(argv[1])
    if html.status_code >= 400:
        print("Error code: {}".format(html.status_code))
    else:
        print(html.text)
