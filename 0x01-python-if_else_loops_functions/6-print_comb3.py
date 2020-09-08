#!/usr/bin/python3
for i in range(0, 10):
    for num in range(0, 10):
        if (i == num) or (i > num):
            continue
        if (i == 8) and (num == 9):
            print("{:d}{:d}".format(i, num))
        else:
            print("{:d}".format(i), end="")
            print("{:d}".format(num), end=", ")
