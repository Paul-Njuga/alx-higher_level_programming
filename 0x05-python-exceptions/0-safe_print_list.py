#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    length = 0
    count = 0
    for i in my_list:
        length += 1
    for j in range(x):
        try:
            print("{}".format(my_list[j]), end="")
        except Exception:
            print("")  # Print newline
            return length  # Print line length when exception occurs
        count += 1
    print("")
    return count
