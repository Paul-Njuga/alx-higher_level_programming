#!/usr/bin/python3
"""Append to a file: """


def append_write(filename="", text=""):
    """Appends a string to a text file (UTF8).
    Args:
        filename: File to append to.
        text (str): String to append.
    Returns:
        Number of characters written.
    """
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
