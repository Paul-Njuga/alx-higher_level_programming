#!/usr/bin/python3
"""My list: """


class MyList(list):
    """MyList class that inherits from list."""

    def print_sorted(self):
        """Prints a sorted list."""
        sorted_list = self[:]
        sorted_list.sort()
        print(sorted_list)
