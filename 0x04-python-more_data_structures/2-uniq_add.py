#!/usr/bin/python3
def uniq_add(my_list=[]):
    new = set(my_list)
    sum = 0
    for i in new:
        sum += i
    return sum
