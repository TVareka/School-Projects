# Course: CS261 - Data Structures
# Student Name: Ty Vareka
# Assignment: #1 Problem 7
# Description: This program will sort an array that is passed to the function sa_sort. The function does change
# original array, and does not create a new array which it returns.


from a1_include import *


def sa_sort(arr: StaticArray) -> None:
    """
    This function will take an array as a parameter and then sort that array in ascending order.
    """
    for pass_num in range(arr.size()-1):
        for index in range(arr.size() - 1 - pass_num):
            if arr[index] > arr[index + 1]:
                temp = arr[index]
                arr[index] = arr[index + 1]
                arr[index + 1] = temp
    return


# BASIC TESTING
if __name__ == "__main__":

    # example 1
    test_cases = (
        [1, 10, 2, 20, 3, 30, 4, 40, 5],
        ['zebra2', 'apple', 'tomato', 'apple', 'zebra1'],
        [(1, 1), (20, 1), (1, 20), (2, 20)]
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        print(arr)
        sa_sort(arr)
        print(arr)
