# Course: CS261 - Data Structures
# Student Name: Ty Vareka
# Assignment: #1 Problem 8
# Description: This program uses the function 'remove_duplicate' to determine if there are multiple inputs in an array
# that are the same, and then creates a new StaticArray that purges those duplicates.  At the end of the function,
# the new static array is returned


from a1_include import *


def remove_duplicates(arr: StaticArray) -> StaticArray:
    """
    This function takes an array as a parameter, then determines if there are multiple duplicates within that array.
    The function then creates a new static array without those duplicates, which is returned at the end of the function
    """
    num = 1 # Important variable to create so that we can determine how big the new array has to be when it is created

    for index in range(1, arr.size()): # This first 'for loop' determines how many duplicates are in the original array
        if arr[index] == arr[index-1]:
            continue
        else:
            num += 1
    out_arr = StaticArray(num) # Creates new array that is the correct size without duplicates
    out_arr[0] = arr[0]
    count = 1
    for index in range(1, arr.size()):
        if arr[index] == arr[index-1]:
            continue
        else:
            out_arr[count] = arr[index]
            count += 1

    return out_arr


# BASIC TESTING
if __name__ == "__main__":

    # example 1
    test_cases = (
        [1], [1, 2], [1, 1, 2], [1, 20, 30, 40, 500, 500, 500],
        [5, 5, 5, 4, 4, 3, 2, 1, 1], [1, 1, 1, 1, 2, 2, 2, 2]
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        print(arr)
        print(remove_duplicates(arr))
    print(arr)
