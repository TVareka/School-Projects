# Author: Ty Vareka
# Date: 1/28/2020
# Description: Recursive function that takes two positive integers and returns the product of those two numbers
def multiply(n, x):
    """n represent first positive integer and x represents the second positive integer"""
    if x < 2:
        return n
    return n + multiply(n, (x-1))



