#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    if a_dictionary:
        for k in a_dictionary:
            if k == key:
                a_dictionary[k] = value
            else:
                a_dictionary[key] = value
    return a_dictionary
