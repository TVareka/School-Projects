# Author: Ty Vareka
# Date: 2/13/2020
# Description: Program takes a parameter list and replaces each value with the square of that value
def square_list(list):
    """Takes a list and mutates it by squaring all the numbers in the list"""
    for nums in range(len(list)):
        list[nums] = list[nums]**2

