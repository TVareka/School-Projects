# Course: CS261 - Data Structures
# Student Name: Tyler Vareka
# Assignment: #1 Problem 2
# Description: This program is used to determine if the values in the static array that is passed in, has
# values that are divisible by 3 and 5.  If the element is divisible by 3, it changes that element to fizz. If the
# element is divisible by 5, it changes the value to buzz.  If the value is divisible by both fizz and buzz, then
# it changes the value to fizzbuzz.


from a1_include import *


def fizz_buzz(arr: StaticArray) -> StaticArray:
    """
    This function receives a Static array.  It then uses '%' to determine if each element of the array is divisble by
    3 or 5.  It then creates a new array that will change the input itself to 'fizz' if divisible by 3, 'buzz' if
    divisible by 5, and 'fizzbuzz' if divisible by both 3 and 5.
    """

    out_arr = StaticArray(arr.size())     # Creates a new static array so that the original is not tampered with
    for index in range(arr.size()):
        if arr[index] % 3 == 0 and arr[index] % 5 == 0:
            out_arr[index] = "fizzbuzz"
        elif arr[index] % 3 == 0:
            out_arr[index] = "fizz"
        elif arr[index] % 5 == 0:
            out_arr[index] = "buzz"
        else:
            out_arr[index] = arr[index]

    return out_arr


# BASIC TESTING
if __name__ == "__main__":

    # example 1
    source = [_ for _ in range(-5, 20, 4)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr[i] = value
    print(fizz_buzz(arr))
    print(arr)
