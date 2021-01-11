#!/bin/bash
#task 0 : Takes a URL, sends a request, and returns the size of the body
curl -s "$1" | wc -c
