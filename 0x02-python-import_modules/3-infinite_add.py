#!/usr/bin/python3
import sys
if __name__ == '__name':
    length = len(sys.argv) - 1
    if length == 0:
        print('0')
    elif length == 1:
        print('{}: {}'.format(length, sys.argv[1]))
    else length > 1:
        print('{} arguments:'.format(length))
        for n in range(1, len(sys.argv)):
            print('{}: {}'.format(n, sys.argv[n]))
