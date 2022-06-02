#!/usr/bin/python3
for c in range(ord('a'), ord('z') + 1):
    if c != ord('q') and c != ord('e'):
        print("{:c}".format(c), end="")
