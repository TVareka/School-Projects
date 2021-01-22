# Author: Ty Vareka
# Date: 5/18/2020
# Description: This program creates a decorator function and then calls bubble count/insertion count within that
# decorator function.  The decorator allows us to see how long it takes to run either bubble or insertion count.  We
# then have a function that compares those times and plots them on a graph for the user to see.

import time
import random
from matplotlib import pyplot

def sort_timer(func):
    '''This decorator function checks the timer when it starts and when it finishes the function.  It then
    returns the end time minus the start time to determine the total time it took to run the function'''
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        func(*args, **kwargs)
        end_time = time.perf_counter()
        return (end_time - start_time)
    return wrapper

@sort_timer
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

@sort_timer
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

def compare_sorts(func_1, func_2):
    '''This function compares the bubble count and insertion count functions in terms of how long it takes to run.
    It then plots those points on a graph for the user to see'''
    bubble_time = []
    insert_time = []
    for val in range(1000, 10001, 1000):
        list_1 = []
        for i in range(val):
            list_1.append(random.randint(1, 10000))
        list_2 = list(list_1)
        bubble_time.append(func_1(list_1))
        insert_time.append(func_2(list_2))
    x_list = [num for num in range(1000, 10001, 1000)]
    pyplot.plot(x_list, bubble_time, 'ro--', linewidth=2)
    pyplot.plot(x_list, insert_time, 'go--', linewidth=2)
    pyplot.show()









if __name__ == '__main__':
    compare_sorts(bubble_count, insertion_count)
