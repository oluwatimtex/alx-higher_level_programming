#!/usr/bin/python3
def no_c(my_string):
    for letter in range(len(my_string)):
        if letter == "c" and letter == "C":
            return ""
        else:
            return letter
