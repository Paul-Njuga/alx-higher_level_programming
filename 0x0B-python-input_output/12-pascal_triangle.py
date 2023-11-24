#!/usr/bin/python3
"""Module 14-pascal_triangle.
Returns a list of lists of integers
representing the Pascal’s triangle of n.
"""


def pascal_triangle(n):
    """Returns the pascal triangle of n.

    Args:
        - n: size of the triangle (rows)

    Returns: a list of list of integers
    """

    if n <= 0:
        return []

    myList = [[0 for x in range(i + 1)] for i in range(n)]
    myList[0] = [1]

    for i in range(1, n):
        myList[i][0] = 1
        for j in range(1, i + 1):
            if j < len(myList[i - 1]):
                myList[i][j] = myList[i - 1][j - 1] + myList[i - 1][j]
            else:
                myList[i][j] = myList[i - 1][0]
    return myList
