#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    len = len(argv) - 1 
    if len == 0:
        print("{} arguments.".format(len))
    elif len == 1:
        print("{} argument:".format(len))
    else:
        print("{} arguments:".format(len))

    for i in range(1, len + 1):
        print("{}: {}".format(i, argv[i]))
