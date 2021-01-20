#!/bin/bash
# Outputs the status code of an HTTP response
curl -s -w "%{http_code}" "$1" -o /dev/null
