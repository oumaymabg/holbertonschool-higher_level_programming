#!/usr/bin/python3
""" Search API """
from sys import argv
import requests


if __name__ == '__main__':
    if len(argv) == 2:
        value = {"q": argv[1]}
    else:
        value = {"q": ""}
    request = requests.post('http://0.0.0.0:5000/search_user', data=value)
    try:
        data = request.json()
        if data == {}:
            print("No result")
        else:
            print("[{}] {}".format(data['id'], data['name']))
    except:
        print("Not a valid JSON")
