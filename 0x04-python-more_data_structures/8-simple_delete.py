#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    if key not in a_dictionary:
        return a_dictionary
    else:
        for k in a_dictionary:
            if k == key:
                del a_dictionary[key]
    return a_dictionary
