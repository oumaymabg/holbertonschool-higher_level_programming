#!/usr/bin/python3
""" What's my status? #1 """
import requests


if __name__ == '__main__':
    print("Body response:")
    html = requests.get('https://intranet.hbtn.io/status').text
    print("\t- type: {}".format(type(html)))
    print("\t- content: {}".format(html))
