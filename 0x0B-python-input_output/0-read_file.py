#!/usr/bin/python3
"""Read file: """


def read_file(filename=""):
    """Reads a text file (UTF8) and prints it to stdout.
    Args:
        filename: The file to read from.
    """
    with open(filename, 'r', encoding="utf-8") as f:
        for line in f:
            print(line, end='')
