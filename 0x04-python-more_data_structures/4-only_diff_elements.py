#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    unique_set_1 = set()
    unique_set_2 = set()

    for i in set_1:
        if i not in set_2:
            unique_set_1.add(i)

    for i in set_2:
        if i not in set_1:
            unique_set_2.add(i)

    return unique_set_1.union(unique_set_2)
