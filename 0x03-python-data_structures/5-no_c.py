#!/usr/bin/python3
def no_c(my_string):
    result_str = ""

    for i in range(len(my_string)):
        if i != "c" or i != "C":
            result_str += my_string[i]
    return result_str
