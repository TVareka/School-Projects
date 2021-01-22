# Author: Ty Vareka
# Date: 5/4/2020
# Description: This program takes a list as its parameter and returns the max value in the list

def array_max(list, max=0, pos=0):
    '''This function takes a list and determines what the max value is in that list.  It then returns that value at the
    end of the list. '''
    if pos == len(list):
        return max
    if list[pos] > max:
        return array_max(list, max=list[pos], pos=pos+1)
    return array_max(list, max, pos+1)


def main():
    '''testing the program with simple parameters'''
    aList = [1, 5, 6, 2, 18, 50, 3, 6, 12, 76, 34, 23, 13]
    print(array_max(aList))

if __name__ == "__main__":
    main()

