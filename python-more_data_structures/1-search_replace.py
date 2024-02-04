#!/usr/bin/python3
def search_replace(my_list, search, replace):
    list_ = list()
    for i in range(len(my_list)):
        if (my_list[i] == search):
            list_.insert(i, replace)
        else:
            list_.insert(i, my_list[i])
    return list_
