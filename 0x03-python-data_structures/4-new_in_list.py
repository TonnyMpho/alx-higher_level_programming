#!/usr/bin/pyhon3

def new_in_list(my_list, idx, element):

    new_list = my_list.copy()

    if idx < 0:
        return new_list
    elif idx > (len(new_list) - 1):
        return new_list

    new_list[idx] = element

    return new_list
