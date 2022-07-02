#!/usr/bin/python3
""" File name : 5-text_indentation.py
    Text indentation :  function that prints a text with 2
    new lines after each of these characters: ., ? and :
    Prototype: def text_indentation(text)
"""


def text_indentation(text):
    """function that prints a square with the character #
    size: numbers the character # to print
    Raises:
        TypeError: size must be an integer
        TypeError: size must be >= 0
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")
    phrase = ""
    i = 0
    while i < len(text):
        if text[i] != "." and text[i] != "?" and text[i] != ":":
            phrase += text[i]
        else:
            phrase += text[i]
            print(phrase)
            print()
            phrase = ""
            while i < (len(text) - 1) and text[i+1] == " ":
                i += 1
        i += 1
    print(phrase, end="")
