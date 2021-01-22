# Author: Ty Vareka
# Date: 4/20/2020
# Description: Creating a binary search function that returns and raises a targetnotfound exception when target
# value is not found

class TargetNotFound(Exception):
    """Target not found in list during binary search function"""
    pass

def bin_except(a_list, target):
    """ Searches a_list for an occurrence of target.  If found, returns the index of its position in the list
    and if not found, returns TargetNotFound exception."""

    first = 0
    last = len(a_list) - 1
    while first <= last:
        middle = (first + last) // 2
        if a_list[middle] == target:
            return middle
        if a_list[middle] > target:
            last = middle - 1
        else:
            first = middle + 1
    raise TargetNotFound


def main():
    '''testing the program with simple parameters'''
    list = [1, 5, 4, 7]
    try:
        print(bin_except(list, 6))
    except TargetNotFound:
        return print('error')

if __name__ == "__main__":
    main()


