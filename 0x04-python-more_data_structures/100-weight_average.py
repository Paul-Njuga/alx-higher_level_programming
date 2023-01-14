#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    average = 0
    div = 0
    for tuple in my_list:
        average += tuple[0] * tuple[1]
        div += tuple[1]
    return float(average / div)
