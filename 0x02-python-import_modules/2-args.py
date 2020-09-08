#!/usr/bin/python3
import sys
if __name__ == '__main__':
    length = len(sys.argv) - 1
    if length == 0:
        print('{} arguments.'.format(length))
    elif length == 1:
        print('{} argument:'.format(length))
        print('{}: {}'.format(length, sys.argv[1]))
    else:
        print('{} arguments:'.format(length))
        for n in range(1, len(sys.argv)):
            print('{}: {}'.format(n, sys.argv[n]))
