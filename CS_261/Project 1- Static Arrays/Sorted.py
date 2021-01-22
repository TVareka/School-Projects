# Course: CS261 - Data Structures
# Student Name: Tyler Vareka
# Assignment: #1 Problem 6
# Description: This program determines if static array is sorted in an ascending or descending order.  If it is
# ascending it it returns a 1, a 2 if it is in descending order, and a 0 if the array is not either.


from a1_include import *


def is_sorted(arr: StaticArray) -> int:
    """
    This function takes an array as a parameter and determines if it is in either ascending or descending order.
    If the array is in strictly ascending order, it returns a 1.  If it is in strictly a descending order, it returns a
    a 2.  If the array is neither ascending nor descending, it returns a 0.
    """
    num = 0 # Num variable is what helps determine if the array is in either ascending or descending order
    for index in range(arr.size()-1):
        if arr[index] < arr[index + 1]:
            num += 1
        elif arr[index] > arr[index + 1]:
            num -= 1
    if num == arr.size()-1: # If the array is strictly ascending, num would add 1 each time making it equal to
        # the array size -1.
        return 1
    elif num == -arr.size()+1: # If the array is strictly descending, num would be subtracted by 1 each time, making it
        # equal to array size +1
        return 2
    else:
        return 0


# BASIC TESTING
if __name__ == "__main__":

    # example 1
    test_cases = (
        [-100, -8, 0, 2, 3, 10, 20, 100],
        ['A', 'B', 'Z', 'a', 'z'],
        ['Z', 'T', 'K', 'A', '1'],
        [1, 3, -10, 20, -30, 0],
        [-10, 0, 0, 10, 20, 30],
        [100, 90, 0, -90, -200],
        ['apple']
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        print('Result:', is_sorted(arr), arr)
