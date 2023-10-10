#!/usr/bin/python3
"""Finds a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """Finds a peak in list_of_integers"""
    ln = len(list_of_integers)
    pk = 0
    even = ln % 2 == 0
    if even:
        semi_mid = ln // 2 - 1
    else:
        semi_mid = ln // 2
    while (semi_mid >= 0):
        if list_of_integers[semi_mid] > pk:
            pk = list_of_integers[semi_mid]
        semi_mid = semi_mid // 2

    if even:
        mid = ln - 1
    else:
        mid = ln
    while (mid > semi_mid):
        if list_of_integers[mid] > pk:
            pk = list_of_integers[mid]
        mid = mid // 2
    return pk
