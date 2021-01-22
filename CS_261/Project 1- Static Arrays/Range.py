# Course: CS261 - Data Structures
# Student Name: Tyler Vareka
# Assignment: #1 Problem 5
# Description: This program will use the sa_range function and take a start/end as parameters.  It will then
# create an array that consists of all integer values from start to finish


from a1_include import *


def sa_range(start: int, end: int) -> StaticArray:
    """
    This program will take a start value and end value as parameters.  It will then create a static array that counts
    by values of one from start to finish, then returns that array.
    """
    if end > start: # This 'if statement' helps make sure the function works properly even if it is creating a
        # descending array
        num = end-start+1
    else:
        num = abs(end-start-1) # Must be absolute value to take into account for a descending array
    out_arr = StaticArray(num)
    for index in range(num):
        if end > start:
            out_arr[index] = start+index
        else:
            out_arr[index] = start-index
    return out_arr


# BASIC TESTING
if __name__ == "__main__":

    # example 1
    cases = [
        (1, 3), (-1, 2), (0, 0), (0, -3),
        (-105, -99), (-99, -105)]
    for start, end in cases:
        print(start, end, sa_range(start, end))
