#!/usr/bin/python3

def search_replace(my_list, search, replace):
    new_list = my_list.copy()
    for i in range(len(my_list)):
        if new_list[i] == search:
            new_list.append(replace)
        else:
            new_list.append(my_list[i])
    return new_list
