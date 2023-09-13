#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq_list = list(set(my_list))
    for num in uniq_list:
        list_sum = sum(uniq_list)
        return list_sum
