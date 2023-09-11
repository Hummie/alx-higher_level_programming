#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    list_res = list(my_list)
    for num in list_res:
        if num % 2 == 0:
            list_res[num] = True
        else:
            list_res[num] = False
    return(list_res)
