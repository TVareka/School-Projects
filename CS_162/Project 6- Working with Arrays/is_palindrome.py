# Author: Ty Vareka
# Date: 5/4/2020
# Description: This program determines if the string used is a palindrome.  It returns True if it is and False if it is
# not.

def rec_is_palindrome(string, first, last):
    '''This recursive function takes the string, 0, and the length of the string - 1 to determine if the string is
    a palindrome.'''
    if first == last:
        return True
    if string[first] != string[last]:
        return False
    if first < last + 1:
        return rec_is_palindrome(string, first + 1, last - 1)
    return True

def is_palindrome(string):
    '''This function allows the user to just put in the string.  This program then determines the length of the string,
    and if the string is 0 characters (in this case it returns True).  It uses these values to then run
    rec_is_palindrome correctly'''
    n = len(string)-1
    if n == 0:
        return True
    return rec_is_palindrome(string, 0, n)

def main():
    '''testing the program with simple parameters'''
    palindrome = 'tacocat'
    print(is_palindrome(palindrome))
    notPalindrome = 'apple'
    print(is_palindrome(notPalindrome))
    capitalPalindrome = 'Tacocat'
    print(is_palindrome(capitalPalindrome))

if __name__ == "__main__":
    main()

