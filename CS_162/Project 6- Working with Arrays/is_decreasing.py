# Author: Ty Vareka
# Date: 5/4/2020
# Description: This program determines if a list that is input, is decreasing.

def is_decreasing(list, pos=0):
    '''This function determines whether or not the list is decreasing.  If it is, it returns True, and if not, it
    returns false.'''
    if pos == len(list)-1:
        return True
    if list[pos+1] > list[pos]:
        return False
    return is_decreasing(list, pos+1)


def main():
    '''testing the program with simple parameters'''
    notDecreasingList = [10, 8, 6, 4, 2, 1, 4]
    print(is_decreasing(notDecreasingList))
    decreasingList = [12, 11, 10, 8, 4, 2, 1]
    print(is_decreasing(decreasingList))
    increasingList = [10,12]
    print(is_decreasing(increasingList))

if __name__ == "__main__":
    main()
