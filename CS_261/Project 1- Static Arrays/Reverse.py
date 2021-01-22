# Course: CS261 - Data Structures
# Student Name: Tyler Vareka
# Assignment: #1 Problem 3
# Description: This program will take an array and reverse that array's order completely.  The function 'reverse'
# alters the original array.


from a1_include import *


def reverse(arr: StaticArray) -> None:
    """
    This function will take an array as a parameter.  The function then reverses the original array and then returns it
    """
    for index in range(int((arr.size())/2)):
        val = arr[index] # saves the current number in the static array to a new variable
        arr[index] = arr[arr.size()-index-1]
        arr[arr.size()-index-1] = val
    return


# BASIC TESTING
if __name__ == "__main__":

    # example 1
    source = [_ for _ in range(-20, 20, 7)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr.set(i, value)
    print(arr)
    reverse(arr)
    print(arr)
    reverse(arr)
    print(arr)
