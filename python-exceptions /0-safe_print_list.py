#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    for i in range(0, x):
        try:
            count = count + 1
            print("{}".format(my_list[i]), end="")
        except IndexError:
            print()
            return count - 1
    print()
    return count
