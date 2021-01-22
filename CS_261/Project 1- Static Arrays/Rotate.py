# Course: CS261 - Data Structures
# Student Name: Tyler Vareka
# Assignment: #1 Problem 4
# Description: This program will take an array and step number to create a new array where the inputs are rotated.  The
# array can be rotated to the right using positive integers and to the left using negative integers. The function will
# also loop if the 'steps' integer is higher than the number of inputs in the array.


from a1_include import *


def rotate(arr: StaticArray, steps: int) -> StaticArray:
    """
    This program takes an array and 'steps' as parameters to rotate the original array.  The function itself does
    not change the original array, but returns a new array with the rotated values.
    """
    out_arr = StaticArray(arr.size()) # Creates a new array so that the original is not overwritten
    stp = steps % arr.size() # Creates the variable stp to use if the steps are larger than array size.  If not then
    # stp is going to be the same as steps
    for index in range(arr.size()):
        if stp + index == arr.size():
            stp = -index
        out_arr[stp + index] = arr[index]

    return out_arr


# BASIC TESTING
if __name__ == "__main__":

    # example 1
    source = [_ for _ in range(-20, 20, 7)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr.set(i, value)
    print(arr)
    for steps in [1, 2, 0, -1, -2, 28, -100]:
        print(rotate(arr, steps), steps)
    print(arr)
