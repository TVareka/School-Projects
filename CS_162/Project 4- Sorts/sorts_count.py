# Author: Ty Vareka
# Date: 4/20/2020
# Description: Making a comparison between insertion count and bubble count to show comparisons verses exchanges

def insertion_count(a_list):
    """
  Sorts a_list in ascending order
  """
    exchanges = 0
    comparisons = 0
    for index in range(1, len(a_list)):
        value = a_list[index]
        pos = index - 1
        while pos >= 0 and a_list[pos] > value:
            a_list[pos + 1] = a_list[pos]
            pos -= 1
            exchanges += 1
            comparisons += 1
        a_list[pos + 1] = value
        if pos >= 0:
            comparisons += 1
    return (comparisons, exchanges,)


def bubble_count(a_list):
    """
  Sorts a_list in ascending order
  """
    exchanges = 0
    comparisons = 0
    for pass_num in range(len(a_list) - 1):
        for index in range(len(a_list) - 1 - pass_num):
            comparisons += 1
            if a_list[index] > a_list[index + 1]:
                temp = a_list[index]
                exchanges += 1
                a_list[index] = a_list[index + 1]
                a_list[index + 1] = temp
    return (comparisons, exchanges,)


def main():
    '''simple test '''
    list_1 = [0, 8, 4, 12, 50, 3, 64]
    list_2 = [1, 5, 7, 3, 4, 5, 6, 10, 15, 12]
    list_3 = [45, 21, 13, 15, 5, 4, 3, 1, 2, 4, 54, 12, 34, 45, 65, 78]
    list_4 = [2, 4, 6, 3]
    list_5 = [2, 4, 6, 1]
    print(insertion_count(list_1))
    print(insertion_count(list_2))
    print(insertion_count(list_3))
    print(insertion_count(list_4))
    print(insertion_count(list_5))
    list_1 = [0, 8, 4, 12, 50, 3, 64]
    list_2 = [1, 5, 7, 3, 4, 5, 6, 10, 15, 12]
    list_3 = [45, 21, 13, 15, 5, 4, 3, 1, 2, 4, 54, 12, 34, 45, 65, 78]
    list_4 = [2, 4, 6, 3]
    list_5 = [2, 4, 6, 1]
    print(bubble_count(list_1))
    print(bubble_count(list_2))
    print(bubble_count(list_3))
    print(bubble_count(list_4))
    print(bubble_count(list_5))

if __name__ == "__main__":
    main()