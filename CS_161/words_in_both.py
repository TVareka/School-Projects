# Author: Ty Vareka
# Date: 2/18/2020
# Description: Takes two strings and returns a set of words that are common to both.

def words_in_both(s1,s2):
    """This function will take two strings and returns a set of words that are common in both"""
    low_s1 = s1.lower()
    list_s1 = low_s1.split()
    low_s2 = s2.lower()
    list_s2 = low_s2.split()
    set_1 = set(list_s1)
    set_2 = set(list_s2)
    set_3 = set_1 & set_2
    return set_3


