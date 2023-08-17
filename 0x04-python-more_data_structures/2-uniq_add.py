#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_integers = set()

    for i in my_list:
        unique_integers.add(i)

    total_sum = sum(unique_integers)

    return total_sum
