#!/usr/bin/python3
for c in range(ord('z'), ord('a') - 1, -1):
    if c % 2 == 0:
        print("{:c}".format(c), end="")
    else:
        print("{:c}".format(c - 32), end="")
