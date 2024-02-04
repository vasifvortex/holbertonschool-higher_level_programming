#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    if not isinstance(a_dictionary, dict):
        return
    sorted_k = list(a_dictionary.keys())
    sorted_k.sort()
    sorted_dict = {i: a_dictionary[i] for i in sorted_k}
    for x in sorted_dict:
        print("{}: {}".format(x, sorted_dict[x]))
