# Author: Ty Vareka
# Date: 4/20/2020
# Description: Creates an insertion sort that sorts a list of strings instead of numbers and is not case sensitive

def string_sort(a_list):
    """Sorts a list of strings in alphabetical order"""
    for index in range(1, len(a_list)):
        value = a_list[index].lower()
        pos = index - 1
        word = a_list[index]
        while pos >= 0 and a_list[pos].lower() > value:
            a_list[pos + 1] = a_list[pos]
            pos -= 1
        a_list[pos + 1] = word

def main():
    list = ['horse', 'Zebra', 'COw', 'bat', 'beaver']
    string_sort(list)
    print(list)

if __name__ == "__main__":
    main()