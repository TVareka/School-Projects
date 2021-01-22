# Author: Ty Vareka
# Date: 5/4/2020
# Description: Puzzle consisting of a row of integers with a zero in the rightmost square.  The goal is to make it to
# the right most square.  This can be done by moving left or right and moving based on the integer landed on.

def rec_row_puzzle(list, current, prev, finish):
    '''This recursive function figures out if is possible to get to the zero integer in the rightmost square.  If it
    is possible, the program returns True and if not, the program returns false.'''
    if list[current] == 0:
        return True
    if finish >= len(list):
        return False
    if current + list[current] > len(list) - 1 and current - list[current] < 0:
        return False
    if current + list[current] > len(list) - 1:
        if current - list[current] == prev:
            return False
        return rec_row_puzzle(list, (current - list[current]), current, finish + 1)
    if current - list[current] < 0:
        if current + list[current] == prev:
            return False
        return rec_row_puzzle(list, current + list[current], current, finish + 1)
    return rec_row_puzzle(list, current - list[current], current, finish + 1) or \
           rec_row_puzzle(list, current + list[current], current, finish + 1)


def row_puzzle(list):
    '''This function allows for a user to just input a list rather than all of the initial values needed for
    rec_row_puzzle to work correctly.'''
    return rec_row_puzzle(list, 0, 0, 0)


def main():
    '''testing the program with simple parameters'''
    aList = [2, 4, 5, 3, 1, 3, 1, 4, 0]
    print(row_puzzle(aList))
    bList = [1, 1, 1, 1, 1, 2, 0]
    print(row_puzzle(bList))



if __name__ == "__main__":
    main()

