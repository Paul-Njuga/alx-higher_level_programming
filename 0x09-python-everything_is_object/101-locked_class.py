#!/usr/bin/python3
""" File name : 101-locked_class.py
    Low memory cost: Defines a locked class
    It is not allowed to import any module
"""


class LockedClass:
    """
    Prevent the user from instantiating new LockedClass attributes
    for anything but attributes called 'first_name'.
    """

    __slots__ = ['first_name']

    def __init__(self, first_name=''):
        self.first_name = first_name
