#!/usr/bin/python3
"""Write to a file: """


def write_file(filename="", text=""):
    """Writes a string to a text file (UTF8).
    Args:
        filename: File to write to.
        text (str): String to write.
    Returns:
        Number of characters written.
    """
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
