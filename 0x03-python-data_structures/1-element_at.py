#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0 or idx > len(my_list):
        return None

    for i, elm in enumerate(my_list):
        if i == idx:
            return elm
