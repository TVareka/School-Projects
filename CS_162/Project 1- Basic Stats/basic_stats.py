# Author: Ty Vareka
# Date: 3/30/2020
# Description: This program creates a class 'Person' which has two private data members (age and name).  Then
# a separate function called basic_stats will create a list of the ages from class 'Person' and determine the
# mean median, and mode.

import statistics


class Person:
    """Creates a class called person that takes a name and age for the person"""

    def __init__(self, name, age):
        self._name = name
        self._age = age

    def get_age(self):
        return self._age


def basic_stats(people):
    """This function is going to take the list made from the class 'Person' and then create a list of the ages.  After
    this, the program will determine the mean, median, and mode from that list of ages."""
    age_list = []
    for n in people:
        age_list.append(n.get_age())
    mean = statistics.mean(age_list)
    median = statistics.median(age_list)
    mode = statistics.mode(age_list)
    return (mean, median, mode,)



