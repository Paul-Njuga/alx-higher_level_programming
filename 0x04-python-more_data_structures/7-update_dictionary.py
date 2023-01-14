#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    if a_dictionary:
        for key not in a_dictionary:
            a_dictionary[key] = value
        else:
            for k in a_dictionary:
                if k == key:
                    a_dictionary[k] = value
    return a_dictionary
