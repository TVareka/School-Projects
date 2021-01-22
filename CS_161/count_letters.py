# Author: Ty Vareka
# Date: 2/18/2020
# Description: This program takes a string and determines how many of each letter are within the string.
# if the letter is not present within the string, it is not counted

def count_letters(string):
    """This function will take a string and returns a dictionary of that string where the keys
    are the individual letters within the string.  The values associated with those strings are
    the amount of times they occur within the given string."""
    string = string.upper()
    d = dict()
    for i in string:
        if i >= 'A' and i <= 'Z':
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
    return d

