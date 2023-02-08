#!/usr/bin/python3
"""Write to a file: """


def append_file(filename="", text=""):
    """Appends a string to a text file (UTF8).
    Returns:
        Number of characters written.
    """
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
