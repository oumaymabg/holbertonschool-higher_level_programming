#!/bin/bash
# Sends a GET request and displays the body of the response with custom header
url -sX GET -H "X-HolbertonSchool-User-Id: 98" "$1"
