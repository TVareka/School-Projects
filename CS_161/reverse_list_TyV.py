# Author: Ty Vareka
# Date: 2/13/2020
# Description: Takes a parameter list and reverses the order of that list
def reverse_list(list_1):
    """This function takes a list and mutates it by reversing the order of the original list"""
    for i in range(int(len(list_1)/2)):
        a = list_1[i]
        list_1[i] = list_1[-i-1]
        list_1[-i-1] = a

