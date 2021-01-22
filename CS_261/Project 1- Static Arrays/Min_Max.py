# Course: CS261 - Data Structures
# Student Name: Ty Vareka
# Assignment: #1 Problem #1
# Description: This program receives an array of numbers and then returns an output that consists of the array's
# maximum and minimum value in the order (min, max).


from a1_include import *


def min_max(arr: StaticArray) -> ():
    """
    This function takes a Static array as a parameter and determines the minimum/maximum in the array.
    """
    # Set the max/min to the first element in the array, so if the array only consists of one input, we can
    # still return a tuple of the max/min value.
    minimum = arr[0]
    maximum = arr[0]
    for index in range(arr.size()):
        if arr[index] < minimum:
            minimum = arr[index]
        elif arr[index] > maximum:
            maximum = arr[index]
    return minimum, maximum


# BASIC TESTING
if __name__ == "__main__":

    # example 1
    arr = StaticArray(5)
    for i, value in enumerate([8, 7, 6, -5, 4]):
        arr[i] = value
    print(min_max(arr))

    # example 2
    arr = StaticArray(1)
    arr[0] = 100
    print(min_max(arr))

    # example 3
    arr = StaticArray(3)
    for i, value in enumerate([3, 3, 3]):
        arr[i] = value
    print(min_max(arr))
